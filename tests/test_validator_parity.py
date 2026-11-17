"""Installed records must enforce the repository's payload integrity checks."""
from __future__ import annotations

import copy
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from scripts import validate_repo
from tests.test_final_repair_contracts import (
    full_dynamics_payload,
    full_mechanism_payload,
    full_post_hoc,
    full_preregistration,
    set_completed_module,
)
from tests.test_method_record_schema import load_schema, valid_record
from tests.test_v21_methodology import design_candidate, record_v21, reopening


@pytest.fixture(scope="module")
def installed_validator():
    path = (
        Path(__file__).resolve().parents[1]
        / "skills/ariadne-skill/scripts/validate_record.py"
    )
    spec = importlib.util.spec_from_file_location("installed_parity_validator", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def payload_record(kind: str) -> dict:
    record = valid_record()
    if kind == "mechanism":
        payload = full_mechanism_payload()
    elif kind == "dynamics":
        payload = full_dynamics_payload()
    else:
        payload = {
            "module": "ariadne-forecast",
            "payload": {
                "preregistration": full_preregistration(record) if kind == "preregistration" else None,
                "post_hoc_reconstruction": full_post_hoc(record) if kind == "post_hoc_reconstruction" else None,
            },
        }
    set_completed_module(record, payload["module"])
    record["module_payloads"] = [payload]
    return record


def assert_semantic_rejection(installed, original: dict, broken: dict, expected: str) -> None:
    schema = load_schema()
    # Every mutation remains schema-valid: rejection must come from the
    # semantic contract, not an unrelated missing field or malformed fixture.
    for record in (original, broken):
        validate_repo.validate_method_record(record, schema)
        assert installed.schema_errors(record, schema)[0] == []
    assert validate_repo.validate_record_semantics(original) == []
    assert installed.semantic_errors(original, None) == ([], [])
    assert expected in validate_repo.validate_record_semantics(broken)
    findings, skipped = installed.semantic_errors(broken, None)
    assert skipped == []
    assert expected in findings


def test_duplicate_mechanism_identifiers_are_rejected_by_both_validators(installed_validator) -> None:
    original = payload_record("mechanism")
    broken = copy.deepcopy(original)
    candidates = broken["module_payloads"][0]["payload"]["candidates"]
    candidates[1]["mechanism_id"] = candidates[0]["mechanism_id"]
    assert_semantic_rejection(
        installed_validator, original, broken, "mechanism candidate IDs must be unique"
    )


def test_renamed_mechanisms_with_the_same_tests_are_rejected_by_both_validators(installed_validator) -> None:
    original = payload_record("mechanism")
    broken = copy.deepcopy(original)
    candidates = broken["module_payloads"][0]["payload"]["candidates"]
    for field in (
        "channel_observation",
        "discriminating_prediction",
        "reverse_or_falsifier",
        "residual_comparison_rule",
    ):
        candidates[1][field] = "  " + candidates[0][field].upper() + "  "
    assert_semantic_rejection(
        installed_validator,
        original,
        broken,
        "mechanism candidates must be distinguishable on their required tests",
    )


def test_unadmitted_event_sources_are_rejected_by_both_validators(installed_validator) -> None:
    original = payload_record("dynamics")
    broken = copy.deepcopy(original)
    event = broken["module_payloads"][0]["payload"]["events"][0]
    event["source_ids"] = ["unadmitted-source"]
    assert_semantic_rejection(
        installed_validator,
        original,
        broken,
        "dynamics event EV-PLAN-1 has unresolved source_id: unadmitted-source",
    )


@pytest.mark.parametrize("kind", ["preregistration", "post_hoc_reconstruction"])
@pytest.mark.parametrize("field,value", [("record_id", "ariadne:another:v1"), ("record_version", 99)])
def test_forecast_record_links_are_checked_by_both_validators(installed_validator, kind, field, value) -> None:
    original = payload_record(kind)
    broken = copy.deepcopy(original)
    broken["module_payloads"][0]["payload"][kind][field] = value
    label = "preregistration" if kind == "preregistration" else "post-hoc reconstruction"
    assert_semantic_rejection(
        installed_validator,
        original,
        broken,
        f"forecast {label} must link the current record_id and record_version",
    )


@pytest.mark.parametrize(
    "path,value",
    [
        (("baseline_time",), "2026-08-05T00:00:00+08:00"),
        (("input_cutoff",), "2026-08-05T00:00:00+08:00"),
        (("horizon", "start"), "2027-02-05T00:00:00+08:00"),
        (("result_writeback", "due_at"), "2027-02-04T00:00:00+08:00"),
    ],
    ids=["baseline-after-cutoff", "cutoff-after-start", "start-after-deadline", "writeback-at-deadline"],
)
def test_each_forecast_chronology_boundary_is_checked_by_both_validators(installed_validator, path, value) -> None:
    original = payload_record("preregistration")
    broken = copy.deepcopy(original)
    target = broken["module_payloads"][0]["payload"]["preregistration"]
    for field in path[:-1]:
        target = target[field]
    target[path[-1]] = value
    assert_semantic_rejection(
        installed_validator,
        original,
        broken,
        "forecast preregistration chronology must satisfy baseline <= cutoff <= start <= deadline < writeback",
    )


@pytest.mark.parametrize(
    "field,factory,changed_field,expected",
    [
        ("problem_reopenings", reopening, "reason", "problem reopening IDs must be unique"),
        ("design_candidates", design_candidate, "proposal", "design candidate IDs must be unique"),
    ],
)
def test_version_21_record_identifiers_are_checked_by_both_validators(
    installed_validator, field, factory, changed_field, expected
) -> None:
    original = record_v21()
    original["request_type"] = "synthesis_design"
    original[field] = [factory()]
    broken = copy.deepcopy(original)
    duplicate = factory()
    duplicate[changed_field] += " Additional detail."
    broken[field].append(duplicate)
    assert_semantic_rejection(installed_validator, original, broken, expected)


def test_reopening_claim_links_are_checked_by_both_validators(installed_validator) -> None:
    original = record_v21()
    original["problem_reopenings"] = [reopening()]
    broken = copy.deepcopy(original)
    broken["problem_reopenings"][0]["affected_claim_ids"] = ["absent-claim"]
    assert_semantic_rejection(
        installed_validator,
        original,
        broken,
        "problem reopening reopen-1 has unresolved affected_claim_id: absent-claim",
    )


def test_duplicate_rule_identifiers_are_rejected_by_both_validators(installed_validator) -> None:
    original = valid_record()
    original["rule_registry"] = [
        {"rule_id": "RULE:shared", "rule_type": "protocol", "text": "Require an evidence check."}
    ]
    broken = copy.deepcopy(original)
    broken["rule_registry"].append(
        {"rule_id": "RULE:shared", "rule_type": "normative", "text": "A conflicting normative premise."}
    )
    assert_semantic_rejection(
        installed_validator, original, broken, "rule registry IDs must be unique"
    )


@pytest.mark.parametrize(
    "timestamp,valid",
    [
        ("not-a-date", False),
        ("2026-11-17T00:00:00", False),
        ("2026-02-30T00:00:00Z", False),
        ("2026-11-17T00:00:00Z", True),
        ("2026-11-17t00:00:00z", True),
        ("2026-11-17T08:00:00+08:00", True),
        ("2026-06-30T23:59:60Z", True),
        ("2026-11-17T23:59:60Z", False),
    ],
)
def test_datetime_formats_are_checked_consistently(installed_validator, timestamp, valid) -> None:
    record = valid_record()
    record["evidence_cutoff"]["as_of"] = timestamp
    schema = load_schema()
    root_findings = list(validate_repo.method_record_validator(schema).iter_errors(record))
    installed_findings, mode = installed_validator.schema_errors(record, schema)
    assert mode == "full JSON Schema (jsonschema)"
    assert (not root_findings) is valid
    assert (not installed_findings) is valid


@pytest.mark.parametrize("field,value", [("problem_reopenings", None), ("design_candidates", [None])])
def test_cli_reports_invalid_extensions_without_entering_semantics(
    installed_validator, tmp_path, capsys, monkeypatch, field, value
) -> None:
    record = record_v21()
    record["request_type"] = "synthesis_design"
    record[field] = value
    path = tmp_path / "invalid-record.json"
    path.write_text(json.dumps(record), encoding="utf-8")

    def should_not_run(*args, **kwargs):
        pytest.fail("semantic validation must not receive a structurally invalid record")

    monkeypatch.setattr(installed_validator, "semantic_errors", should_not_run)
    assert installed_validator.main([str(path)]) == 1
    output = capsys.readouterr().out
    assert "FAIL:" in output
    assert f"schema: {field}" in output
    assert "PASS:" not in output


@pytest.mark.parametrize("zone", ["Z", "z"])
def test_forecast_utc_designators_work_on_supported_python_versions(installed_validator, zone) -> None:
    record = payload_record("preregistration")
    preregistration = record["module_payloads"][0]["payload"]["preregistration"]
    for container, key in (
        (preregistration, "baseline_time"),
        (preregistration, "input_cutoff"),
        (preregistration["horizon"], "start"),
        (preregistration["horizon"], "deadline"),
        (preregistration["result_writeback"], "due_at"),
    ):
        instant = datetime.fromisoformat(container[key]).astimezone(timezone.utc)
        container[key] = instant.isoformat().removesuffix("+00:00") + zone
    schema = load_schema()
    validate_repo.validate_method_record(record, schema)
    assert installed_validator.schema_errors(record, schema)[0] == []
    assert validate_repo.validate_record_semantics(record) == []
    assert installed_validator.semantic_errors(record, None) == ([], [])
