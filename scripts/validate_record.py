"""Command wrapper for the optional legacy Method Record validator.

The implementation ships with the installable skill at
skills/ariadne-skill/scripts/validate_record.py so that installed copies and
this repository run exactly the same checks.
"""
from __future__ import annotations

import sys
try:
    from .legacy_record import implementation
except ImportError:
    from legacy_record import implementation


def _load():
    return implementation


if __name__ == "__main__":
    sys.exit(_load().main())
