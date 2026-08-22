# Mechanism Contracts

## Boundary and Record Discipline

Use this module to organize conditional structural explanations, not to certify a world ontology, infer values, or authorize action. Treat every structural name as a candidate until an eligible external instance supports it.

For a standalone run, create the common Method Record and make these module-specific additions:

- Set `request_type` to the actual output class, normally `explanation` or `diagnosis`.
- Put `S*=<B,X,R,I,T,SP,K>` and the target residual in `object_contract`.
- Freeze source and observation availability in `evidence_cutoff`.
- Put the active scale profile and generalization unit in `scale_scope`.
- Put bounded claims in `claim_ledger`; put every mechanism candidate's channel observation, discriminating prediction, reverse or falsifier, and residual comparison rule in the typed mechanism payload.
- Preserve missing fields and competing accounts in `unknowns_and_counterevidence`.
- Apply the ordered ceiling transition algebra. A normal module child preserves or lowers; only newly admitted external evidence or protocol fulfillment in a child can raise.
- Append this run to `module_runs`, name only useful handoffs in `recommended_next_modules`, and set `authorization_effect: none`.

Create a child record instead of overwriting a parent whenever evidence, scope, object identity, or a frozen comparison changes.

## D0-D3 Structural Grammar

| Contract | Register | Do not infer |
|---|---|---|
| D0 structural object | `S*=<B,X,R,I,T,SP,K>`: boundary, registered state variables, relations or transition constraints, interfaces, time window, scale profile, and identity criterion | Object validity, a natural boundary, a shared subject, or empirical support. Freeze `N0` only inside a concrete G-instance. |
| D1 state terms | Detectable change; operation while `B/R/I/SP/K` hold; persistence of `K`; evolution as above-window contract change; dissolution when old `K` fails; repair toward a declared `K*` or `F*` | Direction, maturity, progress, path dependence, selection, failure, repair value, or permission to repair. |
| D2 effective feedback | Prior state or output, return channel, receiving location, changed downstream field, timing, and no-return or blocked comparison | That receipt, acknowledgement, storage, one update, benefit, learning, or repair has occurred. |
| D3 scale transformation | `M(SP0->SP1)=<preserved, changed, lost, operator, error, validity range>` and whether `K` survives | That shared vocabulary proves successful transfer, that aggregation is simple enlargement, or that a larger scope grants wider jurisdiction. |

Keep representation or statement translation distinct from scale transformation, circle-relation change, propagation, compression, and analogy. Record the source expression and context, target circle and task, translator or rule and version, preserved and allowed changes, collapsed distinctions, omissions, additions, ambiguity, error, lineage, target-side review, validity, failure, and withdrawal. Without target-side review, label the translation pending.

## U01-U11 Primitive Scan

Use primitives as interface positions. Do not treat their presence as evidence.

| Primitive | Minimum registration | Boundary |
|---|---|---|
| U01 candidate-object interface | Complete D0 fields, object ID, scale traceability | Keep the object candidate until a G1-instance supplies finite support. |
| U02 boundary and interface | Inside/outside rule; moving, porous, nested, or overlapping boundary; filtering, delay, conversion, or blocking interface | Do not infer closure, common identity, or control from a boundary or interface. |
| U03 state and observable | Variable, observable, observation position, resolution, and error | Measurement is not the whole state; unobserved is not absent. |
| U04 component, carrier, substrate | Constituent, actual causal carrier, and enabling substrate | A component need not be the carrier; a carrier is not thereby intentional or responsible. |
| U05 relation and constraint | Endpoints, direction, window, and the feasible states or transitions changed | Correlation, adjacency, or co-occurrence is not a causal constraint. |
| U06 flow, channel, conduction | What moves, source, target, direction, rate, distribution, carrier path, capacity, delay, reliability, controllability, and loss by measured dimension | Keep unmeasured dimensions unknown and require G2 for a channel effect. |
| U07 feedback and update | Return relation and downstream update as separate records | A one-way process is not feedback; feedback is not learning or repair. |
| U08 condition and environment | Local enabling condition or external variable plus the interface through which it acts | Do not personify the environment or make it a total cause. |
| U09 load, capacity, recovery margin | Typed units, location, distribution, window, bottleneck, replenishment, substitution, and recovery margin | A momentary gap is not cumulative damage and creates no duty to continue carrying it. |
| U10 trace, memory, path | Trace carrier and persistence; whether the trace enters later transitions; whether history adds information after current state | Storage is not memory-in-use; path difference is not destiny or irreversibility. |
| U11 phase, transition, dissolution | Same `K`, preregistered state regions, threshold, noise and binning robustness; or failed `K` | A phase is not an S0-S6 rank or a universal sequence. Failed `K` means conversion or dissolution, not phase change. |

Close the scan minimally: U01-U03 identify what is being tracked and observed; U04-U06 locate implementation and transmission; U07-U10 locate return, conditions, load, and history; U11 distinguishes operation region from transition, conversion, and dissolution. Mark every missing position explicitly.

## Root-Instance and Evidence Discipline

Separate every root instance into an immutable preregistration segment and an append-only result segment. Freeze before results: instance and contract identity, candidate object, `SP/T/K`, target variables, exactly one subtype and one allowed success criterion, candidate specification, complexity-matched zero model, controls, model classes, sampling and generalization units, primary metric or aggregation, model selection or ensemble rule, multiple-comparison rule, positive decision rule, null decision rule, evidence mode, falsifier, pause condition, and deviations.

Use only four result states: `supported`, `unsupported_or_undecided`, `null_supported`, and `not_evaluated`. Require an eligible confirmatory or replication instance, a frozen-before-evidence contract, completion from that contract, a passed positive rule, resolvable evidence, and analysis artifacts for positive support. Use exploratory or post-result-deviated runs only to generate candidates. A failed positive rule does not support the null. Require the frozen equivalence or sufficiency test, power or sensitivity gate, and tolerance to all pass before `null_supported`.

| Root | Ask | Finite supported output |
|---|---|---|
| G1 | Does a candidate grouping beat a complexity-matched no-group baseline out of sample and survive boundary perturbation plus independent time or place replication? | Object-recognition strength, boundary credibility, and applicability window within frozen `SP/T/K` and generalization unit. |
| G2 | Does one preregistered perturbation, intervention, or identified natural variation change a specified transition through a specified channel beyond threshold? | Candidate causal carrier and only the separately measured channel dimensions. |
| G3 | Does a predeclared historical term add out-of-sample information after controlling current registered state, environment, and measurement? Does a separately chosen history intervention change the result? | Predictive path difference for G3a; causal path difference for G3b. Never destiny or absolute irreversibility. |
| G4 | Does an excluded-scale variable add conditional information, prediction, or intervention gain, or does a frozen mapping show exactly one preselected failure among object-dynamics non-commutation, intervention non-commutation, identity-criterion violation, effective-relation change, and intervention-response change? Never merge the five G4b criteria into one disjunctive fallback. | Criterion-bounded closure failure for G4a or one preregistered object/intervention conversion for G4b. |

Apply E1 before judgment by declaring object, scale, window, variables, zero model, and identity. Apply E2 by recording observation position and model limits. Apply E3 only when observation, naming, scoring, or publication reaches the object through an actual causal channel. Apply E4 by retaining a distinguishable competitor, counterexample, and residual. Apply E5 by auditing the D3 mapping, invariants, changes, losses, error, competitors, and residuals. Treat these as method gates, not empirical causes.

## C1-C12 Inference Ceilings

| Contract | Hard inferential requirements | Highest permitted conclusion before later normative and authorization layers |
|---|---|---|
| C1 object and boundary | D0 plus eligible supported G1 | Finite object-recognition and boundary strength in the frozen scope; no ultimate ontology, subject, goal, value, or authority. |
| C2 carrier and channel | D0 plus eligible supported G2; typed quantities, units, window, accounting boundary, and conversion map | Candidate carrier and measured channel limits; keep unmeasured dimensions unknown and carriers separate from responsibility. |
| C3 feedback and learning | D2 plus G2 for feedback; add G3, retained update, repeated rounds, and predefined task comparison for learning | Effective feedback, or the narrower feedback-mediated learning candidate. |
| C4 history and path | D1 plus G3; add public `K*` or `F*` and timing comparisons for a repair window | Predictive or causal path difference; conditional repair window only with its extra contract. |
| C5 load and recovery | D0 plus G2 and typed demand-capacity mapping; add G3 and history carrier for cumulative damage | Instantaneous gap, or the narrower cumulative-damage or delayed-recovery candidate. |
| C6 scale closure or conversion | D3 plus exactly one eligible G4 subtype and criterion | One bounded closure failure or one bounded object/intervention conversion; zero conclusions require the passed null rule. |
| C7 local change and spillover | G2 plus G4, frozen local and external variables, temporal mechanism bridge, and blocking or substitution counterfactual | Cross-boundary spillover and its distribution; call it an externality only under an explicit institutional or accounting definition. |
| C8 variation-selection-reproduction | D1 plus preregistered variation `V`, differential result `D`, retention `R`, next-round entry, repeated rounds, and drift competitors; add G2 for a carrier | Selection pattern, or a specified retention/reproduction mechanism. No superiority, intentional choice, or governance follows. |
| C9 observation and reflexivity | G2 and an actual observation channel with timing and no-observation, alternative-observation, or blocked counterfactual; add G3 for persistence | Channel-bounded observational participation or reflexive response; persistence only with history support. |
| C10 human carrying | G2 plus H2 separation of carrier, typed cost bearer, beneficiary, stop right, and responsible subject; add G3 for intertemporal reproduction and H5 for a historical carrier | Current carrying chain, intertemporal candidate, or bounded historical-carrier account. No sacrifice duty follows. |
| C11 institutional writeback | D2 plus G2; use H3 to separate receipt, field change, execution, and duration | Receipt, record update, execution, effective writeback, and duration as distinct states. One writeback is not learning or legitimacy. |
| C12 normative bridge | N1 and O1-O4, explicit runtime normative premises and conflicts, protection floor, atomic jurisdiction, no-action option, monitoring, stop, appeal, rollback, remedy, expiry, and reauthorization | Only a bounded recommendation after every gate. This module may report missing requirements but never supply authorization. |

## Conditional Mechanism Contract

For every candidate CM, record:

1. Object, `SP/T/K`, target transition, evidence cutoff, and generalization unit.
2. Formal inferential dependencies separately from protocol gates.
3. Enabling conditions, typed variables, mechanism chain, direction, timing, threshold, and measured dimensions.
4. Minimum external evidence and eligible instance references.
5. Complexity-matched simple baseline and at least two competing mechanisms for every causal or analogy route.
6. For every candidate: a channel observation, discriminating prediction, reverse condition or falsifier, and a residual comparison rule under the same cutoff and baseline.
7. Blocking, substitution, or no-channel counterfactual; counterexamples, failure boundary, output ceiling, and next discriminating observation.

| Mechanism | Required branch conditions | Downgrade or reject when |
|---|---|---|
| CM-FEEDBACK | D2 + G2; prior output returns through a specified channel and changes a later field beyond threshold versus no-return or blocked condition | A signal only arrives, a common input explains the change, or blocking the return leaves the difference intact. |
| CM-LEARNING | CM-FEEDBACK + G3; a localized update persists, enters repeated later rounds, adds history information, and changes a predefined task result against baseline | The update is not retained, does not enter later rounds, current state absorbs history, or only a proxy improves. |
| CM-MAINTENANCE-current | D0 + G2; replenishment, replacement, correction, or removal changes preservation of declared `K/F` in the window; compare maintained, reduced, mistargeted, and stopped maintenance conditions | The object persists without it, the input has no effect, or old `K/F` is used after identity changed. |
| CM-MAINTENANCE-cumulative | Current branch + G3 for wear history or delayed recovery | No historical increment remains after current state or an independent shock explains the pattern. |
| CM-LOAD-instant | D0 + G2; same-type or mapped demand and capacity measured at the same location and window | Units, locations, or windows are incomparable, capacity expands with demand, or no immediate gap exists. |
| CM-LOAD-cumulative | Instant branch + G3 showing history changes later capacity or recovery | The gap clears without later difference. Keep surface output, `K/F`, and internal margin recovery separate. |
| CM-PHASE-pattern | D0 + D1; same `K`, at least two reproducible operating regions, preregistered variables and threshold, noise and bin robustness | A continuous trend suffices, the threshold follows arbitrary bins, or `K` failed before transition. |
| CM-PHASE-causal-trigger | Pattern + G2 for the selected trigger channel | The selected perturbation or identified variation does not change the transition. |
| CM-PHASE-hysteretic | Pattern + G3 for lag, history, or delayed recovery | Current state absorbs the history term. Do not require G3 for a reversible base pattern. |
| CM-SELECTION-pattern | D1 + `V/D/R`, next-round entry, repeated rounds, and drift/common-cause/sampling competitors | There is only change, one differential result, no retention, no next round, or drift suffices. |
| CM-SELECTION-carrier | Pattern + G2 for a specified retention or reproduction channel | Perturbing the candidate carrier leaves retention unchanged. |
| CM-SELECTION-history | Pattern + G3 for cross-round history after current-state control | No conditional history increment remains. |
| Coevolution candidate | Separate D0 and `K` for both objects, two directional G2 channels, timing and speed differences, and a shared-environment competitor; add G3 for lock-in | Change is one-way, caused by a common environment, or the objects lose independent identity. |

Treat dissolution as failed old `K`; distinguish termination from conversion to a new object. Mistargeted maintenance can extend the old `K` while destroying the declared `F`; an ordered stop, object conversion, or dissolution can be a contract-permitted outcome. Define repair against a preregistered `K*` or `F*`, compare timing when claiming a repair window, and add G3 for historical restriction. Keep whether to repair, who chooses the target, who bears responsibility, and who may act outside this module.

## Clocks and Cross-Circle Cascades

Assign each mechanism an update clock and every clock crossing a carrier, execution step, confirmation, and failure condition. At minimum distinguish immediate, interaction, organizational, institutional, and long-term clocks. Do not equate signal receipt with organizational change, a decision with execution, a rule text with local writeback, or short-term compliance with long-term retention.

Register a cascade only when a local change reaches another circle through member overlap, a bridge, shared resources, network propagation, or institutional descent. Recheck object, channel, scale, timing, and evidence at every hop. Allow capacity, filtering, delay, cancellation, and local exclusion to terminate the cascade. Register coevolution only when at least two objects retain distinct `K` and mutually alter one another's feasible paths or constraints.

## Comparison Output

For each target residual, present the simple baseline first, then a compact comparison:

| Field | Required content |
|---|---|
| Residual | The exact observation or difference left unexplained by the baseline |
| Candidate | One named contract, not a narrative label |
| Chain | Source -> carrier -> intermediate change -> target change |
| Support | Eligible instance and measured dimensions, or explicit missing state |
| Competitor | A distinguishable alternative and its expected signal |
| Falsifier | An observation that downgrades or rejects the candidate |
| Scope | `SP/T/K`, generalization unit, and output ceiling |
| Residual after fit | What the candidate still does not explain |

Retain multiple candidates when present evidence cannot distinguish them. Prefer the simple baseline when added mechanisms do not improve out-of-sample explanation or intervention performance.

In the typed payload, every candidate separately fills `channel_observation`, `discriminating_prediction`, `reverse_or_falsifier`, and `residual_comparison_rule`. Candidate IDs and the four-field test signatures must be distinct; relabeling the same story does not create a competitor.

## Worked Example: Complaint Receipt, Writeback, or Learning

Suppose an organization receives a complaint and immediately emits a receipt. Freeze the complaint process object, case fields, organization scale, observation window, and evidence cutoff. Use “automatic receipt with no downstream change” as the simple baseline.

The receipt alone supports only signal arrival. Add a CM-FEEDBACK candidate only if the complaint returns through a specified channel, a named case or rule field changes afterward, and a no-return or blocked-channel comparison distinguishes the change from a parallel management instruction. Keep “independent management instruction changed the field” as a competing mechanism.

If the field changes but no execution record exists, distinguish effective feedback from C11 institutional writeback. If execution occurs, record receipt, field change, execution, and duration separately. Do not call the organization learning yet. Add CM-LEARNING only after a retained rule or state update enters repeated later cases and an eligible G3-instance shows historical conditional gain on a predefined task against the baseline.

Record the result as follows: put the receipt and any field-version evidence in `claim_ledger`; put blocked-channel comparison, execution, retention, repeated-round evidence, and the competing instruction in `unknowns_and_counterevidence`; set `output_ceiling: diagnostic_only`; recommend evidence repair or human-domain writeback analysis only if needed; and set `authorization_effect: none`. The result may distinguish arrival, feedback, writeback, and a learning candidate. It cannot certify institutional legitimacy, assign blame, require a remedy, or authorize a rule change.
