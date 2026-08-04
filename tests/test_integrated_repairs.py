from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema
import pytest

from scripts.validate_repo import (
    extract_marked_method_records,
    validate_method_record,
    validate_record_semantics,
)
from scripts.validate_evals import compare_mode_results, validate_frozen_scenarios
from tests.test_method_record_schema import load_schema, valid_record


ROOT = Path(__file__).resolve().parents[1]


def record_ref(record_id: str, version: int) -> dict:
    return {"record_id": record_id, "record_version": version}


def passed_gate_register() -> dict:
    return {
        "transformations": {
            gate: {"status": "passed", "finding": "contract satisfied"}
            for gate in ("IT1", "IT2", "IT3", "IT4")
        },
        "main_gates": {
            gate: {"status": "passed", "finding": "contract satisfied"}
            for gate in ("IG1", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7")
        },
    }


def affected_positions() -> dict:
    return {
        "direct": {
            "status": "identified",
            "positions": ["interviewed workers"],
            "reason": "directly evaluated",
        },
        "indirect": {
            "status": "identified",
            "positions": ["non-interviewed workers"],
            "reason": "team rules may change their work",
        },
        "low_power": {
            "status": "identified",
            "positions": ["temporary workers"],
            "reason": "weaker challenge routes",
        },
        "no_exit": {
            "status": "unknown",
            "positions": [],
            "reason": "exit capacity is unobserved",
        },
    }


def test_root_linear_and_merge_lineage_are_lossless() -> None:
    root = valid_record()
    validate_method_record(root, load_schema())
    assert validate_record_semantics(root) == []

    linear = copy.deepcopy(root)
    linear.update(
        record_id="ariadne:case-001:v2",
        record_version=2,
        lineage_kind="linear",
        parent_record_id=root["record_id"],
        parent_records=[record_ref(root["record_id"], 1)],
        output_ceiling="diagnostic_only",
        ceiling_transition={
            "operation": "raise",
            "inputs": [{**record_ref(root["record_id"], 1), "ceiling": "description_only"}],
            "basis": [{"basis_id": "src-2", "basis_kind": "external_evidence"}],
            "result": "diagnostic_only",
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
    linear["evidence_cutoff"]["included_source_ids"].append("src-2")
    validate_method_record(linear, load_schema())
    assert validate_record_semantics(linear, [root]) == []

    module_only_raise = copy.deepcopy(linear)
    module_only_raise["ceiling_transition"]["basis"] = []
    with pytest.raises(jsonschema.ValidationError):
        validate_method_record(module_only_raise, load_schema())

    undeclared_raise = copy.deepcopy(linear)
    undeclared_raise["ceiling_transition"]["basis"][0]["basis_id"] = "src-not-admitted"
    assert "ceiling raise basis is not admitted: src-not-admitted" in validate_record_semantics(undeclared_raise)

    merge = copy.deepcopy(linear)
    parents = [record_ref(root["record_id"], 1), record_ref(linear["record_id"], 2)]
    merge.update(
        record_id="ariadne:case-001:merge-v3",
        record_version=3,
        lineage_kind="merge",
        parent_record_id=None,
        parent_records=parents,
        output_ceiling="description_only",
        ceiling_transition={
            "operation": "meet",
            "inputs": [
                {**parents[0], "ceiling": "description_only"},
                {**parents[1], "ceiling": "diagnostic_only"},
            ],
            "basis": [],
            "result": "description_only",
        },
        module_runs=[
            {
                "module": "ariadne-audit",
                "status": "completed",
                "input_records": parents,
                "output_record": record_ref("ariadne:case-001:merge-v3", 3),
            }
        ],
        module_payloads=[
            {
                "module": "ariadne-audit",
                "payload": {
                    "gate_register": passed_gate_register(),
                    "contestability": {
                        "owner": {"contact": "review@example.invalid", "status": "reachable"},
                        "deadline": "2026-08-18T00:00:00+08:00",
                        "original_record_retention": True,
                        "downstream_correction_target": "merged claim registry",
                        "rollback_recovery_target": "pre-merge record state",
                        "remedy": "correct downstream records and restore affected state",
                    }
                },
            }
        ],
    )
    validate_method_record(merge, load_schema())
    assert validate_record_semantics(merge, [root, linear]) == []

    merge["parent_records"].reverse()
    assert "merge parent_records must be sorted by record_id then version" in validate_record_semantics(merge)


def test_supported_claim_requires_source_or_declared_rule_support() -> None:
    record = valid_record()
    claim = record["claim_ledger"][0]
    claim["status"] = "supported"
    claim["support_ids"] = []
    claim["support_rule_ids"] = []
    try:
        validate_method_record(record, load_schema())
    except jsonschema.ValidationError:
        pass
    else:
        raise AssertionError("supported claim without source or rule support was accepted")

    claim["support_rule_ids"] = ["RULE:E1"]
    record["rule_registry"] = [
        {"rule_id": "RULE:E1", "rule_type": "inferential", "text": "Declared support rule"}
    ]
    validate_method_record(record, load_schema())
    assert validate_record_semantics(record) == []


def test_typed_module_payloads_preserve_required_handoffs() -> None:
    record = valid_record()
    record["module_payloads"] = [
        {
            "module": "ariadne-human",
            "payload": {
                "observation_position": "independent interviewer",
                "privacy_state": "restricted",
                "allowed_purpose": "bounded team-process diagnosis",
                "affected_positions": affected_positions(),
                "alternative_explanations": ["workload", "reporting selection"],
                "responsible_human_review": {
                    "required": True,
                    "reviewer": "independent HR reviewer",
                    "status": "pending",
                },
            },
        },
        {
            "module": "ariadne-dynamics",
            "payload": {
                "model_version": "branch-model-1",
                "observation_position": "external event log",
                "events": [
                    {
                        "event_id": "EV-1",
                        "fact_status": "externally_reported",
                        "source_ids": ["src-1"],
                        "time_window": "2026-Q2",
                        "observation_time": "2026-08-04T00:00:00+08:00",
                        "affected_actors": ["delivery team"],
                        "affected_circles": ["product workflow"],
                        "channel": "external event log",
                        "direct_change": "the report entered the analysis record",
                        "evidence_state": "report observed; content not independently verified",
                        "disputes": ["event content remains unverified"],
                        "competing_explanations": ["reporting artifact"],
                        "reversibility": "belief update is reversible",
                        "duration": "unknown",
                        "follow_up_observations": ["independent event verification"],
                    }
                ],
            },
        },
    ]
    validate_method_record(record, load_schema())

    broken = copy.deepcopy(record)
    del broken["module_payloads"][0]["payload"]["privacy_state"]
    try:
        validate_method_record(broken, load_schema())
    except jsonschema.ValidationError:
        pass
    else:
        raise AssertionError("human payload without privacy state was accepted")


def test_forward_safety_payloads_are_structurally_complete() -> None:
    record = valid_record()
    record["module_payloads"] = [
        {
            "module": "ariadne-mechanism",
            "payload": {
                "candidates": [
                    {
                        "mechanism_id": "M1",
                        "channel_observation": "queue delay rises before delivery delay",
                        "discriminating_prediction": "queue intervention changes delay first",
                        "reverse_or_falsifier": "delay changes without queue change",
                        "residual_comparison_rule": "retain only if it beats persistence on held-out weeks",
                    },
                    {
                        "mechanism_id": "M2",
                        "channel_observation": "dependency latency precedes delivery delay",
                        "discriminating_prediction": "external latency explains delay when queue is stable",
                        "reverse_or_falsifier": "delay persists after external latency normalizes",
                        "residual_comparison_rule": "compare residual error with M1 under one cutoff",
                    },
                ]
            },
        },
        {
            "module": "ariadne-choice",
            "payload": {
                "facts": ["unknown"],
                "values": ["unknown"],
                "options": ["inaction", "unknown"],
                "jurisdiction": "unknown",
                "authorization": "unknown",
                "stop_conditions": ["unknown"],
                "rollback_plan": "unknown",
            },
        },
        {
            "module": "ariadne-audit",
            "payload": {
                "gate_register": passed_gate_register(),
                "contestability": {
                    "owner": {"contact": "review@example.invalid", "status": "reachable"},
                    "deadline": "2026-08-18T00:00:00+08:00",
                    "original_record_retention": True,
                    "downstream_correction_target": "eligibility output registry",
                    "rollback_recovery_target": "pre-decision eligibility state",
                    "remedy": "restore access and correct propagated records",
                }
            },
        },
        {
            "module": "ariadne-forecast",
            "payload": {
                "preregistration": None,
                "post_hoc_reconstruction": {
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
                        "assessment": "retrospective method audit only",
                        "baseline_comparison": "persistence comparison",
                        "limitations": ["outcome was already knowable"],
                    },
                    "failure_classification": "not_evaluable",
                }
            },
        },
    ]
    validate_method_record(record, load_schema())


def test_completed_typed_module_cannot_drop_its_payload() -> None:
    record = valid_record()
    record["module_runs"] = [
        {
            "module": "ariadne-choice",
            "status": "completed",
            "input_records": [],
            "output_record": record_ref(record["record_id"], 1),
        }
    ]
    validate_method_record(record, load_schema())
    assert "completed ariadne-choice run requires its typed module payload" in validate_record_semantics(record)


def test_all_marked_markdown_method_records_validate() -> None:
    examples: list[tuple[Path, dict]] = []
    for path in (ROOT / "skills").rglob("*.md"):
        for record in extract_marked_method_records(path.read_text(encoding="utf-8")):
            examples.append((path, record))
            validate_method_record(record, load_schema())
            assert validate_record_semantics(record) == [], path
    assert len(examples) >= 4


def test_frozen_chain_and_cluster_fixtures_compare_invariants() -> None:
    fixture = json.loads(
        (ROOT / "evals" / "fixtures" / "frozen-scenarios.json").read_text(encoding="utf-8")
    )
    assert validate_frozen_scenarios(fixture) == []
    for scenario in fixture["scenarios"]:
        if "mode_results" not in scenario:
            continue
        assert compare_mode_results(
            scenario,
            scenario["mode_results"]["sequential"],
            scenario["mode_results"]["clustered"],
        ) == []
