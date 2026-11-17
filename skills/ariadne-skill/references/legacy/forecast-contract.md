# Legacy Forecast Contract

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/forecast-contract.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## Legacy Method Record serialization

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

## Legacy forecast candidate-count encoding

| `competition_search` | In schema 2.1, required when either mechanisms or paths has only one entry: `search_scope`, `reason_no_alternative`, `failure_conditions`. Not required by legacy 2.0, whose original two-entry minimum remains unchanged. A unique candidate does not establish support or remove the baseline. |

## Legacy forecast payload branches

Label the result retrospective explanation or method audit. It is never a forecast hit, calibration datum, or evidence that the model could have produced the reconstructed judgment in real time. The typed payload contains both keys and exactly one non-null branch: a complete `preregistration` with `post_hoc_reconstruction: null`, or `preregistration: null` with the complete reconstruction above.
