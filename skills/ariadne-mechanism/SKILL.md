---
name: ariadne-mechanism
description: "Explain why and through which channel something happens: competing mechanisms against a simple baseline, each with a temporal route, channel observations, falsifiers, and residual comparison. Use when a root-cause review needs competing, falsifiable explanations on record (post-incident, organizational, market, operational); not for routine debugging of code the agent can inspect and fix. Pair with ariadne-human for people questions; for a multi-module pass, start with ariadne-skill. 适用于：根因复盘、为什么会发生、竞争解释与证伪条件。"
license: MIT
metadata:
  record_schema: "2.0"
---

# Ariadne Mechanism

## Overview

Build bounded mechanism diagnoses. Compare the simplest adequate baseline with explicit competing mechanisms, keep every channel, condition, temporal route, falsifier, residual, and evidence ceiling inspectable, and never let a mechanism name stand in for its evidence.

## Standalone Contract

Create or extend a schema-valid Method Record (field list for standalone installs: [references/record-fields.md](references/record-fields.md); the full schema ships with the suite router). Preserve complete parent ID/version lineage, trace this module's input and output records, record the ceiling transition, and put every mechanism candidate in the typed module payload.

Set `authorization_effect` to `none`. A module run preserves or lowers its parent ceiling. Raise only in a child that newly admits named external evidence or a newly fulfilled protocol. Use `description_only` when the object or evidence is inadequate, `diagnostic_only` for a bounded mechanism comparison, and `requirements_only` only when that diagnosis is retained and explicit external process requirements are added.

## Procedure

1. Classify the requested result. Separate mechanism diagnosis from dynamic derivation, forecast, choice, intervention, and authorization.
2. Freeze the candidate object as `S*=<B,X,R,I,T,SP,K>`, the task profile, the evidence cutoff, the target difference, and the permitted generalization unit. Mark absent fields as `unknown`, `not_applicable`, `not_observable`, or `withheld_for_protection`.
3. Scan D0-D3 (D0 structural object, D1 state terms, D2 effective feedback, D3 scale transformation) and U01-U11 (U01 candidate-object interface, U02 boundary and interface, U03 state and observable, U04 component/carrier/substrate, U05 relation and constraint, U06 flow/channel/conduction, U07 feedback and update, U08 condition and environment, U09 load/capacity/recovery margin, U10 trace/memory/path, U11 phase/transition/dissolution). Select only applicable primitives and record why any required primitive is unavailable.
4. State the simplest adequate baseline and the residual it leaves. Add a circle, variable, or mechanism only when it addresses that residual through a plausible, observable channel.
5. Separate the three history questions for every cross-time claim: how the current state formed, how a current carrier passes it on, and whether history adds anything beyond the current representation. Give each candidate one temporal route: `current_state`, `carried_history`, `historical_increment` (needs G3), or `not_applicable`.
6. Build competing mechanisms for every causal or analogy route: at least two when the material allows, otherwise the search range and failure conditions. For every candidate, record a channel observation, a discriminating prediction, a reverse condition or falsifier, and a residual comparison rule against the same simple baseline; also retain dependencies, enabling conditions, measured dimensions, minimum evidence, failure boundary, and unresolved residual.
7. Apply G1-G4 (G1 grouping gain, G2 named channel, G3 historical increment, G4 representation closure or conversion) and C1-C12 only through eligible instances and their allowed conclusions, branch by branch. Definitions, contract completion, internal labels, and examples are not empirical support; independent domain evidence keeps its own standing.
8. Select only applicable CM contracts and branches (CM-FEEDBACK, CM-LEARNING carried or history, CM-MAINTENANCE, CM-LOAD, CM-PHASE, CM-SELECTION). Keep feedback separate from learning and from stability, instant load from accumulation, phase patterns from triggers and hysteresis, selection patterns from carriers and cross-round history, and say what recovered, for whom, under which support, as of when.
9. Compare candidates against the baseline. Retain ties, null or undecided results, unmeasured dimensions, competing causes, and zero-result requirements instead of choosing the smoothest story.
10. Write the bounded finding into `claim_ledger` with `depends_on`, preserve residuals and counterevidence, and put every complete candidate in the typed mechanism payload. If fewer than two complete candidates exist, stop at `description_only` with `status: completed`: record the bounded finding and the incomplete candidates as `candidate` entries in `claim_ledger`, omit the typed mechanism payload entirely, and list the missing candidate fields in `unknowns`. Use `status: failed`, with a reason, only when a required gate broke and no bounded product exists. Record this module run and recommend only the next modules actually needed.

Stop before assigning value, responsibility, obligation, remedy, or permission. Route event propagation to `ariadne-dynamics`, human roles or privacy to `ariadne-human`, scale and representation to `ariadne-scale`, evidence repair to `ariadne-evidence`, and any real-world choice or authorization question onward without answering it here.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Quick Reference

| Need | Apply |
|---|---|
| Define structural positions | D0-D3 and U01-U11 |
| Test object, channel, history increment, or closure | G1, G2, G3, or G4 |
| Explain a residual | Simple baseline plus competing mechanism contracts |
| Earlier events still matter | Carried route first; G3 only for an increment beyond the current state |
| Distinguish return from learning | CM-FEEDBACK, then CM-LEARNING-carried with retained, invoked updates |
| Feedback with delay | Check the stability interval; effective is not stable |
| Diagnose load or recovery | CM-LOAD with typed units, location, window, branch, and recovery semantics |
| Diagnose thresholds or selection | CM-PHASE or CM-SELECTION without value or stage claims |

## Mini Example

Input: "Why did the error rate double after the deploy?" Skeleton only, not a complete record:

```yaml
request_type: explanation
object_contract: {boundary: one service's request path after a deploy}
module_payloads:
- module: ariadne-mechanism
  candidates: [{id: config-rollout-change, route: current_state}, {id: cache-warmup-debt, route: carried_history}]
output_ceiling: diagnostic_only
```

## Common Mistakes

- Treating a U or CM label as evidence instead of a candidate contract.
- Calling signal arrival feedback, one update learning, or effective feedback stability.
- Using G3 failure to deny that history formed the present, or omitting a known current state to manufacture a G3 gain.
- Generalizing one measured channel dimension to capacity, delay, reliability, controllability, and loss.
- Treating a failed positive test as support for the null without a frozen and passed null rule.
- Subtracting unlike demand and capacity, or turning overload into a duty to keep carrying it.
- Declaring recovery without saying what recovered, for whom, under which support, and as of when.
- Counting two paths as redundant when they share a power source, supplier, operator, or approval node.
- Turning phase, persistence, selection, maintenance, dissolution, or repair into progress, failure, value, or authorization.
- Adding complexity without naming the residual, observable channel, and simple-baseline comparison.

Read [references/mechanism-contracts.md](references/mechanism-contracts.md) for the detailed grammar, temporal routes, CM branches, stability, learning evaluation, recovery semantics, clocks, cascades, comparison record, and worked example.
