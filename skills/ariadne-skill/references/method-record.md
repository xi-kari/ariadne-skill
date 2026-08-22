# Ariadne Method Record

## Contents

1. Purpose
2. Required fields
3. Record identifiers
4. Carrier and lifecycle
5. Lossless lineage
6. Output-ceiling algebra
7. Module handoff and typed payloads
8. L1 compact profile
9. Valid example
10. Lineage example
11. Human-facing presentation
12. Common mistakes

## Purpose

The Method Record makes Ariadne runs continuous, challengeable, and compatible across standalone, sequential, and clustered work. It is a reasoning record, not a reality database or authorization token.

The machine-checkable schema ships with this skill at `references/method-record.schema.json`. That file is byte-identical to the repository-root `schemas/method-record.schema.json` copy, and CI guards the equality. This reference defines its operational meaning.

## Required fields

| Field | Meaning |
|---|---|
| `record_id` | Stable Ariadne case/version identifier. |
| `schema_version` | Record schema version; use `1.2`. |
| `record_version` | Monotonic integer within a lineage. |
| `lineage_kind` | `root`, `linear`, or `merge`. |
| `parent_record_id` | Sole parent ID for a linear child; null for a root or merge. |
| `parent_records` | Complete canonical list of parent IDs and versions. |
| `request_type` | One of the seven Lattice Kernel output classes. |
| `object_contract` | Boundary, state variables, relations/transitions, interfaces, time window, scale profile, identity criterion, status. |
| `evidence_cutoff` | Time and source IDs admitted to this version. |
| `scale_scope` | Source, target, and scale/translation audit status. |
| `claim_ledger` | Typed claims with source support, declared rule support, and counterevidence IDs. |
| `rule_registry` | Explicit in-record inferential, protocol, normative, or operating rules addressable by `RULE:*` IDs. |
| `unknowns_and_counterevidence` | Explicit gaps and evidence against current candidates. |
| `conflicts` | Named irreducible conflicts (`object_contract`, `scale_mapping`, `causal_explanation`, or `value_premise`) with the involved record references; an empty array is valid and usual for root and linear records. |
| `output_ceiling` | `description_only`, `diagnostic_only`, or `requirements_only`. |
| `ceiling_transition` | Input ceilings, operation, admitted basis, result, and the downgrade reason when the operation is `lower`. |
| `module_runs` | Module, run state, exact input records, exact output record, and a `reason` when the state is `not_run` or `not_applicable`. |
| `module_payloads` | Typed human, dynamics, mechanism, forecast, choice, or audit handoff data. |
| `recommended_next_modules` | Only modules justified by remaining work. |
| `authorization_effect` | Always `none`. |

## Record identifiers

Give every new record an ID in the normative syntax:

`ariadne:<case>:<module|merge|root>:v<N>`

Derivation is deterministic so that independent workers produce the same ID without coordination:

- `<case>` is the stable case slug frozen at framing; every descendant record reuses it unchanged. A merge that joins separately framed cases declares one joint case slug in the merge record.
- The middle segment is `root` for a lineage root, the producing module's short name (`framing`, `evidence`, `scale`, `mechanism`, `human`, `dynamics`, `forecast`, `choice`, `audit`) for an ordinary child, and `merge` for an audit merge.
- `<N>` equals the record's `record_version`: 1 for a root, the parent version plus one for a linear child, the highest parent version plus one for a merge.

Example: the scale lane's child of `ariadne:churn-2026:root:v1` is `ariadne:churn-2026:scale:v2`, and the merge of the scale and mechanism siblings is `ariadne:churn-2026:merge:v3`. Old-style IDs that satisfy only the schema pattern `^ariadne:[A-Za-z0-9._:-]+$` (for example `ariadne:delivery-case:v1`) remain legal; do not rename historical records. Use the normative syntax for every new record.

## Carrier and lifecycle

A record that exists only in conversation scrollback cannot be located, continued, challenged, or written back. Give every record a carrier:

- **Standard directory.** In a project with a filesystem, write one file per record version at `.ariadne/records/<case>/<record_id>@v<version>.yaml`. Where the host filesystem forbids `:` in file names, substitute `+` for each `:` in the file name only; the `record_id` inside the file keeps its colons.
- **Parent references.** A handoff names a parent by record ID and carrier path together. The path is derivable from the ID (the case segment selects the directory; the ID plus version form the file name), and the consumer must check that the file's `record_id` and `record_version` match the reference before building on it.
- **Merge reads.** An audit merge reads every sibling record file for the frozen parent from the case directory, not a summary of them. `parent_records` and the audit run's `input_records` list exactly the sibling files read.
- **Correction lifecycle.** Correction never edits or deletes an existing record file. Supersede by writing the child version as a new file. Withdraw, downgrade, or retire by appending a child version that records the transition while the earlier files stay in place. Retain every version file while the case is open and for as long as any downstream record, registered forecast writeback, or open contest window references it; retire a case by archiving its directory as a whole, never by partial deletion.
- **No filesystem.** When the host offers no filesystem, embed the complete record as a fenced YAML block in the conversation every time it changes, and carry the latest embedded record forward verbatim into any continuing session. The parent reference then rests on `record_id` plus `record_version` alone, and a continuation must first re-quote the frozen parent record before extending it.

## Lossless lineage

Use these three forms only:

| Kind | `parent_record_id` | `parent_records` | Meaning |
|---|---|---|---|
| `root` | null | empty | Version 1 has no predecessor. |
| `linear` | the sole parent's ID | one `{record_id, record_version}` | The child version is exactly the parent version plus one. |
| `merge` | null | two or more complete parent references | The merge version is exactly the highest parent version plus one. |

For a merge, sort parents by `record_id` and then `record_version`. Put the same ordered list in the audit module run's `input_records`. For a linear child, use the sole parent reference in every current-output module input. Every completed module run identifies the current `output_record`; a missing or non-applicable run uses null. Reject an unresolved parent ID/version, self or future parent, extra input, dropped merge parent, broken edge, or unconnected record. This makes input and output records reconstructable without guessing from module order.

Create a new child whenever evidence, module results, purpose, object, identity, scale, or ceiling changes. Fork on a materially changed object or purpose. Correct by superseding, withdrawing, downgrading, or retiring; never erase. An outcome arriving after a forecast appends a child and cannot alter the frozen forecast.

Cluster workers consume the same frozen parent. Parallelism has a testable admission rule: two lanes may run in parallel only when their parent references carry the identical `{record_id, record_version}` pair and the parent's `evidence_cutoff` fields (`as_of`, `included_source_ids`, `excluded_after_cutoff`) are equal item by item. Audit retains all siblings as merge parents in canonical order. Sequential workers retain one parent at every step. The shapes differ, but each mode must resolve to the same frozen root sources, module-output responsibilities, facts, unknowns, ceiling, and `authorization_effect`.

## Output-ceiling algebra

The ceilings are nested and ordered:

`description_only < diagnostic_only < requirements_only`

| Ceiling | Includes | Excludes |
|---|---|---|
| `description_only` | Bounded material and observation description, candidate objects, questions, unknowns | Mechanism ranking, diagnosis, forecast, process requirements, action |
| `diagnostic_only` | Everything below plus competing mechanisms, bounded diagnosis, conditional paths and registered forecast evaluation | Normative or procedural requirements, recommendation, permission, execution |
| `requirements_only` | Everything below plus explicit facts/values/options/jurisdiction/authorization/protection/stop/rollback conditions for an external process | Selection by Ariadne, permission, execution, self-issued authorization |

Use these operations:

- `root`: start the lineage. A root record's `output_ceiling` and `ceiling_transition.result` are always `description_only`, and the operation has no inputs or basis. Admitted material never sets a higher initial value; a higher ceiling must be earned later through `raise`.
- `preserve`: return the input ceiling unchanged.
- `lower`: return a strictly lower ceiling when this child exposes a broken dependency, and record the downgrade reason in `ceiling_transition.reason`. A `lower` without a non-empty reason fails the semantic check.
- `raise`: return a strictly higher ceiling only in a child that newly admits external evidence or records a newly fulfilled protocol. List every new source or declared rule ID in `basis`. When the lineage was previously lowered, the raise must also state how its basis resolves the recorded `lower` reason; a basis that is new but unrelated to that reason does not qualify. A module's completion, agreement, simulation, or fuller prose is never a basis.
- `meet`: merge records by taking the minimum ranked input. It is valid only for a merge and never has a raise basis.

For an ordinary module child with requested local ceiling `c`, use `min(parent_ceiling, c)`. A module run alone never raises a ceiling. If new external evidence or protocol fulfillment arrives, create a child, register that new basis in `evidence_cutoff.included_source_ids` or `rule_registry`, and use `raise` only when the semantic validator can resolve the exact parent record and prove the basis absent from it. A clustered merge applies `meet` to every parent ceiling; repetition and votes have no effect.

## Module handoff

A module consumes the latest compatible record and produces:

- its added or changed fields;
- every parent ID and version and the new output ID and version;
- sources it actually used;
- explicit unknowns and counterevidence;
- named `conflicts` entries for any irreducible disagreement it exposes;
- its module-run status;
- its ceiling operation, input ceilings, basis, and result;
- any typed payload required by its domain;
- justified next modules.

Use these run states:

- `not_run`: dependency or availability prevented execution; give the cause in `reason` (a missing peer uses `module_unavailable`);
- `running`: active work, never a publishable result;
- `completed`: the module produced its bounded product;
- `failed`: the module ran but a required gate failed;
- `not_applicable`: responsibility has no legitimate counterpart; give the cause in `reason`.

The schema requires a non-empty `reason` whenever the state is `not_run` or `not_applicable`, and a null `output_record` for both.

`completed` means the procedure completed. It does not mean its empirical claim is true.

Put human observation position, privacy, purpose, all four structured affected-position classes (`direct`, `indirect`, `low_power`, `no_exit`), at least two alternatives, and responsible review in the `ariadne-human` payload. Put the complete event contract, including `planned` fact status, in the `ariadne-dynamics` payload. A forecast payload contains exactly one complete branch: preregistration linked to this record ID/version, or post-hoc reconstruction with calibration and failure classification. Put ordered IT/IG statuses and contestability in the audit payload. Do not overload the closed `evidence_cutoff` object.

A claim with `status: supported` must resolve each `support_id` to an admitted source or an earlier claim in this record and each `support_rule_id` to the explicit `rule_registry`. Module completion, an empty list, a heading, a ghost source, or an undeclared `RULE:*` label is not support.

## L1 compact profile

An L1 run (low impact, reversible, limited material) stays schema-valid while staying small:

- Keep all twenty required top-level fields. `claim_ledger`, `rule_registry`, `conflicts`, and `module_payloads` may remain empty arrays.
- Discharge a bounded module finding as a single-line declaration plus an explicit gap list: put the declaration in the claim ledger (or in `unknowns` when it is a gap), list what a full run would still check in `unknowns`, and do not fabricate a typed payload around it.
- `responsible_human_review.required` must be `true` only for L2/L3 human-domain work; an L1 lightweight observation may set it to `false`.
- Compactness is a size profile, not a ceiling raise: the record keeps `description_only` unless a recorded transition with an admitted basis says otherwise.

## Valid example

<!-- method-record-example:start -->
```yaml
record_id: ariadne:delivery-case:v1
schema_version: '1.2'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: diagnosis
object_contract:
  boundary: Product team A
  state_variables:
  - delivery_delay
  relations_or_transitions:
  - product_to_engineering_handoff
  interfaces:
  - product_engineering
  time_window: 2026-Q2
  scale_profile:
    aggregation: team
    time: quarter
  identity_criterion: Same mandate and membership rule
  status: candidate
evidence_cutoff:
  as_of: '2026-08-04T00:00:00+08:00'
  included_source_ids:
  - interview-01
  excluded_after_cutoff: true
scale_scope:
  source: Individual interview
  target: Team diagnosis
  transform_status: incomplete
claim_ledger:
- claim_id: claim-01
  claim_type: G
  text: Handoff delay may contribute to delivery delay.
  status: candidate
  support_ids:
  - interview-01
  counterevidence_ids: []
  support_rule_ids: []
rule_registry: []
unknowns_and_counterevidence:
  unknowns:
  - External dependency latency
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
    record_id: ariadne:delivery-case:v1
    record_version: 1
module_payloads: []
recommended_next_modules:
- ariadne-evidence
authorization_effect: none
```
<!-- method-record-example:end -->

## Lineage example

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

## Human-facing presentation

Do not dump the entire record by default. Present:

1. current bounded judgment;
2. strongest supporting observations;
3. competing explanations or paths;
4. important unknowns and reverse conditions;
5. output/action ceiling;
6. best next evidence or external decision step.

Expose the full record when another worker must continue it, a forecast will be scored, a high-impact judgment can be challenged, or a decision needs an audit trail.

## Common mistakes

| Mistake | Correction |
|---|---|
| Overwrite a record after new evidence | Create a child version and preserve the parent. |
| Store only conclusions | Store sources, counterevidence, unknowns, and module state. |
| Mark a procedural completion as claim support | Keep module state and claim status separate. |
| Put authorization in a claim support field | Link an external record; keep authorization effect none. |
| Drop sibling parents during a merge | Store every ID and version in canonical `parent_records` and audit inputs. |
| Average away sibling disagreements | Record them as named `conflicts` entries with kind, involved records, and description. |
| Raise a ceiling because more modules agreed | Preserve the parent ceiling; only a child with a newly admitted basis may use `raise`. |
| Keep the record only in chat scrollback | Write each version to `.ariadne/records/<case>/` and reference parents by ID and path. |
| Put privacy, purpose, event state, or model version in `evidence_cutoff` | Use the typed module payload. |
| Treat a protected omission as absent data | Use `withheld_for_protection` in the explanatory record and lower confidence. |
