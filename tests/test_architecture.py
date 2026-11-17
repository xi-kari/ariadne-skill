"""The installable package is complete without fixing its internal route count."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from scripts.architecture import (
    PACKAGE_ROOT,
    declared_resources,
    load_architecture,
    package_path,
    validate_architecture,
)


def make_package(root: Path, *, route_count: int = 2) -> dict:
    """Create a small, complete package with real files and navigable resources."""
    routes = [
        {
            "id": f"route-{index}",
            "name": f"Fixture path {index}",
            "path": f"paths/route-{index}.md",
            "result_types": ["bounded_answer"],
        }
        for index in range(1, route_count + 1)
    ]
    data = {
        "format_version": "1.0",
        "identity": {
            "name": "Ariadne",
            "kernel": "Lattice Kernel",
            "installable_skill": "ariadne-skill",
        },
        "entry": "SKILL.md",
        "source": "references/source.json",
        "routes": routes,
        "shared": ["references/kernel.md"],
        "library": ["references/source.json"],
        "legacy": ["references/legacy/record.md"],
        "contracts": [
            {
                "id": "example",
                "guide": "contracts/example.md",
                "schema": "contracts/example.schema.json",
                "tool": "scripts/example.py",
                "required_when": "Only for this explicitly selected fixture contract.",
            }
        ],
        "bundle": [
            "SKILL.md",
            "references/kernel.md",
            *[route["path"] for route in routes],
            "contracts/example.md",
        ],
        "composition_rule": "Combine only the paths needed by the question.",
        "record_rule": "Use prose unless a particular record is needed.",
    }
    for relative in declared_resources(data):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".json":
            text = '{"fixture": "resource used only by architecture tests"}\n'
        else:
            text = "# Fixture resource\n\nA complete resource for this isolated package.\n"
        path.write_text(text, encoding="utf-8")
    (root / "SKILL.md").write_text(
        "# Ariadne\n\n[Package resources](architecture.json)\n", encoding="utf-8"
    )
    (root / "agents").mkdir()
    (root / "agents/openai.yaml").write_text(
        "interface:\n  display_name: Ariadne\n", encoding="utf-8"
    )
    (root / "architecture.json").write_text(
        json.dumps(data, indent=2) + "\n", encoding="utf-8"
    )
    assert validate_architecture(data, root, check_files=True) == []
    return data


def test_current_package_manifest_contains_every_installed_resource() -> None:
    data = load_architecture(PACKAGE_ROOT)
    assert validate_architecture(data, PACKAGE_ROOT, check_files=True) == []
    assert package_path(PACKAGE_ROOT, data["entry"]).is_file()
    assert len(declared_resources(data)) == len(set(declared_resources(data)))


@pytest.mark.parametrize("field,value", [("source", {}), ("source", []), ("shared", None)])
def test_malformed_manifest_fields_return_diagnostics(tmp_path: Path, field: str, value: object) -> None:
    data = make_package(tmp_path)
    data[field] = value
    assert validate_architecture(data, tmp_path)


def test_manifest_symlink_is_rejected_before_loading(tmp_path: Path) -> None:
    root = tmp_path / "package"
    make_package(root)
    manifest = root / "architecture.json"
    external = tmp_path / "external.json"
    shutil.move(manifest, external)
    try:
        manifest.symlink_to(external)
    except OSError as error:
        pytest.skip(f"file symlink creation is unavailable: {error}")
    with pytest.raises(ValueError, match="symlinked package resource"):
        load_architecture(root)


@pytest.mark.parametrize("relative", ["agents/openai.yaml", "unregistered-directory"])
def test_unlisted_or_metadata_symlinks_cannot_enter_the_installation(tmp_path: Path, relative: str) -> None:
    root = tmp_path / "package"
    data = make_package(root)
    link = root / relative
    external = tmp_path / "outside"
    if link.is_file():
        shutil.move(link, external)
    else:
        external.mkdir()
    try:
        link.symlink_to(external, target_is_directory=external.is_dir())
    except OSError as error:
        pytest.skip(f"symlink creation is unavailable: {error}")
    assert any("symlinked package resource" in error for error in validate_architecture(data, root))


@pytest.mark.parametrize("route_count", [1, 3, 7])
def test_route_counts_can_change_without_changing_the_package_contract(tmp_path: Path, route_count: int) -> None:
    data = make_package(tmp_path, route_count=route_count)
    assert load_architecture(tmp_path) == data
    assert len(data["routes"]) == route_count
    assert validate_architecture(data, tmp_path, check_files=True) == []


def test_duplicate_route_identity_is_rejected_even_with_distinct_files(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    data["routes"][1]["id"] = data["routes"][0]["id"]
    assert "architecture route IDs must be unique" in validate_architecture(data, tmp_path)


def test_one_resource_cannot_have_two_owners(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    data["library"].append(data["shared"][0])
    assert "architecture resource ownership must be unique" in validate_architecture(data, tmp_path)


def test_missing_declared_resource_is_rejected(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    (tmp_path / data["source"]).unlink()
    errors = validate_architecture(data, tmp_path)
    assert f"missing package resource: {data['source']}" in errors


def test_unregistered_installed_file_is_rejected(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    (tmp_path / "unregistered.md").write_text("An undeclared instruction.\n", encoding="utf-8")
    assert "unregistered package resource: unregistered.md" in validate_architecture(data, tmp_path)


@pytest.mark.parametrize("relative", ["../outside.md", "/outside.md", "C:/outside.md", "references\\source.json"])
def test_package_paths_reject_escape_and_platform_ambiguity(tmp_path: Path, relative: str) -> None:
    with pytest.raises(ValueError, match="unsafe package resource"):
        package_path(tmp_path, relative, must_exist=False)


@pytest.mark.parametrize("relative", ["../outside.md", "/outside.md"])
def test_manifest_cannot_declare_a_resource_outside_the_package(tmp_path: Path, relative: str) -> None:
    data = make_package(tmp_path)
    old = data["shared"][0]
    data["shared"][0] = relative
    data["bundle"][data["bundle"].index(old)] = relative
    assert any("unsafe package resource" in error for error in validate_architecture(data, tmp_path))


def test_declared_source_file_symlink_is_rejected(tmp_path: Path) -> None:
    root = tmp_path / "package"
    data = make_package(root)
    source = root / data["source"]
    external = tmp_path / "external-source.json"
    external.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    source.unlink()
    try:
        source.symlink_to(external)
    except OSError as error:
        pytest.skip(f"file symlink creation is unavailable: {error}")
    assert f"symlinked package resource: {data['source']}" in validate_architecture(data, root)


def test_declared_resource_cannot_pass_through_a_directory_symlink(tmp_path: Path) -> None:
    root = tmp_path / "package"
    data = make_package(root)
    external = tmp_path / "external-references"
    shutil.move(root / "references", external)
    try:
        (root / "references").symlink_to(external, target_is_directory=True)
    except OSError as error:
        pytest.skip(f"directory symlink creation is unavailable: {error}")
    assert f"symlinked package resource: {data['source']}" in validate_architecture(data, root)


@pytest.mark.parametrize(
    "missing",
    ["SKILL.md", "references/kernel.md", "paths/route-1.md", "contracts/example.md"],
    ids=["entry", "shared", "route", "contract-guide"],
)
def test_bundle_cannot_omit_a_required_guidance_resource(tmp_path: Path, missing: str) -> None:
    data = make_package(tmp_path)
    data["bundle"].remove(missing)
    assert (
        "architecture bundle must include entry, shared resources, paths, and contract guides"
        in validate_architecture(data, tmp_path)
    )


def test_bundle_cannot_include_undeclared_guidance(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    data["bundle"].append("undeclared.md")
    assert "architecture bundle includes an undeclared resource" in validate_architecture(data, tmp_path)


def test_bundle_cannot_repeat_a_resource(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    data["bundle"].append(data["shared"][0])
    assert "architecture bundle resources must be unique" in validate_architecture(data, tmp_path)


def test_entry_can_reach_deep_resources_through_an_explicit_index(tmp_path: Path) -> None:
    data = make_package(tmp_path)
    (tmp_path / "SKILL.md").write_text(
        "# Ariadne\n\n[Shared method](references/kernel.md)\n", encoding="utf-8"
    )
    (tmp_path / "references/kernel.md").write_text(
        "# Shared method\n\n[Resource index](../architecture.json)\n", encoding="utf-8"
    )
    assert validate_architecture(data, tmp_path) == []


@pytest.mark.parametrize(
    "false_link",
    ["```markdown\n[Resources](architecture.json)\n```", "`[Resources](architecture.json)`"],
    ids=["fenced-example", "inline-code"],
)
def test_code_examples_do_not_establish_resource_reachability(tmp_path: Path, false_link: str) -> None:
    data = make_package(tmp_path)
    (tmp_path / "SKILL.md").write_text("# Ariadne\n\n" + false_link + "\n", encoding="utf-8")
    errors = validate_architecture(data, tmp_path)
    assert f"package resource is unreachable from entry: {data['source']}" in errors
    assert f"package resource is unreachable from entry: {data['routes'][0]['path']}" in errors
