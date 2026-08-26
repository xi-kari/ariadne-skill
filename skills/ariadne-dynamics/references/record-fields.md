# Method Record Field List

This module can be installed alone. The full machine-checkable schema ships with the suite router at `ariadne-skill/references/method-record.schema.json`; when that file is readable in your installation, validate against it (the router also ships `scripts/validate_record.py`). When this module runs standalone and the schema is not readable, produce a compact YAML record with exactly the twenty required fields below and add `schema_unavailable` to `unknowns_and_counterevidence.unknowns`; do not guess additional fields and do not claim the record was schema-validated.

## The twenty required fields

| Field | Constraint |
|---|---|
| `record_id` | `ariadne:<case>:<module\|merge\|root>:v<N>`; case slug without colons. |
| `schema_version` | The string `'1.2'`. |
| `record_version` | Integer: 1 for a root, parent + 1 for a linear child, highest parent + 1 for a merge. |
| `lineage_kind` | `root`, `linear`, or `merge`. |
| `parent_record_id` | Sole parent ID for `linear`; null for `root` and `merge`. |
| `parent_records` | Empty for a root; one `{record_id, record_version}` for linear; two or more, sorted by ID then version, for merge. |
| `request_type` | One of `explanation`, `diagnosis`, `dynamic_derivation`, `conditional_forecast`, `finite_choice`, `intervention_review`, `governance_review`. |
| `object_contract` | `boundary`, `state_variables`, `relations_or_transitions`, `interfaces`, `time_window`, `scale_profile`, `identity_criterion`, `status`. |
| `evidence_cutoff` | `as_of` (RFC 3339), `included_source_ids`, `excluded_after_cutoff`. |
| `scale_scope` | `source`, `target`, `transform_status`. |
| `claim_ledger` | Typed claims with `claim_id`, `claim_type`, `text`, `status`, `support_ids`, `support_rule_ids`, `counterevidence_ids`; may be empty. |
| `rule_registry` | Declared `RULE:*` entries; may be empty. |
| `unknowns_and_counterevidence` | Explicit `unknowns` and `counterevidence` lists. |
| `conflicts` | Named irreducible conflicts; empty array is valid and usual outside merges. |
| `output_ceiling` | `description_only`, `diagnostic_only`, or `requirements_only`. |
| `ceiling_transition` | `operation` (`root`/`preserve`/`lower`/`raise`/`meet`), `inputs`, `basis`, `result` equal to `output_ceiling`; `lower` adds a non-empty `reason`. |
| `module_runs` | Module, status, exact `input_records`, exact `output_record`; `not_run`/`not_applicable` add a `reason` and a null output. |
| `module_payloads` | Typed payloads only for completed human, dynamics, mechanism, forecast, choice, or audit runs. |
| `recommended_next_modules` | Only modules justified by remaining work. |
| `authorization_effect` | Always `none`. |
