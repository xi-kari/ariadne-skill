"""Repository-root wrapper for the bundled single-record validator.

The implementation ships with the installable skill at
skills/ariadne-skill/scripts/validate_record.py so that installed copies and
this repository run exactly the same checks.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

BUNDLED = Path(__file__).resolve().parents[1] / "skills" / "ariadne-skill" / "scripts" / "validate_record.py"


def _load():
    spec = importlib.util.spec_from_file_location("ariadne_validate_record", BUNDLED)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    sys.exit(_load().main())
