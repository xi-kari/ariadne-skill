# Ariadne

Ariadne is a modular methodology skill suite powered by the **Lattice Kernel**.

This repository contains the primary Ariadne router, nine standalone peer modules, the Lattice Kernel references, the Method Record schema, frozen evaluations, and repository validators.

## Execution status

<!-- ariadne-stage-status:start -->
| Phase | Status |
|---|---|
| RED_BASELINE | complete |
| BUILD_ALL_CONTENT | complete |
| WHOLE_SUITE_CONTENT_COMPLETE | complete |
| INTEGRATED_REVIEW | complete |
| WHOLE_SUITE_REPAIR | complete |
| WORKER_FINAL_VALIDATION | complete |
| PARENT_INDEPENDENT_VALIDATION | complete |
| RELEASE | not_authorized |
<!-- ariadne-stage-status:end -->

The complete-content gate, integrated review, consolidated repair, and independent parent validation are complete. Repository publication follows the approved implementation plan; global installation, release tags, and package publication remain unauthorized.

## Identity

- External name: **Ariadne**
- Repository and primary skill: **`ariadne-skill`**
- Methodology kernel: **Lattice Kernel**

## Use and validation

Invoke the local skills explicitly by name or repository path. Do not install this development worktree into a global skill directory.

```powershell
python -X utf8 -B -m pytest -q
python -X utf8 -B scripts/validate_repo.py
python -X utf8 -B scripts/validate_evals.py
```

## Design documents

- [Design specification](docs/superpowers/specs/2026-08-03-ariadne-lattice-kernel-design.md)
- [Implementation plan](docs/superpowers/plans/2026-08-03-ariadne-skill-implementation.md)

The source DOCX is not distributed in this repository. See [source coverage](docs/source-coverage.md) for the owned methodology map.
