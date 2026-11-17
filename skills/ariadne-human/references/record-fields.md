# Method Record Field List

This module can be installed alone. Use a plain-language answer for a light task unless a structured record is requested or needed for checking and continuation. The full machine-checkable schema ships with the suite router at `ariadne-skill/references/method-record.schema.json`; when that file is readable in your installation, validate any emitted record against it (the router also ships `scripts/validate_record.py`). If a record is needed while the schema is unreadable, use the twenty required fields below, add `schema_unavailable` to `unknowns_and_counterevidence.unknowns`, and retain only the documented payload fields. Do not guess additional fields or claim schema validation. Formal forecast registration remains required before outcomes.

## The twenty required fields

| Field | Constraint |
|---|---|
| `record_id` | `ariadne:<case>:<module\|merge\|root>:v<N>`; case slug without colons. |
| `schema_version` | Use the string `'2.1'` for new records. Existing `'2.0'` records remain readable under their original contract; do not silently rewrite them. |
| `record_version` | Integer: 1 for a root, parent + 1 for a linear child, highest parent + 1 for a merge. |
| `lineage_kind` | `root`, `linear`, or `merge`. |
| `parent_record_id` | Sole parent ID for `linear`; null for `root` and `merge`. |
| `parent_records` | Empty for a root; one `{record_id, record_version}` for linear; two or more, sorted by ID then version, for merge. |
| `request_type` | One of `explanation`, `diagnosis`, `dynamic_derivation`, `conditional_forecast`, `finite_choice`, `intervention_review`, `governance_review`, `synthesis_design`. |
| `object_contract` | `boundary`, `state_variables`, `relations_or_transitions`, `interfaces`, `time_window`, `scale_profile`, `identity_criterion`, `task_profile` (`target_query`, `horizon`, `environment`, `allowed_operations`, `error_tolerance`), `status`. |
| `evidence_cutoff` | `as_of` (RFC 3339), `included_source_ids`, `excluded_after_cutoff`. |
| `scale_scope` | `source`, `target`, `transform_kind` (`none` only with `transform_status: not_needed`), `transform_status`. |
| `claim_ledger` | Typed claims (D/G/E/H/N/O/F) with `claim_id`, `claim_type`, `text`, `status`, `support_ids`, `support_rule_ids`, `counterevidence_ids`, optional `depends_on` naming earlier claims and optional `ceiling`; may be empty. |
| `rule_registry` | Declared `RULE:*` entries; may be empty. |
| `unknowns_and_counterevidence` | Explicit `unknowns` and `counterevidence` lists. |
| `conflicts` | Named irreducible conflicts; empty array is valid and usual outside merges. |
| `output_ceiling` | `description_only`, `diagnostic_only`, or `requirements_only`. |
| `ceiling_transition` | `operation` (`root`/`preserve`/`lower`/`raise`/`meet`), `inputs`, `basis`, `result` equal to `output_ceiling`; `lower` adds a non-empty `reason`. |
| `module_runs` | Module, status, exact `input_records`, exact `output_record`; `not_run`/`not_applicable` add a `reason` and a null output. |
| `module_payloads` | Typed payloads only for completed human, dynamics, mechanism, forecast, choice, or audit runs. |
| `recommended_next_modules` | Only modules justified by remaining work. |
| `authorization_effect` | Always `none`. |

## Payload reminders

- A mechanism payload lists at least one complete candidate, each with `mechanism_id`, `temporal_route` (`current_state`, `carried_history`, `historical_increment`, or `not_applicable`), `channel_observation`, `discriminating_prediction`, `reverse_or_falsifier`, and `residual_comparison_rule`. In schema 2.1 a single candidate requires a `competition_search` object with non-empty `search_scope`, `reason_no_alternative`, and `failure_conditions`. Document a real search; do not invent a second candidate or promote the remaining candidate by default.
- A dynamics payload records each event's fact status (`observed`, `externally_reported`, `planned`, `hypothetical`, `simulated`, `unknown`), sources, window, observation time, affected actors and circles, channel, direct change, evidence state, disputes, competing explanations, reversibility, duration, and follow-up observations.
- A human payload records observation position, privacy state, allowed purpose, the four affected-position classes, reasonable `alternative_explanations`, and responsible human review. In schema 2.1 fewer than two alternatives requires the same complete `competition_search` object; an empty list explains the actual search limit rather than proving a unique interpretation.
- A claim whose `depends_on` includes a contradicted, withdrawn, or retired claim is never `supported`, and no claim ceiling exceeds its dependencies' ceilings or the record ceiling.

## Versioned optional records

Schema 2.1 adds optional top-level `problem_reopenings` and `design_candidates`; neither is one of the twenty required fields. Consult the router schema for their complete shapes before emitting them. A reopening retains the original question, proposer, reason, disposition and reasons, relationship to the new question, affected claim IDs, and preserved results. A design candidate retains its starting points, derivation, proposal, assumptions, checks, failure conditions and status; its `evidence_status` stays `candidate`, including after a design check. Design candidates belong only to `synthesis_design` records.

Schema 2.0 records do not admit these additions or `competition_search` and retain their original minimum of two mechanism candidates and two human alternatives. Continue an old record through an explicit child with schema 2.1 when these extensions are needed, preserving its original contents and results. A format migration supplies no new evidence or permission.
