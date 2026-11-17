"""Versioned records preserve inquiry history without manufacturing evidence."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

import jsonschema
import pytest

from scripts import validate_repo
from tests.test_final_repair_contracts import (
    full_human_payload,
    full_mechanism_payload,
    full_preregistration,
    set_completed_module,
)
from tests.test_method_record_schema import load_schema, valid_record


def validate_schema(record: dict) -> None:
    validate_repo.validate_method_record(record, load_schema())


def record_v21() -> dict:
    record = valid_record()
    record["schema_version"] = "2.1"
    return record


def competition_search() -> dict:
    return {
        "search_scope": "Known queue and dependency observations within the frozen cutoff.",
        "reason_no_alternative": "No additional reasonable mechanism was found in that material.",
        "failure_conditions": "Reopen if delay changes without the candidate channel changing.",
    }


def reopening() -> dict:
    return {
        "reopening_id": "reopen-1",
        "original_question": "Which handoff causes delivery delay?",
        "proposed_question": "Which allocation rule creates deadline conflicts?",
        "proposer": "Affected delivery team",
        "reason": "The original frame treated allocation rules as fixed.",
        "disposition": "accepted",
        "disposition_reason": "The omitted constraint can change the remedy comparison.",
        "relationship": "parallel",
        "affected_claim_ids": ["claim-1"],
        "preserved_results": ["The observed delivery delay remains established."],
    }


def design_candidate() -> dict:
    return {
        "candidate_id": "design-1",
        "starting_points": ["One team has conflicting deadlines."],
        "derivation": "Move one review window while preserving the stated delivery target.",
        "proposal": "A staggered review schedule.",
        "assumptions": ["The review deadline is adjustable by its owner."],
        "checks": ["Check joint staffing capacity and review coverage."],
        "failure_conditions": "Reject if the moved window misses an external obligation.",
        "status": "checked",
        "evidence_status": "candidate",
    }


@pytest.mark.parametrize("version", ["2.0", "2.1"])
def test_existing_minimum_record_remains_valid(version: str) -> None:
    record = valid_record()
    record["schema_version"] = version
    validate_schema(record)
    assert validate_repo.validate_record_semantics(record) == []


@pytest.mark.parametrize("kind,count", [("mechanism", 1), ("human", 0), ("human", 1)])
def test_small_candidate_set_requires_a_recorded_search(kind: str, count: int) -> None:
    record = record_v21()
    payload = full_mechanism_payload() if kind == "mechanism" else full_human_payload()
    field = "candidates" if kind == "mechanism" else "alternative_explanations"
    payload["payload"][field] = payload["payload"][field][:count]
    record["module_payloads"] = [payload]
    set_completed_module(record, payload["module"])
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(record)
    payload["payload"]["competition_search"] = competition_search()
    validate_schema(record)
    assert validate_repo.validate_record_semantics(record) == []
    for key in competition_search():
        broken = copy.deepcopy(record)
        broken["module_payloads"][0]["payload"]["competition_search"][key] = ""
        with pytest.raises(jsonschema.ValidationError):
            validate_schema(broken)
    record["schema_version"] = "2.0"
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(record)


@pytest.mark.parametrize("field", ["problem_reopenings", "design_candidates"])
def test_new_top_level_fields_require_version_21_even_when_empty(field: str) -> None:
    record = record_v21()
    record["request_type"] = "synthesis_design"
    record[field] = []
    validate_schema(record)
    record["schema_version"] = "2.0"
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(record)


def test_reopening_records_disposition_and_preserves_existing_claims() -> None:
    record = record_v21()
    record["problem_reopenings"] = [reopening()]
    validate_schema(record)
    assert validate_repo.validate_record_semantics(record) == []
    broken = copy.deepcopy(record)
    del broken["problem_reopenings"][0]["disposition_reason"]
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(broken)
    record["problem_reopenings"][0]["affected_claim_ids"] = ["invented-claim"]
    validate_schema(record)
    assert any("unresolved affected_claim_id: invented-claim" in error
               for error in validate_repo.validate_record_semantics(record))


@pytest.mark.parametrize("field,id_field,factory", [
    ("problem_reopenings", "reopening_id", reopening),
    ("design_candidates", "candidate_id", design_candidate),
])
def test_duplicate_new_record_identifiers_are_rejected(field: str, id_field: str, factory) -> None:
    record = record_v21()
    record["request_type"] = "synthesis_design"
    first = factory()
    second = factory()
    # Different content prevents uniqueItems from masking identifier checks.
    second["reason" if field == "problem_reopenings" else "proposal"] += " Additional detail."
    assert first[id_field] == second[id_field]
    record[field] = [first, second]
    validate_schema(record)
    assert any("IDs must be unique" in error
               for error in validate_repo.validate_record_semantics(record))


def test_checked_design_remains_candidate_and_is_limited_to_synthesis() -> None:
    record = record_v21()
    record["request_type"] = "synthesis_design"
    record["design_candidates"] = [design_candidate()]
    validate_schema(record)
    assert validate_repo.validate_record_semantics(record) == []
    record["design_candidates"][0]["evidence_status"] = "supported"
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(record)
    record["design_candidates"][0]["evidence_status"] = "candidate"
    record["request_type"] = "diagnosis"
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(record)


def test_empty_design_checks_and_new_unregistered_fields_are_rejected() -> None:
    record = record_v21()
    record["request_type"] = "synthesis_design"
    record["design_candidates"] = [design_candidate()]
    record["design_candidates"][0]["checks"] = []
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(record)
    record["design_candidates"][0] = design_candidate()
    record["design_candidates"][0]["can_authorize"] = True
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(record)


def test_reviewable_v21_fixture_contains_reopening_and_candidate_lineage() -> None:
    path = Path(__file__).resolve().parents[1] / "evals/fixtures/v21-design-reopening.json"
    record = json.loads(path.read_text(encoding="utf-8"))
    assert record["schema_version"] == "2.1"
    assert record["request_type"] == "synthesis_design"
    assert record["problem_reopenings"]
    assert record["design_candidates"]
    validate_schema(record)
    assert validate_repo.validate_record_semantics(record) == []


def test_v2_behavioral_scenarios_are_discoverable_without_running_a_host() -> None:
    from scripts.run_evals import load_scenarios

    scenarios = [item for item in load_scenarios() if item["source"] == "v2-methodology-scenarios.md"]
    assert len(scenarios) == 8
    assert all(item["skill"] == "ariadne-skill" for item in scenarios)


def installed_validator():
    path = Path(__file__).resolve().parents[1] / "skills/ariadne-skill/scripts/validate_record.py"
    spec = importlib.util.spec_from_file_location("installed_v21_forecast_validator", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def forecast_record_v21(mechanisms: int = 1, paths: int = 1) -> dict:
    record = record_v21()
    record["request_type"] = "conditional_forecast"
    set_completed_module(record, "ariadne-forecast")
    preregistration = full_preregistration(record)
    preregistration["candidate_mechanisms"] = preregistration["candidate_mechanisms"][:mechanisms]
    preregistration["paths"] = preregistration["paths"][:paths]
    preregistration["competition_search"] = {
        "search_scope": "Review the frozen brief for additional mechanisms and evaluable paths.",
        "reason_no_alternative": "Only the listed complete mechanism or path is supported as a candidate by the available material.",
        "failure_conditions": "Reopen on unmodeled inflows, changed service capacity or incompatible outcome observations.",
    }
    record["module_payloads"] = [{
        "module": "ariadne-forecast",
        "payload": {"preregistration": preregistration, "post_hoc_reconstruction": None},
    }]
    return record


def assert_forecast_valid_on_both(record: dict) -> None:
    validate_schema(record)
    installed = installed_validator()
    assert installed.schema_errors(record, load_schema())[0] == []
    assert validate_repo.validate_record_semantics(record) == []
    assert installed.semantic_errors(record, None) == ([], [])


def assert_forecast_schema_rejected_on_both(record: dict) -> None:
    with pytest.raises(jsonschema.ValidationError):
        validate_schema(record)
    assert installed_validator().schema_errors(record, load_schema())[0]


@pytest.mark.parametrize("mechanisms,paths", [(1, 2), (2, 1), (1, 1)])
def test_single_forecast_mechanism_or_path_requires_a_search_on_both_validators(mechanisms, paths) -> None:
    record = forecast_record_v21(mechanisms, paths)
    assert_forecast_valid_on_both(record)
    assert record["output_ceiling"] == "description_only"
    assert record["authorization_effect"] == "none"
    del record["module_payloads"][0]["payload"]["preregistration"]["competition_search"]
    assert_forecast_schema_rejected_on_both(record)


@pytest.mark.parametrize("missing", ["search_scope", "reason_no_alternative", "failure_conditions"])
def test_forecast_search_cannot_omit_its_explanation(missing) -> None:
    record = forecast_record_v21()
    del record["module_payloads"][0]["payload"]["preregistration"]["competition_search"][missing]
    assert_forecast_schema_rejected_on_both(record)


@pytest.mark.parametrize("field", ["search_scope", "reason_no_alternative", "failure_conditions"])
@pytest.mark.parametrize("kind", ["forecast", "mechanism", "human"])
def test_competition_search_rejects_whitespace_only_fields_on_both_validators(field, kind) -> None:
    if kind == "forecast":
        record = forecast_record_v21()
        search = record["module_payloads"][0]["payload"]["preregistration"]["competition_search"]
    else:
        record = record_v21()
        payload = full_mechanism_payload() if kind == "mechanism" else full_human_payload()
        candidate_field = "candidates" if kind == "mechanism" else "alternative_explanations"
        payload["payload"][candidate_field] = payload["payload"][candidate_field][:1]
        payload["payload"]["competition_search"] = competition_search()
        record["module_payloads"] = [payload]
        set_completed_module(record, payload["module"])
        search = payload["payload"]["competition_search"]
    search[field] = " \t\n "
    assert_forecast_schema_rejected_on_both(record)


@pytest.mark.parametrize("field", ["candidate_mechanisms", "paths"])
def test_forecast_search_does_not_allow_an_empty_candidate_set(field) -> None:
    record = forecast_record_v21()
    record["module_payloads"][0]["payload"]["preregistration"][field] = []
    assert_forecast_schema_rejected_on_both(record)


def test_forecast_search_does_not_waive_the_independent_baseline() -> None:
    record = forecast_record_v21()
    del record["module_payloads"][0]["payload"]["preregistration"]["simple_baseline"]
    assert_forecast_schema_rejected_on_both(record)


def test_legacy_forecast_keeps_its_original_counts_and_disallows_search_extension() -> None:
    record = forecast_record_v21(2, 2)
    record["schema_version"] = "2.0"
    assert_forecast_schema_rejected_on_both(record)
    preregistration = record["module_payloads"][0]["payload"]["preregistration"]
    del preregistration["competition_search"]
    assert_forecast_valid_on_both(record)
    for field in ("candidate_mechanisms", "paths"):
        broken = copy.deepcopy(record)
        broken["module_payloads"][0]["payload"]["preregistration"][field] = preregistration[field][:1]
        assert_forecast_schema_rejected_on_both(broken)
