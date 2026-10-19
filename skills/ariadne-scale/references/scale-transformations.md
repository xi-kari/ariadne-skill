# Scale, Circle, and Translation Contracts

Use this reference after freezing the candidate object, task profile, and evidence cutoff. Keep scale definitions, operating procedures, and empirical claims separate: a complete mapping tells you how to test a transfer, not that the transfer is true. Section anchors (§) point to the source text named in `ariadne-skill/references/source-navigation.json`. Formal sufficiency, closure, and composition results (F1-F6) live in [representation-and-closure.md](representation-and-closure.md).

## Contract Roles and Qualified References

The nine axes are D-type definitions, the nine operators M01-M09 are O-type procedures, and U01-U11 are D-type primitive definitions (§5.1). Use qualified identifiers such as `scale_axis:O`, `scale_operator:M03`, and `universal_primitive:U07` wherever the organizational axis O could be confused with claim type O. Method gates use their formal IDs (CAUSAL, EVIDENCE, ANALOGY, SOURCE) and never become world causes.

## Three Transformation Kinds

| Kind | Question | Required output |
|---|---|---|
| Scale transformation | What changes between SP0 and SP1 for the same task? | Nine-axis comparison, operator, error, loss, and identity mapping |
| Circle-relation transformation | How do candidate circles become parallel, nested, overlapping, bridging, competitive, temporary, transformed, or dissolved? | Relation basis, channel, before/after snapshots, time, evidence, and K check |
| Representation or wording translation | How does a sourced payload enter a target task, vocabulary, or expression through a named converter or rule? | Lineage, converter, preserved and changed content, collapse, omission, additions, ambiguity, review, and return path |

The three can happen at once but are split into ordered atomic records (§5.10.1). A translation may call propagation, compression, or horizontal transfer operators, each judged by its own inputs, outputs, criteria, and failure conditions. Do not add an operator because a process has a new name, and do not merge several operation failures into one overall status. Align each step's target object and SP1 with the next step's source object and SP0, and never let the final step erase an earlier failure or loss. Record the kind in `scale_scope.transform_kind` (`scale`, `circle_relation`, `representation_translation`, or `composite` for an ordered chain; `none` only when no transformation is claimed).

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

Record a `not_applicable` object with its reason rather than deleting an axis when the semantic domain truly lacks it; J not applying to a natural process is not an empty authorization set. If both endpoints meet the same inapplicability rule, the relation can be `equal`; if only one does, use `incomparable`; if the material is insufficient, use `unknown`.

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

A purely descriptive branch may mark G-specific fields `not_applicable` with a reason, and a descriptive bridge that has run and holds may be `supported`; only G, causal, object-conversion, and intervention-conversion branches require a root instance, a preselected subtype, and one success criterion. When registering `supported` or `null_supported` for those branches, resolve the root-instance registry for instance ID, family, contract version, subtype, criterion, and state. Do not switch branch or mode after a disappointing result, and never rescue one mode with another. “Not significant,” “looks unchanged,” “simple model performed similarly,” or “target evidence is missing” does not establish a null result. Non-description modes require resolvable eligible root instances; causal and object/intervention conversion modes also require a nonempty causal bridge.

## Operators M01-M09

Each operator has its own semantic signature (§5.5). The names, numbers, signatures, and classification outputs are method; they never constitute empirical support (§5.9).

| Operator | Semantic signature and minimum bridge | Typical loss and stop boundary |
|---|---|---|
| M01 aggregation | Map units to a total or partition; register members, exclusions, weights, missingness, alternative aggregation rules, and heterogeneity. Fix the estimand first: average improvement among current residents and improvement for the same pre-event cohort are different targets; out-migrants, the deceased, those unable to attend, and non-applicants never silently become zero need. Where needed, report a fixed cohort, a current cross-section, entrants, and leavers side by side; crude and standardized rates can both be correct | Tails, order, covariance, local timing, and minority visibility; fails when the total cannot be reproduced, an alternative rule reverses direction, or a total association is written back as an individual property; never act on members from a total result |
| M02 nesting | Choose one branch: `descriptive_nesting`, `cross_layer_causal`, `object_conversion`, or `intervention_conversion`. Descriptive nesting checks boundaries, members, overlap, exit, and interface mappings and can hold with no cross-layer causation. Cross-layer causation needs a named channel, proportionate comparison, timing, G2 with CAUSAL, and D3/E5; a positive G4 is not necessary for every cross-layer effect, and the absence of a conditional increment is not the absence of cross-layer action | Membership does not imply upper-level priority, lower-level duty, or J expansion; descriptive-branch material never supports the other three branches |
| M03 network propagation | Register nodes, directed edges, weights, capacity, sampled boundary, candidate and alternative paths, delay, and loss. Observe tie strength, bridge position, centrality, and mobilizable resources separately; network position helps find a channel, while channel capacity, cost, substitutability, and arrival time decide whether it is usable | Missing weak or off-network edges and lost sequence; end-point effects cannot recover propagation order; connectivity or synchrony only yields candidates; four contacts may share one message source, so multiple social support is not independent fact sources; centrality is not intent, responsibility, or permission; "unchanged after cutting" without a passed null gate stays `unsupported_or_undecided` |
| M04 temporal accumulation | Freeze time basis, baseline, windows, lags, persistence threshold, accumulation, decay, and recovery rules; compare common trend, season, cohort, and alternate windows | Window sensitivity and hidden cohorts; longitudinal combination does not establish G3; no "no accumulation" claim without a null gate |
| M05 institutionalization | Choose one branch: `institutional_fact`, `institutional_causal_effect`, `institutional_object_conversion`, or `institutional_intervention_conversion`; record durable changes to rules, roles, resources, records, decisions, or transitions. Keep five judgments apart: the institution exists in fact, is legally valid, is normatively legitimate, provides protection, and should continue | Invalid authorization, thin participation, failed protection, or missing appeal, anti-retaliation, or rollback are governance failures and downgrade reasons that never erase the fact that the institution exists; existence never proves legality, legitimacy, adequate protection, or that it should continue |
| M06 emergence | Compare source units and interaction rules with a preregistered simple additive model on the same target metric | Additive parity supports "additive is enough" only through a passed null gate; a macro pattern does not identify a unique micro cause or prove downward causation, which needs a named channel, causal evidence, and D3/E5 |
| M07 delegation/representation | Choose one branch: `representation_claim`, `actual_acts`, `delegation_validity`, or `J_transfer` | Only `J_transfer` can change J; acts performed without authorization are still recorded with their effects and responsibility; invalid authorization triggers stop or downgrade without deleting acts that happened; majority, visibility, influence, self-appointment, or actual control is not a valid delegation |
| M08 compression/abstraction | Preserve source, algorithm, threshold, version, error, unrecoverable content, and task-required invariants. Task sufficiency is F1; the minimum worst-case recovery error is half the largest target amplitude within a fiber, and a decoder within tolerance epsilon exists exactly when every fiber's amplitude is at most 2*epsilon; successive compressions keep the final query only under F4 | Keep the four missing states distinct, never collapsing them into absence; a representation with material task-relevant loss for a proposed high-impact action cannot support that action |
| M09 horizontal transfer | Register source-target map, differences, breaks, forbidden mappings, target responsibility chain, and J differences | Source evidence creates only target candidates; `supported` and `null_supported` need independent target instances; missing target evidence is `not_evaluated` or `unsupported_or_undecided`, not proof the mechanism is absent; analogy never grants target-domain action authority |

### Primitive Scale Boundaries

Basic feedback (U07) does not require G3; learning needs a carrier route, and only a historical increment needs G3. An instant load gap (U09) does not require G3. U10 registers candidate traces without presupposing path dependence. A basic phase (U11) requires neither G3 nor G4. U01 does not guarantee G1, U05 relations do not prove causation, and U06 channel fields do not prove a channel effect (§5.6).

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

### Chain-Level Evaluation

In a record chain, each step has a unique contract ID and one operator, adjacent object references are K-compatible, and each SP1 equals the next SP0. An unresolved, failed, or over-tolerance step stays visible at chain level and is never covered by a final success (§5.7). Evaluate the chain as a whole: does the final task match the stepwise tasks, and has a shared resource been promised twice (two tasks each feasible with one unit of capacity cannot both finish when they share one unit in the same period)? Representation sufficiency, joint causal response, and joint resource feasibility each have their own criterion and never substitute for one another; see [representation-and-closure.md](representation-and-closure.md) for the three composition boundaries and for the mathematical scale-bridge discipline that governs any bridge claiming more than a descriptive translation.

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

Keep scale and circle relation contracts separate (§5.10):

- **parallel:** no current inclusion relation under the stated basis;
- **nested:** one candidate circle is included under a named member or boundary basis;
- **overlapping:** list shared members or interfaces;
- **bridging:** identify an actual cross-circle carrier and transmission;
- **competitive:** show how one changes the other's feasible set or resource access;
- **temporary:** freeze formation and ending conditions.

`transformed` is only the result of a relation update. Record source relation, target relation, basis, direction, channel, delay, threshold, window, evidence, counterevidence, and before/after snapshots. Recheck K on every relation change; when K fails, record object conversion or dissolution instead of preserving identity by renaming.

| Question | Contract | Boundary |
|---|---|---|
| Can an individual represent the team? | M01 plus distribution-loss audit | Belonging is not representing |
| Is the team contained in the organization? | M02 plus containment basis | A shared superior is not member containment |
| Two circles correlate through shared members | Overlap relation plus member mapping plus common environment | Overlap does not by itself create effective feedback |
| Did a bridging person change the other circle? | M03 plus channel plus counterfactual | Contact is not transmission; transmission is not representation |
| Did a temporary group become a lasting object? | K plus longitudinal material plus M05; grouping gain through G1; historical residual through G3 | A trace is not institutionalization |

Preserve an actor's distinct role, visible information, responsibility, risk, and exit capacity in each circle. Do not aggregate one actor state and copy it into every membership; start from local states and register aggregation loss at each step along membership or interface channels. **Translation has a task and a standing:** rendering correctly, helping parties understand each other, being permitted to publish the original words, and signing on someone's behalf are four different abilities or qualifications. Keep the bounded translation that succeeds while stating which meanings and rights were not transferred.

### Parallel and Nested Relations Together

Represent them as a directed multigraph: each node keeps its own object contract and each edge its own relation contract (§5.11). "Upper level" names only a specific containment, jurisdiction, or aggregation relation, never a truer, more correct, or more authorized position. When circles share an environment but no direct channel, keep a common-condition node instead of inventing a direct edge. A channel open only during an event window carries start and end times; relations in opposite directions get separate edges.

## Translation-Loss Audit

For representation or wording translation, register (§3.4.1, §5.10.2):

- source expression and context;
- target circle, task, and vocabulary;
- named converter, bridging person, or rule and version;
- content that must be preserved and changes that are allowed;
- source distinctions collapsed at the target;
- omissions and their reasons, keeping protected opacity distinct;
- interpretations or variables added by the translation;
- ambiguity, error, validity period, target-side review, and failure or withdrawal conditions;
- parent record and a return address for reopening the source contract.

Without independent target-side review, register only a translation awaiting test. Whether a translation actually changed the target's understanding or action needs channel material of its own; whether folded differences still carry conditional increments, or whether order matters, is tested by closure contracts.

The rule is "never presume lossless", not "always lossy". If two source states the task distinguishes become indistinguishable at the target, record task-relevant loss; an identity map, reversible code, or task-sufficient map can pass its declared loss test. Audit each item with its own trap: preserved (a kept title is not kept meaning), changed (an allowed change is not license to alter meaning), collapsed (a collapsed difference did not cease to exist), omitted (protected non-disclosure is not nonexistence), added (an added variable is not a discovered real entity), and returned (a return reopens review; it never patches the earlier run). Round-trip reconstruction is useful but insufficient, because hidden access to source records can fake a round trip and a one-way summary may suffice for the task. Review returns to the predeclared preserved items, loss tolerance, and target-side result.

**Representation keeping a distinction and a rule using it correctly are two judgments.** A handling error alone does not prove translation loss; when the difference is still distinguishable but misused, file the gap at the rule or execution step; both failures can coexist. If target answers are not unique within one fiber, the representation is proven insufficient (no deterministic rule can be right everywhere); if the fiber's answer is unique and the rule still answers wrong, that is sufficient witness of an independent rule error (F4 in [representation-and-closure.md](representation-and-closure.md)). An original being publicly consultable does not mean the executor had that distinction at the time; check existence, timely access, and actual use separately.

### Effective Variables, Closure, and Residual Return

Effective variables are candidates proposed at the target scale or task to compress state and improve a declared explanation, forecast, or option comparison (§5.10.3). Bind each to object, scale, window, task, measurement, simple baseline, error, failure, and retirement; effective does not mean real entity, root cause, universal variable, or authorization ground. A target representation is not presumed dynamically closed: check static sufficiency first (F1, F4), formal dynamics through F2, and the real mapping with separate evidence. Descriptive mappings may mark G-specific fields `not_applicable` with a reason; only a claim for formal empirical support enters G4. Do not invent a scale change to fill a format, and "not significant" is not closure. When an increment appears, register it as memory, noise, lag, unresolved term, or residual candidate, never naming a new entity from its shape.

## Evidence, Protection, and Action Boundaries

Obtain independent, resolvable material for both source and target. Operator names, semantic signatures, complete fields, internal examples, classifier outputs, and algorithm self-reports specify a method; they never enter source or target evidence and do not prove a transformation, mapping, target property, or null (§5.9). Machine validation checks fields, references, versions, outcome consistency, and axis composition; it does not replace a domain comparator (§5.8).

Keep `carrying_vehicles` and `responsible_subjects` in separate columns. Register `protection.applicability` explicitly with object type, downstream use, reason, and evidence; never infer it from an empty list. For a non-human object whose use is description only, or with evidence that use does not affect people or sentient subjects, safe submission and anti-retaliation may be `not_applicable` with a reason; energy, material, or computing resources of a natural system do not by themselves trigger human protection contracts. A real experiment or engineering intervention still states its J, action owner, stop, review, and rollback; only purely descriptive use lets J be `not_applicable`. When the object is human, sentient non-human, mixed, or unknown, or the use touches evaluation of people, scarce-resource allocation, rights, exposure risk, or real disposition, the protection fields become mandatory at once: identify low-power positions and local exclusion zones and provide safe submission, anti-retaliation, stop, appeal, review, and rollback. A prior `not_applicable` is never inherited when the use changes, and protection not applying never makes an action legitimate. When protection is insufficient, judgment and action ceilings fall together.

Any external action later links a selection record that publishes value premises and runtime normative principles, offers structured alternatives with stable option IDs and exactly one `no_action` option, resolves the selected option to the external action field by field, and is covered by at least one currently valid, independently reviewed atomic J tuple matching subject, object, action, region, and term, plus C12, O1-O4, action owner, prohibited acts, stop, protection, appeal, review, and rollback. With any item missing, the action ceiling is no action or continued deliberation. An action owner never implies intervention conversion. This module supplies none of those permissions; `authorization_effect` remains `none`.

## Method Record Update

- Preserve the candidate object and task profile in `object_contract`; create a child version if an endpoint, K, or task changes.
- Keep the source-material cutoff in `evidence_cutoff`; put later target evidence in a child record.
- Summarize endpoints in `scale_scope.source` and `.target`; set `transform_kind` to the move made and `transform_status` to `not_needed`, `candidate`, `incomplete`, `audited`, or `failed` honestly; `none` pairs only with `not_needed`.
- Put transfer claims in `claim_ledger` with supporting and contradicting record IDs and `depends_on` for claims that rest on the mapping.
- Put unknown axes, invalid witnesses, lost distinctions, prohibited mappings, alternatives, residuals, and chain breakpoints in `unknowns_and_counterevidence`.
- Use the narrowest justified output ceiling, add `ariadne-scale` to `module_runs`, and keep `authorization_effect: none`.

## Strong Example

Claim: "Company engagement is 82, so each employee is engaged." The source is individual survey responses; the target is a company-level weighted mean.

The atomic operator is M01 aggregation in descriptive mode. A expands from units to the company total, O expands from employee positions to the company node, and R contracts because the target statistic loses individual distinctions. The profile change is `mixed`, not elevation. The weighted mean can be reproducible while the inference back to each employee remains prohibited. Preserve response distribution, missingness, subgroup and low-visibility positions, and protected omissions. The contradicted back-assignment depends on the supported aggregate, yet the aggregate keeps its own standing.

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

The bounded result is: 82 may be a reproducible company statistic under the frozen aggregation rule; it is not an individual score, proof of shared meaning, or authority to act on any employee.
