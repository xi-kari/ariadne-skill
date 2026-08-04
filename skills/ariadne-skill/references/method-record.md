# Ariadne Method Record

## Contents

1. Purpose
2. Required fields
3. Lossless lineage
4. Output-ceiling algebra
5. Module handoff and typed payloads
6. Valid example
7. Human-facing presentation
8. Common mistakes

## Purpose

The Method Record makes Ariadne runs continuous, challengeable, and compatible across standalone, sequential, and clustered work. It is a reasoning record, not a reality database or authorization token.

The machine-checkable schema lives at repository root in `schemas/method-record.schema.json`. This reference defines its operational meaning.

## Required fields

| Field | Meaning |
|---|---|
| `record_id` | Stable Ariadne case/version identifier. |
| `schema_version` | Record schema version; use `1.1`. |
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
| `output_ceiling` | `description_only`, `diagnostic_only`, or `requirements_only`. |
| `ceiling_transition` | Input ceilings, operation, admitted basis, and result. |
| `module_runs` | Module, run state, exact input records, and exact output record. |
| `module_payloads` | Typed human, dynamics, mechanism, forecast, choice, or audit handoff data. |
| `recommended_next_modules` | Only modules justified by remaining work. |
| `authorization_effect` | Always `none`. |

## Lossless lineage

Use these three forms only:

| Kind | `parent_record_id` | `parent_records` | Meaning |
|---|---|---|---|
| `root` | null | empty | Version 1 has no predecessor. |
| `linear` | the sole parent's ID | one `{record_id, record_version}` | The child version is exactly the parent version plus one. |
| `merge` | null | two or more complete parent references | The merge version is exactly the highest parent version plus one. |

For a merge, sort parents by `record_id` and then `record_version`. Put the same ordered list in the audit module run's `input_records`. For a linear child, use the sole parent reference in every current-output module input. Every completed module run identifies the current `output_record`; a missing or non-applicable run uses null. Reject an unresolved parent ID/version, self or future parent, extra input, dropped merge parent, broken edge, or unconnected record. This makes input and output records reconstructable without guessing from module order.

Create a new child whenever evidence, module results, purpose, object, identity, scale, or ceiling changes. Fork on a materially changed object or purpose. Correct by superseding, withdrawing, downgrading, or retiring; never erase. An outcome arriving after a forecast appends a child and cannot alter the frozen forecast.

Cluster workers consume the same frozen parent. Audit retains all siblings as merge parents in canonical order. Sequential workers retain one parent at every step. The shapes differ, but each mode must resolve to the same frozen root sources, module-output responsibilities, facts, unknowns, ceiling, and `authorization_effect`.

## Output-ceiling algebra

The ceilings are nested and ordered:

`description_only < diagnostic_only < requirements_only`

| Ceiling | Includes | Excludes |
|---|---|---|
| `description_only` | Bounded material and observation description, candidate objects, questions, unknowns | Mechanism ranking, diagnosis, forecast, process requirements, action |
| `diagnostic_only` | Everything below plus competing mechanisms, bounded diagnosis, conditional paths and registered forecast evaluation | Normative or procedural requirements, recommendation, permission, execution |
| `requirements_only` | Everything below plus explicit facts/values/options/jurisdiction/authorization/protection/stop/rollback conditions for an external process | Selection by Ariadne, permission, execution, self-issued authorization |

Use these operations:

- `root`: set the initial ceiling from material admitted to the root; it has no inputs or basis.
- `preserve`: return the input ceiling unchanged.
- `lower`: return a strictly lower ceiling when this child exposes a broken dependency.
- `raise`: return a strictly higher ceiling only in a child that newly admits external evidence or records a newly fulfilled protocol. List every new source or declared rule ID in `basis`; a module's completion, agreement, simulation, or fuller prose is never a basis.
- `meet`: merge records by taking the minimum ranked input. It is valid only for a merge and never has a raise basis.

For an ordinary module child with requested local ceiling `c`, use `min(parent_ceiling, c)`. A module run alone never raises a ceiling. If new external evidence or protocol fulfillment arrives, create a child, register that new basis in `evidence_cutoff.included_source_ids` or `rule_registry`, and use `raise` only when the semantic validator can resolve the exact parent record and prove the basis absent from it. A clustered merge applies `meet` to every parent ceiling; repetition and votes have no effect.

## Module handoff

A module consumes the latest compatible record and produces:

- its added or changed fields;
- every parent ID and version and the new output ID and version;
- sources it actually used;
- explicit unknowns and counterevidence;
- its module-run status;
- its ceiling operation, input ceilings, basis, and result;
- any typed payload required by its domain;
- justified next modules.

Use these run states:

- `not_run`: dependency or availability prevented execution;
- `running`: active work, never a publishable result;
- `completed`: the module produced its bounded product;
- `failed`: the module ran but a required gate failed;
- `not_applicable`: responsibility has no legitimate counterpart, with reason.

`completed` means the procedure completed. It does not mean its empirical claim is true.

Put human observation position, privacy, purpose, all four structured affected-position classes (`direct`, `indirect`, `low_power`, `no_exit`), at least two alternatives, and responsible review in the `ariadne-human` payload. Put the complete event contract, including `planned` fact status, in the `ariadne-dynamics` payload. A forecast payload contains exactly one complete branch: preregistration linked to this record ID/version, or post-hoc reconstruction with calibration and failure classification. Put ordered IT/IG statuses and contestability in the audit payload. Do not overload the closed `evidence_cutoff` object.

A claim with `status: supported` must resolve each `support_id` to an admitted source or an earlier claim in this record and each `support_rule_id` to the explicit `rule_registry`. Module completion, an empty list, a heading, a ghost source, or an undeclared `RULE:*` label is not support.

## Valid example

<!-- method-record-example:start -->
```yaml
record_id: ariadne:delivery-case:v1
schema_version: '1.1'
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
| Raise a ceiling because more modules agreed | Preserve the parent ceiling; only a child with a newly admitted basis may use `raise`. |
| Put privacy, purpose, event state, or model version in `evidence_cutoff` | Use the typed module payload. |
| Treat a protected omission as absent data | Use `withheld_for_protection` in the explanatory record and lower confidence. |
