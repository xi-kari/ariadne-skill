# Evidence Contracts and Support Ceilings

Use this reference for a detailed audit. Keep source identity, claim identity, and record lineage stable throughout the run.

## Six Claim Types

| Type | Responsibility | Evidence status |
|---|---|---|
| D | Define a term or contract field | Makes usage decidable; does not establish a world fact |
| G | State a testable empirical root hypothesis | Gains support only through an eligible frozen instance |
| E | Constrain observation, measurement, inference, and transfer | Limits conclusions; does not act as an empirical cause |
| H | Apply a human-domain empirical, classification, or normative clause | Preserve the subtype-specific evidence and action boundary |
| N | State a value or protective commitment | Make it explicit; do not disguise it as an empirical result |
| O | State an operating procedure | Governs freezing, review, action, correction, or withdrawal |

Split a sentence such as “the system is stable, so management should preserve it” into at least an empirical claim and a normative or operating claim. The first cannot prove the second.

## Four Dependency Types

| Dependency | Meaning | Enter the inference graph? |
|---|---|---|
| `inferential_requires` | A hard premise without which the conclusion does not follow | Yes |
| `protocol_requires` | A causal, evidence, analogy, source, classification, or other method gate | No |
| `specializes` | Restricts a general claim to a domain, object, or subtype | No |
| `applies_to` | States which object, claim, or action a norm or procedure governs | No |

Do not turn a method gate into another world cause, a classification rule into evidence, or a normative scope rule into proof.

## Evidence Chain

Keep these levels separate and justify every conversion:

1. **Source:** who or what produced the material, where, when, under which incentives and access conditions.
2. **Material:** the document, recording, dataset, artifact, statement, or trace as received.
3. **Observation:** a registered reading or measurement with object, position, protocol, time, scale, and error.
4. **Evidence:** an observation used for a specific claim under a stated design, baseline, and threshold.
5. **Counterevidence:** material or observations that contradict, bound, or offer a competing explanation.
6. **Judgment:** the bounded conclusion and its uncertainty, replication status, and extrapolation limit.
7. **External authorization:** a separate legal, institutional, or personal permission record; evidence never supplies it automatically.

Silence or absence is not negative evidence unless observation opportunity, expected signal, sensitivity, window, and alternative reasons for absence were frozen. Treat protected opacity as a reason to lower public confidence, not as guilt, pathology, or nonexistence.

For every `supported` Method Record claim, resolve each `support_id` to a source admitted by this record's cutoff or to an earlier claim ID in the same ledger. Resolve each `support_rule_id` to a full entry in this record's `rule_registry`. A module name, heading, ghost source, or undeclared `RULE:*` string is not support. A ceiling raise additionally requires exact parent-record context and a named evidence or protocol basis absent from every parent.

## Source Contract

For every source, record:

- source ID, domain, creator, material type, original location, timestamp, region, and case type;
- what the source can support and what it cannot support;
- sampling, access, incentives, transformations, and known omissions;
- the target object, SP/T/K, and extrapolation unit;
- counterexamples and independent corroboration or replication;
- bidirectional links from claim to material and material to its limited uses.

Keep original material, secondary interpretation, and Ariadne inference in separate columns. Definitions, field mappings, framework prose, examples, and internal numbering belong to method documentation, not `empirical_evidence_records`.

## Causal Contract

Freeze the following before publishing a causal judgment:

- candidate cause and result;
- temporal order, target variable, object, scale, and applicability window;
- named channel and complete mechanism chain;
- intervention, blockage, replacement, or identified natural variation that distinguishes the channel;
- common inputs, reverse direction, selection, measurement protocol, and substitute channels;
- cross-scale D3/E5 bridge where needed;
- a falsifier, pause condition, and bounded alternative explanations.

A mechanism story, temporal sequence, association, or result change without channel identification supports only a candidate path. If the evidence distinguishes several paths but not one, preserve all of them. Cross-scale correlation is not cross-scale causality.

## Analogy Contract

Mark analogy explicitly. Record source domain, target domain, shared structure, variable mapping, decisive differences, forbidden transfers, non-transferable conditions, target-side test, reverse conditions, and target responsibility or authorization differences.

Use analogy to generate questions. Do not transfer causal effects, normative evaluations, empirical support, or actions from the source domain. Only independent target evidence can support or refute the target claim.

## Root Instance Contract

Treat G1-G4 as question templates. Give empirical status only to a concrete instance.

### Freeze Before Results

Record:

- `instance_id`, `root_id`, immutable `contract_version`, and auditable preregistration timestamp;
- candidate object and object-contract IDs;
- SP, T, K, target variables, sampling unit, and generalization unit;
- exactly one subtype and exactly one success criterion allowed by that subtype;
- candidate specification, complexity-matched `N0`, controls, and model classes;
- one primary target or frozen aggregation rule;
- model selection or ensemble rule and multiple-comparison rule where applicable;
- evaluation metric, positive threshold, decision rule, null decision rule, falsifier, and pause condition;
- evidence mode: exploratory, confirmatory, replication, or falsification;
- every deviation, including `none`.

Keep result fields present but `not_evaluated` until execution. Do not fabricate timestamps, observations, or artifact references.

### Append After Execution

Record result time, the frozen primary result, positive-rule outcome, null-rule outcome, evidence references, analysis artifacts, contract version, and deviations. Use exactly one result state:

- `supported`: an eligible instance passes the frozen positive rule;
- `unsupported_or_undecided`: the positive rule fails or the bridge is inadequate and the null gate is not complete;
- `null_supported`: the frozen equivalence or sufficiency test, power or sensitivity gate, and tolerance all pass;
- `not_evaluated`: the instance has not run.

Only confirmatory or replication instances frozen before evidence and completed from that frozen contract can positively support downstream C conclusions. A falsification instance can support only its registered refutation or bounded null. Exploratory, draft, post-evidence-deviated, undisclosed-deviation, unresolvable-evidence, or unresolvable-artifact records generate candidates or remain unresolved.

### Root Families

| Root | Frozen question | Positive ceiling | Do not infer |
|---|---|---|---|
| G1 candidate grouping | Does the grouping beat a complexity-matched no-grouping baseline out of sample, survive boundary perturbation, and replicate in an independent time block or place? Choose predictive gain or intervention gain before results. | Limited object-identification and boundary support within SP/T/K and the generalization unit | Ultimate ontology, natural boundary, unified subject, value, or authority |
| G2 specified channel | Does one preselected controlled perturbation, controlled intervention, or identified natural variation change a specified transition above threshold? Measure capacity, delay, reliability, controllability, and loss separately. | Candidate causal carrier and only the measured channel dimensions | Universal cost, all channel properties, responsibility, or authorization |
| G3 historical increment | Does a predeclared history variable add out-of-sample information after controlling current registered state, environment, and measurement? For causal path dependence, preselect erasure, restoration, or equivalent intervention. | Predictive or causal path difference within the frozen window | Destiny, irreversibility, progress, fault, or authority |
| G4 scale closure or conversion | Preselect G4a conditional information, prediction, or intervention gain, or G4b exactly one of object-dynamics non-commutation, intervention non-commutation, identity-criterion violation, effective-relation change, and intervention-response change; never merge the five into one disjunctive fallback. | Bounded closure failure or preselected object/intervention conversion | A higher scale is truer, more important, or more authorized |

Never rescue one subtype or success criterion with an unselected favorable result. A positive failure is not a baseline victory; only the complete frozen null gate supports `N0`. A null comparator is a preregistered rule or model, not an observation. Only externally observed outcomes collected under the frozen comparator contract may support `null_supported`; writing `null`, naming `N0`, or observing no supplied counterexample is not evidence.

The four root families are the complete set; this version adds no fifth root. Translation fidelity is not a new root: judge it by combining the translation contract, G2 channel tests, and G4 closure contracts. Discuss a new root family only when a question presents an irreducible independent state machine, its own inputs and outputs, its own failure semantics, and its own success criteria; do not invent a root for a new topic.

### Challengeable Items and Post-Result Downgrade

All four roots share the same scale invariants: the preselected subtype, the success criterion, the `decision_rule`, and the `null_decision_rule`. Every scale transfer must preserve these four unchanged; swapping any of them creates a new instance rather than a transfer.

A challenge may target any of these sixteen items: candidate object, subtype, success criterion, `N0`, primary target or aggregation, model selection or ensemble, multiple-comparison rule, controls, positive threshold, null decision rule, data split, generalization unit, contract version, preregistration status, deviation record, and falsifier. Any item proven to have changed after results lowers the instance's support eligibility. Do not overwrite the frozen record with a post-result version; register the change and the downgrade in a child record.

## Human Empirical Instances

Apply the same freeze, result-state, support-eligibility, deviation, and null discipline to H1, H4, and H5:

| Claim | Preselect one family | Result ceiling |
|---|---|---|
| H1 meaning and coordination | Resource allocation, action choice, or coordination outcome | Conditional directional anchor for that outcome; not a unified inner state, consent, or common will |
| H4 power, mediation, and reflexivity | Evidence coverage, expression safety, object behavior, or reflexive response | Bounded positional, mediation, publicity, or response effect; not malice, responsibility, or disposition |
| H5 historical carrier | One of the five carrier families, one atomic carrier reference, and one of the three persistence criteria | Candidate trace in the named carrier and window; future path effect still requires G3 |

H5 preselects exactly one subtype from the closed list of five carrier families: `institutional_or_textual_record`, `role_or_organizational_arrangement`, `habit_or_practice`, `trauma_record`, and `collective_memory_carrier`. It preselects exactly one criterion from the closed list of three: `threshold_persistence_over_preregistered_window`, `repeat_detection_across_preregistered_windows`, and `persistence_after_event_or_exposure_end`. `selected_carrier` is one non-empty atomic reference, never a list, and `selected_carrier_family_id` must match the preselected subtype's family exactly; any mismatch disqualifies the instance before results are read. Never search across families or criteria for one surviving result.

H2 is a carrier and responsibility classification rule, H3 a classification of institutional writeback, and H6 a normative boundary. Do not treat these classifications as empirical causes. No H instance creates value, obligation, diagnosis, or authorization.

## Epistemic Gates E1-E5

| Gate | Require | Downgrade when absent |
|---|---|---|
| E1 object declaration | Object, scale, window, variables, instance N0, and K | Exploratory questions only |
| E2 observation position | Observer, channel, model limits, error, and blind spots | Description with explicit incompleteness |
| E3 conditional observation participation | An actual observation, naming, scoring, or publication channel plus counterfactual | Do not claim reflexivity |
| E4 alternatives and residuals | At least one distinguishable competing explanation, counterexample, and unexplained residual | Keep mechanisms unresolved; avoid irreversible action |
| E5 cross-scale transfer | D3 mapping, invariants, changes, losses, error, alternatives, and residuals | Parallel scale descriptions only |

E1, E4, EVIDENCE, CAUSAL, ANALOGY, and SOURCE can be protocol gates without becoming inferential causes. Expanded observation never expands J authorization.

## Conditional Inference Ceilings C1-C12

| Conclusion | Inferential minimum | Ceiling and failure boundary |
|---|---|---|
| C1 object and boundary | D0 + eligible G1 | Limited object strength within SP/T/K; otherwise candidate grouping |
| C2 carrier and channel | D0 + eligible G2 | Named carrier and measured dimensions; no unified cost or responsibility |
| C3 feedback and learning | D2 + G2; add G3, retained update, repeated rounds, and task comparison for learning | Feedback only unless every learning condition is present |
| C4 history and path | D1 + G3; add predeclared K*/F* and timing comparison for repair window | Predictive or causal path difference; no destiny or authorized repair |
| C5 load and recovery | D0 + G2 with comparable units/window/location; add G3 and carrier for cumulative damage | Instant gap only without history evidence |
| C6 scale closure/conversion | D3 + one eligible G4 subtype and criterion | Only the selected closure or conversion result; failed positive gate remains unresolved |
| C7 cross-boundary spillover | G2 + G4, timing, channel, counterfactual, and distribution location | Call it an externality only with an additional institutional or accounting rule |
| C8 variation-retention-reproduction | D1 + predeclared variation, differential result, next-round retention, repetition, and drift alternatives; G2 for a named mechanism | Pattern without G2; not intention, superiority, or governance choice |
| C9 observation response | G2 channel and no-observation, alternate-observation, or blockage counterfactual; G3 for persistence | One bounded response; no inherent trait or suppression authority |
| C10 human carrying chain | G2 + H2 classification; G3 for intertemporal reproduction; H5 for a historical carrier | Separate carrier, cost bearer, beneficiary, stop holder, and responsible subject |
| C11 institutional writeback | D2 + G2 return channel + H3 classification of receipt, field change, and execution | Receipt is not writeback; one writeback is not learning or legitimacy |
| C12 normative bridge | N1 + O1-O4, explicit positive norms, protection, J authorization, options including no action, stopping, rollback, and remedy | A procedural gate, not empirical evidence; missing any component blocks real-world disposition |

Root templates in combination are never sufficient by themselves. Definitions, examples, and internal explanations cannot satisfy the empirical parts of these conclusions.

## Method Record Update

- Keep the frozen object in `object_contract`; do not silently refine it after viewing evidence.
- List only included sources in `evidence_cutoff` and preserve the cutoff timestamp.
- Put each split D/G/E/H/N/O claim in `claim_ledger` with explicit support and counterevidence IDs.
- Put alternatives, residuals, missing observations, invalid bridges, and protected opacity in `unknowns_and_counterevidence`.
- Set the local ceiling to match the weakest critical link. A normal child applies the minimum of that ceiling and its parent. Raise only in a child that newly admits named external evidence or a newly fulfilled declared protocol; module completion never raises.
- Add `ariadne-evidence` to `module_runs`, route scale questions to `ariadne-scale`, and keep `authorization_effect: none`.

## Strong Example

Request: “Response time fell 20% after our team adopted a chat tool, so the tool caused the improvement and every department should adopt it.”

Split the statement before auditing it:

- D: what counts as response time and which messages are included;
- G: the tool caused a change in the target transition;
- E: the pre/post dashboard and its measurement limits;
- N: faster response is prioritized over competing values;
- O: every department should adopt the tool.

The dashboard is material. Its time-stamped records can become observations for a defined metric. Without a frozen comparison, channel test, and alternatives such as staffing, workload, seasonality, message mix, and measurement change, it does not identify the tool as the cause. The recommendation additionally lacks values, local feasibility, authorization, stopping, rollback, and remedy.

<!-- method-record-example:start -->
```yaml
record_id: ariadne:chat-response-audit-001
schema_version: '1.2'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: diagnosis
object_contract:
  boundary: One support team's work-message intake and response workflow; other departments are outside the audited object.
  state_variables:
  - response-time metric under a frozen inclusion rule
  - message volume and mix
  - staffing and shift coverage
  - chat-tool use
  relations_or_transitions:
  - incoming message to first qualifying response
  - tool adoption precedes the observed post-period but its causal channel is unresolved
  interfaces:
  - customer-message intake
  - staff scheduling
  - chat notifications and routing
  time_window: eight weeks before and eight weeks after adoption
  scale_profile:
    A: messages aggregated to team-week summaries
    X: one support team
    T: sixteen-week pre/post window
    O: single team
    C: candidate channel effect
    R: message records and weekly summaries
    I: team and its incoming customers
    N: message-routing network
    J: 'not_applicable: no action authorization is evaluated in this evidence audit'
  identity_criterion: The same workflow while message definition, staffing unit, and response rule remain comparable.
  status: candidate
evidence_cutoff:
  as_of: '2026-08-04T00:00:00+08:00'
  included_source_ids:
  - source:team-dashboard-export
  - source:tool-rollout-log
  excluded_after_cutoff: true
scale_scope:
  source: message-level observations in one team
  target: claims about all departments
  transform_status: failed
claim_ledger:
- claim_id: D-response-time
  claim_type: D
  text: Response time requires a frozen message inclusion and first-response rule.
  status: candidate
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
- claim_id: G-tool-cause
  claim_type: G
  text: The chat tool caused the observed response-time decrease.
  status: unresolved
  support_ids:
  - observation:pre-post-dashboard-change
  counterevidence_ids:
  - alternative:staffing-workload-seasonality-measurement
  support_rule_ids: []
- claim_id: N-speed-priority
  claim_type: N
  text: Faster response should take priority over privacy, workload, and other outcomes.
  status: unresolved
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
- claim_id: O-universal-adoption
  claim_type: O
  text: Every department should adopt the tool.
  status: unresolved
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
rule_registry: []
unknowns_and_counterevidence:
  unknowns:
  - 'unknown: frozen response-time definition and dashboard protocol stability'
  - 'unknown: complexity-matched baseline, comparison group, channel intervention, and independent replication'
  - 'unknown: department-specific feasibility, values, authorization, stopping, rollback, and remedy'
  counterevidence:
  - staffing, workload, seasonality, message mix, and metric changes remain live alternatives
conflicts: []
output_ceiling: description_only
ceiling_transition:
  operation: root
  inputs: []
  basis: []
  result: description_only
module_runs:
- module: ariadne-evidence
  status: completed
  input_records: []
  output_record:
    record_id: ariadne:chat-response-audit-001
    record_version: 1
module_payloads: []
recommended_next_modules:
- ariadne-scale
- ariadne-mechanism
- ariadne-choice
- ariadne-audit
authorization_effect: none
```
<!-- method-record-example:end -->

The bounded result is: a pre/post decrease was observed under an incompletely specified metric; causality and cross-department transfer remain unresolved; universal adoption is not supported or authorized.

## Chained Virtual Instances m1-m4

These virtual instances describe a fictional multi-layer transport model that cites no external observation; they only show how root contracts chain and give no empirical support to any G claim.

| Instance | Candidate object | Preselected criterion | N0 | Fails when |
|---|---|---|---|---|
| m1 / G1a | Interconnected unit groups with frozen B, X, T, SP, K, and grouping | `out_of_sample_predictive_gain` | Complexity-matched baseline without the grouping | Gain holds only in training data, dies under slight boundary perturbation, or fails the independent time block |
| m2 / G2a | One conduction channel and target transition on m1's object | `controlled_perturbation_effect` | Controlled blockage leaves the target transition below threshold | The blockage does not move the transition above threshold; success registers the channel only as a candidate causal carrier with delay measured, leaving capacity, reliability, controllability, and loss unknown |
| m3 / G3a | History variable "backlog over the previous three rounds" on the same object | `historical_conditional_predictive_gain` | Current queue, environment input, and measurement protocol suffice | History adds no out-of-sample increment after controls, or causal path dependence is claimed without a preselected erasure, restoration, or equivalent intervention |
| m4 / G4a | Micro-to-aggregate mapping M with frozen retained and excluded variables | `conditional_information_gain` | Excluded local timing adds no above-threshold conditional information given the aggregate variables | The increment stays below threshold, or the criterion is switched to prediction, intervention, or G4b conversion after results |

The four instances feed one another follow-up questions but never substitute for one another: m1 passing does not guarantee m2's channel effect, m2 passing does not guarantee m3's history increment, and m3 passing does not guarantee m4's closure failure.
