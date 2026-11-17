# Legacy Scale Transformations

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/scale-transformations.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## Legacy Method Record serialization

<!-- method-record-example:start -->
```yaml
record_id: ariadne:engagement-aggregation-audit:root:v1
schema_version: '2.0'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: diagnosis
object_contract:
  boundary: Responses included in the named company's Q2 engagement survey and the published company-level statistic.
  state_variables:
  - individual response values
  - response and missingness indicators
  - registered aggregation weights
  - company-level weighted mean
  relations_or_transitions:
  - individual responses are mapped to one weighted company statistic by M01
  interfaces:
  - survey collection channel
  - aggregation and publication channel
  time_window: 2026 Q2 survey collection and publication window
  scale_profile:
    aggregation: individual response units to company aggregate
    space: one named company
    time: one survey wave
    organization: employee positions to company node
    causal_level: descriptive only; no causal level claimed
    observation_resolution: individual response resolution compressed to one mean
    impact: published statistic may be read as applying company-wide
    network: survey collection and reporting network
    jurisdiction: 'not_applicable: no action authorization is evaluated'
  identity_criterion: The same survey wave, inclusion rule, weighting rule, and response scale.
  task_profile:
    target_query: Whether the company mean of 82 can be read as each employee's engagement
    horizon: The 2026 Q2 survey wave
    environment: The registered inclusion and weighting rules
    allowed_operations: Description only
    error_tolerance: Exact reproduction of the published mean; no individual inference
  status: candidate
evidence_cutoff:
  as_of: '2026-08-04T00:00:00+08:00'
  included_source_ids:
  - source:q2-survey-export
  - source:q2-aggregation-specification
  excluded_after_cutoff: true
scale_scope:
  source: individual Q2 survey-response records
  target: company-level weighted mean of 82
  transform_kind: scale
  transform_status: audited
claim_ledger:
- claim_id: D-company-mean
  claim_type: D
  text: The value 82 is a company-level weighted aggregate under the registered rule.
  status: supported
  support_ids:
  - source:q2-survey-export
  - source:q2-aggregation-specification
  counterevidence_ids: []
  support_rule_ids: []
- claim_id: E-each-employee
  claim_type: E
  text: The company mean can be assigned back to every employee as their state.
  status: contradicted
  support_ids: []
  counterevidence_ids:
  - loss:individual-distribution-and-missingness
  support_rule_ids: []
  depends_on:
  - D-company-mean
rule_registry: []
conflicts: []
unknowns_and_counterevidence:
  unknowns:
  - 'withheld_for_protection: individual responses require a bounded trusted review path'
  - 'unknown: task-relevant subgroup distributions and nonresponse effects'
  counterevidence:
  - M01 preserves the registered weighted mean but loses individual and minority-position distinctions
output_ceiling: description_only
ceiling_transition:
  operation: root
  inputs: []
  basis: []
  result: description_only
module_runs:
- module: ariadne-scale
  status: completed
  input_records: []
  output_record:
    record_id: ariadne:engagement-aggregation-audit:root:v1
    record_version: 1
module_payloads: []
recommended_next_modules:
- ariadne-evidence
- ariadne-human
- ariadne-audit
authorization_effect: none
```
<!-- method-record-example:end -->

## Method Record Update

## Method Record Update

- Preserve the candidate object and task profile in `object_contract`; create a child version if an endpoint, K, or task changes.
- Keep the source-material cutoff in `evidence_cutoff`; put later target evidence in a child record.
- Summarize endpoints in `scale_scope.source` and `.target`; set `transform_kind` to the move made and `transform_status` to `not_needed`, `candidate`, `incomplete`, `audited`, or `failed` honestly; `none` pairs only with `not_needed`.
- Put transfer claims in `claim_ledger` with supporting and contradicting record IDs and `depends_on` for claims that rest on the mapping.
- Put unknown axes, invalid witnesses, lost distinctions, prohibited mappings, alternatives, residuals, and chain breakpoints in `unknowns_and_counterevidence`.
- Use the narrowest justified output ceiling, add `ariadne-scale` to `module_runs`, and keep `authorization_effect: none`.

## Legacy comparator registry encoding

**External verification registry.** Every nontrivial axis relation must resolve against an external `comparator_results` registry entry that matches the axis, comparator ID and version, source and target summaries, relation, and verification hash. A record-internal `valid` flag, or an entry ID prefix that merely looks correct, is not a witness; without a resolvable entry, record `unknown`. When both endpoints normalize to the same state, a declared `expands` or `contracts` fails outright; record the failed comparison instead of rereading it as `equal` or parking it as `unknown`.

## Legacy identity-mapping registry encoding

**External verification registry.** Every nontrivial preservation or conversion claim must hand its `mapping_id` to an independent `identity_mapping_results` registry and resolve there: object summaries, K summaries, both mapping directions, the four K-check outcomes, verification artifact, and hash, checked item by item. A record-internal self-reported `valid`, or a mapping ID prefix that merely looks correct, is not a witness; an entry that does not resolve leaves the classification `undetermined`.

## Legacy axis-verification fields

For every non-unknown relation, preserve comparator ID and version, verifier, evidence references, source and target summaries, actual set/interval/graph/mapping/authorization payload, verification artifact and hash, and valid status. Deep equality can witness identical normalized states; every nontrivial comparison needs the appropriate domain comparator.

## Legacy identity-verification fields

Preserve `source_K`, `target_K`, the forward and reverse mappings, criteria preserved and violated, preregistration reference, evidence, verification artifact, and hash. Test source under source K, source under target K, target under source K, and target under target K with `passed`, `failed`, or `undetermined`.
