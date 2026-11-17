"""The single-file compiler includes only the declared guidance resources."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.architecture import load_architecture
from scripts.build_bundle import BUNDLE_PATH, PACKAGE_ROOT, SOURCE_URL, _anchor, build_bundle
from tests.test_architecture import make_package


def test_bundle_embeds_manifest_guidance_in_order_and_links_external_resources(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    for index, relative in enumerate(data["bundle"]):
        path = tmp_path / relative
        path.write_text(path.read_text(encoding="utf-8") + f"\nGUIDANCE_{index}\n", encoding="utf-8")
    (tmp_path / "references/kernel.md").write_text(
        "# Kernel\n\nGUIDANCE_1\n\n"
        "[Path](../paths/route-1.md)\n"
        "[Legacy](legacy/record.md)\n"
        "[Tool](../scripts/example.py)\n"
        "[Schema](../contracts/example.schema.json)\n",
        encoding="utf-8",
    )
    (tmp_path / "references/legacy/record.md").write_text("SECRET_LEGACY_BODY\n", encoding="utf-8")
    (tmp_path / "scripts/example.py").write_text("SECRET_EXECUTABLE_BODY\n", encoding="utf-8")
    generated = build_bundle(tmp_path)
    assert [generated.index(f"GUIDANCE_{index}") for index in range(len(data["bundle"]))] == sorted(
        generated.index(f"GUIDANCE_{index}") for index in range(len(data["bundle"]))
    )
    assert f"[Path](#{_anchor('paths/route-1.md')})" in generated
    for relative in ("references/legacy/record.md", "scripts/example.py", "contracts/example.schema.json"):
        assert SOURCE_URL + relative in generated
    assert "SECRET_LEGACY_BODY" not in generated
    assert "SECRET_EXECUTABLE_BODY" not in generated


def test_bundle_preserves_code_examples_and_removes_frontmatter(tmp_path: Path) -> None:
    make_package(tmp_path)
    entry = tmp_path / "SKILL.md"
    entry.write_text(
        "---\nname: ariadne-skill\n---\n# Ariadne\n\n"
        "[Resources](architecture.json)\n\n"
        "`[example](../not-a-real-resource.md)`\n\n"
        "```markdown\n# Unchanged code heading\n[example](../../outside.md)\n```\n",
        encoding="utf-8",
    )
    generated = build_bundle(tmp_path)
    assert "name: ariadne-skill" not in generated
    assert "## Ariadne" in generated
    assert "`[example](../not-a-real-resource.md)`" in generated
    assert "```markdown\n# Unchanged code heading\n[example](../../outside.md)\n```" in generated


def test_bundle_rejects_actual_links_outside_package(tmp_path: Path) -> None:
    make_package(tmp_path)
    entry = tmp_path / "SKILL.md"
    entry.write_text(entry.read_text(encoding="utf-8") + "\n[Outside](../outside.md)\n", encoding="utf-8")
    with pytest.raises(ValueError, match="link escapes package"):
        build_bundle(tmp_path)


def test_bundle_manifest_controls_guidance_order(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    first = build_bundle(tmp_path)
    data["bundle"][1], data["bundle"][2] = data["bundle"][2], data["bundle"][1]
    (tmp_path / "architecture.json").write_text(json.dumps(data) + "\n", encoding="utf-8")
    second = build_bundle(tmp_path)
    assert first != second
    assert second.index(f'<a id="{_anchor(data["bundle"][1])}"') < second.index(
        f'<a id="{_anchor(data["bundle"][2])}"'
    )


def test_committed_bundle_matches_current_manifest_selected_guidance() -> None:
    data = load_architecture(PACKAGE_ROOT)
    generated = build_bundle(PACKAGE_ROOT)
    assert BUNDLE_PATH.read_text(encoding="utf-8") == generated
    for relative in data["bundle"]:
        assert f'<a id="{_anchor(relative)}"></a>' in generated
    for relative in set(data["legacy"]) | set(data["library"]):
        assert f'<a id="{_anchor(relative)}"></a>' not in generated
