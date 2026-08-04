from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

EXPECTED_REFERENCES = {
    "ariadne-skill": {"lattice-kernel.md", "routing.md", "method-record.md", "source-navigation.json"},
    "ariadne-framing": {"object-contract.md"},
    "ariadne-evidence": {"evidence-contracts.md"},
    "ariadne-scale": {"scale-transformations.md"},
    "ariadne-mechanism": {"mechanism-contracts.md"},
    "ariadne-human": {"human-domain.md", "human-variable-cards.json"},
    "ariadne-dynamics": {"dynamic-derivation.md"},
    "ariadne-forecast": {"forecast-contract.md"},
    "ariadne-choice": {"choice-and-authorization.md"},
    "ariadne-audit": {"gates-and-governance.md", "application-contracts.json"},
}

FORBIDDEN_MARKERS = ("TODO", "TBD", "PLACEHOLDER", "implement later", "fill in details")
FOREIGN_PRODUCT_NAMES = ("CrossFrame", "world-structure")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
METHOD_RECORD_EXAMPLE = re.compile(
    r"<!--\s*method-record-example:start\s*-->\s*"
    r"```yaml\s*(.*?)```\s*"
    r"<!--\s*method-record-example:end\s*-->",
    re.DOTALL,
)
CEILING_RANK = {
    "description_only": 0,
    "diagnostic_only": 1,
    "requirements_only": 2,
}
RFC3339_DATETIME = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})[Tt]"
    r"(?P<hour>[01]\d|2[0-3]):(?P<minute>[0-5]\d):(?P<second>[0-5]\d|60)"
    r"(?P<fraction>\.\d+)?(?P<zone>[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)$"
)
FORMAT_CHECKER = jsonschema.FormatChecker()
EXPECTED_NUMBERING_SYSTEMS = {
    "D0-D3",
    "U01-U11",
    "G1-G4",
    "E1-E5",
    "C1-C12",
    "A/X/T/O/C/R/I/N/J",
    "M01-M09",
    "CM-*",
    "H1-H6",
    "GC/GS/GE/CV/RS/IS/IM/IB",
    "HV01-HV11",
    "S0-S6/X0",
    "IG1-IG7",
    "SJ1-SJ8",
    "L1-L3",
    "TOOL-*",
    "N1-N5",
    "O1-O4",
    "PF-1-PF-10",
    "T0-T4",
    "APP-*",
    "GOV-01-GOV-24",
}
EXPECTED_SHARED_NOTATION = {"S*=<B,X,R,I,T,SP,K>", "N0", "K*/F*", "G-instance/H-instance"}
EXPECTED_SHARED_SEMANTICS = {
    "preserved",
    "changed",
    "collapsed",
    "omitted",
    "new_unknowns",
    "source_lineage",
    "applicability",
    "residuals",
    "stopping",
}
EXPECTED_RETAINED_DIFFERENCES = {
    "operator_alignment": {
        "nine_scale_operators",
        "common_operator_steps",
        "no_forced_one_to_one_alignment",
    },
    "record_system_separation": {
        "fourteen_section_scale_record",
        "closed_artifact_system",
        "no_merge",
    },
}
EXPECTED_PROHIBITED_SUBSTITUTIONS = {
    "contract_substitution": {"names", "analogies", "examples", "shared_steps", "complete_contract"},
    "difference_erasure": {
        "shared_vocabulary",
        "non_transferable_elements",
        "source_authority",
        "recorded_differences",
    },
}
EXPECTED_D5_APPLICABILITY = {
    "kind": "conditional_proof_discipline",
    "admissible_output": ["testable_bridge_requirements", "bounded_candidate"],
    "prohibited_output": ["cross_domain_theorem", "empirical_transfer_without_conditions"],
}
EXPECTED_PROOF_FIELDS = {
    "source_object",
    "target_object",
    "limit_or_scale_law",
    "initial_conditions",
    "history_structure",
    "error",
    "valid_time",
    "failure_boundary",
}
EXPECTED_NON_PROOF_BOUNDARIES = {
    "not_all_transfers_lose_information",
    "not_social_or_psychological_boltzmann",
    "task_loss_not_physical_entropy",
}
STAGE_PHASES = (
    "RED_BASELINE",
    "BUILD_ALL_CONTENT",
    "WHOLE_SUITE_CONTENT_COMPLETE",
    "INTEGRATED_REVIEW",
    "WHOLE_SUITE_REPAIR",
    "WORKER_FINAL_VALIDATION",
    "PARENT_INDEPENDENT_VALIDATION",
    "RELEASE",
)
STAGE_BLOCK = re.compile(
    r"<!--\s*ariadne-stage-status:start\s*-->(.*?)"
    r"<!--\s*ariadne-stage-status:end\s*-->",
    re.DOTALL,
)


@FORMAT_CHECKER.checks("date-time")
def _is_rfc3339_datetime(instance: object) -> bool:
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


def method_record_validator(schema: dict | None = None) -> jsonschema.Draft202012Validator:
    if schema is None:
        schema = json.loads(
            (ROOT / "schemas" / "method-record.schema.json").read_text(encoding="utf-8")
        )
    return jsonschema.Draft202012Validator(schema, format_checker=FORMAT_CHECKER)


def validate_method_record(record: dict, schema: dict | None = None) -> None:
    method_record_validator(schema).validate(record)


def validate_source_navigation(data: dict) -> list[str]:
    errors: list[str] = []
    numbering = data.get("appendix_b_numbering")
    if not isinstance(numbering, list):
        errors.append("source navigation appendix_b_numbering must be a list")
    else:
        codes = {entry.get("code") for entry in numbering if isinstance(entry, dict)}
        if codes != EXPECTED_NUMBERING_SYSTEMS or len(numbering) != len(EXPECTED_NUMBERING_SYSTEMS):
            errors.append("source navigation numbering systems are incomplete or noncanonical")
        for entry in numbering:
            if not isinstance(entry, dict) or set(entry) != {"code", "meaning", "authority", "owner"}:
                errors.append("source navigation numbering entry shape is invalid")
                continue
            if not all(isinstance(entry[field], str) and entry[field] for field in entry):
                errors.append(f"source navigation numbering entry is empty: {entry.get('code')}")

    notation = data.get("shared_notation")
    if not isinstance(notation, list):
        errors.append("source navigation shared_notation must be a list")
    else:
        symbols = {entry.get("notation") for entry in notation if isinstance(entry, dict)}
        if symbols != EXPECTED_SHARED_NOTATION or len(notation) != len(EXPECTED_SHARED_NOTATION):
            errors.append("source navigation shared notation is incomplete or noncanonical")

    appendix_d = data.get("appendix_d")
    if not isinstance(appendix_d, dict):
        return errors + ["source navigation appendix_d must be an object"]
    dual_text = appendix_d.get("dual_text_difference")
    if not isinstance(dual_text, dict):
        errors.append("source navigation D.4 dual_text_difference is missing")
    else:
        shared = set(dual_text.get("minimum_shared_semantics", []))
        shared_items = dual_text.get("minimum_shared_semantics", [])
        if shared != EXPECTED_SHARED_SEMANTICS or len(shared_items) != len(EXPECTED_SHARED_SEMANTICS):
            errors.append("source navigation D.4 minimum shared semantics are incomplete")
        retained = dual_text.get("retained_differences", [])
        retained_map = {
            entry.get("id"): set(entry.get("semantic_elements", []))
            for entry in retained
            if isinstance(entry, dict)
        }
        if retained_map != EXPECTED_RETAINED_DIFFERENCES or len(retained) != len(
            EXPECTED_RETAINED_DIFFERENCES
        ) or any(
            set(entry) != {"id", "rule", "semantic_elements"}
            or not isinstance(entry["rule"], str)
            or len(entry["rule"].strip()) < 40
            for entry in retained
            if isinstance(entry, dict)
        ):
            errors.append("source navigation D.4 must retain both contract-system differences")
        substitutions = dual_text.get("prohibited_substitutions", [])
        substitution_map = {
            entry.get("id"): set(entry.get("guards", []))
            for entry in substitutions
            if isinstance(entry, dict)
        }
        if substitution_map != EXPECTED_PROHIBITED_SUBSTITUTIONS or len(
            substitutions
        ) != len(EXPECTED_PROHIBITED_SUBSTITUTIONS) or any(
            set(entry) != {"id", "rule", "guards"}
            or not isinstance(entry["rule"], str)
            or len(entry["rule"].strip()) < 40
            for entry in substitutions
            if isinstance(entry, dict)
        ):
            errors.append("source navigation D.4 prohibited substitutions are incomplete")

    heuristic = appendix_d.get("cross_scale_proof_heuristic")
    if not isinstance(heuristic, dict):
        errors.append("source navigation D.5 cross_scale_proof_heuristic is missing")
    else:
        proof_fields = heuristic.get("required_fields", [])
        if set(proof_fields) != EXPECTED_PROOF_FIELDS or len(proof_fields) != len(EXPECTED_PROOF_FIELDS):
            errors.append("source navigation D.5 proof fields are incomplete")
        non_proof = heuristic.get("non_proof_boundaries", [])
        if set(non_proof) != EXPECTED_NON_PROOF_BOUNDARIES or len(non_proof) != len(EXPECTED_NON_PROOF_BOUNDARIES):
            errors.append("source navigation D.5 non-proof boundaries are incomplete")
        if heuristic.get("execution_owner") != "ariadne-scale":
            errors.append("source navigation D.5 must route execution to ariadne-scale")
        if heuristic.get("applicability") != EXPECTED_D5_APPLICABILITY:
            errors.append("source navigation D.5 applicability boundary is missing")
    return errors


def extract_stage_status(text: str) -> dict[str, str]:
    match = STAGE_BLOCK.search(text)
    if match is None:
        return {}
    status: dict[str, str] = {}
    for line in match.group(1).splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2 or cells[0] in {"Phase", "---"} or set(cells[0]) == {"-"}:
            continue
        status[cells[0]] = cells[1]
    return status


def validate_stage_status(status: dict[str, str]) -> list[str]:
    errors: list[str] = []
    if tuple(status) != STAGE_PHASES:
        errors.append("execution stage table must list the canonical phases in order")
        return errors
    allowed = {"complete", "in_progress", "pending", "not_authorized"}
    for phase, value in status.items():
        if value not in allowed:
            errors.append(f"invalid execution stage status: {phase}={value}")
    ordered_work = STAGE_PHASES[:-2]
    for index, phase in enumerate(ordered_work):
        value = status[phase]
        if value in {"complete", "in_progress"}:
            for prerequisite in ordered_work[:index]:
                if status[prerequisite] != "complete":
                    errors.append(f"{phase} cannot advance before {prerequisite} is complete")
    if sum(value == "in_progress" for value in status.values()) > 1:
        errors.append("at most one execution phase may be in_progress")
    if status["PARENT_INDEPENDENT_VALIDATION"] == "complete" and status["WORKER_FINAL_VALIDATION"] != "complete":
        errors.append("parent validation cannot complete before worker validation")
    if status["RELEASE"] != "not_authorized":
        errors.append("release must remain not_authorized in this worktree")
    return errors


def validate_skill_metadata(name: str, metadata: dict) -> list[str]:
    errors: list[str] = []
    try:
        interface = metadata["interface"]
        if metadata.get("policy", {}).get("allow_implicit_invocation") is not True:
            errors.append(f"implicit invocation disabled or absent for {name}")
        short = interface["short_description"]
        if not 25 <= len(short) <= 64:
            errors.append(f"short_description length invalid for {name}: {len(short)}")
        if f"${name}" not in interface["default_prompt"]:
            errors.append(f"default_prompt does not invoke ${name}")
    except (KeyError, TypeError) as exc:
        errors.append(f"metadata invalid for {name}: {exc}")
    return errors


def validate_reference_routes(name: str, skill_text: str, expected_refs: set[str]) -> list[str]:
    linked_refs = {
        target.removeprefix("references/")
        for target in MARKDOWN_LINK.findall(skill_text)
        if target.startswith("references/")
    }
    missing = sorted(expected_refs - linked_refs)
    return [f"{name} does not directly route reference: {reference}" for reference in missing]


def extract_marked_method_records(text: str) -> list[dict]:
    records: list[dict] = []
    for block in METHOD_RECORD_EXAMPLE.findall(text):
        record = yaml.safe_load(block)
        if not isinstance(record, dict):
            raise ValueError("marked Method Record example is not a mapping")
        records.append(record)
    return records


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
                    datetime.fromisoformat(preregistration["baseline_time"])
                    <= datetime.fromisoformat(preregistration["input_cutoff"])
                    <= datetime.fromisoformat(preregistration["horizon"]["start"])
                    <= datetime.fromisoformat(preregistration["horizon"]["deadline"])
                    < datetime.fromisoformat(preregistration["result_writeback"]["due_at"])
                )
            except ValueError:
                chronology = False
            if not chronology:
                errors.append(
                    "forecast preregistration chronology must satisfy "
                    "baseline <= cutoff <= start <= deadline < writeback"
                )

    audit_payload = payload_by_module.get("ariadne-audit")
    if audit_payload is not None:
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


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        raise ValueError(f"missing frontmatter: {path}")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"frontmatter is not a mapping: {path}")
    return data


def collect_errors() -> list[str]:
    errors: list[str] = []
    actual = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
    if actual != set(EXPECTED_REFERENCES):
        errors.append(f"skill namespace mismatch: {sorted(actual)}")

    for name, expected_refs in EXPECTED_REFERENCES.items():
        skill_dir = SKILLS_ROOT / name
        skill_md = skill_dir / "SKILL.md"
        metadata_path = skill_dir / "agents" / "openai.yaml"
        refs_dir = skill_dir / "references"

        for required in (skill_md, metadata_path, refs_dir):
            if not required.exists():
                errors.append(f"missing required path: {required.relative_to(ROOT)}")
        if not skill_md.is_file() or not metadata_path.is_file() or not refs_dir.is_dir():
            continue

        actual_refs = {path.name for path in refs_dir.iterdir() if path.is_file()}
        if actual_refs != expected_refs:
            errors.append(f"reference mismatch for {name}: {sorted(actual_refs)}")

        try:
            data = frontmatter(skill_md)
            if set(data) != {"name", "description"}:
                errors.append(f"frontmatter keys for {name}: {sorted(data)}")
            if data.get("name") != name:
                errors.append(f"frontmatter name mismatch for {name}")
            description = data.get("description")
            if not isinstance(description, str) or not description.startswith("Use when "):
                errors.append(f"description trigger invalid for {name}")
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))

        try:
            metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
            errors.extend(validate_skill_metadata(name, metadata))
        except yaml.YAMLError as exc:
            errors.append(f"metadata invalid for {name}: {exc}")

        for path in skill_dir.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml", ".json"}:
                continue
            text = path.read_text(encoding="utf-8")
            for marker in FORBIDDEN_MARKERS:
                if marker in text:
                    errors.append(f"unfinished marker {marker!r}: {path.relative_to(ROOT)}")
            for product in FOREIGN_PRODUCT_NAMES:
                if product in text:
                    errors.append(f"foreign product name {product!r}: {path.relative_to(ROOT)}")

        for target in MARKDOWN_LINK.findall(skill_md.read_text(encoding="utf-8")):
            if not target.startswith("references/"):
                continue
            if target.startswith("../"):
                errors.append(f"deep reference from {name}: {target}")
            elif not (skill_dir / target).is_file():
                errors.append(f"missing reference from {name}: {target}")
        errors.extend(
            validate_reference_routes(name, skill_md.read_text(encoding="utf-8"), expected_refs)
        )

    coverage_path = ROOT / "docs" / "source-coverage.md"
    if not coverage_path.is_file():
        errors.append("missing docs/source-coverage.md")
    else:
        coverage = coverage_path.read_text(encoding="utf-8")
        for part in range(1, 17):
            if f"Part {part}" not in coverage:
                errors.append(f"source coverage missing Part {part}")
        for appendix in "ABCD":
            if f"Appendix {appendix}" not in coverage:
                errors.append(f"source coverage missing Appendix {appendix}")

    navigation_path = SKILLS_ROOT / "ariadne-skill" / "references" / "source-navigation.json"
    try:
        navigation = json.loads(navigation_path.read_text(encoding="utf-8"))
        errors.extend(validate_source_navigation(navigation))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"source navigation invalid: {exc}")

    plan_path = ROOT / "docs" / "superpowers" / "plans" / "2026-08-03-ariadne-skill-implementation.md"
    readme_path = ROOT / "README.md"
    try:
        plan_status = extract_stage_status(plan_path.read_text(encoding="utf-8"))
        readme_status = extract_stage_status(readme_path.read_text(encoding="utf-8"))
        if plan_status != readme_status:
            errors.append("README and implementation plan stage status differ")
        errors.extend(validate_stage_status(plan_status))
    except OSError as exc:
        errors.append(f"execution stage status unavailable: {exc}")

    schema_path = ROOT / "schemas" / "method-record.schema.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
    except (OSError, json.JSONDecodeError, jsonschema.SchemaError) as exc:
        errors.append(f"method record schema invalid: {exc}")
    else:
        example_count = 0
        for path in SKILLS_ROOT.rglob("*.md"):
            try:
                records = extract_marked_method_records(path.read_text(encoding="utf-8"))
            except (OSError, ValueError, yaml.YAMLError) as exc:
                errors.append(f"Method Record example parse failed in {path.relative_to(ROOT)}: {exc}")
                continue
            for record in records:
                example_count += 1
                try:
                    validate_method_record(record, schema)
                except jsonschema.ValidationError as exc:
                    errors.append(
                        f"Method Record example invalid in {path.relative_to(ROOT)}: {exc.message}"
                    )
                    continue
                for error in validate_record_semantics(record):
                    errors.append(f"Method Record semantics invalid in {path.relative_to(ROOT)}: {error}")
        if example_count < 4:
            errors.append(f"expected at least 4 marked Method Record examples, found {example_count}")

    cards_path = SKILLS_ROOT / "ariadne-human" / "references" / "human-variable-cards.json"
    try:
        cards = json.loads(cards_path.read_text(encoding="utf-8"))
        expected_ids = [f"HV{index:02d}" for index in range(1, 12)]
        if len(cards["field_order"]) != 39:
            errors.append("human variable card field_order must contain 39 fields")
        if [card["id"] for card in cards["human_variables"]] != expected_ids:
            errors.append("human variable cards must cover HV01-HV11 in order")
        for card in cards["human_variables"]:
            if list(card) != cards["field_order"]:
                errors.append(f"human variable card field map is incomplete: {card.get('id')}")
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors.append(f"human variable cards invalid: {exc}")

    apps_path = SKILLS_ROOT / "ariadne-audit" / "references" / "application-contracts.json"
    try:
        apps = json.loads(apps_path.read_text(encoding="utf-8"))
        expected_ids = ["APP-REL", "APP-FAM", "APP-ORG", "APP-PLT", "APP-INS", "APP-OPI", "APP-SPC", "APP-EMG", "APP-ULS"]
        if [contract["id"] for contract in apps["contracts"]] != expected_ids:
            errors.append("application contracts must cover all nine Part 15 domains in order")
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors.append(f"application contracts invalid: {exc}")

    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        print("Ariadne repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Ariadne repository validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
