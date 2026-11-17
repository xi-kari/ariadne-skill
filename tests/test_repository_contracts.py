from __future__ import annotations

import re
from pathlib import Path

import yaml

from scripts.validate_repo import (
    ALLOWED_FRONTMATTER_KEYS,
    FORBIDDEN_MARKERS,
    FOREIGN_PRODUCT_NAMES,
    REQUIRED_FRONTMATTER_KEYS,
    validate_source_coverage,
)


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
PACKAGE_ROOT = SKILLS_ROOT / "ariadne-skill"

SCANNED_SUFFIXES = {".md", ".yaml", ".yml", ".json"}


def load_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    assert match, f"missing YAML frontmatter: {path}"
    data = yaml.safe_load(match.group(1))
    assert isinstance(data, dict)
    return data


def test_exact_skill_namespace_exists() -> None:
    actual = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
    assert actual == {"ariadne-skill"}


def test_complete_package_resources_are_declared_and_available() -> None:
    from scripts.architecture import load_architecture, validate_architecture

    manifest = load_architecture(PACKAGE_ROOT)
    assert manifest["identity"]["installable_skill"] == PACKAGE_ROOT.name
    assert (PACKAGE_ROOT / manifest["entry"]).is_file()
    assert (PACKAGE_ROOT / "agents" / "openai.yaml").is_file()
    assert validate_architecture(manifest, PACKAGE_ROOT, check_files=True) == []


def test_frontmatter_is_discoverable_and_matches_folder() -> None:
    data = load_frontmatter(PACKAGE_ROOT / "SKILL.md")
    assert REQUIRED_FRONTMATTER_KEYS <= set(data)
    assert not set(data) - ALLOWED_FRONTMATTER_KEYS
    assert data["name"] == PACKAGE_ROOT.name
    assert isinstance(data["description"], str)
    assert data["description"].strip()
    assert len(data["description"]) <= 1024


def test_openai_metadata_enables_global_discovery_and_local_explicit_prompt() -> None:
    path = PACKAGE_ROOT / "agents" / "openai.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert data["policy"]["allow_implicit_invocation"] is True
    interface = data["interface"]
    assert 25 <= len(interface["short_description"]) <= 64
    assert f"${PACKAGE_ROOT.name}" in interface["default_prompt"]


def test_installable_files_have_no_unfinished_or_foreign_product_text() -> None:
    for path in SKILLS_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in SCANNED_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in FORBIDDEN_MARKERS:
            assert marker not in text, f"{marker!r} in {path}"
        for product in FOREIGN_PRODUCT_NAMES:
            assert product not in text, f"foreign dependency name {product!r} in {path}"


def test_appendix_a_cards_are_complete_one_to_one_maps() -> None:
    import json

    path = SKILLS_ROOT / "ariadne-skill" / "references" / "library" / "human-variable-cards.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    fields = data["field_order"]
    assert len(fields) == 39
    assert [card["id"] for card in data["human_variables"]] == [
        f"HV{index:02d}" for index in range(1, 12)
    ]
    for card in data["human_variables"]:
        assert list(card) == fields
        assert card["conditional_support_routes"]
        for route in card["conditional_support_routes"]:
            assert set(route) == {
                "route_id",
                "claim_level",
                "when",
                "additional_inferential_requires",
                "additional_protocol_requires",
                "allowed_conclusion",
                "result_ceiling",
            }


def test_part_15_application_contracts_cover_all_domains_and_boundaries() -> None:
    import json

    path = SKILLS_ROOT / "ariadne-skill" / "references" / "library" / "application-contracts.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert [contract["id"] for contract in data["contracts"]] == [
        "APP-REL",
        "APP-FAM",
        "APP-ORG",
        "APP-PLT",
        "APP-INS",
        "APP-OPI",
        "APP-SPC",
        "APP-EMG",
        "APP-ULS",
    ]
    required = {
        "id",
        "object_and_method",
        "protected_positions",
        "evidence_scope",
        "allowed_output",
        "prohibited_leap_or_action",
        "stop_or_failure_boundary",
        "next_handoff",
    }
    for contract in data["contracts"]:
        assert set(contract) == required
        assert all(contract[field] for field in required - {"id"})


def test_source_coverage_maps_all_parts_and_appendices() -> None:
    text = (ROOT / "docs" / "source-coverage.md").read_text(encoding="utf-8")
    assert validate_source_coverage(text) == []

    dropped_part_one = text.replace("| Part 1 -", "| Part 99 -", 1)
    assert "source coverage missing Part 1" in validate_source_coverage(dropped_part_one)

    dropped_appendix = text.replace("| Appendix A -", "| Appendix Z -", 1)
    assert "source coverage missing Appendix A" in validate_source_coverage(dropped_appendix)
