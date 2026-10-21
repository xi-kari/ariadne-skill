"""Record schema 2.0 contracts: task profiles, transform kinds, per-proposition
downgrade, structured choices with analytic recommendations, and the
strong-judgment register. Each semantic rule is checked against the repository
validator and the bundled standalone validator so the two cannot drift."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

import jsonschema
import pytest

from scripts import validate_repo as repo_validator
from tests.test_method_record_schema import load_schema, valid_record


ROOT = Path(__file__).resolve().parents[1]
BUNDLED = ROOT / "skills" / "ariadne-skill" / "scripts" / "validate_record.py"


def _bundled():
    spec = importlib.util.spec_from_file_location("bundled_validate_record_v2", BUNDLED)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUNDLED_MODULE = _bundled()


def repo_errors(record: dict) -> list[str]:
    return repo_validator.validate_record_semantics(record, None)


def bundled_errors(record: dict) -> list[str]:
    errors, _skipped = BUNDLED_MODULE.semantic_errors(record, None)
    return errors


BOTH = pytest.mark.parametrize("errors_of", [repo_errors, bundled_errors], ids=["repo", "bundled"])


def contains(errors: list[str], fragment: str) -> bool:
    return any(fragment in error for error in errors)


def schema_valid(record: dict) -> None:
    repo_validator.validate_method_record(record, load_schema())


def test_bundled_schema_copy_is_byte_identical() -> None:
    canonical = (ROOT / "schemas" / "method-record.schema.json").read_bytes()
    bundled = (ROOT / "skills" / "ariadne-skill" / "references" / "method-record.schema.json").read_bytes()
    assert canonical == bundled
    assert json.loads(canonical)["properties"]["schema_version"]["const"] == "2.0"


def test_task_profile_is_required_and_closed() -> None:
    record = valid_record()
    schema_valid(record)
    missing = copy.deepcopy(record)
    del missing["object_contract"]["task_profile"]
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(missing)
    partial = copy.deepcopy(record)
    del partial["object_contract"]["task_profile"]["allowed_operations"]
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(partial)
    extra = copy.deepcopy(record)
    extra["object_contract"]["task_profile"]["authority"] = "granted"
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(extra)


def test_formal_claims_are_a_registered_role() -> None:
    record = valid_record()
    record["claim_ledger"].append(
        {
            "claim_id": "F-recovery",
            "claim_type": "F",
            "text": "Within the stated model, the mean cannot recover local overload for every state.",
            "status": "candidate",
            "support_ids": [],
            "support_rule_ids": [],
            "counterevidence_ids": [],
        }
    )
    schema_valid(record)


@BOTH
def test_transform_kind_none_pairs_only_with_not_needed(errors_of) -> None:
    record = valid_record()
    assert errors_of(record) == []
    none_but_incomplete = copy.deepcopy(record)
    none_but_incomplete["scale_scope"]["transform_kind"] = "none"
    assert errors_of(none_but_incomplete)
    not_needed_but_scale = copy.deepcopy(record)
    not_needed_but_scale["scale_scope"]["transform_status"] = "not_needed"
    assert errors_of(not_needed_but_scale)
    consistent = copy.deepcopy(record)
    consistent["scale_scope"].update(transform_kind="none", transform_status="not_needed")
    assert errors_of(consistent) == []


def dependent_record() -> dict:
    record = valid_record()
    record["claim_ledger"] = [
        {
            "claim_id": "E-observed",
            "claim_type": "E",
            "text": "Weekly delay rose after the handoff change.",
            "status": "observed",
            "support_ids": ["src-1"],
            "support_rule_ids": [],
            "counterevidence_ids": [],
        },
        {
            "claim_id": "G-cause",
            "claim_type": "G",
            "text": "The handoff change caused the delay.",
            "status": "candidate",
            "support_ids": ["src-1"],
            "support_rule_ids": [],
            "counterevidence_ids": [],
            "depends_on": ["E-observed"],
        },
    ]
    return record


@BOTH
def test_dependencies_must_point_to_earlier_claims(errors_of) -> None:
    record = dependent_record()
    assert errors_of(record) == []
    forward = copy.deepcopy(record)
    forward["claim_ledger"][0]["depends_on"] = ["G-cause"]
    assert errors_of(forward)
    ghost = copy.deepcopy(record)
    ghost["claim_ledger"][1]["depends_on"] = ["E-missing"]
    assert errors_of(ghost)


@BOTH
def test_claim_resting_on_a_failed_dependency_cannot_be_supported(errors_of) -> None:
    record = dependent_record()
    record["claim_ledger"][0]["status"] = "contradicted"
    record["claim_ledger"][1]["status"] = "supported"
    assert errors_of(record)
    record["claim_ledger"][1]["status"] = "unresolved"
    assert errors_of(record) == []


@BOTH
def test_claim_ceiling_never_exceeds_dependency_or_record(errors_of) -> None:
    record = dependent_record()
    record["claim_ledger"][1]["ceiling"] = "diagnostic_only"
    assert errors_of(record)
    record["claim_ledger"][1]["ceiling"] = "description_only"
    assert errors_of(record) == []
    record["output_ceiling"] = "description_only"
    record["claim_ledger"][0]["ceiling"] = "description_only"
    record["claim_ledger"][1]["ceiling"] = "description_only"
    assert errors_of(record) == []


def choice_record(ceiling: str = "description_only") -> dict:
    record = valid_record()
    record["request_type"] = "finite_choice"
    record["output_ceiling"] = ceiling
    record["claim_ledger"].append(
        {
            "claim_id": "N-protect",
            "claim_type": "N",
            "text": "Protection for low-power positions must not degrade.",
            "status": "candidate",
            "support_ids": [],
            "support_rule_ids": [],
            "counterevidence_ids": [],
        }
    )
    record["module_runs"] = [
        {
            "module": "ariadne-choice",
            "status": "completed",
            "input_records": [],
            "output_record": {"record_id": record["record_id"], "record_version": 1},
        }
    ]
    record["module_payloads"] = [
        {
            "module": "ariadne-choice",
            "payload": {
                "facts": ["Weekly delay rose after the handoff change"],
                "values": ["Protection for low-power positions must not degrade"],
                "options": [
                    {"option_id": "OPT-TRIAL", "kind": "probing_action", "description": "eight-week reversible pilot"},
                    {"option_id": "OPT-STATUS", "kind": "maintain_status_quo", "description": "keep current rules"},
                    {"option_id": "OPT-NONE", "kind": "no_action", "description": "no new action"},
                ],
                "jurisdiction": "unknown",
                "authorization": "unknown",
                "stop_conditions": ["protection floor fails"],
                "rollback_plan": "restore the pre-trial state",
                "analytic_recommendation": None,
            },
        }
    ]
    return record


def recommendation(option_id: str = "OPT-TRIAL", premise: str = "N-protect") -> dict:
    return {
        "option_id": option_id,
        "normative_premise_ids": [premise],
        "reasons": ["narrowest reversible step"],
        "costs": ["coordination load on two members"],
        "objections": "immediate change would relieve overload sooner",
        "change_conditions": ["switch if verified hours keep rising"],
        "adoption_status": "deliberation_only",
    }


@BOTH
def test_choice_options_need_exactly_one_no_action(errors_of) -> None:
    record = choice_record()
    schema_valid(record)
    assert errors_of(record) == []
    options = record["module_payloads"][0]["payload"]["options"]
    without = copy.deepcopy(record)
    without["module_payloads"][0]["payload"]["options"] = [o for o in options if o["kind"] != "no_action"]
    assert contains(errors_of(without), "no_action")
    doubled = copy.deepcopy(record)
    doubled["module_payloads"][0]["payload"]["options"].append(
        {"option_id": "OPT-NONE-2", "kind": "no_action", "description": "duplicate baseline"}
    )
    assert contains(errors_of(doubled), "no_action")
    duplicate_id = copy.deepcopy(record)
    duplicate_id["module_payloads"][0]["payload"]["options"][1]["option_id"] = "OPT-TRIAL"
    assert contains(errors_of(duplicate_id), "unique")


def test_choice_options_must_be_structured() -> None:
    record = choice_record()
    record["module_payloads"][0]["payload"]["options"] = ["inaction", "pilot"]
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(record)
    record = choice_record()
    del record["module_payloads"][0]["payload"]["analytic_recommendation"]
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(record)


@BOTH
def test_analytic_recommendation_requires_requirements_only(errors_of) -> None:
    record = choice_record("description_only")
    record["module_payloads"][0]["payload"]["analytic_recommendation"] = recommendation()
    schema_valid(record)
    assert contains(errors_of(record), "requirements_only")


@BOTH
def test_analytic_recommendation_must_name_a_registered_option_and_premise(errors_of) -> None:
    record = choice_record("requirements_only")
    record["module_payloads"][0]["payload"]["analytic_recommendation"] = recommendation()
    findings = [f for f in errors_of(record) if "recommendation" in f]
    assert findings == []
    ghost_option = copy.deepcopy(record)
    ghost_option["module_payloads"][0]["payload"]["analytic_recommendation"]["option_id"] = "OPT-GHOST"
    assert contains(errors_of(ghost_option), "registered option_id")
    ghost_premise = copy.deepcopy(record)
    ghost_premise["module_payloads"][0]["payload"]["analytic_recommendation"]["normative_premise_ids"] = ["G-cause"]
    assert contains(errors_of(ghost_premise), "N claim or normative rule")
    rule_premise = copy.deepcopy(record)
    rule_premise["rule_registry"] = [
        {"rule_id": "RULE:protect", "rule_type": "normative", "text": "Protection must not degrade."}
    ]
    rule_premise["module_payloads"][0]["payload"]["analytic_recommendation"]["normative_premise_ids"] = ["RULE:protect"]
    assert not contains(errors_of(rule_premise), "N claim or normative rule")


def test_analytic_recommendation_is_deliberation_only() -> None:
    record = choice_record("requirements_only")
    rec = recommendation()
    rec["adoption_status"] = "authorized"
    record["module_payloads"][0]["payload"]["analytic_recommendation"] = rec
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(record)


def audit_record(ig6: str, strong_status: str, sj_status: str) -> dict:
    record = valid_record()
    record["request_type"] = "governance_review"
    record["module_runs"] = [
        {
            "module": "ariadne-audit",
            "status": "completed",
            "input_records": [],
            "output_record": {"record_id": record["record_id"], "record_version": 1},
        }
    ]
    passed = {"status": "passed", "finding": "contract satisfied"}
    main = {gate: dict(passed) for gate in ("IG1", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7")}
    main["IG6"] = {"status": ig6, "finding": "strong-judgment check"}
    record["module_payloads"] = [
        {
            "module": "ariadne-audit",
            "payload": {
                "gate_register": {
                    "transformations": {gate: dict(passed) for gate in ("IT1", "IT2", "IT3", "IT4")},
                    "main_gates": main,
                },
                "strong_judgment": {
                    "status": strong_status,
                    "reason": "decided by actual and foreseeable use",
                    "components": {
                        f"SJ{index}": {"status": sj_status, "finding": "item check"} for index in range(1, 9)
                    },
                },
                "contestability": {
                    "owner": {"contact": "review@example.invalid", "status": "reachable"},
                    "deadline": "2026-08-18T00:00:00+08:00",
                    "original_record_retention": True,
                    "downstream_correction_target": "derived records",
                    "rollback_recovery_target": "last verified state",
                    "remedy": "correct propagated records",
                },
            },
        }
    ]
    return record


@BOTH
def test_strong_judgment_register_matches_ig6(errors_of) -> None:
    passed = audit_record("passed", "triggered", "passed")
    schema_valid(passed)
    assert not contains(errors_of(passed), "SJ")
    not_applicable = audit_record("not_applicable", "not_triggered", "not_applicable")
    assert not contains(errors_of(not_applicable), "strong-judgment")
    assert contains(errors_of(audit_record("passed", "not_triggered", "not_applicable")), "triggered")
    failing_item = audit_record("passed", "triggered", "passed")
    failing_item["module_payloads"][0]["payload"]["strong_judgment"]["components"]["SJ4"]["status"] = "failed"
    assert contains(errors_of(failing_item), "SJ4")
    assert contains(errors_of(audit_record("not_applicable", "triggered", "passed")), "not_triggered")
    assert contains(errors_of(audit_record("not_applicable", "not_triggered", "passed")), "not_applicable")


def test_audit_payload_requires_the_strong_judgment_register() -> None:
    record = audit_record("passed", "triggered", "passed")
    del record["module_payloads"][0]["payload"]["strong_judgment"]
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(record)


def test_mechanism_candidates_declare_a_temporal_route() -> None:
    record = valid_record()
    record["module_runs"] = [
        {
            "module": "ariadne-mechanism",
            "status": "completed",
            "input_records": [],
            "output_record": {"record_id": record["record_id"], "record_version": 1},
        }
    ]
    candidate = {
        "mechanism_id": "M1",
        "temporal_route": "carried_history",
        "channel_observation": "a",
        "discriminating_prediction": "b",
        "reverse_or_falsifier": "c",
        "residual_comparison_rule": "d",
    }
    second = dict(candidate, mechanism_id="M2", temporal_route="historical_increment", channel_observation="e")
    record["module_payloads"] = [{"module": "ariadne-mechanism", "payload": {"candidates": [candidate, second]}}]
    schema_valid(record)
    broken = copy.deepcopy(record)
    del broken["module_payloads"][0]["payload"]["candidates"][0]["temporal_route"]
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(broken)
    invented = copy.deepcopy(record)
    invented["module_payloads"][0]["payload"]["candidates"][0]["temporal_route"] = "destiny"
    with pytest.raises(jsonschema.ValidationError):
        schema_valid(invented)


def test_human_variable_cards_carry_low_tier_routes_and_new_source() -> None:
    cards = json.loads(
        (ROOT / "skills" / "ariadne-human" / "references" / "human-variable-cards.json").read_text(encoding="utf-8")
    )
    assert cards["source_sha256"] == "18a7cc167faa3eda68a04b21313f833be6583abf1a2a47523a246a5f8a7eaee6"
    for card in cards["human_variables"]:
        routes = card["conditional_support_routes"]
        assert "-R0-" in routes[0]["route_id"], card["id"]
        assert routes[0]["additional_inferential_requires"] == [], card["id"]
    assert set(cards["shared_action_boundary"]["per_variable_outputs"]) == {
        f"HV{index:02d}" for index in range(1, 12)
    }


def test_domain_atlas_covers_all_thirty_two_domains() -> None:
    atlas = (ROOT / "skills" / "ariadne-framing" / "references" / "domain-atlas.md").read_text(encoding="utf-8")
    for index in range(1, 33):
        assert f"### D.{index:02d} " in atlas


def test_formal_propositions_are_owned_by_scale() -> None:
    text = (ROOT / "skills" / "ariadne-scale" / "references" / "representation-and-closure.md").read_text(
        encoding="utf-8"
    )
    for code in ("F1", "F2", "F3", "F4", "F5", "F6"):
        assert f"**{code}.**" in text, code
