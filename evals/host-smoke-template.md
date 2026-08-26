# Host Smoke Record Template

Copy this template to `evals/host-smoke-<host>-<date>.md` when running the universal smoke contract for a host, then set that host's `verification` field in `adapters/compatibility.json` to `smoke-passed` with the same date. Run in a disposable container or VM, never against the maintainer workstation's global skill directories.

## Environment

- Host and version:
- Install command used (verbatim):
- Install target path confirmed:
- Date (`last_verified` value):

## Check 1: json-references

Prompt the host to read one JSON reference through the skill (for example the `toc` of `human-variable-cards.json`). Paste the command or prompt and the relevant output lines. Pass condition: the host resolves the file from the installed skill directory without inlining the whole file.

## Check 2: peer-routing

Prompt the router with a multi-facet request and one peer intentionally uninstalled. Paste the produced module-run entries. Pass condition: the missing peer appears as `not_run` with reason `module_unavailable`, and the router does not execute the peer's responsibility inline.

## Check 3: context-growth

Ask a trivial question with the suite installed. Paste evidence of what was loaded (host trace, token report, or the visible answer path). Pass condition: only the relevant SKILL.md enters context; references load only when the run's declared depth requires them.

## Verdict

- Result: smoke-passed / failed (with the failing check)
- Follow-up: manifest updated at `adapters/compatibility.json` (yes/no)
