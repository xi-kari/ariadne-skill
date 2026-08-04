from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml
from jsonschema.exceptions import ValidationError

from scripts import validate_repo as repo_validator
from scripts.validate_evals import compare_mode_results, validate_frozen_scenarios
from tests.test_method_record_schema import load_schema, valid_record


ROOT = Path(__file__).resolve().parents[1]


def record_ref(record_id: str, version: int) -> dict:
    return {"record_id": record_id, "record_version": version}


def validate_schema(record: dict) -> None:
    validator = getattr(repo_validator, "validate_method_record", None)
    assert callable(validator), "repository validator must expose one FormatChecker-backed schema entry point"
    validator(record, load_schema())


def semantic_errors(record: dict, parents: list[dict] | None = None) -> list[str]:
    try:
        return repo_validator.validate_record_semantics(record, parents)
    except TypeError:
        pytest.fail("semantic validator must accept exact parent-record context")


def set_completed_module(record: dict, module: str) -> None:
    record["module_runs"] = [
        {
            "module": module,
            "status": "completed",
            "input_records": copy.deepcopy(record["parent_records"]),
            "output_record": record_ref(record["record_id"], record["record_version"]),
        }
    ]


def make_linear_record() -> tuple[dict, dict]:
    root = valid_record()
    child = copy.deepcopy(root)
    child.update(
        record_id="ariadne:case-001:v2",
        record_version=2,
        lineage_kind="linear",
        parent_record_id=root["record_id"],
        parent_records=[record_ref(root["record_id"], 1)],
        ceiling_transition={
            "operation": "preserve",
            "inputs": [{**record_ref(root["record_id"], 1), "ceiling": "description_only"}],
            "basis": [],
            "result": "description_only",
        },
        module_runs=[
            {
                "module": "ariadne-evidence",
                "status": "completed",
                "input_records": [record_ref(root["record_id"], 1)],
                "output_record": record_ref("ariadne:case-001:v2", 2),
            }
        ],
    )
    return root, child


def full_mechanism_payload() -> dict:
    return {
        "module": "ariadne-mechanism",
        "payload": {
            "candidates": [
                {
                    "mechanism_id": "M1",
                    "channel_observation": "queue delay rises before delivery delay",
                    "discriminating_prediction": "queue repair changes delay before other changes",
                    "reverse_or_falsifier": "delivery delay changes while queue delay is stable",
                    "residual_comparison_rule": "retain only if held-out residual beats persistence",
                },
                {
                    "mechanism_id": "M2",
                    "channel_observation": "dependency latency rises before delivery delay",
                    "discriminating_prediction": "dependency recovery changes delay while queue is stable",
                    "reverse_or_falsifier": "delay persists after dependency latency normalizes",
                    "residual_comparison_rule": "compare held-out residual with M1 under one cutoff",
                },
            ]
        },
    }


def full_human_payload() -> dict:
    return {
        "module": "ariadne-human",
        "payload": {
            "observation_position": "independent interviewer",
            "privacy_state": "restricted",
            "allowed_purpose": "bounded team-process diagnosis",
            "affected_positions": {
                "direct": {
                    "status": "identified",
                    "positions": ["interviewed workers"],
                    "reason": "their work is directly evaluated",
                },
                "indirect": {
                    "status": "identified",
                    "positions": ["non-interviewed coworkers"],
                    "reason": "team rules can change their work",
                },
                "low_power": {
                    "status": "identified",
                    "positions": ["temporary workers"],
                    "reason": "they have weaker challenge routes",
                },
                "no_exit": {
                    "status": "unknown",
                    "positions": [],
                    "reason": "actual exit capacity has not been observed",
                },
            },
            "alternative_explanations": ["workload", "reporting selection"],
            "responsible_human_review": {
                "required": True,
                "reviewer": "independent HR reviewer",
                "status": "pending",
            },
        },
    }


def full_dynamics_payload() -> dict:
    return {
        "module": "ariadne-dynamics",
        "payload": {
            "model_version": "branch-model-1",
            "observation_position": "external event log",
            "events": [
                {
                    "event_id": "EV-PLAN-1",
                    "fact_status": "planned",
                    "source_ids": ["src-1"],
                    "time_window": "2026-09-01/2026-09-30",
                    "observation_time": "2026-08-04T00:00:00+08:00",
                    "affected_actors": ["delivery team"],
                    "affected_circles": ["product workflow"],
                    "channel": "published implementation plan",
                    "direct_change": "preparation may begin; execution is not established",
                    "evidence_state": "the plan document is observed",
                    "disputes": ["resource approval is unknown"],
                    "competing_explanations": ["announcement without implementation"],
                    "reversibility": "cancellable before execution",
                    "duration": "unknown until execution",
                    "follow_up_observations": ["execution receipt", "cancellation notice"],
                }
            ],
        },
    }


def full_preregistration(record: dict) -> dict:
    return {
        "forecast_id": "F-001",
        "record_id": record["record_id"],
        "record_version": record["record_version"],
        "model_version": "forecast-model-1",
        "target": "At least three verified voluntary exits by the deadline",
        "horizon": {
            "start": "2026-08-04T00:00:00+08:00",
            "deadline": "2027-02-04T00:00:00+08:00",
        },
        "object_scope": "the frozen 24-person roster",
        "baseline_time": "2026-08-04T00:00:00+08:00",
        "input_cutoff": "2026-08-04T00:00:00+08:00",
        "information_set_ids": ["src-1"],
        "simple_baseline": "matched historical frequency",
        "candidate_mechanisms": ["workload persistence", "appeal repair"],
        "paths": ["threshold met", "threshold not met", "target invalid"],
        "expression": "ordered support",
        "evaluation_rule": "apply the frozen roster, notice, and deadline rules",
        "calibration_plan": {
            "metric": "rank score",
            "reference_class": "all forecasts under forecast-model-1",
            "minimum_cases": 10,
        },
        "early_signals": ["verified workload remains above threshold"],
        "reverse_signals": ["verified workload falls below threshold"],
        "review_triggers": ["roster identity changes"],
        "pause_conditions": ["source registry becomes unavailable"],
        "retirement_conditions": ["baseline wins on the frozen reference class"],
        "failure_semantics": {
            "supported": "target rule met",
            "not_supported": "target rule not met",
            "unresolved": "evidence rule cannot distinguish the result",
            "target_invalid": "the frozen object identity changed",
            "not_evaluable": "observation or timing failure prevents evaluation",
        },
        "result_writeback": {
            "owner": "forecast-registry@example.invalid",
            "due_at": "2027-02-05T00:00:00+08:00",
            "destination": "FORECAST-REGISTRY/F-001",
        },
    }


def full_post_hoc(record: dict) -> dict:
    return {
        "record_id": record["record_id"],
        "record_version": record["record_version"],
        "original_question": "Will target Y occur by date D?",
        "reconstruction_time": "2026-08-04T00:00:00+08:00",
        "target": "Y",
        "deadline": "2026-08-03T00:00:00+08:00",
        "input_cutoff": "2026-07-01T00:00:00+08:00",
        "available_information_ids": ["src-1"],
        "model_version": "model-1",
        "simple_baseline": "persistence",
        "expression": "ordered support",
        "evaluation_rule": "frozen threshold",
        "early_signals": ["signal-a"],
        "reverse_signals": ["signal-b"],
        "actual_outcome": "unknown",
        "hindsight_exclusions": ["src-after-cutoff"],
        "calibration": {
            "metric": "rank score",
            "assessment": "excluded from live calibration because this is retrospective",
            "baseline_comparison": "method-audit comparison only",
            "limitations": ["outcome was already knowable"],
        },
        "failure_classification": "not_evaluable",
    }


def full_audit_payload() -> dict:
    return {
        "module": "ariadne-audit",
        "payload": {
            "gate_register": {
                "transformations": {
                    "IT1": {"status": "failed", "finding": "observable protocol missing"},
                    "IT2": {"status": "not_run", "finding": "stopped after IT1"},
                    "IT3": {"status": "not_run", "finding": "stopped after IT1"},
                    "IT4": {"status": "not_run", "finding": "stopped after IT1"},
                },
                "main_gates": {
                    "IG1": {"status": "failed", "finding": "object boundary mixed"},
                    "IG2": {"status": "not_run", "finding": "stopped after IG1"},
                    "IG3": {"status": "not_run", "finding": "stopped after IG1"},
                    "IG4": {"status": "not_run", "finding": "stopped after IG1"},
                    "IG5": {"status": "not_run", "finding": "stopped after IG1"},
                    "IG6": {"status": "not_run", "finding": "stopped after IG1"},
                    "IG7": {"status": "not_run", "finding": "stopped after IG1"},
                },
            },
            "contestability": {
                "owner": {"contact": "review@example.invalid", "status": "reachable"},
                "deadline": "2026-08-18T00:00:00+08:00",
                "original_record_retention": True,
                "downstream_correction_target": "eligibility output registry",
                "rollback_recovery_target": "pre-decision eligibility state",
                "remedy": "restore access and correct propagated records",
            },
        },
    }


def test_lineage_rejects_version_drift_ghost_inputs_and_missing_parent_context() -> None:
    root, child = make_linear_record()

    wrong_version = copy.deepcopy(child)
    wrong_version["record_version"] = 3
    wrong_version["module_runs"][0]["output_record"]["record_version"] = 3
    assert "linear record_version must equal sole parent version plus one" in semantic_errors(wrong_version)

    ghost_input = copy.deepcopy(child)
    ghost_input["module_runs"][0]["input_records"] = [record_ref("ariadne:ghost:v1", 1)]
    assert "linear module inputs must equal the sole parent record" in semantic_errors(ghost_input)

    wrong_parent_ref = copy.deepcopy(child)
    wrong_parent_ref["parent_records"][0]["record_id"] = "ariadne:ghost:v1"
    assert "unresolved parent record: ariadne:ghost:v1@1" in semantic_errors(wrong_parent_ref, [root])


def test_merge_version_rule_and_exact_audit_parents_are_enforced() -> None:
    root = valid_record()
    left = copy.deepcopy(root)
    left.update(record_id="ariadne:left:v2", record_version=2)
    right = copy.deepcopy(root)
    right.update(record_id="ariadne:right:v3", record_version=3)
    parents = [record_ref(left["record_id"], 2), record_ref(right["record_id"], 3)]
    merge = copy.deepcopy(root)
    merge.update(
        record_id="ariadne:merge:v4",
        record_version=4,
        lineage_kind="merge",
        parent_record_id=None,
        parent_records=parents,
        ceiling_transition={
            "operation": "meet",
            "inputs": [
                {**parents[0], "ceiling": "description_only"},
                {**parents[1], "ceiling": "description_only"},
            ],
            "basis": [],
            "result": "description_only",
        },
        module_runs=[
            {
                "module": "ariadne-audit",
                "status": "completed",
                "input_records": parents,
                "output_record": record_ref("ariadne:merge:v4", 4),
            }
        ],
        module_payloads=[full_audit_payload()],
    )
    assert semantic_errors(merge, [left, right]) == []

    drift = copy.deepcopy(merge)
    drift["record_version"] = 5
    drift["module_runs"][0]["output_record"]["record_version"] = 5
    assert "merge record_version must equal highest parent version plus one" in semantic_errors(drift)

    dropped = copy.deepcopy(merge)
    dropped["module_runs"][0]["input_records"] = parents[:1]
    assert "merge audit inputs must equal all canonical parent records" in semantic_errors(dropped)

    ghost_completed_run = copy.deepcopy(merge)
    ghost_completed_run["module_runs"].append(
        {
            "module": "ariadne-human",
            "status": "completed",
            "input_records": [record_ref("ariadne:ghost:v1", 1)],
            "output_record": record_ref(merge["record_id"], merge["record_version"]),
        }
    )
    ghost_completed_run["module_payloads"].append(full_human_payload())
    assert "merge completed module inputs must equal all canonical parent records" in semantic_errors(
        ghost_completed_run, [left, right]
    )


def test_support_and_ceiling_raise_must_resolve_and_be_new_relative_to_parent() -> None:
    record = valid_record()
    record["claim_ledger"][0].update(
        status="supported",
        support_ids=["ghost-source"],
        support_rule_ids=["RULE:invented"],
    )
    errors = semantic_errors(record)
    assert "supported claim claim-1 has unresolved support_id: ghost-source" in errors
    assert "supported claim claim-1 has unresolved support_rule_id: RULE:invented" in errors

    unresolved_chain = valid_record()
    unresolved_chain["claim_ledger"].append(
        {
            "claim_id": "claim-2",
            "claim_type": "G",
            "text": "A supported conclusion cannot rest only on a candidate claim.",
            "status": "supported",
            "support_ids": ["claim-1"],
            "support_rule_ids": [],
            "counterevidence_ids": [],
        }
    )
    assert "supported claim claim-2 references non-supporting claim: claim-1" in semantic_errors(
        unresolved_chain
    )

    root, child = make_linear_record()
    child.update(output_ceiling="diagnostic_only")
    child["ceiling_transition"] = {
        "operation": "raise",
        "inputs": [{**record_ref(root["record_id"], 1), "ceiling": "description_only"}],
        "basis": [{"basis_id": "src-1", "basis_kind": "external_evidence"}],
        "result": "diagnostic_only",
    }
    assert "ceiling raise basis is not new relative to parents: src-1" in semantic_errors(child, [root])

    forged_parent_ceiling = copy.deepcopy(child)
    forged_parent_ceiling["output_ceiling"] = "requirements_only"
    forged_parent_ceiling["ceiling_transition"] = {
        "operation": "preserve",
        "inputs": [{**record_ref(root["record_id"], 1), "ceiling": "requirements_only"}],
        "basis": [],
        "result": "requirements_only",
    }
    assert (
        "ceiling input does not match resolved parent output_ceiling: ariadne:case-001:v1@1"
        in semantic_errors(forged_parent_ceiling, [root])
    )

    wrong_rule_kind = copy.deepcopy(child)
    wrong_rule_kind["rule_registry"] = [
        {
            "rule_id": "RULE:new-norm",
            "rule_type": "normative",
            "text": "A value premise is not protocol fulfillment.",
        }
    ]
    wrong_rule_kind["ceiling_transition"]["basis"] = [
        {"basis_id": "RULE:new-norm", "basis_kind": "protocol_fulfillment"}
    ]
    assert "ceiling protocol basis must reference a protocol rule: RULE:new-norm" in semantic_errors(
        wrong_rule_kind, [root]
    )

    meet = copy.deepcopy(child)
    meet.update(output_ceiling="description_only")
    meet["ceiling_transition"].update(operation="meet", basis=[], result="description_only")
    with pytest.raises(ValidationError):
        validate_schema(meet)
    assert "linear lineage forbids meet ceiling operation" in semantic_errors(meet)


def test_dynamics_planned_event_requires_the_full_event_contract() -> None:
    record = valid_record()
    record["module_payloads"] = [full_dynamics_payload()]
    validate_schema(record)

    for field in (
        "observation_time",
        "affected_actors",
        "affected_circles",
        "channel",
        "direct_change",
        "evidence_state",
        "disputes",
        "competing_explanations",
        "reversibility",
        "duration",
        "follow_up_observations",
    ):
        broken = copy.deepcopy(record)
        del broken["module_payloads"][0]["payload"]["events"][0][field]
        with pytest.raises(ValidationError):
            validate_schema(broken)

    for field in (
        "source_ids",
        "affected_actors",
        "affected_circles",
        "disputes",
        "competing_explanations",
        "follow_up_observations",
    ):
        empty = copy.deepcopy(record)
        empty["module_payloads"][0]["payload"]["events"][0][field] = []
        with pytest.raises(ValidationError):
            validate_schema(empty)


def test_forecast_preregistration_is_typed_linked_and_exclusive_with_post_hoc() -> None:
    record = valid_record()
    set_completed_module(record, "ariadne-forecast")
    record["module_payloads"] = [
        {
            "module": "ariadne-forecast",
            "payload": {
                "preregistration": full_preregistration(record),
                "post_hoc_reconstruction": None,
            },
        }
    ]
    validate_schema(record)
    assert semantic_errors(record) == []

    drift = copy.deepcopy(record)
    drift["module_payloads"][0]["payload"]["preregistration"]["record_version"] = 999
    assert "forecast preregistration must link the current record_id and record_version" in semantic_errors(drift)

    wrong_chronology = copy.deepcopy(record)
    prereg = wrong_chronology["module_payloads"][0]["payload"]["preregistration"]
    prereg["horizon"]["deadline"] = "2026-08-03T00:00:00+08:00"
    prereg["result_writeback"]["due_at"] = "2026-08-02T00:00:00+08:00"
    assert (
        "forecast preregistration chronology must satisfy baseline <= cutoff <= start <= deadline < writeback"
        in semantic_errors(wrong_chronology)
    )

    both = copy.deepcopy(record)
    both["module_payloads"][0]["payload"]["post_hoc_reconstruction"] = full_post_hoc(record)
    with pytest.raises(ValidationError):
        validate_schema(both)


def test_post_hoc_forecast_requires_calibration_and_failure_classification() -> None:
    record = valid_record()
    record["module_payloads"] = [
        {
            "module": "ariadne-forecast",
            "payload": {
                "preregistration": None,
                "post_hoc_reconstruction": full_post_hoc(record),
            },
        }
    ]
    validate_schema(record)

    for field in ("calibration", "failure_classification"):
        broken = copy.deepcopy(record)
        del broken["module_payloads"][0]["payload"]["post_hoc_reconstruction"][field]
        with pytest.raises(ValidationError):
            validate_schema(broken)


def test_every_frozen_scenario_requires_both_mode_results() -> None:
    fixture = json.loads(
        (ROOT / "evals" / "fixtures" / "frozen-scenarios.json").read_text(encoding="utf-8")
    )
    assert all(set(scenario.get("mode_results", {})) == {"sequential", "clustered"} for scenario in fixture["scenarios"])

    broken = copy.deepcopy(fixture)
    del broken["scenarios"][0]["mode_results"]
    assert any("mode_results" in error for error in validate_frozen_scenarios(broken))

    missing_contract = copy.deepcopy(fixture)
    del missing_contract["scenarios"][0]["mode_contract"]
    assert any("mode_contract" in error for error in validate_frozen_scenarios(missing_contract))


def test_mode_comparator_rejects_version_drift_broken_order_and_matching_orphan() -> None:
    fixture = json.loads(
        (ROOT / "evals" / "fixtures" / "frozen-scenarios.json").read_text(encoding="utf-8")
    )
    scenario = fixture["scenarios"][-1]

    version_drift = copy.deepcopy(scenario["mode_results"]["sequential"])
    version_drift["lineage"]["nodes"][1]["input_records"][0]["record_version"] += 100
    assert compare_mode_results(scenario, version_drift, scenario["mode_results"]["clustered"])

    broken_order = copy.deepcopy(scenario["mode_results"]["sequential"])
    broken_order["lineage"]["nodes"][1]["input_records"] = copy.deepcopy(
        broken_order["lineage"]["nodes"][0]["input_records"]
    )
    assert compare_mode_results(scenario, broken_order, scenario["mode_results"]["clustered"])

    orphan = copy.deepcopy(scenario["mode_results"]["sequential"])
    extra = copy.deepcopy(orphan["lineage"]["nodes"][0])
    extra.update(record_id="ariadne:eval:K02:matching-orphan-v2", record_version=2)
    orphan["lineage"]["nodes"].append(extra)
    assert compare_mode_results(scenario, orphan, scenario["mode_results"]["clustered"])

    self_rewritten = copy.deepcopy(fixture)
    c01 = self_rewritten["scenarios"][0]
    c01["mode_contract"]["sequential_order"][2:4] = [
        "ariadne-mechanism",
        "ariadne-scale",
    ]
    c01["mode_results"]["sequential"]["lineage"]["nodes"][1]["module"] = "ariadne-mechanism"
    c01["mode_results"]["sequential"]["lineage"]["nodes"][2]["module"] = "ariadne-scale"
    assert any("canonical mode contract" in error for error in validate_frozen_scenarios(self_rewritten))

    bool_version = copy.deepcopy(fixture)
    seq_lineage = bool_version["scenarios"][0]["mode_results"]["sequential"]["lineage"]
    seq_lineage["root_records"][0]["record_version"] = True
    seq_lineage["nodes"][0]["input_records"][0]["record_version"] = True
    assert any("record_version must be an integer" in error for error in validate_frozen_scenarios(bool_version))

    float_version = copy.deepcopy(fixture)
    seq_lineage = float_version["scenarios"][0]["mode_results"]["sequential"]["lineage"]
    seq_lineage["nodes"][0]["record_version"] = 2.0
    seq_lineage["nodes"][1]["input_records"][0]["record_version"] = 2.0
    assert any("record_version must be an integer" in error for error in validate_frozen_scenarios(float_version))


def test_f4_candidates_are_individually_complete_and_distinguishable() -> None:
    record = valid_record()
    record["module_payloads"] = [full_mechanism_payload()]
    validate_schema(record)

    duplicate = copy.deepcopy(record)
    duplicate["module_payloads"][0]["payload"]["candidates"][1]["mechanism_id"] = "M1"
    assert "mechanism candidate IDs must be unique" in semantic_errors(duplicate)

    identical = copy.deepcopy(record)
    identical["module_payloads"][0]["payload"]["candidates"][1] = copy.deepcopy(
        identical["module_payloads"][0]["payload"]["candidates"][0]
    )
    identical["module_payloads"][0]["payload"]["candidates"][1]["mechanism_id"] = "M2"
    assert "mechanism candidates must be distinguishable on their required tests" in semantic_errors(identical)

    whitespace_only_difference = copy.deepcopy(record)
    first = whitespace_only_difference["module_payloads"][0]["payload"]["candidates"][0]
    whitespace_only_difference["module_payloads"][0]["payload"]["candidates"][1] = {
        key: ("M2" if key == "mechanism_id" else f"{value} ")
        for key, value in first.items()
    }
    assert "mechanism candidates must be distinguishable on their required tests" in semantic_errors(
        whitespace_only_difference
    )

    for field in (
        "channel_observation",
        "discriminating_prediction",
        "reverse_or_falsifier",
        "residual_comparison_rule",
    ):
        broken = copy.deepcopy(record)
        del broken["module_payloads"][0]["payload"]["candidates"][1][field]
        with pytest.raises(ValidationError):
            validate_schema(broken)


def test_f7_human_payload_requires_four_closed_position_classes() -> None:
    record = valid_record()
    record["module_payloads"] = [full_human_payload()]
    validate_schema(record)

    for position_class in ("direct", "indirect", "low_power", "no_exit"):
        broken = copy.deepcopy(record)
        del broken["module_payloads"][0]["payload"]["affected_positions"][position_class]
        with pytest.raises(ValidationError):
            validate_schema(broken)

    free_text = copy.deepcopy(record)
    free_text["module_payloads"][0]["payload"]["affected_positions"] = "everyone affected"
    with pytest.raises(ValidationError):
        validate_schema(free_text)


def test_f8_first_gate_failure_forces_not_run_and_description_only() -> None:
    record = valid_record()
    set_completed_module(record, "ariadne-audit")
    record["module_payloads"] = [full_audit_payload()]
    validate_schema(record)
    assert semantic_errors(record) == []

    later_pass = copy.deepcopy(record)
    later_pass["module_payloads"][0]["payload"]["gate_register"]["transformations"]["IT2"] = {
        "status": "passed",
        "finding": "improperly continued",
    }
    assert "IT2 must be not_run after IT1 failed" in semantic_errors(later_pass)

    elevated = copy.deepcopy(record)
    elevated["output_ceiling"] = "requirements_only"
    elevated["ceiling_transition"]["result"] = "requirements_only"
    assert "IT1 or IG1 failure requires output_ceiling description_only" in semantic_errors(elevated)

    root, later_failure = make_linear_record()
    later_failure["evidence_cutoff"]["included_source_ids"].append("src-2")
    later_failure["output_ceiling"] = "diagnostic_only"
    later_failure["ceiling_transition"] = {
        "operation": "raise",
        "inputs": [{**record_ref(root["record_id"], 1), "ceiling": "description_only"}],
        "basis": [{"basis_id": "src-2", "basis_kind": "external_evidence"}],
        "result": "diagnostic_only",
    }
    set_completed_module(later_failure, "ariadne-audit")
    payload = full_audit_payload()
    payload["payload"]["gate_register"]["transformations"] = {
        "IT1": {"status": "passed", "finding": "observable protocol exists"},
        "IT2": {"status": "failed", "finding": "evidence strength is unresolved"},
        "IT3": {"status": "not_run", "finding": "stopped after IT2"},
        "IT4": {"status": "not_run", "finding": "stopped after IT2"},
    }
    payload["payload"]["gate_register"]["main_gates"] = {
        gate: {"status": "passed", "finding": "gate passed"}
        for gate in ("IG1", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7")
    }
    later_failure["module_payloads"] = [payload]
    assert "audit gate failure forbids ceiling raise" in semantic_errors(later_failure, [root])


def test_typed_payload_requires_a_matching_completed_module_run() -> None:
    record = valid_record()
    record["module_payloads"] = [full_human_payload()]
    assert "ariadne-human payload requires a matching completed module run" in semantic_errors(record)


def test_rfc3339_format_checker_rejects_invalid_deadlines_everywhere() -> None:
    record = valid_record()
    record["module_payloads"] = [full_audit_payload()]
    record["module_payloads"][0]["payload"]["contestability"]["deadline"] = "not-a-date"
    with pytest.raises(ValidationError):
        validate_schema(record)

    cutoff = valid_record()
    cutoff["evidence_cutoff"]["as_of"] = "2026-08-04"
    with pytest.raises(ValidationError):
        validate_schema(cutoff)

    impossible_leap = valid_record()
    impossible_leap["evidence_cutoff"]["as_of"] = "2026-01-01T00:00:60Z"
    with pytest.raises(ValidationError):
        validate_schema(impossible_leap)

    valid_leap = valid_record()
    valid_leap["evidence_cutoff"]["as_of"] = "2016-12-31T23:59:60Z"
    validate_schema(valid_leap)


def test_source_navigation_rejects_missing_numbering_and_non_proof_boundaries() -> None:
    path = ROOT / "skills" / "ariadne-skill" / "references" / "source-navigation.json"
    assert path.is_file(), "ariadne-skill must directly own Appendix B/D navigation"
    data = json.loads(path.read_text(encoding="utf-8"))
    validate_source = getattr(repo_validator, "validate_source_navigation", None)
    validate_routes = getattr(repo_validator, "validate_reference_routes", None)
    assert callable(validate_source)
    assert callable(validate_routes)
    assert validate_source(data) == []

    main_skill = (ROOT / "skills" / "ariadne-skill" / "SKILL.md").read_text(encoding="utf-8")
    expected_refs = repo_validator.EXPECTED_REFERENCES["ariadne-skill"]
    assert validate_routes("ariadne-skill", main_skill, expected_refs) == []
    without_direct_route = main_skill.replace(
        "(references/source-navigation.json)", "(source-navigation.json)"
    )
    assert validate_routes("ariadne-skill", without_direct_route, expected_refs)

    missing_numbering = copy.deepcopy(data)
    missing_numbering["appendix_b_numbering"].pop()
    assert validate_source(missing_numbering)

    duplicate_numbering = copy.deepcopy(data)
    duplicate_numbering["appendix_b_numbering"].append(
        copy.deepcopy(duplicate_numbering["appendix_b_numbering"][0])
    )
    assert validate_source(duplicate_numbering)

    missing_boundary = copy.deepcopy(data)
    missing_boundary["appendix_d"]["cross_scale_proof_heuristic"]["non_proof_boundaries"].pop()
    assert validate_source(missing_boundary)

    content_free_d4 = copy.deepcopy(data)
    content_free_d4["appendix_d"]["dual_text_difference"]["retained_differences"] = ["x", "y"]
    content_free_d4["appendix_d"]["dual_text_difference"]["prohibited_substitutions"] = ["x", "y"]
    assert validate_source(content_free_d4)

    content_free_d5 = copy.deepcopy(data)
    content_free_d5["appendix_d"]["cross_scale_proof_heuristic"]["applicability"] = "x"
    assert validate_source(content_free_d5)


def test_stage_order_and_distribution_metadata_fail_closed() -> None:
    extract_status = getattr(repo_validator, "extract_stage_status", None)
    validate_status = getattr(repo_validator, "validate_stage_status", None)
    validate_metadata = getattr(repo_validator, "validate_skill_metadata", None)
    assert callable(extract_status) and callable(validate_status) and callable(validate_metadata)

    plan_status = extract_status(
        (ROOT / "docs" / "superpowers" / "plans" / "2026-08-03-ariadne-skill-implementation.md").read_text(encoding="utf-8")
    )
    readme_status = extract_status((ROOT / "README.md").read_text(encoding="utf-8"))
    assert plan_status == readme_status
    assert validate_status(plan_status) == []

    invalid_order = copy.deepcopy(plan_status)
    invalid_order["WHOLE_SUITE_CONTENT_COMPLETE"] = "pending"
    invalid_order["INTEGRATED_REVIEW"] = "complete"
    assert validate_status(invalid_order)

    metadata = yaml.safe_load(
        (ROOT / "skills" / "ariadne-skill" / "agents" / "openai.yaml").read_text(encoding="utf-8")
    )
    metadata["policy"]["allow_implicit_invocation"] = False
    assert validate_metadata("ariadne-skill", metadata)
