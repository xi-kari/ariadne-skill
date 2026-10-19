# Choice and Authorization Contract

Use this reference to build a finite-choice card, form an analytic recommendation where its premises allow, and determine any intervention ceiling. Keep the choice card beside the schema-compatible common Method Record; link them by stable IDs. Section anchors (§) point to the source text named in `ariadne-skill/references/source-navigation.json`.

## 1. Keep Four Tasks Separate

Run this fixed chain (§15.1):

```text
explanation -> diagnosis -> normative choice -> intervention
```

- Explanation outputs descriptive or explanatory claims, evidence status, the zero model, competing explanations, and a descriptive action ceiling; never a responsibility verdict, value priority, or command.
- Diagnosis compares problems, mechanisms, and falsifiers through the tool flow without granting power.
- Normative choice identifies who may choose what, under which jurisdiction, term, and value premises. **Evaluations, recommendations, and draft rules for deliberation may be formed here once N premises and conflicts, affected positions, costs, and the no-action option are explicitly registered.** Actual adoption runs `SEL-AGT` or `SEL-GOV` and passes C12 and O1-O3; legal validity, normative legitimacy, and J authorization are verified separately; majority, stability, survival, efficiency, and model confidence never substitute.
- Intervention only consumes an existing choice and authorization; it never manufactures either. It binds one `selected_action`, all ten C12 components, runtime explicit N premises, O1-O4, the full protection floor, and one currently valid, independently reviewed atomic J tuple. With anything missing, execution stops and the action requirement stays at no action, evidence needs, preservation needs, continued deliberation, or an external referral. Writing "we have explained it clearly", "the problem is serious", or "the goal is good" as a reason for action skips levels.

Four operational transformations (§14.1):

| Stage | Freeze | Prevent |
|---|---|---|
| O1 | Descriptive claims, evidence, scale, uncertainty, and descriptive ceiling. | Editing facts, thresholds, or evidence grades after seeing options. |
| O2 | Explicit runtime N premises, premise roles, conflicts, dissent, beneficiaries, and burden bearers. | Hiding value selection inside analysis. |
| O3 | Options including exactly one no-action option, choosing subject, authority source, jurisdiction, duration, J axis, and conflicts of interest; a separate normative selection record freezes the decision. | Treating influence or expertise as permission. |
| O4 | Bounded execution: reversible, monitorable, stoppable, appealable, rollback-capable, expiring. | Letting a finite choice become indefinite or irreversible. |

There is no path from "the diagnosis is severe" to direct action, or from "confidence is high" to wider authority; stronger evidence can raise the descriptive ceiling but never by itself the action ceiling. C12 does not choose values for anyone, and least harm and proportionality are selected, explained, and reviewed explicitly in the choice record rather than hidden in C12.

For every action request, populate the typed Method Record choice payload: `facts`, `values`, `options` (each with `option_id`, `kind`, and `description`, exactly one of kind `no_action`), `jurisdiction`, `authorization`, `stop_conditions`, `rollback_plan`, and `analytic_recommendation` (an object or explicit `null`). Use the literal state `unknown` inside any unresolved field rather than omitting it.

## 2. Two Identities: Analytic Recommendation and Authorized Choice

The source separates two outputs that older practice merged (§12.1, §12.8, §12.15, §12.16, §13.10 DF7):

| Identity | What it is | What it needs | What it never does |
|---|---|---|---|
| Analytic recommendation | A refutable preference for deliberation: the current choice, why, at what cost, the strongest counterargument, and what would change it | Explicit normative premises, current evidence, affected positions, the option set including no action, costs and distribution | Grant execution, bind anyone, or pose as an executable decision |
| Authorized choice record | A qualified subject's selection of one option within its authority | Everything above plus C12, PF-1 to PF-10, one atomic J tuple, O1-O4, stopping, appeal, rollback, remedy, expiry | Arise from the model, from urgency, or from forecast accuracy |

**Form the analytic recommendation whenever its premises are in hand.** It does not require that a not-yet-taken execution already be authorized. Withhold it only for the specific missing norm, protection, or option that blocks it, and say which; an analysis already supported by evidence is never sent back to a question list merely because nobody has authority to execute. When norms are only N1, or no positive norm is stated, the recommendation is limited to no action, more evidence, or continued deliberation, and independent evaluations and conditional advice under stated premises remain.

In the Method Record, a non-null `analytic_recommendation` carries `option_id` (a registered option), `normative_premise_ids` (each resolving to an N claim in the ledger or a normative rule in the registry), `reasons`, `costs`, `strongest_counterargument`, `change_conditions`, and `adoption_status: deliberation_only`, and the record ceiling is `requirements_only`. In prose, open with the current analytic recommendation, then give the reasons for accepting and rejecting each option, costs, objections, and change conditions, and state plainly that real execution is not yet authorized. Never use imperative mood to dress a recommendation as an executable decision. An analyst's recommendation is not the actor's adoption.

## 3. Classify the Selection Process

| Type | Required subject and evidence | Hard boundary |
|---|---|---|
| `SEL-SYS` | A unit, environment, retention mechanism, time window, and stochastic baseline. | Describe differential retention only: forms were kept, copied, or eliminated, never that the system "judged them better". Survival, stability, popularity, or efficiency is not legitimacy. Never `authorized`, never `external_action`. |
| `SEL-AGT` | An identifiable subject, genuine options, information, capacity, safe refusal, real exit, territory, and duration. | Bind only that subject within actual authority. "Choices" produced by coercion, default lock-in, information deprivation, incapacity, unsafe refusal, or blocked exit are never free consent; not exiting is not consent, and entering a process is not continuing consent. |
| `SEL-GOV` | A bounded public object plus agenda, representation, participation, minority protection, dissent, conflicts, execution accountability, and expiring authority. | "Shared" is not "the majority speaks for all"; the range affected is not the range of jurisdiction. Headcount, volume, efficiency, self-declared representation, or legal form never alone substitutes for bounded public authority. |

These boundaries are non-convertible (§14.2).

## 4. Register N1-N5 at Runtime

List each premise actually used in `public_value_premises` with a stable ID, role (`goal`, `constraint`, or `veto`), interpretation, beneficiaries, burden bearers, dissent, and review status; an unregistered normative premise may not appear in a conclusion (§14.3).

| Premise | Runtime effect |
|---|---|
| N1: explanation does not authorize disposition | A veto gate. Alone it permits only no action, more evidence, or continued deliberation. |
| N2: protection must not degrade | Scale-up and action keep or strengthen existing low-power protection; when protective infrastructure is missing, shrink the action, not the protection. |
| N3: high-impact judgments must be correctable | Appeal, independent review, stop, withdrawal, rollback, remedy, and version writeback are really reachable. |
| N4: do not requisition love or bearing | Reject one-sided, unlimited, non-exitable sacrifice demanded in the name of love, duty, care, loyalty, or system survival. It does not cancel independently grounded bounded commitments, maintenance, contracts, or remedy duties; releasing or transferring a duty states the dependants' real carrying, term, and residual risk; it never forces a victim to stay exposed; capacity, causal contribution, benefit, fault, and remedy duty are argued separately. |
| N5: survival and selection are not legitimacy | Stability, efficiency, coherence, and selection outcomes stay in the position of consequence evidence. |

Keep conflicts (fast loss-stopping versus full participation, public benefit versus minority rights risk, short pilots versus long-term stability) under stable IDs with the conflicting premises, affected positions, dissent, decision rule, and status. Never flatten them into a total score, and never "resolve" one by deleting dissent; an unresolved material conflict can pause, narrow a pilot, or keep no action. `rights_floor` registers the active PF IDs, which never trade against efficiency: N says what a choice rests on, PF says what no basis may cross.

## 5. Build a Finite Option Set

Give each option a stable `option_id` and freeze its `kind`, action type, target object, territory, validity period, reversibility, expected impact, and distributional impact; changes create a new version or ID (§14.4). Check six kinds for applicability and give a reason for any that does not apply; never invent options to fill a count (§12.9):

| Kind | Check |
|---|---|
| `maintain_status_quo` | Hidden costs, continuing harm, lock-in, and the resources and enforcement that maintenance itself needs |
| `active_action` | Authority, irreversibility, cross-circle spillover |
| `delayed_action` | Harm caused by delay itself and lost opportunity |
| `probing_action` | Who bears the trial's cost and whether it can really be rolled back |
| `exit_or_transfer` | People unable to exit, responsibility, and preserved history |
| `no_action` | Default bias, continuing consequences, responsibility for not acting |

**Every option set has exactly one `no_action`**: the baseline path of not carrying out the proposed new action. Register existing maintenance, legal duties, and actions already under way with their continuing conditions; choosing no action does not discharge existing duties; actively maintaining the status quo is a separate option. Account in the same window for the baseline path's natural change, risk accumulation, opportunity cost, and distribution; deleting no action usually writes "something must be done" into the premises. For `no_action`, state the baseline time, expected path, observation plan, reopening conditions, and responsible subject; never model it as zero consequence. When no choice was requested, do not force an action list. For `SEL-SYS`, the extra kind `system_variant` compares outcomes under different environments or retention mechanisms; it never enters `authorized` or converts into `external_action`.

## 6. Compare Options on One Card

Compare every option on the same baseline (§12.10): description, forecast references, normative premises, affected positions, rights floor, expected path, worst acceptable outcome, cross-circle spillover, distribution of costs and benefits, information value, lock-in risk, reversibility, resource cost, executor, authorization, stop, rollback, and remedy.

| Dimension | Do not substitute |
|---|---|
| Target and path | Abstract "things get better" |
| Protection floor | Average benefit |
| Distribution | Aggregate net value |
| Cross-circle spillover | The main circle's indicator |
| Information value | Dramatic action |
| Reversibility and lock-in | Verbal promises |
| Authority | Model advice or job title |
| No action | Zero cost |

When no single scale applies, keep the multi-dimensional result and the open conflict; never force a sum. Conflicting value premises are settled by qualified subjects and procedures; the analysis shows exactly where the conflict sits and what follows, and may state a preference and reasons under published premises for deliberation, never a binding final decision for the qualified subject.

The expected value of sample information is EVSI = E_Z[max_a E(U|Z)] - max_a E(U), non-negative when information is free, negligible in effect, and leaves actions and goals unchanged. Real investigation costs time, privacy, and resources, may miss a window, or may change available actions, so net value is counted separately; two clues may change the action only when obtained together; and the value of understanding can stand on its own.

**From an identifiable answer to a feasible choice** (§12.10.1). A question can have an adequate answer while no action is feasible, and an action can be acceptable in every state consistent with the material before the state is identified (F3: the intersection of qualifying action sets is non-empty; see `ariadne-scale/references/representation-and-closure.md`). When the intersection is empty, check whether more evidence, waiting, narrowing the task, or a grounded protective action changes the conditions. The intersection covers only the listed credible states and explicit constraints. Risk probabilities, costs, and normative tolerance may support other selection rules, stated explicitly; never smuggle the worst-case rule in as the only rational one. Randomized or sequential strategies are analyzed separately.

**Joint feasibility of several options** (§12.10.2). Options feasible one by one may share capacity, budget, staff, or stop channels; check them together. Capacity added next period cannot recover a deadline missed this period; adding same-period capacity or obtaining an approved deadline change forms a new option and never rewrites the old task as completed. Account jointly for resource use, task dependencies, and key deadlines so departments do not promise the same resource twice; serial steps of finding, authorizing, implementing, and taking effect still need to connect. Treating the first node's completion as protection of the last affected person misjudges both time and coverage.

## 7. Compare Consequences and Distribution

Register consequences along all nine axes `SP=<A,X,T,O,C,R,I,N,J>`: immediate local benefit is not long-term system benefit, average improvement does not cover local exclusion zones, and upper-level stability does not replace lower-level loss. Keep a distribution ledger per position: benefit, cost, risk, rights impact, burden transfer, and power position (`low`, `medium`, `high`, `unknown`), covering direct, indirect, second-order, cross-domain, and intergenerational positions, with `low_power_position_ids`. Every option answers who benefits, who bears, who decides, who cannot refuse, whether costs move from high power to low power, and whether unobservable positions are being treated as absent (§14.4, §14.9). Improvement in a main circle never offsets rights harm in another; averages never cover people who cannot exit; overlapping members may bear costs twice; bridges bear translation and conflict risk; dissolved temporary circles may leave responsibility and history.

Compare each option's worst acceptable outcome on the same baseline; never substitute average benefit or aggregate net value, and keep the protection floor and low-probability high-consequence paths beside it. Least harm and proportionality are two explicit selection principles, each recorded with principle ID and version, selected option, all compared options, assessment dimensions, reasons, evidence, reviewer, review time, and state:

- `NSP-LEAST-HARM`: among all feasible options including no action, which harms are avoidable and why the selected option is the narrowest.
- `NSP-PROPORTIONALITY`: suitability, necessity, benefit against rights cost, intensity, scope, and duration, checked separately; it is not another name for "the goal is good".

The reviewer is separate from the deciding subject, reviews before any authorization transition, cites only the current registered version, and PF validity and re-review cover the selected option's validity period.

## 8. Resources, Status, Representation, and Non-Domination

Ask together about actual control of resources, equal standing within institutions, and agenda and representation, and how they support one another: do resources provide the capacity to refuse dependence; does status change entry and evidential rules; can representation actually change budgets and execution (§14.10)? The three can diverge: payments rise behind humiliating thresholds, identity is affirmed while resources stay unreachable, or same-identity representation grows while internal dissent is excluded. **Improvement in one never closes the other two.** Domination can exist without actual interference: when one side keeps power to change another's key options at will, the other pre-emptively pleases, falls silent, or limits itself. Adopting non-domination as a principle states which power is constrained how, whether decisions can be contested, and how the constrainers are held to account; it is never inferred from low conflict rates or present satisfaction, and it does not make all lawful interference domination. The range affected, the range bound by a governance structure, legal membership, and formal representation may differ: the first two find omissions and protection needs, the last two are fixed by specific institutions and authorization, and no principle by itself generates voting rights or jurisdiction. The framework's own review gates are its bounded action contract, not the only legitimate decision system for any community.

## 9. Audit Choice Quality and Governance

Before a subject says yes, check the conditions for saying no (§14.5). For `SEL-AGT` and `SEL-GOV`, the `coercion_and_choice` record states, each with status, reason, and evidence: direct or indirect coercion; whether defaults lock in through inertia, complexity, or penalty; whether information is comprehensible and symmetric; decision capacity; safe refusal; and real, affordable exit. `unknown` is not a pass. Default design is not a neutral background, and coercion includes more than orders: tied key resources, relational retaliation, identity exposure, information blockades, unbearable exit costs, and moralized care duties.

For `SEL-GOV`, the `governance_procedure` record states agenda formation (who may propose, who may exclude, when emergency procedure ends), representation (source, scope, recallability, the unrepresented), participation (safe, accessible, informed, able to change outcomes), minority protection (rights a majority cannot cancel, local exclusion zones, pause conditions), conflicts of interest among deciders, executors, evaluators, and beneficiaries, and execution accountability. **Formal participation is not real participation.** Give each dissent a stable ID, claim, position, evidence, disposition reasons, response deadline, and safe channel. Before `authorized`, material dissent that could change key facts, the protection floor, option feasibility, or valid authority is answered proportionately, or the affected part pauses; dissent is never excluded for being small or inconvenient. Value disagreement that remains after reasoned answers is kept as minority opinion under the explicit decision rule; **never fake unanimity to pass**. `authorized` is the framework's internal state for its own scope of adoption and never replaces legal validity, office, or the consent of the people concerned; emergencies need explicit temporary authority, narrowest scope, expiry, and later review.

## 10. Pass the C12 Bridge

This section owns the C12 component enumeration for the whole suite, and section 11 owns the J tuple; other references cite these instead of restating them. Require all ten components:

1. `descriptive_or_explanatory_claim_ids`
2. `current_evidence_and_epistemic_constraints`
3. `explicit_normative_premise_ids`
4. `normative_conflict_record`
5. `protection_floor_status`
6. `authorization_and_jurisdiction_record`
7. `options_including_no_action`
8. `operational_procedure_records`
9. `action_ceiling`
10. `stop_review_rollback_and_remedy`

C12 is a validity gate, not a value selector and not an authorization issuer (§4.10). All ten passing forms a bounded proposal that may enter real adoption. An analytic recommendation for deliberation needs explicit normative premises, evidence, and costs, but not yet-granted execution authority. If only N1 is present, or no positive N premise exists, the result is no action, more evidence, or continued deliberation. With any explicit N premise, PF requirement, J record, or O1-O4 record absent, stop before real-world disposition.

## 11. Require Atomic J Coverage

Use one valid J tuple that simultaneously covers (§14.6):

```text
(decision subject, target object, one action, territory, complete validity interval, authority source)
```

Never combine partial tuples. The option's territory equals the tuple's scope and its validity interval lies within the term; the selection record, selected option, external `selected_action`, and J tuple match field by field. An authority source existing is not legal validity, which is not normative legitimacy; O3 records them separately. Keep observation range, impact range, technical reach, legal validity, normative legitimacy, and authorization distinct.

**Composite procedures** (intake, adjudication, preservation, service, enforcement carried on lawfully by different subjects) check each step's authority and premises separately and state how one step's result becomes the next step's valid input; incomplete tuples are never stitched together, and a lawful composite procedure is not declared invalid because no single person holds all the authority. Personal consent, private mandate, public office, and an organization's lawfully obtained standing to request may each be valid; a public act not requiring a private mandate does not mean the person consented.

Verify external records through stable IDs and independent evidence. Write every external verification reference with four fields: `record_type`, the external record ID, the reported status, and an independent `verification_ref`. Keep every `record_id`, `verification_ref`, and procedure ID an external reference without leading or trailing whitespace. Treat `none`, `self`, `self:*`, `GHOST`, and their case or whitespace variants as invalid tokens, and treat self-reported status strings such as `selection:passed`, `C12:passed`, or `J:authorized` as equally invalid. The module links to and checks external records and keeps `authorization_effect: none`.

## 12. Bind PF-1-PF-10

Create exactly ten unique protection bindings (§14.8). For each, record applicability, reason, evidence, mechanism reference (resolving to a mechanism in the same record whose owner matches the responsible subject), owner, stop trigger, appeal, review, rollback, remedy, and expiry. Bare strings, ghost references, or self-declared independence are not protection.

| PF | Required protection |
|---|---|
| PF-1 | List every affected and low-power position in options and distribution. |
| PF-2 | Provide anonymous, proxy, or low-exposure submission. |
| PF-3 | Make refusal and stopping effective; past consent is not permanent consent. |
| PF-4 | Provide a timed appeal that can change the result. |
| PF-5 | Protect evidence, dissent, refusal, stopping, appeal, and exit from retaliation. |
| PF-6 | Permit evidence supplementation, dispute annotation, source correction, and downstream synchronization. |
| PF-7 | Trigger external independent review for high impact, conflicts, or failed internal correction. |
| PF-8 | Make withdrawal, rollback, repair, and authoritative writeback operational. |
| PF-9 | Provide real exit or transfer; where exit is impossible, provide proxy and substitute support. |
| PF-10 | Freeze the action ceiling, forbidden acts, stop triggers, responsible subject, and review time. |

For human, sentient, mixed, or unknown objects, all ten stay active and any pending, failed, or not-applicable item blocks `authorized`. A human-specific mechanism may be `not_applicable` with a reason only when the object and downstream use together prove purely nonhuman impact; PF-10 and real-world J, responsibility, stopping, review, rollback, and expiry gates always stay. Reopen applicability when use changes. Protection never degrades with direction of scale: from local to whole, short to long term, or one relationship to an institution or platform, protection is kept or strengthened, and when a larger scale hides low-power positions, restore local records, narrow the action, and raise protection. The floor provides minimum procedural and burden constraints and does not exhaust substantive rights: the ten mechanisms do not by themselves justify any allocation of income, eligibility, care, or property, and independently grounded rights did not begin to exist when this table was filled.

## 13. Control State, Ceiling, and Correction

Use only these append-only states (§14.7):

```text
draft -> under_review -> authorized -> paused -> stopped -> rolled_back -> closed
```

Record the prior state, time, responsible subject, and basis for every transition. `draft` organizes material and compares options within existing valid authority and grants no new intervention power. `under_review` may state preservation needs, but real protection, freezing, evidence-gathering, or reversible probing still needs independent valid authority (existing statutory duties or emergency powers are recorded within their own scope). Only `SEL-AGT` or `SEL-GOV` reach `authorized`, capped at the one selected and authorized option. `paused` (failed facts, protection, authority, procedure, or monitoring) and pending review never by themselves authorize freezing resources, restricting movement, collecting information, or continuing intervention. `stopped` ends execution on a registered trigger, revoked authority, expiry, or a prohibited act, under the stop procedure, with safe withdrawal and independent remedy duties checked, without waiting for a new theoretical reason. `rolled_back` completes the declared restoration and starts verifiable remedy and version writeback. `closed` follows only when open harms, appeals, remedies, and record duties are settled or formally transferred.

The final action ceiling is the narrowest intersection of the descriptive ceiling, normative principles, protection floor, selected option, J tuple, O4 trial scope, reversibility, and expiry. Any one tightening tightens the whole; an unknown or failed item is never offset by strength elsewhere.

Appeal is reachable, timed, and able to change records or actions, and high-impact or conflicted cases reach external independent review. Anti-retaliation covers evidence, dissent, refusal, stopping, appeal, and exit. Rollback restores an acceptable state, corrects authoritative records, synchronizes downstream versions, remedies real harm, and tracks residual harm. Every authorization has an expiry and lapses automatically; continuing needs reauthorization, never default renewal. **Correction has four endpoints**: the objection is safely heard; the evidence is understood; a competent authority actually changes the wrong decision; resources and rights are restored and reach the person. Each earlier step has its own value but never closes a later one; a higher reversal rate is not automatically better; rollback cannot make harm already done, missed opportunities, or others' costs disappear.

## 14. Action Ceilings and Informational Trials

Evidence, reversibility, authority, and protection together set the action ceiling (§12.11). With weak evidence, high risk, irreversibility, or insufficient authority, first observe, narrow the action, improve information, protect affected people, open appeal, or do nothing for now. An informational trial is not a responsibility-free small step: it states its subjects, affected people, minimum scope, reversibility, stop, data use, and remedy; low-power positions are never calibration material, and without real exit there is no voluntary participation.

| Situation | Ceiling |
|---|---|
| Weak evidence, low harm, reversible, clear authority | Small-scope observation or probing |
| Moderate evidence, controllable harm, rollback-capable | Staged action with strong stop gates |
| Strong evidence, insufficient authority | Submit to the competent subject; do not execute |
| Strong evidence, irreversible, protection unmet | Pause to complete procedure and protection |
| Urgent safety threat | Only the minimal protective act under external emergency authority, with prompt review |

## 15. When Not to Act, and When Inaction Needs Stricter Review

Current no action or protective observation is supported when object facts are unclear; when an irreversible step rests on thin evidence; when authority is missing; when the protection floor is unmet; when costs would be passed to people who cannot exit; when neither simple nor complex models can separate the paths; or when outside intervention could interrupt an existing recovery (§12.14).

No action needs stricter review when harm is ongoing, inaction entrenches incumbent advantage, the responsible subject has clear legal duties or commitments, low-power positions cannot exit on their own, delay creates irreversible lock-in, or "waiting for more evidence" becomes indefinite postponement. Review `no_action` then at the same tier as `active_action`, with the same C12 bridge and PF bindings, and register the minimum protection, disclosure, appeal access, or interim carrying that remains required even without a main action.

## 16. Route Intervention Tasks Without Turning Them Into Stages

T0-T4 are intervention task types, not maturity ranks or a mandatory sequence (§15.2); the machine contract, including entry conditions, success scope, exit continuity, and the execution-state log, is the companion `intervention-levels.json`. Re-select the task when the object, scale, identity criterion, time, jurisdiction, affected positions, or action changes. Weak signals, low power, inability to exit, and anti-retaliation are hard gates on whether to act.

Chain the `execution_state_log`: append state events in order, close each event with the previous event's hash and its own hash, and register the event count, head hash, and current state with an external anchor. Keep in every event the full choice as of that moment plus the `selected_action`, C12, unique J, and O1-O4 references. Terminal `rolled_back`, `completed`, `expired`, and `withdrawn` records never return to active; continuing requires new selection, authorization, and execution records. Keep the current execution state equal to the state of the complete 17-field choice record. A hash chain only checks linkage and byte changes of saved content; it cannot prove the log was not rewritten as a whole, that events happened, or that the anchor is independent.

| Type | Task | Allowed direction | Immediate stop or reroute |
|---|---|---|---|
| T0 | Make evidence, counterexamples, refusal, and help-seeking able to enter safely; not psychological comfort and no demand to keep talking. | Anonymous, encrypted, proxy, staged submission; identity separated from facts; refusal, withdrawal, emergency stop, independent review; connection to outside professional, safety, or statutory support. | Identity exposure, retaliation, lost receiver independence, contact raising immediate risk, or lapsed authority. Without a minimum safe receiver, only low-exposure preservation and referral; never report T0 as complete. |
| T1 | Stop identifiable harm, preserve evidence and key supports, restore minimum communication and essential services while diagnosis continues. | Safe separation, reduced coupling, evidence preservation, short auto-expiring measures that are low-risk, observable, and reversible. | Growing harm, lost reversibility, unauthorized extension, rising low-power cost, suppressed appeal, or lapsed J. |
| T2 | Repair an evidence-located breakpoint in cost bearing, resource return, transmission, bad-news writeback, middle-layer carrying, responsibility, or bounded authority. | Restore oversight and feedback, support middle carriers, bounded replacement or gradual node restructuring, minimal verifiable test cuts; **old channels are never dismantled faster than replacements are built**. | Replacement not running, benefits not reaching burdened positions, bad news unable to change the plan, falling middle or end-of-chain margin, group harm over threshold, or lapsed authority. |
| T3 | Maintain slow variables, succession, multiple carriers, redundancy, and recovery margin once safety, minimum order, and key return chains show sustained evidence. | Deep-time warning, slow-variable monitoring, successors and bounded trial-and-error, multi-center carrying, periodic review, vulnerability drills. | T0-T2 resources squeezed, monitoring turning into unauthorized control, succession copying power, costs outsourced to low-power or future positions, counterexamples never changing rules. |
| T4 | Exit, transfer, or preserve evolutionary memory when staying or repairing is unsafe, infeasible, or unjustified; may be assessed directly. | Safe exit, local buffers, staged transfer, substitute carrying, consent-bounded minimal memory, settlement of care, compensation, and outstanding duties, protection of those who stay or cannot leave. | Retaliation, withdrawn consent, unsafe new carrier, excess data use, or evaded obligations. |

Three T4 clauses apply. A strategic-cost action is a candidate only when the subject is voluntary and informed, the cost is bearable, the experience is explicitly recorded, and it does not exhaust all remaining strength. Never romanticize exit as brave, loyal, mature, or the only right course, and never let it become a unilateral escape for the well-resourced or a way for responsible subjects to evade compensation, care, or legal duties. After entry into a new carrier system, re-register from the new object's T0, scale, and identity criterion; old authorizations do not carry over. Exit is not deletion from the table: wages, care, debts, compensation, knowledge handover, and record custody remain.

Do not let a T type bypass explanation, diagnosis, normative choice, C12, PF, J, or O1-O4. In an emergency, defer to valid external emergency authority for the minimum protective act and restore ordinary review promptly. Before any domain application, freeze the D0 object, nine-axis scale, identity criterion, time window, sources, and affected and low-power positions, then run the seven main gates; a module name is not evidence and never grants access to people, data, property, services, employment, public resources, or command.

## Worked Example: Reorganization Under Attrition Risk

Treat this as an illustrative choice record, not a decision for a real workplace. The team lead asked which option to take. A framing root froze the object and task at `description_only`; the choice child below admits the verified workload export and fulfills the premise-registration protocol, which together raise it to `requirements_only` so that an analytic recommendation can be recorded.

### Finite-choice card

```yaml
choice_id: CH-TEAM-022
selection_type: SEL-GOV
record_state: draft
O1:
  descriptive_claims: [E-workload-verified, FC-F-TEAM-017]
  evidence_ceiling: diagnostic_only
  uncertainty: The forecast has ordinal support and a small sample; no calibrated probability exists.
O2:
  premises:
    - {id: N2-protect, role: veto, interpretation: Do not lower protection for low-power team members.}
    - {id: N3-correctable, role: constraint, interpretation: Any high-impact result must be appealable and reversible.}
    - {id: N5-continuity, role: veto, interpretation: Organizational continuity does not justify avoidable rights harm.}
  unresolved_conflicts: [speed-versus-participation, workload-relief-versus-transfer-burden]
options:
  - {option_id: OPT-STATUS, kind: maintain_status_quo, summary: Continue current allocation with existing enforcement.}
  - {option_id: OPT-ACT, kind: active_action, summary: Immediate team-wide mandatory reorganization.}
  - {option_id: OPT-DELAY, kind: delayed_action, summary: Delay structural change while gathering protected evidence.}
  - {option_id: OPT-TRIAL, kind: probing_action, summary: Eight-week workload and independent-appeal pilot with automatic expiry.}
  - {option_id: OPT-EXIT, kind: exit_or_transfer, summary: Voluntary transfer with no retaliation or record penalty.}
  - {option_id: OPT-NONE, kind: no_action, summary: Do not change structure; continue protection, observation, and a fixed reopening review.}
analytic_recommendation:
  option: OPT-TRIAL
  status: deliberation_only
  reasons: Narrowest reversible step that tests the workload mechanism behind P1 while keeping appeal independent.
  costs: Eight weeks of coordination load on the two most burdened members; delayed structural relief.
  strongest_counterargument: Immediate reorganization would relieve overload sooner if the forecast is right.
  change_conditions: Switch to OPT-ACT if verified weekly hours keep rising for three weeks; to OPT-NONE if the independent appeal owner cannot be confirmed.
C12_status: incomplete
missing_for_execution: [verified protection floor, atomic J tuple, affected-position review, independent appeal owner]
authorization_effect: none
```

The card keeps the urgent reorganization option visible but does not treat urgency as authority. It distinguishes maintaining current rules from no action, prices the harms of delay and of not acting, and gives a current analytic recommendation with its premises, costs, strongest objection, and change conditions. Real adoption still waits for protected participation and a matching external authorization.

### Linked Method Record lineage

<!-- method-record-lineage-example:start -->
```yaml
- record_id: ariadne:team-choice:root:v1
  schema_version: '2.0'
  record_version: 1
  lineage_kind: root
  parent_record_id: null
  parent_records: []
  request_type: finite_choice
  object_contract:
    boundary: Work-allocation and appeal arrangements for the frozen 24-person product team; exclude employment termination
      and compensation changes.
    state_variables:
    - workload distribution
    - appeal access
    - departure notices
    relations_or_transitions:
    - candidate options under comparison
    interfaces:
    - protected participation
    - independent appeal
    - management authority
    time_window: Review now; any trial may last no more than eight weeks.
    scale_profile:
      aggregation: individual distribution within one team
    identity_criterion: A change to team, action, territory, or duration requires a new choice version.
    task_profile:
      target_query: Which option to put to the team for deliberation, and what blocks real adoption
      horizon: The next eight weeks
      environment: Current workload, appeal process, and management authority
      allowed_operations: Analysis and recommendation for deliberation; no execution
      error_tolerance: Ordinal comparison of options under the registered premises
    status: candidate
  evidence_cutoff:
    as_of: '2026-08-31T16:00:00+08:00'
    included_source_ids:
    - SRC-HR-HISTORY
    - SRC-HOURS-CUTOFF
    - SRC-APPEAL-CUTOFF
    excluded_after_cutoff: true
  scale_scope:
    source: individual and team records
    target: bounded team choice
    transform_kind: scale
    transform_status: candidate
  claim_ledger: []
  rule_registry: []
  unknowns_and_counterevidence:
    unknowns:
    - 'unknown: verified weekly hours per member'
    - 'unknown: normative premises of the deciding team'
    counterevidence: []
  conflicts: []
  output_ceiling: description_only
  ceiling_transition:
    operation: root
    inputs: []
    basis: []
    result: description_only
  module_runs:
  - module: ariadne-framing
    status: completed
    input_records: []
    output_record:
      record_id: ariadne:team-choice:root:v1
      record_version: 1
  module_payloads: []
  recommended_next_modules:
  - ariadne-evidence
  - ariadne-choice
  authorization_effect: none
- record_id: ariadne:team-choice:choice:v2
  schema_version: '2.0'
  record_version: 2
  lineage_kind: linear
  parent_record_id: ariadne:team-choice:root:v1
  parent_records:
  - record_id: ariadne:team-choice:root:v1
    record_version: 1
  request_type: finite_choice
  object_contract:
    boundary: Work-allocation and appeal arrangements for the frozen 24-person product team; exclude employment termination
      and compensation changes.
    state_variables:
    - workload distribution
    - appeal access
    - departure notices
    - transfer availability
    relations_or_transitions:
    - status quo
    - mandatory reorganization
    - delay
    - reversible trial
    - transfer
    - no action
    interfaces:
    - protected participation
    - independent appeal
    - management authority
    - execution monitor
    time_window: Review now; any trial may last no more than eight weeks.
    scale_profile:
      aggregation: individual distribution within one team
      impact: direct and household spillover
      jurisdiction: unverified team-level authority
    identity_criterion: A change to team, action, territory, or duration requires a new choice version.
    task_profile:
      target_query: Which option to put to the team for deliberation, and what blocks real adoption
      horizon: The next eight weeks
      environment: Current workload, appeal process, and management authority
      allowed_operations: Analysis and recommendation for deliberation; no execution
      error_tolerance: Ordinal comparison of options under the registered premises
    status: candidate
  evidence_cutoff:
    as_of: '2026-09-07T16:00:00+08:00'
    included_source_ids:
    - SRC-HR-HISTORY
    - SRC-HOURS-CUTOFF
    - SRC-APPEAL-CUTOFF
    - SRC-WORKLOAD-VERIFIED
    excluded_after_cutoff: true
  scale_scope:
    source: individual and team evidence
    target: bounded team choice
    transform_kind: scale
    transform_status: audited
  claim_ledger:
  - claim_id: E-workload-verified
    claim_type: E
    text: Verified weekly hours exceed the registered team norm for six of 24 members.
    status: supported
    support_ids:
    - SRC-WORKLOAD-VERIFIED
    counterevidence_ids: []
    support_rule_ids: []
  - claim_id: N2-protect
    claim_type: N
    text: The choice must not lower protection for low-power positions.
    status: supported
    support_ids: []
    counterevidence_ids: []
    support_rule_ids:
    - RULE:N2-protect
  - claim_id: N3-correctable
    claim_type: N
    text: Any high-impact result must remain appealable and reversible.
    status: supported
    support_ids: []
    counterevidence_ids: []
    support_rule_ids:
    - RULE:N3-correctable
  - claim_id: O-recommendation
    claim_type: O
    text: The eight-week reversible pilot is the current analytic recommendation for deliberation; it is not authorized
      for execution.
    status: candidate
    support_ids:
    - E-workload-verified
    counterevidence_ids: []
    support_rule_ids: []
    depends_on:
    - E-workload-verified
    - N2-protect
    - N3-correctable
  - claim_id: O-authority
    claim_type: O
    text: No selected action has a verified atomic J authorization.
    status: unresolved
    support_ids: []
    counterevidence_ids: []
    support_rule_ids: []
  rule_registry:
  - rule_id: RULE:N2-protect
    rule_type: normative
    text: Affected positions and the rights floor must be explicit and protection may not degrade.
  - rule_id: RULE:N3-correctable
    rule_type: normative
    text: High-impact results must keep reachable appeal, review, and rollback.
  - rule_id: RULE:premises-registered
    rule_type: protocol
    text: Normative premises, conflicts, affected positions, the option set with no action, and costs are registered
      before an analytic recommendation.
  unknowns_and_counterevidence:
    unknowns:
    - 'unknown: the independent appeal owner and full affected-position distribution are not verified'
    - 'unknown: atomic J authorization for any option'
    counterevidence:
    - Immediate reorganization may relieve overload sooner if P1 is right, but may create irreversible burden before
      protected participation occurs.
  conflicts: []
  output_ceiling: requirements_only
  ceiling_transition:
    operation: raise
    inputs:
    - record_id: ariadne:team-choice:root:v1
      record_version: 1
      ceiling: description_only
    basis:
    - basis_kind: external_evidence
      basis_id: SRC-WORKLOAD-VERIFIED
    - basis_kind: protocol_fulfillment
      basis_id: RULE:premises-registered
    result: requirements_only
  module_runs:
  - module: ariadne-choice
    status: completed
    input_records:
    - record_id: ariadne:team-choice:root:v1
      record_version: 1
    output_record:
      record_id: ariadne:team-choice:choice:v2
      record_version: 2
  module_payloads:
  - module: ariadne-choice
    payload:
      facts:
      - Verified workload records show six of 24 members over the registered norm
      - The attrition forecast gives P1 medium ordinal support without a calibrated probability
      values:
      - Do not lower protection for low-power positions
      - Keep any high-impact result appealable and reversible
      options:
      - option_id: OPT-STATUS
        kind: maintain_status_quo
        description: Continue current allocation with existing enforcement.
      - option_id: OPT-ACT
        kind: active_action
        description: Immediate team-wide mandatory reorganization.
      - option_id: OPT-DELAY
        kind: delayed_action
        description: Delay structural change while gathering protected evidence.
      - option_id: OPT-TRIAL
        kind: probing_action
        description: Eight-week workload and independent-appeal pilot with automatic expiry.
      - option_id: OPT-EXIT
        kind: exit_or_transfer
        description: Voluntary transfer with no retaliation or record penalty.
      - option_id: OPT-NONE
        kind: no_action
        description: No structural change; continue protection, observation, and a fixed reopening review.
      jurisdiction: unknown
      authorization: unknown
      stop_conditions:
      - Protection floor, appeal access, or rollback capacity fails
      - Verified weekly hours rise for three consecutive weeks
      rollback_plan: Restore the pre-trial work and record state; responsible owner remains external and unverified.
      analytic_recommendation:
        option_id: OPT-TRIAL
        normative_premise_ids:
        - N2-protect
        - N3-correctable
        reasons:
        - Narrowest reversible step that tests the workload mechanism behind P1
        - Keeps appeal independent of the reorganizing line manager
        costs:
        - Eight weeks of extra coordination load on the two most burdened members
        - Structural relief is delayed compared with immediate reorganization
        strongest_counterargument: Immediate reorganization would relieve overload sooner if the forecast is right.
        change_conditions:
        - Switch to OPT-ACT if verified weekly hours keep rising for three weeks
        - Switch to OPT-NONE if the independent appeal owner cannot be confirmed
        adoption_status: deliberation_only
  recommended_next_modules:
  - ariadne-audit
  authorization_effect: none
```
<!-- method-record-lineage-example:end -->

Present the result as "the current analytic recommendation, for the team's deliberation, is the eight-week reversible pilot", followed by the reasons for and against every option, costs, the strongest objection, and change conditions, and then the external conditions (protection floor, independent appeal owner, atomic J tuple) that must be met before a qualified subject may select and authorize any option. Never phrase it as "Ariadne has decided" or in imperative mood.
