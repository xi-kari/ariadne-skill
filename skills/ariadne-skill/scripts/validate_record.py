"""Validate optional legacy Ariadne Method Record 2.0/2.1 files.

These schemas remain available for existing machine records and explicit
interoperability. Current Ariadne paths do not require this record format.
This file is the single implementation used by installed and repository tools.

Usage: python scripts/validate_record.py <record.yaml> [--parent <record.yaml> ...]
JSON uses the standard library; YAML needs PyYAML. Structural checking uses
jsonschema when available and reports a limited subset otherwise. The strict
programmatic interface requires exact parent context; the CLI reports omitted
parent-dependent checks separately. No validator result establishes evidence,
legitimacy, or authorization.

Exit codes: 0 checks passed; 1 findings; 2 unreadable input.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "references" / "method-record.schema.json"
RECORD_ID = re.compile(r"^ariadne:[A-Za-z0-9._:-]+$")
RFC3339_DATETIME = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})[Tt]"
    r"(?P<hour>[01]\d|2[0-3]):(?P<minute>[0-5]\d):(?P<second>[0-5]\d|60)"
    r"(?P<fraction>\.\d+)?(?P<zone>[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)$"
)
CEILING_RANK = {"description_only": 0, "diagnostic_only": 1, "requirements_only": 2}
METHOD_RECORD_EXAMPLE = re.compile(
    r"<!--\s*method-record-example:start\s*-->\s*"
    r"```yaml\s*(.*?)```\s*"
    r"<!--\s*method-record-example:end\s*-->",
    re.DOTALL,
)
METHOD_RECORD_LINEAGE_EXAMPLE = re.compile(
    r"<!--\s*method-record-lineage-example:start\s*-->\s*"
    r"```yaml\s*(.*?)```\s*"
    r"<!--\s*method-record-lineage-example:end\s*-->",
    re.DOTALL,
)

def load_record(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml
    except ModuleNotFoundError:
        raise SystemExit(
            f"cannot read {path}: YAML input needs PyYAML (pip install pyyaml) "
            "or supply the record as .json"
        )
    return yaml.safe_load(text)

def _is_rfc3339_datetime(instance: object) -> bool:
    """Match the repository's timezone, calendar, and leap-second checks."""
    if not isinstance(instance, str):
        return True
    match = RFC3339_DATETIME.fullmatch(instance)
    if match is None:
        return False
    second = match.group("second")
    normalized_second = "59" if second == "60" else second
    zone = match.group("zone")
    normalized_zone = "+00:00" if zone in {"Z", "z"} else zone
    normalized = (
        f"{match.group('date')}T{match.group('hour')}:{match.group('minute')}:"
        f"{normalized_second}{match.group('fraction') or ''}{normalized_zone}"
    )
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    if second == "60":
        utc = parsed.astimezone(timezone.utc)
        if (utc.month, utc.day, utc.hour, utc.minute) not in {
            (6, 30, 23, 59),
            (12, 31, 23, 59),
        }:
            return False
    return True

def _parse_forecast_time(value: str) -> datetime:
    """Normalize RFC 3339 UTC designators for Python 3.10 compatibility."""
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    return datetime.fromisoformat(normalized)

def method_record_validator(schema: dict | None = None):
    """Build the complete validator for an explicitly selected legacy record."""
    import jsonschema

    if schema is None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    checker = jsonschema.FormatChecker()
    checker.checks("date-time")(_is_rfc3339_datetime)
    return jsonschema.Draft202012Validator(schema, format_checker=checker)

def validate_method_record(record: dict, schema: dict | None = None) -> None:
    method_record_validator(schema).validate(record)

def schema_errors(record: dict, schema: dict) -> tuple[list[str], str]:
    try:
        import jsonschema
    except ModuleNotFoundError:
        return _structural_subset_errors(record, schema), "structural-subset (jsonschema not installed)"
    validator = method_record_validator(schema)
    found = [
        f"schema: {'/'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in validator.iter_errors(record)
    ]
    return found, "full JSON Schema (jsonschema)"

def _structural_subset_errors(record: dict, schema: dict) -> list[str]:
    errors: list[str] = []
    required = schema.get("required", [])
    for field in required:
        if field not in record:
            errors.append(f"schema-subset: missing required field {field}")
    extra = set(record) - set(schema.get("properties", {}))
    for field in sorted(extra):
        errors.append(f"schema-subset: unknown top-level field {field}")
    props = schema.get("properties", {})
    defs = schema.get("$defs", {})

    def enum_of(prop: dict) -> list | None:
        if "$ref" in prop:
            prop = defs.get(prop["$ref"].rsplit("/", 1)[-1], {})
        return prop.get("enum") or ([prop["const"]] if "const" in prop else None)

    for field in ("request_type", "output_ceiling", "lineage_kind", "authorization_effect", "schema_version"):
        allowed = enum_of(props.get(field, {}))
        if allowed and field in record and record[field] not in allowed:
            errors.append(f"schema-subset: {field} value {record[field]!r} not in {allowed}")
    record_id = record.get("record_id")
    if isinstance(record_id, str) and not RECORD_ID.fullmatch(record_id):
        errors.append("schema-subset: record_id does not match ^ariadne:[A-Za-z0-9._:-]+$")
    if "record_version" in record and not isinstance(record["record_version"], int):
        errors.append("schema-subset: record_version must be an integer")
    return errors

def extract_marked_method_records(text: str) -> list[dict]:
    import yaml

    records: list[dict] = []
    for block in METHOD_RECORD_EXAMPLE.findall(text):
        record = yaml.safe_load(block)
        if not isinstance(record, dict):
            raise ValueError("marked Method Record example is not a mapping")
        records.append(record)
    return records

def extract_marked_method_record_lineages(text: str) -> list[list[dict]]:
    import yaml

    lineages: list[list[dict]] = []
    for block in METHOD_RECORD_LINEAGE_EXAMPLE.findall(text):
        records = yaml.safe_load(block)
        if (
            not isinstance(records, list)
            or len(records) < 2
            or not all(isinstance(record, dict) for record in records)
        ):
            raise ValueError("marked Method Record lineage example is not a list of record mappings")
        lineages.append(records)
    return lineages

def _plain_ref(item: dict) -> dict:
    return {"record_id": item["record_id"], "record_version": item["record_version"]}

def validate_record_semantics(
    record: dict,
    parent_records: Iterable[dict] | None = None,
) -> list[str]:
    errors: list[str] = []
    current_ref = {
        "record_id": record["record_id"],
        "record_version": record["record_version"],
    }
    current_key = (record["record_id"], record["record_version"])
    lineage = record["lineage_kind"]
    parents = record["parent_records"]
    parent_keys = [(item["record_id"], item["record_version"]) for item in parents]

    parent_registry: dict[tuple[str, int], dict] | None = None
    if parent_records is not None:
        parent_registry = {
            (item["record_id"], item["record_version"]): item for item in parent_records
        }
        for parent_id, parent_version in parent_keys:
            if (parent_id, parent_version) not in parent_registry:
                errors.append(f"unresolved parent record: {parent_id}@{parent_version}")
    elif lineage != "root":
        errors.append("non-root semantic validation requires exact parent-record context")

    if lineage == "root":
        if record["parent_record_id"] is not None or parents:
            errors.append("root record must have no parents")
        if record["record_version"] != 1:
            errors.append("root record_version must equal one")
        if record["output_ceiling"] != "description_only":
            errors.append("root record output_ceiling must be description_only")
    elif lineage == "linear":
        if len(parents) != 1 or record["parent_record_id"] != parents[0]["record_id"]:
            errors.append("linear parent_record_id must identify the sole parent_records entry")
        if len(parents) == 1 and record["record_version"] != parents[0]["record_version"] + 1:
            errors.append("linear record_version must equal sole parent version plus one")
    elif lineage == "merge":
        expected = sorted(parents, key=lambda item: (item["record_id"], item["record_version"]))
        if parents != expected:
            errors.append("merge parent_records must be sorted by record_id then version")
        if parents and record["record_version"] != max(
            item["record_version"] for item in parents
        ) + 1:
            errors.append("merge record_version must equal highest parent version plus one")

    if current_key in parent_keys:
        errors.append("record may not identify itself as a parent")
    for parent_id, parent_version in parent_keys:
        if parent_version >= record["record_version"]:
            errors.append(f"parent version must precede current record: {parent_id}@{parent_version}")

    transition = record["ceiling_transition"]
    operation = transition["operation"]
    inputs = transition["inputs"]
    result = transition["result"]
    if result != record["output_ceiling"]:
        errors.append("ceiling transition result must equal output_ceiling")
    if operation == "lower":
        lower_reason = transition.get("reason")
        if not isinstance(lower_reason, str) or not lower_reason.strip():
            errors.append("lower ceiling transition requires a non-empty reason")

    if lineage == "root" and operation != "root":
        errors.append("root lineage requires root ceiling operation")
    if lineage == "linear" and operation == "meet":
        errors.append("linear lineage forbids meet ceiling operation")
    if lineage == "merge" and operation != "meet":
        errors.append("merge lineage requires meet ceiling operation")
    if lineage != "root":
        input_refs = [_plain_ref(item) for item in inputs]
        if input_refs != parents:
            errors.append("ceiling inputs must match parent_records in canonical order")
        if parent_registry is not None:
            for item in inputs:
                key = (item["record_id"], item["record_version"])
                parent = parent_registry.get(key)
                if parent is not None and item["ceiling"] != parent["output_ceiling"]:
                    errors.append(
                        "ceiling input does not match resolved parent output_ceiling: "
                        f"{key[0]}@{key[1]}"
                    )

    if operation == "preserve" and inputs and result != inputs[0]["ceiling"]:
        errors.append("preserve must keep the input ceiling")
    elif operation == "lower" and inputs and CEILING_RANK[result] >= CEILING_RANK[inputs[0]["ceiling"]]:
        errors.append("lower must produce a strictly lower ceiling")
    elif operation == "raise" and inputs:
        if CEILING_RANK[result] <= CEILING_RANK[inputs[0]["ceiling"]]:
            errors.append("raise must produce a strictly higher ceiling")
        source_ids = set(record["evidence_cutoff"]["included_source_ids"])
        rule_entries = {
            entry["rule_id"]: entry for entry in record.get("rule_registry", [])
        }
        rule_ids = set(rule_entries)
        parent_source_ids: set[str] = set()
        parent_rule_ids: set[str] = set()
        if parent_registry is None:
            errors.append("ceiling raise requires exact parent-record context")
        else:
            for key in parent_keys:
                parent = parent_registry.get(key)
                if parent is None:
                    continue
                parent_source_ids.update(parent["evidence_cutoff"]["included_source_ids"])
                parent_rule_ids.update(
                    entry["rule_id"] for entry in parent.get("rule_registry", [])
                )
        seen_basis: set[tuple[str, str]] = set()
        for basis in transition["basis"]:
            basis_key = (basis["basis_kind"], basis["basis_id"])
            if basis_key in seen_basis:
                errors.append(f"ceiling raise basis is duplicated: {basis['basis_id']}")
            seen_basis.add(basis_key)
            if basis["basis_kind"] == "external_evidence":
                registry = source_ids
                parent_registry_ids = parent_source_ids
            else:
                registry = rule_ids
                parent_registry_ids = parent_rule_ids
            if basis["basis_id"] not in registry:
                errors.append(f"ceiling raise basis is not admitted: {basis['basis_id']}")
            elif (
                basis["basis_kind"] == "protocol_fulfillment"
                and rule_entries[basis["basis_id"]]["rule_type"] != "protocol"
            ):
                errors.append(
                    "ceiling protocol basis must reference a protocol rule: "
                    f"{basis['basis_id']}"
                )
            elif parent_registry is not None and basis["basis_id"] in parent_registry_ids:
                errors.append(
                    f"ceiling raise basis is not new relative to parents: {basis['basis_id']}"
                )
    elif operation == "meet" and inputs:
        expected = min(inputs, key=lambda item: CEILING_RANK[item["ceiling"]])["ceiling"]
        if result != expected:
            errors.append("meet result must be the minimum input ceiling")

    claim_ids = [claim["claim_id"] for claim in record["claim_ledger"]]
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("claim IDs must be unique")
    errors.extend(methodology_extension_errors(record))
    rule_ids_list = [entry["rule_id"] for entry in record.get("rule_registry", [])]
    if len(rule_ids_list) != len(set(rule_ids_list)):
        errors.append("rule registry IDs must be unique")
    admitted_sources = set(record["evidence_cutoff"]["included_source_ids"])
    declared_rules = set(rule_ids_list)
    seen_claims: dict[str, str] = {}
    for claim in record["claim_ledger"]:
        if claim["status"] == "supported":
            for support_id in claim["support_ids"]:
                if support_id not in admitted_sources and support_id not in seen_claims:
                    errors.append(
                        f"supported claim {claim['claim_id']} has unresolved support_id: {support_id}"
                    )
                elif (
                    support_id in seen_claims
                    and seen_claims[support_id] not in {"observed", "supported"}
                ):
                    errors.append(
                        f"supported claim {claim['claim_id']} references non-supporting claim: {support_id}"
                    )
            for rule_id in claim["support_rule_ids"]:
                if rule_id not in declared_rules:
                    errors.append(
                        f"supported claim {claim['claim_id']} has unresolved support_rule_id: {rule_id}"
                    )
        seen_claims[claim["claim_id"]] = claim["status"]
    errors.extend(claim_dependency_errors(record))
    errors.extend(scale_scope_errors(record))

    completed_runs = [run for run in record["module_runs"] if run["status"] == "completed"]
    if not any(run["output_record"] == current_ref for run in completed_runs):
        errors.append("a completed module run must identify the current output record")
    for run in completed_runs:
        if run["output_record"] != current_ref:
            errors.append(f"completed {run['module']} run must output the current record")
        if lineage == "root" and run["input_records"]:
            errors.append("root module inputs must be empty")
        elif lineage == "linear" and run["input_records"] != parents:
            errors.append("linear module inputs must equal the sole parent record")
    if lineage == "merge":
        if any(run["input_records"] != parents for run in completed_runs):
            errors.append("merge completed module inputs must equal all canonical parent records")
        audit_runs = [run for run in completed_runs if run["module"] == "ariadne-audit"]
        if not audit_runs or any(run["input_records"] != parents for run in audit_runs):
            errors.append("merge audit inputs must equal all canonical parent records")

    payload_modules = [payload["module"] for payload in record["module_payloads"]]
    if len(payload_modules) != len(set(payload_modules)):
        errors.append("module_payloads may contain at most one payload per module")
    typed_modules = {
        "ariadne-human",
        "ariadne-dynamics",
        "ariadne-mechanism",
        "ariadne-forecast",
        "ariadne-choice",
        "ariadne-audit",
    }
    completed_modules = {run["module"] for run in completed_runs}
    for module in sorted(completed_modules & typed_modules):
        if module not in payload_modules:
            errors.append(f"completed {module} run requires its typed module payload")
    for module in sorted(set(payload_modules) - completed_modules):
        errors.append(f"{module} payload requires a matching completed module run")

    payload_by_module = {
        payload["module"]: payload["payload"] for payload in record["module_payloads"]
    }
    mechanism_payload = payload_by_module.get("ariadne-mechanism")
    if mechanism_payload is not None:
        candidates = mechanism_payload["candidates"]
        candidate_ids = [candidate["mechanism_id"] for candidate in candidates]
        if len(candidate_ids) != len(set(candidate_ids)):
            errors.append("mechanism candidate IDs must be unique")
        signatures = [
            (
                candidate["channel_observation"].strip().casefold(),
                candidate["discriminating_prediction"].strip().casefold(),
                candidate["reverse_or_falsifier"].strip().casefold(),
                candidate["residual_comparison_rule"].strip().casefold(),
            )
            for candidate in candidates
        ]
        if len(signatures) != len(set(signatures)):
            errors.append("mechanism candidates must be distinguishable on their required tests")

    dynamics_payload = payload_by_module.get("ariadne-dynamics")
    if dynamics_payload is not None:
        for event in dynamics_payload["events"]:
            for source_id in event["source_ids"]:
                if source_id not in admitted_sources:
                    errors.append(
                        f"dynamics event {event['event_id']} has unresolved source_id: {source_id}"
                    )

    forecast_payload = payload_by_module.get("ariadne-forecast")
    if forecast_payload is not None:
        preregistration = forecast_payload["preregistration"]
        linked = (
            preregistration
            if preregistration is not None
            else forecast_payload["post_hoc_reconstruction"]
        )
        if linked is not None and (
            linked["record_id"] != record["record_id"]
            or linked["record_version"] != record["record_version"]
        ):
            label = (
                "forecast preregistration"
                if forecast_payload["preregistration"] is not None
                else "forecast post-hoc reconstruction"
            )
            errors.append(f"{label} must link the current record_id and record_version")
        if preregistration is not None:
            try:
                chronology = (
                    _parse_forecast_time(preregistration["baseline_time"])
                    <= _parse_forecast_time(preregistration["input_cutoff"])
                    <= _parse_forecast_time(preregistration["horizon"]["start"])
                    <= _parse_forecast_time(preregistration["horizon"]["deadline"])
                    < _parse_forecast_time(preregistration["result_writeback"]["due_at"])
                )
            except ValueError:
                chronology = False
            if not chronology:
                errors.append(
                    "forecast preregistration chronology must satisfy "
                    "baseline <= cutoff <= start <= deadline < writeback"
                )

    choice_payload = payload_by_module.get("ariadne-choice")
    if choice_payload is not None:
        errors.extend(choice_payload_errors(choice_payload, record["output_ceiling"], record))

    audit_payload = payload_by_module.get("ariadne-audit")
    if audit_payload is not None:
        errors.extend(strong_judgment_errors(audit_payload))
        register = audit_payload["gate_register"]
        any_gate_failed = False
        for gate_ids, gate_results in (
            (("IT1", "IT2", "IT3", "IT4"), register["transformations"]),
            (("IG1", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7"), register["main_gates"]),
        ):
            failed_gate: str | None = None
            for gate_id in gate_ids:
                status = gate_results[gate_id]["status"]
                if failed_gate is not None and status != "not_run":
                    errors.append(f"{gate_id} must be not_run after {failed_gate} failed")
                if failed_gate is None and status == "failed":
                    failed_gate = gate_id
                    any_gate_failed = True
        if any_gate_failed and operation == "raise":
            errors.append("audit gate failure forbids ceiling raise")
        if (
            register["transformations"]["IT1"]["status"] == "failed"
            or register["main_gates"]["IG1"]["status"] == "failed"
        ) and record["output_ceiling"] != "description_only":
            errors.append("IT1 or IG1 failure requires output_ceiling description_only")
    return errors

def methodology_extension_errors(record: dict) -> list[str]:
    """Check references and identity in optional inquiry and design records."""
    errors: list[str] = []
    claim_ids = {claim["claim_id"] for claim in record["claim_ledger"]}
    reopenings = record.get("problem_reopenings", [])
    reopening_ids = [item["reopening_id"] for item in reopenings]
    if len(reopening_ids) != len(set(reopening_ids)):
        errors.append("problem reopening IDs must be unique")
    for item in reopenings:
        for claim_id in item["affected_claim_ids"]:
            if claim_id not in claim_ids:
                errors.append(
                    f"problem reopening {item['reopening_id']} has unresolved affected_claim_id: {claim_id}"
                )
    candidate_ids = [item["candidate_id"] for item in record.get("design_candidates", [])]
    if len(candidate_ids) != len(set(candidate_ids)):
        errors.append("design candidate IDs must be unique")
    return errors

def claim_dependency_errors(record: dict) -> list[str]:
    """Proposition-level downgrade: a claim inherits the limits of what it depends on."""
    errors: list[str] = []
    record_rank = CEILING_RANK[record["output_ceiling"]]
    earlier: dict[str, dict] = {}
    for claim in record["claim_ledger"]:
        claim_id = claim["claim_id"]
        own = claim.get("ceiling")
        if own is not None and CEILING_RANK[own] > record_rank:
            errors.append(f"claim {claim_id} ceiling exceeds the record output_ceiling")
        for dependency in claim.get("depends_on", []):
            parent = earlier.get(dependency)
            if parent is None:
                errors.append(
                    f"claim {claim_id} depends_on must name an earlier claim in this record: {dependency}"
                )
                continue
            if claim["status"] == "supported" and parent["status"] in {
                "contradicted",
                "withdrawn",
                "retired",
            }:
                errors.append(
                    f"claim {claim_id} cannot stay supported on a {parent['status']} dependency: {dependency}"
                )
            parent_ceiling = parent.get("ceiling")
            if (
                own is not None
                and parent_ceiling is not None
                and CEILING_RANK[own] > CEILING_RANK[parent_ceiling]
            ):
                errors.append(
                    f"claim {claim_id} ceiling exceeds the ceiling of its dependency {dependency}"
                )
        earlier[claim_id] = claim
    return errors

def scale_scope_errors(record: dict) -> list[str]:
    scope = record["scale_scope"]
    kind = scope["transform_kind"]
    status = scope["transform_status"]
    if (kind == "none") != (status == "not_needed"):
        return ["scale_scope transform_kind none must pair exactly with transform_status not_needed"]
    return []

def choice_payload_errors(payload: dict, output_ceiling: str, record: dict | None = None) -> list[str]:
    errors: list[str] = []
    option_ids = [option["option_id"] for option in payload["options"]]
    if len(option_ids) != len(set(option_ids)):
        errors.append("choice option_id values must be unique")
    no_action = [option for option in payload["options"] if option["kind"] == "no_action"]
    if len(no_action) != 1:
        errors.append("choice options must contain exactly one no_action option")
    recommendation = payload["analytic_recommendation"]
    if recommendation is not None:
        if recommendation["option_id"] not in option_ids:
            errors.append(
                "analytic recommendation must name a registered option_id: "
                f"{recommendation['option_id']}"
            )
        if output_ceiling != "requirements_only":
            errors.append("an analytic recommendation requires output_ceiling requirements_only")
        if record is not None:
            normative = {claim["claim_id"] for claim in record["claim_ledger"] if claim["claim_type"] == "N"}
            normative |= {
                entry["rule_id"] for entry in record.get("rule_registry", []) if entry.get("rule_type") == "normative"
            }
            for premise in recommendation["normative_premise_ids"]:
                if premise not in normative:
                    errors.append(
                        "analytic recommendation premise must resolve to an N claim or normative rule: " + premise
                    )
    return errors

def strong_judgment_errors(payload: dict) -> list[str]:
    errors: list[str] = []
    ig6 = payload["gate_register"]["main_gates"]["IG6"]["status"]
    strong = payload["strong_judgment"]
    components = strong["components"]
    if ig6 == "passed":
        if strong["status"] != "triggered":
            errors.append("IG6 passed requires a triggered strong-judgment register")
        failing = [code for code, result in components.items() if result["status"] != "passed"]
        if failing:
            errors.append(
                "IG6 passed requires SJ1-SJ8 all passed; not passed: " + ", ".join(sorted(failing))
            )
    if ig6 == "not_applicable" and strong["status"] != "not_triggered":
        errors.append("IG6 not_applicable requires strong_judgment status not_triggered with a reason")
    if strong["status"] == "not_triggered" and any(
        result["status"] != "not_applicable" for result in components.values()
    ):
        errors.append("an untriggered strong-judgment register must mark SJ1-SJ8 not_applicable")
    return errors

def semantic_errors(record: dict, parents: list[dict] | None) -> tuple[list[str], list[str]]:
    """Adapt the shared strict checks to the CLI's explicit partial-check mode."""
    errors = validate_record_semantics(record, parents)
    skipped: list[str] = []
    if parents is None and record["lineage_kind"] != "root":
        missing_context = {
            "non-root semantic validation requires exact parent-record context",
            "ceiling raise requires exact parent-record context",
        }
        errors = [error for error in errors if error not in missing_context]
        skipped.append("parent-dependent checks (raise novelty, input-ceiling match): supply --parent")
    return errors, skipped

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("record", type=Path, help="record file (.yaml or .json)")
    parser.add_argument(
        "--parent",
        action="append",
        type=Path,
        default=[],
        help="parent record file; repeat for every parent of a linear or merge record",
    )
    args = parser.parse_args(argv)

    try:
        record = load_record(args.record)
        parents = [load_record(path) for path in args.parent] or None
    except (OSError, ValueError) as exc:
        print(f"unreadable record: {exc}")
        return 2
    if not isinstance(record, dict):
        print("record file must contain a single mapping")
        return 2

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    findings, mode = schema_errors(record, schema)
    print(f"structural check: {mode}")
    if findings:
        skipped = ["semantic checks: record structure is invalid"]
    else:
        semantic, skipped = semantic_errors(record, parents)
        findings.extend(semantic)

    for note in skipped:
        print(f"skipped: {note}")
    if findings:
        print(f"FAIL: {len(findings)} finding(s)")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("PASS: record satisfies the schema and semantic checks that ran")
    return 0

if __name__ == "__main__":
    sys.exit(main())
