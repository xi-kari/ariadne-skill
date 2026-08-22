---
name: ariadne-mechanism
description: "Explain why and through which channel something happens by making at least two competing mechanisms beat a simple baseline, each with channel observations, falsifiers, and residual comparison. Use when a why or how question, root-cause diagnosis, causal route, or analogy needs competing explanations instead of one coherent story. Part of the Ariadne methodology suite. 适用于：机制比较、根因分析、竞争机制与证伪条件、残差分析。"
license: MIT
metadata:
  record_schema: "1.2"
---

# Ariadne Mechanism

## Overview

Build bounded mechanism diagnoses. Compare the simplest adequate baseline with explicit competing mechanisms, and keep every channel, condition, falsifier, residual, and evidence ceiling inspectable.

## Standalone Contract

Create or extend a schema-valid Method Record. Preserve complete parent ID/version lineage, trace this module's input and output records, record the ceiling transition, and put every mechanism candidate in the typed module payload.

Set `authorization_effect` to `none`. A module run preserves or lowers its parent ceiling. Raise only in a child that newly admits named external evidence or a newly fulfilled protocol. Use `description_only` when the object or evidence is inadequate, `diagnostic_only` for a bounded mechanism comparison, and `requirements_only` only when that diagnosis is retained and explicit external process requirements are added.

## Procedure

1. Classify the requested result. Separate mechanism diagnosis from dynamic derivation, forecast, choice, intervention, and authorization.
2. Freeze the candidate object as `S*=<B,X,R,I,T,SP,K>`, the evidence cutoff, the target difference, and the permitted generalization unit. Mark absent fields as `unknown`, `not_applicable`, `not_observable`, or `withheld_for_protection`.
3. Scan D0-D3 (D0 structural object, D1 state terms, D2 effective feedback, D3 scale transformation) and U01-U11 (U01 candidate-object interface, U02 boundary and interface, U03 state and observable, U04 component/carrier/substrate, U05 relation and constraint, U06 flow/channel/conduction, U07 feedback and update, U08 condition and environment, U09 load/capacity/recovery margin, U10 trace/memory/path, U11 phase/transition/dissolution). Select only applicable primitives, preserve their distinct roles, and record why any required primitive is unavailable.
4. State the simplest adequate baseline and the residual it leaves. Add a circle, variable, or mechanism only when it addresses that residual through a plausible, observable channel.
5. Build at least two competing mechanisms for every causal or analogy route. For every candidate, record a channel observation, a discriminating prediction, a reverse condition or falsifier, and a residual comparison rule against the same simple baseline; also retain dependencies, enabling conditions, measured dimensions, minimum evidence, failure boundary, and unresolved residual.
6. Apply G1-G4 (G1 candidate grouping, G2 specified channel, G3 historical increment, G4 scale closure or conversion) and C1-C12 (C1 object and boundary, C2 carrier and channel, C3 feedback and learning, C4 history and path, C5 load and recovery, C6 scale closure or conversion, C7 local change and spillover, C8 variation-selection-reproduction, C9 observation and reflexivity, C10 human carrying, C11 institutional writeback, C12 normative bridge) only through eligible instances and their allowed conclusions. Treat definitions, contract completion, internal labels, and examples as no empirical support.
7. Select only applicable CM contracts (CM-FEEDBACK effective feedback, CM-LEARNING feedback-mediated learning, CM-MAINTENANCE maintenance and preservation-dissolution, CM-LOAD load/capacity/recovery, CM-PHASE phase and threshold transition, CM-SELECTION variation-retention-reproduction). Keep feedback separate from learning, instantaneous load separate from cumulative damage, phase patterns separate from causal or hysteretic transitions, and selection patterns separate from carriers and cross-round history.
8. Compare candidates against the baseline. Retain ties, null or undecided results, unmeasured dimensions, competing causes, and zero-result requirements instead of choosing the smoothest story.
9. Write the bounded finding into `claim_ledger`, preserve residuals and counterevidence, and put every complete candidate in the typed mechanism payload. If fewer than two complete candidates exist, stop at `description_only`. Record this module run and recommend only the next modules actually needed.

Stop before assigning value, responsibility, obligation, remedy, or permission. Route event propagation to `ariadne-dynamics`, human roles or privacy to `ariadne-human`, scale translation to `ariadne-scale`, evidence repair to `ariadne-evidence`, and any real-world choice or authorization question onward without answering it here.

If a routed peer skill is unavailable in this installation, record the handoff in module_runs as not_run with reason module_unavailable, keep that responsibility's outputs unknown, preserve or lower the output ceiling, and do not execute the peer's responsibility inline or claim it ran.

## Quick Reference

| Need | Apply |
|---|---|
| Define structural positions | D0-D3 and U01-U11 |
| Test object, channel, history, or scale | G1, G2, G3, or G4 |
| Explain a residual | Simple baseline plus competing mechanism contracts |
| Distinguish return from learning | CM-FEEDBACK, then CM-LEARNING only with retained multi-round history |
| Diagnose load or recovery | CM-LOAD with typed units, location, window, and branch |
| Diagnose thresholds or selection | CM-PHASE or CM-SELECTION without value or stage claims |

## Mini Example

Input: "Why did the error rate double after the deploy?" Skeleton only, not a complete record:
```yaml
request_type: explanation
object_contract: {boundary: one service's request path after a deploy}
module_payloads:
- {module: ariadne-mechanism, candidates: [config-rollout-change, dependency-timeout]}
output_ceiling: diagnostic_only
```

## Common Mistakes

- Treating a U or CM label as evidence instead of a candidate contract.
- Calling signal arrival feedback, or calling one update learning.
- Generalizing one measured channel dimension to capacity, delay, reliability, controllability, and loss.
- Treating a failed positive test as support for the null without a frozen and passed null rule.
- Subtracting unlike demand and capacity, or turning overload into a duty to keep carrying it.
- Turning phase, persistence, selection, maintenance, dissolution, or repair into progress, failure, value, or authorization.
- Adding complexity without naming the residual, observable channel, and simple-baseline comparison.

Read [mechanism-contracts.md](references/mechanism-contracts.md) for the detailed grammar, root and inference ceilings, CM contracts, comparison record, and worked example.
