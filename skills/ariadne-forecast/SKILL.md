---
name: ariadne-forecast
description: "Register future claims that can visibly fail: frozen target, deadline, inputs, simple baseline, recursion order, response regime, calibration, early and reverse signals, failure semantics, and result writeback. Use when a future judgment has a target and deadline and must be evaluable; for undated path exploration use ariadne-dynamics, and when the forecast feeds a real decision, follow with ariadne-choice. For a multi-module pass, start with ariadne-skill. 适用于：立一个可验证的预测、这个预测靠不靠谱、基线与校准、失败判定与回写。"
license: MIT
metadata:
  record_schema: "2.0"
---

# Ariadne Forecast

## Overview

Register future-facing claims before outcomes appear, then evaluate them against the frozen contract. Keep every forecast local, conditional, calibratable, able to fail, and separate from finite choice or real-world authorization. Choose the expression the evidence supports, not the one the reader hopes for: classes, grades, intervals, and probabilities carry different duties and are not a ladder to climb.

## Route the Request

- Use this module for a future judgment with a target and deadline.
- Return a scenario or dynamic derivation, not a forecast, when no outcome can be judged at a declared horizon; avoid "will" and "expected hit" phrasing there.
- Refuse retrospective preregistration when the outcome or outcome-bearing inputs are already known. Preserve the material as explanation and open a new forecast only for a later target.
- Finish the forecast record before handing an action question to `ariadne-choice`.
- Hand forecast misuse, selective publication, or lifecycle questions to `ariadne-audit`.

## Run the Forecast

1. Freeze the object contract and task profile, scale scope, evidence cutoff, input cutoff, target, outcome rule, horizon, allowed error, observation source, and model version. Mark an unstable object or target as a contract failure.
2. Register a fair simple baseline under the same target, horizon, cutoff, information set, budget, and evaluation rule. State separately what added information, computation, and structure contribute; add mechanisms or circles only when they can earn specified out-of-sample incremental value.
3. Enumerate mutually exclusive, parallel, and incomparable paths. Keep every model-proposed variable `candidate` until external evidence supports it. Record the recursion stage (0 when there is no re-entry).
4. Choose the expression the evidence supports: probability or interval, ordered support, conditional direction, or unknown. Keep real probability, actors' beliefs, decision weights, model path rankings, and computation priorities apart; model sampling frequencies are never real probabilities, and no number is invented from prose or model confidence.
5. Preregister the calibration metric, evaluation rule, response regime, early signals, reverse signals, review triggers, pause conditions, retirement conditions, and append-only writeback plan. Measure warning clocks to the point where the last affected person can complete protection.
6. At the deadline, assign exactly one result state: `supported`, `not_supported`, `unresolved`, `target_invalid`, or `not_evaluable`. Evaluate recursive orders separately against their own simpler baselines, and answer separately how the forecast scored, what publication or action changed, and whether adopting the forecast and response is appropriate.
7. Append the observation source, actual result, metric, baseline comparison, distributional errors, unexpected effects, downgrade or retirement decision, and next review. Never overwrite the original target, probability, horizon, or failure.
8. State the narrowest output ceiling and recommended handoff. Keep `authorization_effect` equal to `none` in every version.

## Method Record

Create or extend a schema-valid Method Record. Preserve complete parent ID/version lineage, trace module inputs and output, and apply the ceiling algebra. The full schema ships with the suite router at `ariadne-skill/references/method-record.schema.json`; the complete standalone example in [references/forecast-contract.md](references/forecast-contract.md) is schema-checked in CI. The typed forecast payload always carries both closed branches and exactly one is non-null. For a live forecast, fill the complete `preregistration` (including `recursion_stage` and `response_regime`), link its `record_id` and `record_version` to the current Method Record, and set `post_hoc_reconstruction: null`. For an outcome-aware reconstruction, set `preregistration: null`, fill every reconstruction field including `calibration` and `failure_classification`, and never disguise it as preregistration.

A normal module child preserves or lowers its parent ceiling. Raise only in a child that newly admits named external evidence or a newly fulfilled declared protocol. Keep `authorization_effect: none`.

## Output Contract

Publish the complete analysis by default: open with the current judgment and its scope, then the forecast ID, frozen target and deadline, input cutoff, simple baseline, every substantive path compared, expression strength, early and reverse signals, evaluation rule, failure states, next review, and compact Method Record. Do not drop substantive analysis because it does not change the headline; compress only when the user asks for brevity, and keep the full version available. Use `requirements_only` only when lower permissions remain satisfied and the output adds conditions a downstream external choice process still needs; do not phrase those conditions as a recommendation.

Stop at `description_only` when the object, target, observation rule, horizon, or cutoff is not stable. Stop at `diagnostic_only` after publishing or evaluating a forecast. Never claim inevitability, empirical verification from simulation, value priority, consent, jurisdiction, or permission to act.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Quick Reference

| Situation | Required response |
|---|---|
| No judgeable target or deadline | Do not publish a forecast; repair the contract. |
| No fair simple baseline | Keep only a scenario or conditional direction. |
| Data support ranking but not probability | Publish an ordered support level, not a number. |
| A path matters for its consequences, not its likelihood | Prioritize checking it, publish the reason, keep its probability unknown. |
| Warning is used to trigger responses | Register the response regime; score the original target separately from response effects. |
| Outcome changes the object identity | Mark `target_invalid`; preserve the original record. |
| Complex model ties the baseline | Prefer the baseline and withdraw incremental-ability claims. |
| Action question follows | Hand off conditions to `ariadne-choice`; keep authorization at `none`. |

## Mini Example

Skeleton only, not a complete record; the schema-valid template ships with the suite router as `l1-record-template.md`.

```yaml
# Input: "Will at least 3 of the 24 team members resign by 2026-11-30?"
target: three voluntary departure notices from the frozen roster
horizon: {start: '2026-09-01', deadline: '2026-11-30'}
simple_baseline: matched historical frequency predicts two departures
recursion_stage: 0
output_ceiling: description_only
```

## Common Mistakes

- **Backdating the forecast:** Treat an outcome-aware account as explanation, not preregistration.
- **Choosing a weak baseline:** Match the information, target, horizon, budget, and metric before comparing complexity.
- **Calling every branch a hit:** Freeze path relations and success rules before the outcome.
- **Turning prose or sample counts into probabilities:** Downgrade to rank, direction, or unknown when calibration support is absent.
- **Treating "no event" as success or false alarm:** Separate the forecast's score from what the response changed.
- **Counting `unresolved` as partial success:** Keep all five result states distinct.
- **Repairing failure by editing history:** Append a child record and preserve the failed original.
- **Converting accuracy into authority:** Keep forecast, choice, and authorization in separate records.

## Load Detailed Guidance

Read [references/forecast-contract.md](references/forecast-contract.md) when defining fields, selecting baselines or metrics, choosing an expression, evaluating recursive forecasts or response regimes, publishing a result, writing back outcomes, or following the worked example.
