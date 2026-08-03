from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "method-record.schema.json"


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def valid_record() -> dict:
    return {
        "record_id": "ariadne:case-001:v1",
        "schema_version": "1.0",
        "record_version": 1,
        "parent_record_id": None,
        "request_type": "diagnosis",
        "object_contract": {
            "boundary": "Product team A",
            "state_variables": ["delivery_delay"],
            "relations_or_transitions": ["handoff"],
            "interfaces": ["product-engineering"],
            "time_window": "2026-Q2",
            "scale_profile": {"aggregation": "team", "time": "quarter"},
            "identity_criterion": "same mandate and membership rule",
            "status": "candidate",
        },
        "evidence_cutoff": {
            "as_of": "2026-08-04T00:00:00+08:00",
            "included_source_ids": ["src-1"],
            "excluded_after_cutoff": True,
        },
        "scale_scope": {
            "source": "individual reports",
            "target": "team diagnosis",
            "transform_status": "incomplete",
        },
        "claim_ledger": [
            {
                "claim_id": "claim-1",
                "claim_type": "G",
                "text": "Handoff delay may contribute to delivery delay.",
                "status": "candidate",
                "support_ids": ["src-1"],
                "counterevidence_ids": [],
            }
        ],
        "unknowns_and_counterevidence": {
            "unknowns": ["external dependency latency"],
            "counterevidence": [],
        },
        "output_ceiling": "diagnostic_only",
        "module_runs": [
            {"module": "ariadne-framing", "status": "completed", "record_version": 1}
        ],
        "recommended_next_modules": ["ariadne-evidence"],
        "authorization_effect": "none",
    }


def test_valid_record_matches_schema() -> None:
    jsonschema.validate(valid_record(), load_schema())


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("authorization_effect", "authorized"),
        ("output_ceiling", "execute"),
        ("request_type", "prophecy"),
    ],
)
def test_closed_enums_reject_unauthorized_values(field: str, value: str) -> None:
    record = valid_record()
    record[field] = value
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, load_schema())


def test_child_record_requires_parent_and_higher_version() -> None:
    record = copy.deepcopy(valid_record())
    record["record_version"] = 2
    record["parent_record_id"] = "ariadne:case-001:v1"
    jsonschema.validate(record, load_schema())


def test_additional_top_level_fields_are_rejected() -> None:
    record = valid_record()
    record["silent_authorization"] = True
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, load_schema())
