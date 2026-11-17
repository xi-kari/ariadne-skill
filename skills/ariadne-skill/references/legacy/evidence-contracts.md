# Legacy Evidence Contracts

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/evidence-contracts.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## Legacy Method Record serialization

<!-- method-record-example:start -->
```yaml
record_id: ariadne:chat-response-audit:root:v1
schema_version: '2.0'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: diagnosis
object_contract:
  boundary: One support team's work-message intake and response workflow; other departments are outside the audited
    object.
  state_variables:
  - response-time metric under a frozen inclusion rule
  - message volume and mix
  - staffing and shift coverage
  - chat-tool use
  relations_or_transitions:
  - incoming message to first qualifying response
  - tool adoption precedes the observed post-period but its causal channel is unresolved
  interfaces:
  - customer-message intake
  - staff scheduling
  - chat notifications and routing
  time_window: eight weeks before and eight weeks after adoption
  scale_profile:
    aggregation: messages aggregated to team-week summaries
    space: one support team
    time: sixteen-week pre/post window
    organization: single team
    causal_level: candidate channel effect
    observation_resolution: message records and weekly summaries
    impact: team and its incoming customers
    network: message-routing network
    jurisdiction: 'not_applicable: no action authorization is evaluated in this evidence audit'
  identity_criterion: The same workflow while message definition, staffing unit, and response rule remain comparable.
  task_profile:
    target_query: Whether the chat tool caused the response-time decrease in this team
    horizon: The sixteen-week pre/post window
    environment: This team's staffing, message mix, and dashboard protocol
    allowed_operations: Observation and record review only
    error_tolerance: Direction of effect with stated alternatives; no effect-size estimate
  status: candidate
evidence_cutoff:
  as_of: '2026-08-04T00:00:00+08:00'
  included_source_ids:
  - source:team-dashboard-export
  - source:tool-rollout-log
  excluded_after_cutoff: true
scale_scope:
  source: message-level observations in one team
  target: claims about all departments
  transform_kind: scale
  transform_status: failed
claim_ledger:
- claim_id: D-response-time
  claim_type: D
  text: Response time requires a frozen message inclusion and first-response rule.
  status: candidate
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
- claim_id: E-observed-decrease
  claim_type: E
  text: The exported dashboard shows a lower weekly median response time after adoption under its current protocol.
  status: observed
  support_ids:
  - source:team-dashboard-export
  counterevidence_ids: []
  support_rule_ids: []
  depends_on:
  - D-response-time
- claim_id: G-tool-cause
  claim_type: G
  text: The chat tool caused the observed response-time decrease.
  status: unresolved
  support_ids:
  - E-observed-decrease
  counterevidence_ids:
  - alternative:staffing-workload-seasonality-measurement
  support_rule_ids: []
  depends_on:
  - D-response-time
  - E-observed-decrease
- claim_id: N-speed-priority
  claim_type: N
  text: Faster response should take priority over privacy, workload, and other outcomes.
  status: unresolved
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
- claim_id: O-universal-adoption
  claim_type: O
  text: Every department should adopt the tool.
  status: unresolved
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
  depends_on:
  - G-tool-cause
  - N-speed-priority
rule_registry: []
unknowns_and_counterevidence:
  unknowns:
  - 'unknown: frozen response-time definition and dashboard protocol stability'
  - 'unknown: complexity-matched baseline, comparison group, channel intervention, and independent replication'
  - 'unknown: department-specific feasibility, values, authorization, stopping, rollback, and remedy'
  counterevidence:
  - staffing, workload, seasonality, message mix, and metric changes remain live alternatives
conflicts: []
output_ceiling: description_only
ceiling_transition:
  operation: root
  inputs: []
  basis: []
  result: description_only
module_runs:
- module: ariadne-evidence
  status: completed
  input_records: []
  output_record:
    record_id: ariadne:chat-response-audit:root:v1
    record_version: 1
module_payloads: []
recommended_next_modules:
- ariadne-scale
- ariadne-mechanism
- ariadne-choice
- ariadne-audit
authorization_effect: none
```
<!-- method-record-example:end -->

## Method Record Update

## Method Record Update

- Keep the frozen object and task profile in `object_contract`; do not silently refine either after viewing evidence.
- List only included sources in `evidence_cutoff` and preserve the cutoff timestamp.
- Put each split D/G/E/H/N/O/F claim in `claim_ledger` with explicit support, counterevidence, and `depends_on` IDs.
- Put competitors, residuals, missing observations, invalid bridges, and protected opacity in `unknowns_and_counterevidence`.
- Set each claim's level by its weakest critical dependency, and the record ceiling by the claims the output actually rests on. A normal child applies the minimum of that ceiling and its parent. Raise only in a child that newly admits named external evidence or a newly fulfilled declared protocol; module completion never raises.
- Add `ariadne-evidence` to `module_runs`, route scale and representation questions to `ariadne-scale`, and keep `authorization_effect: none`.

## Legacy support-reference validation

For every `supported` Method Record claim, resolve each `support_id` to a source admitted by this record's cutoff or to an earlier claim ID in the same ledger, and each `support_rule_id` to a full entry in this record's `rule_registry`. A module name, heading, ghost source, or undeclared `RULE:*` string is not support. A ceiling raise additionally requires exact parent-record context and a named evidence or protocol basis absent from every parent.

## A downgrade is registered per proposition,

A downgrade is registered per proposition, with its dependencies and the impact of the missing item (§2.9, §13.1). Claims with independent grounds keep their level; a failed global source, shared premise, or object boundary blocks every related output. In the Method Record this is checked mechanically:

- every `depends_on` entry names a claim that appears earlier in the same ledger;
- a claim whose dependency is `contradicted`, `withdrawn`, or `retired` cannot be `supported`;
- a claim's own `ceiling`, when present, never exceeds the ceiling of any dependency or the record's `output_ceiling`.

The conclusion steps down from candidate hypothesis to question list to description only as critical variables, non-applicability handling, or core-channel visibility fail. Renaming a claim, splitting it, or moving it to another branch never restores its ceiling.
