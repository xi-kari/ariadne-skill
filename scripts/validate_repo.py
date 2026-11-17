"""Validate the current package architecture and its optional legacy formats."""
from __future__ import annotations

import filecmp
import json
import re
import sys
import tempfile
from pathlib import Path

import jsonschema
import yaml

try:
    from .architecture import load_architecture, validate_architecture, package_path
    from .legacy_record import (
        CEILING_RANK, method_record_validator, validate_method_record,
        validate_record_semantics, extract_marked_method_records,
        extract_marked_method_record_lineages, claim_dependency_errors,
        scale_scope_errors, choice_payload_errors, strong_judgment_errors,
        methodology_extension_errors,
    )
except ImportError:
    from architecture import load_architecture, validate_architecture, package_path
    from legacy_record import (
        CEILING_RANK, method_record_validator, validate_method_record,
        validate_record_semantics, extract_marked_method_records,
        extract_marked_method_record_lineages, claim_dependency_errors,
        scale_scope_errors, choice_payload_errors, strong_judgment_errors,
        methodology_extension_errors,
    )

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
SKILL_ROOT = SKILLS_ROOT / "ariadne-skill"
SUPPORTED_RECORD_SCHEMA_VERSIONS = {"2.0", "2.1"}


def _resource_resolves(relative: object) -> bool:
    try:
        package_path(SKILL_ROOT, relative)
    except (OSError, ValueError, TypeError):
        return False
    return True


def _numbering_probe_resolves(code: str, owner: str) -> bool:
    probes = NUMBERING_PROBES.get(code)
    if probes is None or not _resource_resolves(owner):
        return False
    text = package_path(SKILL_ROOT, owner).read_text(encoding="utf-8")
    return any(probe in text for probe in probes)

REQUIRED_FRONTMATTER_KEYS = {"name", "description"}

SKILL_NAME_PATTERN = re.compile(r"[a-z][a-z0-9-]{0,63}")

DESCRIPTION_MAX_CHARS = 1024

NUMBERING_PROBES = {
    "D0-D3": ("D0",),
    "U01-U11": ("U01",),
    "G1-G4": ("G1",),
    "法1-法3": ("法1",),
    "F1-F6": ("F1",),
    "E1-E5": ("E1",),
    "C1-C12": ("C12",),
    "A/X/T/O/C/R/I/N/J": ("A,X,T,O,C,R,I,N,J", "A aggregation"),
    "M01-M09": ("M01",),
    "CM-*": ("CM-",),
    "H1-H6": ("H1",),
    "GC/GS/GE/CV/RS/IS/IM/IB": ("GC",),
    "HV01-HV11": ("HV01",),
    "S0-S6/X0": ("S0",),
    "IG1-IG7": ("IG1",),
    "SJ1-SJ8": ("SJ1",),
    "L1-L3": ("L1",),
    "TOOL-*": ("TOOL-*",),
    "N1-N5": ("N1",),
    "O1-O4": ("O1",),
    "PF-1-PF-10": ("PF-1",),
    "T0-T4": ("T0",),
    "APP-*": ("APP-",),
    "GOV-01-GOV-24": ("GOV-0",),
}

ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "metadata"}

FORBIDDEN_MARKERS = ("TODO", "TBD", "PLACEHOLDER", "implement later", "fill in details")

FOREIGN_PRODUCT_NAMES = ("CrossFrame", "world-structure")

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

EXPECTED_NUMBERING_SYSTEMS = {
    "D0-D3",
    "U01-U11",
    "G1-G4",
    "法1-法3",
    "F1-F6",
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
    "double_evidence_ban": {
        "dual_text_agreement",
        "independent_evidence_count",
        "shared_lineage",
    },
}

EXPECTED_C5_APPLICABILITY = {
    "kind": "conditional_proof_discipline",
    "admissible_output": ["testable_bridge_requirements", "bounded_candidate"],
    "prohibited_output": ["cross_domain_theorem", "empirical_transfer_without_conditions"],
}

EXPECTED_SOURCE_SHA256 = "6ef2e508474d4ac1ad07d7e4e068955342c405b5f680afcfc40d68cca3d0149c"

EXPECTED_DERIVED_STATUS = "derived_candidate_not_author_confirmed"

EXPECTED_GOVERNANCE_INVARIANTS = (
    "SHOU-1",
    "SHOU-2",
    "SHOU-3",
    "SHOU-4",
    "SHOU-5",
    "SHOU-6",
    "SHOU-7",
    "SHOU-8",
    "SHOU-9",
)

EXPECTED_KERNEL_LAYERS = (
    "definition",
    "common_method_constraint",
    "conditional_formal_proposition",
    "empirical_question_family",
    "result_and_mechanism_contract",
    "governance_invariant",
)

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
                continue
            if not _numbering_probe_resolves(entry["code"], entry["owner"]):
                errors.append(
                    "source navigation code does not resolve in its owner's files: "
                    f"{entry['code']} -> {entry['owner']}"
                )

    notation = data.get("shared_notation")
    if not isinstance(notation, list):
        errors.append("source navigation shared_notation must be a list")
    else:
        symbols = {entry.get("notation") for entry in notation if isinstance(entry, dict)}
        if symbols != EXPECTED_SHARED_NOTATION or len(notation) != len(EXPECTED_SHARED_NOTATION):
            errors.append("source navigation shared notation is incomplete or noncanonical")

    identity = data.get("source_identity")
    if not isinstance(identity, dict) or identity.get("sha256") != EXPECTED_SOURCE_SHA256:
        errors.append("source navigation must pin the source identity and SHA-256")
    elif identity.get("derived_status") != EXPECTED_DERIVED_STATUS:
        errors.append("source navigation must keep the derived-candidate status of Ariadne entries")

    invariants = data.get("governance_invariants")
    if not isinstance(invariants, list) or [
        entry.get("id") for entry in invariants if isinstance(entry, dict)
    ] != list(EXPECTED_GOVERNANCE_INVARIANTS):
        errors.append("source navigation must list the nine shared governance invariants in order")
    elif any(
        set(entry) != {"id", "rule"} or not isinstance(entry["rule"], str) or len(entry["rule"].strip()) < 30
        for entry in invariants
    ):
        errors.append("source navigation governance invariant entries are malformed")

    layers = data.get("shared_kernel_layers", {}).get("layers") if isinstance(
        data.get("shared_kernel_layers"), dict
    ) else None
    if not isinstance(layers, list) or [
        entry.get("layer") for entry in layers if isinstance(entry, dict)
    ] != list(EXPECTED_KERNEL_LAYERS):
        errors.append("source navigation shared kernel must list the six responsibility layers in order")

    appendix_c = data.get("appendix_c")
    if not isinstance(appendix_c, dict):
        return errors + ["source navigation appendix_c must be an object"]
    dual_text = appendix_c.get("dual_text_difference")
    if not isinstance(dual_text, dict):
        errors.append("source navigation C.4 dual_text_difference is missing")
    else:
        shared = set(dual_text.get("minimum_shared_semantics", []))
        shared_items = dual_text.get("minimum_shared_semantics", [])
        if shared != EXPECTED_SHARED_SEMANTICS or len(shared_items) != len(EXPECTED_SHARED_SEMANTICS):
            errors.append("source navigation C.4 minimum shared semantics are incomplete")
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
            errors.append("source navigation C.4 must retain both contract-system differences")
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
            errors.append("source navigation C.4 prohibited substitutions are incomplete")

    heuristic = appendix_c.get("cross_scale_proof_heuristic")
    if not isinstance(heuristic, dict):
        errors.append("source navigation C.5 cross_scale_proof_heuristic is missing")
    else:
        proof_fields = heuristic.get("required_fields", [])
        if set(proof_fields) != EXPECTED_PROOF_FIELDS or len(proof_fields) != len(EXPECTED_PROOF_FIELDS):
            errors.append("source navigation C.5 proof fields are incomplete")
        non_proof = heuristic.get("non_proof_boundaries", [])
        if set(non_proof) != EXPECTED_NON_PROOF_BOUNDARIES or len(non_proof) != len(EXPECTED_NON_PROOF_BOUNDARIES):
            errors.append("source navigation C.5 non-proof boundaries are incomplete")
        if not _resource_resolves(heuristic.get("execution_owner")):
            errors.append("source navigation C.5 must route to an installed resource")
        if heuristic.get("applicability") != EXPECTED_C5_APPLICABILITY:
            errors.append("source navigation C.5 applicability boundary is missing")

    atlas = data.get("appendix_d")
    if not isinstance(atlas, dict) or not _resource_resolves(atlas.get("owner")):
        errors.append("source navigation appendix_d must route to an installed resource")
    else:
        domains = atlas.get("domains")
        if not isinstance(domains, list) or [
            entry.get("code") for entry in domains if isinstance(entry, dict)
        ] != [f"D.{index:02d}" for index in range(1, 33)]:
            errors.append("source navigation appendix_d must list all 32 domain entries in order")
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
    if status["RELEASE"] != "complete":
        errors.append(
            "release stage must remain complete; it was authorized in the reviewed change of "
            "2026-08-26 (tag v1.0.0), and any further release-state change needs another reviewed change here"
        )
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

def validate_source_coverage(coverage: str) -> list[str]:
    errors: list[str] = []
    for part in range(1, 17):
        if f"| Part {part} -" not in coverage:
            errors.append(f"source coverage missing Part {part}")
    for appendix in "ABCD":
        if f"| Appendix {appendix} -" not in coverage:
            errors.append(f"source coverage missing Appendix {appendix}")
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

def validate_extension_contracts() -> list[str]:
    if __package__:
        from .build_site import build_site
        from .content_quality import validate_content
        from .validate_adapters import validate_adapters
    else:
        from build_site import build_site
        from content_quality import validate_content
        from validate_adapters import validate_adapters

    errors = validate_content(ROOT)
    errors.extend(validate_adapters(ROOT))
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            build_site(ROOT, Path(temp_dir) / "site")
    except (OSError, ValueError) as exc:
        errors.append(f"site-build: {exc}")
    return errors


def validate_legacy_formats() -> list[str]:
    """Keep old machine records readable without imposing them on current work."""
    errors: list[str] = []
    schema_path = ROOT / "schemas/method-record.schema.json"
    installed = SKILL_ROOT / "references/method-record.schema.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        versions = set(schema["properties"]["schema_version"].get("enum", []))
        if versions != SUPPORTED_RECORD_SCHEMA_VERSIONS:
            errors.append("legacy schema must continue accepting 2.0 and 2.1")
        if not filecmp.cmp(schema_path, installed, shallow=False):
            errors.append("installable legacy schema must be byte-identical to the root schema")
    except (OSError, KeyError, ValueError, jsonschema.SchemaError) as exc:
        return [f"legacy schema invalid: {exc}"]
    count = 0
    merges = 0
    for path in sorted((SKILL_ROOT / "references/legacy").glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
            singles = extract_marked_method_records(text)
            lineages = extract_marked_method_record_lineages(text)
            for record in singles:
                count += 1
                validate_method_record(record, schema)
                errors.extend(f"{path.name}: {error}" for error in validate_record_semantics(record))
            for records in lineages:
                for index, record in enumerate(records):
                    context = [other for position, other in enumerate(records) if position != index]
                    merges += record.get("lineage_kind") == "merge"
                    validate_method_record(record, schema)
                    errors.extend(f"{path.name}: {error}" for error in validate_record_semantics(record, context))
        except (OSError, ValueError, yaml.YAMLError, jsonschema.ValidationError) as exc:
            errors.append(f"legacy example invalid in {path.name}: {exc}")
    if count < 4 or merges < 1:
        errors.append("legacy compatibility must retain four record examples and a merge lineage")
    return errors


def validate_library_registers() -> list[str]:
    errors: list[str] = []
    library = SKILL_ROOT / "references/library"
    try:
        cards = json.loads((library / "human-variable-cards.json").read_text(encoding="utf-8"))
        if len(cards["field_order"]) != 39:
            errors.append("human variable cards must retain the 39-field source map")
        if [item["id"] for item in cards["human_variables"]] != [f"HV{index:02d}" for index in range(1, 12)]:
            errors.append("human variable cards must cover HV01-HV11 in order")
        if any(list(card) != cards["field_order"] for card in cards["human_variables"]):
            errors.append("human variable card field map is incomplete")
        apps = json.loads((library / "application-contracts.json").read_text(encoding="utf-8"))
        expected = ["APP-REL", "APP-FAM", "APP-ORG", "APP-PLT", "APP-INS", "APP-OPI", "APP-SPC", "APP-EMG", "APP-ULS"]
        if [item["id"] for item in apps["contracts"]] != expected:
            errors.append("application contracts must cover all nine Part 15 domains in order")
    except (OSError, KeyError, TypeError, ValueError) as exc:
        errors.append(f"library registers invalid: {exc}")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    actual = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
    if actual != {"ariadne-skill"}:
        errors.append(f"the installation must expose one Ariadne entry: {sorted(actual)}")
    try:
        architecture = load_architecture(SKILL_ROOT)
        errors.extend(validate_architecture(architecture, SKILL_ROOT))
        navigation = json.loads(package_path(SKILL_ROOT, architecture["source"]).read_text(encoding="utf-8"))
        errors.extend(validate_source_navigation(navigation))
        for contract in architecture["contracts"]:
            schema = json.loads(package_path(SKILL_ROOT, contract["schema"]).read_text(encoding="utf-8"))
            jsonschema.Draft202012Validator.check_schema(schema)
    except (OSError, KeyError, TypeError, ValueError, jsonschema.SchemaError) as exc:
        errors.append(f"package architecture invalid: {exc}")
    try:
        entry = package_path(SKILL_ROOT, "SKILL.md")
        data = frontmatter(entry)
        if not REQUIRED_FRONTMATTER_KEYS <= set(data) or set(data) - ALLOWED_FRONTMATTER_KEYS:
            errors.append("entry frontmatter keys are invalid")
        if data.get("name") != "ariadne-skill":
            errors.append("entry name must remain ariadne-skill")
        description = data.get("description")
        if not isinstance(description, str) or not description.strip() or len(description) > DESCRIPTION_MAX_CHARS:
            errors.append("entry description must be nonempty and at most 1024 characters")
        metadata = yaml.safe_load(package_path(SKILL_ROOT, "agents/openai.yaml").read_text(encoding="utf-8"))
        errors.extend(validate_skill_metadata("ariadne-skill", metadata))
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f"entry metadata invalid: {exc}")
    for path in SKILL_ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml", ".json"}:
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                errors.append(f"unreadable installation resource {path.relative_to(ROOT)}: {exc}")
                continue
            for marker in (*FORBIDDEN_MARKERS, *FOREIGN_PRODUCT_NAMES):
                if marker in text:
                    errors.append(f"invalid installation marker {marker!r}: {path.relative_to(ROOT)}")
    try:
        errors.extend(validate_source_coverage((ROOT / "docs/source-coverage.md").read_text(encoding="utf-8")))
        # This is an archived release decision, not the current task's workflow.
        history = ROOT / "docs/superpowers/plans/2026-08-03-ariadne-skill-implementation.md"
        errors.extend(validate_stage_status(extract_stage_status(history.read_text(encoding="utf-8"))))
    except OSError as exc:
        errors.append(f"source coverage or release history unavailable: {exc}")
    errors.extend(validate_legacy_formats())
    errors.extend(validate_library_registers())
    errors.extend(validate_extension_contracts())
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
