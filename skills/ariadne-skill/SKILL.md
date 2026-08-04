---
name: ariadne-skill
description: Use when a complex problem requires multiple Lattice Kernel modules, a full methodology pass, or coordinated framing, evidence, scale, mechanism, dynamics, forecast, choice, and audit work.
---

# Ariadne

## Core promise

Turn a complex request into a bounded, inspectable method run. Classify the requested output, freeze the candidate object and evidence cutoff, route only the needed modules, preserve disagreements and unknowns, and stop every conclusion at its supported output ceiling.

Do not use Ariadne as an ontology, truth engine, personality judge, clinical tool, value selector, or authorization authority.

## Required references

Read all four references before running a full pass:

1. [Lattice Kernel](references/lattice-kernel.md) - invariants, claim classes, missing states, and hard boundaries.
2. [Routing](references/routing.md) - module selection, order, clustered execution, and stopping rules.
3. [Method Record](references/method-record.md) - shared record, lineage, ceilings, and handoff format.
4. [Source navigation](references/source-navigation.json) - stable numbering and terminology ownership, dual-text difference retention, and the cross-scale proof heuristic.

## Full-pass workflow

1. Restate the user's real-world question without Ariadne vocabulary.
2. Classify it as one or more of: explanation, diagnosis, dynamic derivation, conditional forecast, finite choice, intervention review, governance review. Keep the outputs separate.
3. Run `ariadne-framing`. Freeze the candidate object, boundary, variables, interfaces, time window, scale profile, identity criterion, and unresolved fields.
4. Run `ariadne-evidence`. Freeze the evidence cutoff and separate source, material, observation, evidence, counterevidence, judgment, and external authorization.
5. Select the minimum adequate module set. Do not retain a module merely because it is available.
   When a source code or shared term is ambiguous, resolve its owner through `source-navigation.json`; use the D.4 difference rule before mapping paired source contracts and route the D.5 eight-field bridge checklist to `ariadne-scale`.
6. After framing and evidence are frozen, run independent scale, mechanism, or human-domain lanes in parallel when the runtime supports it. Otherwise run the same lanes sequentially.
7. Run dynamics only for event propagation or path derivation. Run forecast only for a dated, evaluable future claim. Run choice only for option comparison. Run audit for high-impact use and as the merger of clustered records.
8. Merge child records without averaging conflicts. Preserve every parent ID/version and module input/output reference; apply the deterministic ceiling meet and keep `authorization_effect: none`.
9. For every action request, emit the complete facts/values/options/jurisdiction/authorization/stop/rollback boundary card even when entries are `unknown`.
10. Present a plain-language result first. Add the compact Method Record when it improves checking, continuation, challenge, or writeback.

## Module dispatch

Use these peers as independent method workers:

| Need | Module |
|---|---|
| Object, boundary, scope, task type | `ariadne-framing` |
| Claims, sources, causality, analogy | `ariadne-evidence` |
| Cross-level, cross-time, cross-domain transfer | `ariadne-scale` |
| Channels, feedback, baselines, residuals | `ariadne-mechanism` |
| People, roles, circles, power, privacy | `ariadne-human` |
| Events, clocks, thresholds, branches | `ariadne-dynamics` |
| Dated future judgment and calibration | `ariadne-forecast` |
| Action, delay, experiment, exit, inaction | `ariadne-choice` |
| High-impact gates, appeal, rollback, retirement | `ariadne-audit` |

If a peer Skill is unavailable, execute that responsibility inline from the Lattice Kernel and routing reference. Mark the module run as `not_run` with reason `module_unavailable`; do not pretend the peer ran.

## Cluster contract

Parallelize only after the object record and evidence cutoff are identical across workers. Give each worker the raw task, frozen record, its bounded responsibility, and required output fields. Do not give it a preferred conclusion.

Merge through `ariadne-audit` and apply these rules:

- Shared frozen facts remain shared.
- Distinct unknowns accumulate.
- Incompatible boundaries, scales, or identity criteria remain conflicts.
- Evidence grades do not rise by vote or repetition.
- Sort all sibling parent references canonically and retain them in the audit merge.
- The ordered meet `description_only < diagnostic_only < requirements_only` governs the merged record.
- No number of completed modules creates authorization.

## Output contract

Default to two layers:

1. **Usable answer:** current bounded judgment, supporting observations, alternatives, uncertainty, and the safest next information or option.
2. **Method record:** request type, object status, evidence cutoff, scale scope, claim ledger, counterevidence, module runs, output ceiling, and next modules.

For low-impact questions, keep the record compact. For forecasts, high-impact judgments, public claims, automated use, or real-world choices, expose the fields needed for failure, appeal, rollback, and writeback.

## Stop and downgrade

Stop or lower the ceiling when any of these holds:

- The object changes under the chosen identity criterion.
- Critical evidence is unknown, not observable, or protected without a trusted review path.
- A scale bridge or causal channel is only asserted.
- Forecast inputs were not frozen before the outcome.
- The request asks facts or predictions to manufacture values, jurisdiction, or authorization.
- A high-impact output lacks contestability, stopping, correction, or rollback.

Downgrade is a valid result. Return a candidate analysis, evidence request, scenario set, requirements-only handoff, or explicit non-action state.

## Example

Request: “A competitor cut prices. Predict the year and tell us the one correct action.”

Route:

1. `ariadne-framing` fixes market, product, geography, one-year window, and decision owner.
2. `ariadne-evidence` freezes known price facts and unknown duration/cost/demand data.
3. `ariadne-scale` separates one competitor event from market-wide change.
4. `ariadne-mechanism` compares clearance, cost advantage, distress, and share-grab mechanisms.
5. `ariadne-dynamics` derives conditional branches.
6. `ariadne-forecast` registers only branches with a baseline and signals.
7. `ariadne-choice` compares targeted experiment, delay, value change, price response, and inaction.
8. `ariadne-audit` checks affected positions, authority, stopping, and rollback.

The result is a conditional comparison, not a prophecy or self-authorizing command.

## Common mistakes

| Mistake | Correction |
|---|---|
| Run every module to appear thorough | Run the minimum adequate set and state why each is applicable. |
| Ask the user to fill every field | Mark ordinary gaps explicitly; ask only when a missing choice would materially change the task. |
| Treat module agreement as proof | Preserve independent evidence and shared assumptions. |
| Hide method vocabulary in a confident narrative | Lead with plain language but keep the record available. |
| Let a later module repair an earlier broken gate | Restart from the earliest changed object, evidence, scale, or purpose. |
| Turn requirements into instructions | Keep `authorization_effect: none` and identify the external decision process. |
