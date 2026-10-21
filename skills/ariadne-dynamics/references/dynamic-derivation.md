# Dynamic Derivation Contracts

Section anchors (§) point to the source text named in `ariadne-skill/references/source-navigation.json`.

## Boundary and Method Record

Use dynamic derivation to ask which registered variables may change first, through which channels, after which delays and thresholds, with which feedback, cascades, and branches. Do not use it to state what will certainly happen, verify an event, select values, or authorize an action. Unlike narrative continuation, which picks a sequel by coherence, structural derivation keeps conditions, channels, competing paths, and failure semantics: a missing key variable stops at unknown or a variable candidate, several consistent sequels stay branched, and incomparable branches are not forced into a ranking (§11.1). Actions that actually happen can change reality whether or not they were authorized, so record them as evidence; whether an act occurred, how it is normatively judged, what legal or institutional authority it had, and whether this run may execute anything are four separate judgments (§11 opening).

For a standalone run, create the common Method Record and record:

- the frozen joint object, identities, and task profile (target query, horizon, environment, allowed operations, error tolerance) in `object_contract`;
- only the source and observation cutoff in `evidence_cutoff`;
- every event ID, fact status, source IDs, window, observation position, and model version in the typed `ariadne-dynamics` payload;
- active actor, circle, network, temporal, impact, and jurisdiction axes in `scale_scope`;
- event contracts, state deltas, mechanism provenance, branches, signals, and stop states in `claim_ledger`;
- disputed facts, missing channels, parameter intervals, residuals, candidate variables, and counterpaths in `unknowns_and_counterevidence`;
- the ordered ceiling transition; a normal child preserves or lowers, and only newly admitted external evidence or protocol fulfillment in a child can raise;
- this run and its parent path in `module_runs`, necessary handoffs in `recommended_next_modules`, and `authorization_effect: none`.

Create a new child record when a later observation, changed scope, altered model, or new event enters. Never pour later outcomes back into the original starting state.

## Minimum Input and Output

Freeze these inputs before expanding a path:

| Input | Required content |
|---|---|
| Joint snapshot | Actors, circles, relations, memberships, material state, experience-meaning state, channels, clocks, evidence cutoff, unknowns, residuals, `SP`, and `K` |
| Event set | Separate event record per input, ordered when more than one enters |
| Mechanisms | Direction, carrier, delay, threshold, measured dimensions, failure condition, and evidence status |
| Parameters | Value, interval, ordered category, or explicit unknown; never unsupported decimal precision |
| Clock policy | Immediate, interaction, organizational, institutional, and long-term update rules plus cross-clock bridges |
| Propagation policy | Channel admission, capacity, loss, saturation, reversal, recovery, and cascade rules |
| Stop policy | Information, identity, scale, sensitivity, branch, residual, resource, privacy, safety, and authorization conditions |

Return at minimum a conditional path graph, state difference at every node, support state and provenance, clock, early signal, reverse signal, residual, variable candidates, termination reason, and result-writeback requirement. Keep derivation separate from forecast registration and action selection.

## Event Contract

Classify every event before using it:

| Type | May enter | Fact status and restriction |
|---|---|---|
| Observed | Explanation, replay, and forward derivation | Established only within its observation contract; preserve source, omission, and measurement error. |
| Reported | Belief propagation and conditional paths | The report occurred; its content remains unverified unless separately supported. Preserve reporter position, verification, and dispute. |
| Planned | Expectation, preparation, and strategic response | The plan exists; execution remains separate. Preserve authority, resources, cancellation, and implementation conditions. |
| Hypothetical | Scenario and counterfactual comparison | Not a real-world fact. State the condition, purpose, and feasibility. |
| Simulated | Model-internal expansion | Model state only. Preserve model version, parameters, lineage, and prohibition on factual writeback. |

Record at least `event_id`, event type, occurrence time or window, observation time, source, affected actors, affected circles, channel, direct change, evidence state, disputes, competing explanations, reversibility, duration, and follow-up observations. A reported event may change the beliefs of people who receive the report without its reported content becoming true. A plan may change preparation without becoming execution. **Observed violations, overreach, refusals to execute orders, and unauthorized acting on another's behalf enter `e(t)` as observed or reported events**, with actor, consequences, and authority status listed separately; lacking authority never deletes them from the facts. Violations that have not happened appear only in hypothetical or simulated branches (§11.3).

## Joint State and Update

Represent the frozen state as:

`Omega(t)=<A(t),C(t),R(t),M(t),Psi(t),Q(t),E<=t,SP(t),W(t),K(t)>`

where `A` is actors, `C` circles, `R` memberships and inter-circle relations, `M` material conditions, `Psi` experience-meaning conditions, `Q` channels and constraints, `E<=t` admitted event history, `SP` scale, `W` evidence/unknown/residual state, and `K` identity.

Represent one update obligation as:

`Omega(t+delta)=F[Omega(t),e(t),u(t),xi(t) | theta,h]`

Use `e(t)` for an event (including actions that actually occurred without authorization), `u(t)` only for an externally authorized action that actually occurs, `xi(t)` for exogenous disturbance or unmodeled residual, `theta` for frozen mechanism and parameter assumptions, and `h` for history. Treat `F` as a bookkeeping interface, not a claim that one true function exists.

Tag every state entry and delta as exactly one of:

- directly observed under a stated observation contract;
- inferred through a supported mechanism contract;
- assigned as a scenario value for exploration;
- unexplained residual.

Preserve the tag downstream. Co-location in one snapshot does not equalize evidence status.

### State, Observation, and the Identification Set

Keep the actual state `z(t)` apart from the record `o(t)=H[z(t),m(t),epsilon(t)]`, where `H` is the observation rule, `m(t)` says who can enter the record, when measurement happens, and which fields are withheld for protection, and `epsilon(t)` is used only when an error model exists; not every unknown is random noise (§11.3.1). A changed observation rule is never written as a changed object. Let `Z(o)` be the set of states consistent with the record. If question `q` takes the same value on every state in `Z(o)`, the current material already suffices for that question and a bounded answer can be given without recovering every hidden variable; otherwise report the range, the identifiable direction, or what is genuinely unknown. A finite sample that found no difference has not shown that only one answer remains.

Choose the next observation by first finding the state differences that would change the current answer or the action comparison, then finding feasible observations that separate them. Precision that changes no answer is not automatically worth having; a cheap observation that narrows a key branch can beat a longer variable list. Data collection stays bound to purpose, necessity, and protection: **a need to identify never creates a right to collect**.

### Event Handling and State Continuity

Every input keeps three times: when the event happened, when the record was obtained, and when it entered the model (§11.3.2). Late material can change what is known about the past but never rewrites the information set available at the time. A corrected source adds a correction relation; recompute only the states and paths that depend on it and keep the rest. Several retellings keep several sources and one candidate event identity, so one shock is not applied twice; similar events are not merged without verification. Separate **evidence update** (revising the judgment about `z(t)`) from **mechanism advance** (estimating how `z(t)` moves to later states): a credible record that work stopped yesterday is today's evidence update, while re-running a model that says work "may stop" only adds simulation material. Concurrent events merge in arbitrary order only when operations commute, shared resources do not conflict, and neither changes the other's conditions; contention for resources, overwriting the same record, or changing each other's action sets calls for ordered branches or an explicit concurrency rule. Close timestamps are not simultaneity, and the order in which executors return is not the real causal order.

## Five Clocks and Cross-Clock Bridges

| Clock | Typical variables | Update condition | Error to prevent |
|---|---|---|---|
| Immediate | Emotion, attention, bodily arousal, local price, direct resource shock | Signal arrival or direct impact | Calling a short fluctuation a durable change |
| Interaction | Trust, strategy, relationship expectation, local norm | Multiple ordered action-feedback rounds | Ignoring sequence, memory, and reciprocal adaptation |
| Organizational | Role, workflow, budget, workload, metric, allocation | Decision plus execution and review | Treating a decision or announcement as implementation |
| Institutional | Rule, right, responsibility, appeal, official record | Valid procedure plus actual field writeback | Treating an oral promise or intake receipt as institutional change |
| Long-term | Capacity, identity, infrastructure, culture, learning, generation | Accumulation, retention, maintenance, succession, or replacement | Extrapolating a short window into durable history |

Assign every variable one or more update clocks and every crossing a carrier, execution step, confirmation, delay, and failure condition. Update only variables reached by the event channel and passing their threshold. Leave untouched variables unchanged; mark stale values unknown. Do not refresh the whole snapshot to make it look complete.

## Nine-Step Derivation Loop

1. **Freeze current state.** Record cutoff, objects, variables, unknowns, disputes, model version, baseline, and stop policy. Create a new run to use later evidence.
2. **Identify actors and circles.** Keep unsupported groups as candidate groupings and unsupported personality terms as variable candidates. Do not instantiate them to complete a diagram.
3. **Separate dual-channel conditions.** List material and experience-meaning conditions independently and name any bridge. Leave the unsupported channel unknown.
4. **Declare clocks, thresholds, capacity, and delay.** Register update clocks, channel capacity, queueing, loss, saturation, reversal, recovery window, and threshold before propagation.
5. **Inject events or actions.** Preserve a separate contract for every ordered event. First determine whether an action actually happened, then record actor, object, consequences, and authorization status separately; lacking authorization is never a reason to delete an occurred fact. Planned, proposed, and simulated actions keep their conditional identity. A model initiating or carrying out a real action needs separate valid authorization; forming a recommendation for deliberation needs only explicit evidence, normative premises, costs, the authority gap, and change conditions.
6. **Propagate along declared channels.** Record direct effects first, then return signals, indirect effects, and cross-circle cascades. An identified total intervention effect may enter a bounded outcome judgment while unknown internal mechanisms stay unknown, with no invented propagation edges. Where only co-occurrence or correlation exists, keep common background and selection as competitors. Store model-derived and observed state differences separately; keep a no-channel influence as a candidate.
7. **Generate paths at branch points.** Branch on conditions, thresholds, actor choices, external disturbances, or mechanism uncertainty. Separate mutually exclusive paths, allow parallel paths, and merge only under declared conditions.
8. **Register signals, residuals, and variable candidates.** Give every path early and reverse signals. Keep unexplained differences as residuals and generate candidates without assigning real values.
9. **Write back results.** When outcomes arrive, append which paths gained or lost support, when deviations occurred, whether the simple baseline performed better, how calibration changed, and which mechanism, variable, boundary, or model should be downgraded, split, revised, or retired. Never overwrite the run.

## Propagation, Feedback, and Cascades

Separate signal arrival from effective state change. Seeing information establishes arrival. A changed belief establishes an experience-meaning delta. A changed resource, behavior, rule, role, relation, or transition establishes only that corresponding structural delta.

For every hop, record:

| Element | Required question | Nonlinearity to retain |
|---|---|---|
| Channel | What carrier connects source and target? | Closure, filtering, substitution |
| Capacity | How much of the typed quantity can pass per window? | Saturation, congestion, queueing |
| Delay | When does it arrive and when can it take effect? | Delayed feedback and false “no effect” judgments |
| Threshold | What condition changes the state? | Abrupt change, hysteresis, cascade |
| Loss or conversion | What disappears, changes type, or shifts meaning? | Dissipation and translation drift |
| Direction | Is influence symmetric? | One-way dependence and reverse cancellation |
| Recovery | How does the object return to `K/F` or convert? | Resilience, cumulative damage, lock-in |

Register feedback only when an earlier state or output returns through a channel and changes a later state, transition probability, timing, or constraint relative to no-return or blocking. Register a cross-circle cascade only when one local change reaches another circle through member overlap, a bridge, shared resources, institutional descent, or network propagation. Require timing and channel evidence at every hop. Allow a cascade to stop at nonparticipation, failed receipt, resource isolation, substitution, no behavior or rule change, local cancellation, or exhausted amplification. Do not rank a cascade by member count; a small bridge can be high-impact and a large circle can remain isolated.

Keep distribution visible. The same event can reduce load in one circle and increase competition in another; it can improve external legitimacy while decreasing internal trust. Record channel by channel and do not collapse opposite effects into one net score (§11.5).

| Cascade type | Requires | Stops when |
|---|---|---|
| Member | Real transmission through people, not shared background | Members no longer take part or the information is not received |
| Resource | Accounting boundary, conversion, and loss | Resources are isolated or a substitute source appears |
| Meaning | Interpretive differences across positions | It does not arrive or does not change experience-meaning state; action or rule effects need their own check |
| Institutional | Decision, execution, and actual writeback | The rule is not implemented or is offset locally |
| Platform | Algorithm, selective visibility, and reflexivity | Exposure stops growing or audiences do not respond |

A cascade is not more important for being larger; attend to position, channel, and threshold rather than headcount (§11.6). Two equally weighted subgroups can each show a link-average effect of 1/2 while the whole chain's effect is 0, so check how upstream output enters downstream input, the support of the joint response, capacity and delay, and offsetting or parallel paths. A finite total effect identified by a qualified comparison is kept directly; when one edge is unidentified, independently established upstream changes and terminal effects keep their own evidence.

## Branch Graph Contract

Use a directed acyclic graph. Time-expand recurring feedback into later nodes so that a node is not its own cause and result within one run.

Record for every node:

- node and parent IDs;
- condition set and trigger event or action;
- state delta with provenance;
- affected clocks, circles, and positions;
- support state and probability expression or ordinal comparison when justified;
- early signal and reverse signal;
- next nodes and termination reason.

Keep four uncertainty sources separate:

| Source | Correct treatment | Incorrect treatment |
|---|---|---|
| Fact uncertainty | Verify the event; retain conditional paths until then | Select one report as fact |
| Mechanism uncertainty | Keep competing mechanisms and distinguishing signals | Close the question with a personality or theory label |
| Actor choice | Retain feasible choices, conditions, and external authorization status | Claim free choice is exactly predictable |
| Exogenous disturbance | Use stress scenarios, ranges, and recovery checks | Attribute residuals to fate or silently tune the model |

Do not force a probability or ranking when current evidence does not support one. Preserve ties and incomparability.

## Variable-Candidate Ledger

Turn a residual into a testable task rather than deleting it or naming a hidden truth. Record the source residual, candidate name, possible type, possible channel, observable implication, competing candidates, minimum distinguishing test, privacy and risk, current state, evidence, promotion rule, rejection rule, and retirement rule.

Use only `proposed`, `testing`, `supported_candidate`, `rejected`, or `retired`. Even a supported candidate must enter the relevant object, variable, circle, or mechanism contract before use. A post-result candidate can improve the next run but cannot support the original derivation or forecast. Treat an AI suggestion as candidate generation only.

Type every candidate by its source; each source carries one allowed action and one shortcut to refuse:

| Candidate source | Allowed action | Must avoid |
|---|---|---|
| Systemic residual | Propose multiple competing candidates with distinguishing observations, as registered above | Absorbing all error into one mysterious variable |
| Participant account | Preserve its position, its meaning, and its verifiable parts | Automatically downgrading it to subjective noise or upgrading it to the full factual picture |
| Cross-case repetition | Build a candidate mechanism with an explicit extrapolation boundary | Treating similar narratives as a universal law |
| Model search | Preregister the next-round test under the post-result rule above | Reporting only favorable results after the outcome |
| AI suggestion | Generate and compare candidates, and form judgments and analytic recommendations where evidence, use, and explicit normative premises allow | Letting AI output verify reality or authorize action |

## Scenarios, Counterfactuals, and Simulation

Use a scenario to ask what paths follow if stated conditions hold. Use a counterfactual to compare an observed outcome with a changed event or mechanism under explicit comparability conditions. Use a simulation to expand declared rules and parameters. Keep all three distinct from factual description.

When removing an event in a counterfactual, also change downstream information, actor knowledge, and circle relations caused by that event, and keep the information boundary of the time (deleting an announcement cannot keep the attendance and execution it produced). Do not remove an unwanted cause while retaining all of its effects. "Removing a person who later held the post" and "the person never existed" are different starting points. Keep numerical precision at or below input and mechanism evidence; use intervals, ordered categories, and sensitivity analysis for unknown parameters. Material for a short-range branch does not make a decades-long alternative history knowable. Ordinary people's actions, frontline discretion, and organizational constraints can enter one explanation without assigning causal percentages that have no identification basis (§11.9).

**Mechanism equivalence.** Observations consistent with X -> M -> Y can also come from X changing M and Y separately; more observations of the same kind do not break the equivalence, which needs a discriminating design or a grounded assumption. A counterfactual may output one answer, a set of feasible answers, or a conditional bound. Report a direction as robust only when every compatible mechanism supports it; when the conclusion flips across reasonable mechanisms, report the flip conditions and the evidence needed.

### Recursive Simulation Evidence Ceiling

Keep three dimensions orthogonal:

- **Multi-step time roll-forward:** advance states through time within one run.
- **Simulation re-entry:** use a simulated future node as the start of a child run.
- **Anticipatory reflexivity:** let simulated actors form expectations about later futures or other reactions and alter current strategy.

Use three orders as the default exploratory ceiling:

1. Expand direct consequences and the leading competing paths.
2. Examine how first-order states alter action sets, resources, circle structure, feedback, and adaptation.
3. Examine institutionalization, lock-in, reversal, cross-circle spillover, and changes to the generating conditions.

Treat these as orders of dependence, not three clock ticks, natural stages, or capability grades. Do not force recursion on a static question or one with no independent next-order question, and stop earlier when conditions fail.

Apply the invariant: generate broadly, assign state strictly, never let evidence self-upgrade, and require separate authorization for action (§11.9.1). Boldness widens the space of reasonable mechanisms, competing paths, and low-probability high-consequence branches, and also lets the run state clear judgments that its evidence supports; judgment strength comes only from evidence, applicable conditions, and use, never from tone or the number of generated stories. Recursive depth, narrower conditional scope, or more simulation samples does not raise fact status, empirical support, calibration, capability, value, or authorization. More samples may reduce computational error only. Without new external observation, execution receipt, or independent adjudication, a child run inherits the parent's output ceiling and unresolved unknowns, losses, and residuals.

Before every re-entry, record current order, parent run, parent path and node, simulated start time, current and cumulative windows, model version, inherited assumptions, added conditions, preserved and changed fields, collapsed and omitted information, added unknowns, target effective variables, residuals, identity status, return path, and stop reason. Never rewrite a simulated start as present reality.

At every order retain at least:

- the current principal path;
- the strongest competing path;
- a low-probability high-consequence path;
- a residual exit.

Create branches only from explicit conditions, mechanism differences, actor choices, disturbances, or typed unknowns. Merge branches only when object identity holds, key states are equivalent within preregistered tolerance, historical differences do not alter later transitions, and later actions and constraints match. Declare pruning before expansion; preserve every pruned branch, reason, possible probability mass, and harm level. Keeping a high-consequence branch means it needs study or preparation, not that its probability is known; do not invent events to fill a category. Never prune a high-consequence branch solely for low probability.

Stop or downgrade recursion when object or scale identity fails; a key inherited assumption cannot be carried; the transition leaves the mechanism's domain; the re-entry interface does not close; branches explode without distinguishing signals; small changes reverse results broadly; residuals exceed the use threshold; a deeper order adds no value over the shallower order or simple baseline; the run exceeds a calibrated window; rights or authorization boundaries arise; or the third-order ceiling is reached. State what remains sayable and what is no longer supported.

## Action Selection and Conditional Update

Do not let a model merely comment on static options (§11.13). At each step first identify the actions actually available, the actions excluded, and the source of each restriction, then analyze how the actor may choose given their information, resources, relations, habits, and goals. Keep **capability, belief, willingness, and actual action** apart: being able is not doing, stating an intention is not having done, and an analyst's recommendation is not the actor's adoption. For each grounded choice, state which mechanism it triggers, which states change first, through which interface it affects whom, and how it changes the next action set, with state differences landing on concrete items (resources, rules, relations, beliefs, feasible actions). Feeding the same material to another model or regenerating a narrative never substitutes for a state update. Without material to fix a choice, keep several conditional paths rather than choosing for the actor; later derivation inherits unresolved unknowns and limits.

When real feedback arrives, first check its source and event identity, then compare the original path, competing paths, and the simple baseline, separating errors of fact, errors of mechanism, a different action choice, execution deviation, and external change. Correction changes the states, parameters, mechanism range, or paths used next; **keeping the feedback text while the same choice rule continues is not evidence that the model has learned**.

## Run-Level Stop and Writeback

Pause or lower the ceiling when the key object lacks finite support, event fact status is unclear, propagation channel is absent, scale mapping fails, path count grows without distinguishing signals, parameters create extreme sensitivity, privacy or safety cost exceeds information value, a diagnosis or punishment is requested, authorization is missing, or a simple baseline performs as well or better.

Downgrade only the affected propositions and the paths that depend on them; stop everything only when a shared premise fails (§11.10). Treat stopping as an output. Record where the run stopped, what it established, which unknown prevented continuation, the next highest-information observation, and the risk of continuing.

Append real outcomes without rewriting prior paths. Record path support, timing deviations, baseline performance, calibration effects, and model changes. A dynamic run without preregistered future target, deadline, simple baseline, calibration, and continuing writeback does not establish forecasting ability. A dynamic run without normative and authorization records does not justify an action. An analytic first choice, veto, or deferral stated under explicit normative premises is not a claim that the option may be executed, and its grounds, costs, objections, and change conditions are stated in full (§11.12).

## Worked Example: Public Resignation Across Circles

Freeze a joint snapshot containing an employee, project team, company management, family-care circle, professional community, and platform audience. Record high work hours and care demand as material conditions, declining team trust as an experience-meaning condition, external job opportunities as a professional-community bridge, and platform attention as not yet activated. Register the employee's public resignation statement as a separate event: publication is observed; some content is verifiable, some is the actor's account, and disputed claims remain reported rather than fact.

Record direct effects first: the team receives the statement, the platform receives transmissible text, and management faces response pressure. Branch on explicit conditions:

- In a denial branch, external attention may decay or amplify. Keep an internal-trust decline and professional-community exit cascade only if member or bridge channels transmit the response and later behavior changes.
- In an acknowledgement-and-adjustment branch, treat a public statement, resource allocation, complaint process, and actual execution as separate events. Organizational workload may change before interaction-clock trust. A rule text without local execution does not update the institutional state.
- In a changed-care-condition branch, lower personal exit pressure only through the material channel. Do not update team state unless the employee continues to transmit information, labor, or resources.

Use internal complaint counts, work-hour execution records, member expression, hiring, and exits as early signals. Use a policy announcement without resource change, falling public exposure alongside growing internal silence, and no professional-community bridge as reverse signals. Put manager state, platform recommendation behavior, and unobserved legal constraints in the variable-candidate ledger, not into the snapshot as facts.

Keep the path graph conditional and unranked unless evidence supports comparison. Put the frozen snapshot, event status, mechanisms, branches, clocks, and signals in `claim_ledger`; put disputed content, missing channels, residuals, and candidates in `unknowns_and_counterevidence`; set `output_ceiling: diagnostic_only`; recommend `ariadne-forecast` only if the user separately asks for a preregistered future claim; and set `authorization_effect: none`. The derivation may expose conditions and observations. It may not decide what the company should do or authorize anyone to act.
