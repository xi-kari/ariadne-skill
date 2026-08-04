from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_SKILLS = (
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
)

EXPECTED_HOSTS = {
    "codex": {
        "name": "Codex",
        "compatibility": "native-agent-skills",
        "project_paths": (".agents/skills",),
        "global_paths": ("~/.agents/skills", "~/.codex/skills"),
        "invocation": "$ariadne-skill",
        "evidence_url": "https://developers.openai.com/codex/skills",
    },
    "claude-code": {
        "name": "Claude Code",
        "compatibility": "native-agent-skills",
        "project_paths": (".claude/skills",),
        "global_paths": ("~/.claude/skills",),
        "invocation": "/ariadne-skill",
        "evidence_url": "https://code.claude.com/docs/en/slash-commands",
    },
    "gemini-cli": {
        "name": "Gemini CLI",
        "compatibility": "native-agent-skills",
        "project_paths": (".gemini/skills", ".agents/skills"),
        "global_paths": ("~/.gemini/skills", "~/.agents/skills"),
        "invocation": "natural-language: ariadne-skill",
        "evidence_url": "https://geminicli.com/docs/cli/using-agent-skills/",
    },
    "cursor": {
        "name": "Cursor",
        "compatibility": "native-agent-skills",
        "project_paths": (
            ".cursor/skills",
            ".agents/skills",
            ".claude/skills",
            ".codex/skills",
        ),
        "global_paths": (
            "~/.cursor/skills",
            "~/.agents/skills",
            "~/.claude/skills",
            "~/.codex/skills",
        ),
        "invocation": "/ariadne-skill",
        "evidence_url": "https://cursor.com/docs/context/skills",
    },
    "github-copilot": {
        "name": "GitHub Copilot",
        "compatibility": "native-agent-skills",
        "project_paths": (".github/skills", ".claude/skills", ".agents/skills"),
        "global_paths": ("~/.copilot/skills", "~/.agents/skills"),
        "invocation": "natural-language: ariadne-skill",
        "evidence_url": (
            "https://docs.github.com/en/copilot/how-tos/copilot-on-github/"
            "customize-copilot/customize-cloud-agent/add-skills"
        ),
    },
    "reasonix": {
        "name": "Reasonix",
        "compatibility": "directory-compatible-subset",
        "project_paths": (
            ".reasonix/skills",
            ".agents/skills",
            ".agent/skills",
            ".claude/skills",
        ),
        "global_paths": (
            "~/.reasonix/skills",
            "~/.agents/skills",
            "~/.claude/skills",
        ),
        "invocation": "/ariadne-skill",
        "evidence_url": "https://reasonix.io/docs/",
    },
}

REASONIX_SMOKE_CHECKS = {
    "json-references",
    "peer-routing",
    "context-growth",
}

FRONTMATTER = re.compile(r"\A---\n(?P<body>.*?)\n---(?:\n|\Z)", re.DOTALL)


def _string_list(value: object) -> list[str] | None:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        return None
    return value


def _has_exact_unique_members(value: object, expected: tuple[str, ...] | set[str]) -> bool:
    items = _string_list(value)
    return items is not None and len(items) == len(set(items)) and set(items) == set(expected)


def _is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and parsed.username is None


def _validate_frontmatter(repo_root: Path, skill_name: str) -> list[str]:
    skill_path = repo_root / "skills" / skill_name / "SKILL.md"
    if not skill_path.is_file():
        return [f"missing Skill entrypoint: skills/{skill_name}/SKILL.md"]

    try:
        text = skill_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return [f"unreadable Skill entrypoint for {skill_name}: {exc}"]

    match = FRONTMATTER.match(text)
    if match is None:
        return [f"missing basic frontmatter for {skill_name}"]

    try:
        metadata = yaml.safe_load(match.group("body"))
    except yaml.YAMLError as exc:
        return [f"invalid frontmatter for {skill_name}: {exc}"]

    if not isinstance(metadata, dict):
        return [f"frontmatter is not a mapping for {skill_name}"]

    errors: list[str] = []
    if metadata.get("name") != skill_name:
        errors.append(f"frontmatter name mismatch for {skill_name}")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"frontmatter description missing for {skill_name}")
    return errors


def _validate_host(host_id: str, host: dict[str, object]) -> list[str]:
    expected = EXPECTED_HOSTS[host_id]
    errors: list[str] = []

    for field in ("name", "compatibility", "invocation", "evidence_url"):
        if host.get(field) != expected[field]:
            errors.append(f"host {host_id} has invalid {field}")

    evidence_url = host.get("evidence_url")
    if not _is_https_url(evidence_url):
        errors.append(f"host {host_id} evidence_url must be HTTPS")

    for field in ("project_paths", "global_paths"):
        expected_paths = expected[field]
        actual_paths = host.get(field)
        if not _has_exact_unique_members(actual_paths, expected_paths):
            errors.append(f"host {host_id} has incomplete {field}")

    if host_id == "reasonix":
        checks = host.get("required_smoke_checks")
        if not _has_exact_unique_members(checks, REASONIX_SMOKE_CHECKS):
            errors.append("reasonix required_smoke_checks are incomplete")
    elif "required_smoke_checks" in host:
        errors.append(f"host {host_id} must not claim Reasonix smoke checks")

    return errors


def validate_adapters(repo_root: Path) -> list[str]:
    repo_root = Path(repo_root).resolve()
    errors: list[str] = []
    manifest_path = repo_root / "adapters" / "compatibility.json"

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return ["missing adapters/compatibility.json"]
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"invalid adapters/compatibility.json: {exc}"]

    if not isinstance(manifest, dict):
        return ["adapter manifest must be a JSON object"]

    if manifest.get("schema_version") != 1:
        errors.append("adapter manifest schema_version must equal 1")
    if manifest.get("source_of_truth") != "skills":
        errors.append("adapter manifest source_of_truth must equal skills")
    if manifest.get("default_bundle") != "complete":
        errors.append("adapter manifest default_bundle must equal complete")
    if manifest.get("release_channel") != "rolling-main":
        errors.append("adapter manifest release_channel must equal rolling-main")
    if manifest.get("windows_install_mode") != "copy":
        errors.append("adapter manifest windows_install_mode must equal copy")

    for field in ("agent_skills_spec_url", "installer_evidence_url"):
        if not _is_https_url(manifest.get(field)):
            errors.append(f"adapter manifest {field} must be HTTPS")

    fallback = manifest.get("router_only_degradation")
    expected_fallback = {
        "installed_skills": ["ariadne-skill"],
        "missing_peer_status": "module_unavailable",
        "semantic_equivalence": False,
    }
    if fallback != expected_fallback:
        errors.append("adapter manifest router-only degradation is invalid")

    manifest_skills = manifest.get("skills")
    if not _has_exact_unique_members(manifest_skills, EXPECTED_SKILLS):
        errors.append("adapter manifest Skill set is not exact")

    skills_root = repo_root / "skills"
    try:
        actual_skills = {path.name for path in skills_root.iterdir() if path.is_dir()}
    except OSError as exc:
        errors.append(f"unreadable skills directory: {exc}")
        actual_skills = set()
    if actual_skills != set(EXPECTED_SKILLS):
        errors.append(f"repository Skill set is not exact: {sorted(actual_skills)}")

    for skill_name in EXPECTED_SKILLS:
        errors.extend(_validate_frontmatter(repo_root, skill_name))

    hosts = manifest.get("hosts")
    if not isinstance(hosts, list) or not all(isinstance(host, dict) for host in hosts):
        errors.append("adapter manifest hosts must be a list of objects")
    else:
        host_ids = [host.get("id") for host in hosts]
        if not all(isinstance(host_id, str) for host_id in host_ids):
            errors.append("adapter manifest host IDs must be strings")
        else:
            if len(host_ids) != len(set(host_ids)):
                errors.append("adapter manifest host IDs must be unique")
            if set(host_ids) != set(EXPECTED_HOSTS):
                errors.append("adapter manifest host set is not exact")

            hosts_by_id = {host["id"]: host for host in hosts}
            for host_id in EXPECTED_HOSTS:
                host = hosts_by_id.get(host_id)
                if host is not None:
                    errors.extend(_validate_host(host_id, host))

    if isinstance(hosts, list) and all(isinstance(host, dict) for host in hosts):
        forbidden_mirrors = {
            relative
            for host in hosts
            for relative in _string_list(host.get("project_paths")) or []
        }
        for relative in sorted(forbidden_mirrors):
            path = repo_root / relative
            if path.exists() or path.is_symlink():
                errors.append(f"forbidden host mirror exists: {relative}")

    return errors


def main() -> int:
    errors = validate_adapters(ROOT)
    if errors:
        print("Ariadne adapter validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Ariadne adapter validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
