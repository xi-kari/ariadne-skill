# Ariadne Method Record

## Contents

1. Purpose
2. Required fields
3. Version and lineage rules
4. Module handoff
5. Valid example
6. Human-facing presentation
7. Common mistakes

## Purpose

The Method Record makes Ariadne runs continuous, challengeable, and compatible across standalone, sequential, and clustered work. It is a reasoning record, not a reality database or authorization token.

The machine-checkable schema lives at repository root in `schemas/method-record.schema.json`. This reference defines its operational meaning.

## Required fields

| Field | Meaning |
|---|---|
| `record_id` | Stable Ariadne case/version identifier. |
| `schema_version` | Record schema version; start with `1.0`. |
| `record_version` | Monotonic integer within a lineage. |
| `parent_record_id` | Previous immutable record, or null for version 1. |
| `request_type` | One of the seven Lattice Kernel output classes. |
| `object_contract` | Boundary, state variables, relations/transitions, interfaces, time window, scale profile, identity criterion, status. |
| `evidence_cutoff` | Time and source IDs admitted to this version. |
| `scale_scope` | Source, target, and scale/translation audit status. |
| `claim_ledger` | Typed claims with status, support IDs, and counterevidence IDs. |
| `unknowns_and_counterevidence` | Explicit gaps and evidence against current candidates. |
| `output_ceiling` | `description_only`, `diagnostic_only`, or `requirements_only`. |
| `module_runs` | Module, run state, and record version. |
| `recommended_next_modules` | Only modules justified by remaining work. |
| `authorization_effect` | Always `none`. |

## Version and lineage rules

1. Create version 1 after initial framing, even when the object is incomplete.
2. Create a child version whenever evidence, module results, output ceiling, or external references change.
3. Use an explicit fork when the object, identity criterion, purpose, or materially relevant scale changes.
4. Preserve parent records. Correct by superseding, withdrawing, downgrading, or retiring; never erase.
5. An outcome arriving after a forecast appends evaluation to a child record and cannot alter the frozen forecast.
6. A child may lower its ceiling immediately. It may raise the ceiling only when the missing evidence or external record is identified in the new version.

## Module handoff

A module consumes the latest compatible record and produces:

- its added or changed fields;
- the parent and new version;
- sources it actually used;
- explicit unknowns and counterevidence;
- its module-run status;
- its supported ceiling;
- justified next modules.

Use these run states:

- `not_run`: dependency or availability prevented execution;
- `running`: active work, never a publishable result;
- `completed`: the module produced its bounded product;
- `failed`: the module ran but a required gate failed;
- `not_applicable`: responsibility has no legitimate counterpart, with reason.

`completed` means the procedure completed. It does not mean its empirical claim is true.

## Valid example

```yaml
record_id: ariadne:delivery-case:v1
schema_version: "1.0"
record_version: 1
parent_record_id: null
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
  as_of: 2026-08-04T00:00:00+08:00
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
unknowns_and_counterevidence:
  unknowns:
    - External dependency latency
  counterevidence: []
output_ceiling: diagnostic_only
module_runs:
  - module: ariadne-framing
    status: completed
    record_version: 1
recommended_next_modules:
  - ariadne-evidence
authorization_effect: none
```

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
| Raise a ceiling because more modules agreed | Require new evidence or a valid external record. |
| Treat a protected omission as absent data | Use `withheld_for_protection` in the explanatory record and lower confidence. |
