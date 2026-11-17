---
name: ariadne-skill
description: "Handle a complex question or design: frame or reopen the task, establish evidence, route needed peers, generate traceable candidates, compare and judge within the evidence, then deliver the complete analysis or requested artifact. For choices, give a recommendation under explicit premises and keep real authorization separate. Use when a question mixes explanation, prediction, and action, spans people, evidence, and decisions, or the user asks for a systematic, thorough, multi-angle, or auditable analysis. 适用于：系统分析、全面评估、多角度复盘、复杂问题怎么看或该不该做。"
license: MIT
metadata:
  record_schema: "2.1"
---

# Ariadne

## Core promise

Turn a complex request into a complete, bounded result with inspectable reasoning. Start from the concrete difference that needs explaining or deciding, declare the task together with its representation, freeze the candidate object and evidence cutoff, route only the needed modules, preserve disagreements and unknowns, lower each conclusion only as far as its own dependencies require, and deliver the complete analysis at its supported ceiling.

Ariadne covers judgment-type outputs: explanation, diagnosis, dynamic derivation, conditional forecast, finite choice, intervention review, governance review, and design synthesis. For a generative or build request (write, design, implement, create), use `synthesis_design` for its judgment core and traceable candidate generation, then continue through the host workflow to complete and verify the requested artifact within the user's existing authorization. With no substantive judgment core, ordinary construction can proceed directly without a method run. Do not use Ariadne as an ontology, truth engine, personality judge, clinical tool, value selector, or authorization authority. A shorter adequate domain method may answer alone; Ariadne then adds only source and boundary checks.

Ariadne's entries are method and retrieval entries derived from its source theory, with candidate status; where an entry and the source disagree, the source governs.

## Working method

Use seven operations as dependencies require: pose or reopen the question, represent the task, establish support, connect judgments, generate and derive candidates, compare and judge, then deliver and revise. Read [Working method](references/methodology.md) for this operational distillation and its source anchors. It is the method entry for a first substantive run; the detailed kernel supplies the limits. Preserve successful local findings, make clear supported judgments, and continue useful independent work when a dependent claim is blocked.

## Required references

Read by declared depth instead of all at once. Depth levels L0-L3 are defined in the routing reference: L0 direct bounded answer, L1 light description and probing questions, L2 standard reviewable judgment, L3 high-responsibility strong-judgment candidate set by use and foreseeable impact.

- L0: no reference read is required beyond this file.
- L1: read [Lattice Kernel](references/lattice-kernel.md) - invariants, claim roles, connection conditions, history routes, missing states, ceilings, and the coding family index - and, when a machine record is useful or requested, copy its shape from the [L1 record template](references/l1-record-template.md). Ordinary light work can keep the task, evidence, judgment and boundary in concise prose.
- L2: add [Method Record](references/method-record.md) - shared record, task profile, proposition-level dependencies, carrier, lineage, ceilings, raise rules, typed payloads, and presentation.
- Full pass or L3: add [Routing](references/routing.md) - intake, depth selection by use, module map, routing algorithm, retrieval order, restarts, and stop-loss.
- Generative or build work: add [Generative workflow](references/generative-workflow.md) for starting points, derivation, candidates, checks and artifact completion.
- Clustered execution, merging, or continuing an earlier run: add [Clustering](references/clustering.md) - lane admission, merge rules, per-proposition stop table, continuation events, host orchestration mapping, and the merge lineage example.
- Only when a source code or term is ambiguous, dual-text work is in scope, or the source identity must be checked: consult [Source navigation](references/source-navigation.json) - source SHA-256 and derived status, Appendix B numbering ownership, body-only codes, the nine governance invariants, the six kernel layers, the C.4 dual-text difference rule, the C.5 cross-scale proof heuristic, and the D.01-D.32 domain-atlas route.

Validate every emitted record by running the shipped validator, `python scripts/validate_record.py <record.yaml>`, from this skill's directory; it checks the [Method Record schema](references/method-record.schema.json) (byte-identical to the repository-root copy) plus the semantic rules. Without code execution, use the manual checklist in the L1 record template and say which path was taken; never claim a validation that did not run.

## Full-pass workflow

1. Restate the user's real-world question without Ariadne vocabulary, and name the difference that needs explaining, deciding, or protecting.
2. Classify it as one or more of: explanation, diagnosis, dynamic derivation, conditional forecast, finite choice, intervention review, governance review, synthesis design. Keep the outputs separate; each extra output adds its own conditions. If no substantive judgment is needed, finish the ordinary task through the host workflow.
3. Select depth by intended and foreseeable use. L0: answer directly with a one-line boundary declaration; no module run, no record. L1: use framing plus the relevant method; emit the compact machine record only when it helps continuation, checking, or the user requests it. Only L2 and above continue with the full workflow below. When in doubt between L0 and L1, use L1.
4. Run `ariadne-framing`. Reopen the question when its target, members, losses or assumed constraints are disputed; retain the original question, disposition and results. Freeze the candidate object, task profile (target query, horizon, environment, allowed operations, error tolerance), boundary, variables, interfaces, time window, scale profile, identity criterion, and unresolved fields.
5. Run `ariadne-evidence`. Freeze the evidence cutoff; separate source, material, observation, evidence, counterevidence, judgment, and authorization; register claim roles and `depends_on` links.
6. Select the minimum adequate module set. Do not retain a module merely because it is available. Resolve an ambiguous code family through the coding family index in the Lattice Kernel or through `source-navigation.json`. When the user has supplied two source contract texts, apply the C.4 dual-text difference rule; otherwise mark dual-text work `not_applicable`. Route any cross-scale bridge proof to `ariadne-scale` (C.5).
7. After framing and evidence are frozen, run independent scale, mechanism, or human-domain lanes in parallel when the runtime supports it (see the host orchestration mapping in Clustering). Otherwise run the same lanes sequentially.
8. Run dynamics only for event propagation or path derivation. Run forecast only for a dated, evaluable future claim. Run choice for option comparison and every action request. Run audit for high-impact use and as the merger of clustered records.
9. Merge child records without averaging conflicts; record irreducible disagreements as named `conflicts` entries. Preserve every parent ID/version, module input/output reference, claim dependency, and claim-level ceiling; apply the deterministic ceiling meet and keep `authorization_effect: none`.
10. For `synthesis_design`, follow the generative workflow: construct traceable candidates, compare them under explicit criteria, then complete and check the requested artifact through the host tools. For an action request at L2 or above, emit the typed choice card: facts, explicit values, structured options with exactly one no-action option, jurisdiction, authorization, stop conditions, rollback plan, and an analytic recommendation or an explicit `null` naming what blocks it. An action request that meets every L1 condition may compress the card into a short declaration preserving supplied facts, values, options and existing authorization; mark only actual gaps unknown, as the routing reference specifies.
11. Deliver the complete plain-language analysis first: current judgment and scope, evidence, every substantive path compared, unknowns and reverse conditions, the ceiling, and, for choices, the recommendation with its premises, costs, objections, and change conditions. Compress only when the user asks for brevity. Add the Method Record when it improves checking, continuation, challenge, or writeback. A draft or build request also receives the actual artifact and its endpoint verification.

## Module dispatch

Use these peers as independent method workers:

| Need | Module |
|---|---|
| Object, task, representation, boundary, domain entry | `ariadne-framing` |
| Claims, sources, causality, analogy, measurement, independence | `ariadne-evidence` |
| Cross-scale, cross-circle, and representation transfer; closure | `ariadne-scale` |
| Channels, feedback, carriers, baselines, residuals | `ariadne-mechanism` |
| People, roles, circles, power, privacy, actors | `ariadne-human` |
| Events, clocks, thresholds, branches, recursion | `ariadne-dynamics` |
| Dated future judgment and calibration | `ariadne-forecast` |
| Action, delay, probing, exit, inaction, recommendation | `ariadne-choice` |
| Strong-judgment gates, appeal, rollback, governance, retirement | `ariadne-audit` |

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Cluster contract

Parallelize only after the object record and evidence cutoff are identical across workers; give each worker the raw task, the frozen record, its bounded responsibility, and no preferred conclusion. Merge through `ariadne-audit` under the merge rules in [Clustering](references/clustering.md): shared frozen facts stay shared, unknowns accumulate, incompatible boundaries or explanations stay named conflicts, evidence grades never rise by vote, lanes that share data or sources count as one lineage, the ceiling meet takes the minimum, and no number of completed modules creates authorization.

## Output contract

Default to two layers:

1. **Complete analysis:** current bounded judgment and scope, supporting evidence, every substantive alternative or path actually compared, uncertainty and what would change the judgment, and the safest next information or option; for choices, the analytic recommendation for deliberation with its normative premises, reasons, costs, objections, and change conditions, with the actual external adoption and authorization state kept separate; the recommendation itself creates neither.
2. **Method record when needed:** request type, object and task profile, evidence cutoff, scale scope and transformation kind, claim ledger with dependencies, counterevidence, conflicts, module runs, output ceiling, and next modules.

Shorten the visible analysis only when the user asks; never drop a substantive comparison because it is a minor branch. For forecasts, high-impact judgments, public claims, automated use, or real-world choices, expose the fields needed for failure, appeal, rollback, and writeback.

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

Lower the propositions that depend on any of these, and only those, unless the failure is global:

- The object changes under the chosen identity criterion, or the task changes.
- Critical evidence is unknown, not observable, or protected without a trusted review path.
- A scale, circle, or translation bridge, or a causal channel, is only asserted.
- A cross-time claim has no identified formation, carrier, or increment route.
- Forecast inputs were not frozen before the outcome.
- The request asks facts or predictions to manufacture values, jurisdiction, or authorization.
- A high-impact output lacks contestability, stopping, correction, or rollback.
- The stop-loss in the routing reference fires: projected record work is disproportionate to the stakes, with an explained budget and the remaining valuable work named. An unchanged headline alone is not a stopping reason.

A failure of the shared source, a common premise, the object boundary, or the task's lawful use blocks every dependent output. Renaming or splitting a claim never restores its ceiling. Downgrade is a valid result: return a candidate analysis, evidence request, scenario set, requirements handoff, recommendation for deliberation, or explicit non-action state.

Router-only installation (only this skill installed): the deliverable is still defined. Run intake, classification, and depth selection, which are this router's own responsibilities: produce the request classification, a candidate object, task profile, and boundary statement, the evidence cutoff, the module-absence list with installation guidance, and a degraded root record whose peer responsibilities are `not_run` with reason `module_unavailable` and whose ceiling stays `description_only`. Do not execute peer responsibilities inline; a single-file bundle for hosts without multi-skill support ships as `dist/ariadne-bundle.md` in the repository.

## Example

Request: "A competitor cut prices. Predict the year and tell us the one correct action."

Route:

1. `ariadne-framing` names the difference (our share or margin under the cut), fixes market, product, geography, one-year window, decision owner, and the task profile.
2. `ariadne-evidence` freezes known price facts and unknown duration, cost, and demand data, and maps which claims depend on which.
3. `ariadne-scale` separates one competitor event from market-wide change.
4. `ariadne-mechanism` compares clearance, cost advantage, distress, and share-grab mechanisms, each with its temporal route.
5. `ariadne-dynamics` derives conditional branches with early and reverse signals.
6. `ariadne-forecast` registers only branches with a baseline and signals.
7. `ariadne-choice` compares a targeted experiment, delay, value change, price response, maintaining the status quo, and no action, then gives an analytic recommendation under stated premises with its costs and change conditions.
8. `ariadne-audit` checks affected positions, authority, strong-judgment use, stopping, and rollback.

The result is a conditional comparison with a recommendation for deliberation, not a prophecy or a self-authorizing command.

## Common mistakes

| Mistake | Correction |
|---|---|
| Run every module to appear thorough | Run the minimum adequate set and state why each is applicable. |
| Run the full pass on a casual question | Use the L0/L1 depth gate; a direct bounded answer is a valid Ariadne outcome. |
| Ask the user to fill every field | Mark ordinary gaps explicitly; ask only when a missing choice would materially change the task. |
| Treat module agreement as proof | Preserve independent evidence and shared assumptions; shared lineage is one source. |
| Lower everything when one bridge breaks | Lower only the claims that depend on it; keep independently supported findings. |
| Return a question list when a supported choice analysis exists | Register the premises and give the analytic recommendation as deliberation only. |
| Shorten the analysis by dropping paths that do not change the headline | Deliver every substantive comparison unless the user asks for brevity. |
| Let a later module repair an earlier broken gate | Restart from the earliest changed object, task, evidence, scale, or purpose, preserving the old result and explaining any practical work budget. |
| Turn requirements or recommendations into instructions | Keep `authorization_effect: none` and identify the external decision process. |
