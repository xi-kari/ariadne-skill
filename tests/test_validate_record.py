from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from scripts.validate_repo import (
    extract_marked_method_record_lineages,
    extract_marked_method_records,
)

ROOT = Path(__file__).resolve().parents[1]
BUNDLED = ROOT / "skills" / "ariadne-skill" / "scripts" / "validate_record.py"


def _bundled():
    spec = importlib.util.spec_from_file_location("bundled_validate_record", BUNDLED)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_bundled_validator_accepts_every_marked_repository_example() -> None:
    module = _bundled()
    schema = json.loads(
        (ROOT / "schemas" / "method-record.schema.json").read_text(encoding="utf-8")
    )
    checked = 0
    for path in sorted((ROOT / "skills").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for record in extract_marked_method_records(text):
            findings, mode = module.schema_errors(record, schema)
            assert findings == [], (path, findings)
            semantic, _skipped = module.semantic_errors(record, None)
            assert semantic == [], (path, semantic)
            checked += 1
        for lineage in extract_marked_method_record_lineages(text):
            for index, record in enumerate(lineage):
                context = [other for position, other in enumerate(lineage) if position != index]
                findings, _mode = module.schema_errors(record, schema)
                assert findings == [], (path, findings)
                semantic, _skipped = module.semantic_errors(record, context)
                assert semantic == [], (path, semantic)
                checked += 1
    assert checked >= 4


def test_bundled_validator_rejects_a_broken_record() -> None:
    module = _bundled()
    schema = json.loads(
        (ROOT / "schemas" / "method-record.schema.json").read_text(encoding="utf-8")
    )
    text = (ROOT / "skills/ariadne-skill/references/l1-record-template.md").read_text(
        encoding="utf-8"
    )
    record = extract_marked_method_records(text)[0]
    record["output_ceiling"] = "diagnostic_only"
    semantic, _skipped = module.semantic_errors(record, None)
    assert any("description_only" in finding for finding in semantic)
    record["authorization_effect"] = "granted"
    findings, _mode = module.schema_errors(record, schema)
    assert findings
