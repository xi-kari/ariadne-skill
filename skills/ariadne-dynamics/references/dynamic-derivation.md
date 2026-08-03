# Dynamic Derivation Contracts

## Boundary and Method Record

Use dynamic derivation to ask which registered variables may change first, through which channels, after which delays and thresholds, with which feedback, cascades, and branches. Do not use it to state what will certainly happen, verify an event, select values, or authorize an action.

For a standalone run, create the common Method Record and record:

- the frozen joint object and identities in `object_contract`;
- the source and observation cutoff, event fact status, and model version in `evidence_cutoff`;
- active actor, circle, network, temporal, impact, and jurisdiction axes in `scale_scope`;
- event contracts, state deltas, mechanism provenance, branches, signals, and stop states in `claim_ledger`;
- disputed facts, missing channels, parameter intervals, residuals, candidate variables, and counterpaths in `unknowns_and_counterevidence`;
- `description_only`, `diagnostic_only`, or `requirements_only` in `output_ceiling`, never above the parent ceiling;
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

Record at least `event_id`, event type, occurrence time or window, observation time, source, affected actors, affected circles, channel, direct change, evidence state, disputes, competing explanations, reversibility, duration, and follow-up observations. A reported event may change the beliefs of people who receive the report without its reported content becoming true. A plan may change preparation without becoming execution. An unapproved action may appear only as a hypothetical input; attach external authorization only when an action actually occurred under that authority.

## Joint State and Update

Represent the frozen state as:

`Omega(t)=<A(t),C(t),R(t),M(t),Psi(t),Q(t),E<=t,SP(t),W(t),K(t)>`

where `A` is actors, `C` circles, `R` memberships and inter-circle relations, `M` material conditions, `Psi` experience-meaning conditions, `Q` channels and constraints, `E<=t` admitted event history, `SP` scale, `W` evidence/unknown/residual state, and `K` identity.

Represent one update obligation as:

`Omega(t+delta)=F[Omega(t),e(t),u(t),xi(t) | theta,h]`

Use `e(t)` for an event, `u(t)` only for an externally authorized action that actually occurs, `xi(t)` for exogenous disturbance or unmodeled residual, `theta` for frozen mechanism and parameter assumptions, and `h` for history. Treat `F` as a bookkeeping interface, not a claim that one true function exists.

Tag every state entry and delta as exactly one of:

- directly observed under a stated observation contract;
- inferred through a supported mechanism contract;
- assigned as a scenario value for exploration;
- unexplained residual.

Preserve the tag downstream. Co-location in one snapshot does not equalize evidence status.

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
5. **Inject events or actions.** Preserve a separate contract for every ordered event. Treat unauthorized actions as hypothetical scenarios rather than instructions.
6. **Propagate along declared channels.** Record direct effects first, then return signals, indirect effects, and cross-circle cascades. Keep a no-channel influence as a candidate.
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

Keep distribution visible. The same event can reduce load in one circle and increase competition in another; it can improve external legitimacy while decreasing internal trust. Do not collapse opposite effects into one net score.

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

## Scenarios, Counterfactuals, and Simulation

Use a scenario to ask what paths follow if stated conditions hold. Use a counterfactual to compare an observed outcome with a changed event or mechanism under explicit comparability conditions. Use a simulation to expand declared rules and parameters. Keep all three distinct from factual description.

When removing an event in a counterfactual, also change downstream information, actor knowledge, and circle relations caused by that event. Do not remove an unwanted cause while retaining all of its effects. Keep numerical precision at or below input and mechanism evidence; use intervals, ordered categories, and sensitivity analysis for unknown parameters.

### Recursive Simulation Evidence Ceiling

Keep three dimensions orthogonal:

- **Multi-step time roll-forward:** advance states through time within one run.
- **Simulation re-entry:** use a simulated future node as the start of a child run.
- **Anticipatory reflexivity:** let simulated actors form expectations about later futures or other reactions and alter current strategy.

Use three orders as the default exploratory ceiling:

1. Expand direct consequences and the leading competing paths.
2. Examine how first-order states alter action sets, resources, circle structure, feedback, and adaptation.
3. Examine institutionalization, lock-in, reversal, cross-circle spillover, and changes to the generating conditions.

Treat these as orders of dependence, not three clock ticks or natural stages. Stop earlier when conditions fail.

Apply the invariant: generate broadly, assign state strictly, never let evidence self-upgrade, and require separate authorization for action. Recursive depth, narrower conditional scope, or more simulation samples does not raise fact status, empirical support, calibration, capability, value, or authorization. More samples may reduce computational error only. Without new external observation, execution receipt, or independent adjudication, a child run inherits the parent's output ceiling and unresolved unknowns, losses, and residuals.

Before every re-entry, record current order, parent run, parent path and node, simulated start time, current and cumulative windows, model version, inherited assumptions, added conditions, preserved and changed fields, collapsed and omitted information, added unknowns, target effective variables, residuals, identity status, return path, and stop reason. Never rewrite a simulated start as present reality.

At every order retain at least:

- the current principal path;
- the strongest competing path;
- a low-probability high-consequence path;
- a residual exit.

Create branches only from explicit conditions, mechanism differences, actor choices, disturbances, or typed unknowns. Merge branches only when object identity holds, key states are equivalent within preregistered tolerance, historical differences do not alter later transitions, and later actions and constraints match. Declare pruning before expansion; preserve every pruned branch, reason, possible probability mass, and harm level. Never prune a high-consequence branch solely for low probability.

Stop or downgrade recursion when object or scale identity fails; a key inherited assumption cannot be carried; the transition leaves the mechanism's domain; the re-entry interface does not close; branches explode without distinguishing signals; small changes reverse results broadly; residuals exceed the use threshold; a deeper order adds no value over the shallower order or simple baseline; the run exceeds a calibrated window; rights or authorization boundaries arise; or the third-order ceiling is reached. State what remains sayable and what is no longer supported.

## Run-Level Stop and Writeback

Pause or lower the ceiling when the key object lacks finite support, event fact status is unclear, propagation channel is absent, scale mapping fails, path count grows without distinguishing signals, parameters create extreme sensitivity, privacy or safety cost exceeds information value, a diagnosis or punishment is requested, authorization is missing, or a simple baseline performs as well or better.

Treat stopping as an output. Record where the run stopped, what it established, which unknown prevented continuation, the next highest-information observation, and the risk of continuing.

Append real outcomes without rewriting prior paths. Record path support, timing deviations, baseline performance, calibration effects, and model changes. A dynamic run without preregistered future target, deadline, simple baseline, calibration, and continuing writeback does not establish forecasting ability. A dynamic run without normative and authorization records does not justify an action.

## Worked Example: Public Resignation Across Circles

Freeze a joint snapshot containing an employee, project team, company management, family-care circle, professional community, and platform audience. Record high work hours and care demand as material conditions, declining team trust as an experience-meaning condition, external job opportunities as a professional-community bridge, and platform attention as not yet activated. Register the employee's public resignation statement as a separate event: publication is observed; some content is verifiable, some is the actor's account, and disputed claims remain reported rather than fact.

Record direct effects first: the team receives the statement, the platform receives transmissible text, and management faces response pressure. Branch on explicit conditions:

- In a denial branch, external attention may decay or amplify. Keep an internal-trust decline and professional-community exit cascade only if member or bridge channels transmit the response and later behavior changes.
- In an acknowledgement-and-adjustment branch, treat a public statement, resource allocation, complaint process, and actual execution as separate events. Organizational workload may change before interaction-clock trust. A rule text without local execution does not update the institutional state.
- In a changed-care-condition branch, lower personal exit pressure only through the material channel. Do not update team state unless the employee continues to transmit information, labor, or resources.

Use internal complaint counts, work-hour execution records, member expression, hiring, and exits as early signals. Use a policy announcement without resource change, falling public exposure alongside growing internal silence, and no professional-community bridge as reverse signals. Put manager state, platform recommendation behavior, and unobserved legal constraints in the variable-candidate ledger, not into the snapshot as facts.

Keep the path graph conditional and unranked unless evidence supports comparison. Put the frozen snapshot, event status, mechanisms, branches, clocks, and signals in `claim_ledger`; put disputed content, missing channels, residuals, and candidates in `unknowns_and_counterevidence`; set `output_ceiling: diagnostic_only`; recommend `ariadne-forecast` only if the user separately asks for a preregistered future claim; and set `authorization_effect: none`. The derivation may expose conditions and observations. It may not decide what the company should do or authorize anyone to act.
