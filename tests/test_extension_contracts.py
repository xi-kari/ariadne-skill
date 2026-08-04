from __future__ import annotations

import importlib
import importlib.util
import json
import re
import shutil
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_SKILLS = {
    "ariadne-skill",
    "ariadne-framing",
    "ariadne-evidence",
    "ariadne-scale",
    "ariadne-mechanism",
    "ariadne-human",
    "ariadne-dynamics",
    "ariadne-forecast",
    "ariadne-choice",
    "ariadne-audit",
}
EXPECTED_HOSTS = {
    "codex",
    "claude-code",
    "gemini-cli",
    "cursor",
    "github-copilot",
    "reasonix",
}
EXPECTED_SITE_FILES = {
    "index.html",
    "404.html",
    "assets/site.css",
    "assets/site.js",
    "assets/favicon.svg",
    "assets/og-cover.svg",
    "assets/readme-hero.svg",
    "assets/lattice-kernel-map.svg",
}
REQUIRED_DELIVERY_FILES = {
    "LICENSE",
    "requirements-dev.txt",
    ".editorconfig",
    ".gitattributes",
    ".github/workflows/validate-and-deploy.yml",
    ".github/dependabot.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/methodology.yml",
    ".github/pull_request_template.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
}


def _load_module(name: str):
    spec = importlib.util.find_spec(name)
    assert spec is not None, f"missing production module: {name}"
    return importlib.import_module(name)


def test_site_build_emits_complete_self_contained_artifact(tmp_path: Path) -> None:
    module = _load_module("scripts.build_site")

    output = module.build_site(ROOT, tmp_path / "site")

    actual = {
        path.relative_to(output).as_posix()
        for path in output.rglob("*")
        if path.is_file()
    }
    assert EXPECTED_SITE_FILES <= actual
    assert not any(path.is_symlink() for path in output.rglob("*"))


def test_site_build_preserves_existing_external_output_directory(tmp_path: Path) -> None:
    """Catches build cleanup escaping the repository-controlled build directory."""
    module = _load_module("scripts.build_site")
    output = tmp_path / "external-site"
    output.mkdir()
    sentinel = output / "sentinel.txt"
    sentinel.write_text("must survive\n", encoding="utf-8")

    with pytest.raises(ValueError, match="external"):
        module.build_site(ROOT, output)
    assert sentinel.read_text(encoding="utf-8") == "must survive\n"


def test_site_build_rejects_a_symlinked_source_directory(tmp_path: Path) -> None:
    """Catches copying site content through a source link outside the repository."""
    module = _load_module("scripts.build_site")
    repo_root = tmp_path / "repository"
    repo_root.mkdir()
    source = tmp_path / "external-site"
    source.mkdir()
    (source / "index.html").write_text("<!doctype html>\n", encoding="utf-8")
    assets = repo_root / "docs" / "assets"
    assets.mkdir(parents=True)
    for name in module.SHARED_ASSETS:
        (assets / name).write_text("<svg><title>asset</title></svg>\n", encoding="utf-8")
    try:
        (repo_root / "site").symlink_to(source, target_is_directory=True)
    except OSError as error:
        pytest.skip(f"source symlink creation is unavailable in this Windows environment: {error}")

    with pytest.raises(ValueError, match="symbolic link"):
        module.build_site(repo_root, repo_root / "build" / "site")


def test_site_html_exposes_all_modules_without_javascript(tmp_path: Path) -> None:
    module = _load_module("scripts.build_site")
    output = module.build_site(ROOT, tmp_path / "site")
    html = (output / "index.html").read_text(encoding="utf-8")
    static_html = html.split("<script", maxsplit=1)[0]

    for skill in EXPECTED_SKILLS:
        assert skill in static_html
    assert "一套让 AI Agent 思考和处理复杂问题的方法论集群" in static_html
    assert "authorization_effect" in static_html
    assert "none" in static_html


def test_site_links_to_all_adapter_compatibility_evidence() -> None:
    """Catches the site omitting one of the published compatibility evidence links."""
    html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")

    for href in (
        "https://reasonix.io/docs/",
        "https://github.com/vercel-labs/skills",
        "../docs/agent-compatibility.md",
    ):
        assert f'href="{href}"' in html


def test_adapter_manifest_covers_exact_hosts_and_skills() -> None:
    manifest_path = ROOT / "adapters" / "compatibility.json"
    assert manifest_path.is_file(), "missing adapter compatibility manifest"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert data["schema_version"] == 1
    assert data["default_bundle"] == "complete"
    assert set(data["skills"]) == EXPECTED_SKILLS
    assert {host["id"] for host in data["hosts"]} == EXPECTED_HOSTS


def test_cursor_manifest_lists_all_documented_skill_discovery_paths() -> None:
    """Catches a regression that drops Cursor's Claude or Codex compatibility paths."""
    data = json.loads((ROOT / "adapters" / "compatibility.json").read_text(encoding="utf-8"))
    cursor = next(host for host in data["hosts"] if host["id"] == "cursor")

    assert cursor["project_paths"] == [
        ".cursor/skills",
        ".agents/skills",
        ".claude/skills",
        ".codex/skills",
    ]
    assert cursor["global_paths"] == [
        "~/.cursor/skills",
        "~/.agents/skills",
        "~/.claude/skills",
        "~/.codex/skills",
    ]


def test_adapter_validator_accepts_repository_contract() -> None:
    module = _load_module("scripts.validate_adapters")
    assert module.validate_adapters(ROOT) == []


def test_adapter_validator_rejects_every_declared_host_mirror_root(tmp_path: Path) -> None:
    """Catches a mirror gate that overlooks a path declared only by one host."""
    module = _load_module("scripts.validate_adapters")
    copied_root = tmp_path / "repository"
    shutil.copytree(ROOT, copied_root)
    (copied_root / ".agent" / "skills").mkdir(parents=True)

    errors = module.validate_adapters(copied_root)
    assert "forbidden host mirror exists: .agent/skills" in errors


def test_adapter_validator_rejects_broken_declared_host_mirror_symlink(tmp_path: Path) -> None:
    """Catches a mirror gate that treats a broken declared link as absent."""
    module = _load_module("scripts.validate_adapters")
    copied_root = tmp_path / "repository"
    shutil.copytree(ROOT, copied_root)
    (copied_root / ".codex").mkdir()
    try:
        (copied_root / ".codex" / "skills").symlink_to(
            copied_root / "missing-skills", target_is_directory=True
        )
    except OSError as error:
        pytest.skip(f"broken symlink creation is unavailable in this Windows environment: {error}")

    assert "forbidden host mirror exists: .codex/skills" in module.validate_adapters(copied_root)


def test_reasonix_stays_a_bounded_compatibility_subset() -> None:
    manifest_path = ROOT / "adapters" / "compatibility.json"
    assert manifest_path.is_file(), "missing adapter compatibility manifest"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    reasonix = next(host for host in data["hosts"] if host["id"] == "reasonix")

    assert reasonix["compatibility"] == "directory-compatible-subset"
    assert set(reasonix["required_smoke_checks"]) == {
        "json-references",
        "peer-routing",
        "context-growth",
    }


def test_source_repository_contains_no_host_mirror_tree() -> None:
    forbidden = {
        ".agents/skills",
        ".claude/skills",
        ".cursor/skills",
        ".gemini/skills",
        ".github/skills",
        ".reasonix/skills",
    }
    assert not {path for path in forbidden if (ROOT / path).exists()}


def test_delivery_infrastructure_is_complete() -> None:
    missing = sorted(path for path in REQUIRED_DELIVERY_FILES if not (ROOT / path).is_file())
    assert missing == []


def test_ci_validates_before_deploying_only_main() -> None:
    workflow_path = ROOT / ".github" / "workflows" / "validate-and-deploy.yml"
    assert workflow_path.is_file(), "missing validate-and-deploy workflow"
    data = yaml.load(workflow_path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)

    jobs = data["jobs"]
    validate = jobs["validate"]
    deploy = jobs["deploy"]
    assert validate["permissions"] == {"contents": "read"}
    assert deploy["needs"] == "validate"
    assert deploy["permissions"] == {"contents": "read", "pages": "write", "id-token": "write"}
    assert deploy["environment"]["name"] == "github-pages"
    assert "github.ref == 'refs/heads/main'" in deploy["if"]
    assert "github.event_name == 'push'" in deploy["if"]


def test_ci_uses_only_frozen_official_action_commits() -> None:
    workflow_path = ROOT / ".github" / "workflows" / "validate-and-deploy.yml"
    assert workflow_path.is_file(), "missing validate-and-deploy workflow"
    text = workflow_path.read_text(encoding="utf-8")
    expected = {
        "actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803",
        "actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1",
        "actions/configure-pages@983d7736d9b0ae728b81ab479565c72886d7745b",
        "actions/upload-pages-artifact@7b1f4a764d45c48632c6b24a0339c27f5614fb0b",
        "actions/deploy-pages@d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e",
    }
    assert expected <= set(text.split())


def test_ci_workflow_has_an_exact_action_surface_and_ephemeral_checkout_credentials() -> None:
    """Catches extra actions, broadened deploy triggers, and persistent checkout credentials."""
    data = yaml.load(
        (ROOT / ".github" / "workflows" / "validate-and-deploy.yml").read_text(encoding="utf-8"),
        Loader=yaml.BaseLoader,
    )
    expected_actions = {
        "actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803",
        "actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1",
        "actions/configure-pages@983d7736d9b0ae728b81ab479565c72886d7745b",
        "actions/upload-pages-artifact@7b1f4a764d45c48632c6b24a0339c27f5614fb0b",
        "actions/deploy-pages@d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e",
    }
    steps = [step for job in data["jobs"].values() for step in job["steps"]]
    uses = {step["uses"] for step in steps if "uses" in step}

    assert uses == expected_actions
    assert all(re.fullmatch(r"[^@]+@[0-9a-f]{40}", action) for action in uses)
    assert set(data["on"]) == {"push", "pull_request", "workflow_dispatch"}
    assert data["on"]["push"]["branches"] == ["main"]
    assert data["jobs"]["validate"]["steps"][-1]["with"]["path"] == "build/site"
    assert "github.event_name == 'push'" in data["jobs"]["validate"]["steps"][-1]["if"]
    assert "github.ref == 'refs/heads/main'" in data["jobs"]["validate"]["steps"][-1]["if"]
    assert data["jobs"]["validate"]["steps"][0]["with"]["persist-credentials"] == "false"


def test_repository_validator_executes_all_extension_contracts() -> None:
    module = importlib.import_module("scripts.validate_repo")
    assert hasattr(module, "validate_extension_contracts")
    assert module.validate_extension_contracts() == []
