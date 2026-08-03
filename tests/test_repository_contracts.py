from __future__ import annotations

import re
from pathlib import Path

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


def load_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    assert match, f"missing YAML frontmatter: {path}"
    data = yaml.safe_load(match.group(1))
    assert isinstance(data, dict)
    return data


def test_exact_skill_namespace_exists() -> None:
    actual = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
    assert actual == set(EXPECTED_REFERENCES)


def test_each_skill_has_required_files_and_references() -> None:
    for name, references in EXPECTED_REFERENCES.items():
        skill_dir = SKILLS_ROOT / name
        assert (skill_dir / "SKILL.md").is_file()
        assert (skill_dir / "agents" / "openai.yaml").is_file()
        actual_refs = {
            path.name for path in (skill_dir / "references").iterdir() if path.is_file()
        }
        assert actual_refs == references, name


def test_frontmatter_is_discoverable_and_matches_folder() -> None:
    for name in EXPECTED_REFERENCES:
        data = load_frontmatter(SKILLS_ROOT / name / "SKILL.md")
        assert set(data) == {"name", "description"}
        assert data["name"] == name
        assert isinstance(data["description"], str)
        assert data["description"].startswith("Use when ")
        assert len(data["description"]) <= 1024


def test_openai_metadata_enables_global_discovery_and_local_explicit_prompt() -> None:
    for name in EXPECTED_REFERENCES:
        path = SKILLS_ROOT / name / "agents" / "openai.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert data["policy"]["allow_implicit_invocation"] is True
        interface = data["interface"]
        assert 25 <= len(interface["short_description"]) <= 64
        assert f"${name}" in interface["default_prompt"]


def test_installable_files_have_no_unfinished_or_foreign_product_text() -> None:
    for path in SKILLS_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in FORBIDDEN_MARKERS:
            assert marker not in text, f"{marker!r} in {path}"
        for product in FOREIGN_PRODUCT_NAMES:
            assert product not in text, f"foreign dependency name {product!r} in {path}"


def test_skill_reference_links_are_one_level_and_resolve() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
    for name in EXPECTED_REFERENCES:
        skill_md = SKILLS_ROOT / name / "SKILL.md"
        for target in link_pattern.findall(skill_md.read_text(encoding="utf-8")):
            assert not target.startswith("../"), f"deep reference in {skill_md}: {target}"
            assert (skill_md.parent / target).is_file(), f"missing link target: {target}"


def test_source_coverage_maps_all_parts_and_appendices() -> None:
    text = (ROOT / "docs" / "source-coverage.md").read_text(encoding="utf-8")
    for part in range(1, 17):
        assert f"Part {part}" in text
    for appendix in "ABCD":
        assert f"Appendix {appendix}" in text

