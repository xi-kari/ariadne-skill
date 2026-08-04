# Human-Domain Contracts

## Domain and Method Record Boundary

Use the H-World adapter only after declaring a D0 object and scale. Apply it to human intention, meaning, power, institutions, authorization, responsibility, and value-bearing activity. Do not project those properties onto technology, crises, metrics, platforms, resources, or nonhuman systems merely because they affect people.

For a standalone run, create the common Method Record and record:

- the actor, circle, or joint object and its `B/X/R/I/T/SP/K` in `object_contract`;
- only the source cutoff timestamp, admitted source IDs, and after-cutoff exclusion flag in `evidence_cutoff`;
- only source scale, target scale, and transformation status in `scale_scope`;
- observed behavior, candidate variables, H-instance state, HV route, circle relations, and bounded conclusions in `claim_ledger`;
- missing states, refusals, conflicts, counterexamples, local exclusion zones, and competing explanations in `unknowns_and_counterevidence`;
- observation position, privacy state, allowed purpose, at least two distinct alternatives, and responsible human review in the typed `ariadne-human` module payload;
- `affected_positions` as a closed four-class object: `direct`, `indirect`, `low_power`, and `no_exit`; every class contains `status`, `positions`, and `reason`, and an unknown/protected/non-applicable class remains explicit with an empty list rather than collapsing into free text;
- the ceiling transition, traceable module input/output records, necessary handoffs, and `authorization_effect: none`.

Create a child record rather than overwriting a parent when the object, evidence, permitted use, identity, or scale changes. Do not let a fuller form raise the empirical or action status of its contents.

## H1-H6 Role Boundary

| Claim | Role | Permit | Stop before |
|---|---|---|---|
| H1 meaning and coordination | Empirical hypothesis requiring an eligible H1-instance | Register a conditional anchor only for one preregistered resource-allocation, action-choice, or coordination result | Shared inner life, genuine consent, common will, or enforced unity |
| H2 carrying and responsibility separation | Operating rule | Separate carrying vehicle, same-type cost bearer, beneficiary, stop right, and responsible subject | Treating capacity as duty, visibility as responsibility, or classification as a reproduction mechanism |
| H3 institutional writeback | Classification rule | Separate receipt, field change, actual execution, effective writeback, and duration | Treating intake as writeback, one writeback as learning, or an update as lasting repair |
| H4 power, mediation, and reflexivity | Empirical hypothesis requiring an eligible H4-instance | Register one preregistered effect on evidence coverage, expression safety, object behavior, or reflexive response through a specified channel | Inferring malice, consent from silence, automatic remedy, or mechanism from a “power,” “platform,” “metric,” or “AI” label |
| H5 historical trace carrier | Empirical hypothesis requiring an eligible H5-instance | Register a persistent trace in one preregistered carrier family, one matching atomic carrier, and one persistence criterion | Future path effect without a separate G3-instance, or protection and repair without later normative and authorization gates |
| H6 open-ended bearing | Normative boundary | Describe real cost, voluntariness, direction, alternatives, structural consequences, and stop rights | Diagnosing love, treating sacrifice as proof, or conscripting continued unilateral bearing |

Use the same two-stage, version-frozen, append-only evidence discipline for H1-, H4-, and H5-instances as for G-instances. Accept only `supported`, `unsupported_or_undecided`, `null_supported`, or `not_evaluated`. Freeze exactly one subtype and one allowed success criterion before results. A failed positive rule is not a supported null. H2, H3, H6, field completion, definitions, and framework prose are not empirical support. Even a supported H-instance produces description or explanation only.

## Strong Types

Keep each type independently evidenced. Allow several types in one case, but never use evidence for one to close another.

| Type | Ask and minimum evidence | Do not collapse into |
|---|---|---|
| GC generation condition | What resource, technical, institutional, relational, trauma, crisis, or opportunity condition made generation possible or more likely? Compare its timing, change or removal, outcome difference, channel, and competitors. | GS, GE, intention, or responsibility |
| GS generating subject | Who could understand and perform initiation, translation, or transfer? Check identity, capacity, resources, actual action, and authorization. | Technology, crisis, platform, metric, resource window, or the whole responsibility set |
| GE generation event | What thresholded state transition occurred and when? Compare pre-event and post-event state under one measurement contract, mechanism bridge, and concurrent events. | A personified event or an invented subject for emergence |
| CV carrying vehicle | Who or what actually executes, transmits, maintains, records, cares, or repairs? Use work logs, resource and capacity flow, cost, stop rights, and substitution effects. | RS; a nonhuman carrier has no moral or legal responsibility merely by carrying |
| RS responsible subject | Who bears what responsibility on what basis? Separate conduct, decision, authorization, supervision, benefit, and remedy, with knowledge, control, scope, period, appeal, and remedy evidence. | The most visible actor, lowest-power executor, CV, or person harmed |
| IS instability source | Where did a disturbance enter or accumulate? Locate first appearance or accumulation, entry point, timing, exposure difference, and alternatives. | Malice, IM, all responsibility, or dissenters as a source by identity |
| IM instability mechanism | Through what causal path did disturbance alter state, boundary, feedback, rhythm, or direction? Trace intermediates, timing, bridge evidence, failure conditions, and competitors. | A person, group, dissenter, or mechanism story without causal evidence |
| IB instability behavior | What action, inaction, or output was observed? Preserve actor or carrier, context, scale, window, logs, and multi-source observation. | IS, IM, malice, total responsibility, or an interpretation of silence |

Apply IS, IM, and IB across HV02, HV06, HV07, HV08, HV09, and HV10 rather than treating them as an HV09-only appendix.

## Complete HV Card Semantics

Fill all 39 fields for each invoked human variable. Use five zones:

| Zone | Fields | Required meaning |
|---|---|---|
| A identity and applicability | `id`, `qualified_id`, `name`, `proposition`, `scope`, `claim_type`, `contract_role`, `pause_condition` | Identify `human_variable:HV01` through `human_variable:HV11`, keep `claim_type=H` and `contract_role=human_variable_interface`, state the claim and where it applies, and name the condition that stops the route. |
| B dependency and inference | `allowed_inference`, `prohibited_leap`, `inferential_requires`, `protocol_requires`, `specializes`, `applies_to`, `conditional_support_routes` | State the exact allowed conclusion and forbidden elevation. Keep formal causes, method gates, specializations, and applicability relations distinct. |
| C scale and object | `scale_profile`, `effective_object`, `scale_invariants`, `required_scale_additions`, `changing_semantics`, `non_applicable_objects`, `forbidden_elevation` | Register `SP=<A,X,T,O,C,R,I,N,J>`, the object, what must remain, what must be added on scale change, what changes meaning, where the interface does not apply, and which aggregation is forbidden. |
| D state, evidence, and flow | `state`, `observables`, `evidence`, `input_dependencies`, `output_effects`, `time_window_and_lag`, `uncertainty`, `local_exclusion_zone`, `affected_positions` | Use closed states, operational observations, external evidence, input and output content, timing, uncertainty, protected or unseen positions, and the full distribution of effects. |
| E carrying, norms, and correction | `carrier`, `responsible_subject`, `normative_status`, `judgment_ceiling`, `action_ceiling`, `counterexamples`, `appeal`, `rollback` | Separate implementation from responsibility, state the non-self-authorizing normative status, cap judgment and action, retain counterexamples, and bind real appeal and rollback procedures. |

Keep the four dependency relations disjoint:

- Put prerequisites that every conclusion level needs in `inferential_requires`.
- Put epistemic, causal, source, evidence, normative, or operating gates that every level must pass in `protocol_requires`.
- Put a definition, classification rule, or normative boundary refined by the interface in `specializes`.
- Put only the object to which the interface applies in `applies_to`.

Put level-specific conditions inside `conditional_support_routes`. Fill each route with `route_id`, `claim_level`, `when`, `additional_inferential_requires`, `additional_protocol_requires`, `allowed_conclusion`, and `result_ceiling`. Read one route as a whole. Do not combine favorable fields from different routes after seeing a result. Use qualified IDs such as `human_variable:HV03`, `human_strong_type:RS`, `universal_primitive:U07`, `scale_axis:J`, and explicit `O1`-`O4`; do not use ambiguous bare `O`.

### HV01-HV11 Route Map

The table below is an orientation index only. Before invoking a route, load [human-variable-cards.json](human-variable-cards.json), select the matching ID, and preserve all 39 fields exactly as its one-to-one Appendix A map. Do not reconstruct a card from this summary.

| Interface | Base object and route | Elevation requirements and ceiling | Prohibited leap |
|---|---|---|---|
| HV01 structural domain | A D0 candidate object, material set, boundary dispute, and G1 evidence need | Only an eligible supported G1-instance permits finite domain, recognition strength, boundary credibility, and applicability window within frozen `SP/T/K` and generalization unit | Naming creates a community; shared situation creates shared will; local group represents every affected position |
| HV02 boundary and interface | Selective boundary over resources, information, rights, or responsibility; record membership, access, exit, cross-boundary flows, gatekeeping, reasons for refusal, and formal-versus-actual boundary | Describe accessibility and exclusion risk at base; require eligible G2 for a specified selective effect | Formal membership, a representative, or visibility proves representation or control |
| HV03 directional anchor | Candidate target, identity, memory, commitment, fear, or common problem with heterogeneous expression and representation dispute | Require one supported H1 result family before calling it an effective resource, action, or coordination anchor | Expression is a structural anchor; a few positive statements represent the group; meaning may be forcibly unified |
| HV04 generation node | Split GC, GS, and GE across their own nine-axis profiles | Use type separation at base; require eligible G2 for a specified generation mechanism | Conditions have intent; event proves subject; subject proves event; technology or crisis is an actor |
| HV05 carrying layer | Human, role, process, facility, or institution that executes, transmits, maintains, records, cares, or repairs; apply H2 separation | Require G2 for carrier effects, G2+G3 for intertemporal reproduction, and a supported H5 atomic carrier only to submit a trace candidate to G3 | Carrier equals responsible subject; capacity creates unlimited duty; H5 proves future path |
| HV06 motive-carrying chain | Trace candidate chain segments from HV03 through HV04 to HV05 with aligned object, scale, window, and quantity mapping | Require all linked interface records for a complete candidate chain, G2 for an effective channel, and G3 for intertemporal history | “Motivation” fills a missing carrier; one successful pass proves reproduction |
| HV07 feedback writeback | Return path that can alter later institutional state; separate submission, receipt, field versions, execution, effective date, and duration under D2 and H3 | Require G2 for causal feedback; add G3, retained update, repeated rounds, and predefined task for feedback-mediated learning | Receipt, statement, or unexecuted field change is writeback; one writeback is learning |
| HV08 conditional field | Conditions that may change action probability, expression safety, or evidence distribution; list positions, blind spots, and evidence needs | Require one supported H4 outcome for a position or mediation effect; apply E3 for an observation or publication reflexive response | The field is a willing subject; “power,” “platform,” or “AI” is a mechanism; silence is consent |
| HV09 structural load | Typed task and coordination demand relative to capacity and recovery margin at one place and window; preserve local overload hidden by averages | Describe margin, backlog, local gap, and recovery at base; require CM-LOAD plus G2 for overload mechanism and G3 for cumulative damage or delayed recovery | Universal social or psychological “entropy”; instantaneous overload proves damage, collapse, or a duty to sacrifice |
| HV10 evolutionary phase | Component assessments for HV03, HV04, HV05, and HV07 in an intentional human collective | Use those records only to assess applicability or missing components; require CM-PHASE for pattern, G2 for causal transition, and G3 for hysteresis or path dependence | S0-S6 is universal, linear, moral, personal, or authorizes advancement, elimination, or exit |
| HV11 open-ended bearing action | A human action with real cost, voluntariness, direction, alternatives, structural effect, refusal, exit, and stop-right record under H6 and N4 | Permit a bounded description only when voluntariness and real refusal are visible; require G2 for a structural effect | Diagnose love or personality, treat sacrifice as proof, or turn individual bearing into collective duty |

For every HV route, record observed, candidate, disputed, unknown, and non-applicable states without silently upgrading them. Keep the judgment ceiling at or below the supporting evidence and the action ceiling at `none` unless later, external normative and authorization procedures independently act.

## Actor State and Personality Boundary

Represent an actor as:

`A*=<actor_id, observation_window, circle_memberships, roles, slow_variables, medium_variables, fast_variables, material_conditions, experience_meaning_conditions, unknowns, evidence_state, privacy_and_allowed_use>`.

Treat the star as a reminder that this is a candidate snapshot. Do not fill the state from a name, occupation, identity, or single act.

| Time band | Candidate content | Evidence and update rule | Misuse to block |
|---|---|---|---|
| Slow | Long-term value ordering, interpretive habits, capacities and resource position, identity commitments, trust or attachment tendencies | Require cross-time or cross-context evidence. After one event, normally update support rather than value; split, revise, or retire after major restructuring or contrary contexts. | Innate essence, true self, or universal cross-context trait |
| Medium | Role identity, phase goals, relationship expectations, alliance position, accumulated fatigue, recent reputation and trust | Require repeated observations within a stage and explicit role and circle conditions. Update after relationship, project, organization, or resource changes. | Role reaction rewritten as personality |
| Fast | Immediate emotion, arousal, attention, fear, impulse, current belief, short-term bodily state, perceived opportunity, strategy | Bind to an event and time. Update after a channel actually reaches the actor. Trace thresholds and feedback before allowing persistence. | One emotion or act predicts the person's whole future |

Before raising a personality candidate, compare at least visible information, available resources, rewards and sanctions, responsibility, identity activation, and exit capacity across circles. Define a personality hypothesis in falsifiable behavioral terms; list observed and unobserved contexts, duration, sources, counterexamples, simpler role/material/strategy/measurement explanations, status, allowed use, and prohibited use. Permit only observation record, supported hypothesis, candidate, disputed, unknown, or retired. Never perform clinical or psychiatric diagnosis, unlicensed psychological assessment, discriminatory screening, automatic punishment, or essence adjudication.

Trace actor-circle effects in two directions. For circle-to-actor effects, connect a rule, event, resource, or meaning change through information, reward, bodily load, role, reputation, or belonging to a fast, medium, or slow variable. For actor-to-circle effects, connect expression, labor, refusal, exit, bridge, alliance, or innovation through resource flow, imitation, institutional writeback, network propagation, or representation to a circle field. Require a return channel, delay, threshold, and downstream change before calling the pair feedback.

Classify actor evidence as `unknown`, `candidate`, `supported_hypothesis`, `observation_record`, `disputed`, or `retired`. A post-outcome candidate may guide the next test but cannot support the prior forecast. Create a new version when its definition, time band, indicator, or allowed use changes.

Record material conditions and experience-meaning conditions in parallel. Material conditions include body, time, space, money, tools, transport, care, legal position, and actual exit capacity. Experience-meaning conditions include feeling, expectation, memory, identity, trust, shame, hope, fear, commitment, legitimacy, and value conflict. Require a named bridge and direction for cross-channel claims; neither channel erases the other.

Classify information as public, context-limited, sensitive, highly sensitive, or refused. Bind reuse to collection purpose, authority, and protection. Do not reuse communication material for employment, insurance, enforcement, medical, punitive, or public-rating purposes without a separate valid basis. Treat refusal, silence, absence, and protected opacity as missing information with an explicit effect on the ceiling.

## Human Collective State Prototypes

Apply S0-S6 only to intentional human collectives organized around an expressible problem, commitment, goal, or meaning through roles, resources, rules, relations, and feedback. Freeze object ID, `K`, nine-axis `SP`, time window, subsystem, entry, exit, observables, counterexamples, falsifiers, evidence, and missing states. Use only `single_dominant`, `mixed`, `parallel`, or `unknown` as classification modes. Require external evidence references, independent review, structured appeal and rollback, `normative_status=descriptive_only`, and no action authorization.

| Prototype | Candidate configuration | Boundary |
|---|---|---|
| S0 anchor condensation | Attention, relation, time, and limited resources begin to gather around a candidate problem or meaning while boundary, roles, commitment, and `K` remain fluid | Formation, not inferiority; it may disperse, split, sleep, or be absorbed without “failing.” |
| S1 generative-core foundation | Anchor, boundary, and at least one generative role repeat across decisions; early rules and memory appear; key functions still depend on a small core | Central dependence does not prove legitimate or permanent leadership. |
| S2 first expansion and carrying differentiation | A boundary or interface expands and carrying, cost, exit, disagreement, and unresolved participation positions differentiate beyond the core | Growth or open conflict alone is not structural development or instability. |
| S3 development under connected constraints | At least two repeated constraints reinforce one another and divide feedback, carrying, recovery, or cost return while operation continues | Do not name a person a “barrier” or authorize coercive reform. |
| S4 structural-reconfiguration window | A key relation, authority, resource path, writeback, or boundary actually changes; old and new arrangements coexist with traceable transition cost | Rebranding, personnel change, or disruption alone is not constructive reconfiguration. |
| S5 efficient coordination and elastic expansion | Key channels coordinate with relatively low loss, substitution, writeback, recovery, and flexible boundary change without silencing or hidden externalization | Output, survival, resource abundance, or low visible complaint is not enough and grants no right to expand. |
| S6 adaptive dynamic balance | Distributed carrying, feedback, recovery, renewal, succession, and local self-stabilization remain available across disturbance without one irreplaceable center | Not a final state, moral ideal, conflict-free society, or authority over other objects. |

Allow mixed and parallel states, jumps, regression relative to the same object's functions, split, merge, dormancy, takeover, functional transfer, paradigm replacement, trauma-built development, pseudo-steady state, forced rewrite, external-carrier migration, and collapse. Treat these as path candidates, not moral verdicts. Keep X0 as a separate possible orderly-exit path from any registered origin, never S7. Require independent anchor review, safe transfer or closure of functions, people and relations, resources, memory and evidence, debts and responsibility, appeal, receiving capacity, rollback, and bounded weak links before calling X0 complete. X0 itself does not authorize dissolution, dismissal, asset transfer, publication, debt release, or representative consent.

Do not use a physical metaphor without a formal mapping, dimensional account, falsifiable prediction, and termination condition. If prototypes add no value beyond direct variables, skip them.

## Multi-Circle and Joint-State Boundary

Represent each candidate circle as:

`C*=<circle_id, candidate_boundary, membership, role_rules, entry_and_exit, internal_state, external_interfaces, material_channels, experience_meaning_channels, constraints, time_window, scale_profile, identity_criterion, evidence_state, counterexamples>`.

Keep a circle as an analyst grouping until it has internal role, relation, channel, or constraint structure and finite gain over a complexity-matched alternative or no-group baseline. A circle does not require common consciousness or purpose.

Represent the joint object as:

`MC*=<A,C,Rcc,Rac,M,Psi,Q,E,T,SP,W,K>`

where `A` is actors, `C` circles, `Rcc` directed circle relations, `Rac` memberships and roles, `M` material state, `Psi` experience-meaning state, `Q` channels and constraints, `E` event flow, `T` multiple clocks, `SP` scale, `W` evidence/unknown/residual state, and `K` identity. Do not turn the joint object into a higher subject.

| Relation | Minimum criterion | Special check |
|---|---|---|
| Parallel | No current membership or operating-contract containment | Shared environment and indirect coupling; add propagation only with a channel |
| Nested | Explicit membership, role, accounting, jurisdiction, or spatial containment | Name the containment basis; inner state does not represent outer state and outer rules may not be locally executed |
| Overlapping | Shared members, roles, resources, or interfaces without full containment | Role conflict, double counting, information leakage, and exact shared items |
| Bridging | An actor, institution, interface, text, platform, or event provides an actual cross-circle path | Translation loss, filtering, representation, replaceability, overload, responsibility, and exit |
| Competitive | One circle's use, rule, or action restricts another's available resource, attention, legitimacy, commitment, interpretation, or action set | Scarcity, window, and simultaneous cooperation on another channel |
| Temporary | The circle exists around a bounded event, task, crisis, exposure, or short-term goal | End condition, traces, responsibility handoff, institutionalization, or dissolution |

Treat the relation graph as directed and multi-edged with local containment, not a tree. Register source, target, direction, shared item or interface, channel, range, window, delay, threshold, evidence, counterexample, and failure for every edge. Record transformation after an event as a before-and-after state, not a seventh relation.

For multiple membership, record entry basis, start and end, role, commitment state, actual participation, exit capacity, dispute, and representation. Separate transmission ability, representative authority, and responsibility. An actor becomes a bridge only when actual transmission changes another circle's information or state.

Keep `M` and `Psi` parallel. For every `M->Psi`, `Psi->M`, or closed-loop claim, state the source, mediator, result, direction, delay, and counterfactual. Do not require equal weights; require that neither channel be deleted.

Use at least five clocks:

| Clock | Typical state | Update trigger |
|---|---|---|
| Immediate | Emotion, attention, bodily arousal, local price | Signal arrival or direct shock |
| Interaction | Trust, strategy, relationship expectation, local norm | Multiple action-feedback rounds |
| Organizational | Role, budget, process, metric | Decision, execution, and review cycle |
| Institutional | Rule, right, responsibility, appeal, record | Valid procedure plus actual writeback |
| Long-term | Capacity, identity, infrastructure, culture, generation | Accumulation, learning, maintenance, and replacement |

Update only variables reached through a channel and threshold. Leave untouched values unchanged or mark them unknown when stale. Freeze joint snapshots with timestamp, evidence cutoff, actor and circle references, relations, memberships, `M/Psi`, channels, constraints, clocks, scale, unknowns, residuals, and `K`.

Perturb membership thresholds, time windows, and circle inclusion. Lower object support when small boundary changes reverse the result. If `K` fails, register conversion or dissolution without erasing the old object's failure, responsibility, or traces. Add a circle or relation only when it explains a named residual through an independently observable channel and improves the appropriate simple baseline enough to justify measurement and privacy cost. Otherwise return to a single actor, single circle, or continuous variable.

## Appeal, Rollback, and Protection

Make appeal safely reachable and resistant to retaliation. Provide anonymous, proxy, low-exposure, or delayed routes when risk requires them. Require review independent of the original judgment and decision chain. Preserve low-power actors, evaluated people, carriers, excluded people, dissenters, and those unable to speak publicly as affected positions.

Treat an accepted appeal as incomplete until rollback actually changes or restores the object, record, rule, resource, task, right, or downstream judgment; names an executor and deadline; preserves version history; and verifies completion. A notice, receipt, apology, or promise is not rollback. These interfaces generate procedural requirements only; they do not build the channel or authorize the change.

## Worked Example: A Project Lead Publicly Rejects a Team Plan

Freeze the observed event as a public rejection in one meeting, including wording, time, participants, immediate effects, evidence cutoff, and allowed purpose. Register it as `IB` only. Do not infer `IS`, `IM`, malice, total responsibility, or a “controlling personality” from the act.

Create an actor snapshot for the lead. Put time pressure, fatigue, threat perception, and anger in the fast-variable candidate set; project goal, formal role, recent trust, and reputation risk in the medium set; keep tolerance for uncertainty as a slow-variable candidate requiring cross-context evidence. Record organizational metrics, resource shortage, role authority, expression safety, and exit cost as circle conditions. Keep any private health or family information unknown or protected unless it is legitimately available for this purpose.

Represent the team as a candidate circle nested in the organization. Record the lead's overlapping management and team roles and the role conflict they create. Treat the rejection as an actor-to-circle input only if it reaches later resource, role, trust, expression, or record states through a named channel. Treat later team silence as missing or candidate response, not consent. A power or mediation effect remains an H4 candidate until one result family and its channel receive eligible support. Separate the lead as possible `GS` for the decision, any meeting rule or metric as `GC`, the rejection as `GE/IB` only when its state-transition contract is met, the implementing role as `CV`, and `RS` by independent knowledge, control, authorization, supervision, and remedy evidence.

Place confirmed behavior, role facts, and supported circle conditions in `claim_ledger`. Put personality, intent, hidden constraints, dissent, protected information, alternative role and resource explanations, and unobserved downstream effects in `unknowns_and_counterevidence`. Use `output_ceiling: diagnostic_only` only if the object and evidence support the bounded actor-circle diagnosis; otherwise lower it to `description_only`. Recommend `ariadne-dynamics` only if event propagation is requested. Set `authorization_effect: none`. The result may identify discriminating observations; it may not diagnose, punish, compel disclosure, or authorize a management action.
