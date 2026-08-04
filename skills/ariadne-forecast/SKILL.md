---
name: ariadne-forecast
description: Use when a future claim needs a target, deadline, frozen inputs, simple baseline, calibration, early and reverse signals, failure semantics, or result writeback.
---

# Ariadne Forecast

## Overview

Register future-facing claims before outcomes appear, then evaluate them against the frozen contract. Keep every forecast local, conditional, calibratable, able to fail, and separate from finite choice or real-world authorization.

## Route the Request

- Use this module for a future judgment with a target and deadline.
- Return a scenario or dynamic derivation, not a forecast, when no outcome can be judged at a declared horizon.
- Refuse retrospective preregistration when the outcome or outcome-bearing inputs are already known. Preserve the material as explanation and open a new forecast only for a later target.
- Finish the forecast record before handing an action question to `ariadne-choice`.
- Hand forecast misuse, selective publication, or lifecycle questions to `ariadne-audit`.

## Run the Forecast

1. Freeze the object contract, scale scope, evidence cutoff, input cutoff, target, outcome rule, horizon, allowed error, observation source, and model version. Mark an unstable object or target as a contract failure.
2. Register a fair simple baseline under the same target, horizon, cutoff, information set, and evaluation rule. Add mechanisms or circles only when they can earn specified out-of-sample incremental value.
3. Enumerate mutually exclusive, parallel, and incomparable paths. Keep every model-proposed variable `candidate` until external evidence supports it.
4. Choose the weakest adequate expression: probability or interval, ordered support, conditional direction, or abstention. Never invent numbers from prose or model confidence.
5. Preregister the calibration metric, decision-independent evaluation rule, early signals, reverse signals, review triggers, pause conditions, retirement conditions, and append-only writeback plan.
6. At the deadline, assign exactly one result state: `supported`, `not_supported`, `unresolved`, `target_invalid`, or `not_evaluable`. Evaluate recursive orders separately and compare each order with its own simpler continuation baseline.
7. Append the observation source, actual result, metric, baseline comparison, distributional errors, unexpected effects, downgrade or retirement decision, and next review. Never overwrite the original target, probability, horizon, or failure.
8. State the narrowest output ceiling and recommended handoff. Keep `authorization_effect` equal to `none` in every version.

## Method Record

Create or extend a schema-valid Method Record. Preserve complete parent ID/version lineage, trace module inputs and output, and apply the ceiling algebra. The typed forecast payload always carries both closed branches and exactly one is non-null. For a live forecast, fill the complete `preregistration`, link its `record_id` and `record_version` to the current Method Record, and set `post_hoc_reconstruction: null`. For an outcome-aware reconstruction, set `preregistration: null`, fill every reconstruction field including `calibration` and `failure_classification`, and never disguise it as preregistration.

A normal module child preserves or lowers its parent ceiling. Raise only in a child that newly admits named external evidence or a newly fulfilled declared protocol. Keep `authorization_effect: none`.

## Output Contract

Return plain-language reasoning first. Then expose the forecast ID, frozen target and deadline, input cutoff, simple baseline, paths, expression strength, early and reverse signals, evaluation rule, failure states, next review, and compact Method Record. Use `requirements_only` only when lower permissions remain satisfied and the output adds conditions a downstream external choice process still needs; do not phrase those conditions as a recommendation.

Stop at `description_only` when the object, target, observation rule, horizon, or cutoff is not stable. Stop at `diagnostic_only` after publishing or evaluating a forecast. Never claim inevitability, empirical verification from simulation, value priority, consent, jurisdiction, or permission to act.

## Quick Reference

| Situation | Required response |
|---|---|
| No judgeable target or deadline | Do not publish a forecast; repair the contract. |
| No fair simple baseline | Keep only a scenario or conditional direction. |
| Data support ranking but not probability | Publish an ordered support level, not a number. |
| Outcome changes the object identity | Mark `target_invalid`; preserve the original record. |
| Complex model ties the baseline | Prefer the baseline and withdraw incremental-ability claims. |
| Action question follows | Hand off conditions to `ariadne-choice`; keep authorization at `none`. |

## Common Mistakes

- **Backdating the forecast:** Treat an outcome-aware account as explanation, not preregistration.
- **Choosing a weak baseline:** Match the information, target, horizon, and metric before comparing complexity.
- **Calling every branch a hit:** Freeze path relations and success rules before the outcome.
- **Turning prose into probabilities:** Downgrade to rank, direction, or abstention when calibration support is absent.
- **Counting `unresolved` as partial success:** Keep all five result states distinct.
- **Repairing failure by editing history:** Append a child record and preserve the failed original.
- **Converting accuracy into authority:** Keep forecast, choice, and authorization in separate records.

## Load Detailed Guidance

Read [forecast-contract.md](references/forecast-contract.md) when defining fields, selecting baselines or metrics, evaluating recursive forecasts, publishing a result, writing back outcomes, or following the worked example.
