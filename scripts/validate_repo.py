from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

EXPECTED_REFERENCES = {
    "ariadne-skill": {"lattice-kernel.md", "routing.md", "method-record.md"},
    "ariadne-framing": {"object-contract.md"},
    "ariadne-evidence": {"evidence-contracts.md"},
    "ariadne-scale": {"scale-transformations.md"},
    "ariadne-mechanism": {"mechanism-contracts.md"},
    "ariadne-human": {"human-domain.md"},
    "ariadne-dynamics": {"dynamic-derivation.md"},
    "ariadne-forecast": {"forecast-contract.md"},
    "ariadne-choice": {"choice-and-authorization.md"},
    "ariadne-audit": {"gates-and-governance.md"},
}

FORBIDDEN_MARKERS = ("TODO", "TBD", "PLACEHOLDER", "implement later", "fill in details")
FOREIGN_PRODUCT_NAMES = ("CrossFrame", "world-structure")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


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
            interface = metadata["interface"]
            if metadata.get("policy", {}).get("allow_implicit_invocation") is not True:
                errors.append(f"implicit invocation disabled or absent for {name}")
            short = interface["short_description"]
            if not 25 <= len(short) <= 64:
                errors.append(f"short_description length invalid for {name}: {len(short)}")
            if f"${name}" not in interface["default_prompt"]:
                errors.append(f"default_prompt does not invoke ${name}")
        except (KeyError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"metadata invalid for {name}: {exc}")

        for path in skill_dir.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml"}:
                continue
            text = path.read_text(encoding="utf-8")
            for marker in FORBIDDEN_MARKERS:
                if marker in text:
                    errors.append(f"unfinished marker {marker!r}: {path.relative_to(ROOT)}")
            for product in FOREIGN_PRODUCT_NAMES:
                if product in text:
                    errors.append(f"foreign product name {product!r}: {path.relative_to(ROOT)}")

        for target in MARKDOWN_LINK.findall(skill_md.read_text(encoding="utf-8")):
            if not target.endswith(".md"):
                continue
            if target.startswith("../"):
                errors.append(f"deep reference from {name}: {target}")
            elif not (skill_dir / target).is_file():
                errors.append(f"missing reference from {name}: {target}")

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

    schema_path = ROOT / "schemas" / "method-record.schema.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
    except (OSError, json.JSONDecodeError, jsonschema.SchemaError) as exc:
        errors.append(f"method record schema invalid: {exc}")

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
