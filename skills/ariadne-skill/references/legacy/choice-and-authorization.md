# Legacy Choice And Authorization

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/choice-and-authorization.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## Legacy Method Record serialization

<!-- method-record-lineage-example:start -->
```yaml
- record_id: ariadne:team-choice:root:v1
  schema_version: '2.0'
  record_version: 1
  lineage_kind: root
  parent_record_id: null
  parent_records: []
  request_type: finite_choice
  object_contract:
    boundary: Work-allocation and appeal arrangements for the frozen 24-person product team; exclude employment termination
      and compensation changes.
    state_variables:
    - workload distribution
    - appeal access
    - departure notices
    relations_or_transitions:
    - candidate options under comparison
    interfaces:
    - protected participation
    - independent appeal
    - management authority
    time_window: Review now; any trial may last no more than eight weeks.
    scale_profile:
      aggregation: individual distribution within one team
    identity_criterion: A change to team, action, territory, or duration requires a new choice version.
    task_profile:
      target_query: Which option to put to the team for deliberation, and what blocks real adoption
      horizon: The next eight weeks
      environment: Current workload, appeal process, and management authority
      allowed_operations: Analysis and recommendation for deliberation; no execution
      error_tolerance: Ordinal comparison of options under the registered premises
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
    target: bounded team choice
    transform_kind: scale
    transform_status: candidate
  claim_ledger: []
  rule_registry: []
  unknowns_and_counterevidence:
    unknowns:
    - 'unknown: verified weekly hours per member'
    - 'unknown: normative premises of the deciding team'
    counterevidence: []
  conflicts: []
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
      record_id: ariadne:team-choice:root:v1
      record_version: 1
  module_payloads: []
  recommended_next_modules:
  - ariadne-evidence
  - ariadne-choice
  authorization_effect: none
- record_id: ariadne:team-choice:choice:v2
  schema_version: '2.0'
  record_version: 2
  lineage_kind: linear
  parent_record_id: ariadne:team-choice:root:v1
  parent_records:
  - record_id: ariadne:team-choice:root:v1
    record_version: 1
  request_type: finite_choice
  object_contract:
    boundary: Work-allocation and appeal arrangements for the frozen 24-person product team; exclude employment termination
      and compensation changes.
    state_variables:
    - workload distribution
    - appeal access
    - departure notices
    - transfer availability
    relations_or_transitions:
    - status quo
    - mandatory reorganization
    - delay
    - reversible trial
    - transfer
    - no action
    interfaces:
    - protected participation
    - independent appeal
    - management authority
    - execution monitor
    time_window: Review now; any trial may last no more than eight weeks.
    scale_profile:
      aggregation: individual distribution within one team
      impact: direct and household spillover
      jurisdiction: unverified team-level authority
    identity_criterion: A change to team, action, territory, or duration requires a new choice version.
    task_profile:
      target_query: Which option to put to the team for deliberation, and what blocks real adoption
      horizon: The next eight weeks
      environment: Current workload, appeal process, and management authority
      allowed_operations: Analysis and recommendation for deliberation; no execution
      error_tolerance: Ordinal comparison of options under the registered premises
    status: candidate
  evidence_cutoff:
    as_of: '2026-09-07T16:00:00+08:00'
    included_source_ids:
    - SRC-HR-HISTORY
    - SRC-HOURS-CUTOFF
    - SRC-APPEAL-CUTOFF
    - SRC-WORKLOAD-VERIFIED
    excluded_after_cutoff: true
  scale_scope:
    source: individual and team evidence
    target: bounded team choice
    transform_kind: scale
    transform_status: audited
  claim_ledger:
  - claim_id: E-workload-verified
    claim_type: E
    text: Verified weekly hours exceed the registered team norm for six of 24 members.
    status: supported
    support_ids:
    - SRC-WORKLOAD-VERIFIED
    counterevidence_ids: []
    support_rule_ids: []
  - claim_id: N2-protect
    claim_type: N
    text: The choice must not lower protection for low-power positions.
    status: supported
    support_ids: []
    counterevidence_ids: []
    support_rule_ids:
    - RULE:N2-protect
  - claim_id: N3-correctable
    claim_type: N
    text: Any high-impact result must remain appealable and reversible.
    status: supported
    support_ids: []
    counterevidence_ids: []
    support_rule_ids:
    - RULE:N3-correctable
  - claim_id: O-recommendation
    claim_type: O
    text: The eight-week reversible pilot is the current analytic recommendation for deliberation; it is not authorized
      for execution.
    status: candidate
    support_ids:
    - E-workload-verified
    counterevidence_ids: []
    support_rule_ids: []
    depends_on:
    - E-workload-verified
    - N2-protect
    - N3-correctable
  - claim_id: O-authority
    claim_type: O
    text: No selected action has a verified atomic J authorization.
    status: unresolved
    support_ids: []
    counterevidence_ids: []
    support_rule_ids: []
  rule_registry:
  - rule_id: RULE:N2-protect
    rule_type: normative
    text: Affected positions and the rights floor must be explicit and protection may not degrade.
  - rule_id: RULE:N3-correctable
    rule_type: normative
    text: High-impact results must keep reachable appeal, review, and rollback.
  - rule_id: RULE:premises-registered
    rule_type: protocol
    text: Normative premises, conflicts, affected positions, the option set with no action, and costs are registered
      before an analytic recommendation.
  unknowns_and_counterevidence:
    unknowns:
    - 'unknown: the independent appeal owner and full affected-position distribution are not verified'
    - 'unknown: atomic J authorization for any option'
    counterevidence:
    - Immediate reorganization may relieve overload sooner if P1 is right, but may create irreversible burden before
      protected participation occurs.
  conflicts: []
  output_ceiling: requirements_only
  ceiling_transition:
    operation: raise
    inputs:
    - record_id: ariadne:team-choice:root:v1
      record_version: 1
      ceiling: description_only
    basis:
    - basis_kind: external_evidence
      basis_id: SRC-WORKLOAD-VERIFIED
    - basis_kind: protocol_fulfillment
      basis_id: RULE:premises-registered
    result: requirements_only
  module_runs:
  - module: ariadne-choice
    status: completed
    input_records:
    - record_id: ariadne:team-choice:root:v1
      record_version: 1
    output_record:
      record_id: ariadne:team-choice:choice:v2
      record_version: 2
  module_payloads:
  - module: ariadne-choice
    payload:
      facts:
      - Verified workload records show six of 24 members over the registered norm
      - The attrition forecast gives P1 medium ordinal support without a calibrated probability
      values:
      - Do not lower protection for low-power positions
      - Keep any high-impact result appealable and reversible
      options:
      - option_id: OPT-STATUS
        kind: maintain_status_quo
        description: Continue current allocation with existing enforcement.
      - option_id: OPT-ACT
        kind: active_action
        description: Immediate team-wide mandatory reorganization.
      - option_id: OPT-DELAY
        kind: delayed_action
        description: Delay structural change while gathering protected evidence.
      - option_id: OPT-TRIAL
        kind: probing_action
        description: Eight-week workload and independent-appeal pilot with automatic expiry.
      - option_id: OPT-EXIT
        kind: exit_or_transfer
        description: Voluntary transfer with no retaliation or record penalty.
      - option_id: OPT-NONE
        kind: no_action
        description: No structural change; continue protection, observation, and a fixed reopening review.
      jurisdiction: unknown
      authorization: unknown
      stop_conditions:
      - Protection floor, appeal access, or rollback capacity fails
      - Verified weekly hours rise for three consecutive weeks
      rollback_plan: Restore the pre-trial work and record state; responsible owner remains external and unverified.
      analytic_recommendation:
        option_id: OPT-TRIAL
        normative_premise_ids:
        - N2-protect
        - N3-correctable
        reasons:
        - Narrowest reversible step that tests the workload mechanism behind P1
        - Keeps appeal independent of the reorganizing line manager
        costs:
        - Eight weeks of extra coordination load on the two most burdened members
        - Structural relief is delayed compared with immediate reorganization
        objections: Immediate reorganization would relieve overload sooner if the forecast is right.
        change_conditions:
        - Switch to OPT-ACT if verified weekly hours keep rising for three weeks
        - Switch to OPT-NONE if the independent appeal owner cannot be confirmed
        adoption_status: deliberation_only
  recommended_next_modules:
  - ariadne-audit
  authorization_effect: none
```
<!-- method-record-lineage-example:end -->

## Legacy choice payload

For every action request, populate the typed Method Record choice payload: `facts`, `values`, `options` (each with `option_id`, `kind`, and `description`, exactly one of kind `no_action`), `jurisdiction`, `authorization`, `stop_conditions`, `rollback_plan`, and `analytic_recommendation` (an object or explicit `null`). Use the literal state `unknown` inside any unresolved field rather than omitting it.

## Legacy analytic-recommendation encoding

In the Method Record, a non-null `analytic_recommendation` carries `option_id` (a registered option), `normative_premise_ids` (each resolving to an N claim in the ledger or a normative rule in the registry), `reasons`, `costs`, `objections`, `change_conditions`, and `adoption_status: deliberation_only`, and the record ceiling is `requirements_only`. In prose, open with the current analytic recommendation, then give the reasons for accepting and rejecting each option, costs, objections, and change conditions, and report the actual external adoption and authorization state. If authorization is absent, unverified or has not passed, state that execution is not yet authorized; if valid external authority exists, retain its scope and limits. The recommendation itself never supplies it. Never use imperative mood to dress a recommendation as an executable decision. An analyst's recommendation is not the actor's adoption.

## Legacy external-reference token validation

Verify external records through stable IDs and independent evidence. Write every external verification reference with four fields: `record_type`, the external record ID, the reported status, and an independent `verification_ref`. Keep every `record_id`, `verification_ref`, and procedure ID an external reference without leading or trailing whitespace. Treat `none`, `self`, `self:*`, `GHOST`, and their case or whitespace variants as invalid tokens, and treat self-reported status strings such as `selection:passed`, `C12:passed`, or `J:authorized` as equally invalid. The module links to and checks external records and keeps `authorization_effect: none`.

## Legacy execution-state encoding

Chain the `execution_state_log`: append state events in order, close each event with the previous event's hash and its own hash, and register the event count, head hash, and current state with an external anchor. Keep in every event the full choice as of that moment plus the `selected_action`, C12, unique J, and O1-O4 references. Terminal `rolled_back`, `completed`, `expired`, and `withdrawn` records never return to active; continuing requires new selection, authorization, and execution records. Keep the current execution state equal to the state of the complete 17-field choice record. A hash chain only checks linkage and byte changes of saved content; it cannot prove the log was not rewritten as a whole, that events happened, or that the anchor is independent.

## Finite-choice card

### Finite-choice card

```yaml
choice_id: CH-TEAM-022
selection_type: SEL-GOV
record_state: draft
O1:
  descriptive_claims: [E-workload-verified, FC-F-TEAM-017]
  evidence_ceiling: diagnostic_only
  uncertainty: The forecast has ordinal support and a small sample; no calibrated probability exists.
O2:
  premises:
    - {id: N2-protect, role: veto, interpretation: Do not lower protection for low-power team members.}
    - {id: N3-correctable, role: constraint, interpretation: Any high-impact result must be appealable and reversible.}
    - {id: N5-continuity, role: veto, interpretation: Organizational continuity does not justify avoidable rights harm.}
  unresolved_conflicts: [speed-versus-participation, workload-relief-versus-transfer-burden]
options:
  - {option_id: OPT-STATUS, kind: maintain_status_quo, summary: Continue current allocation with existing enforcement.}
  - {option_id: OPT-ACT, kind: active_action, summary: Immediate team-wide mandatory reorganization.}
  - {option_id: OPT-DELAY, kind: delayed_action, summary: Delay structural change while gathering protected evidence.}
  - {option_id: OPT-TRIAL, kind: probing_action, summary: Eight-week workload and independent-appeal pilot with automatic expiry.}
  - {option_id: OPT-EXIT, kind: exit_or_transfer, summary: Voluntary transfer with no retaliation or record penalty.}
  - {option_id: OPT-NONE, kind: no_action, summary: Do not change structure; continue protection, observation, and a fixed reopening review.}
analytic_recommendation:
  option: OPT-TRIAL
  status: deliberation_only
  reasons: Narrowest reversible step that tests the workload mechanism behind P1 while keeping appeal independent.
  costs: Eight weeks of coordination load on the two most burdened members; delayed structural relief.
  objections: Immediate reorganization would relieve overload sooner if the forecast is right.
  change_conditions: Switch to OPT-ACT if verified weekly hours keep rising for three weeks; to OPT-NONE if the independent appeal owner cannot be confirmed.
C12_status: incomplete
missing_for_execution: [verified protection floor, atomic J tuple, affected-position review, independent appeal owner]
authorization_effect: none
```
