from __future__ import annotations

import importlib
import importlib.util
import json
from pathlib import Path

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


def test_adapter_manifest_covers_exact_hosts_and_skills() -> None:
    manifest_path = ROOT / "adapters" / "compatibility.json"
    assert manifest_path.is_file(), "missing adapter compatibility manifest"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert data["schema_version"] == 1
    assert data["default_bundle"] == "complete"
    assert set(data["skills"]) == EXPECTED_SKILLS
    assert {host["id"] for host in data["hosts"]} == EXPECTED_HOSTS


def test_adapter_validator_accepts_repository_contract() -> None:
    module = _load_module("scripts.validate_adapters")
    assert module.validate_adapters(ROOT) == []


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
