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

Use the dependency order and the two-restarts-per-dependency budget defined in [routing.md](routing.md). Each module creates a linear child with one parent reference. Its module run copies that reference into `input_records` and names the child in `output_record`.

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

Audit merges after the lanes complete. Create `lineage_kind: merge`, set `parent_record_id: null`, list every sibling ID and version in `parent_records` sorted by ID then version, copy that list into the audit run's `input_records`, and name the merge record in `output_record`. Never select one sibling as a surrogate parent.

## Continuous execution

Treat a follow-up as one of four events:

| Event | Record action |
|---|---|
| New evidence within same object and purpose | Create child version from evidence onward. |
| Changed object, boundary, scale, identity, or purpose | Restart framing with a new lineage or explicit fork. |
| Outcome arrives for a forecast | Preserve forecast; append result and calibration writeback. |
| External choice or authorization arrives | Link its external identifier; keep Ariadne's authorization effect as none. |

Never rewrite the parent record to make a later result appear expected.

## Merge rules

1. Union compatible source IDs, unknowns, counterevidence, and module runs while retaining each run's exact input and output record references.
2. Preserve incompatible object contracts, scale mappings, causal explanations, and value premises as named entries in the record's `conflicts` field, each with a `conflict_id`, a `kind` (`object_contract`, `scale_mapping`, `causal_explanation`, or `value_premise`), the involved `record_refs`, and a description; never average them.
3. Prefer no conclusion over a false synthesis.
4. Apply the ceiling `meet`: `description_only < diagnostic_only < requirements_only`, so the result is the minimum ranked parent ceiling. A merge never raises.
5. Mark a missing required lane `not_run`, not `passed`.
6. Keep external authorization references outside empirical claim support.
7. Preserve lane provenance per conclusion: a merged claim may carry the optional `ceiling` annotation recording the ceiling of the lane it came from. The record-level `meet` still bounds every cross-lane or action-facing conclusion, but the human-facing answer may present each lane-local finding at its annotated lane ceiling instead of flattening all findings to the merged minimum.

## Stop rules

| Broken dependency | Stop at |
|---|---|
| Candidate object incomplete | Questions or `description_only` |
| Evidence chain cannot be traced | Material organization or candidate claim |
| Scale bridge fails | Source-scale statement only |
| Mechanisms not distinguishable | Parallel candidates |
| Dynamic inputs not frozen | Qualitative scenario outline |
| Forecast not pre-registered | Scenario, not forecast |
| Norms or affected positions missing | Options and requirements, not recommendation |
| Jurisdiction or authorization missing | External handoff, no execution |
| Appeal/rollback missing in L3 | Pause or downgrade |

## Worked route

Request: “Use three employee interviews to prove the whole company is culturally broken and replace managers.”

- Framing declares the interviews' team, time window, and intended organization-wide use; the company-wide object remains incomplete.
- Evidence separates interview sources, statements, observations, interpretations, and counterevidence.
- Scale audits the move from three individuals to team and company claims.
- Human identifies power, retaliation risk, privacy, missing positions, and role/responsibility distinctions.
- Mechanism compares manager behavior, workload, incentives, selection effects, and reporting-channel trust.
- Choice can compare investigation, reversible pilot, delay, protection, or inaction only after explicit values and jurisdiction.
- Audit blocks organization-wide personnel action while preserving a requirements-only path for independent review.

## Host orchestration mapping

When the runtime provides subagent, task, or parallel-tool primitives, map cluster lanes onto them instead of simulating parallel work inside one context. Give each lane worker only its module's SKILL.md, the frozen parent record, the shared raw materials, and its bounded responsibility; never the whole suite, a sibling's output, or a preferred answer. Run the merge in the coordinating context through `ariadne-audit`. When the host offers a plan or todo primitive, map the full-pass steps onto it so progress and restarts stay visible. Without such primitives, run the same lanes sequentially in dependency order; every record shape stays identical.

## Merge lineage example

Two regional lanes were framed independently as roots and then joined by an audit merge under a declared joint case slug. The parents come first. The merge preserves their scale-mapping disagreement as a named `conflicts` entry instead of averaging it, and the ceiling `meet` keeps `description_only`.

<!-- method-record-lineage-example:start -->
```yaml
- record_id: ariadne:retention-east:root:v1
  schema_version: '1.2'
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
    status: candidate
  evidence_cutoff:
    as_of: '2026-08-01T00:00:00+08:00'
    included_source_ids:
    - east-billing-export
    excluded_after_cutoff: true
  scale_scope:
    source: Account-level billing events
    target: East-region churn diagnosis
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
  schema_version: '1.2'
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
    status: candidate
  evidence_cutoff:
    as_of: '2026-08-01T00:00:00+08:00'
    included_source_ids:
    - west-billing-export
    excluded_after_cutoff: true
  scale_scope:
    source: Seat-level provisioning events
    target: West-region churn diagnosis
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
  schema_version: '1.2'
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
          IG3: {status: passed, finding: No affected position is judged; the merge only describes.}
          IG4: {status: passed, finding: No power asymmetry is engaged by a descriptive merge.}
          IG5: {status: passed, finding: 'The unit-mapping conflict is preserved, not reconciled.'}
          IG6: {status: passed, finding: No strong judgment is issued at description_only.}
          IG7: {status: passed, finding: Action ceiling stays description_only by meet of both parents.}
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
