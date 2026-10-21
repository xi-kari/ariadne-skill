"""Validate one Ariadne Method Record file against the shipped schema and semantics.

Ships inside the ariadne-skill package so any host with a Python runtime can run:

    python scripts/validate_record.py <record.yaml> [--parent <record.yaml> ...]

- Structural validation uses the bundled JSON schema (jsonschema when installed,
  a built-in structural subset otherwise, and the mode used is always reported).
- Semantic validation mirrors the repository validator: lineage arithmetic,
  ceiling algebra, raise-basis novelty, module-run and payload pairing,
  supported-claim resolution, proposition-level dependency limits, transform
  kind/status pairing, choice options and analytic recommendation, audit gate
  order, and the IG6 strong-judgment binding. Non-root records need --parent context for the
  parent-dependent checks; without it those checks are reported as skipped.
- Records may be YAML (needs PyYAML) or JSON (standard library only).

Exit code 0 means every requested check passed; 1 means findings; 2 means the
record could not be read at all.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "references" / "method-record.schema.json"
RECORD_ID = re.compile(r"^ariadne:[A-Za-z0-9._:-]+$")
CEILING_RANK = {"description_only": 0, "diagnostic_only": 1, "requirements_only": 2}
TYPED_MODULES = {
    "ariadne-human",
    "ariadne-dynamics",
    "ariadne-mechanism",
    "ariadne-forecast",
    "ariadne-choice",
    "ariadne-audit",
}


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


def schema_errors(record: dict, schema: dict) -> tuple[list[str], str]:
    try:
        import jsonschema
    except ModuleNotFoundError:
        return _structural_subset_errors(record, schema), "structural-subset (jsonschema not installed)"
    validator = jsonschema.Draft202012Validator(schema)
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


def semantic_errors(record: dict, parents: list[dict] | None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    skipped: list[str] = []
    ref = {"record_id": record["record_id"], "record_version": record["record_version"]}
    lineage = record["lineage_kind"]
    parent_refs = record["parent_records"]
    registry = None
    if parents is not None:
        registry = {(p["record_id"], p["record_version"]): p for p in parents}
        for item in parent_refs:
            if (item["record_id"], item["record_version"]) not in registry:
                errors.append(f"unresolved parent record: {item['record_id']}@{item['record_version']}")
    elif lineage != "root":
        skipped.append("parent-dependent checks (raise novelty, input-ceiling match): supply --parent")

    if lineage == "root":
        if record["parent_record_id"] is not None or parent_refs:
            errors.append("root record must have no parents")
        if record["record_version"] != 1:
            errors.append("root record_version must equal one")
        if record["output_ceiling"] != "description_only":
            errors.append("root record output_ceiling must be description_only")
    elif lineage == "linear":
        if len(parent_refs) != 1 or record["parent_record_id"] != parent_refs[0]["record_id"]:
            errors.append("linear parent_record_id must identify the sole parent_records entry")
        if len(parent_refs) == 1 and record["record_version"] != parent_refs[0]["record_version"] + 1:
            errors.append("linear record_version must equal sole parent version plus one")
    elif lineage == "merge":
        ordered = sorted(parent_refs, key=lambda p: (p["record_id"], p["record_version"]))
        if parent_refs != ordered:
            errors.append("merge parent_records must be sorted by record_id then version")
        if len(parent_refs) < 2:
            errors.append("merge needs at least two parents")
        elif record["record_version"] != max(p["record_version"] for p in parent_refs) + 1:
            errors.append("merge record_version must equal highest parent version plus one")

    for item in parent_refs:
        if item["record_version"] >= record["record_version"]:
            errors.append(f"parent version must precede current record: {item['record_id']}")
        if item["record_id"] == record["record_id"] and item["record_version"] == record["record_version"]:
            errors.append("record may not identify itself as a parent")

    transition = record["ceiling_transition"]
    operation, inputs, result = transition["operation"], transition["inputs"], transition["result"]
    if result != record["output_ceiling"]:
        errors.append("ceiling transition result must equal output_ceiling")
    if operation == "lower" and not str(transition.get("reason", "")).strip():
        errors.append("lower ceiling transition requires a non-empty reason")
    if lineage == "root" and operation != "root":
        errors.append("root lineage requires root ceiling operation")
    if lineage == "linear" and operation == "meet":
        errors.append("linear lineage forbids meet ceiling operation")
    if lineage == "merge" and operation != "meet":
        errors.append("merge lineage requires meet ceiling operation")
    if lineage != "root":
        plain = [{"record_id": i["record_id"], "record_version": i["record_version"]} for i in inputs]
        if plain != parent_refs:
            errors.append("ceiling inputs must match parent_records in canonical order")
        if registry is not None:
            for item in inputs:
                parent = registry.get((item["record_id"], item["record_version"]))
                if parent is not None and item["ceiling"] != parent["output_ceiling"]:
                    errors.append(f"ceiling input does not match resolved parent output_ceiling: {item['record_id']}")

    if operation == "preserve" and inputs and result != inputs[0]["ceiling"]:
        errors.append("preserve must keep the input ceiling")
    elif operation == "lower" and inputs and CEILING_RANK[result] >= CEILING_RANK[inputs[0]["ceiling"]]:
        errors.append("lower must produce a strictly lower ceiling")
    elif operation == "raise" and inputs:
        if CEILING_RANK[result] <= CEILING_RANK[inputs[0]["ceiling"]]:
            errors.append("raise must produce a strictly higher ceiling")
        sources = set(record["evidence_cutoff"]["included_source_ids"])
        rules = {entry["rule_id"]: entry for entry in record.get("rule_registry", [])}
        seen = set()
        for basis in transition["basis"]:
            key = (basis["basis_kind"], basis["basis_id"])
            if key in seen:
                errors.append(f"ceiling raise basis is duplicated: {basis['basis_id']}")
            seen.add(key)
            pool = sources if basis["basis_kind"] == "external_evidence" else set(rules)
            if basis["basis_id"] not in pool:
                errors.append(f"ceiling raise basis is not admitted: {basis['basis_id']}")
            elif basis["basis_kind"] == "protocol_fulfillment" and rules[basis["basis_id"]]["rule_type"] != "protocol":
                errors.append(f"ceiling protocol basis must reference a protocol rule: {basis['basis_id']}")
            elif registry is not None:
                parent_pool: set[str] = set()
                for parent in registry.values():
                    parent_pool.update(parent["evidence_cutoff"]["included_source_ids"])
                    parent_pool.update(entry["rule_id"] for entry in parent.get("rule_registry", []))
                if basis["basis_id"] in parent_pool:
                    errors.append(f"ceiling raise basis is not new relative to parents: {basis['basis_id']}")
        if registry is None:
            skipped.append("raise novelty against parents: supply --parent")
    elif operation == "meet" and inputs:
        expected = min(inputs, key=lambda item: CEILING_RANK[item["ceiling"]])["ceiling"]
        if result != expected:
            errors.append("meet result must be the minimum input ceiling")

    claim_ids = [claim["claim_id"] for claim in record["claim_ledger"]]
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("claim IDs must be unique")
    admitted = set(record["evidence_cutoff"]["included_source_ids"])
    declared_rules = {entry["rule_id"] for entry in record.get("rule_registry", [])}
    earlier: dict[str, str] = {}
    for claim in record["claim_ledger"]:
        if claim["status"] == "supported":
            for support_id in claim["support_ids"]:
                if support_id not in admitted and support_id not in earlier:
                    errors.append(f"supported claim {claim['claim_id']} has unresolved support_id: {support_id}")
                elif support_id in earlier and earlier[support_id] not in {"observed", "supported"}:
                    errors.append(f"supported claim {claim['claim_id']} references non-supporting claim: {support_id}")
            for rule_id in claim["support_rule_ids"]:
                if rule_id not in declared_rules:
                    errors.append(f"supported claim {claim['claim_id']} has unresolved support_rule_id: {rule_id}")
        earlier[claim["claim_id"]] = claim["status"]
    errors.extend(claim_dependency_errors(record))
    scope = record["scale_scope"]
    if (scope["transform_kind"] == "none") != (scope["transform_status"] == "not_needed"):
        errors.append("scale_scope transform_kind none must pair exactly with transform_status not_needed")

    completed = [run for run in record["module_runs"] if run["status"] == "completed"]
    if not any(run["output_record"] == ref for run in completed):
        errors.append("a completed module run must identify the current output record")
    for run in completed:
        if run["output_record"] != ref:
            errors.append(f"completed {run['module']} run must output the current record")
        if lineage == "root" and run["input_records"]:
            errors.append("root module inputs must be empty")
        elif lineage == "linear" and run["input_records"] != parent_refs:
            errors.append("linear module inputs must equal the sole parent record")
        elif lineage == "merge" and run["input_records"] != parent_refs:
            errors.append("merge completed module inputs must equal all canonical parent records")
    if lineage == "merge":
        audits = [run for run in completed if run["module"] == "ariadne-audit"]
        if not audits:
            errors.append("merge requires a completed ariadne-audit run over all canonical parents")

    payload_modules = [payload["module"] for payload in record["module_payloads"]]
    if len(payload_modules) != len(set(payload_modules)):
        errors.append("module_payloads may contain at most one payload per module")
    completed_modules = {run["module"] for run in completed}
    for module in sorted((completed_modules & TYPED_MODULES) - set(payload_modules)):
        errors.append(f"completed {module} run requires its typed module payload")
    for module in sorted(set(payload_modules) - completed_modules):
        errors.append(f"{module} payload requires a matching completed module run")

    payloads = {payload["module"]: payload["payload"] for payload in record["module_payloads"]}
    choice = payloads.get("ariadne-choice")
    if choice is not None:
        errors.extend(choice_payload_errors(choice, record["output_ceiling"], record))
    audit = payloads.get("ariadne-audit")
    if audit is not None:
        errors.extend(audit_payload_errors(audit, record["output_ceiling"], transition["operation"]))

    return errors, skipped


def claim_dependency_errors(record: dict) -> list[str]:
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
                errors.append(f"claim {claim_id} depends_on must name an earlier claim in this record: {dependency}")
                continue
            if claim["status"] == "supported" and parent["status"] in {"contradicted", "withdrawn", "retired"}:
                errors.append(f"claim {claim_id} cannot stay supported on a {parent['status']} dependency: {dependency}")
            parent_ceiling = parent.get("ceiling")
            if own is not None and parent_ceiling is not None and CEILING_RANK[own] > CEILING_RANK[parent_ceiling]:
                errors.append(f"claim {claim_id} ceiling exceeds the ceiling of its dependency {dependency}")
        earlier[claim_id] = claim
    return errors


def choice_payload_errors(payload: dict, output_ceiling: str, record: dict | None = None) -> list[str]:
    errors: list[str] = []
    option_ids = [option["option_id"] for option in payload["options"]]
    if len(option_ids) != len(set(option_ids)):
        errors.append("choice option_id values must be unique")
    if sum(option["kind"] == "no_action" for option in payload["options"]) != 1:
        errors.append("choice options must contain exactly one no_action option")
    recommendation = payload["analytic_recommendation"]
    if recommendation is not None:
        if recommendation["option_id"] not in option_ids:
            errors.append(f"analytic recommendation must name a registered option_id: {recommendation['option_id']}")
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


def audit_payload_errors(payload: dict, output_ceiling: str, operation: str) -> list[str]:
    errors: list[str] = []
    register = payload["gate_register"]
    any_failed = False
    for gate_ids, results in (
        (("IT1", "IT2", "IT3", "IT4"), register["transformations"]),
        (("IG1", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7"), register["main_gates"]),
    ):
        failed_gate = None
        for gate_id in gate_ids:
            status = results[gate_id]["status"]
            if failed_gate is not None and status != "not_run":
                errors.append(f"{gate_id} must be not_run after {failed_gate} failed")
            if failed_gate is None and status == "failed":
                failed_gate = gate_id
                any_failed = True
    if any_failed and operation == "raise":
        errors.append("audit gate failure forbids ceiling raise")
    if (
        register["transformations"]["IT1"]["status"] == "failed"
        or register["main_gates"]["IG1"]["status"] == "failed"
    ) and output_ceiling != "description_only":
        errors.append("IT1 or IG1 failure requires output_ceiling description_only")
    ig6 = register["main_gates"]["IG6"]["status"]
    strong = payload["strong_judgment"]
    components = strong["components"]
    if ig6 == "passed":
        if strong["status"] != "triggered":
            errors.append("IG6 passed requires a triggered strong-judgment register")
        failing = sorted(code for code, result in components.items() if result["status"] != "passed")
        if failing:
            errors.append("IG6 passed requires SJ1-SJ8 all passed; not passed: " + ", ".join(failing))
    if ig6 == "not_applicable" and strong["status"] != "not_triggered":
        errors.append("IG6 not_applicable requires strong_judgment status not_triggered with a reason")
    if strong["status"] == "not_triggered" and any(result["status"] != "not_applicable" for result in components.values()):
        errors.append("an untriggered strong-judgment register must mark SJ1-SJ8 not_applicable")
    return errors


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
