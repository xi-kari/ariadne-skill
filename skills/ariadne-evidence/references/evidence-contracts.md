# Evidence Contracts and Support Ceilings

Use this reference for a detailed audit. Keep source identity, claim identity, and record lineage stable throughout the run. Section anchors (§) point to the source text named in `ariadne-skill/references/source-navigation.json`. This file owns the G1-G4, E1-E5, 法1-法3, and C1-C12 definitions for the whole suite; other modules consume recorded instance results and cite this file instead of restating the rules.

## Contents

1. Proposition roles and dependencies
2. Common method constraints 法1-法3
3. Evidence chain, independence, and defect propagation
4. Source contract
5. Measurement and data generation
6. Causal contract, estimands, and chains
7. Analogy and formal conclusions
8. Domain evidence and formal-instance standing
9. Root instance contract and the G1-G4 question families
10. History: three questions and two routes
11. Human empirical instances
12. Epistemic gates E1-E5
13. Result contracts C1-C12 and condition trees
14. Per-proposition downgrade
15. Method Record update, strong example, and virtual instances

## Proposition Roles and Dependencies

| Role | Responsibility | Evidence status |
|---|---|---|
| D | Define a term or contract field | Makes usage decidable; does not establish a world fact |
| G | Instantiate an empirical question family (G1-G4) as a concrete factual claim | Gains formal support only through an eligible frozen instance; ordinary evidence still supports what its design supports |
| E | Constrain observation, measurement, inference, and transfer | Limits conclusions; does not act as an empirical cause |
| H | Apply a human-domain empirical, classification, or normative clause | Preserve the subtype-specific evidence and action boundary |
| N | State a value or protective commitment | Make it explicit; never disguise it as an empirical result |
| O | State an operating procedure | Governs freezing, review, action, correction, or withdrawal |
| F | State a conditional formal proposition inside a declared model | Established by proof, exhaustive finite check, or verified computation; never by observation count |

C entries are not an eighth kind of fact. They are use contracts that say what bounded output registered results and added mechanism conditions can jointly license; C12 is a normative procedure gate (§2.2, §4.10). Split a sentence such as "the system is stable, so management should preserve it" into at least an empirical claim and a normative or operating claim; the first cannot prove the second.

| Dependency | Meaning | Enter the inference graph? |
|---|---|---|
| `inferential_requires` | A hard premise without which the conclusion does not follow | Yes |
| `protocol_requires` | A causal, evidence, analogy, source, domain-classification, or other method gate | No |
| `specializes` | Restricts a general claim to a domain, object, or subtype | No |
| `applies_to` | States which object, claim, or action a norm or procedure governs | No |

Do not turn a method gate into another world cause, a classification rule into evidence, or a normative scope rule into proof. In the Method Record, `depends_on` lists the earlier claims a claim inferentially rests on; it is what makes per-proposition downgrade auditable.

## Common Method Constraints 法1-法3

The three constraints are duties on how a model is used, not empirical laws of the world (§4.17, Appendix C.2). Whether following them reduces error or adds needless burden is a separate empirical question; compliance never proves the framework valid.

- **法1 Task and representation are declared together.** State object, layering, coarse and fine scales, target variables bound to the task, observation position, horizon, environment, and use. For every conversion check what is kept, folded, omitted, and added. Do not presume a lossless conversion, and do not assert that every conversion loses something task-relevant. Recovering an answer, advancing dynamics, and evaluating an intervention are checked separately, and so is whether two conversion orders are equivalent. What must be kept is the distinction the task depends on, not every detail.
- **法2 Material identity and support range stay traceable.** Reports, observations, model beliefs, formal proofs, simulation outputs, and execution receipts keep their own identities. Each inference states the new information, premises, and rules it adds. Reprocessing the same material is not a new observation. A simulated state may seed the next simulation round, but recursion depth adds no empirical support and no capability grade. The gain from a new computation or proof comes from a checkable argument and is never packaged as a new real-world sample.
- **法3 Fact, value, and action standing are established separately.** Facts, forecasts, formal feasibility, and technical ability never alone produce value, responsibility, or disposal power. An analytic recommendation publishes its normative aim, evidence, costs, and dissent; real adoption additionally needs valid authority, the protection floor, implementation resources, and stop and remedy conditions. Normative premises never prove an empirical mechanism.

Framework evaluation is a separate empirical target (§4.17.4): the number of G question families does not prove coverage, a complete C contract does not prove reliability, and whether the method is worth using is decided by a comparison against adequate professional methods and simpler alternatives on shared goals, material, and budget. An individual instance effect, a question family's applicability rate, and the framework's net gain are three different targets.

## Evidence Chain, Independence, and Defect Propagation

Keep these levels separate and justify every conversion (§2.5):

1. **Source:** who or what produced the material, where, when, under which incentives and access conditions.
2. **Material:** the document, recording, dataset, artifact, statement, or trace as received.
3. **Observation:** a registered reading or measurement with object, position, protocol, time, scale, and error.
4. **Evidence:** an observation used for a specific claim under a stated design, baseline, and threshold.
5. **Counterevidence:** material or observations that contradict, bound, or offer a competing explanation.
6. **Judgment:** the bounded conclusion and its uncertainty, replication status, and extrapolation limit.
7. **External authorization:** a separate legal, institutional, or personal permission record; evidence never supplies it automatically.

Unobservable is not nonexistent. Protected opacity states its reason, minimum scope, duration, and trusted reviewer, and lowers public confidence; it is never read as guilt, pathology, or nonexistence. When a counterexample or residual appears after freezing, keep the failure record and downgrade, pause, or withdraw under the contract; never rewrite the object, subtype, threshold, or success criterion after the result.

**Independence is judged relative to the supported claim** (§2.7.2). Later outcomes from the same random assignment add time and outcome information but not independent randomizations. Re-running the same data with another algorithm can expose implementation or interpretive problems but adds no new cohort. Different underlying samples are not merged because their names are similar. Record shared data, common measurement, version inheritance, and genuinely new observation; never turn a file count into an evidence score. Keep the dependency chain from source value to transcription, model input, derived statistic, and stated judgment traceable. When numbers disagree, first separate a same-object conflict, a legitimate difference between objects, and a display-precision artifact, then suspend only the precise conclusions that truly depend on the difference. A closed total does not certify each component, and a source anomaly does not reveal its own cause. Other independently grounded judgments keep their actual range.

For every `supported` Method Record claim, resolve each `support_id` to a source admitted by this record's cutoff or to an earlier claim ID in the same ledger, and each `support_rule_id` to a full entry in this record's `rule_registry`. A module name, heading, ghost source, or undeclared `RULE:*` string is not support. A ceiling raise additionally requires exact parent-record context and a named evidence or protocol basis absent from every parent.

## Source Contract

For every source, record (§2.7):

- source ID, domain, creator, material type, original location, timestamp, region, and case type;
- what the source can support and what it cannot support;
- sampling, access, incentives, transformations, and known omissions;
- the target object, SP/T/K, and extrapolation unit;
- counterexamples and independent corroboration or replication;
- bidirectional links from claim to material and material to its limited uses.

Keep original material, secondary interpretation, and Ariadne inference in separate columns. Definitions, field mappings, framework prose, examples, and internal numbering belong to method documentation, not `empirical_evidence_records`; a method definition is not empirical support.

Record how far the material was actually read (§2.7.1): table of contents, abstract, chapter, or full text; finding a link, downloading, and understanding the argument are different states. Different analyses of one dataset, a preprint and its published version, and an original report and its retelling keep their source relation and are never added up as independent replications. When a version changes the outcome, sample, or definition, state the change before comparing. A theory's historical adoption, mere mention, explicit limitation or rejection, compatibility with the present text, and the analyst's new connection are separate claims. Not finding an adoption record is not proof it never happened; a transcribed catalogue is not a checked original. Generation, retention, destruction, opening, retrieval, and narrative selection all create absences, so **absence counts against a claim only when that kind of event should have left a record that could be found**. An inaccurate oral date still gets corrected, and the way a story is told remains important material for understanding memory.

## Measurement and Data Generation

State what is measured and how the material was produced before deciding which errors and counterexamples matter (§2.5.1). Directly recorded quantities, definitional composite indices, measures of latent attributes, formative conditions, and predictive proxies carry different interpretive duties; a reflective indicator and a component that defines an index need different validity arguments. Comparisons across groups or periods need proportionate comparability: latent means need an explained unit and origin, individual threshold decisions also need personal error and consequence, and an identical score mapping does not mean identical psychological strategy. A drifting common anchor needs external anchoring or sensitivity analysis.

An indicator can move for four reasons that may coexist and must be checked separately: real improvement, real adaptation to a narrow target, a change in who enters or reports, and record falsification. Two legitimate indicators moving in opposite directions do not mean one is wrong or manipulated. Observation records are jointly formed by the object, collection, and reporting: fewer positive records can come from lower risk, responses that prevented the outcome, or lower detection.

## Causal Contract, Estimands, and Chains

Freeze the following before publishing a causal judgment (§2.4):

- the specific version of the treatment or cause, the result, the object and population, the time window, the scale, and the effect asked about;
- why the comparison identifies it; common inputs, selection, attrition, measurement change, reverse action, and interference between units, handled as relevant;
- for a named structural channel or complete mediation: the mechanism chain, timing, and discriminating evidence (do blockage, replacement, or identified natural variation move the result as predicted; can a substitute channel explain it; is a D3/E5 bridge in place for cross-level claims; which observation would break it);
- a falsifier, a pause condition, and bounded competing explanations.

Timing, correlation, and a coherent story cannot identify causation alone. "Effect bounded and identified, specific mechanism unresolved" is a legitimate result. Causal strength, mechanism resolution, and extrapolation range are graded separately. Opposing paths can cancel, so a near-zero total effect does not prove a mechanism absent.

**Estimand and mechanism duty** (§2.4.1). Offering an opportunity, actual receipt, and institutional expansion are different treatments; average, complier, and individual effects are different targets. A damaged identification assumption lowers only the conclusions resting on it. More controls are not always better: controlling a mediator changes the total effect, and controlling a collider introduces bias. More data cannot separate explanations the design cannot distinguish. When point identification fails, keep bounds, sign sets, excluded necessary conditions, and concrete process knowledge, and say what was not answered. Agreement text, verification, enforcement, and daily use are different outcomes; announcement, understanding, attendance, handling, and release are evidenced link by link.

**Local effects, joint response, and whole chains** (§2.4.2). Composing local channels keeps the correspondence of upstream output and downstream input, same-case identity and timing, common support, joint response, and terminal outcome. **Two average link effects are never multiplied into a chain effect.** Counterexample: types s in {0,1} with equal weight, m(a) = a(1-s), y = s*m. Each link's average effect is 1/2, the chain effect is 0, and the product 1/4 is wrong, because different types carry the two links. "Complete" is always relative to the declared result, window, and dependency route. Identifying a total effect does not require exhausting micro-processes; operating a mediator, transferring across domains, or allocating responsibility adds the dependent connections back. Shared resources, offsetting paths, and feedback change how links connect; nodes evidenced separately are not a same-case joint test.

## Analogy and Formal Conclusions

Mark analogy explicitly (§2.6). Record source domain, target domain, shared structure, variable mapping, decisive differences, forbidden transfers, non-transferable conditions, target-side test, reverse conditions, and differences in target responsibility or authorization. Keep three states apart (§2.6.1): a heuristic analogy, a formal instance that satisfies explicit mathematical premises, and a target-domain relation tested on independent material. Only the last supports a target claim. Similar words, diagrams, narratives, or outcomes are not bridging evidence. Historical and archaeological comparison separates how a trace physically formed, what activity it served, and what social relation it reflects; different knowledge sources need not carry equal weight on every question.

A formal proposition states its state space, mappings, target, allowed operations, and logical premises, and its conclusion is fixed by proof; exhaustive enumeration can check every case of a finite domain; numerical computation states precision, boundary decisions, and implementation error, and repeated computation adds no independent empirical support (§2.1.2). Applying a formal result to a real object also states how quantities map to model variables, which premises have material, the error and validity interval, and which counterexample breaks the mapping. Six judgments need separate grounds: formally feasible, an algorithm exists, computable within budget, data available in time, actually executed correctly, and authorized to adopt.

## Domain Evidence and Formal-Instance Standing

Two-stage admission governs only strong G, C, and CM claims made in this framework's name (§2.1, §2.1.1). Existing research, archives, oral history, archaeology, and original texts support description, explanation, or bounded causal conclusions according to their actual design. Record that design truthfully (preregistered confirmation, post hoc discovery, exploration, historical reconstruction); never back-fill a pre-result contract. Such material does not automatically earn G-instance support, and it does not lose its content because it was never converted into one. When an existing finding seeds a new formal instance, treat it as a source of questions and models and test it on independent material, a later window, or a replication design, keeping exploration and confirmation data, and model selection and final evaluation, apart. Formal proofs, textual interpretation, and normative claims stand by their own standards and never impersonate one another.

## Root Instance Contract and the G1-G4 Question Families

G1-G4 are four kinds of empirical question, not laws about all objects (§4 opening): does a candidate grouping add conditional gain; does a named channel have an identifiable effect on a target transition; does history add conditions beyond the current representation; under which tasks, dynamics, and interventions does a stated representation close. A G-instance registers both the factual claim under test and the evidence rule; whether the effect exists is settled by the world and the conditions asked about, and whether the evidence suffices is settled by design and result. Registering one result twice adds no evidence, and the number of families passed does not measure the framework's usefulness.

### Freeze Before Results

Record (§4.1):

- `instance_id`, `root_id`, immutable `contract_version`, and auditable preregistration timestamp;
- candidate object and object-contract IDs;
- SP, T, K, target variables, sampling unit, and generalization unit;
- one subtype and one success criterion allowed by that subtype, selected before evidence;
- candidate specification, complexity-matched `N0`, controls, and model classes;
- one primary target or a frozen aggregation or joint rule;
- model selection or ensemble rule and multiple-comparison rule where applicable;
- evaluation metric, positive threshold, decision rule, null decision rule, falsifier, and pause condition;
- evidence mode: exploratory, confirmatory, replication, or falsification; preregistration status: draft, frozen before evidence, completed from frozen, or deviated after evidence;
- every deviation, including `none`.

The single primary criterion is the default defense against choosing the best result afterwards, not the only valid research form. Multiple outcomes, multiple models, joint criteria, explore-then-confirm, and sequential designs are legitimate when the primary target or joint rule, selection procedure, stopping rule, and multiple-comparison handling are stated in advance; failed single items are never stitched into a success afterwards. Keep result fields present but `not_evaluated` until execution. Do not fabricate timestamps, observations, or artifact references.

### Append After Execution

Record result time, the frozen primary result, positive-rule outcome, null-rule outcome, evidence references, analysis artifacts, contract version, and deviations. Use exactly one result state:

- `supported`: an eligible instance passes the frozen positive rule;
- `unsupported_or_undecided`: the positive rule fails or the bridge is inadequate and the null gate is not complete;
- `null_supported`: the frozen equivalence or sufficiency test, power or sensitivity gate, and tolerance all pass;
- `not_evaluated`: the instance has not run.

The summary state does not replace the specific findings: also record which criteria passed, which were refuted, and which stayed undecided for lack of precision or material. Only confirmatory or replication instances frozen before evidence and completed from that contract can positively support downstream C conclusions. A falsification instance supports only its registered refutation or bounded null. Exploratory, draft, post-evidence-deviated, undisclosed-deviation, unresolvable-evidence, or unresolvable-artifact records generate candidates or remain unresolved.

### Question Families

| Family | Frozen question | Positive ceiling | Do not infer |
|---|---|---|---|
| G1 grouping gain | Does the grouping beat a complexity-matched no-grouping baseline out of sample (G1a predictive or G1b intervention gain, chosen first), survive boundary perturbation, and replicate in an independent time block or place, controlling common environment, sampling, classification bias, grouping leakage, and complexity? | Bounded object-identification strength, boundary credibility, and grouping window within SP/T/K | Ultimate ontology, natural boundary, unified subject, goal, value, responsibility, or authority |
| G2 named channel | Does one preselected controlled perturbation or intervention (G2a) or identified natural variation (G2b) change a specified transition above threshold? Capacity, delay, reliability, controllability, and loss are measured channel by channel, dimension by dimension. | Candidate causal carrier and only the measured dimensions | Universal cost, unmeasured dimensions, responsibility, or authorization |
| G3 historical increment | After the current registered state, environment, and measurement, does a predeclared history variable add out-of-sample information (G3a), or does a preselected erasure, restoration, or equivalent intervention change the path (G3b)? `N0`: the current registered state is a sufficient statistic. | Predictive or causal path difference beyond the current representation, within the window | Destiny, irreversibility, progress, fault, authority, or the absence of history's formative role |
| G4 representation closure or conversion | G4a closure failure: preselect conditional information, predictive, or intervention gain from excluded variables given the retained ones. G4b conversion: preselect exactly one of object-dynamics non-commutation, intervention non-commutation, identity-criterion violation, effective-relation change, or intervention-response change; never merge the five into a disjunctive fallback. | Bounded closure failure or the preselected conversion, relative to stated targets, horizon, environment, and operations | A higher scale is truer, more important, or more authorized |

G2 is not the only entrance to causal knowledge: when a qualified comparison identifies a total effect but cannot separate channels, keep the total effect, mark the channel unresolved, and do not invent a mechanism. Like quantities or an explicit conversion are needed before a transfer can be traced. If common inputs, substitute channels, or measurement protocol explain the difference, withdraw the channel claim.

G4 holds symmetric interest in closure and non-closure (§4.6): closure shows a simple representation suffices; non-closure shows the representation, task, or operation range needs revision; neither result ranks methods. Closure is always relative to targets, horizon, environment, and allowed operations; adequacy for routine prediction is not adequacy under a new intervention. A shortfall can be met by adding the necessary variable, keeping composition or history, restricting the action set, shortening the horizon, or narrowing the use, without restoring every micro detail. Emergence, aggregation, same-scale omitted variables, and cross-boundary transmission do not require G4 closure failure. General correlation, unconditional coupling, similar narratives, and same-scale omitted variables do not support G4. "Not significant" is not closure; only a passed null gate registers criterion-bounded closure (G4a) or no preselected conversion found (G4b). A formal proof of exact closure and a finite dataset that found no deviation are different evidence identities, and a proof grants no real G4-instance support.

Never rescue one subtype or success criterion with an unselected favorable result. A null comparator is a preregistered rule or model, not an observation; only externally observed outcomes collected under the frozen comparator contract may support `null_supported`. The four families are not claimed exhaustive or logically independent, and no fifth family is added for a new topic; translation fidelity is judged by combining the translation contract, G2 channel tests, and G4 closure contracts.

### Challengeable Items and Post-Result Downgrade

All four families share the same scale invariants: the preselected subtype, the success criterion, the `decision_rule`, and the `null_decision_rule`. Every scale transfer preserves these four; swapping any of them creates a new instance rather than a transfer. A challenge may target any of these sixteen items: candidate object, subtype, success criterion, `N0`, primary target or aggregation, model selection or ensemble, multiple-comparison rule, controls, positive threshold, null decision rule, data split, generalization unit, contract version, preregistration status, deviation record, and falsifier. Any item proven to have changed after results lowers the instance's support eligibility; register the change and the downgrade in a child record without overwriting the frozen one.

## History: Three Questions and Two Routes

Historical research first separates three questions (§4.5):

1. How did earlier experience form the current state?
2. How does a current carrier keep, update, and pass on that formation to later results?
3. Given the current registered representation, does historical material still add information or effect?

The first two can hold while the third fails, and a failed third never shows the first two hold. **G3 tests only the third.** Example: H forms skill S, and S drives result Y. When S fully carries the history, H adds no predictive information; G3's narrow condition fails, yet H's formative role and ordinary learning can be supported by independent material. Report total historical effect, current carrier, and conditional residual separately. Never create a G3 gain by leaving out a known current state: the increment depends on the chosen representation z = pi(x), and history may only be restoring what pi folded away. "In principle the state could be enlarged to a sufficient one" does not prove that this case has no historical increment, and when the full current carrier is unavailable, no one may claim to have excluded one (Appendix C.11).

Register two cross-time routes separately:

- **Carried route:** the measured current state or carrier, the grounds that earlier inputs entered it, its retention or update within the window, and longitudinal material showing it goes on to affect the predeclared result. A persisting result or an existing carrier alone does not confirm the mechanism. A causal claim compares interruption, replacement, restoration, or natural variation under §2.4 and handles common inputs, continued exposure, selection, attrition, and measurement change; correlational material stops at cross-time description or mechanism candidate. Formal carried-branch support needs a qualified G2-instance or an interface-specified H-instance for the channel and result; H5 supports only the selected carrier and window; one immediate effect is never extrapolated into a long-term one.
- **Increment route:** G3 as above.

The carried route can hold while G3 is unsupported, and a failed G3 does not disprove the carried route. Never switch routes after results to rescue a claim. Accumulation, persistence, learning, delayed recovery, and cross-time reproduction earn no support by their names.

## Human Empirical Instances

Apply the same freeze, result-state, support-eligibility, deviation, and null discipline to H1, H4, and H5, with `claim_id` in place of `root_id` (§4.2):

| Claim | Preselect one family | Result ceiling |
|---|---|---|
| H1 meaning and coordination | Resource allocation, action choice, or coordination outcome | Conditional directional anchor for that outcome; not a unified inner state, true consent, or common will |
| H4 power, mediation, and reflexivity | Evidence coverage, expression safety, object behavior, or reflexive response | Bounded positional, mediation, publicity, or response effect; not malice, responsibility, or disposition |
| H5 historical carrier | One of the five carrier families, one atomic carrier reference, and one of the three persistence criteria | Candidate trace in the named carrier and window; later effects follow the carried route, and an increment beyond the current representation still needs G3 |

H5 preselects exactly one subtype from the closed list of five carrier families: `institutional_or_textual_record`, `role_or_organizational_arrangement`, `habit_or_practice`, `trauma_record`, and `collective_memory_carrier`. It preselects exactly one criterion from the closed list of three: `threshold_persistence_over_preregistered_window`, `repeat_detection_across_preregistered_windows`, and `persistence_after_event_or_exposure_end`. `selected_carrier` is one non-empty atomic reference, never a list, and `selected_carrier_family_id` must match the preselected subtype's family exactly; any mismatch disqualifies the instance before results are read. Never search across families or criteria for one surviving result.

H2 is a carrier and responsibility classification rule, H3 a classification of institutional writeback, and H6 a normative boundary for open bearing; none enters the empirical instance contract. Without a qualified external instance, `empirical_evidence_records` stays empty and the status is `requires_instance_evidence` (§4.9). No H-instance, even when supported, creates value, responsibility, obligation, legitimacy, authorization, or disposition; protective, harm-reducing, or repair action passes through C12, explicit N, and O procedures.

## Epistemic Gates E1-E5

| Gate | Require | Downgrade when absent |
|---|---|---|
| E1 object declaration | Object, range, scale, window, necessary variables, and K; a comparison also states its baseline or zero model | Name which inference each missing field limits; never cancel an independently established source fact for a formatting gap |
| E2 observation position | Observer, measurement channel, model limits, error, and blind spots; adequacy judged against target, horizon, environment, and operations | Gather evidence, narrow the use, or stay unresolved; do not presume every task needs more perspectives |
| E3 conditional observation participation | An actual causal coupling of observing, naming, scoring, or publishing with the object, a located channel, and a no-observation, alternate-observation, or blockage counterfactual | Do not claim reflexivity |
| E4 competing explanations and residuals | Competitors the material allows and that could change the judgment; what they compete over (effect size, mechanism, contextual meaning, extrapolation range, normative premise); counterexamples and residuals | Keep mechanisms unresolved; with no reasonable competitor, record the search range and failure conditions instead of inventing one |
| E5 cross-scale transfer | D3 mapping, invariants, changes, losses, error, competitors, and residuals | Parallel scale descriptions only |

Compatible explanations can carry different levels of responsibility. Openness, love, complexity, or a sense of theoretical wholeness never fills an evidence gap. How unresolved competitors limit action is judged with harm, reversibility, external duties, and current authority. E5's only inferential hard prerequisite is D3; E1, E4, EVIDENCE, ANALOGY, and SOURCE are method gates. E5 does not depend on G4 being true, and every G4-instance must pass E5. A wider observation range is not a wider authorization range, and the J axis never extrapolates along with other axes.

## Result Contracts C1-C12 and Condition Trees

C1, C2, the G3 branch of C4, and C6 mainly register bounded results already supported by empirical instances and add a use range. C3, C5, C7, and C9-C11 also combine separately listed mechanism, timing, or domain conditions. C8's base pattern depends on separately obtained variation-differential-reproduction evidence. C12 is a normative procedure gate. Sharing a numbering does not make them one kind of empirical law, and citing the same material again adds no second independent support (§4.10).

| Contract | Inferential minimum and branches | Ceiling and forbidden jump |
|---|---|---|
| C1 object and boundary | D0 + eligible G1 | Bounded object strength within SP/T/K; not ultimate ontology, natural boundary, unified subject, common goal, S0-S6 stage, value, responsibility, or authority |
| C2 carrier and channel | D0 + eligible G2; like quantities or explicit conversion, units, identity rule, window, accounting boundary | Named carrier and measured dimensions; no unified cost, one dimension for all, carrier as responsible subject, or conservation from resource occupation |
| C3 feedback and feedback-mediated learning | D2 + G2. `C3-feedback`; `C3-carried-learning` (updated carrier, repeated invocation, task result under the carried route); `C3-learning` (history increment: add G3, retained update, repeated rounds, preset out-of-sample task comparison) | Entry or receipt is not effective feedback; one update is not learning, repair, or improvement; no value direction or authorization |
| C4 history, path difference, repair window | D1; G3 branch, plus carried and timing branches under the carried route and §2.4; a repair window needs K*/F*, comparison of intervention times, and causal identification, adding G3 only for an extra historical residual | A preserved trace is not a historical effect; predictive gain is not causation or irreversibility; path difference is not destiny, progress, decline, fault, or regression; no "repair" before K*/F* is public |
| C5 load, capacity, recovery | D0 + G2 with comparable units, window, and location. `C5-instant`; `C5-carried-cumulative` (carried route); `C5-cumulative` (G3) | Load is not necessarily monotone; overload is not necessarily collapse; unlike quantities are not subtracted; an instant gap is not lasting damage; recovery need creates no sacrifice duty for a named subject |
| C6 representation closure and conversion | D3 + one preselected G4a or G4b subtype and criterion; null gate actually passed before closure or no-conversion is registered | No G4 from general correlation; no post hoc union; "not significant" is not closure; larger scale is not truer or more authorized; same name is not same object |
| C7 local improvement and cross-boundary spillover | G2; real cross-scale moves add D3/E5; closure failure or conversion adds G4 | Crossing an object or administrative boundary is not automatically a scale change; local improvement does not necessarily harm a larger scale; "externality" needs an institutional or accounting definition; finding spillover assigns no compensation, responsibility, or disposition; a well-closed model can represent cross-boundary action correctly |
| C8 variation, differential retention, reproduction | D1 + predeclared variation, differential result, next-round retention, repeated rounds, and drift competitors. `C8-pattern`; `C8-mechanism` (G2) | Not every evolution is selection; one survival is not differential retention; the retained are not better or more legitimate; system filtering is not actor choice, governance, or authorization |
| C9 observation channel and reflexive response | G2 + E2/E3 counterfactual. `C9-response`; `C9-carried-persistence`; `C9-persistent` (G3) | Not every observation changes the object; a post-observation reaction is not an original essence; reflexivity never authorizes hiding or suppressing observation or handling the object; separate sustained observation, repeated stimulus, and common change |
| C10 human carrying and cross-time reproduction | G2 + H2 classification of carrier, like-cost bearer, beneficiary, stop holder, and responsible subject. `C10-current`; `C10-carried-reproduction`; `C10-intertemporal` (G3); `C10-historical-carrier` (G3 + H5) | Ability to carry is not a duty to carry; the most visible executor is not the responsible subject; H2 classification is an operating gate, not a reproduction mechanism; no chain authorizes a subject's sacrifice, continuation, or exit |
| C11 institutional writeback | D2 + G2 return channel + H3 classification of receipt, field change, execution, and duration | An appeal or audit entrance is not effective writeback; one writeback is not lasting repair or improvement; writeback proves no legitimacy and widens no authority |
| C12 normative bridge | N1 + O1-O4 with the ten bridge components enumerated canonically in choice-and-authorization.md (owned by `ariadne-choice`), the protection floor item by item, and PF-1 to PF-10 | A procedural gate, not empirical evidence. All components passing forms a bounded proposal that may enter real adoption; an analytic recommendation for deliberation needs explicit norms, evidence, and costs but not yet-granted execution authority; N1 alone can only block overreach and never yields a positive proposal |

**Condition trees** (§4.15). G1 + bridge + G2 gives a channel candidate; adding return and blockage gives effective feedback; adding the carried route gives carried learning, or adding G3 gives increment learning. Adding G4 with D3/E5 gives a closure-failure or conversion candidate. G2 with a like-quantity mapping gives instant overload, then carried or increment accumulation. D1 with variation, differential result, retention, next round, repeated rounds, and drift competitors gives a pattern, then G2 for a mechanism or G3 for a cross-round path. Listing instance names never makes a mechanism sufficient. When conditions are incomplete, name the gap and the conclusion it blocks without withdrawing independently grounded findings. Even G1-G4 all passing yields no S0-S6 stage, direction, value, responsibility, selection, or authorization.

## Per-Proposition Downgrade

A downgrade is registered per proposition, with its dependencies and the impact of the missing item (§2.9, §13.1). Claims with independent grounds keep their level; a failed global source, shared premise, or object boundary blocks every related output. In the Method Record this is checked mechanically:

- every `depends_on` entry names a claim that appears earlier in the same ledger;
- a claim whose dependency is `contradicted`, `withdrawn`, or `retired` cannot be `supported`;
- a claim's own `ceiling`, when present, never exceeds the ceiling of any dependency or the record's `output_ceiling`.

The conclusion steps down from candidate hypothesis to question list to description only as critical variables, non-applicability handling, or core-channel visibility fail. Renaming a claim, splitting it, or moving it to another branch never restores its ceiling.

## Method Record Update

- Keep the frozen object and task profile in `object_contract`; do not silently refine either after viewing evidence.
- List only included sources in `evidence_cutoff` and preserve the cutoff timestamp.
- Put each split D/G/E/H/N/O/F claim in `claim_ledger` with explicit support, counterevidence, and `depends_on` IDs.
- Put competitors, residuals, missing observations, invalid bridges, and protected opacity in `unknowns_and_counterevidence`.
- Set each claim's level by its weakest critical dependency, and the record ceiling by the claims the output actually rests on. A normal child applies the minimum of that ceiling and its parent. Raise only in a child that newly admits named external evidence or a newly fulfilled declared protocol; module completion never raises.
- Add `ariadne-evidence` to `module_runs`, route scale and representation questions to `ariadne-scale`, and keep `authorization_effect: none`.

## Strong Example

Request: "Response time fell 20% after our team adopted a chat tool, so the tool caused the improvement and every department should adopt it."

Split the statement before auditing it:

- D: what counts as response time and which messages are included;
- E: the pre/post dashboard and its measurement limits;
- G: the tool caused a change in the target transition (depends on D and E);
- N: faster response is prioritized over competing values;
- O: every department should adopt the tool (depends on G and N).

The dashboard is material. Its time-stamped records can become observations for a defined metric, and the observed decrease can stand as an observation in its own right. Without a frozen comparison, channel test, and competitors such as staffing, workload, seasonality, message mix, and measurement change, it does not identify the tool as the cause. The adoption sentence additionally lacks values, local feasibility, authorization, stopping, rollback, and remedy, so it falls with the causal claim it depends on while the observed decrease keeps its own standing.

<!-- method-record-example:start -->
```yaml
record_id: ariadne:chat-response-audit:root:v1
schema_version: '2.0'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: diagnosis
object_contract:
  boundary: One support team's work-message intake and response workflow; other departments are outside the audited
    object.
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
    aggregation: messages aggregated to team-week summaries
    space: one support team
    time: sixteen-week pre/post window
    organization: single team
    causal_level: candidate channel effect
    observation_resolution: message records and weekly summaries
    impact: team and its incoming customers
    network: message-routing network
    jurisdiction: 'not_applicable: no action authorization is evaluated in this evidence audit'
  identity_criterion: The same workflow while message definition, staffing unit, and response rule remain comparable.
  task_profile:
    target_query: Whether the chat tool caused the response-time decrease in this team
    horizon: The sixteen-week pre/post window
    environment: This team's staffing, message mix, and dashboard protocol
    allowed_operations: Observation and record review only
    error_tolerance: Direction of effect with stated alternatives; no effect-size estimate
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
  transform_kind: scale
  transform_status: failed
claim_ledger:
- claim_id: D-response-time
  claim_type: D
  text: Response time requires a frozen message inclusion and first-response rule.
  status: candidate
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
- claim_id: E-observed-decrease
  claim_type: E
  text: The exported dashboard shows a lower weekly median response time after adoption under its current protocol.
  status: observed
  support_ids:
  - source:team-dashboard-export
  counterevidence_ids: []
  support_rule_ids: []
  depends_on:
  - D-response-time
- claim_id: G-tool-cause
  claim_type: G
  text: The chat tool caused the observed response-time decrease.
  status: unresolved
  support_ids:
  - E-observed-decrease
  counterevidence_ids:
  - alternative:staffing-workload-seasonality-measurement
  support_rule_ids: []
  depends_on:
  - D-response-time
  - E-observed-decrease
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
  depends_on:
  - G-tool-cause
  - N-speed-priority
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
    record_id: ariadne:chat-response-audit:root:v1
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

The bounded result is: a pre/post decrease was observed under an incompletely specified metric; causality and cross-department transfer remain unresolved; universal adoption is neither supported nor authorized.

## Chained Virtual Instances m1-m4

These virtual instances describe a fictional multi-layer transport model that cites no external observation; they only show how instance contracts chain and give no empirical support to any G claim (§4.7).

| Instance | Candidate object | Preselected criterion | N0 | Fails when |
|---|---|---|---|---|
| m1 / G1a | Interconnected unit groups with frozen B, X, T, SP, K, and grouping | `out_of_sample_predictive_gain` | Complexity-matched baseline without the grouping | Gain holds only in training data, dies under slight boundary perturbation, or fails the independent time block |
| m2 / G2a | One conduction channel and target transition on m1's object | `controlled_perturbation_effect` | Controlled blockage leaves the target transition below threshold | The blockage does not move the transition above threshold; success registers the channel only as a candidate causal carrier with delay measured, leaving capacity, reliability, controllability, and loss unknown |
| m3 / G3a | History variable "backlog over the previous three rounds" on the same object | `historical_conditional_predictive_gain` | Current queue, environment input, and measurement protocol suffice | History adds no out-of-sample increment after controls, or causal path dependence is claimed without a preselected erasure, restoration, or equivalent intervention |
| m4 / G4a | Micro-to-aggregate mapping M with frozen retained and excluded variables | `conditional_information_gain` | Excluded local timing adds no above-threshold conditional information given the aggregate variables | The increment stays below threshold, or the criterion is switched to prediction, intervention, or G4b conversion after results |

The four instances feed one another follow-up questions but never substitute for one another: m1 passing does not guarantee m2's channel effect, m2 passing does not guarantee m3's history increment, and m3 passing does not guarantee m4's closure failure. If m3 fails, the backlog's carried effect through the current queue is still an open carried-route question, not a refuted one.
