"""Dedicated forecasts freeze inputs and append outcomes without a global record."""
from __future__ import annotations

import copy
import importlib.util
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/ariadne-skill/scripts/forecast.py"


@pytest.fixture
def forecast(monkeypatch):
    spec = importlib.util.spec_from_file_location("ariadne_forecast_registry", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "utc_now", lambda: datetime(2026, 11, 17, 12, tzinfo=timezone.utc))
    return module


def draft() -> dict:
    return {
        "artifact_version": "1.0",
        "artifact_type": "forecast_draft",
        "forecast_id": "queue-week-1",
        "outcome_known": False,
        "model": {"id": "manual-queue-rule", "version": "1"},
        "target": {
            "question": "Will the observed queue exceed 100 items by the deadline?",
            "scope": "One named support queue; count open items using the frozen definition.",
            "outcome_rule": "Use the final observed open-item count; missing observation is not zero.",
        },
        "input": {
            "cutoff": "2026-11-17T11:00:00Z",
            "sources": [{
                "source_id": "queue-snapshot",
                "description": "Synthetic exercise: supplied snapshot says 80 open items.",
                "kind": "reported",
                "available_at": "2026-11-17T10:00:00Z",
            }],
        },
        "window": {
            "starts_at": "2026-11-17T12:00:00Z",
            "deadline": "2026-11-24T12:00:00Z",
            "error_tolerance": "Exact final count if observable; no imputation for missing labels.",
        },
        "baseline": {
            "as_of": "2026-11-17T10:00:00Z",
            "description": "Persistence of the supplied current count.",
            "expectation": "80 open items at the deadline.",
            "evaluation_rule": "Compare the observed count with 80 under the same counting rule.",
        },
        "mechanisms": [{
            "candidate_id": "persistence",
            "claim": "Inflow and service may approximately balance.",
            "basis_source_ids": ["queue-snapshot"],
        }],
        "paths": [{
            "path_id": "stable-queue",
            "description": "Approximately stable queue if inflow and service balance.",
            "mechanism_ids": ["persistence"],
            "basis_source_ids": ["queue-snapshot"],
        }],
        "competition_search": {
            "search_scope": "Only the supplied snapshot and stated queue task were available.",
            "reason_no_alternative": "No second mechanism or path has enough material for this register.",
            "failure_conditions": "Reopen when measured inflow or service contradicts balance.",
        },
        "expression": {"kind": "unknown", "reason": "One snapshot does not support a probability or path ranking."},
        "decision_use": {"status": "not_applicable", "reason": "This exercise monitors a target without selecting an action."},
        "evaluation": {
            "rule": "Evaluate the fixed target using the final observation and retain missingness.",
            "calibration_plan": "No calibrated probability is claimed; retain outcome and baseline comparison for later review.",
            "failure_rules": {
                "supported": "Not applicable to this unknown expression: no positive forecast was made.",
                "not_supported": "Not applicable to this unknown expression: an abstention cannot count as a miss.",
                "unresolved": "Conflicting observations do not settle the count.",
                "target_invalid": "The queue identity or counting definition changes.",
                "not_evaluable": "The expression abstained; retain any target observation without scoring a forecast, and preserve missing labels when unavailable.",
            },
        },
        "signals": {
            "early": ["A measured change in inflow or service."],
            "reverse": ["A sustained queue decrease contradicts a growing path."],
            "pause": ["The source becomes inaccessible."],
            "retirement": ["The queue is replaced by a non-comparable process."],
        },
        "response_regime": "Monitoring only; no intervention is triggered by this artifact.",
        "review": {
            "owner": "Exercise reviewer",
            "next_review_at": "2026-11-20T12:00:00Z",
            "writeback_due_at": "2026-11-25T12:00:00Z",
            "destination": "This local registry; an owner must run resolve explicitly.",
        },
    }


def resolution() -> dict:
    return {
        "artifact_version": "1.0",
        "artifact_type": "resolution_draft",
        "resolution_id": "review-1",
        "observed_at": "2026-11-24T12:00:00Z",
        "sources": [{
            "source_id": "missing-monitor",
            "description": "Exercise report: the deadline monitor was unavailable.",
            "kind": "reported",
            "available_at": "2026-11-24T12:01:00Z",
        }],
        "actual_result": None,
        "status": "not_evaluable",
        "reason": "The outcome label is missing.",
        "baseline_comparison": "Neither forecast nor persistence can be scored without the label.",
        "response_observations": "No response intervention was recorded.",
        "next_step": "Seek an independently preserved deadline snapshot; do not manufacture a zero.",
    }


def after_deadline(forecast, monkeypatch) -> None:
    monkeypatch.setattr(forecast, "utc_now", lambda: datetime(2026, 11, 25, 12, tzinfo=timezone.utc))


def test_register_readback_then_append_preserves_frozen_bytes(forecast, tmp_path, monkeypatch) -> None:
    registry = tmp_path / "registry"
    path = forecast.register(draft(), registry)
    before = path.read_bytes()
    saved = forecast.load_json(path)
    assert saved["artifact_type"] == "forecast_registration"
    assert saved["registered_at"] == "2026-11-17T12:00:00Z"
    forecast.validate_artifact(saved)
    after_deadline(forecast, monkeypatch)
    appended = forecast.resolve("queue-week-1", resolution(), registry)
    result = forecast.load_json(appended)
    assert result["actual_result"] is None
    assert result["status"] == "not_evaluable"
    assert result["forecast_id"] == saved["forecast_id"]
    assert result["registered_artifact_sha256"] == forecast.sha256_bytes(before)
    assert path.read_bytes() == before
    forecast.validate_artifact(result)


def test_duplicate_registration_and_resolution_do_not_overwrite(forecast, tmp_path, monkeypatch) -> None:
    path = forecast.register(draft(), tmp_path)
    before = path.read_bytes()
    with pytest.raises(forecast.ForecastError):
        forecast.register(draft(), tmp_path)
    assert path.read_bytes() == before
    after_deadline(forecast, monkeypatch)
    added = forecast.resolve("queue-week-1", resolution(), tmp_path)
    original_resolution = added.read_bytes()
    with pytest.raises(forecast.ForecastError):
        forecast.resolve("queue-week-1", resolution(), tmp_path)
    assert added.read_bytes() == original_resolution


@pytest.mark.parametrize("mutation", ["known", "expired", "future_cutoff", "source_after_cutoff", "bad_window", "bad_review"])
def test_registration_rejects_hindsight_and_inconsistent_times(forecast, tmp_path, mutation) -> None:
    value = draft()
    if mutation == "known":
        value["outcome_known"] = True
    elif mutation == "expired":
        value["window"]["deadline"] = "2026-11-17T12:00:00Z"
    elif mutation == "future_cutoff":
        value["input"]["cutoff"] = "2026-11-18T00:00:00Z"
        value["window"]["starts_at"] = value["input"]["cutoff"]
    elif mutation == "source_after_cutoff":
        value["input"]["sources"][0]["available_at"] = "2026-11-17T11:30:00Z"
    elif mutation == "bad_window":
        value["window"]["starts_at"] = "2026-11-25T00:00:00Z"
    else:
        value["review"]["writeback_due_at"] = value["window"]["deadline"]
    with pytest.raises(forecast.ForecastError):
        forecast.register(value, tmp_path)
    assert not (tmp_path / value["forecast_id"]).exists()


@pytest.mark.parametrize("bad", ["2026-11-17T10:00:00", "not-a-time", "2026-02-30T10:00:00Z"])
def test_unzoned_or_invalid_dates_are_rejected(forecast, bad) -> None:
    value = draft()
    value["input"]["cutoff"] = bad
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


@pytest.mark.parametrize("suffix", ["Z", "z", "+00:00"])
def test_utc_designators_work_on_supported_python(forecast, tmp_path, suffix) -> None:
    value = draft()
    value["input"]["cutoff"] = "2026-11-17T11:00:00" + suffix
    assert forecast.register(value, tmp_path).is_file()


def test_one_reasonable_candidate_does_not_create_probability(forecast, tmp_path) -> None:
    value = draft()
    path = forecast.register(value, tmp_path)
    assert forecast.load_json(path)["expression"] == value["expression"]
    del value["competition_search"]
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


@pytest.mark.parametrize("mutation", ["invented_source", "invented_mechanism", "unknown_probability", "empty_search", "missing_baseline"])
def test_references_and_expression_identity_are_enforced(forecast, mutation) -> None:
    value = draft()
    if mutation == "invented_source":
        value["mechanisms"][0]["basis_source_ids"] = ["absent"]
    elif mutation == "invented_mechanism":
        value["paths"][0]["mechanism_ids"] = ["absent"]
    elif mutation == "unknown_probability":
        value["expression"]["value"] = 0.8
    elif mutation == "empty_search":
        value["competition_search"]["search_scope"] = "  \n "
    else:
        del value["baseline"]
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


@pytest.mark.parametrize("unsafe", ["../escape", "a/b", "..", "a\\b", "/tmp/escape"])
def test_forecast_and_resolution_ids_cannot_escape_registry(forecast, tmp_path, unsafe, monkeypatch) -> None:
    value = draft()
    value["forecast_id"] = unsafe
    with pytest.raises(forecast.ForecastError):
        forecast.register(value, tmp_path)
    forecast.register(draft(), tmp_path)
    after_deadline(forecast, monkeypatch)
    obs = resolution()
    obs["resolution_id"] = unsafe
    with pytest.raises(forecast.ForecastError):
        forecast.resolve("queue-week-1", obs, tmp_path)
    with pytest.raises(forecast.ForecastError):
        forecast.resolve(unsafe, resolution(), tmp_path)


def test_symlink_registry_and_frozen_artifact_are_rejected(forecast, tmp_path, monkeypatch) -> None:
    outside = tmp_path / "outside"
    outside.mkdir()
    linked = tmp_path / "linked"
    linked.symlink_to(outside, target_is_directory=True)
    with pytest.raises(forecast.ForecastError):
        forecast.register(draft(), linked / "nested")
    real_registry = tmp_path / "registry"
    path = forecast.register(draft(), real_registry)
    moved = outside / "original.json"
    path.rename(moved)
    path.symlink_to(moved)
    after_deadline(forecast, monkeypatch)
    with pytest.raises(forecast.ForecastError):
        forecast.resolve("queue-week-1", resolution(), real_registry)
    assert not (real_registry / "queue-week-1" / "resolutions").exists()


def test_missing_labels_cannot_be_resolved_as_supported(forecast) -> None:
    value = resolution()
    value["status"] = "supported"
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


def test_cli_validation_reports_clean_error_and_real_readback(forecast, tmp_path, capsys) -> None:
    path = tmp_path / "input.json"
    path.write_text(json.dumps(draft()), encoding="utf-8")
    assert forecast.main(["register", "--input", str(path), "--registry", str(tmp_path / "registry")]) == 0
    receipt = json.loads(capsys.readouterr().out)
    artifact = Path(receipt["artifact_path"])
    assert artifact.is_file()
    assert forecast.main(["validate", str(artifact)]) == 0
    assert "validated" in capsys.readouterr().out
    path.write_text('{"artifact_version":', encoding="utf-8")
    assert forecast.main(["validate", str(path)]) == 1
    assert "Traceback" not in capsys.readouterr().err


def test_nonfinite_probability_and_duplicate_json_fields_are_rejected(forecast, tmp_path) -> None:
    value = draft()
    value["expression"] = {"kind": "probability", "value": float("nan"), "event": "target event", "basis": "declared model", "basis_source_ids": ["queue-snapshot"], "method": "probabilistic_model"}
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)
    path = tmp_path / "ambiguous.json"
    path.write_text('{"outcome_known":true,"outcome_known":false}', encoding="utf-8")
    with pytest.raises(forecast.ForecastError):
        forecast.load_json(path)


def test_resolution_can_retain_evidence_that_registration_was_invalid(forecast, tmp_path, monkeypatch) -> None:
    frozen = forecast.register(draft(), tmp_path)
    original = frozen.read_bytes()
    after_deadline(forecast, monkeypatch)
    value = resolution()
    value.update(observed_at="2026-11-17T10:00:00Z", status="target_invalid", actual_result="An earlier outcome was later discovered.", reason="The registration's claim of an unknown outcome is challenged by a retained source.")
    result = forecast.resolve("queue-week-1", value, tmp_path)
    assert forecast.load_json(result)["status"] == "target_invalid"
    assert frozen.read_bytes() == original


def test_resolution_future_observation_and_symlink_append_directory_are_rejected(forecast, tmp_path, monkeypatch) -> None:
    forecast.register(draft(), tmp_path)
    with pytest.raises(forecast.ForecastError):
        forecast.resolve("queue-week-1", resolution(), tmp_path)
    assert not (tmp_path / "queue-week-1" / "resolutions").exists()
    after_deadline(forecast, monkeypatch)
    outside = tmp_path / "outside"
    outside.mkdir()
    (tmp_path / "queue-week-1" / "resolutions").symlink_to(outside, target_is_directory=True)
    with pytest.raises(forecast.ForecastError):
        forecast.resolve("queue-week-1", resolution(), tmp_path)
    assert list(outside.iterdir()) == []


def test_installable_contract_example_matches_the_dedicated_schema(forecast) -> None:
    contract = SCRIPT.parents[1] / "contracts/forecast.md"
    examples = re.findall(r"```json\n(.*?)\n```", contract.read_text(encoding="utf-8"), re.S)
    assert examples
    for example in examples:
        forecast.validate_artifact(json.loads(example))


@pytest.mark.parametrize("status", ["supported", "not_supported"])
def test_abstention_cannot_be_counted_as_hit_or_miss(forecast, tmp_path, monkeypatch, status) -> None:
    frozen = forecast.register(draft(), tmp_path)
    original = frozen.read_bytes()
    after_deadline(forecast, monkeypatch)
    value = resolution()
    value.update(status=status, actual_result="120 open items were reported at the deadline.", reason="The target threshold was crossed.")
    value["sources"][0]["description"] = "Reported deadline count: 120 open items."
    with pytest.raises(forecast.ForecastError, match="abstention"):
        forecast.resolve("queue-week-1", value, tmp_path)
    assert frozen.read_bytes() == original
    assert not (tmp_path / "queue-week-1" / "resolutions").exists()
    value.update(status="not_evaluable", reason="The original unknown expression abstained from a forecast; the target observation is retained.")
    appended = forecast.resolve("queue-week-1", value, tmp_path)
    assert forecast.load_json(appended)["actual_result"] == value["actual_result"]
    assert frozen.read_bytes() == original


@pytest.mark.parametrize("factory,field", [(draft, "forecast_id"), (resolution, "resolution_id")])
def test_identifier_trailing_newline_is_rejected_during_validation(forecast, factory, field) -> None:
    value = factory()
    value[field] += "\n"
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


@pytest.mark.parametrize("missing", ["model", "model_version", "baseline_time", "decision_use", "decision_reason"])
def test_model_baseline_and_decision_context_cannot_be_omitted(forecast, missing) -> None:
    value = draft()
    if missing == "model_version":
        del value["model"]["version"]
    elif missing == "baseline_time":
        del value["baseline"]["as_of"]
    elif missing == "decision_reason":
        del value["decision_use"]["reason"]
    else:
        del value[missing]
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


@pytest.mark.parametrize("timestamp", ["2026-11-17T11:01:00Z", "2026-11-17T10:00:00"])
def test_baseline_must_be_dated_no_later_than_input_cutoff(forecast, timestamp) -> None:
    value = draft()
    value["baseline"]["as_of"] = timestamp
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


def test_decision_use_requires_a_threshold_without_creating_permission(forecast, tmp_path) -> None:
    value = draft()
    value["decision_use"] = {"status": "applicable", "decision": "Whether to discuss a staffing trial", "threshold": "Discuss the option if a supported forecast exceeds 100 open items; adoption needs the existing decision process."}
    forecast.validate_artifact(value)
    path = forecast.register(value, tmp_path)
    assert forecast.load_json(path)["decision_use"] == value["decision_use"]
    del value["decision_use"]["threshold"]
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


def test_empirical_probability_estimate_does_not_require_claimed_calibration(forecast) -> None:
    value = draft()
    value["expression"] = {"kind": "probability", "value": 0.3, "event": "The frozen threshold is crossed.", "basis": "A declared estimate from an appropriate reference sample; calibration remains unevaluated.", "basis_source_ids": ["queue-snapshot"], "method": "empirical_estimate"}
    forecast.validate_artifact(value)
    assert value["expression"]["method"] == "empirical_estimate"


def test_belief_identifies_whose_belief_and_weight_identifies_its_purpose(forecast) -> None:
    value = draft()
    value["expression"] = {"kind": "belief", "subject": "The named analyst", "value": 0.4, "basis": "The analyst's credence given only the supplied snapshot and no arrival-rate observations.", "basis_source_ids": ["queue-snapshot"]}
    forecast.validate_artifact(value)
    del value["expression"]["subject"]
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)
    value["expression"] = {"kind": "scenario_weight", "weights": [{"path_id": "stable-queue", "value": 1}], "normalization": "Weights total one within this exploration batch.", "purpose": "Allocate exploration effort; not an outcome probability.", "basis": "Only one complete candidate path is currently available.", "basis_source_ids": ["queue-snapshot"]}
    forecast.validate_artifact(value)
    del value["expression"]["purpose"]
    with pytest.raises(forecast.ForecastError):
        forecast.validate_artifact(value)


def test_nonabstaining_expression_can_receive_a_reasoned_outcome(forecast, tmp_path, monkeypatch) -> None:
    value = draft()
    value["expression"] = {"kind": "qualitative", "statement": "Within this stipulated teaching case, the queue is expected to exceed 100.", "basis": "An explicit teaching assumption, not an empirical performance claim.", "basis_source_ids": ["queue-snapshot"]}
    value["evaluation"]["failure_rules"].update(supported="Observed count exceeds the frozen threshold.", not_supported="Observed count does not exceed the frozen threshold.")
    frozen = forecast.register(value, tmp_path)
    original = frozen.read_bytes()
    after_deadline(forecast, monkeypatch)
    outcome = resolution()
    outcome.update(status="supported", actual_result="Reported count: 120", reason="The observed count meets the frozen qualitative criterion; this is not probability calibration.", baseline_comparison="The persistence baseline of 80 differs from the reported 120.")
    outcome["sources"][0]["description"] = "Teaching report of the deadline count."
    appended = forecast.resolve("queue-week-1", outcome, tmp_path)
    assert forecast.load_json(appended)["status"] == "supported"
    assert frozen.read_bytes() == original
