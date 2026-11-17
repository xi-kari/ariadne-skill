"""Repository access to the installable legacy record implementation.

Method Record 2.0/2.1 remains an optional compatibility format. Its schema and
semantic rules live in the installed package; repository checks reuse them.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path


IMPLEMENTATION_PATH = (
    Path(__file__).resolve().parents[1]
    / "skills/ariadne-skill/scripts/validate_record.py"
)


def _load():
    spec = importlib.util.spec_from_file_location("ariadne_legacy_record", IMPLEMENTATION_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load legacy record implementation: {IMPLEMENTATION_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


implementation = _load()

__all__ = [
    "CEILING_RANK",
    "SCHEMA_PATH",
    "method_record_validator",
    "validate_method_record",
    "validate_record_semantics",
    "extract_marked_method_records",
    "extract_marked_method_record_lineages",
    "methodology_extension_errors",
    "claim_dependency_errors",
    "scale_scope_errors",
    "choice_payload_errors",
    "strong_judgment_errors",
    "schema_errors",
    "semantic_errors",
    "load_record",
    "main",
]

for _name in __all__:
    globals()[_name] = getattr(implementation, _name)
