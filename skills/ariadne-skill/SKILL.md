---
name: ariadne-skill
description: "Coordinate a structured multi-angle analysis of a complex real-world question: frame the object, freeze evidence, route only the needed peer modules (framing, evidence, scale, mechanism, human, dynamics, forecast, choice, audit), and merge results into one bounded, inspectable record. Use when a question mixes explanation, prediction, and action, spans people, evidence, and decisions at once, or the user asks for a systematic, thorough, multi-angle, or auditable analysis. 适用于：系统分析、全面评估、多角度复盘、这个复杂问题怎么看/该不该做、需要可检查可续接的结论。"
license: MIT
metadata:
  record_schema: "1.2"
---

# Ariadne

## Core promise

Turn a complex request into a bounded, inspectable method run. Classify the requested output, freeze the candidate object and evidence cutoff, route only the needed modules, preserve disagreements and unknowns, and stop every conclusion at its supported output ceiling.

Ariadne covers judgment-type outputs: explanation, diagnosis, dynamic derivation, conditional forecast, finite choice, intervention review, and governance review. A generative or build request (write, design, implement, create) is out of scope as a whole: declare that, hand the construction work back to the host's normal workflow, and apply single modules only to the judgment-type claims or decisions inside it. Do not use Ariadne as an ontology, truth engine, personality judge, clinical tool, value selector, or authorization authority.

## Required references

Read by declared depth instead of all at once. Depth levels L0-L3 are defined in the routing reference: L0 direct bounded answer, L1 low-impact reversible work, L2 comparative work with reviewable impact, L3 public, automated, institutional, high-power, or hard-to-reverse use.

- L0: no reference read is required beyond this file.
- L1: read [Lattice Kernel](references/lattice-kernel.md) - invariants, claim classes, missing states, hard boundaries, and the coding family index - and copy the record shape from the [L1 record template](references/l1-record-template.md).
- L2: add [Method Record](references/method-record.md) - shared record, identifiers, carrier, lineage, ceilings, raise rules, and handoff format.
- Full pass or L3: add [Routing](references/routing.md) - intake, depth selection, module map, routing algorithm, restarts, and stop-loss.
- Clustered execution, merging, or continuing an earlier run: add [Clustering](references/clustering.md) - lane admission, merge rules, stop table, host orchestration mapping, and the merge lineage example.
- Only when a shared source code or term is ambiguous, or dual-text work is in scope: consult [Source navigation](references/source-navigation.json) - stable numbering ownership, D.4 dual-text difference rule, D.5 cross-scale proof heuristic, and Chinese stable references.

Validate every emitted record by running the shipped validator, `python scripts/validate_record.py <record.yaml>`, from this skill's directory; it checks the [Method Record schema](references/method-record.schema.json) (byte-identical to the repository-root copy) plus the semantic rules, so the 30KB schema never needs to enter context. Without code execution, use the manual checklist in the L1 record template and say which path was taken; never claim a validation that did not run.

## Full-pass workflow

1. Restate the user's real-world question without Ariadne vocabulary.
2. Classify it as one or more of: explanation, diagnosis, dynamic derivation, conditional forecast, finite choice, intervention review, governance review. Keep the outputs separate. If none fits, declare out of scope as promised above.
3. Select depth. L0: answer directly with a one-line boundary declaration; no module run, no record. L1: run framing plus the one relevant module and emit a compact record from the template. Only L2 and above continue with the full workflow below. When in doubt between L0 and L1, use L1.
4. Run `ariadne-framing`. Freeze the candidate object, boundary, variables, interfaces, time window, scale profile, identity criterion, and unresolved fields.
5. Run `ariadne-evidence`. Freeze the evidence cutoff and separate source, material, observation, evidence, counterevidence, judgment, and external authorization.
6. Select the minimum adequate module set. Do not retain a module merely because it is available. When a source code (G1, C1-C12, CM-*, and similar Appendix B families) or a shared term is ambiguous, resolve its owner through the coding family index in the Lattice Kernel or through `source-navigation.json`. When the user has supplied two source contract texts, apply the D.4 dual-text difference rule from `source-navigation.json`; otherwise mark dual-text work `not_applicable`. Route any cross-scale bridge proof to `ariadne-scale` (D.5).
7. After framing and evidence are frozen, run independent scale, mechanism, or human-domain lanes in parallel when the runtime supports it (see the host orchestration mapping in Clustering). Otherwise run the same lanes sequentially.
8. Run dynamics only for event propagation or path derivation. Run forecast only for a dated, evaluable future claim. Run choice only for option comparison. Run audit for high-impact use and as the merger of clustered records.
9. Merge child records without averaging conflicts; record irreducible disagreements as named entries in the `conflicts` field. Preserve every parent ID/version and module input/output reference; apply the deterministic ceiling meet and keep `authorization_effect: none`.
10. For an action request at L2 or above, emit the complete facts/values/options/jurisdiction/authorization/stop/rollback boundary card even when entries are `unknown`. An action request that meets every L1 condition may compress the all-unknown card into a single declaration line, as the routing reference specifies.
11. Present a plain-language result first. Add the compact Method Record when it improves checking, continuation, challenge, or writeback.

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

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Cluster contract

Parallelize only after the object record and evidence cutoff are identical across workers; give each worker the raw task, the frozen record, its bounded responsibility, and no preferred conclusion. Merge through `ariadne-audit` under the merge rules in [Clustering](references/clustering.md): shared frozen facts stay shared, unknowns accumulate, incompatible boundaries or explanations stay named conflicts, evidence grades never rise by vote, the ceiling meet takes the minimum, and no number of completed modules creates authorization.

## Output contract

Default to two layers:

1. **Usable answer:** current bounded judgment, supporting observations, alternatives, uncertainty, and the safest next information or option.
2. **Method record:** request type, object status, evidence cutoff, scale scope, claim ledger, counterevidence, conflicts, module runs, output ceiling, and next modules.

For low-impact questions, keep the record compact and show it only when the user asks or continuation needs it. For forecasts, high-impact judgments, public claims, automated use, or real-world choices, expose the fields needed for failure, appeal, rollback, and writeback.

## Mini example

Request: "Why did weekly deployments slow down this quarter?"

Illustrative excerpt only - not a schema-valid record. The complete twenty-field template that CI validates is the [L1 record template](references/l1-record-template.md); copy that, never this.

```yaml
record_id: ariadne:deploy-slowdown:root:v1
request_type: explanation
lineage_kind: root
output_ceiling: description_only
conflicts: []
recommended_next_modules: [ariadne-evidence]
```

At `description_only` this run may already list unranked candidate mechanisms (marked `candidate`) and the observations that would discriminate them; ranking or endorsing one needs `diagnostic_only` earned through the raise rules.

## Stop and downgrade

Stop or lower the ceiling when any of these holds:

- The object changes under the chosen identity criterion.
- Critical evidence is unknown, not observable, or protected without a trusted review path.
- A scale bridge or causal channel is only asserted.
- Forecast inputs were not frozen before the outcome.
- The request asks facts or predictions to manufacture values, jurisdiction, or authorization.
- A high-impact output lacks contestability, stopping, correction, or rollback.
- The stop-loss in the routing reference fires: projected record work is disproportionate to the stakes, or two consecutive module runs left the conclusion unchanged.

Downgrade is a valid result. Return a candidate analysis, evidence request, scenario set, requirements-only handoff, or explicit non-action state.

Router-only installation (only this skill installed): the deliverable is still defined. Run intake, classification, and depth selection, which are this router's own responsibilities: produce the request classification, a candidate object and boundary statement, the evidence cutoff, the module-absence list with installation guidance, and a degraded root record whose peer responsibilities are `not_run` with reason `module_unavailable` and whose ceiling stays `description_only`. Do not execute peer responsibilities inline; a single-file bundle for hosts without multi-skill support ships as `dist/ariadne-bundle.md` in the repository.

## Example

Request: "A competitor cut prices. Predict the year and tell us the one correct action."

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
| Run the full pass on a casual question | Use the L0/L1 depth gate; a direct bounded answer is a valid Ariadne outcome. |
| Ask the user to fill every field | Mark ordinary gaps explicitly; ask only when a missing choice would materially change the task. |
| Treat module agreement as proof | Preserve independent evidence and shared assumptions. |
| Hide method vocabulary in a confident narrative | Lead with plain language but keep the record available. |
| Let a later module repair an earlier broken gate | Restart from the earliest changed object, evidence, scale, or purpose, within the two-restarts-per-dependency budget. |
| Turn requirements into instructions | Keep `authorization_effect: none` and identify the external decision process. |
