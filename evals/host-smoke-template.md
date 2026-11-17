# Host Smoke Record Template

Copy this template to `evals/host-smoke-<host>-<date>.md` when running the universal smoke contract for a host, then set that host's `verification` field in `adapters/compatibility.json` to `smoke-passed` with the same date. Run in a disposable container or VM, never against the maintainer workstation's global skill directories.

## Environment

- Host and version:
- Install command used (verbatim):
- Install target path confirmed:
- Date (`last_verified` value):

## Check 1: resource-loading

Prompt the host to read a selected library resource through the installed package (for example `field_order` in `references/library/human-variable-cards.json`). Paste the command or prompt and the relevant output lines. Pass condition: the host resolves the file from the installed skill directory without inlining the whole file.

## Check 2: path-routing

Give the single Ariadne entry a request that needs more than one kind of work. Paste the selected internal paths and their actual outputs. Pass condition: the host reads the necessary `paths/` and shared references, composes their responsibilities, and returns the requested result without requiring unavailable peer Skills or a universal legacy record. Also verify that a missing internal resource is reported as an incomplete installation rather than silently invented.

## Check 3: context-growth

Ask a trivial question with the single package installed. Paste evidence of what was loaded (host trace, token report, or the visible answer path). Pass condition: the entry selects proportionate work; only relevant paths and references are loaded, and a simple answer does not trigger the deep library or a mandatory legacy record.

## Verdict

- Result: smoke-passed / failed (with the failing check)
- Follow-up: manifest updated at `adapters/compatibility.json` (yes/no)
