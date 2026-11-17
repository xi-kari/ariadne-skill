# Formal forecast registration

Use this contract when the `project` path will issue a dated, evaluable future claim. Ordinary conditional derivation, scenario exploration and explanations need no forecast artifact. Registration is a purpose-specific responsibility from source §12, not a global prerequisite for analysis, creation or recommendation.

Freeze the actual forecast before its outcome is known. A retrospective reconstruction can still be useful, but it must not be registered as a prior prediction or counted as a hit. The local tool records when it wrote a file; it cannot establish when a person actually learned the outcome, whether a supplied source is genuine, or whether the forecast is useful.

## Required content and expression

The [artifact 1.0 schema](forecast.schema.json) has four types: `forecast_draft`, `forecast_registration`, `resolution_draft`, and `forecast_resolution`. It does not require a Method Record, module runs or an authorization ceiling. The twenty-field legacy record is not a prerequisite.

| Forecast field | Responsibility |
|---|---|
| `forecast_id`, `outcome_known` | A unique local identifier and an explicit declaration that the outcome is not known. IDs use 1–80 letters, digits, underscores or hyphens, starting with a letter or digit. |
| `model` | The model or rule's `id` and `version`. A named manual rule is valid; model identity must not change silently after results. |
| `target` | Question, object/population scope and the exact outcome rule. Preserve target identity across evaluation. |
| `input` | Input cutoff and identified sources, each with description, material kind and availability time. Assumptions, reports, observations, simulations, formal material and inferences retain their different identities. |
| `window` | Start, deadline and task-specific error tolerance. |
| `baseline` | Simple comparison, its frozen expectation, evaluation rule and timezone-bearing `as_of` timestamp no later than the input cutoff. A candidate exception never removes this comparison. |
| `mechanisms`, `paths` | Material-grounded candidates with source and mechanism references. Include the reasonable candidates actually found. One mechanism or one path requires `competition_search`: search scope, why no additional complete candidate was identified, and failure conditions. A single candidate is not thereby more credible. |
| `expression` | One explicitly typed expression and its basis; do not silently convert among the types below. |
| `decision_use` | Either `status: not_applicable` with a reason, or `status: applicable` with the decision and its use threshold. The threshold explains how a forecast would inform a decision; it grants no permission to execute. |
| `evaluation` | Evaluation rule, calibration plan and the meanings of all five outcome states. A plan is not evidence that calibration has occurred. |
| `signals` | Early and reverse signals, pause conditions and retirement conditions. A restatement of the outcome is not an independent early signal. |
| `response_regime` | How publication or response actions may affect the target and observations. Evaluate the original forecast, the effects of responding, and whether adoption was appropriate separately. |
| `review` | A responsible owner, next review time, writeback deadline and destination. The owner must actually arrange the review; this file schedules no background work. |

The expression kinds are deliberately distinct:

- `probability`: `value` between 0 and 1, the `event`, `basis`, `basis_source_ids`, and `method` (`empirical_estimate`, `empirically_calibrated` or `probabilistic_model`). An empirical estimate may be declared before its calibration has been established. Calibration is a separate evaluation responsibility; neither the selected label nor validation verifies calibration or a model's real-world premises.
- `belief`: a named `subject`, their subjective `value` between 0 and 1, `basis` and `basis_source_ids`. The basis must state the information conditions under which that subject holds the belief. It is not an empirically calibrated frequency by declaration.
- `scenario_weight`: `weights` containing `path_id` and nonnegative `value`, a `normalization` description, `purpose`, `basis` and source IDs. State whether the weights allocate decision attention, computation, exploration or another specified resource. Weights are not outcome probabilities.
- `path_ranking`: ordered `tiers` of path IDs, permitting ties, with `basis` and source IDs. Ranking requires support even when no numbers are used. An omitted path remains unranked; it is not silently assigned to the lowest tier.
- `qualitative`: a bounded `statement`, `basis` and source IDs.
- `unknown`: a `reason`, with no numeric value or ranking. This is an explicit abstention record, not an evaluable positive or negative forecast. Inadequate material must not be completed with an invented probability.

Repeated model samples, internal simulated frequencies and the number of candidate paths are not empirical probabilities. Retain shared source lineage; a simulation remains a simulation even when its numeric output is precise. Formal or probabilistic calculations have their own premises and mapping responsibilities.

This schema supports scalar probabilities and beliefs, not numeric intervals. Preserve an interval forecast in an equivalent durable external registration that meets the same pre-outcome, identity, evidence, baseline and evaluation responsibilities. Do not collapse an interval into a point estimate merely to fit this tool.

## Local commands and file behavior

From the installed `ariadne-skill` directory:

```sh
python scripts/forecast.py validate draft.json
python scripts/forecast.py register --input draft.json --registry ./forecast-registry
python scripts/forecast.py resolve --id queue-week-1 --input observation.json --registry ./forecast-registry
python scripts/forecast.py validate ./forecast-registry/queue-week-1/forecast.json
```

The tool needs Python 3.10+ and `jsonschema`; install the runtime dependency with `python -m pip install jsonschema==4.26.0` if needed (the repository also pins it in `requirements-dev.txt`). Safe file access uses POSIX directory descriptors and `O_NOFOLLOW`, available on the tested Linux environment and normally on macOS/WSL. Native environments without those operations receive an explicit failure; do not claim that a registration was saved there. No network or model call is made.

`register` accepts only `forecast_draft`. It sets a real UTC `registered_at`, writes `forecast-registry/<forecast_id>/forecast.json` once, flushes it and checks the bytes by reading them back. The receipt reports the artifact path and SHA-256. Retain the receipt if later integrity comparisons matter. The tool does not overwrite an existing ID, including an existing directory with that name.

Registration refuses a known outcome, a deadline that has arrived, a future input cutoff, a baseline or input source dated after that cutoff, or inconsistent dates. The required ordering is `baseline.as_of <= cutoff <= start <= deadline < writeback`; registration must occur at or after the cutoff, before the deadline and no later than the next review. Times require timezone-bearing RFC 3339 dates with seconds 00–59; both `Z` and `z` work on Python 3.10. Leap-second timestamps are outside this tool's supported comparison format. Unknown local dates cannot be repaired by assuming a timezone.

IDs cannot traverse paths. Directory traversal segments and symbolic links in registry and input paths are rejected; existing files cannot be overwritten. JSON must be a single UTF-8 object with unique keys and finite numeric values. This protects the tool's writes; it does not make the filesystem immune to a user changing files outside the tool.

To change target, inputs, model version, baseline, decision-use threshold or evaluation rule, create a new draft and a new forecast ID, explicitly citing the earlier artifact in the new source descriptions. Keep the earlier registration and its failures. A later revision does not rewrite the earlier score or become a second independent source.

## Appending observations and retaining failures

`resolve` takes a `resolution_draft` and appends `resolutions/<resolution_id>.json` beneath the forecast directory. It adds real UTC `resolved_at`, the forecast ID and the SHA-256 of the frozen registration. It validates and reads back the new file, and checks that the original registration bytes remain unchanged. A second observation or correction needs a new resolution ID. No older observation is replaced.

The observation supplies `observed_at`, identified `sources`, `actual_result` (a string or explicit `null`), one of five `status` values, `reason`, `baseline_comparison`, `response_observations`, and `next_step`. Source descriptions must distinguish outcome observation from an assumption or simulation. A settled result needs an observed or reported outcome source. Resolution refuses observations or source-availability times in the future.

| State | Required handling |
|---|---|
| `supported` | Record outcome material and explain how the frozen expression's evaluation criterion is met; unavailable for an `unknown` expression. |
| `not_supported` | Record outcome material and explain how the frozen expression's criterion failed; unavailable for an `unknown` expression. It is not automatically support for a null mechanism. |
| `unresolved` | Retain the conflict or insufficiency that prevents a conclusion. |
| `target_invalid` | Explain the broken identity, target condition, or registration premise; preserve the original artifact. |
| `not_evaluable` | Explain why the forecast cannot be evaluated, including an explicit original abstention or unavailable outcome/comparison. Retain any actual target observation separately. |

These are explicit reviewer assignments, not automatic scores. A target event occurring does not establish probability calibration, the accuracy of an unknown expression, the truth of a proposed mechanism or the value of the skill. When the frozen expression is `unknown`, `resolve` rejects `supported` and `not_supported`: retain an observed target result with `not_evaluable` and explain the abstention. A target crossing its threshold does not turn an abstention into a hit. The tool neither computes a success rate nor infers the causal benefit of a response action.

Missing labels remain `actual_result: null`; they are never filled with zero. A reasoned `not_evaluable` or `unresolved` observation can have no outcome source, provided the absence is explained. Keep the baseline comparison explicit even when it too is not evaluable. Evidence discovered later that the outcome predated registration may be retained in an invalidity or unresolved review; it cannot be appended as a successful prior forecast.

`validate` checks structure, field references and applicable timing conditions. It does not reverify source facts, authenticate a saved timestamp, certify an external consequence, or schedule later review. After registration, the owner remains responsible for collecting observations and invoking `resolve`.

## Complete synthetic draft

This is a teaching example, not a real forecast or evidence. Replace its identity, dates, supplied assumptions and owner with the actual task before registering; do not claim a hypothetical snapshot was observed. The single candidate is deliberately paired with an `unknown` expression.

```json
{
  "artifact_version": "1.0",
  "artifact_type": "forecast_draft",
  "forecast_id": "queue-week-1",
  "outcome_known": false,
  "model": {"id": "manual-queue-rule", "version": "1"},
  "target": {
    "question": "Will the queue exceed 100 open items at the deadline?",
    "scope": "One specified support queue under an unchanged counting rule.",
    "outcome_rule": "Use the observed deadline count; missing observation is not zero."
  },
  "input": {
    "cutoff": "2027-01-01T10:00:00Z",
    "sources": [{"source_id": "example-input", "description": "Synthetic premise: the queue currently has 80 items.", "kind": "assumption", "available_at": "2027-01-01T09:00:00Z"}]
  },
  "window": {"starts_at": "2027-01-02T00:00:00Z", "deadline": "2027-01-09T00:00:00Z", "error_tolerance": "Use the exact count if available; preserve missingness otherwise."},
  "baseline": {"as_of": "2027-01-01T09:00:00Z", "description": "Persistence", "expectation": "80 open items", "evaluation_rule": "Compare the actual count with 80 using the same observation."},
  "mechanisms": [{"candidate_id": "balance", "claim": "Inflow and service may balance.", "basis_source_ids": ["example-input"]}],
  "paths": [{"path_id": "stable", "description": "Queue remains approximately stable if inflow and service balance.", "mechanism_ids": ["balance"], "basis_source_ids": ["example-input"]}],
  "competition_search": {"search_scope": "The supplied synthetic premise only.", "reason_no_alternative": "No further material-grounded mechanism or path is available.", "failure_conditions": "Measured inflow or service differs enough to change the path."},
  "expression": {"kind": "unknown", "reason": "The supplied premise cannot support a probability or ranking."},
  "decision_use": {"status": "not_applicable", "reason": "This exercise monitors the target without selecting an action."},
  "evaluation": {
    "rule": "Apply the frozen threshold to the observed deadline count.",
    "calibration_plan": "No calibrated probability is claimed; retain outcome and baseline comparison for future review.",
    "failure_rules": {"supported": "Unavailable: the unknown expression makes no positive forecast.", "not_supported": "Unavailable: an abstention cannot count as a forecast miss.", "unresolved": "Conflicting observations cannot be settled.", "target_invalid": "The queue or counting rule changes.", "not_evaluable": "The expression abstained; retain any actual count without scoring a forecast, and keep missing labels explicit."}
  },
  "signals": {"early": ["Measured change in arrivals or service."], "reverse": ["Sustained change opposite to the candidate path."], "pause": ["Observation source is unavailable."], "retirement": ["Queue identity is replaced."]},
  "response_regime": "Monitoring only; the draft triggers no intervention.",
  "review": {"owner": "The actual task owner must be identified", "next_review_at": "2027-01-05T00:00:00Z", "writeback_due_at": "2027-01-10T00:00:00Z", "destination": "The explicitly chosen local registry"}
}
```
