# Forecast Contract

Use this reference to build or evaluate a forecast registry entry. Keep the registry entry beside the common Method Record; link them with the forecast ID and claim ID rather than adding undeclared keys to the Method Record schema. Section anchors (§) point to the source text named in `ariadne-skill/references/source-navigation.json`.

## 1. Preserve Output Isolation

Keep four outputs distinct (§12.1):

| Output | Question | Maximum content |
|---|---|---|
| Explanation | What happened and through which candidate mechanism? | Bounded account of past or current evidence. |
| Dynamic derivation | What paths follow if declared events and conditions occur? | Conditional paths and differentiating signals. |
| Conditional forecast | Which path or target should receive more support by a deadline? | Preregistered, calibrated, falsifiable future judgment. |
| Finite choice | What should be done, how, when to stop, and when not to act? | A refutable analytic recommendation under explicit norms, or an authorized bounded choice record; the two identities stay separate. |

Do not let explanation certify a future result, let a branch set count as a forecast, or let forecast confidence create values, consent, jurisdiction, or authorization. "Predicted a consequence" never turns into "may make others bear an action". Even a passed finite choice does not guarantee successful execution and still needs stopping, rollback, and writeback.

## 2. Freeze the Forecast Registry Entry

Freeze the entry after the input cutoff and before the outcome (§12.2). Use explicit `unknown`, `not_observable`, `not_applicable`, or `withheld_for_protection` states where appropriate.

| Field | Required content |
|---|---|
| `forecast_id` | Stable identifier that survives later failure. |
| `record_id` / `record_version` | Linked Ariadne Method Record and its version. |
| `model_version` | Exact method, model, or rule set used. |
| `target` | Observable result, threshold, observer, and decision rule; a vague target such as "the relationship improves" names observables, observer, threshold, and what counts as unresolved. |
| `horizon` | Start, end, and any intermediate deadlines; a window is allowed, a fabricated date is not. |
| `object_scope` | Object boundary, circles, identity criterion, and excluded population, frozen so the target cannot shrink to a successful subgroup. |
| `baseline_time` | State from which change is measured. |
| `input_cutoff` | Last admissible input time; exclude later evidence from the frozen run. |
| `information_set_ids` | Every source admitted at the cutoff. |
| `simple_baseline` | Fair trend, persistence, frequency, single-focus, or domain baseline. |
| `candidate_mechanisms` | Distinguishable channels, each with weakening evidence. |
| `paths` | Mutually exclusive, parallel, or incomparable paths with stable IDs. |
| `recursion_stage` | 0 for a forecast with no recursive re-entry; 1-3 for the order being evaluated. |
| `expression` | Probability or interval, ordered support, conditional direction, or abstention. |
| `evaluation_rule` | Metric, tolerance, missing-data rule, comparison population, and decision threshold when the forecast feeds a decision (otherwise `not_applicable`). |
| `response_regime` | The response arrangement in force when the forecast is used: who receives it, what actions it can trigger, and how those actions could change the outcome, or `none` when the forecast is not used to act. |
| `calibration_plan` | How repeated forecasts will be grouped and checked. |
| `early_signals` | Mechanism-proximal observations expected before the target. |
| `reverse_signals` | Observations that weaken the favored path or support a competitor. |
| `review_triggers` | Conditions that open a new record rather than alter the old one. |
| `pause_conditions` | Conditions that block publication or downstream use. |
| `retirement_conditions` | Conditions that withdraw the model or capability claim. |
| `failure_semantics` | The five deadline states, defined before the deadline. |
| `result_writeback` | Owner, due date, and append-only destination. |

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

Label the result retrospective explanation or method audit. It is never a forecast hit, calibration datum, or evidence that the model could have produced the reconstructed judgment in real time. The typed payload contains both keys and exactly one non-null branch: a complete `preregistration` with `post_hoc_reconstruction: null`, or `preregistration: null` with the complete reconstruction above.

## 3. Bound Local Predictability

Bind every predictability claim to the object and state region, scale and circle scope, time window and allowed error, available information, computation and observation resources, model version, fair baseline, and abstention, invalidation, and retirement conditions (§12.2.1). Whether the world as a whole is predictable cannot be answered directly; claim only a bounded incremental result for the registered task.

**Classes, grades, intervals, and probabilities carry different duties; they are not a precision ladder that must be climbed in order.** A class needs observable categories; a grade needs grounds for relative ordering; an interval needs units, generation rules, and error bounds; a probability needs repeated outcomes and calibration or a formally stated model. When even a qualitative direction has no grounds, keep it unknown instead of offering it as the default answer when a probability is missing. Keep formally known probabilities apart from empirical ones, and never let prose structure or an AI supply real-world parameters. A borrowed mathematical or physical theory registers its original object, assumptions, limits or scale laws, error, valid domain, object mapping, counterexamples, and exit conditions, not just the outward form of a formula.

## 4. Use a Fair Simple Baseline

Compare the complex forecast with the simplest adequate alternative under the same information, cutoff, target, and evaluation rule, with reasoning budget and tuning opportunity kept as comparable as possible (§12.3). State separately what added information, added computation, and added structural assumptions contribute; the baseline is not artificially inflated to match the complex model's size. Consider current-state persistence, current-trend continuation, historical frequency, actor-only state, primary-circle-only state, and an established domain model. Do not weaken the baseline or leak complex-model information into one side. A forecasting system needs independent testing or out-of-sample review; otherwise its capability stays unproven.

Record these outcomes honestly: explanation improves but forecast does not ("explanatory gain present, forecasting gain unsupported"); gain appears only in a bounded subgroup; gain decays over time; complex and simple models tie; complex model performs worse. Count complexity costs (missingness, measurement error, privacy risk, overfitting, maintenance debt). Prefer the simple model on a tie, and restrict, downgrade, or retire the complex capability when its gain does not persist.

## 5. Match Expression to Evidence and Use

| Evidence state | Expression |
|---|---|
| A probability model with stated prior, data, and calibration basis | Probability or interval |
| Grounds for grades or ordering | Grade or ranking |
| Identification grounds for a direction | Conditional direction; otherwise unknown |
| Unstable target or object | No forecast; contract repair only |

Sample size alone does not decide the expression type, and "direction only" does not exempt the claim from evidence. Expression strength follows evidence and use, never the certainty the user hopes for (§12.4).

**Keep five quantities apart:** real-world probability, actors' subjective beliefs, decision weights, the model's path ranking, and the allocation of the next computation step. Branch frequencies from repeated model sampling are never real probabilities. The path most worth checking, or most hoped for, is never written as the most likely. When probability cannot be fixed reliably, a path may still be checked first because consequences are severe, the response window is short, or it is easy to distinguish: publish the priority reason and budget, keep the probability unknown, and never invent a percentage to rank. An action comparison separately states normative aims, distributional consequences, and feasible choices; a probability ranking never yields a recommendation ranking directly. A posterior can come from a small sample and an explicit prior, but its real-world use still depends on the model; a very large sample cannot repair a wrong measurement definition.

Match the horizon to each candidate mechanism's update clock: immediate, interaction, organizational, institutional, or long-term. Compressing a long-clock mechanism into a short window misjudges it as ineffective; that is a horizon contract error to repair, not a `not_supported` result. When mechanisms on several clocks coexist, register a separate deadline for each intermediate result.

## 6. Calibrate and Evaluate

Forecasting ability is a long-run registered record, not a writing style (§12.5). Probability tasks use Brier score, log loss, calibration curves, resolution, and interval coverage; rankings use a preregistered rank metric; event detection uses precision, recall, or domain metrics; timing uses window coverage and lead time. Match metrics to use: low-probability high-harm events are not judged on overall accuracy alone, and a false positive that prompts observation costs differently from one that compels action. Good metrics do not prove the explanation, fairness, or permissibility of action. Also track distributional error: which positions are persistently under-forecast or falsely flagged, which triggers affected-party review, remedy, and stronger protection.

**Once a warning is in use, state its response regime.** Keep reach, execution, entry and exit, and record-formation logs. A changed regime requires restating which results are comparable. No observed event is not a false alarm and not a protection success. Claims that harm was avoided need a causal comparison. A prediction defined under the current regime can still be scored against its original target, and the original target, horizon, and success rule are never rewritten after a response.

Answer three parallel questions:

1. **How did the original forecast perform on the frozen target?** Use real labels on the same definition; one case's score is not long-run calibration; missing labels are never filled with zero.
2. **How much did publication or action change the outcome?** Use a proportionate causal comparison; no event alone cannot separate "was low risk" from "was successfully avoided".
3. **Is adopting this forecast and response appropriate?** Under explicit normative premises, compare protection, wrongful refusal, delay, distribution, and cost; neither accuracy nor a positive effect alone grants authority.

Example: a forecast of 0.8 against a label of 0 scores a Brier loss of 0.64; with a registered threshold of 0.5 it is a false positive. That score does not say what the risk would have been without action or that the response was ineffective. Labels of approved cases evaluate only that population; extending to refused, unreached, or exited people needs their labels or an identification method. When the response regime changes, first decide whether the original target is still the same question. Reflexivity never cancels a computable score, and one successful response never rescues every wrong forecast.

## 7. Evaluate Recursive Orders Separately

Freeze first-, second-, and third-order forecasts separately and never merge them into one hit rate (§12.2.2). For each order, compare it with a no-recursion continuation, a direct forecast at the same horizon, and the shallower order plus simple continuation. A third order that only adds story without stable out-of-sample gain stays an exploratory scenario and earns no forecasting standing. Without new external material, every child run's lineage ends at the same frozen start; post-processing cannot manufacture real evidence. When a real intermediate result arrives, open a new frozen run and compare it with the earlier recursive path; never feed the result backward into the old record.

## 8. Register Signals and Triggers

An early signal is not a smaller restatement of the outcome; it is an observable change the path's mechanism should produce first (§12.6). A reverse signal shows a key condition failing or a competing path gaining support. Register both before the result. Triggers open review of object, path, probability, norms, and authorization; they never execute automatically. High-risk uses add veto triggers: a breached protection floor, key affected people unable to exit, corrupted data sources, concentrated distributional error, or declining calibration.

**Clock comparisons end at an action that can be completed.** Detecting a signal, verifying it, publishing, reaching people, being understood, mobilizing resources, and moving to safety or taking effect each have their own delay; an algorithm detecting early does not ensure that the last affected person is protected before harm. Keep the denominators of the operational false-positive rate, the false-alarm share among warnings, and the miss rate separate.

## 9. Close With Failure Semantics and Writeback

Assign exactly one deadline state (§12.7):

| State | Meaning |
|---|---|
| `supported` | The frozen outcome rule was met. |
| `not_supported` | The frozen outcome rule was not met. |
| `unresolved` | The preregistered evidence rule cannot distinguish the result; it is not a compromise. |
| `target_invalid` | The object or identity criterion changed so the target no longer denotes the same thing; never a hit. |
| `not_evaluable` | Data, observation, execution, or timing failure prevents evaluation; say which. |

Changing target, horizon, circle scope, or path grouping after the result forfeits the original success standing; a new explanation is a new version with the old record kept. Append, never replace (§12.12): observation time and source; actual outcome and path match; metric and simple-baseline comparison; unexpected and cross-circle effects; errors by affected position; implementation deviation, kept separate from model error; claim downgrade, variable or path retirement, and next review. One success does not prove generality, and one failure may come from execution deviation; the frozen contract tells them apart, and execution explanations never rescue a model at will.

## 10. Bridge to Finite Choice Without Authorizing

A forecast answers only conditional consequences (§12.8). Forming an analytic recommendation requires explicit normative premises, evidence, affected positions, options, costs and benefits, and change conditions, and the recommendation creates no execution permission. Real adoption additionally needs the choosing subject, jurisdiction, rights floor, distribution, authorization, stopping, appeal, rollback, and remedy (N, PF, J, O, and C12, owned by `ariadne-choice` and `ariadne-audit`). A forecast never generates authorization: high probability does not license forcing others to bear avoidance costs, maximal average benefit does not license ignoring a minority's rights, and recommending no action still reviews the continuing harm and responsibility of not acting. Pass these as missing or externally verified conditions; never manufacture them inside the forecast.

## 11. Publish the Complete Analysis

Publication defaults to the complete analysis (§12.16). Open with the current judgment and its scope, then set out conditions, evidence, and uncertainty in full: cutoff, target and horizon, object and circle scope, simple baseline, every substantive path comparison actually carried out, each path's conditions, early and reverse signals, expression strength, pause conditions, and next review. Never delete substantive analysis because it "does not change the main conclusion", is "a minor branch", or "is not decisive"; never hide conditions in footnotes; never let "the model thinks" replace evidential responsibility. Compress the visible answer only when the user explicitly asks for brevity or sets a length, and keep the full analysis available; when it exceeds one delivery, deliver it in consecutive sections and say what remains. A summary, attachment link, or coverage marker never replaces the argument.

| Publication status | What the text may say |
|---|---|
| Explanation only | What happened and through which candidate mechanisms; no future claim |
| Derivation only | Conditional paths and signals; no "will" or "expected hit" phrasing |
| Registered forecast | The frozen judgment with its baseline, signals, and failure semantics |
| Norms not yet passed | An analytic recommendation under explicit premises is possible; real execution still needs N, PF, J, and O |
| Externally authorized | The authorization record lets the named subject act within its ceiling and stop on its conditions; the authority is never attributed to the model |

After publication the publisher corrects misreadings instead of exploiting them; updates are appended as new versions, and the original title, probability, horizon, and failure records stay traceable.

## Worked Example: Team Attrition Forecast

Treat this as an illustrative contract, not evidence about a real team.

### Frozen registry entry

```yaml
forecast_id: F-TEAM-017
record_id: ariadne:team-attrition:root:v1
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
recursion_stage: 0
expression: P1 has medium support; P2 has low-to-medium support; no numeric probability is admitted.
evaluation_rule: Apply the frozen notice, roster, and deadline rules; compare the top-ranked path and threshold result with the simple baseline; decision threshold not_applicable.
response_regime: Shared only with the team lead and HR partner for monitoring; it triggers no personnel action.
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
record_id: ariadne:team-attrition:root:v1
schema_version: '2.0'
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
    aggregation: individual notices within one team
    time: three months
    jurisdiction: observation only
  identity_criterion: The roster and departure definition remain frozen through evaluation.
  task_profile:
    target_query: Whether at least 3 voluntary departure notices arrive from the frozen roster by the deadline
    horizon: 2026-09-01 through 2026-11-30
    environment: Current workload, appeal process, and labor market at cutoff
    allowed_operations: Observation only; the forecast triggers no personnel action
    error_tolerance: Ordered path support; no numeric probability
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
  transform_kind: scale
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
  - 'withheld_for_protection: protected reports may be withheld'
  - 'unknown: the small sample does not support a calibrated probability'
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
    record_id: ariadne:team-attrition:root:v1
    record_version: 1
module_payloads:
- module: ariadne-forecast
  payload:
    preregistration:
      forecast_id: F-TEAM-017
      record_id: ariadne:team-attrition:root:v1
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
      recursion_stage: 0
      expression: Ordered support without a numeric probability.
      evaluation_rule: Apply the frozen notice, roster, and deadline rules and compare with the baseline.
      response_regime: Shared only with the team lead and HR partner for monitoring; it triggers no personnel action.
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

If the threshold is later met, append a child record with the observed result, baseline comparison, distributional review, and any downgrade. Do not rewrite "medium support" as a probability, and do not infer that management is authorized to restructure the team.
