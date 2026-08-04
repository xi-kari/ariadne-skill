# Ariadne Chinese README Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Do not review partial README content; finish the entire deliverable before the unified review gate.

**Goal:** Replace the short English README with a Chinese Ariadne methodology landing page and two independent C-style SVG visuals that explain all ten Skills.

**Architecture:** `README.md` is the human-facing entrypoint. `docs/assets/readme-hero.svg` carries the Ariadne identity and approved positioning; `docs/assets/lattice-kernel-map.svg` shows the one-router/nine-peer, on-demand collaboration model. The README links every module contract and repeats no implementation diary.

**Tech Stack:** GitHub-flavored Markdown, accessible SVG 1.1/XML, repository-local Python validators, PowerShell verification.

## Global Constraints

- Use **Ariadne** as the external name, **`ariadne-skill`** as the repository and primary Skill, and **Lattice Kernel** as the methodology kernel.
- Use the approved line: “一套让 AI Agent 思考和处理复杂问题的方法论集群。”
- Use Chinese for explanatory copy; retain only fixed brand names, Skill IDs, field names, and commands in English.
- Implement the full README and both SVG files before any content, visual, or contract review.
- Do not modify Skills, schemas, validators, evals, CrossFrame, global Skill directories, or publication state.
- Keep `authorization_effect: none`; never present forecast, choice, audit, or module agreement as reality or authorization.
- Do not add a website, Release, License, installer, or unsupported capability claim.

---

### Task 1: Build the complete README deliverable

**Files:**
- Modify: `README.md`
- Create: `docs/assets/readme-hero.svg`
- Create: `docs/assets/lattice-kernel-map.svg`
- Reference: `docs/superpowers/specs/2026-08-04-ariadne-readme-redesign.md`
- Reference: `skills/ariadne-skill/SKILL.md`
- Reference: `skills/ariadne-framing/SKILL.md`
- Reference: `skills/ariadne-evidence/SKILL.md`
- Reference: `skills/ariadne-scale/SKILL.md`
- Reference: `skills/ariadne-mechanism/SKILL.md`
- Reference: `skills/ariadne-human/SKILL.md`
- Reference: `skills/ariadne-dynamics/SKILL.md`
- Reference: `skills/ariadne-forecast/SKILL.md`
- Reference: `skills/ariadne-choice/SKILL.md`
- Reference: `skills/ariadne-audit/SKILL.md`

**Interfaces:**
- Consumes: the approved C palette, fixed identity, real Skill contracts, current local-only invocation boundary, and existing validation commands.
- Produces: one complete Chinese README plus two relative-linked, accessible SVG assets.

- [ ] **Step 1: Record the expected RED baseline**

Run before editing:

```powershell
$required = @(
  '一套让 AI Agent 思考和处理复杂问题的方法论集群。',
  'ariadne-framing', 'ariadne-evidence', 'ariadne-scale',
  'ariadne-mechanism', 'ariadne-human', 'ariadne-dynamics',
  'ariadne-forecast', 'ariadne-choice', 'ariadne-audit'
)
$missing = $required | Where-Object { -not (Select-String -LiteralPath README.md -SimpleMatch $_ -Quiet) }
if ($missing.Count -eq 0 -and
    (Test-Path -LiteralPath 'docs/assets/readme-hero.svg') -and
    (Test-Path -LiteralPath 'docs/assets/lattice-kernel-map.svg')) {
  throw 'Expected the pre-implementation README baseline to be incomplete.'
}
throw "RED: README deliverable is incomplete; missing $($missing.Count) required content items or SVG assets."
```

Expected: command exits non-zero with `RED: README deliverable is incomplete`.

- [ ] **Step 2: Create both approved SVG assets without reviewing either as a final deliverable**

Create `docs/assets/readme-hero.svg` with the exact palette `#EDF2EF`, `#173532`, `#B7CBC4`, `#8B62AD`, and `#C4874F`; include `role="img"`, a Chinese `aria-label`, the Ariadne/Lattice Kernel identity, the approved line, grid nodes, and a path/thread motif.

Create `docs/assets/lattice-kernel-map.svg` with these labeled groups: `ariadne-skill` router; framing/evidence freeze; scale/mechanism/human parallel peers; dynamics/forecast/choice conditional continuation; audit merge/governance. Include “按需选取，不是每次全跑” and a Chinese `aria-label`.

- [ ] **Step 3: Replace README with the complete Chinese information architecture**

Write, in order: centered Hero and badges; four-column facts; numbered directory; Ariadne identity, human-thinking use, and non-goals; Lattice Kernel map with text fallback; ten-Skill quick map; ten full method cards; five collaboration modes and task chains; Method Record/output ceilings; invocation and validation; repository status and documents.

Every method card must contain `负责什么`, `可以完成`, `适合任务`, `典型产出`, and `边界`. Link its Skill ID to the corresponding `skills/<id>/SKILL.md`. Preserve the current `RELEASE: not_authorized` fact in the final engineering section, not the Hero.

- [ ] **Step 4: Establish `README_CONTENT_COMPLETE` before review**

Run:

```powershell
$ids = @(
  'ariadne-skill', 'ariadne-framing', 'ariadne-evidence', 'ariadne-scale',
  'ariadne-mechanism', 'ariadne-human', 'ariadne-dynamics',
  'ariadne-forecast', 'ariadne-choice', 'ariadne-audit'
)
$missing = $ids | Where-Object {
  -not (Select-String -LiteralPath README.md -SimpleMatch "skills/$_/SKILL.md" -Quiet)
}
if ($missing) { throw "Missing Skill links: $($missing -join ', ')" }
foreach ($label in '负责什么','可以完成','适合任务','典型产出','边界') {
  if (-not (Select-String -LiteralPath README.md -SimpleMatch $label -Quiet)) {
    throw "Missing method-card field: $label"
  }
}
foreach ($svg in 'docs/assets/readme-hero.svg','docs/assets/lattice-kernel-map.svg') {
  if (-not (Test-Path -LiteralPath $svg)) { throw "Missing SVG: $svg" }
  [void][xml](Get-Content -LiteralPath $svg -Raw)
}
'README_CONTENT_COMPLETE'
```

Expected: `README_CONTENT_COMPLETE`. Only now may Task 2 begin.

### Task 2: Run one unified parallel review

**Files:**
- Review: `README.md`
- Review: `docs/assets/readme-hero.svg`
- Review: `docs/assets/lattice-kernel-map.svg`
- Reference: all ten `skills/*/SKILL.md` contracts

**Interfaces:**
- Consumes: the complete Task 1 deliverable.
- Produces: three read-only finding sets, merged without averaging disagreements.

- [ ] **Step 1: Dispatch three read-only reviewers together**

Reviewer A checks Chinese clarity, CrossFrame-inspired reading rhythm, C visual fidelity, SVG accessibility, and narrow-screen legibility. Reviewer B checks each of the ten cards against its real Skill contract and flags responsibility drift. Reviewer C checks links, anchors, repository facts, unsupported claims, invocation limits, and authorization boundaries.

No reviewer edits files. Each returns severity, exact file/line evidence, and a pass/fail verdict.

- [ ] **Step 2: Merge findings after all three reviewers finish**

Deduplicate findings by exact claim or rendering defect. Preserve conflicting reviewer judgments and resolve them against the approved design spec and repository contracts.

### Task 3: Repair once and run final verification

**Files:**
- Modify if required: `README.md`
- Modify if required: `docs/assets/readme-hero.svg`
- Modify if required: `docs/assets/lattice-kernel-map.svg`

**Interfaces:**
- Consumes: the unified review finding set.
- Produces: corrected final deliverable and validation evidence.

- [ ] **Step 1: Apply all accepted review corrections in one repair pass**

Use only evidence-backed corrections. Do not add new scope or rewrite Skill contracts.

- [ ] **Step 2: Run structural and repository verification**

```powershell
python -X utf8 -B -m pytest -q
python -X utf8 -B scripts/validate_repo.py
python -X utf8 -B scripts/validate_evals.py
git diff --check
```

Expected: every command exits zero with pytest and both validators reporting success.

- [ ] **Step 3: Run final README-specific checks**

Re-run the Task 1 completeness command. Verify every relative Markdown target with `Test-Path`, parse both SVG files as XML, search for hidden zero-width characters, and visually inspect both SVG files at full and narrow widths. Confirm the README contains no copied CrossFrame product names, ProMax metrics, or unsupported Release/License/site links.

- [ ] **Step 4: Commit the complete README redesign**

```powershell
git add -- README.md docs/assets/readme-hero.svg docs/assets/lattice-kernel-map.svg
git commit -m "docs: redesign Ariadne README in Chinese"
```
