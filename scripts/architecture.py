"""Validate package resources independently of any particular workflow count."""
from __future__ import annotations

import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

try:
    from .content_quality import _strip_markdown_code
except ImportError:
    from content_quality import _strip_markdown_code


PACKAGE_ROOT = Path(__file__).resolve().parents[1] / "skills/ariadne-skill"
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IDENTITY = {"name": "Ariadne", "kernel": "Lattice Kernel", "installable_skill": "ariadne-skill"}


def load_architecture(package_root: Path = PACKAGE_ROOT) -> dict:
    return json.loads(package_path(package_root, "architecture.json").read_text(encoding="utf-8"))


def declared_resources(data: dict) -> list[str]:
    """Return the ownership list; source and bundle are references to this list."""
    paths = [data.get("entry")]
    for key in ("shared", "library", "legacy"):
        value = data.get(key, [])
        if isinstance(value, list):
            paths.extend(value)
    for route in data.get("routes", []) if isinstance(data.get("routes"), list) else []:
        if isinstance(route, dict):
            paths.append(route.get("path"))
    for contract in data.get("contracts", []) if isinstance(data.get("contracts"), list) else []:
        if isinstance(contract, dict):
            paths.extend(contract.get(key) for key in ("guide", "schema", "tool"))
    return paths


def package_path(package_root: Path, relative: str, *, must_exist: bool = True) -> Path:
    """Reject escaping, ambiguous, and symlinked resources before opening them."""
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        raise ValueError(f"unsafe package resource: {relative!r}")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or ".." in pure.parts or pure.as_posix() != relative or relative == ".":
        raise ValueError(f"unsafe package resource: {relative!r}")
    root = package_root.resolve()
    candidate = root.joinpath(*pure.parts)
    current = root
    for part in pure.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"symlinked package resource: {relative}")
    if root not in candidate.resolve().parents:
        raise ValueError(f"package resource escapes the installation: {relative}")
    if must_exist and not candidate.is_file():
        raise ValueError(f"missing package resource: {relative}")
    return candidate


def _nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _strings(value: object) -> bool:
    return isinstance(value, list) and all(_nonempty(item) for item in value)


def _reachable(data: dict, package_root: Path, resources: set[str]) -> set[str]:
    """Follow real local navigation, including an explicitly linked resource index."""
    known = resources | {"architecture.json"}
    edges: dict[str, set[str]] = {"architecture.json": set(resources)}
    for relative in resources:
        path = package_path(package_root, relative)
        targets: set[str] = set()
        if path.suffix == ".md":
            text = _strip_markdown_code(path.read_text(encoding="utf-8"))
            for raw in LINK.findall(text):
                parsed = urlsplit(unquote(raw.strip().strip("<>")))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = (path.parent / parsed.path).resolve()
                try:
                    target = resolved.relative_to(package_root.resolve()).as_posix()
                except ValueError:
                    continue
                if target in known:
                    targets.add(target)
        elif path.suffix == ".json":
            def collect(node: object) -> None:
                if isinstance(node, str) and node in known:
                    targets.add(node)
                elif isinstance(node, list):
                    for value in node:
                        collect(value)
                elif isinstance(node, dict):
                    for value in node.values():
                        collect(value)
            collect(json.loads(path.read_text(encoding="utf-8")))
        edges[relative] = targets
    found: set[str] = set()
    pending = [data["entry"]]
    while pending:
        node = pending.pop()
        if node not in found:
            found.add(node)
            pending.extend(edges.get(node, set()) - found)
    return found


def validate_architecture(data: dict, package_root: Path = PACKAGE_ROOT, *, check_files: bool = True) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["architecture must be an object"]
    if data.get("format_version") != "1.0":
        errors.append("architecture format_version must be 1.0")
    if data.get("identity") != IDENTITY:
        errors.append("architecture must preserve the Ariadne installation and kernel identity")
    if data.get("entry") != "SKILL.md":
        errors.append("architecture entry must be SKILL.md")
    for key in ("composition_rule", "record_rule"):
        if not _nonempty(data.get(key)):
            errors.append(f"architecture requires a nonempty {key}")
    for key in ("shared", "library", "legacy", "bundle"):
        if not _strings(data.get(key)):
            errors.append(f"architecture {key} must be a list of nonempty resource paths")
    routes = data.get("routes")
    if not isinstance(routes, list) or not routes:
        errors.append("architecture routes must be a nonempty list")
        routes = []
    route_ids: list[str] = []
    for route in routes:
        if not isinstance(route, dict) or not all(_nonempty(route.get(key)) for key in ("id", "name", "path")):
            errors.append("architecture route requires id, name, and path")
            continue
        route_ids.append(route["id"])
        if not _strings(route.get("result_types")) or not route["result_types"]:
            errors.append(f"architecture route {route['id']} requires result_types")
    if len(route_ids) != len(set(route_ids)):
        errors.append("architecture route IDs must be unique")
    contracts = data.get("contracts")
    if not isinstance(contracts, list):
        errors.append("architecture contracts must be a list")
        contracts = []
    contract_ids: list[str] = []
    for contract in contracts:
        if not isinstance(contract, dict) or not all(_nonempty(contract.get(key)) for key in ("id", "guide", "schema", "tool", "required_when")):
            errors.append("architecture contract requires id, guide, schema, tool, and required_when")
            continue
        contract_ids.append(contract["id"])
    if len(contract_ids) != len(set(contract_ids)):
        errors.append("architecture contract IDs must be unique")
    resources = declared_resources(data)
    if not all(isinstance(path, str) for path in resources):
        errors.append("architecture resource declarations must be strings")
        return errors
    if len(resources) != len(set(resources)):
        errors.append("architecture resource ownership must be unique")
    resource_set = set(resources)
    if not isinstance(data.get("source"), str) or data["source"] not in resource_set:
        errors.append("architecture source must name a declared resource")
    bundle = data.get("bundle", [])
    if _strings(bundle):
        if len(bundle) != len(set(bundle)):
            errors.append("architecture bundle resources must be unique")
        if not set(bundle) <= resource_set:
            errors.append("architecture bundle includes an undeclared resource")
        shared = data.get("shared")
        required = {data.get("entry")} | set(shared if _strings(shared) else [])
        required |= {route["path"] for route in routes if isinstance(route, dict) and isinstance(route.get("path"), str)}
        required |= {contract["guide"] for contract in contracts if isinstance(contract, dict) and isinstance(contract.get("guide"), str)}
        if not required <= set(bundle):
            errors.append("architecture bundle must include entry, shared resources, paths, and contract guides")
        if bundle and bundle[0] != data.get("entry"):
            errors.append("architecture bundle must start with the entry")
        if any(not item.endswith(".md") for item in bundle):
            errors.append("architecture bundle may inline only Markdown guidance")
    for relative in resources:
        try:
            path = package_path(package_root, relative, must_exist=check_files)
            if check_files and not path.read_text(encoding="utf-8").strip():
                errors.append(f"empty package resource: {relative}")
        except (OSError, ValueError, UnicodeDecodeError) as exc:
            errors.append(str(exc))
    if check_files:
        for path in package_root.rglob("*"):
            if path.is_symlink():
                errors.append(f"symlinked package resource: {path.relative_to(package_root).as_posix()}")
        actual = {
            path.relative_to(package_root).as_posix()
            for path in package_root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        expected = resource_set | {"architecture.json", "agents/openai.yaml"}
        for extra in sorted(actual - expected):
            errors.append(f"unregistered package resource: {extra}")
        for absent in sorted(expected - actual):
            errors.append(f"missing registered package resource: {absent}")
        if not errors:
            try:
                unreachable = resource_set - _reachable(data, package_root, resource_set)
                errors.extend(f"package resource is unreachable from entry: {path}" for path in sorted(unreachable))
            except (OSError, ValueError, UnicodeDecodeError) as exc:
                errors.append(f"package navigation invalid: {exc}")
    return errors
