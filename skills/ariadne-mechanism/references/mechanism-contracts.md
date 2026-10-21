# Mechanism Contracts

Section anchors (§) point to the source text named in `ariadne-skill/references/source-navigation.json`.

## Boundary and Record Discipline

Use this module to organize conditional structural explanations, not to certify a world ontology, infer values, or authorize action. Operation, feedback, learning, maintenance, load, phase, and selection are not interchangeable narrative words: each is a conditional mechanism with its own inferential premises, enabling conditions, counterfactual, and stopping place. A name is never a sufficient condition; a mechanism instance is registered in a stated SP/T/K only when dependencies, conditions, minimum evidence, and competitors all pass (§6 opening).

For a standalone run, create the common Method Record and make these module-specific additions:

- Set `request_type` to the actual output class, normally `explanation` or `diagnosis`.
- Put `S*=<B,X,R,I,T,SP,K>`, the task profile, and the target residual in `object_contract`.
- Freeze source and observation availability in `evidence_cutoff`.
- Put the active scale profile, transform kind, and generalization unit in `scale_scope`.
- Put bounded claims in `claim_ledger` with `depends_on`; put every mechanism candidate's temporal route, channel observation, discriminating prediction, reverse or falsifier, and residual comparison rule in the typed mechanism payload.
- Preserve missing fields and competing accounts in `unknowns_and_counterevidence`.
- Apply the ordered ceiling transition algebra. A normal module child preserves or lowers; only newly admitted external evidence or protocol fulfillment in a child can raise.
- Append this run to `module_runs`, name only useful handoffs in `recommended_next_modules`, and set `authorization_effect: none`.

Create a child record instead of overwriting a parent whenever evidence, scope, task, object identity, or a frozen comparison changes.

## D0-D3 Structural Grammar

| Contract | Register | Do not infer |
|---|---|---|
| D0 structural object | `S*=<B,X,R,I,T,SP,K>` plus the task the object must serve (target query, horizon, environment, allowed operations, error) | Object validity, a natural boundary, a shared subject, empirical support, or sufficiency for another task. Freeze `N0` only inside a concrete G-instance. |
| D1 state terms | Detectable change; operation while `B/R/I/SP/K` hold; persistence of `K`; evolution as above-window contract change; dissolution when old `K` fails; repair toward a declared `K*` or `F*` | Direction, maturity, progress, path dependence, selection, failure, repair value, or permission to repair. |
| D2 effective feedback | Prior state or output, return channel, receiving location, changed downstream field, and a detectable difference against no return or blocked return | That receipt, acknowledgement, storage, benefit, learning, repair, or stability has occurred. |
| D3 scale transformation | `M(SP0->SP1)=<preserved, changed, lost, operator, error, validity range>`, the task each sufficiency claim refers to, and whether `K` survives | That shared vocabulary proves transfer, that static adequacy gives dynamic or intervention adequacy, or that a larger scope grants wider jurisdiction. |

D2 keeps action, stability, and goal improvement apart (§3.3). A claim of correction states the target deviation, gain, execution delay, working range, and instability criterion; a claim of improvement also evaluates transient peaks, cost, and distribution. Fixed rules can form feedback. The phrase "negative feedback" never generalizes into real-world self-stabilization.

Keep representation or statement translation distinct from scale transformation, circle-relation change, propagation, compression, and analogy; its audit belongs to `ariadne-scale`.

## U01-U11 Primitive Scan

Use primitives as interface positions. Their presence is not evidence, and they are not claimed to be logically independent, unique, or complete; a task may use a sufficient subset or add domain variables with a reason (§3.5-3.6).

| Primitive | Minimum registration | Boundary |
|---|---|---|
| U01 candidate-object interface | Complete D0 fields, object ID, scale traceability | Keep the object candidate until a G1-instance supplies finite support. |
| U02 boundary and interface | Inside/outside rule; moving, porous, nested, or overlapping boundary; filtering, delay, conversion, or blocking interface | Spatial proximity is not a shared boundary; a boundary is not closure; an interface is not one side's control. |
| U03 state and observable | Variable, observable, observation position, resolution, and error | Measurement is not the whole state; unobserved is not absent; records can contain the measuring process's own contribution. |
| U04 component, carrier, substrate | Constituent, actual causal carrier of the specified transition, and enabling substrate | A component need not be the key carrier; replacing components can keep K; a carrier is not thereby intentional, responsible, or obliged to keep carrying. |
| U05 relation and constraint | Endpoints, direction, window, and the feasible states or transitions changed | Correlation, adjacency, or co-occurrence is not a causal constraint; a constraint is not legitimate by existing. |
| U06 flow, channel, conduction | What moves, source, target, direction, rate, distribution, carrier path, and capacity, delay, reliability, controllability, and loss by measured dimension | Keep unmeasured dimensions unknown; a channel effect needs a G2-instance; a channel is not a responsible subject. |
| U07 feedback and update | Return relation and downstream update as separate records | Feedback is not learning or repair; carried learning follows the carried route, and only increment learning needs G3. |
| U08 condition and environment | Local enabling condition or external variable plus the interface through which it acts | Do not personify the environment or make it a total cause; a scale change redraws the object-environment boundary. |
| U09 load, capacity, recovery margin | Typed units, location, distribution, window, bottleneck, replenishment, substitution, and recovery margin | A momentary gap is not cumulative damage and creates no duty to continue carrying it. |
| U10 trace, memory, path | Trace carrier and persistence; whether the trace enters later transitions; the carried route for current-carrier effects; G3 only for an increment beyond the current registered state | Storage is not memory-in-use; path difference is not destiny or irreparability. |
| U11 phase, transition, dissolution | Same `K`, preregistered state regions, threshold, noise and binning robustness; or failed `K` | A phase is not an S0-S6 rank or a required stage; triggers need G2, carrier persistence the carried route, and only an increment beyond the current representation G3. Failed `K` means conversion or dissolution. |

Close the scan minimally: U01-U03 identify what is being tracked and observed; U04-U06 locate implementation and transmission; U07-U10 locate return, conditions, load, and history; U11 distinguishes operation region from transition, conversion, and dissolution. Mark every missing position with one of the four missing states and state its effect on the ceiling; never fill a contract from natural-language familiarity.

## Operation and Temporal Routes

Register an operation as input, named carrier or channel, state transition, output, environmental condition, window, and possible trace; if output returns, add the return channel, receiving location, and changed field (§6.1). For every cross-time claim, first separate the three history questions owned by `ariadne-evidence`: formation of the current state, transmission through a current carrier, and an increment beyond the current representation. Only the increment claim compares a history-aware model with a current-state-sufficient model. Cross-scale claims complete D3/E5.

Every typed mechanism candidate declares one `temporal_route`:

| Route | Use when | Evidence it needs |
|---|---|---|
| `current_state` | The mechanism acts within the window through present conditions only | Channel evidence for the present transition |
| `carried_history` | Earlier inputs act through a measured current carrier that is retained or updated and goes on to affect the result | Carrier measurement, entry grounds, retention or update, longitudinal material; causal claims add interruption, replacement, restoration, or natural variation |
| `historical_increment` | History is claimed to add information or effect beyond the current registered representation | An eligible G3-instance; never created by omitting a known current state |
| `not_applicable` | The candidate makes no cross-time claim | A reason |

Never switch route after results to rescue a candidate. The carried route can hold while G3 fails, and a failed G3 never refutes the carried route.

## Instance and Evidence Discipline

The frozen questions, pass rules, result states, and non-inference boundaries for G1-G4, E1-E5, and C1-C12 are owned by `ariadne-evidence` in evidence-contracts.md; consume recorded instance results instead of re-deriving or re-wording them here. What a supported instance unlocks for mechanism work:

| Family | A supported instance unlocks |
|---|---|
| G1 | Object-recognition strength, boundary credibility, and applicability window within frozen `SP/T/K` and generalization unit. |
| G2 | Candidate causal carrier and only the separately measured channel dimensions. A qualified total-effect comparison without channel separation keeps the total effect and leaves the channel unresolved. |
| G3 | Predictive (G3a) or causal (G3b) path difference beyond the current representation. Never destiny, absolute irreversibility, or a verdict on history's formative role. |
| G4 | Criterion-bounded closure failure (G4a) or one preregistered object or intervention conversion (G4b), relative to stated targets, horizon, environment, and operations. |

Use only four result states: `supported`, `unsupported_or_undecided`, `null_supported`, and `not_evaluated`. A failed positive rule does not support the null. General learning, lasting burden, or historical causation can still be supported by independent domain evidence without a formal mechanism instance; report "the practice changed", "net later effect undetermined", and "feedback-mediated mechanism unidentified" side by side when that is what the material shows.

## Result Contracts in Mechanism Work

The full C1-C12 table lives in evidence-contracts.md. In mechanism work, apply its branches without merging them:

- C3: `C3-feedback`, `C3-carried-learning`, `C3-learning` (increment, with G3).
- C4: G3 branch, carried and timing branches, repair window with public K*/F* and intervention-time comparison.
- C5: `C5-instant`, `C5-carried-cumulative`, `C5-cumulative` (G3).
- C8: `C8-pattern`, `C8-mechanism` (G2).
- C9: `C9-response`, `C9-carried-persistence`, `C9-persistent` (G3).
- C10: `C10-current`, `C10-carried-reproduction`, `C10-intertemporal` (G3), `C10-historical-carrier` (G3 + H5).
- C11: receipt, field change, execution, and duration as distinct states.
- C12: the normative bridge enumerated canonically in choice-and-authorization.md (owned by `ariadne-choice`); this module may report missing requirements but never supplies authorization.

## Conditional Mechanism Contract

For every candidate CM, record:

1. Object, `SP/T/K`, task, target transition, evidence cutoff, and generalization unit.
2. Formal inferential dependencies separately from protocol gates.
3. Enabling conditions, typed variables, mechanism chain, direction, timing, threshold, measured dimensions, and temporal route.
4. Minimum external evidence and eligible instance references.
5. Complexity-matched simple baseline and at least two competing mechanisms for every causal or analogy route when the material allows them; otherwise the search range and failure conditions.
6. For every candidate: a channel observation, discriminating prediction, reverse condition or falsifier, and a residual comparison rule under the same cutoff and baseline.
7. Blocking, substitution, or no-channel counterfactual; counterexamples, failure boundary, output ceiling, and next discriminating observation.

| Mechanism | Required branch conditions | Downgrade or reject when |
|---|---|---|
| CM-FEEDBACK | D2 + G2, not G3: prior state or output -> return signal -> named channel -> uptake at the receiving location -> later state, probability, or constraint changes, checked against blockage | A signal only arrives, a common input explains the change, or blocking the return leaves the difference intact. |
| CM-LEARNING-carried | CM-FEEDBACK; a locatable internal update is retained or keeps updating, later rounds actually invoke it, and a predefined task result changes; causal claims compare interruption, replacement, restoration, or identified variation and handle common inputs, continued training, selection, attrition, and measurement change | One parameter change, one success, one writeback, or one archive entry; transfer or predictive gain without an independent task or out-of-sample evaluation. |
| CM-LEARNING-history | Carried branch + an eligible G3-instance | The current carrier already holds what was learned (the increment can vanish while carried learning stands); never delete the known carrier to manufacture an increment. |
| CM-MAINTENANCE | D0 + G2; a predeclared K or function F and maintenance window; replenishment, replacement, correction, or removal identified as changing K/F persistence; compare maintained, reduced, mistargeted, and stopped maintenance. Branches `-current`, `-carried-cumulative`, `-cumulative` (G3) | The object keeps without it, maintenance changes do not move results, an independent shock explains wear, or old K/F is used after identity changed. |
| CM-LOAD | D0 + G2; like or mapped demand and capacity at the same location and window, reported by position and distribution, not only on average. Branches `-instant`, `-carried-cumulative`, `-cumulative` (G3) | Units, locations, or windows are incomparable, capacity expands with demand, or no immediate gap exists; load need not accumulate monotonically and instant overload need not cause damage or collapse. |
| CM-PHASE | D0 + D1 with E4 and EVIDENCE as gates. Branches `-pattern` (same K, two reproducible regions, preregistered threshold), `-causal-trigger` (+ G2), `-carried-persistence` (carried route), `-hysteretic` (+ G3); causal readings add CAUSAL | A continuous trend suffices, the threshold follows arbitrary bins, or K failed before transition; the same curve shape never proves any route. |
| CM-SELECTION | D1. Branches `-pattern` (V, D, R, next round, repeated rounds, drift competitors), `-carrier` (+ G2), `-history` (+ G3) | Only change without D, one differential result without R or later rounds, drift suffices, or perturbing the reproduction channel leaves retention unchanged. |
| Coevolution candidate | Separate D0 and K for both objects, two directional G2 channels, timing and speed differences, and a shared-environment competitor | Change is one-way, caused by a common shock, synchronized only in measurement, or one object loses independent identity (record nesting or conversion). |

### Feedback Delay and Stability

Effective feedback is not stability (§6.2.1, Appendix C.10). For x_{t+1} = x_t - k*x_{t-d} with fixed delay d, the zero solution is asymptotically stable for every initial history exactly when 0 < k < 2 sin[pi/(4d+2)]. With k = 0.8, delays 0 and 1 are stable while delays 2 and 3 (critical gains about 0.618 and 0.445) are not, although all four return the same first-step correction. Stability still says nothing about transient peaks, cost, human acceptability, or real repair. Time-varying delay, noise, nonlinearity, and execution limits need fresh analysis, and the formula never sets an unidentified real correction gain.

### Learning Evaluation

Keep three outcomes apart (§6.3): completing the task with support, independent transfer after support is withdrawn, and later life outcomes. Necessary support can be part of the task; failure without support does not cancel earlier success; withdrawal comparisons are needed only when independent transfer is the stated goal. Continued support never denies an acquired function, and assisted results never stand in for independent skill. When the goal changes, state why and who decided, keep results, failures, and costs under the old goal, and build a new comparison; a later reconstructed goal never rewrites an old failure as success. Effective feedback, general learning, cross-context transfer, and net benefit are judged separately, and learning does not mean becoming better, a unified goal, or permission to act.

### Receipt, Feedback, Writeback, Learning

Evidence gates rise step by step (§6.4): a receipt with no field change is signal arrival only; a field change without execution is D2 feedback but not complete H3 writeback; a field change that enters execution with receipt, change, execution, and duration recorded is one institutional writeback (not legitimacy or lasting repair); a retained rule entering later similar cases, with task comparison and causal grounds, is a carried feedback-mediated learning candidate; a historical increment additionally needs G3.

### Maintenance and Redundancy

Separate tasks during normal running, migration, failure, and recovery. An interface standard is not actual compatibility (implementation version, business semantics, environmental load, testing, field fit). A spare part existing is not correct specification, verifiable quality, staff able to arrive, or the right to shut down. Maintenance growth may land outside the object (users, households, contractors, other agencies), so central work orders do not measure total maintenance. **Test redundancy by failure conditions**: two paths may share power, software state, transport, supplier, operator, or approval node; verify standby capacity, common-cause exposure, switching time, field skill, and the actual right to switch, and put the communications, roads, fuel, parts, and people that recovery depends on into the same window. Needing maintenance is not a duty to persist forever, a maintenance channel names no carrier or sacrifice duty, and an ordered stop, conversion, or dissolution can be a permitted outcome.

### Recovery Semantics

A recovery claim says what recovered, for whom, under which support, and as of when (§6.6). Evidence actual output quantity, quality, continuity, and reach; internal rest, spares, maintenance backlog, and funding continuity; new care, commuting, borrowing, or substitute-service burdens beyond the boundary; and later interruptions and near misses. Pre-event population, current population, eligible people, and actual users are never swapped when computing a recovery ratio. Confirming one limited function does not require every other outcome to recover. Temporary sites, continuing outside help, and assistive equipment can be real functional repair; dependence on support is not failed recovery, but check its sustainability, end date, and replacement. "False recovery" means only a claim reaching beyond the supported object, population, function, or duration; it does not imply deceit. When instability returns, compare continued old damage, unreplenished reserves, interrupted support, a new shock, and changed measurement; one new failure never erases an accurately bounded earlier result, and necessary support is never withdrawn just to test recovery.

### Same End State, Different Mechanisms

Processes converging to the same fixed point can differ in update rule, return speed, transients, and intervention response (§6.9). A simpler representation may suffice for the long-run end value; questions about time to arrival or targeted operations do not inherit that adequacy.

### Dissolution and Repair

Treat dissolution as failed old K; distinguish termination from conversion to a new object. Dissolution is not failure and persistence is not success. Define repair against a preregistered K* or F*; a repair window compares reachability and cost of intervening at different times; historically formed current limits follow the carried route, and only a historical conditional residual needs G3. Whether to repair, who chooses the target, who bears responsibility, and who may act pass through N, J, and O1-O4 outside this module.

## Mechanism Output Gate

All six mechanisms pass, in order, object and scale declaration, inferential dependencies, enabling conditions, mechanism chain, minimum evidence, competitors, counterexamples, and failure boundary; a missing item leaves only a candidate mechanism or a check question (§6.11). **Feedback never smuggles in learning, instant load never smuggles in accumulation, a base phase never smuggles in hysteresis, a selection pattern never smuggles in mechanism or value, and maintenance or repair never smuggles in a duty to persist.**

## Clocks

Assign each mechanism an update clock and every clock crossing a carrier, execution step, confirmation, and failure condition (§6.12). Distinguish immediate, interaction, organizational, institutional, and long-term clocks; a fast variable's change is not a long-term result.

| Crossing | Bridge required | Typical failure |
|---|---|---|
| Immediate -> interaction | Persists over several rounds and changes the other side's response | A single emotion fades |
| Interaction -> organization | Enters roles, procedures, resources, or records | Verbal agreement never executed |
| Organization -> institution | Verifiable rule or procedure change, responsibility arrangement, and actual execution, with authorization, legal validity, and legitimacy recorded separately | A document published but not executed, or a real institutional change left unrecorded because it was unlawful |
| Institution -> long term | Sustained execution, maintenance, learning, and substitute paths | Short-term compliance rebounds |

Violations, overreach, and disputed changes that factual evidence shows actually happened enter the process record, with authorization and legality status recorded separately; explaining is not permitting. Authorization, rule publication, or an agency announcing completion never stands in for evidence of actual execution.

## Cross-Circle Cascades and Coevolution

A cascade travels through member overlap, bridging interfaces, shared resources, network propagation, or institutional descent; recheck object, channel, scale, and evidence at every hop, and let capacity, filtering, delay, cancellation, and local exclusion terminate it (§6.13). First name what propagates and what the target change requires: a message can arrive over one bridge while action needing several people's cooperation, confirmation from distinct sources, or enough safe support stops there. The count of same-source retellings is not the number of independent confirmers or actual collaborators. A bridge's effect depends on source relations, landing point, arrival order, action duration, and feasibility, not on shortest path, degree, or a model threshold.

Distinguish three failure situations: one failure triggering the next (hop-by-hop transmission evidence), several failures jointly blocking recovery (recovery dependence), and a common external cause damaging several places at once (common-cause exposure). Human multi-source adoption and facility supply dependence can coexist but never swap variables or thresholds; complex contagion does not guarantee that higher clustering helps. Coevolution keeps mutually independent K; absorption is nesting or conversion, a common environment is not coevolution, and a return that changes nothing later is only coupling or common exposure. Neither cascades nor coevolution carry a value direction.

## Retrieval Order

Screen candidate mechanisms by object, scale, window, and requested output, then search paths from observed state differences (§6.14); the full procedure is in `ariadne-skill/references/routing.md`. What is found first is not more likely true. Keep competitors and a simple baseline beside each candidate (returned signal versus learning; local overload versus a demand rise, capacity drop, or common cause; cascade versus synchronized exposure). For each candidate path, write what keeps it alive, the observable change it should produce first, opposite signals, and its stop. An early signal is not the outcome restated smaller, and evidence shared across paths adds no independent support.

## Comparison Output

For each target residual, present the simple baseline first, then a compact comparison:

| Field | Required content |
|---|---|
| Residual | The exact observation or difference left unexplained by the baseline |
| Candidate | One named contract and branch, not a narrative label |
| Route | `current_state`, `carried_history`, `historical_increment`, or `not_applicable` |
| Chain | Source -> carrier -> intermediate change -> target change |
| Support | Eligible instance and measured dimensions, independent domain evidence, or explicit missing state |
| Competitor | A distinguishable alternative and its expected signal |
| Falsifier | An observation that downgrades or rejects the candidate |
| Scope | `SP/T/K`, task, generalization unit, and output ceiling |
| Residual after fit | What the candidate still does not explain |

Retain multiple candidates when present evidence cannot distinguish them. Prefer the simple baseline when added mechanisms do not improve out-of-sample explanation or intervention performance. In the typed payload, every candidate separately fills `temporal_route`, `channel_observation`, `discriminating_prediction`, `reverse_or_falsifier`, and `residual_comparison_rule`. Candidate IDs and the four-field test signatures must be distinct; relabeling the same story does not create a competitor.

## Worked Example: Complaint Receipt, Writeback, or Learning

Suppose an organization receives a complaint and immediately emits a receipt. Freeze the complaint process object, case fields, organization scale, observation window, task (did complaints change later handling), and evidence cutoff. Use "automatic receipt with no downstream change" as the simple baseline.

The receipt alone supports only signal arrival. Add a CM-FEEDBACK candidate (`temporal_route: current_state`) only if the complaint returns through a specified channel, a named case or rule field changes afterward, and a no-return or blocked-channel comparison distinguishes the change from a parallel management instruction. Keep "independent management instruction changed the field" as a competing mechanism.

If the field changes but no execution record exists, distinguish effective feedback from C11 institutional writeback. If execution occurs, record receipt, field change, execution, and duration separately. Do not call the organization learning yet. Add a CM-LEARNING-carried candidate (`temporal_route: carried_history`) only after a retained rule or state update enters repeated later cases and changes a predefined task result against the baseline; add CM-LEARNING-history only with an eligible G3-instance showing gain beyond the current rule state.

Record the result as follows: put the receipt and any field-version evidence in `claim_ledger`; put blocked-channel comparison, execution, retention, repeated-round evidence, and the competing instruction in `unknowns_and_counterevidence`; set `output_ceiling: diagnostic_only`; recommend evidence repair or human-domain writeback analysis only if needed; and set `authorization_effect: none`. The result may distinguish arrival, feedback, writeback, and a learning candidate. It cannot certify institutional legitimacy, assign blame, require a remedy, or authorize a rule change.
