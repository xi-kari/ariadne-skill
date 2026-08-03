# Ariadne Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to execute this plan. Do not use a workflow that inserts reviewer gates between module builds; Ariadne requires a whole-suite build before integrated review.

**Goal:** Build the complete ten-skill Ariadne methodology suite, powered by the Lattice Kernel, as an isolated and globally distributable repository while keeping local development explicitly invoked.

**Architecture:** One primary router coordinates nine standalone peer modules through a versioned common method record. Detailed methodology contracts use one-level references, while repository tests enforce naming, metadata, source coverage, record compatibility, and the boundary between reasoning and authorization.

**Tech Stack:** Agent Skills Markdown, YAML `agents/openai.yaml`, JSON Schema, Python 3.10, PyYAML 6.x, pytest 9.x, the local Skill Creator scripts, Git, and GitHub.

## Global Constraints

- External name is **Ariadne**; repository and primary skill are **`ariadne-skill`**; methodology kernel is **Lattice Kernel**.
- All installable modules use the `ariadne-*` namespace and remain independent of every other repository.
- The DOCX v8.2 source is authoritative; the referenced conversation is secondary design context.
- Do not copy the source DOCX into GitHub.
- Set `policy.allow_implicit_invocation: true` for global distribution.
- On this workstation, use explicit invocation or direct repository paths; do not install, copy, or link Ariadne into a global skill directory.
- Run no-skill baseline evaluations before writing production skill content.
- Build every planned skill body, reference, metadata file, contract, evaluation prompt, and validator before any integrated review or forward test.
- Do not request user approval, dispatch reviewers, publish partial branches, or make per-module quality decisions during the whole-suite content phase.
- After the complete-content gate, review the full suite once, correct findings across the suite, then rerun the complete validation surface.
- Keep installable Skill files free of development diary text and iteration explanations.

## Mandatory phase gate

The execution order is fixed:

```text
RED BASELINE
  -> BUILD ALL CONTENT
  -> WHOLE_SUITE_CONTENT_COMPLETE
  -> INTEGRATED REVIEW
  -> WHOLE_SUITE REPAIR
  -> FINAL VALIDATION AND RELEASE
```

Before `WHOLE_SUITE_CONTENT_COMPLETE`, do not run module reviews, forward tests, polish passes, partial release checks, or user checkpoints. Baseline evaluation is allowed before the build because it defines the failures the complete suite must correct. Local commits may preserve work, but nothing is pushed as a partial implementation.

## Planned file map

### Primary router

- `skills/ariadne-skill/SKILL.md`
- `skills/ariadne-skill/agents/openai.yaml`
- `skills/ariadne-skill/references/lattice-kernel.md`
- `skills/ariadne-skill/references/routing.md`
- `skills/ariadne-skill/references/method-record.md`

### Peer modules

- `skills/ariadne-framing/{SKILL.md,agents/openai.yaml,references/object-contract.md}`
- `skills/ariadne-evidence/{SKILL.md,agents/openai.yaml,references/evidence-contracts.md}`
- `skills/ariadne-scale/{SKILL.md,agents/openai.yaml,references/scale-transformations.md}`
- `skills/ariadne-mechanism/{SKILL.md,agents/openai.yaml,references/mechanism-contracts.md}`
- `skills/ariadne-human/{SKILL.md,agents/openai.yaml,references/human-domain.md}`
- `skills/ariadne-dynamics/{SKILL.md,agents/openai.yaml,references/dynamic-derivation.md}`
- `skills/ariadne-forecast/{SKILL.md,agents/openai.yaml,references/forecast-contract.md}`
- `skills/ariadne-choice/{SKILL.md,agents/openai.yaml,references/choice-and-authorization.md}`
- `skills/ariadne-audit/{SKILL.md,agents/openai.yaml,references/gates-and-governance.md}`

### Repository contracts and evaluation

- `schemas/method-record.schema.json`
- `scripts/validate_repo.py`
- `tests/test_repository_contracts.py`
- `tests/test_method_record_schema.py`
- `evals/rubric.md`
- `evals/baseline-scenarios.md`
- `evals/standalone-scenarios.md`
- `evals/chain-scenarios.md`
- `evals/cluster-scenarios.md`
- `docs/source-coverage.md`

## Exact trigger descriptions

| Skill | Frontmatter description |
|---|---|
| `ariadne-skill` | `Use when a complex problem requires multiple Lattice Kernel modules, a full methodology pass, or coordinated framing, evidence, scale, mechanism, dynamics, forecast, choice, and audit work.` |
| `ariadne-framing` | `Use when a problem has an unclear object, boundary, time window, scale, identity criterion, task type, or requested output level.` |
| `ariadne-evidence` | `Use when claims, sources, observations, causal stories, analogies, counterevidence, or evidence strength must be separated and audited.` |
| `ariadne-scale` | `Use when reasoning crosses individual and collective levels, short and long time windows, local and global scopes, nested circles, representations, or vocabularies.` |
| `ariadne-mechanism` | `Use when a task needs competing mechanisms, channels, feedback, constraints, baselines, residuals, or conditional structural explanations.` |
| `ariadne-human` | `Use when analyzing people, relationships, teams, organizations, institutions, power, privacy, roles, responsibility, or human meaning without personality or clinical diagnosis.` |
| `ariadne-dynamics` | `Use when a task asks how events propagate through states, clocks, thresholds, feedback loops, circles, branches, scenarios, or recursive simulations.` |
| `ariadne-forecast` | `Use when a future claim needs a target, deadline, frozen inputs, simple baseline, calibration, early and reverse signals, failure semantics, or result writeback.` |
| `ariadne-choice` | `Use when comparing action, delay, experiment, exit, or inaction while separating facts, values, authorization, limits, stopping, rollback, and remedy.` |
| `ariadne-audit` | `Use when a high-impact judgment, automated output, public claim, governance process, or completed Ariadne record needs gates, challenge, appeal, downgrade, rollback, retirement, or AI-boundary review.` |

## Task 1: Establish the RED baseline before Skill content

**Files:**

- Create: `evals/rubric.md`
- Create: `evals/baseline-scenarios.md`
- Create: `evals/standalone-scenarios.md`
- Create: `evals/chain-scenarios.md`
- Create: `evals/cluster-scenarios.md`

**Produces:** Frozen prompts and scoring rules that expose object invention, evidence jumps, scale collapse, mechanism storytelling, post-hoc forecasting, unauthorized recommendations, personality inference, and missing appeal or rollback.

- [ ] Write eight composite no-guidance scenarios covering all ten planned skills; each scenario names observable failure conditions without revealing the desired answer.
- [ ] Run each no-guidance scenario in a fresh context and record the exact failure pattern outside installable skill directories.
- [ ] Confirm that the controls actually exhibit the target failures. Remove any scenario whose control already behaves correctly.
- [ ] Freeze the surviving prompts and rubric before creating any `skills/` content.
- [ ] Commit locally with `test: add Ariadne baseline evaluations`; do not push.

## Task 2: Scaffold the complete namespace and common contracts

**Files:**

- Create every directory under `skills/` listed in the file map.
- Create: `schemas/method-record.schema.json`
- Create: `tests/test_repository_contracts.py`
- Create: `tests/test_method_record_schema.py`
- Create: `scripts/validate_repo.py`
- Create: `docs/source-coverage.md`

**Interfaces:**

- `method-record.schema.json` requires `record_id`, `schema_version`, `record_version`, `request_type`, `object_contract`, `evidence_cutoff`, `scale_scope`, `claim_ledger`, `unknowns_and_counterevidence`, `output_ceiling`, `module_runs`, `recommended_next_modules`, and `authorization_effect`.
- `authorization_effect` accepts only `none`.
- `output_ceiling` accepts only `description_only`, `diagnostic_only`, and `requirements_only`.
- A child record identifies its parent and never overwrites it.

- [ ] Create all ten Skill directories with the verified local `init_skill.py`, using `--resources references` and exact `display_name`, `short_description`, and `$skill-name` default prompts.
- [ ] Add `policy.allow_implicit_invocation: true` to every generated `agents/openai.yaml`.
- [ ] Implement the JSON Schema and repository tests before writing the Skill bodies.
- [ ] Make `validate_repo.py` check namespace isolation, required files, frontmatter fields, UI metadata, one-level references, record-schema examples, source coverage, and absence of unfinished template markers.
- [ ] Do not run review or forward-test commands in this task.
- [ ] Commit locally with `build: scaffold complete Ariadne suite`; do not push.

Use these verified local tools during execution:

```powershell
$creator = 'C:\Users\cangm\.codex\skills\.system\skill-creator\scripts'
python "$creator\init_skill.py" ariadne-skill --path skills --resources references --interface "display_name=Ariadne" --interface "short_description=Coordinate complete Lattice Kernel methodology work" --interface 'default_prompt=Use $ariadne-skill to apply the complete Lattice Kernel methodology to this problem.'
python "$creator\init_skill.py" ariadne-framing --path skills --resources references --interface "display_name=Ariadne Framing" --interface "short_description=Frame objects, boundaries, scales, and output types" --interface 'default_prompt=Use $ariadne-framing to define the object, boundary, time window, scale, and output type.'
python "$creator\init_skill.py" ariadne-evidence --path skills --resources references --interface "display_name=Ariadne Evidence" --interface "short_description=Audit claims, evidence, causes, analogies, and limits" --interface 'default_prompt=Use $ariadne-evidence to separate claims, sources, evidence, causes, analogies, and support limits.'
python "$creator\init_skill.py" ariadne-scale --path skills --resources references --interface "display_name=Ariadne Scale" --interface "short_description=Audit scale changes, circle mappings, and translation loss" --interface 'default_prompt=Use $ariadne-scale to audit scale changes, circle mappings, and translation losses.'
python "$creator\init_skill.py" ariadne-mechanism --path skills --resources references --interface "display_name=Ariadne Mechanism" --interface "short_description=Compare mechanisms, baselines, channels, and residuals" --interface 'default_prompt=Use $ariadne-mechanism to compare mechanisms, channels, baselines, falsifiers, and residuals.'
python "$creator\init_skill.py" ariadne-human --path skills --resources references --interface "display_name=Ariadne Human" --interface "short_description=Analyze human systems with power, privacy, and role boundaries" --interface 'default_prompt=Use $ariadne-human to analyze human systems while preserving power, privacy, role, and responsibility boundaries.'
python "$creator\init_skill.py" ariadne-dynamics --path skills --resources references --interface "display_name=Ariadne Dynamics" --interface "short_description=Derive event paths across clocks, thresholds, and feedback" --interface 'default_prompt=Use $ariadne-dynamics to derive event paths across states, clocks, thresholds, feedback, and branches.'
python "$creator\init_skill.py" ariadne-forecast --path skills --resources references --interface "display_name=Ariadne Forecast" --interface "short_description=Register bounded forecasts, calibration, and failure semantics" --interface 'default_prompt=Use $ariadne-forecast to register a bounded forecast with a baseline, deadline, calibration, and failure semantics.'
python "$creator\init_skill.py" ariadne-choice --path skills --resources references --interface "display_name=Ariadne Choice" --interface "short_description=Compare action and inaction within value and authority limits" --interface 'default_prompt=Use $ariadne-choice to compare action, delay, experiment, exit, and inaction within value and authority limits.'
python "$creator\init_skill.py" ariadne-audit --path skills --resources references --interface "display_name=Ariadne Audit" --interface "short_description=Audit high-impact judgments, appeals, rollback, and retirement" --interface 'default_prompt=Use $ariadne-audit to audit a high-impact judgment for gates, appeal, rollback, downgrade, and retirement.'
```

## Task 3: Build the entire Lattice Kernel Skill group

**Files:** All primary-router and peer-module files in the planned file map.

**Consumes:** Frozen baseline scenarios, the approved design specification, the v8.2 source, and the common method-record schema.

**Produces:** The complete router, nine standalone modules, their references, metadata, routing rules, examples embedded in references, and source-coverage mapping.

- [ ] Write `lattice-kernel.md` with the twelve invariants, output types, missing-state semantics, evidence and authorization ceilings, and self-governance boundary.
- [ ] Write `method-record.md` and `routing.md` so standalone, sequential, clustered, continuous, and full-suite modes use the same record semantics.
- [ ] Write all ten `SKILL.md` files in imperative form. Keep each body focused on trigger response, procedure, input/output contract, stopping conditions, and reference routing.
- [ ] Write every module reference listed in the file map, covering its assigned v8.2 sections without copying the DOCX wholesale.
- [ ] Make the router select only applicable modules, parallelize only after object and evidence cutoffs are frozen, and merge through `ariadne-audit`.
- [ ] Make every standalone module create a minimal valid record, preserve unknowns, and declare its output ceiling.
- [ ] Complete all `agents/openai.yaml` files with exact display names, 25-64 character short descriptions, explicit `$skill-name` prompts, and implicit invocation enabled.
- [ ] Complete `docs/source-coverage.md` with a section-level mapping for all sixteen parts and appendices A-D.
- [ ] Add no cross-repository imports, mirrors, symlinks, global installation steps, development narration, or partial release artifacts.
- [ ] Confirm the whole-suite content-complete gate: every planned file exists, every source area has an owner, every module has standalone instructions, every handoff uses the common record, and no generated template text remains.
- [ ] Only after every preceding item is complete, commit locally with `feat: implement complete Ariadne Lattice Kernel suite`; do not push.

## Task 4: Perform the first integrated review after content completion

**Files:** Review the complete repository; do not review isolated modules as separate acceptance units.

**Gate:** Start only after Task 3 records `WHOLE_SUITE_CONTENT_COMPLETE` in the execution log.

- [ ] Run the verified Skill Creator validator for all ten skills:

```powershell
$validator = 'C:\Users\cangm\.codex\skills\.system\skill-creator\scripts\quick_validate.py'
Get-ChildItem -LiteralPath skills -Directory | Sort-Object Name | ForEach-Object {
    python $validator $_.FullName
    if ($LASTEXITCODE -ne 0) { throw "Skill validation failed: $($_.Name)" }
}
```
- [ ] Run `python -m pytest -q` and `python scripts/validate_repo.py` from the repository root.
- [ ] Run all frozen scenarios with each relevant standalone skill.
- [ ] Run sequential and clustered versions of the same composite scenarios and compare frozen facts, unknowns, lineage, output ceilings, and `authorization_effect`.
- [ ] Run the full router against the same scenarios used in the no-guidance baseline and score improvement with the frozen rubric.
- [ ] Dispatch one independent whole-repository review only now. Give it the repository and raw spec, not suspected defects or expected conclusions.
- [ ] Consolidate all findings into one whole-suite correction set; do not accept or reject modules separately.

Expected validation environment:

```powershell
python -c "import yaml, pytest; print(yaml.__version__); print(pytest.__version__)"
python -m pytest -q
python scripts/validate_repo.py
```

## Task 5: Apply whole-suite corrections and validate release state

**Files:** Modify any Ariadne file implicated by the integrated findings; update the root planning-status text only after all checks pass.

- [ ] Apply the consolidated correction set across the complete suite.
- [ ] Rerun all ten quick validations, the full pytest suite, repository validation, standalone scenarios, chain scenarios, cluster scenarios, and router scenarios.
- [ ] Confirm that clustered and sequential results preserve the same frozen facts, unknowns, lineage, output ceilings, and non-authorization effect.
- [ ] Confirm that local evaluation used explicit invocation or repository paths and that no global skill directory changed.
- [ ] Review the final Git diff once for source fidelity, namespace isolation, cleanliness, and absence of unrelated files.
- [ ] Commit locally with `fix: close integrated Ariadne review findings`.

## Task 6: Publish only the completed and validated suite

**Files:** No new Skill behavior is introduced in this task.

- [ ] Build on branch `codex/lattice-kernel-v1`; do not push it before Tasks 3-5 finish.
- [ ] After final validation, push the completed branch and merge it to `main` without publishing an intermediate Skill release.
- [ ] Push the validated `main` branch to `origin`.
- [ ] Verify `https://github.com/xi-kari/ariadne-skill` shows the complete suite and planning documents.
- [ ] Do not install globally, create a release tag, or publish a package unless the user gives a separate instruction.

## Plan self-review result

- Every design requirement maps to an implementation task.
- Exact file ownership, triggers, record fields, gates, commands, and completion criteria are specified.
- The plan contains one review phase after whole-suite content completion and no per-module review loop.
- No implementation work is authorized by this planning commit; execution begins only on a later user instruction.
