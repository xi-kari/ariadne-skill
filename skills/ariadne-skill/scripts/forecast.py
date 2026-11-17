"""Register a dated forecast locally and append explicit outcome observations.

Requires Python 3.10+ and jsonschema. No network, model invocation, scoring, or
background monitoring occurs. Safe registry access requires POSIX dir_fd and
O_NOFOLLOW support; unsupported filesystems fail closed.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import stat
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

import jsonschema


SCHEMA_PATH = Path(__file__).resolve().parents[1] / "contracts/forecast.schema.json"
SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}\Z")
RFC3339 = re.compile(
    r"\d{4}-\d{2}-\d{2}[Tt](?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d"
    r"(?:\.\d+)?(?:[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)\Z"
)


class ForecastError(ValueError):
    """A record or registry operation failed its explicit contract."""


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def stamp(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def parse_time(value: str) -> datetime:
    if not isinstance(value, str) or not RFC3339.fullmatch(value):
        raise ForecastError("timestamps require RFC 3339 with a timezone and seconds 00-59")
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        return datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ForecastError("timestamp has an invalid date or offset") from exc


FORMAT_CHECKER = jsonschema.FormatChecker()


@FORMAT_CHECKER.checks("date-time")
def valid_time(value: object) -> bool:
    if not isinstance(value, str):
        return True
    try:
        parse_time(value)
    except ForecastError:
        return False
    return True


def _unique(items: list[str], label: str) -> set[str]:
    if len(items) != len(set(items)):
        raise ForecastError(f"{label} must be unique")
    return set(items)


def _references(items: list[str], known: set[str], label: str) -> None:
    missing = set(items) - known
    if missing:
        raise ForecastError(f"{label} contains unknown references: {', '.join(sorted(missing))}")


def validate_artifact(value: dict) -> None:
    try:
        json.dumps(value, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise ForecastError("artifact must contain only finite JSON values") from exc
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=FORMAT_CHECKER)
    error = next(validator.iter_errors(value), None)
    if error is not None:
        # Avoid dumping the full input, which may contain private observations.
        raise ForecastError("artifact does not match forecast.schema.json; check type, required fields, expression and timestamps")
    for identifier in ("forecast_id", "resolution_id"):
        if identifier in value:
            _safe_id(value[identifier])
    kind = value["artifact_type"]
    if kind in {"forecast_draft", "forecast_registration"}:
        sources = value["input"]["sources"]
        source_ids = _unique([s["source_id"] for s in sources], "input source IDs")
        mechanism_ids = _unique([m["candidate_id"] for m in value["mechanisms"]], "mechanism IDs")
        path_ids = _unique([p["path_id"] for p in value["paths"]], "path IDs")
        cutoff = parse_time(value["input"]["cutoff"])
        baseline_time = parse_time(value["baseline"]["as_of"])
        start = parse_time(value["window"]["starts_at"])
        deadline = parse_time(value["window"]["deadline"])
        writeback = parse_time(value["review"]["writeback_due_at"])
        review = parse_time(value["review"]["next_review_at"])
        if not baseline_time <= cutoff <= start <= deadline < writeback or not cutoff <= review <= writeback:
            raise ForecastError("chronology requires baseline <= cutoff <= start <= deadline < writeback, and cutoff <= review <= writeback")
        if any(parse_time(s["available_at"]) > cutoff for s in sources):
            raise ForecastError("an input source was available only after the frozen cutoff")
        for item in value["mechanisms"]:
            _references(item["basis_source_ids"], source_ids, "mechanism basis")
        for item in value["paths"]:
            _references(item["basis_source_ids"], source_ids, "path basis")
            _references(item["mechanism_ids"], mechanism_ids, "path mechanisms")
        expression = value["expression"]
        _references(expression.get("basis_source_ids", []), source_ids, "expression basis")
        if expression["kind"] == "path_ranking":
            ranked = [item for tier in expression["tiers"] for item in tier]
            _unique(ranked, "ranked path IDs")
            _references(ranked, path_ids, "path ranking")
        elif expression["kind"] == "scenario_weight":
            weighted = [item["path_id"] for item in expression["weights"]]
            _unique(weighted, "weighted path IDs")
            _references(weighted, path_ids, "scenario weights")
        if kind == "forecast_registration":
            registered = parse_time(value["registered_at"])
            if not cutoff <= registered < deadline or review < registered:
                raise ForecastError("registration must precede deadline and review and follow the input cutoff")
    else:
        _unique([s["source_id"] for s in value["sources"]], "observation source IDs")
        if value["status"] in {"supported", "not_supported"} and not any(
            s["kind"] in {"observed", "reported"} for s in value["sources"]
        ):
            raise ForecastError("settled outcomes need an observed or reported outcome source")
        if kind == "forecast_resolution":
            resolved = parse_time(value["resolved_at"])
            if parse_time(value["observed_at"]) > resolved:
                raise ForecastError("observation cannot be dated after resolution")
            if any(parse_time(s["available_at"]) > resolved for s in value["sources"]):
                raise ForecastError("an observation source is not yet available at resolution")


def _safe_id(value: str) -> None:
    if not isinstance(value, str) or not SAFE_ID.fullmatch(value):
        raise ForecastError("IDs allow 1-80 letters, digits, underscores or hyphens and start with a letter or digit")


@contextmanager
def _directory(path: Path, create: bool = False):
    """Walk directories without following symlinks, holding a final dir_fd."""
    if not hasattr(os, "O_NOFOLLOW") or os.open not in os.supports_dir_fd:
        raise ForecastError("safe registry access requires POSIX dir_fd and O_NOFOLLOW support")
    path = Path(path)
    if ".." in path.parts:
        raise ForecastError("registry and input paths cannot contain parent traversal segments")
    absolute = path.absolute()
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    current = os.open(absolute.anchor, flags)
    try:
        for component in absolute.parts[1:]:
            if create:
                try:
                    os.mkdir(component, mode=0o700, dir_fd=current)
                except FileExistsError:
                    pass
            child = os.open(component, flags, dir_fd=current)
            os.close(current)
            current = child
        yield current
    except OSError as exc:
        raise ForecastError("directory is unavailable, unsafe, or a symbolic link") from exc
    finally:
        os.close(current)


def _read_at(directory: int, name: str) -> bytes:
    try:
        descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory)
        with os.fdopen(descriptor, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ForecastError("artifact must be a regular file")
            return stream.read()
    except OSError as exc:
        raise ForecastError("artifact is unreadable or a symbolic link") from exc


def _decode(raw: bytes) -> dict:
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ForecastError("JSON contains a duplicate field")
            result[key] = value
        return result
    def reject_constant(_value):
        raise ForecastError("JSON numbers must be finite")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_keys, parse_constant=reject_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ForecastError("input must be a valid UTF-8 JSON artifact") from exc
    if not isinstance(value, dict):
        raise ForecastError("input must be a JSON object")
    return value


def load_json(path: Path) -> dict:
    path = Path(path)
    if ".." in path.parts:
        raise ForecastError("input path cannot contain parent traversal segments")
    with _directory(path.parent) as directory:
        return _decode(_read_at(directory, path.name))


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _write_new(directory: int, name: str, value: dict) -> bytes:
    raw = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    try:
        descriptor = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=directory)
    except FileExistsError as exc:
        raise ForecastError("artifact already exists; overwrite is forbidden") from exc
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        if _read_at(directory, name) != raw:
            raise ForecastError("artifact readback differs from the written bytes")
        os.fsync(directory)
    except BaseException:
        # Remove only this operation's new incomplete file, never an older one.
        os.unlink(name, dir_fd=directory)
        raise
    return raw


def register(draft: dict, registry: Path) -> Path:
    validate_artifact(draft)
    if draft["artifact_type"] != "forecast_draft":
        raise ForecastError("register accepts only a forecast_draft")
    now = utc_now()
    if parse_time(draft["input"]["cutoff"]) > now:
        raise ForecastError("registration input cutoff is in the future")
    if parse_time(draft["window"]["deadline"]) <= now:
        raise ForecastError("registration deadline has already arrived")
    value = copy.deepcopy(draft)
    value.update(artifact_type="forecast_registration", registered_at=stamp(now))
    validate_artifact(value)
    forecast_id = value["forecast_id"]
    _safe_id(forecast_id)
    with _directory(Path(registry), create=True) as root:
        try:
            os.mkdir(forecast_id, mode=0o700, dir_fd=root)
        except FileExistsError as exc:
            raise ForecastError("forecast ID already exists; frozen registrations cannot be replaced") from exc
        with _directory(Path(registry) / forecast_id) as directory:
            _write_new(directory, "forecast.json", value)
    return Path(registry).absolute() / forecast_id / "forecast.json"


def resolve(forecast_id: str, observation: dict, registry: Path) -> Path:
    _safe_id(forecast_id)
    validate_artifact(observation)
    if observation["artifact_type"] != "resolution_draft":
        raise ForecastError("resolve accepts only a resolution_draft")
    folder = Path(registry) / forecast_id
    with _directory(folder) as directory:
        original = _read_at(directory, "forecast.json")
        frozen = _decode(original)
        validate_artifact(frozen)
        if frozen["artifact_type"] != "forecast_registration" or frozen["forecast_id"] != forecast_id:
            raise ForecastError("registry location and frozen forecast identity differ")
        if frozen["expression"]["kind"] == "unknown" and observation["status"] in {"supported", "not_supported"}:
            raise ForecastError("an unknown expression is an abstention, not a forecast hit or miss; retain the target observation with status not_evaluable")
        now = utc_now()
        if observation["status"] in {"supported", "not_supported"} and parse_time(observation["observed_at"]) < parse_time(frozen["registered_at"]):
            raise ForecastError("outcome predates registration; append an explicit target_invalid or unresolved review instead of counting a forecast result")
        value = copy.deepcopy(observation)
        value.update(
            artifact_type="forecast_resolution", forecast_id=forecast_id,
            registered_artifact_sha256=sha256_bytes(original), resolved_at=stamp(now),
        )
        validate_artifact(value)
        try:
            os.mkdir("resolutions", mode=0o700, dir_fd=directory)
        except FileExistsError:
            pass
        with _directory(folder / "resolutions") as observations:
            _write_new(observations, value["resolution_id"] + ".json", value)
        if _read_at(directory, "forecast.json") != original:
            raise ForecastError("frozen registration changed during resolution")
    return folder.absolute() / "resolutions" / (value["resolution_id"] + ".json")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    register_parser = commands.add_parser("register", help="freeze a new future-facing forecast")
    register_parser.add_argument("--input", required=True, type=Path)
    register_parser.add_argument("--registry", required=True, type=Path)
    resolve_parser = commands.add_parser("resolve", help="append an outcome observation without changing the forecast")
    resolve_parser.add_argument("--id", required=True)
    resolve_parser.add_argument("--input", required=True, type=Path)
    resolve_parser.add_argument("--registry", required=True, type=Path)
    validate_parser = commands.add_parser("validate", help="check one draft or saved artifact")
    validate_parser.add_argument("artifact", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            value = load_json(args.artifact)
            validate_artifact(value)
            print(json.dumps({"validated": str(args.artifact), "artifact_type": value["artifact_type"], "reality_certified": False}))
        else:
            value = load_json(args.input)
            path = register(value, args.registry) if args.command == "register" else resolve(args.id, value, args.registry)
            readback = load_json(path)
            with _directory(path.parent) as directory:
                digest = sha256_bytes(_read_at(directory, path.name))
            print(json.dumps({"artifact_path": str(path), "artifact_type": readback["artifact_type"], "sha256": digest, "readback_verified": True, "background_monitoring": False}))
    except (ForecastError, OSError, ValueError) as exc:
        print(f"forecast: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
