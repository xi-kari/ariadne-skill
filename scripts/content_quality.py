from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".svg",
    ".txt",
    ".yaml",
    ".yml",
}
IGNORED_PARTS = {".git", ".worktrees", "__pycache__", ".pytest_cache", "build"}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
EXPLICIT_ANCHOR = re.compile(r"<(?:a|[A-Za-z][\w:-]*)\b[^>]*(?:id|name)=[\"']([^\"']+)[\"']")
MARKDOWN_HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "chatgpt-conversation"}
RUNTIME_TAG_ATTRIBUTES = {
    "audio": {"src"},
    "iframe": {"src"},
    "img": {"src"},
    "link": {"href"},
    "script": {"src"},
    "source": {"src", "srcset"},
    "video": {"poster", "src"},
}
SHARED_SITE_ASSETS = {"readme-hero.svg", "lattice-kernel-map.svg"}


class _HTMLReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str, str]] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized = tag.lower()
        for name, value in attrs:
            if value is None:
                continue
            attr = name.lower()
            if attr in {"id", "name"}:
                self.anchors.add(value)
            if attr in {"href", "src", "srcset", "poster"}:
                self.references.append((normalized, attr, value))


def _iter_text_files(root: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file()
            and path.suffix.lower() in TEXT_SUFFIXES
            and not IGNORED_PARTS.intersection(path.relative_to(root).parts)
        ),
        key=lambda path: path.relative_to(root).as_posix(),
    )


def _issue(code: str, root: Path, path: Path, detail: str) -> str:
    return f"{code}: {path.relative_to(root).as_posix()}: {detail}"


def _strip_markdown_code(text: str) -> str:
    visible: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)[0]
            fence = None if fence == marker else marker
            visible.append("\n" if line.endswith("\n") else "")
            continue
        visible.append(("\n" if line.endswith("\n") else "") if fence else line)
    return INLINE_CODE.sub("", "".join(visible))


def _github_slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value).strip().lower()
    value = re.sub(r"[^\w\-\s\u4e00-\u9fff]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s]+", "-", value)


def _anchors_for(path: Path, text: str) -> set[str]:
    anchors = set(EXPLICIT_ANCHOR.findall(text))
    if path.suffix.lower() == ".md":
        counts: dict[str, int] = {}
        for heading in MARKDOWN_HEADING.findall(_strip_markdown_code(text)):
            base = _github_slug(heading)
            if not base:
                continue
            count = counts.get(base, 0)
            anchors.add(base if count == 0 else f"{base}-{count}")
            counts[base] = count + 1
    elif path.suffix.lower() == ".html":
        parser = _HTMLReferences()
        parser.feed(text)
        anchors.update(parser.anchors)
    return anchors


def _split_markdown_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    match = re.match(r"([^\s]+)", target)
    return match.group(1) if match else target


def _local_target(raw: str) -> tuple[str, str] | None:
    parsed = urlsplit(unquote(raw))
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or parsed.netloc:
        return None
    return parsed.path, parsed.fragment


def _validate_reference(
    root: Path,
    source: Path,
    raw_target: str,
    decoded: dict[Path, str],
    anchor_cache: dict[Path, set[str]],
) -> list[str]:
    local = _local_target(raw_target)
    if local is None:
        return []
    path_part, fragment = local
    candidate = source if not path_part else source.parent / path_part
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        return [_issue("path-escape", root, source, raw_target)]
    if not resolved.exists():
        source_relative = source.relative_to(root)
        generated_name = Path(path_part).name
        if (
            source_relative.parts
            and source_relative.parts[0] == "site"
            and Path(path_part).parent.as_posix() == "assets"
            and generated_name in SHARED_SITE_ASSETS
        ):
            shared_source = (root / "docs" / "assets" / generated_name).resolve()
            if shared_source.exists():
                resolved = shared_source
    if not resolved.exists():
        return [_issue("missing-target", root, source, raw_target)]
    if fragment:
        if resolved not in decoded:
            try:
                decoded[resolved] = resolved.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                return []
        anchors = anchor_cache.setdefault(
            resolved,
            _anchors_for(resolved, decoded[resolved]),
        )
        if fragment not in anchors:
            return [_issue("missing-anchor", root, source, raw_target)]
    return []


def _has_accessible_svg_text(root: ET.Element) -> bool:
    if root.attrib.get("aria-label", "").strip():
        return True
    for element in root.iter():
        if element.tag.rsplit("}", maxsplit=1)[-1] == "title" and (element.text or "").strip():
            return True
    return False


def validate_content(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    decoded: dict[Path, str] = {}
    anchor_cache: dict[Path, set[str]] = {}

    for path in _iter_text_files(root):
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(_issue("invalid-utf8", root, path, "file is not UTF-8"))
            continue
        decoded[path.resolve()] = text
        if raw and not raw.endswith(b"\n"):
            errors.append(_issue("missing-final-newline", root, path, "file must end with LF"))
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.endswith((" ", "\t")):
                errors.append(
                    _issue("trailing-whitespace", root, path, f"line {line_number}")
                )

        if path.suffix.lower() == ".svg":
            try:
                svg_root = ET.fromstring(text)
            except ET.ParseError as exc:
                errors.append(_issue("invalid-svg", root, path, str(exc)))
            else:
                if not _has_accessible_svg_text(svg_root):
                    errors.append(
                        _issue(
                            "missing-svg-accessibility",
                            root,
                            path,
                            "add aria-label or a non-empty title",
                        )
                    )

    for path, text in sorted(decoded.items(), key=lambda item: item[0].as_posix()):
        suffix = path.suffix.lower()
        if suffix == ".md":
            visible = _strip_markdown_code(text)
            for raw in MARKDOWN_LINK.findall(visible):
                errors.extend(
                    _validate_reference(
                        root,
                        path,
                        _split_markdown_target(raw),
                        decoded,
                        anchor_cache,
                    )
                )
        elif suffix == ".html":
            parser = _HTMLReferences()
            parser.feed(text)
            for tag, attr, raw in parser.references:
                value = raw.split(",", maxsplit=1)[0].strip().split(" ", maxsplit=1)[0]
                local = _local_target(value)
                if local is None:
                    if attr in RUNTIME_TAG_ATTRIBUTES.get(tag, set()):
                        errors.append(
                            _issue(
                                "external-runtime-asset",
                                root,
                                path,
                                f"{tag}[{attr}] -> {value}",
                            )
                        )
                    continue
                errors.extend(
                    _validate_reference(root, path, value, decoded, anchor_cache)
                )

    return sorted(set(errors))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_content(root)
    if errors:
        print("Ariadne content quality validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Ariadne content quality validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
