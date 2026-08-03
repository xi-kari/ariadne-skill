---
name: ariadne-mechanism
description: Use when a task needs competing mechanisms, channels, feedback, constraints, baselines, residuals, or conditional structural explanations.
---

# Ariadne Mechanism

## Overview

Build bounded mechanism diagnoses. Compare the simplest adequate baseline with explicit competing mechanisms, and keep every channel, condition, falsifier, residual, and evidence ceiling inspectable.

## Standalone Contract

Create a minimal common Method Record when none is supplied. Preserve an incoming record and its lineage when one is supplied. Populate `record_id`, `schema_version`, `record_version`, `parent_record_id`, `request_type`, `object_contract`, `evidence_cutoff`, `scale_scope`, `claim_ledger`, `unknowns_and_counterevidence`, `output_ceiling`, `module_runs`, `recommended_next_modules`, and `authorization_effect`.

Set `authorization_effect` to `none`. Keep an upstream ceiling or lower it; never raise it without a new evidence-bearing record version. Use `description_only` when the object or evidence is inadequate, `diagnostic_only` for a bounded mechanism comparison, and `requirements_only` when reporting only the requirements for a stronger claim.

## Procedure

1. Classify the requested result. Separate mechanism diagnosis from dynamic derivation, forecast, choice, intervention, and authorization.
2. Freeze the candidate object as `S*=<B,X,R,I,T,SP,K>`, the evidence cutoff, the target difference, and the permitted generalization unit. Mark absent fields as `unknown`, `not_applicable`, `not_observable`, or `withheld_for_protection`.
3. Scan D0-D3 and U01-U11. Select only applicable primitives, preserve their distinct roles, and record why any required primitive is unavailable.
4. State the simplest adequate baseline and the residual it leaves. Add a circle, variable, or mechanism only when it addresses that residual through a plausible, observable channel.
5. Build at least one competing explanation. For each candidate, state formal dependencies, enabling conditions, mechanism chain, measured dimensions, minimum evidence, counterexample, falsifier, failure boundary, and unresolved residual.
6. Apply G1-G4 and C1-C12 only through eligible instances and their allowed conclusions. Treat definitions, contract completion, internal labels, and examples as no empirical support.
7. Select only applicable CM contracts. Keep feedback separate from learning, instantaneous load separate from cumulative damage, phase patterns separate from causal or hysteretic transitions, and selection patterns separate from carriers and cross-round history.
8. Compare candidates against the baseline. Retain ties, null or undecided results, unmeasured dimensions, competing causes, and zero-result requirements instead of choosing the smoothest story.
9. Write the bounded finding into `claim_ledger`, preserve residuals and counterevidence, record this module run, and recommend only the next modules actually needed.

Stop before assigning value, responsibility, obligation, remedy, or permission. Route event propagation to `ariadne-dynamics`, human roles or privacy to `ariadne-human`, scale translation to `ariadne-scale`, evidence repair to `ariadne-evidence`, and any real-world choice or authorization question onward without answering it here.

## Quick Reference

| Need | Apply |
|---|---|
| Define structural positions | D0-D3 and U01-U11 |
| Test object, channel, history, or scale | G1, G2, G3, or G4 |
| Explain a residual | Simple baseline plus competing mechanism contracts |
| Distinguish return from learning | CM-FEEDBACK, then CM-LEARNING only with retained multi-round history |
| Diagnose load or recovery | CM-LOAD with typed units, location, window, and branch |
| Diagnose thresholds or selection | CM-PHASE or CM-SELECTION without value or stage claims |

## Common Mistakes

- Treating a U or CM label as evidence instead of a candidate contract.
- Calling signal arrival feedback, or calling one update learning.
- Generalizing one measured channel dimension to capacity, delay, reliability, controllability, and loss.
- Treating a failed positive test as support for the null without a frozen and passed null rule.
- Subtracting unlike demand and capacity, or turning overload into a duty to keep carrying it.
- Turning phase, persistence, selection, maintenance, dissolution, or repair into progress, failure, value, or authorization.
- Adding complexity without naming the residual, observable channel, and simple-baseline comparison.

Read [mechanism-contracts.md](references/mechanism-contracts.md) for the detailed grammar, root and inference ceilings, CM contracts, comparison record, and worked example.
