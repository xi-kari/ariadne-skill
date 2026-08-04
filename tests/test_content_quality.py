from __future__ import annotations

import importlib
import importlib.util
from pathlib import Path


def _validator():
    name = "scripts.content_quality"
    spec = importlib.util.find_spec(name)
    assert spec is not None, f"missing production module: {name}"
    return importlib.import_module(name).validate_content


def _codes(root: Path) -> set[str]:
    return {error.split(":", maxsplit=1)[0] for error in _validator()(root)}


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
