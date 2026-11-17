# Ariadne Repository Instructions

## Fixed identity

- Use **Ariadne** as the external name.
- Use **`ariadne-skill`** as the repository name and primary installable skill name.
- Use **Lattice Kernel** as the methodology-kernel name.
- Keep `skills/ariadne-skill` as the single installable entry. Internal paths are composable resources, not separate skills.
- Do not depend on, mirror, or modify other skill repositories; the foreign product names banned from installable files are pinned in `FOREIGN_PRODUCT_NAMES` in `scripts/validate_repo.py`.

## Source and scope

- Treat 《Xikari-条件结构与转化论》 (Xikari, v2, 2026-11-16; SHA-256 `6ef2e508474d4ac1ad07d7e4e068955342c405b5f680afcfc40d68cca3d0149c`) as the primary methodology source; the earlier *跨尺度多圈层结构推演框架 v8.2* is superseded and kept only as history in the 2026-08 design documents.
- Keep Ariadne's derived status explicit: it is organized method and retrieval entries with candidate status, bound to the source hash and section anchors, never presented as author-confirmed item by item or as a separate author theory.
- Build a methodology for agent work and human thinking, not an ontology, personality taxonomy, clinical tool, truth engine, or authorization system.
- Do not copy the source text into the public repository.

## Mandatory implementation sequence (historical construction-phase note)

This section records the one-shot order used to build the suite; it is kept for
audit context. Routine maintenance edits do not restart this sequence — they
follow the boundaries above and the pre-commit checks below.

Follow this order without interleaving the phases:

1. Freeze requirements and record no-skill baseline failures.
2. Build the complete content of the primary skill and every module.
3. Confirm the whole-suite content-complete gate.
4. Only then begin integrated review, validation, forward testing, and correction.

Do not review, approve, reject, polish, or forward-test modules one by one while other module content is still incomplete. Do not request user approval between modules. Automated or human review begins only after all planned skill bodies, references, metadata, contracts, evaluation prompts, and repository validators exist.

## Local and publishing boundaries

- Test local skills only by explicit name or direct repository path.
- Do not install this development clone into a global skills directory on the maintainer's workstation; end users installing via the README commands are out of scope for this rule.
- Host smoke verification runs in a disposable container, VM, or throwaway project-scoped directory that never enters any global skills path; record outcomes in the `verification` fields of adapters/compatibility.json.
- Do not publish partial implementation branches or partial skill releases.
- Keep skill files free of iteration narration, development diary text, and version-by-version explanations.

## Before you commit

Run the four validation commands from the repository root and keep them green:

1. `python -X utf8 -B -m pytest -q -p no:cacheprovider`
2. `python -X utf8 -B scripts/validate_repo.py`
3. `python -X utf8 -B scripts/validate_evals.py`
4. `python -X utf8 -B scripts/validate_adapters.py`

CONTRIBUTING.md holds the full workflow, including the site build and `git diff --check`; if a command cannot run, report that honestly instead of describing the change as validated.

These machine-checked invariants break most otherwise-reasonable edits:

- **Release seal.** `RELEASE` is `complete`: the seal was lifted in the reviewed change of 2026-08-26 that shipped the full external-review remediation and tag `v1.0.0`. The stage must stay `complete`; any further release-state change (re-sealing included) requires another reviewed change that updates the assertion in `scripts/validate_repo.py` itself, and no edit to README, plan, or docs alone can change release state.
- **Package manifest.** `skills/ariadne-skill/architecture.json` declares the entry, shared guidance, paths, library, selective contracts, legacy resources, and bundle order. Every package resource must exist, be safe to read, and be reachable from the entry; internal route counts are not fixed.
- **Legacy compatibility.** Method Record 2.0/2.1 remains optional. Its two schema copies stay byte-identical; `skills/ariadne-skill/scripts/validate_record.py` is the sole semantic implementation, imported by repository wrappers. Legacy records do not define ordinary current outputs.
- **Bundle scope.** Rebuild `dist/ariadne-bundle.md` after changes to any manifest-selected guidance. Links to libraries, schemas, and tools must not imply they were embedded, read, or executed.
- **File hygiene.** Every text file must be UTF-8 with LF line endings, no trailing whitespace, and a final newline.
- **Banned markers.** Unfinished-work markers and foreign product names — pinned as `FORBIDDEN_MARKERS` and `FOREIGN_PRODUCT_NAMES` in `scripts/validate_repo.py` — fail validation in any installable file.
