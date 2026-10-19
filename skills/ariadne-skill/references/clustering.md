# Ariadne Clustering and Continuation

## Contents

1. Sequential execution
2. Clustered execution
3. Continuous execution
4. Merge rules
5. Stop rules
6. Worked route
7. Host orchestration mapping
8. Merge lineage example

Intake, depth selection, the module map, the routing algorithm, and the restart budget live in [routing.md](routing.md).

## Sequential execution

Use the dependency order and the two-restarts-per-dependency budget defined in [routing.md](routing.md). Each module creates a linear child with one parent reference. Its module run copies that reference into `input_records` and names the child in `output_record`. A later module inherits every unresolved unknown, loss, and residual from its parent; choosing one branch narrows the conditions but does not remove uncertainty that only new material could remove (source §11.9.2).

## Clustered execution

After framing and evidence are frozen, scale, mechanism, and human lanes may run independently. Parallel admission is machine-checkable: two lanes may run in parallel only when their parent references carry the same `{record_id, record_version}` and the parent's `evidence_cutoff` fields (`as_of`, `included_source_ids`, `excluded_after_cutoff`) are equal item by item. Give every worker:

- the same parent record;
- the same raw materials and cutoff;
- only its assigned responsibility;
- no preferred answer;
- the required Method Record fields.

Each sibling creates a child of the same frozen parent. Derive its record ID deterministically with the normative syntax `ariadne:<case>:<module>:v<N>` defined in the Method Record reference. Do not let one sibling consume another sibling's output.

Do not parallelize:

- forecast before eligible dynamic paths exist;
- choice before bounded conclusions and explicit normative premises exist;
- audit as a peer whose vote can be averaged with the analyzed modules.

Parallel lanes that read shared state are independent; lanes that would write the same object, compete for the same resource, or change one another's option set need an order or an explicit concurrency rule, never "both at once" (source §11.3.2). Audit merges after the lanes complete. Create `lineage_kind: merge`, set `parent_record_id: null`, list every sibling ID and version in `parent_records` sorted by ID then version, copy that list into the audit run's `input_records`, and name the merge record in `output_record`. Never select one sibling as a surrogate parent.

## Continuous execution

Treat a follow-up as one of five events:

| Event | Record action |
|---|---|
| New evidence within same object, task, and purpose | Create child version from evidence onward. |
| Changed object, boundary, task, scale, identity, affected positions, or purpose | Restart from the earliest affected module with a new lineage or explicit fork. |
| Outcome arrives for a forecast | Preserve the forecast; append result, calibration, and writeback in a child. |
| Real feedback arrives after a derivation or choice | First check its source and event identity; then compare the original path, the competing path, and the simple baseline, and classify the gap as a fact error, mechanism error, different actor choice, execution deviation, or external change. Only a changed state, parameter, mechanism range, or path counts as learning (source §11.13). |
| External choice or authorization arrives | Link its external identifier; keep Ariadne's authorization effect as none. |

Never rewrite the parent record to make a later result appear expected, and never re-describe an old task's failure as success under a target chosen afterward (source §6.3).

## Merge rules

1. Union compatible source IDs, unknowns, counterevidence, and module runs while retaining each run's exact input and output record references.
2. Preserve incompatible object contracts, scale mappings, causal explanations, and value premises as named entries in the record's `conflicts` field, each with a `conflict_id`, a `kind`, the involved `record_refs`, and a description; never average them. Say what each conflict is about: effect size, mechanism, contextual meaning, transfer range, or normative premise (source §4.8.4).
3. Prefer no conclusion over a false synthesis.
4. Apply the ceiling `meet`: `description_only < diagnostic_only < requirements_only`, so the result is the minimum ranked parent ceiling. A merge never raises.
5. Mark a missing required lane `not_run`, not `passed`.
6. Keep external authorization references outside empirical claim support.
7. Preserve lane provenance per conclusion: a merged claim keeps its own `ceiling` and its `depends_on` links. The record-level `meet` still bounds every cross-lane or action-facing conclusion, but the human-facing answer presents each lane-local finding at its own ceiling instead of flattening all findings to the merged minimum.
8. Count independence by what supports the claim: lanes that reanalyze the same data, cite the same original, or repeat the same source are one lineage, not several confirmations (source §2.7.2).

## Stop rules

Each stop applies to the propositions that depend on the broken item; independently supported findings continue at their own ceiling. A failure of the shared source, common premise, object boundary, or lawful use stops everything that depends on it.

| Broken dependency | Dependent propositions stop at |
|---|---|
| Candidate object or task incomplete | Questions or `description_only` |
| Evidence chain cannot be traced | Material organization or candidate claim |
| Scale, circle, or translation bridge fails | Source-side statement only; parallel descriptions |
| Mechanisms not distinguishable | Parallel candidates with discriminating observations |
| Cross-time route not identified | Cross-time description or mechanism candidate |
| Dynamic inputs not frozen | Qualitative scenario outline |
| Forecast not pre-registered | Scenario, not forecast |
| Norms, protection floor, or affected positions missing | Options, distribution, and requirements; the blocked recommendation pauses, independent evaluations remain |
| Jurisdiction or authorization missing | Analytic recommendation for deliberation at most; external handoff; no execution |
| Appeal, anti-retaliation, or rollback missing in L3 | Pause the strong judgment and its high-impact use |

## Worked route

Request: "Use three employee interviews to prove the whole company is culturally broken and replace managers."

- Framing names the difference to explain, declares the interviews' team, time window, task, and the intended organization-wide use; the company-wide object remains incomplete.
- Evidence separates interview sources, statements, observations, interpretations, and counterevidence, and counts the three interviews by their shared or independent lineage.
- Scale audits the move from three individuals to team and company claims and records what the aggregation would lose.
- Human identifies power, retaliation risk, privacy, missing positions, the CV/RS distinction, and role activation as a competitor to personality labels.
- Mechanism compares manager behavior, workload, incentives, selection effects, and reporting-channel trust, each with its temporal route.
- Choice compares independent investigation, reversible pilot, delay, protection, maintaining the status quo, and no action under explicit premises; it can give an analytic recommendation for deliberation (for example an independent, protected review first) with costs and change conditions, while replacing managers stays an external decision it cannot authorize.
- Audit classifies the personnel use as a strong judgment by use, blocks organization-wide personnel action while SJ1-SJ8 are incomplete, and keeps the requirements path for independent review.

## Host orchestration mapping

When the runtime provides subagent, task, or parallel-tool primitives, map cluster lanes onto them instead of simulating parallel work inside one context. Give each lane worker only its module's SKILL.md, the frozen parent record, the shared raw materials, and its bounded responsibility; never the whole suite, a sibling's output, or a preferred answer. Run the merge in the coordinating context through `ariadne-audit`. When the host offers a plan or todo primitive, map the full-pass steps onto it so progress and restarts stay visible. Without such primitives, run the same lanes sequentially in dependency order; every record shape stays identical. Feeding the same material to another model or regenerating a narrative is not a state update and adds no independent support (source §11.13, §13.11.1).

## Merge lineage example

Two regional lanes were framed independently as roots and then joined by an audit merge under a declared joint case slug. The parents come first. The merge preserves their scale-mapping disagreement as a named `conflicts` entry instead of averaging it, the ceiling `meet` keeps `description_only`, and IG6 is `not_applicable` with a stated reason because no strong-judgment use exists.

<!-- method-record-lineage-example:start -->
```yaml
- record_id: ariadne:retention-east:root:v1
  schema_version: '2.0'
  record_version: 1
  lineage_kind: root
  parent_record_id: null
  parent_records: []
  request_type: diagnosis
  object_contract:
    boundary: East-region customer accounts
    state_variables:
    - monthly_churn_rate
    relations_or_transitions:
    - renewal_decision
    interfaces:
    - billing_system
    time_window: 2026-H1
    scale_profile:
      aggregation: account
      time: month
    identity_criterion: Same paying account ID
    task_profile:
      target_query: Monthly churn level and its voluntary or involuntary split in the east region
      horizon: 2026-H1
      environment: Current billing system and pricing
      allowed_operations: Observation only
      error_tolerance: One percentage point on the monthly rate
    status: candidate
  evidence_cutoff:
    as_of: '2026-08-01T00:00:00+08:00'
    included_source_ids:
    - east-billing-export
    excluded_after_cutoff: true
  scale_scope:
    source: Account-level billing events
    target: East-region churn diagnosis
    transform_kind: scale
    transform_status: candidate
  claim_ledger: []
  rule_registry: []
  unknowns_and_counterevidence:
    unknowns:
    - Voluntary versus involuntary churn split
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
      record_id: ariadne:retention-east:root:v1
      record_version: 1
  module_payloads: []
  recommended_next_modules:
  - ariadne-evidence
  authorization_effect: none
- record_id: ariadne:retention-west:root:v1
  schema_version: '2.0'
  record_version: 1
  lineage_kind: root
  parent_record_id: null
  parent_records: []
  request_type: diagnosis
  object_contract:
    boundary: West-region customer accounts
    state_variables:
    - monthly_churn_rate
    relations_or_transitions:
    - renewal_decision
    interfaces:
    - billing_system
    time_window: 2026-H1
    scale_profile:
      aggregation: seat
      time: month
    identity_criterion: Same provisioned seat ID
    task_profile:
      target_query: Monthly churn level in the west region
      horizon: 2026-H1
      environment: Current provisioning system and pricing
      allowed_operations: Observation only
      error_tolerance: One percentage point on the monthly rate
    status: candidate
  evidence_cutoff:
    as_of: '2026-08-01T00:00:00+08:00'
    included_source_ids:
    - west-billing-export
    excluded_after_cutoff: true
  scale_scope:
    source: Seat-level provisioning events
    target: West-region churn diagnosis
    transform_kind: scale
    transform_status: candidate
  claim_ledger: []
  rule_registry: []
  unknowns_and_counterevidence:
    unknowns:
    - Seat-to-account consolidation rule
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
      record_id: ariadne:retention-west:root:v1
      record_version: 1
  module_payloads: []
  recommended_next_modules:
  - ariadne-evidence
  authorization_effect: none
- record_id: ariadne:retention-2026:merge:v2
  schema_version: '2.0'
  record_version: 2
  lineage_kind: merge
  parent_record_id: null
  parent_records:
  - record_id: ariadne:retention-east:root:v1
    record_version: 1
  - record_id: ariadne:retention-west:root:v1
    record_version: 1
  request_type: diagnosis
  object_contract:
    boundary: East and west region customer accounts
    state_variables:
    - monthly_churn_rate
    relations_or_transitions:
    - renewal_decision
    interfaces:
    - billing_system
    time_window: 2026-H1
    scale_profile:
      aggregation: mixed
      time: month
    identity_criterion: Region-local account or seat ID with no shared unit yet
    task_profile:
      target_query: Company-wide churn diagnosis across both regions
      horizon: 2026-H1
      environment: Two billing units with no registered mapping
      allowed_operations: Observation only
      error_tolerance: Not yet definable until a shared unit exists
    status: incomplete
  evidence_cutoff:
    as_of: '2026-08-01T00:00:00+08:00'
    included_source_ids:
    - east-billing-export
    - west-billing-export
    excluded_after_cutoff: true
  scale_scope:
    source: Region-level churn records
    target: Company-wide churn diagnosis
    transform_kind: composite
    transform_status: incomplete
  claim_ledger: []
  rule_registry: []
  unknowns_and_counterevidence:
    unknowns:
    - Voluntary versus involuntary churn split
    - Seat-to-account consolidation rule
    counterevidence: []
  conflicts:
  - conflict_id: conflict-unit-01
    kind: scale_mapping
    record_refs:
    - record_id: ariadne:retention-east:root:v1
      record_version: 1
    - record_id: ariadne:retention-west:root:v1
      record_version: 1
    description: East measures churn per paying account while west measures churn per provisioned seat; the two monthly rates lack a registered unit mapping and cannot be compared or summed until a scale audit supplies one.
  output_ceiling: description_only
  ceiling_transition:
    operation: meet
    inputs:
    - record_id: ariadne:retention-east:root:v1
      record_version: 1
      ceiling: description_only
    - record_id: ariadne:retention-west:root:v1
      record_version: 1
      ceiling: description_only
    basis: []
    result: description_only
  module_runs:
  - module: ariadne-audit
    status: completed
    input_records:
    - record_id: ariadne:retention-east:root:v1
      record_version: 1
    - record_id: ariadne:retention-west:root:v1
      record_version: 1
    output_record:
      record_id: ariadne:retention-2026:merge:v2
      record_version: 2
  module_payloads:
  - module: ariadne-audit
    payload:
      gate_register:
        transformations:
          IT1: {status: passed, finding: Both parents freeze their object contracts and billing-event observables.}
          IT2: {status: passed, finding: Each regional rate is traced to its own admitted export.}
          IT3: {status: passed, finding: No claim is promoted; both ledgers stay empty at merge.}
          IT4: {status: passed, finding: The meet keeps description_only and issues no requirements.}
        main_gates:
          IG1: {status: passed, finding: Region-local identity criteria are kept separate and declared.}
          IG2: {status: passed, finding: Both evidence cutoffs match and admit only regional exports.}
          IG3: {status: passed, finding: Account holders and seat holders are listed as affected; no position is judged by a descriptive merge.}
          IG4: {status: passed, finding: No adverse inference is drawn from missing churn reasons; silence stays unknown.}
          IG5: {status: passed, finding: Billing exports are not changed by this analysis; no publication is planned.}
          IG6: {status: not_applicable, finding: "No handling, eligibility, allocation, or reputational use is intended or foreseeable for a descriptive merge."}
          IG7: {status: passed, finding: Action ceiling stays description_only by meet of both parents.}
      strong_judgment:
        status: not_triggered
        reason: Descriptive merge with no handling, eligibility, allocation, reputational, or automated use.
        components:
          SJ1: {status: not_applicable, finding: Strong-judgment procedure not triggered.}
          SJ2: {status: not_applicable, finding: Strong-judgment procedure not triggered.}
          SJ3: {status: not_applicable, finding: Strong-judgment procedure not triggered.}
          SJ4: {status: not_applicable, finding: Strong-judgment procedure not triggered.}
          SJ5: {status: not_applicable, finding: Strong-judgment procedure not triggered.}
          SJ6: {status: not_applicable, finding: Strong-judgment procedure not triggered.}
          SJ7: {status: not_applicable, finding: Strong-judgment procedure not triggered.}
          SJ8: {status: not_applicable, finding: Strong-judgment procedure not triggered.}
      contestability:
        owner:
          contact: retention-review@example.invalid
          status: reachable
        deadline: '2026-09-01T00:00:00+08:00'
        original_record_retention: true
        downstream_correction_target: any churn summary derived from this merge record
        rollback_recovery_target: the two parent root records as the last verified state
        remedy: correct derived summaries and re-register the unit mapping before reuse
  recommended_next_modules:
  - ariadne-scale
  authorization_effect: none
```
<!-- method-record-lineage-example:end -->
