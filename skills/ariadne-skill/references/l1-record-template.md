# L1 Record Template

The single copy-ready template for the L1 compact profile defined in [method-record.md](method-record.md). It keeps all twenty required top-level fields and passes the shipped schema and semantic checks as written; adapt the values, never the field set. `claim_ledger`, `rule_registry`, `conflicts`, and `module_payloads` may stay empty arrays; every other field stays explicit.

## Template

<!-- method-record-example:start -->
```yaml
record_id: ariadne:quick-check:root:v1
schema_version: '1.2'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: explanation
object_contract:
  boundary: One named team's weekly deploy pipeline
  state_variables:
  - weekly_deploy_count
  relations_or_transitions:
  - release_approval
  interfaces:
  - ci_system
  time_window: 2026-Q3
  scale_profile:
    aggregation: team
    time: week
  identity_criterion: Same repository set and release process
  status: candidate
evidence_cutoff:
  as_of: '2026-08-26T00:00:00+08:00'
  included_source_ids:
  - user-statement-01
  excluded_after_cutoff: true
scale_scope:
  source: One conversational statement
  target: Team deploy-frequency explanation
  transform_status: incomplete
claim_ledger: []
rule_registry: []
unknowns_and_counterevidence:
  unknowns:
  - Deploy counts per week before and after the change
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
    record_id: ariadne:quick-check:root:v1
    record_version: 1
module_payloads: []
recommended_next_modules:
- ariadne-evidence
authorization_effect: none
```
<!-- method-record-example:end -->

## Manual validation checklist

Prefer running the shipped validator: `python scripts/validate_record.py <record.yaml>` from this skill's directory (or `python scripts/validate_record.py --help` for parent-context options). When the runtime cannot execute code, check the emitted record by hand against this list instead of reading the JSON schema:

1. All twenty top-level fields above are present; none renamed, none added.
2. `record_id` matches `ariadne:<case>:<module|merge|root>:v<N>`; the case slug contains no colon.
3. `schema_version` is `'1.2'`; `record_version` is an integer.
4. Lineage is consistent: `root` has null `parent_record_id`, empty `parent_records`, version 1, ceiling `description_only`, operation `root`. `linear` has exactly one parent, version = parent version + 1. `merge` has two or more parents sorted by ID then version, version = highest parent version + 1, operation `meet`.
5. `object_contract` carries all eight subfields (`boundary`, `state_variables`, `relations_or_transitions`, `interfaces`, `time_window`, `scale_profile`, `identity_criterion`, `status`); `scale_profile` names at least one axis.
6. `evidence_cutoff.as_of` is an RFC 3339 datetime; every ID that supports a `supported` claim appears in `included_source_ids` or as an earlier claim.
7. `ceiling_transition.result` equals `output_ceiling`; `lower` carries a non-empty `reason`; `raise` lists only newly admitted basis IDs absent from every parent.
8. Exactly one completed module run names this record as its `output_record`; `not_run` and `not_applicable` runs carry a `reason` and a null `output_record`.
9. `authorization_effect` is `none`.

If neither the validator nor this checklist can be completed, say so in the answer and record `validation: not_run` in `unknowns_and_counterevidence.unknowns` instead of claiming the record was validated.
