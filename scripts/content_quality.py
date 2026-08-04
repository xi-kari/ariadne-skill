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
MARKDOWN_REFERENCE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
EXPLICIT_ANCHOR = re.compile(r"<(?:a|[A-Za-z][\w:-]*)\b[^>]*(?:id|name)=[\"']([^\"']+)[\"']")
MARKDOWN_HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "chatgpt-conversation"}
RUNTIME_TAG_ATTRIBUTES = {
    "audio": {"src"},
    "iframe": {"src"},
    "img": {"src", "srcset"},
    "link": {"href"},
    "script": {"src"},
    "source": {"src", "srcset"},
    "video": {"poster", "src"},
}
SHARED_SITE_ASSETS = {"readme-hero.svg", "lattice-kernel-map.svg"}
CSS_REFERENCE = re.compile(r"(?:@import\s+(?:url\(\s*)?|url\(\s*)([^)\s'\"]+|['\"][^'\"]+['\"])", re.IGNORECASE)
SCRIPT_REFERENCE = re.compile(r"(?:import\s*(?:\(\s*)?|from\s+)[\"']([^\"']+)[\"']")


class _HTMLReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str, str]] = []
        self.anchors: set[str] = set()
        self.embedded_styles: list[str] = []
        self.embedded_scripts: list[str] = []
        self._embedded_tag: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized = tag.lower()
        self._embedded_tag = normalized if normalized in {"style", "script"} else None
        for name, value in attrs:
            if value is None:
                continue
            attr = name.lower()
            if attr in {"id", "name"}:
                self.anchors.add(value)
            if attr in {"href", "src", "srcset", "poster"}:
                self.references.append((normalized, attr, value))

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == self._embedded_tag:
            self._embedded_tag = None

    def handle_data(self, data: str) -> None:
        if self._embedded_tag == "style":
            self.embedded_styles.append(data)
        elif self._embedded_tag == "script":
            self.embedded_scripts.append(data)


def _iter_text_files(root: Path) -> list[Path]:
    def is_text_candidate(path: Path) -> bool:
        if path.suffix.lower() in TEXT_SUFFIXES:
            return True
        if path.suffix:
            return False
        try:
            return b"\0" not in path.read_bytes()
        except OSError:
            return False

    return sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file()
            and is_text_candidate(path)
            and not IGNORED_PARTS.intersection(path.relative_to(root).parts)
        ),
        key=lambda path: path.relative_to(root).as_posix(),
    )


def _issue(code: str, root: Path, path: Path, detail: str) -> str:
    return f"{code}: {path.relative_to(root).as_posix()}: {detail}"


def _strip_markdown_code(text: str) -> str:
    visible: list[str] = []
    fence: tuple[str, int] | None = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            run = match.group(1)
            marker = run[0]
            if fence is None:
                fence = (marker, len(run))
                visible.append("\n" if line.endswith("\n") else "")
                continue
            if marker == fence[0] and len(run) >= fence[1]:
                fence = None
                visible.append("\n" if line.endswith("\n") else "")
                continue
        visible.append(("\n" if line.endswith("\n") else "") if fence else line)
    return _strip_inline_code("".join(visible))


def _strip_inline_code(text: str) -> str:
    visible: list[str] = []
    index = 0
    while index < len(text):
        if text[index] != "`":
            visible.append(text[index])
            index += 1
            continue
        end = index
        while end < len(text) and text[end] == "`":
            end += 1
        marker = text[index:end]
        closing = text.find(marker, end)
        if closing == -1 or "\n" in text[end:closing]:
            visible.append(marker)
            index = end
            continue
        index = closing + len(marker)
    return "".join(visible)


def _github_slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value).strip().lower()
    value = re.sub(r"[^\w\-\s\u4e00-\u9fff]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s]+", "-", value)


def _anchors_for(path: Path, text: str) -> set[str]:
    visible = _strip_markdown_code(text) if path.suffix.lower() == ".md" else text
    anchors = set(EXPLICIT_ANCHOR.findall(visible))
    if path.suffix.lower() == ".md":
        counts: dict[str, int] = {}
        for heading in MARKDOWN_HEADING.findall(visible):
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
    if not resolved.is_file():
        return [_issue("directory-target", root, source, raw_target)]
    if resolved not in decoded:
        try:
            decoded[resolved] = resolved.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return [_issue("unreadable-target", root, source, raw_target)]
    if fragment:
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
    for element in root:
        if element.tag.rsplit("}", maxsplit=1)[-1] == "title" and (element.text or "").strip():
            return True
    return False


def _reference_candidates(value: str, attribute: str) -> list[str]:
    if attribute != "srcset":
        return [value]
    return [
        candidate.strip().split(maxsplit=1)[0]
        for candidate in value.split(",")
        if candidate.strip()
    ]


def _validate_runtime_reference(
    root: Path,
    source: Path,
    tag: str,
    attribute: str,
    value: str,
    decoded: dict[Path, str],
    anchor_cache: dict[Path, set[str]],
) -> list[str]:
    errors: list[str] = []
    for candidate in _reference_candidates(value, attribute):
        local = _local_target(candidate)
        if local is None:
            if attribute in RUNTIME_TAG_ATTRIBUTES.get(tag, set()) or tag in {"css", "script", "svg"}:
                errors.append(
                    _issue(
                        "external-runtime-asset",
                        root,
                        source,
                        f"{tag}[{attribute}] -> {candidate}",
                    )
                )
            continue
        errors.extend(_validate_reference(root, source, candidate, decoded, anchor_cache))
    return errors


def validate_content(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    decoded: dict[Path, str] = {}
    anchor_cache: dict[Path, set[str]] = {}

    def validate_embedded_html_runtime(path: Path, parser: _HTMLReferences) -> list[str]:
        embedded_errors: list[str] = []
        for style in parser.embedded_styles:
            for raw in CSS_REFERENCE.findall(style):
                embedded_errors.extend(
                    _validate_runtime_reference(
                        root, path, "css", "url", raw.strip("'\""), decoded, anchor_cache
                    )
                )
        for script in parser.embedded_scripts:
            for raw in SCRIPT_REFERENCE.findall(script):
                embedded_errors.extend(
                    _validate_runtime_reference(
                        root, path, "script", "script", raw, decoded, anchor_cache
                    )
                )
        return embedded_errors

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
                if svg_root.tag.rsplit("}", maxsplit=1)[-1] != "svg":
                    errors.append(_issue("invalid-svg-root", root, path, "root element must be svg"))
                if not _has_accessible_svg_text(svg_root):
                    errors.append(
                        _issue(
                            "missing-svg-accessibility",
                            root,
                            path,
                            "add aria-label or a non-empty title",
                        )
                    )
                for element in svg_root.iter():
                    tag = element.tag.rsplit("}", maxsplit=1)[-1].lower()
                    for attribute, value in element.attrib.items():
                        if value is None:
                            continue
                        name = attribute.rsplit("}", maxsplit=1)[-1].lower()
                        if name in {"href", "src"}:
                            errors.extend(
                                _validate_runtime_reference(
                                    root, path, "svg", name, value, decoded, anchor_cache
                                )
                            )
                    if tag == "style" and element.text:
                        for raw in CSS_REFERENCE.findall(element.text):
                            errors.extend(
                                _validate_runtime_reference(
                                    root,
                                    path,
                                    "svg",
                                    "style",
                                    raw.strip("'\""),
                                    decoded,
                                    anchor_cache,
                                )
                            )
                    if tag == "script" and element.text:
                        for raw in SCRIPT_REFERENCE.findall(element.text):
                            errors.extend(
                                _validate_runtime_reference(
                                    root,
                                    path,
                                    "svg",
                                    "script",
                                    raw,
                                    decoded,
                                    anchor_cache,
                                )
                            )

    for path, text in sorted(decoded.items(), key=lambda item: item[0].as_posix()):
        suffix = path.suffix.lower()
        if suffix == ".md":
            visible = _strip_markdown_code(text)
            for raw in [*MARKDOWN_LINK.findall(visible), *MARKDOWN_REFERENCE.findall(visible)]:
                errors.extend(
                    _validate_reference(
                        root,
                        path,
                        _split_markdown_target(raw),
                        decoded,
                        anchor_cache,
                    )
                )
            parser = _HTMLReferences()
            parser.feed(visible)
            for tag, attr, raw in parser.references:
                errors.extend(
                    _validate_runtime_reference(
                        root, path, tag, attr, raw, decoded, anchor_cache
                    )
                )
            errors.extend(validate_embedded_html_runtime(path, parser))
        elif suffix == ".html":
            parser = _HTMLReferences()
            parser.feed(text)
            for tag, attr, raw in parser.references:
                errors.extend(
                    _validate_runtime_reference(root, path, tag, attr, raw, decoded, anchor_cache)
                )
            errors.extend(validate_embedded_html_runtime(path, parser))
        elif suffix == ".css":
            for raw in CSS_REFERENCE.findall(text):
                errors.extend(
                    _validate_runtime_reference(
                        root,
                        path,
                        "css",
                        "url",
                        raw.strip("'\""),
                        decoded,
                        anchor_cache,
                    )
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
