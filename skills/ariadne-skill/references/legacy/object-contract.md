# Legacy Object Contract

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/object-contract.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## Legacy Method Record serialization

<!-- method-record-example:start -->
```yaml
record_id: ariadne:school-reporting-frame:root:v1
schema_version: '2.0'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: intervention_review
object_contract:
  boundary: The incident-reporting workflow in three named district schools after the app change; excludes unreported
    events and the proposed camera system.
  state_variables:
  - reported incident count by school and week
  - reporting participation by role
  - report classification and duplicate rate
  - response time after a report
  relations_or_transitions:
  - app access and prompts may change report submission; causal status unknown
  - submitted reports enter review, classification, and response stages
  interfaces:
  - student, staff, and parent submission channels
  - school review and escalation channel
  time_window: 2025-08-01 through 2026-07-31, with the app-change date retained
  scale_profile:
    aggregation: individual reports to school-level summaries
    space: three named schools
    time: weekly observations across one school year
    organization: school workflows within one district
    causal_level: candidate reporting-channel effect only
    observation_resolution: report-level records plus weekly summaries
    impact: students, staff, parents, and school response units
    network: submission and escalation network
    jurisdiction: 'unknown: camera authorization and district jurisdiction not audited'
  identity_criterion: The same reporting workflow while submission, classification, and escalation rules remain materially
    unchanged.
  task_profile:
    target_query: Whether the rise in reports reflects more incidents, more reporting, or changed classification
    horizon: The 2025-26 school year
    environment: Current app, staffing, and escalation rules in the three schools
    allowed_operations: Observation and record review only; the camera proposal is not evaluated in this frame
    error_tolerance: Direction of change per school; no incident-rate estimate
  status: candidate
evidence_cutoff:
  as_of: '2026-08-04T00:00:00+08:00'
  included_source_ids:
  - source:user-request
  excluded_after_cutoff: true
scale_scope:
  source: report-level events
  target: school and district summaries
  transform_kind: scale
  transform_status: candidate
claim_ledger:
- claim_id: D1
  claim_type: D
  text: The current object is the reporting workflow, not all incidents and not the proposed camera intervention.
  status: candidate
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
- claim_id: Q1
  claim_type: G
  text: 'Candidate G2 question: the app change altered report submission through its prompts and access channel.'
  status: candidate
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
  depends_on:
  - D1
rule_registry: []
conflicts: []
unknowns_and_counterevidence:
  unknowns:
  - 'unknown: whether underlying incident occurrence changed'
  - 'unknown: reporting participation and duplicate-classification changes'
  - 'unknown: camera necessity, privacy effects, alternatives, jurisdiction, stopping, remedy, and appeal'
  - 'connection need: report counts to incident occurrence (identification breakpoint)'
  counterevidence: []
output_ceiling: description_only
ceiling_transition:
  operation: root
  inputs: []
  basis: []
  result: description_only
module_runs:
- module: ariadne-framing
  status: completed
  input_records: []
  output_record:
    record_id: ariadne:school-reporting-frame:root:v1
    record_version: 1
module_payloads: []
recommended_next_modules:
- ariadne-evidence
- ariadne-scale
- ariadne-human
- ariadne-choice
- ariadne-audit
authorization_effect: none
```
<!-- method-record-example:end -->

## Method Record Mapping

## Method Record Mapping

- Put the seven frozen object fields, the task profile, and status in `object_contract`.
- Put the material cutoff in `evidence_cutoff`; included material is not empirical evidence merely because it is listed.
- Summarize source and target positions and the anticipated transform kind in `scale_scope`; use `transform_kind: none` with `transform_status: not_needed` when no transformation is claimed.
- Put definitions and framed claims in `claim_ledger` with D/G/E/H/N/O/F types and `depends_on` where a claim rests on another.
- Put unresolved fields, connection needs, protection gaps, and strong-judgment gaps in `unknowns_and_counterevidence`.
- Add `ariadne-framing` to `module_runs` and route only applicable next modules.
- Use `output_ceiling: description_only` for standalone framing and `authorization_effect: none` in every run.
