# Forecast Contract

Use this reference to build or evaluate a forecast registry entry. Keep the registry entry beside the common Method Record; link them with the forecast ID and claim ID rather than adding undeclared keys to the Method Record schema.

## 1. Preserve Output Isolation

Keep four outputs distinct:

| Output | Question | Maximum content |
|---|---|---|
| Explanation | What happened and through which candidate mechanism? | Bounded account of past or current evidence. |
| Dynamic derivation | What paths follow if declared events and conditions occur? | Conditional paths and differentiating signals. |
| Conditional forecast | Which path or target should receive more support by a deadline? | Preregistered, calibrated, falsifiable future judgment. |
| Finite choice | What may a qualified subject choose under values and authority? | Conditional choice record with protection and correction. |

Do not let explanation certify a future result, let a branch set count as a forecast, or let forecast confidence create values, consent, jurisdiction, or authorization.

## 2. Freeze the Forecast Registry Entry

Freeze the entry after the input cutoff and before the outcome. Use explicit `unknown`, `not_observable`, `not_applicable`, or `withheld_for_protection` states where appropriate.

| Field | Required content |
|---|---|
| `forecast_id` | Stable identifier that survives later failure. |
| `record_id` / `record_version` | Linked Ariadne Method Record and its version. |
| `model_version` | Exact method, model, or rule set used. |
| `target` | Observable result, threshold, observer, and decision rule. |
| `horizon` | Start, end, and any intermediate deadlines. |
| `object_scope` | Object boundary, circles, identity criterion, and excluded population. |
| `baseline_time` | State from which change is measured. |
| `input_cutoff` | Last admissible input time; exclude later evidence from the frozen run. |
| `simple_baseline` | Fair trend, persistence, frequency, single-focus, or domain baseline. |
| `candidate_mechanisms` | Distinguishable channels, each with weakening evidence. |
| `paths` | Mutually exclusive, parallel, or incomparable paths with stable IDs. |
| `expression` | Probability interval, support rank, direction, or abstention. |
| `evaluation_rule` | Metric, tolerance, missing-data rule, and comparison population. |
| `calibration_plan` | How repeated forecasts will be grouped and checked. |
| `early_signals` | Mechanism-proximal observations expected before the target. |
| `reverse_signals` | Observations that weaken the favored path or support a competitor. |
| `review_triggers` | Conditions that open a new record rather than alter the old one. |
| `pause_conditions` | Conditions that block publication or downstream use. |
| `retirement_conditions` | Conditions that withdraw the model or capability claim. |
| `result_writeback` | Source, due date, responsible recorder, and append-only destination. |

Define success, failure, unresolved evidence, object conversion, and non-evaluability before the deadline. Do not use a vague target such as “the relationship improves” without observable variables, thresholds, an observer, and an outcome rule.

### Post-hoc reconstruction

When the outcome was already knowable before the forecast record existed, do not create a forecast entry. Create an outcome-aware reconstruction and fill every typed payload field:

| Field | Required content |
|---|---|
| `record_id` / `record_version` | Current Method Record link for the reconstruction; this is not a backdated forecast link. |
| `original_question` | The exact future-looking question being reconstructed. |
| `reconstruction_time` | When the retrospective account was created. |
| `target` / `deadline` | The target and deadline that would have been frozen. |
| `input_cutoff` | The historical cutoff used to prevent hindsight leakage. |
| `available_information_ids` | Every source demonstrably available at that cutoff. |
| `model_version` | The exact rule or model reconstructed, not a later improved version. |
| `simple_baseline` | The fair comparator that would have been available then. |
| `expression` / `evaluation_rule` | The strength and scoring rule that would have been published. |
| `early_signals` / `reverse_signals` | Signals defined without using the known outcome to select only favorable items. |
| `actual_outcome` | The later outcome, kept separate from the reconstructed judgment. |
| `hindsight_exclusions` | Later sources, model changes, labels, and interpretations excluded from the reconstruction. |
| `calibration` | Metric, retrospective assessment, simple-baseline comparison, and limitations; explicitly exclude the reconstruction from live calibration. |
| `failure_classification` | Exactly one of `supported`, `not_supported`, `unresolved`, `target_invalid`, or `not_evaluable`, interpreted as a method audit rather than a forecast hit. |

Label the result retrospective explanation or method audit. It is never a forecast hit, calibration datum, or evidence that the model could have produced the reconstructed judgment in real time.

The typed payload contains both keys and exactly one non-null branch: a complete `preregistration` with `post_hoc_reconstruction: null`, or `preregistration: null` with the complete reconstruction above.

## 3. Bound Local Predictability

Bind every predictability claim to:

- the object and state region;
- the scale and circle scope;
- the time window and allowed error;
- the available information, observation, and computation;
- the model version and fair baseline;
- the abstention, invalidation, and retirement conditions.

Do not claim that a whole domain or the world is predictable. Claim only a bounded incremental result for the registered task.

Admit quantification in this order:

1. Use a nominal class when only categories are observable.
2. Use an ordered grade when evidence supports relative ordering.
3. Use an interval when units, generation rules, and error bounds exist.
4. Use a probability only when repeated outcomes and calibration support it.

Downgrade when a required measurement, unit, sample, generation method, or calibration record is absent. Treat imported formal theories as contracts: record their original object, assumptions, valid domain, error, mapping, counterexamples, and exit condition.

## 4. Use a Fair Simple Baseline

Compare the complex forecast with the simplest adequate alternative under the same target, horizon, cutoff, information access, and metric. Consider:

- current-state persistence;
- current-trend continuation;
- historical frequency;
- actor-only state;
- primary-circle-only state;
- an established domain model.

Do not deliberately weaken the baseline or leak complex-model information into only one side. Retain extra circles or variables only when they produce stable out-of-sample gain that exceeds their missingness, measurement, privacy, overfitting, and maintenance costs.

Record these outcomes honestly:

- explanation improves but forecast does not;
- gain appears only in a bounded subgroup;
- gain decays over time;
- complex and simple models tie;
- complex model performs worse.

Prefer the simple model on a tie. Restrict, downgrade, or retire the complex capability when its gain does not persist.

## 5. Match Expression to Evaluation

| Evidence and task | Expression | Evaluation |
|---|---|---|
| Stable repeated binary or multinomial outcomes | Probability or interval | Brier score, log loss, calibration curve, resolution, interval coverage. |
| Limited sample with distinguishable paths | Ordered support | Preregistered rank score and baseline comparison. |
| Sparse data with plausible mechanisms | Conditional direction | Trigger precision, reverse-signal response, and explicit abstention. |
| Unstable object or target | No forecast | Contract repair only. |

Match the horizon to the update clock of each candidate mechanism: immediate, interaction, organizational, institutional, or long-term. An immediate reaction can use a short window; organizational or institutional change needs a longer one. Compressing a long-clock mechanism into a short window misjudges it as ineffective: that is a horizon contract error to repair, not a `not_supported` result. Extrapolating a short-window signal without limit misjudges a trend. When mechanisms on several clocks coexist, register a separate deadline for each intermediate result.

Match metrics to use. Include false-positive and false-negative costs, low-probability high-harm events, timing error, and error concentration across affected positions. Good predictive metrics do not prove the mechanism, fairness, or permissibility of action.

## 6. Evaluate Recursive Orders Separately

Freeze first-, second-, and third-order forecasts separately. For each order:

1. Compare it with a no-recursion continuation baseline.
2. Compare it with a direct forecast at the same horizon.
3. Compare it with the shallower order plus simple continuation.
4. Keep all downstream reasoning tied to the same original evidence cutoff unless new external material arrives.

Treat deeper model output as simulated content, not new evidence. When a real intermediate result arrives, open a new frozen run and compare it with the earlier recursive path; never feed the result backward into the old record.

## 7. Register Signals and Triggers

Define an early signal as a mechanism-proximal change expected before the outcome. Define a reverse signal as evidence that a necessary condition is failing or a competitor is strengthening.

Use triggers to open review, not to execute automatically. Add veto triggers for high-impact uses, including protection-floor failure, loss of a real exit, corrupted data, concentrated distributional error, or calibration decline.

## 8. Close With Failure Semantics and Writeback

Assign exactly one deadline state:

| State | Meaning |
|---|---|
| `supported` | The frozen outcome rule was met. |
| `not_supported` | The frozen outcome rule was not met. |
| `unresolved` | The preregistered evidence rule cannot distinguish the result. |
| `target_invalid` | The object or identity criterion changed so the target no longer denotes the same thing. |
| `not_evaluable` | Data, observation, execution, or timing failure prevents evaluation. |

Append, do not replace:

- observation time and source;
- actual outcome and path match;
- metric and simple-baseline comparison;
- unexpected and cross-circle effects;
- errors by affected position;
- implementation deviation, kept separate from model error;
- claim downgrade, variable or path retirement, and next review.

Keep every success, failure, unresolved result, invalid target, and non-evaluable run available for governance review.

## 9. Bridge Without Authorizing

Before any finite-choice handoff, require explicit value premises, the choosing subject, jurisdiction, affected positions, rights floor, option set, distribution, authorization evidence, stopping, appeal, rollback, and remedy. Pass these as missing or externally verified conditions. Do not manufacture them inside the forecast.

Publish the condition before the judgment. Include the cutoff, target, horizon, scope, baseline, leading paths, necessary conditions, early and reverse signals, expression strength, pause condition, and next review. Put any finite-choice summary in a separate normative section.

## Worked Example: Team Attrition Forecast

Treat this as an illustrative contract, not evidence about a real team.

### Frozen registry entry

```yaml
forecast_id: F-TEAM-017
record_id: ariadne:forecast:F-TEAM-017
record_version: 1
model_version: lattice-forecast-rule-1
target: At least 3 of the 24 people in the frozen product-team roster submit a voluntary departure notice by 2026-11-30.
horizon: 2026-09-01 through 2026-11-30
object_scope: The 24-person roster at cutoff; involuntary exits and transfers outside the roster are excluded.
baseline_time: 2026-08-31T00:00:00+08:00
input_cutoff: 2026-08-31T16:00:00+08:00
information_set_ids: [SRC-HR-HISTORY, SRC-HOURS-CUTOFF, SRC-APPEAL-CUTOFF]
simple_baseline: Matched historical frequency predicts 2 voluntary departures.
candidate_mechanisms:
  - Workload persistence with unresolved appeal failures.
  - Verified workload reduction with effective appeal repair.
paths:
  - P1: Workload and appeal failures persist; threshold is met.
  - P2: Verified workload and appeal changes occur; threshold is not met.
  - P3: Roster identity changes materially; target becomes invalid.
expression: P1 has medium support; P2 has low-to-medium support; no numeric probability is admitted.
evaluation_rule: Apply the frozen notice, roster, and deadline rules; compare the top-ranked path and threshold result with the simple baseline.
calibration_plan: Score all forecasts under lattice-forecast-rule-1 by registered rank score after at least 10 cases.
early_signals:
  - Verified change in actual weekly hours, not only policy text.
  - Independent appeal cases resolved within the promised window.
reverse_signals:
  - Public policy changes without observed workload change.
  - Reduced public complaint alongside increased protected or anonymous reports.
review_triggers:
  - Roster identity or departure definition changes.
pause_conditions:
  - Roster or departure definition changes before evaluation.
  - Reporting creates retaliation or identity exposure.
retirement_conditions:
  - Repeated registered runs fail to beat the matched historical baseline.
result_writeback: Append all five result states on 2026-12-01 using HR notices plus protected-position review.
failure_semantics: Keep supported, not_supported, unresolved, target_invalid, and not_evaluable distinct.
```

### Linked common Method Record

<!-- method-record-example:start -->
```yaml
record_id: ariadne:forecast:F-TEAM-017
schema_version: '1.3'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: conditional_forecast
object_contract:
  boundary: Frozen 24-person product-team roster; exclude involuntary exits and outside transfers.
  state_variables:
  - voluntary departure notices
  - actual weekly hours
  - appeal resolution
  relations_or_transitions:
  - P1 persistence path
  - P2 verified-repair path
  - P3 object-conversion path
  interfaces:
  - HR notice record
  - protected reporting channel
  - workload record
  time_window: 2026-09-01 through 2026-11-30
  scale_profile:
    A: individual notices within one team
    T: three months
    J: observation only
  identity_criterion: The roster and departure definition remain frozen through evaluation.
  status: candidate
evidence_cutoff:
  as_of: '2026-08-31T16:00:00+08:00'
  included_source_ids:
  - SRC-HR-HISTORY
  - SRC-HOURS-CUTOFF
  - SRC-APPEAL-CUTOFF
  excluded_after_cutoff: true
scale_scope:
  source: individual and team records
  target: one frozen team
  transform_status: audited
claim_ledger:
- claim_id: FC-F-TEAM-017
  claim_type: G
  text: P1 receives more support than P2 for the registered threshold and horizon.
  status: candidate
  support_ids:
  - SRC-HR-HISTORY
  - SRC-HOURS-CUTOFF
  counterevidence_ids:
  - SRC-APPEAL-CUTOFF
  support_rule_ids: []
rule_registry: []
conflicts: []
unknowns_and_counterevidence:
  unknowns:
  - Protected reports may be withheld
  - and the small sample does not support a calibrated probability.
  counterevidence:
  - A verified reduction in actual hours would strengthen P2.
output_ceiling: description_only
ceiling_transition:
  operation: root
  inputs: []
  basis: []
  result: description_only
module_runs:
- module: ariadne-forecast
  status: completed
  input_records: []
  output_record:
    record_id: ariadne:forecast:F-TEAM-017
    record_version: 1
module_payloads:
- module: ariadne-forecast
  payload:
    preregistration:
      forecast_id: F-TEAM-017
      record_id: ariadne:forecast:F-TEAM-017
      record_version: 1
      model_version: lattice-forecast-rule-1
      target: At least 3 verified voluntary departure notices from the frozen roster by the deadline.
      horizon:
        start: '2026-09-01T00:00:00+08:00'
        deadline: '2026-11-30T23:59:59+08:00'
      object_scope: The frozen 24-person roster; exclude involuntary exits and outside transfers.
      baseline_time: '2026-08-31T00:00:00+08:00'
      input_cutoff: '2026-08-31T16:00:00+08:00'
      information_set_ids:
      - SRC-HR-HISTORY
      - SRC-HOURS-CUTOFF
      - SRC-APPEAL-CUTOFF
      simple_baseline: Matched historical frequency predicts 2 voluntary departures.
      candidate_mechanisms:
      - Workload persistence with unresolved appeal failures.
      - Verified workload reduction with effective appeal repair.
      paths:
      - P1 threshold met
      - P2 threshold not met
      - P3 target invalid
      expression: Ordered support without a numeric probability.
      evaluation_rule: Apply the frozen notice, roster, and deadline rules and compare with the baseline.
      calibration_plan:
        metric: registered rank score
        reference_class: all forecasts under lattice-forecast-rule-1
        minimum_cases: 10
      early_signals:
      - Verified change in actual weekly hours.
      - Independent appeal cases resolved within the promised window.
      reverse_signals:
      - Public policy changes without observed workload change.
      - Protected reports rise while public complaints fall.
      review_triggers:
      - Roster identity or departure definition changes.
      pause_conditions:
      - Reporting creates retaliation or identity exposure.
      retirement_conditions:
      - Repeated registered runs fail to beat the matched historical baseline.
      failure_semantics:
        supported: The frozen outcome rule is met.
        not_supported: The frozen outcome rule is not met.
        unresolved: The evidence rule cannot distinguish the result.
        target_invalid: The object identity changed.
        not_evaluable: Observation or timing failure prevents evaluation.
      result_writeback:
        owner: forecast-registry@example.invalid
        due_at: '2026-12-01T12:00:00+08:00'
        destination: FORECAST-REGISTRY/F-TEAM-017
    post_hoc_reconstruction: null
recommended_next_modules:
- ariadne-choice
- ariadne-audit
authorization_effect: none
```
<!-- method-record-example:end -->

If the threshold is later met, append a child record with the observed result, baseline comparison, distributional review, and any downgrade. Do not rewrite “medium support” as a probability, and do not infer that management is authorized to restructure the team.
