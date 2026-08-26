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

# adapters/compatibility.json is the single source of truth for the host
# matrix. This validator checks its structure and invariants and reconciles the
# user-facing install documentation against it; it does not keep a second copy.
HOST_REQUIRED_FIELDS = (
    "id",
    "name",
    "compatibility",
    "project_paths",
    "global_paths",
    "invocation",
    "evidence_url",
)
COMPATIBILITY_LEVELS = {"native-agent-skills", "directory-compatible-subset"}
SUBSET_COMPATIBILITY = "directory-compatible-subset"
EXPECTED_REPO_SLUG = "xi-kari/ariadne-skill"
# README documents only the default complete bundle; the compatibility guide
# may additionally document registered partial-install degradation modes.
INSTALL_DOCUMENT_RULES = {
    "README.md": "complete-bundle-only",
    "docs/agent-compatibility.md": "registered-skills",
}

UNIVERSAL_SMOKE_CHECKS = {
    "json-references",
    "peer-routing",
    "context-growth",
}
VERIFICATION_STATUSES = {"unverified", "smoke-passed"}

FRONTMATTER = re.compile(r"\A---\n(?P<body>.*?)\n---(?:\n|\Z)", re.DOTALL)
BACKTICK_TOKEN = re.compile(r"`([^`]+)`")


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


def _validate_host(host: dict[str, object]) -> list[str]:
    host_id = host.get("id")
    errors: list[str] = []

    unknown_fields = set(host) - set(HOST_REQUIRED_FIELDS) - {"required_smoke_checks", "verification"}
    if unknown_fields:
        errors.append(f"host {host_id} declares unknown fields: {sorted(unknown_fields)}")
    for field in ("name", "invocation"):
        value = host.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"host {host_id} must declare a non-empty {field}")

    if host.get("compatibility") not in COMPATIBILITY_LEVELS:
        errors.append(f"host {host_id} has an unknown compatibility level")

    if not _is_https_url(host.get("evidence_url")):
        errors.append(f"host {host_id} evidence_url must be HTTPS")

    for field in ("project_paths", "global_paths"):
        paths = _string_list(host.get(field))
        if (
            paths is None
            or not paths
            or len(paths) != len(set(paths))
            or not all(path.strip() for path in paths)
        ):
            errors.append(f"host {host_id} {field} must be unique non-empty paths")

    if host.get("compatibility") == SUBSET_COMPATIBILITY:
        checks = host.get("required_smoke_checks")
        if not _has_exact_unique_members(checks, UNIVERSAL_SMOKE_CHECKS):
            errors.append(f"host {host_id} required_smoke_checks are incomplete")
    elif "required_smoke_checks" in host and not _has_exact_unique_members(
        host.get("required_smoke_checks"), UNIVERSAL_SMOKE_CHECKS
    ):
        errors.append(f"host {host_id} declares a nonstandard smoke-check set")

    verification = host.get("verification")
    if (
        not isinstance(verification, dict)
        or set(verification) != {"status", "last_verified"}
        or verification.get("status") not in VERIFICATION_STATUSES
    ):
        errors.append(f"host {host_id} must declare verification status and last_verified")
    elif verification["status"] == "smoke-passed" and not (
        isinstance(verification.get("last_verified"), str) and verification["last_verified"].strip()
    ):
        errors.append(f"host {host_id} smoke-passed requires a last_verified date")
    elif verification["status"] == "unverified" and verification.get("last_verified") is not None:
        errors.append(f"host {host_id} unverified hosts keep last_verified null")

    return errors


def _extract_install_commands(text: str) -> list[dict[str, object]]:
    commands: list[dict[str, object]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"npx\s+skills\s+add\s", stripped) is None:
            continue
        tokens = stripped.split()
        command: dict[str, object] = {
            "line": stripped,
            "repo": tokens[3] if len(tokens) > 3 else None,
            "skills": [],
            "adapters": [],
        }
        for index, token in enumerate(tokens[:-1]):
            if token == "--skill":
                command["skills"].append(tokens[index + 1].strip("'\""))
            elif token == "-a":
                command["adapters"].append(tokens[index + 1])
        commands.append(command)
    return commands


def _validate_install_documents(
    repo_root: Path,
    manifest_skills: list[str],
    host_ids: list[str],
    native_host_ids: list[str],
) -> list[str]:
    errors: list[str] = []
    for relative, rule in INSTALL_DOCUMENT_RULES.items():
        path = repo_root / relative
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"unreadable install document {relative}: {exc}")
            continue
        commands = _extract_install_commands(text)
        if not commands:
            errors.append(f"{relative} documents no npx skills add command")
            continue
        for command in commands:
            repo = command["repo"]
            repo_base = repo.split("@", 1)[0] if isinstance(repo, str) else repo
            if repo_base != EXPECTED_REPO_SLUG:
                errors.append(
                    f"{relative} install command targets {command['repo']!r}"
                    f" instead of {EXPECTED_REPO_SLUG}"
                )
            skills = command["skills"]
            if not skills:
                errors.append(f"{relative} install command does not pin --skill")
            for skill in skills:
                if rule == "complete-bundle-only" and skill != "*":
                    errors.append(
                        f"{relative} install command must install the complete bundle,"
                        f" not {skill!r}"
                    )
                elif skill != "*" and skill not in manifest_skills:
                    errors.append(
                        f"{relative} install command names unregistered skill {skill!r}"
                    )
            adapters = command["adapters"]
            if len(adapters) != len(set(adapters)) or not set(adapters) <= set(host_ids):
                errors.append(
                    f"{relative} install command adapters are not registered manifest hosts:"
                    f" {adapters}"
                )
            elif not set(native_host_ids) <= set(adapters):
                errors.append(
                    f"{relative} install command must include every native-agent-skills host:"
                    f" {adapters}"
                )
        if not any("*" in command["skills"] for command in commands):
            errors.append(f"{relative} must document the complete-bundle install command")
    return errors


def _validate_host_table(repo_root: Path, hosts: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    relative = "docs/agent-compatibility.md"
    path = repo_root / relative
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return [f"unreadable install document {relative}: {exc}"]

    hosts_by_name = {
        host["name"]: host
        for host in hosts
        if isinstance(host.get("name"), str)
    }
    documented: set[str] = set()
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 6 or cells[0] not in hosts_by_name:
            continue
        host = hosts_by_name[cells[0]]
        documented.add(cells[0])
        for column, field in ((2, "project_paths"), (3, "global_paths")):
            table_paths = BACKTICK_TOKEN.findall(cells[column])
            if table_paths != list(host.get(field) or []):
                errors.append(
                    f"{relative} table row {cells[0]} {field} differ from manifest:"
                    f" {table_paths}"
                )
    for missing in sorted(set(hosts_by_name) - documented):
        errors.append(f"{relative} host table is missing a row for {missing}")
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

    bundle = manifest.get("single_file_bundle")
    if (
        not isinstance(bundle, dict)
        or not isinstance(bundle.get("path"), str)
        or not isinstance(bundle.get("generator"), str)
    ):
        errors.append("adapter manifest must register the single_file_bundle path and generator")
    else:
        for field in ("path", "generator"):
            if not (repo_root / bundle[field]).is_file():
                errors.append(f"single_file_bundle {field} does not exist: {bundle[field]}")

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
        if not hosts:
            errors.append("adapter manifest must declare at least one host")
        host_ids = [host.get("id") for host in hosts]
        if not all(isinstance(host_id, str) and host_id for host_id in host_ids):
            errors.append("adapter manifest host IDs must be non-empty strings")
        else:
            if len(host_ids) != len(set(host_ids)):
                errors.append("adapter manifest host IDs must be unique")
            for host in hosts:
                errors.extend(_validate_host(host))
            if not any(host.get("compatibility") == SUBSET_COMPATIBILITY for host in hosts):
                errors.append("adapter manifest must keep the bounded compatibility subset host")

            known_skills = (
                list(manifest_skills)
                if _string_list(manifest_skills) is not None
                else list(EXPECTED_SKILLS)
            )
            native_host_ids = [
                host["id"]
                for host in hosts
                if host.get("compatibility") == "native-agent-skills"
                and isinstance(host.get("id"), str)
            ]
            errors.extend(
                _validate_install_documents(repo_root, known_skills, host_ids, native_host_ids)
            )
            errors.extend(_validate_host_table(repo_root, hosts))

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
