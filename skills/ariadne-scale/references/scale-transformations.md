# Scale, Circle, and Translation Contracts

Use this reference after freezing the candidate object and evidence cutoff. Keep scale definitions, operating procedures, and empirical claims separate: a complete mapping tells you how to test a transfer, not that the transfer is true.

## Three Transformation Kinds

| Kind | Question | Required output |
|---|---|---|
| Scale transformation | What changes between SP0 and SP1 for the same task? | Nine-axis comparison, operator, error, loss, and identity mapping |
| Circle-relation transformation | How do candidate circles become parallel, nested, overlapping, bridging, competitive, temporary, transformed, or dissolved? | Relation basis, channel, before/after snapshots, time, evidence, and K check |
| Representation or wording translation | How does a sourced payload enter a target task, vocabulary, or expression? | Lineage, converter, preserved and changed content, collapse, omission, additions, ambiguity, review, and return path |

Split simultaneous transformations into ordered atomic records. Align each step's target object and SP1 with the next step's source object and SP0. Do not let the final step erase an earlier failure or loss.

## Nine-Axis Scale Profile

Write `SP=<A,X,T,O,C,R,I,N,J>`. Use qualified identifiers such as `scale_axis:O` when claim type O could be confused with the organizational axis.

| Axis | Freeze | `expands` witness | Boundary |
|---|---|---|---|
| A aggregation | Units, member set, partition, aggregation rule, weights, exclusions | Target population covers source and target partition is a registered coarsening | Does not imply organization, space, influence, or authority |
| X spatial scope | Coordinate system, spatial set, boundary channels, outside links | Source is a strict subset after coordinate alignment | Proximity does not establish membership or causality |
| T temporal span | Time basis, window role, start/end, lag model | Target interval strictly contains source under the same basis and role | A snapshot and a trajectory are not substitutes |
| O organizational level | Versioned organization graph, nodes, containment edges, interfaces, overlap | Target node covers the source node's ancestor closure in the same graph version | Higher rank does not expand J |
| C causal level | Causal model, variables, edges, intervention semantics, abstraction map | A semantics-preserving map covers the source model and adds distinguishable levels | Labels, timing, and association are not causal bridges |
| R observation resolution | Protocol, distinguishable classes, parameters, error, protected omissions | Target preserves all source distinctions and adds at least one | Resolution is not completeness or permission |
| I influence scope | Outcomes, thresholds, windows, affected positions, effect order | Target affected-position set strictly contains source after alignment | Influence is not jurisdiction |
| N network-topology scope | Versioned graph, nodes, edges, semantics, sampling boundary | A semantics-preserving graph embedding covers the source graph | Centrality is not responsibility |
| J jurisdiction and authorization | Atomic tuples of source, subject, one object, one action, region, term, revocation, validity, and evidence | Target valid normalized tuple set strictly contains source, with independent proof for every new tuple | No other axis can substitute for J; never form object-action Cartesian products |

Record `not_applicable` rather than deleting an axis when the semantic domain truly lacks it. If both endpoints meet the same inapplicability rule, the relation can be `equal`; if only one does, use `incomparable`; if the material is insufficient, use `unknown`.

## Axis Comparison Contract

Assign one relation per axis:

- `equal`: normalized states occupy the same equivalence class;
- `expands`: the target is strictly greater under that axis's registered partial order;
- `contracts`: the inverse of a witnessed expansion;
- `incomparable`: both are known but neither validly orders the other;
- `unknown`: the comparison lacks a valid witness.

For every non-unknown relation, preserve comparator ID and version, verifier, evidence references, source and target summaries, actual set/interval/graph/mapping/authorization payload, verification artifact and hash, and valid status. Deep equality can witness identical normalized states; every nontrivial comparison needs the appropriate domain comparator.

Define equality through a shared normalizer or fixed bins, not arbitrary pairwise distance. Preserve reflexivity, antisymmetry, and transitivity only when intermediate states, versions, coordinates, graph semantics, mappings, variables, and authorization chains compose. If auxiliary fields such as interfaces, lags, errors, intervention semantics, or protected omissions conflict without a semantic map, use `incomparable` or `unknown` even when the main range is larger.

**External verification registry.** Every nontrivial axis relation must resolve against an external `comparator_results` registry entry that matches the axis, comparator ID and version, source and target summaries, relation, and verification hash. A record-internal `valid` flag, or an entry ID prefix that merely looks correct, is not a witness; without a resolvable entry, record `unknown`. When both endpoints normalize to the same state, a declared `expands` or `contracts` fails outright; record the failed comparison instead of rereading it as `equal` or parking it as `unknown`.

## Product-Order Classification

Classify in this exact order:

1. Any `incomparable` -> `horizontal_or_incomparable`.
2. Otherwise at least one `expands` and one `contracts` -> `mixed`.
3. Otherwise any `unknown` -> `unresolved`.
4. All `equal` -> `all_equal`.
5. Only `equal` or `expands`, with at least one expansion -> `elevation`.
6. Only `equal` or `contracts`, with at least one contraction -> `reduction`.

Use `SP0 <= SP1` only when every axis is equal or expands, and call it strict elevation only when at least one expands. A larger aggregation paired with lower observation resolution is `mixed`, even if another axis remains unknown. A horizontal analogy is usually incomparable, not elevation.

Build J only from valid atomic authorization tuples. Split multiple objects or actions into separate tuples. Self-assertion, actual control, seniority, observation coverage, influence, network centrality, or a valid but unrelated authorization never witnesses J expansion.

## Atomic Operator and Outcome Contract

For each atomic record:

1. Select one operator ID and one branch from that operator's branch registry.
2. Select one compatible claim mode: `descriptive_mapping`, `root_hypothesis`, `causal`, `object_conversion`, or `intervention_conversion`.
3. Freeze branch, mode, positive rule, threshold, and null rule before results.
4. Use one evaluated outcome:
   - `supported`: the selected bridge and positive rule pass;
   - `unsupported_or_undecided`: the bridge is inadequate or the positive rule fails without a complete null gate;
   - `null_supported`: frozen equivalence or sufficiency, power or sensitivity, and tolerance gates all pass.
5. Use `not_evaluated` only when the branch has not run.

Do not switch branch or mode after a disappointing result. “Not significant,” “looks unchanged,” “simple model performed similarly,” or “target evidence is missing” does not establish a null result. Non-description modes require resolvable eligible root instances; causal and object/intervention conversion modes also require a nonempty causal bridge.

## Operators M01-M09

| Operator | Semantic signature and minimum bridge | Typical loss and stop boundary |
|---|---|---|
| M01 aggregation | Map units to a total or partition; register members, exclusions, weights, missingness, alternative aggregation rules, and heterogeneity | Tails, order, covariance, local timing, and minority visibility; never allocate a total result back to each unit |
| M02 nesting | Map boundaries, members, overlap, exit, and interfaces for descriptive nesting; use a separate eligible G4 branch for cross-layer causal or conversion claims | Membership does not imply cross-layer effect, upper-level priority, lower-level duty, or J expansion |
| M03 network propagation | Register nodes, directed edges, weights, capacity, sampled boundary, candidate and alternative paths, delay, and loss | Missing weak or off-network edges and lost sequence; connectivity is not transmission, intent, responsibility, or permission |
| M04 temporal accumulation | Freeze time basis, baseline, windows, lags, persistence threshold, accumulation, decay, and recovery rules; compare trend, season, cohort, and alternate windows | Window sensitivity and hidden cohorts; basic longitudinal combination does not establish G3 path dependence |
| M05 institutionalization | Separate institutional fact, causal effect, object conversion, and intervention conversion; record durable changes to rules, roles, resources, records, decisions, or transitions | Existence is separate from legal validity, legitimacy, protection, and whether the institution should continue |
| M06 emergence | Compare source units and interaction rules with a preregistered simple additive model on the same target metric | A macro pattern does not identify a unique micro cause or downward causality; model parity needs the complete null gate |
| M07 delegation/representation | Separate representation claim, actual acts, delegation validity, and J transfer | Visibility, majority, influence, self-appointment, or actual control is not a valid delegation; only a verified J-transfer branch changes J |
| M08 compression/abstraction | Preserve source, algorithm, threshold, version, error, unrecoverable content, and task-required invariants | Do not collapse missing states into absence; high-loss representations cannot support high-impact action |
| M09 horizontal transfer | Register source-target map, differences, breaks, forbidden mappings, target responsibility chain, and J differences | Source evidence creates only target candidates; support and bounded null require independent target evidence |

## Unified Transformation Audit

Keep these fourteen sections in the detailed audit adjacent to the common Method Record. Do not add undeclared properties to the Method Record schema.

| Section | Minimum contents |
|---|---|
| identity | Contract ID, concept, version, proposition IDs, purpose |
| scale | SP0, SP1, nine axis differences, unchanged axes, classification, J authorization |
| objects | Source and target objects, K criteria and mapping, units, totals, boundaries, members, exclusions |
| semantics | Preserved core, allowed changes, lost elements, prohibited mappings |
| transformation | One operator, branch, mode, rules, causal bridge, lags, error, validity, root instance, subtype, criterion, thresholds, null gates, outcome |
| variables | Inputs, states, outputs, and cross-variable dependencies |
| evidence | Independent source and target evidence, coverage, heterogeneity, counterexamples, absent signals, alternatives, residuals, replication |
| loss | Compressed detail, unrecoverable information, low-visibility positions, local exclusions |
| responsibility | Actors, decision makers, authorizers, carriers, responsible subjects, beneficiaries, and cost bearers kept distinct |
| normative | Value premises, choice type, runtime N principles, authorization source, C12, and O1-O4 when action is later considered |
| protection | Applicability, low-power positions, safe submission, anti-retaliation |
| action | Judgment and action ceilings, prohibited acts, stop conditions, owner, and selected action if separately authorized |
| correction | Challenge, review, rollback, repair, and writeback |
| lifecycle | Validity, review point, pause, and retirement |

A descriptive scale audit normally fills normative and action sections with an explicit non-action boundary, not an invented authorization procedure.

Records created under an earlier audit layout remain readable. Mark a newer field that an older record never carried as an explicit legacy absence; do not backfill it silently with reconstructed content.

### Cross-scale proof heuristic

For a proposed bridge that claims more than a descriptive translation, carry all eight fields together: `source_object`, `target_object`, `limit_or_scale_law`, `initial_conditions`, `history_structure`, `error`, `valid_time`, and `failure_boundary`. Treat the result as a proof-discipline checklist under explicit conditions. Missing fields leave a candidate bridge or requirements for a test; they do not permit a strong transfer claim.

This heuristic does not prove that every scale transfer loses information. It does not import a kinetic equation or physical model into a social or psychological object. It does not identify task-relevant representation loss with physical entropy. Preserve those non-proof boundaries in every cross-domain handoff.

## Identity Mapping

Preserve `source_K`, `target_K`, the forward and reverse mappings, criteria preserved and violated, preregistration reference, evidence, verification artifact, and hash. Test source under source K, source under target K, target under source K, and target under target K with `passed`, `failed`, or `undetermined`.

| Classification | Minimum condition | Ceiling |
|---|---|---|
| `same_object` | Both directions valid and both objects pass both K checks | Identity only; no automatic semantic, causal, or normative preservation |
| `converted_object` | Each object passes its own K, target fails source K, and a frozen G4b object-conversion instance is supported | Only the predeclared conversion |
| `incomparable` | Each passes its own K and at least one cross-check fails with evidence | Known incompatibility, not “not evaluated” |
| `undetermined` | Mapping or criteria have not run, are unknown, or are unobservable | No identity or conversion claim |

Do not use a shared name as identity evidence. A supported object-conversion mode must align with `converted_object`; a bounded null aligns with `same_object`; an unrun test remains `undetermined`.

**External verification registry.** Every nontrivial preservation or conversion claim must hand its `mapping_id` to an independent `identity_mapping_results` registry and resolve there: object summaries, K summaries, both mapping directions, the four K-check outcomes, verification artifact, and hash, checked item by item. A record-internal self-reported `valid`, or a mapping ID prefix that merely looks correct, is not a witness; an entry that does not resolve leaves the classification `undetermined`.

## Circle Relations

Keep scale and circle relation contracts separate:

- **parallel:** no current inclusion relation under the stated basis;
- **nested:** one candidate circle is included under a named member or boundary basis;
- **overlapping:** list shared members or interfaces;
- **bridging:** identify an actual cross-circle carrier and transmission;
- **competitive:** show how one changes the other's feasible set or resource access;
- **temporary:** freeze formation and ending conditions.

Record source relation, target relation, basis, direction, channel, delay, threshold, window, evidence, counterevidence, and before/after snapshots. Recheck K on every relation change; when K fails, record object conversion or dissolution instead of preserving identity by renaming.

Preserve an actor's distinct role, visible information, responsibility, risk, and exit capacity in each circle. Do not aggregate one actor state and copy it into every membership. Use a shared environment node when circles have a common condition but no direct channel.

## Translation-Loss Audit

For representation or wording translation, register:

- source expression and context;
- target circle, task, and vocabulary;
- named converter or rule and version;
- content that must be preserved and changes that are allowed;
- source distinctions collapsed at the target;
- omissions and their reasons, keeping protected opacity distinct;
- interpretations or variables added by the translation;
- ambiguity, error, validity period, target-side review, and failure or withdrawal conditions;
- parent record and a return address for reopening the source contract.

If two source states that matter to the task become indistinguishable at the target, record task-relevant loss. Do not assume every nontrivial translation is lossy: an identity map, reversible code, or task-sufficient map can pass its declared loss test. Round-trip reconstruction is useful but insufficient if hidden source access masks target-side semantic loss.

Treat target effective variables as task-bound candidates with object, scale, window, measurement, simple baseline, error, failure, and retirement. They are not automatically real entities, root causes, universal variables, or authorization grounds. A target representation is not assumed dynamically closed; test excluded-variable conditional gain through G4 and return unexplained effects to memory, noise, lag, unresolved terms, or residual candidates without naming a new entity from its shape.

## Evidence, Protection, and Action Boundaries

Obtain independent, resolvable material for both source and target. Operator names, semantic signatures, complete fields, internal examples, and classifier outputs specify a method; they do not prove a transformation, mapping, target property, or null.

Keep carriers and responsible subjects separate. When the downstream use affects people or sentient subjects, scarce resources, rights, exposure risk, or real disposition, require low-power positions, safe submission, anti-retaliation, stopping, challenge, review, and rollback. A prior `not_applicable` protection state cannot be inherited when the use changes.

Any external action later requires explicit value premises, a structured option set including one no-action option, matching J tuples, C12, O1-O4, stopping, protection, review, rollback, and remedy. This module supplies none of those permissions; `authorization_effect` remains `none`.

## Method Record Update

- Preserve the candidate object in `object_contract`; create a child version if an endpoint or K changes.
- Keep the source-material cutoff in `evidence_cutoff`; put later target evidence in a child record.
- Summarize endpoints in `scale_scope.source` and `.target`; set `not_needed`, `candidate`, `incomplete`, `audited`, or `failed` honestly.
- Put transfer claims in `claim_ledger` and map supporting and contradicting record IDs.
- Put unknown axes, invalid witnesses, lost distinctions, prohibited mappings, alternatives, and residuals in `unknowns_and_counterevidence`.
- Use the narrowest justified output ceiling, add `ariadne-scale` to `module_runs`, and keep `authorization_effect: none`.

## Strong Example

Claim: “Company engagement is 82, so each employee is engaged.” The source is individual survey responses; the target is a company-level weighted mean.

The atomic operator is M01 aggregation in descriptive mode. A expands from units to the company total, O expands from employee positions to the company node, and R contracts because the target statistic loses individual distinctions. The profile change is `mixed`, not elevation. The weighted mean can be reproducible while the inference back to each employee remains prohibited. Preserve response distribution, missingness, subgroup and low-visibility positions, and protected omissions.

<!-- method-record-example:start -->
```yaml
record_id: ariadne:engagement-aggregation-audit-001
schema_version: '1.2'
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
    A: individual response units to company aggregate
    X: one named company
    T: one survey wave
    O: employee positions to company node
    C: descriptive only; no causal level claimed
    R: individual response resolution compressed to one mean
    I: published statistic may be read as applying company-wide
    N: survey collection and reporting network
    J: 'not_applicable: no action authorization is evaluated'
  identity_criterion: The same survey wave, inclusion rule, weighting rule, and response scale.
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
    record_id: ariadne:engagement-aggregation-audit-001
    record_version: 1
module_payloads: []
recommended_next_modules:
- ariadne-evidence
- ariadne-human
- ariadne-audit
authorization_effect: none
```
<!-- method-record-example:end -->

The bounded result is: 82 may be a reproducible company statistic under the frozen aggregation rule; it is not an individual score, proof of shared meaning, or authority to act on any employee.
