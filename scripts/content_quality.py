from __future__ import annotations

import json
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
FRONTMATTER_BLOCK = re.compile(r"\A---\n.*?\n---\n?", re.DOTALL)

# Byte floors are pinned at roughly 55% of the reviewed method text so that a
# regression cannot hollow a reference into a heading-only shell while CI stays
# green. Raising method text is always allowed; shrinking below a floor fails.
REFERENCE_MARKDOWN_BYTE_FLOORS = {
    "skills/ariadne-skill/references/lattice-kernel.md": 5800,
    "skills/ariadne-skill/references/routing.md": 6000,
    "skills/ariadne-skill/references/method-record.md": 12000,
    "skills/ariadne-framing/references/object-contract.md": 6700,
    "skills/ariadne-evidence/references/evidence-contracts.md": 12900,
    "skills/ariadne-scale/references/scale-transformations.md": 12500,
    "skills/ariadne-mechanism/references/mechanism-contracts.md": 11200,
    "skills/ariadne-human/references/human-domain.md": 23300,
    "skills/ariadne-dynamics/references/dynamic-derivation.md": 11400,
    "skills/ariadne-forecast/references/forecast-contract.md": 10200,
    "skills/ariadne-choice/references/choice-and-authorization.md": 12700,
    "skills/ariadne-audit/references/gates-and-governance.md": 22600,
}
SKILL_BODY_MIN_BYTES = 3000
SKILL_BODY_MIN_H2_SECTIONS = 3
H2_SECTION_MIN_CHARS = 60
HUMAN_CARD_MIN_SERIALIZED_CHARS = 1500
APPLICATION_CONTRACT_MIN_SERIALIZED_CHARS = 800
CARD_STRING_LEAF_MIN_CHARS = 3
# These fields hold source-registered short codes (claim type letters, rule
# codes such as D0/E1, two-character state tokens); they must stay non-empty
# but cannot satisfy the three-character floor that guards free text.
HUMAN_CARD_SHORT_CODE_FIELDS = {
    "additional_inferential_requires",
    "additional_protocol_requires",
    "affected_positions",
    "carrier",
    "claim_type",
    "evidence",
    "field_order",
    "inferential_requires",
    "input_dependencies",
    "output_effects",
    "protocol_requires",
    "required_scale_additions",
    "specializes",
    "state",
}
STATE_PROTOTYPE_IDS = ("S0", "S1", "S2", "S3", "S4", "S5", "S6")
STATE_PROTOTYPE_REQUIRED_FIELDS = (
    "id",
    "name",
    "entry",
    "exit",
    "observables",
    "counterexamples",
    "falsifiers",
    "scale_boundary",
    "evidence_elevation",
    "contract_links",
    "non_authorization",
)
NONLINEAR_PATH_REQUIRED_KEYS = {"id", "meaning", "key_distinction"}
NONLINEAR_PATH_MIN_COUNT = 15
INTERVENTION_LEVEL_IDS = ("T0", "T1", "T2", "T3", "T4")
INTERVENTION_LEVEL_REQUIRED_FIELDS = (
    "id",
    "name",
    "entry_conditions",
    "execution_state_log",
    "stop_or_failure",
    "handoff",
)


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


def _h2_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    fence: tuple[str, int] | None = None
    current: tuple[str, list[str]] | None = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            run = match.group(1)
            marker = run[0]
            if fence is None:
                fence = (marker, len(run))
            elif marker == fence[0] and len(run) >= fence[1]:
                fence = None
            if current is not None:
                current[1].append(line)
            continue
        if fence is None and re.match(r"^##\s+\S", line):
            if current is not None:
                sections.append((current[0], "\n".join(current[1])))
            current = (line.lstrip("#").strip(), [])
            continue
        if current is not None:
            current[1].append(line)
    if current is not None:
        sections.append((current[0], "\n".join(current[1])))
    return sections


def _value_is_populated(value: object) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value) and all(_value_is_populated(item) for item in value)
    if isinstance(value, dict):
        return bool(value) and all(_value_is_populated(item) for item in value.values())
    return value is not None


def _short_string_leaves(node: object, field_name: str | None = None) -> list[str]:
    violations: list[str] = []
    if isinstance(node, dict):
        for key, value in node.items():
            violations.extend(_short_string_leaves(value, key))
    elif isinstance(node, list):
        for value in node:
            violations.extend(_short_string_leaves(value, field_name))
    elif isinstance(node, str):
        floor = 1 if field_name in HUMAN_CARD_SHORT_CODE_FIELDS else CARD_STRING_LEAF_MIN_CHARS
        if len(node.strip()) < floor:
            violations.append(f"{field_name}={node!r}")
    return violations


def _load_card_file(root: Path, relative: str) -> tuple[Path, object | None, list[str]]:
    path = root / relative
    if not path.is_file():
        return path, None, []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        return path, None, [_issue("card-unreadable", root, path, str(exc))]
    if not isinstance(data, dict):
        return path, None, [
            _issue("card-structure", root, path, "top-level value must be a JSON object")
        ]
    return path, data, []


def _validate_human_variable_cards(root: Path) -> list[str]:
    path, data, errors = _load_card_file(
        root, "skills/ariadne-human/references/human-variable-cards.json"
    )
    if data is None or not isinstance(data, dict):
        return errors
    for violation in sorted(set(_short_string_leaves(data))):
        errors.append(
            _issue(
                "card-value-too-short",
                root,
                path,
                f"string leaf under {CARD_STRING_LEAF_MIN_CHARS} chars: {violation}",
            )
        )
    cards = data.get("human_variables")
    if isinstance(cards, list):
        for card in cards:
            if not isinstance(card, dict):
                continue
            serialized = len(json.dumps(card, ensure_ascii=False))
            if serialized < HUMAN_CARD_MIN_SERIALIZED_CHARS:
                errors.append(
                    _issue(
                        "card-below-floor",
                        root,
                        path,
                        f"card {card.get('id')} serializes to {serialized} chars"
                        f" < {HUMAN_CARD_MIN_SERIALIZED_CHARS}",
                    )
                )
    return errors


def _validate_application_contracts(root: Path) -> list[str]:
    path, data, errors = _load_card_file(
        root, "skills/ariadne-audit/references/application-contracts.json"
    )
    if data is None or not isinstance(data, dict):
        return errors
    contracts = data.get("contracts")
    if not isinstance(contracts, list):
        errors.append(_issue("card-structure", root, path, "contracts must be a list"))
        return errors
    for contract in contracts:
        if not isinstance(contract, dict):
            continue
        serialized = len(json.dumps(contract, ensure_ascii=False))
        if serialized < APPLICATION_CONTRACT_MIN_SERIALIZED_CHARS:
            errors.append(
                _issue(
                    "card-below-floor",
                    root,
                    path,
                    f"contract {contract.get('id')} serializes to {serialized} chars"
                    f" < {APPLICATION_CONTRACT_MIN_SERIALIZED_CHARS}",
                )
            )
    return errors


def _validate_state_prototypes(root: Path) -> list[str]:
    path, data, errors = _load_card_file(
        root, "skills/ariadne-human/references/state-prototypes.json"
    )
    if data is None or not isinstance(data, dict):
        return errors
    prototypes = data.get("prototypes")
    if (
        not isinstance(prototypes, list)
        or len(prototypes) != len(STATE_PROTOTYPE_IDS)
        or not all(isinstance(prototype, dict) for prototype in prototypes)
        or [prototype.get("id") for prototype in prototypes] != list(STATE_PROTOTYPE_IDS)
    ):
        errors.append(_issue("card-structure", root, path, "prototypes must cover S0-S6 in order"))
    else:
        for prototype in prototypes:
            for field in STATE_PROTOTYPE_REQUIRED_FIELDS:
                if not _value_is_populated(prototype.get(field)):
                    errors.append(
                        _issue(
                            "card-structure",
                            root,
                            path,
                            f"prototype {prototype.get('id')} needs a non-empty {field}",
                        )
                    )
    nonlinear_paths = data.get("nonlinear_paths")
    if not isinstance(nonlinear_paths, list) or len(nonlinear_paths) < NONLINEAR_PATH_MIN_COUNT:
        errors.append(
            _issue(
                "card-structure",
                root,
                path,
                f"nonlinear_paths must list at least {NONLINEAR_PATH_MIN_COUNT} entries",
            )
        )
    else:
        for entry in nonlinear_paths:
            if (
                not isinstance(entry, dict)
                or set(entry) != NONLINEAR_PATH_REQUIRED_KEYS
                or not all(_value_is_populated(entry[key]) for key in NONLINEAR_PATH_REQUIRED_KEYS)
            ):
                errors.append(
                    _issue(
                        "card-structure",
                        root,
                        path,
                        "each nonlinear path needs non-empty id, meaning and key_distinction",
                    )
                )
                break
    if not _value_is_populated(data.get("x0")):
        errors.append(_issue("card-structure", root, path, "x0 register must be present and non-empty"))
    return errors


def _validate_intervention_levels(root: Path) -> list[str]:
    path, data, errors = _load_card_file(
        root, "skills/ariadne-choice/references/intervention-levels.json"
    )
    if data is None or not isinstance(data, dict):
        return errors
    levels = data.get("levels")
    if (
        not isinstance(levels, list)
        or len(levels) != len(INTERVENTION_LEVEL_IDS)
        or not all(isinstance(level, dict) for level in levels)
        or [level.get("id") for level in levels] != list(INTERVENTION_LEVEL_IDS)
    ):
        errors.append(_issue("card-structure", root, path, "levels must cover T0-T4 in order"))
    else:
        for level in levels:
            for field in INTERVENTION_LEVEL_REQUIRED_FIELDS:
                if not _value_is_populated(level.get(field)):
                    errors.append(
                        _issue(
                            "card-structure",
                            root,
                            path,
                            f"level {level.get('id')} needs a non-empty {field}",
                        )
                    )
    if not _value_is_populated(data.get("execution_state_log_contract")):
        errors.append(
            _issue(
                "card-structure",
                root,
                path,
                "execution_state_log_contract must be present and non-empty",
            )
        )
    return errors


def validate_method_content(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    for relative, floor in REFERENCE_MARKDOWN_BYTE_FLOORS.items():
        path = root / relative
        if not path.is_file():
            continue
        size = path.stat().st_size
        if size < floor:
            errors.append(
                _issue("reference-below-floor", root, path, f"{size} bytes < {floor} byte floor")
            )
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for heading, body in _h2_sections(text):
            if len(body.strip()) < H2_SECTION_MIN_CHARS:
                errors.append(
                    _issue(
                        "thin-h2-section",
                        root,
                        path,
                        f"section {heading!r} body under {H2_SECTION_MIN_CHARS} chars",
                    )
                )

    skills_root = root / "skills"
    if skills_root.is_dir():
        for skill_md in sorted(skills_root.glob("*/SKILL.md")):
            try:
                text = skill_md.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            body = FRONTMATTER_BLOCK.sub("", text, count=1)
            body_bytes = len(body.encode("utf-8"))
            if body_bytes < SKILL_BODY_MIN_BYTES:
                errors.append(
                    _issue(
                        "skill-body-below-floor",
                        root,
                        skill_md,
                        f"{body_bytes} bytes < {SKILL_BODY_MIN_BYTES} byte floor",
                    )
                )
            section_count = len(_h2_sections(body))
            if section_count < SKILL_BODY_MIN_H2_SECTIONS:
                errors.append(
                    _issue(
                        "skill-body-missing-sections",
                        root,
                        skill_md,
                        f"{section_count} H2 sections < {SKILL_BODY_MIN_H2_SECTIONS}",
                    )
                )

    errors.extend(_validate_human_variable_cards(root))
    errors.extend(_validate_application_contracts(root))
    errors.extend(_validate_state_prototypes(root))
    errors.extend(_validate_intervention_levels(root))
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

    errors.extend(validate_method_content(root))
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
