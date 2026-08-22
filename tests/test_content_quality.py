from __future__ import annotations

import importlib
import importlib.util
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _validator():
    name = "scripts.content_quality"
    spec = importlib.util.find_spec(name)
    assert spec is not None, f"missing production module: {name}"
    return importlib.import_module(name).validate_content


def _codes(root: Path) -> set[str]:
    return {error.split(":", maxsplit=1)[0] for error in _validator()(root)}


def _method_guard():
    name = "scripts.content_quality"
    spec = importlib.util.find_spec(name)
    assert spec is not None, f"missing production module: {name}"
    return importlib.import_module(name).validate_method_content


def _method_codes(root: Path) -> set[str]:
    return {error.split(":", maxsplit=1)[0] for error in _method_guard()(root)}


def _copied_skills_sandbox(tmp_path: Path) -> Path:
    sandbox = tmp_path / "repository"
    shutil.copytree(ROOT / "skills", sandbox / "skills")
    return sandbox


def test_missing_relative_target_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("[missing](docs/missing.md)\n", encoding="utf-8")
    assert "missing-target" in _codes(tmp_path)


def test_missing_explicit_anchor_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("[jump](guide.md#missing)\n", encoding="utf-8")
    (tmp_path / "guide.md").write_text("# Existing\n", encoding="utf-8")
    assert "missing-anchor" in _codes(tmp_path)


def test_markdown_code_links_are_not_treated_as_navigation(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        "```markdown\n[example](missing.md)\n```\n`[inline](also-missing.md)`\n",
        encoding="utf-8",
    )
    assert _validator()(tmp_path) == []


def test_markdown_reference_and_raw_html_navigation_are_validated_outside_fences(
    tmp_path: Path,
) -> None:
    """Catches link validation that misses reference definitions or parses a short fence close."""
    (tmp_path / "README.md").write_text(
        "````markdown\n"
        "[hidden](missing.md)\n"
        "<a id=\"hidden\"></a>\n"
        "```\n"
        "````\n"
        "[guide][guide-ref]\n"
        "[guide-ref]: guide.md#missing\n"
        "<a href=\"../outside.md\">outside</a>\n"
        "[directory](docs/)\n"
        "[unreadable](broken.md#section)\n",
        encoding="utf-8",
    )
    (tmp_path / "guide.md").write_text("# Existing\n", encoding="utf-8")
    (tmp_path / "docs").mkdir()
    (tmp_path / "broken.md").write_bytes(b"\xff\xfe")

    codes = _codes(tmp_path)
    assert {"missing-anchor", "path-escape", "directory-target", "unreadable-target"} <= codes
    assert "missing-target" not in codes


def test_invalid_svg_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "broken.svg").write_text("<svg><title>Broken</svg>\n", encoding="utf-8")
    assert "invalid-svg" in _codes(tmp_path)


def test_svg_without_accessible_text_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "silent.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"></svg>\n',
        encoding="utf-8",
    )
    assert "missing-svg-accessibility" in _codes(tmp_path)


def test_external_runtime_asset_is_rejected_but_anchor_is_allowed(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text(
        '<!doctype html><html lang="zh-CN"><head>'
        '<script src="https://cdn.example/app.js"></script></head>'
        '<body><a href="https://example.com/docs">Docs</a></body></html>\n',
        encoding="utf-8",
    )
    assert "external-runtime-asset" in _codes(tmp_path)


def test_external_runtime_urls_are_rejected_in_all_asset_reference_surfaces(tmp_path: Path) -> None:
    """Catches runtime checks that inspect only the first HTML source or omit SVG script imports."""
    (tmp_path / "index.html").write_text(
        '<style>@import "https://cdn.example/inline.css";</style>'
        '<img srcset="local.svg 1x, https://cdn.example/image.svg 2x" alt="example">\n',
        encoding="utf-8",
    )
    (tmp_path / "local.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" aria-label="local"></svg>\n',
        encoding="utf-8",
    )
    (tmp_path / "site.css").write_text(
        '@import url("https://cdn.example/theme.css");\n', encoding="utf-8"
    )
    (tmp_path / "runtime.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" aria-label="runtime">'
        '<script>import "https://cdn.example/runtime.js"</script></svg>\n',
        encoding="utf-8",
    )
    (tmp_path / "not-svg.svg").write_text("<html><title>wrong root</title></html>\n", encoding="utf-8")
    (tmp_path / "nested-title.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg"><g><title>nested</title></g></svg>\n',
        encoding="utf-8",
    )

    errors = _validator()(tmp_path)
    assert "external-runtime-asset" in _codes(tmp_path)
    assert any("https://cdn.example/inline.css" in error for error in errors)
    assert any("svg[script] -> https://cdn.example/runtime.js" in error for error in errors)
    assert "invalid-svg-root" in _codes(tmp_path)
    assert "missing-svg-accessibility" in _codes(tmp_path)


def test_generated_site_asset_resolves_to_shared_source(tmp_path: Path) -> None:
    (tmp_path / "site").mkdir()
    (tmp_path / "docs" / "assets").mkdir(parents=True)
    (tmp_path / "site" / "index.html").write_text(
        '<!doctype html><html lang="zh-CN"><body>'
        '<img src="assets/lattice-kernel-map.svg" alt="方法图">'
        "</body></html>\n",
        encoding="utf-8",
    )
    (tmp_path / "docs" / "assets" / "lattice-kernel-map.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg"><title>方法图</title></svg>\n',
        encoding="utf-8",
    )
    assert _validator()(tmp_path) == []


def test_link_that_escapes_repository_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("[outside](../outside.md)\n", encoding="utf-8")
    assert "path-escape" in _codes(tmp_path)


def test_invalid_utf8_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_bytes(b"\xff\xfe")
    assert "invalid-utf8" in _codes(tmp_path)


def test_invalid_utf8_extensionless_contract_file_is_rejected(tmp_path: Path) -> None:
    """Catches text-quality scanning that silently skips a tracked extensionless contract."""
    (tmp_path / "contract").write_bytes(b"\xff\xfe")
    assert "invalid-utf8" in _codes(tmp_path)


def test_trailing_whitespace_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("trailing  \n", encoding="utf-8")
    assert "trailing-whitespace" in _codes(tmp_path)


def test_missing_final_newline_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("no newline", encoding="utf-8")
    assert "missing-final-newline" in _codes(tmp_path)


def test_repository_method_content_satisfies_its_own_floors() -> None:
    assert _method_guard()(ROOT) == []


def test_hollowed_reference_method_text_is_rejected(tmp_path: Path) -> None:
    """Catches the degradation probe that keeps headings while gutting method text."""
    sandbox = _copied_skills_sandbox(tmp_path)
    target = sandbox / "skills" / "ariadne-mechanism" / "references" / "mechanism-contracts.md"
    headings_only = "\n".join(
        line for line in target.read_text(encoding="utf-8").splitlines() if line.startswith("#")
    )
    target.write_text(headings_only + "\n", encoding="utf-8")

    codes = _method_codes(sandbox)
    assert "reference-below-floor" in codes
    assert "thin-h2-section" in codes


def test_stubbed_skill_body_is_rejected(tmp_path: Path) -> None:
    """Catches a SKILL.md body replaced by a stub while frontmatter stays valid."""
    sandbox = _copied_skills_sandbox(tmp_path)
    target = sandbox / "skills" / "ariadne-mechanism" / "SKILL.md"
    text = target.read_text(encoding="utf-8")
    frontmatter_end = text.index("\n---", 3) + len("\n---")
    target.write_text(text[:frontmatter_end] + "\n\nStub body.\n", encoding="utf-8")

    codes = _method_codes(sandbox)
    assert "skill-body-below-floor" in codes
    assert "skill-body-missing-sections" in codes


def test_single_character_card_values_are_rejected(tmp_path: Path) -> None:
    """Catches the degradation probe that rewrites card values while keeping key shape."""
    sandbox = _copied_skills_sandbox(tmp_path)
    cards_path = sandbox / "skills" / "ariadne-human" / "references" / "human-variable-cards.json"
    cards = json.loads(cards_path.read_text(encoding="utf-8"))

    def degrade(node: object) -> object:
        if isinstance(node, dict):
            return {key: degrade(value) for key, value in node.items()}
        if isinstance(node, list):
            return [degrade(value) for value in node]
        if isinstance(node, str):
            return "x"
        return node

    cards["human_variables"] = degrade(cards["human_variables"])
    cards_path.write_text(json.dumps(cards, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    codes = _method_codes(sandbox)
    assert "card-value-too-short" in codes
    assert "card-below-floor" in codes


def test_malformed_state_prototype_register_is_rejected(tmp_path: Path) -> None:
    sandbox = tmp_path / "repository"
    references = sandbox / "skills" / "ariadne-human" / "references"
    references.mkdir(parents=True)
    (references / "state-prototypes.json").write_text(
        json.dumps({"prototypes": [{"id": "S0"}], "nonlinear_paths": []}) + "\n",
        encoding="utf-8",
    )
    assert "card-structure" in _method_codes(sandbox)


def test_malformed_intervention_level_register_is_rejected(tmp_path: Path) -> None:
    sandbox = tmp_path / "repository"
    references = sandbox / "skills" / "ariadne-choice" / "references"
    references.mkdir(parents=True)
    (references / "intervention-levels.json").write_text(
        json.dumps({"levels": [{"id": "T0"}, {"id": "T9"}]}) + "\n",
        encoding="utf-8",
    )
    assert "card-structure" in _method_codes(sandbox)


def test_non_object_card_register_is_rejected(tmp_path: Path) -> None:
    """Catches the degradation probe that replaces a whole card register with []."""
    sandbox = tmp_path / "repository"
    human_references = sandbox / "skills" / "ariadne-human" / "references"
    choice_references = sandbox / "skills" / "ariadne-choice" / "references"
    human_references.mkdir(parents=True)
    choice_references.mkdir(parents=True)
    (human_references / "state-prototypes.json").write_text("[]\n", encoding="utf-8")
    (choice_references / "intervention-levels.json").write_text("[]\n", encoding="utf-8")

    errors = _method_guard()(sandbox)
    hits = [error for error in errors if "top-level value must be a JSON object" in error]
    assert len(hits) == 2
