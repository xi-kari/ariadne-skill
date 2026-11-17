# Choice and Authorization Contract

Use this reference to compare finite options, form a recommendation where its premises allow, and examine the authority and protection needed for consequential adoption. The comparison may be prose, a decision table or a formal choice record appropriate to the task. Section anchors (§) resolve through [source-navigation.json](source-navigation.json).

These are derived methods from the v2 source, not item-by-item author certification. Apply three distinct layers (Part 14 introduction): **argument principles** separate facts, values and conflicts, beneficiaries and burden bearers, and options including no action; **substantive adoption safeguards** require action-covering authority and real protection, refusal, exit, challenge, correction, remedy and expiry; **record format** specifies how Ariadne documents its own formal states. The exact component counts and field names below belong to that last layer. Another implementation may carry the same substantive responsibilities in a different format only after independent review verifies the equivalence; its implementer's assertion is insufficient. Removing something that changes who is protected, bears costs, decides, stops, or corrects removes a substantive safeguard, not mere formatting. A serialization check can reject an old record without thereby invalidating an outside institution or suspending an independently authorized duty.

## 1. Keep Four Tasks Separate

Keep these responsibilities distinct when they are needed (§15.1); reuse sound existing results rather than requiring every request to replay a fixed pipeline:

```text
explanation -> diagnosis -> normative choice -> intervention
```

- Explanation outputs descriptive or explanatory claims, evidence status, the zero model, competing explanations, and a descriptive action ceiling; never a responsibility verdict, value priority, or command.
- Diagnosis compares problems, mechanisms, and falsifiers through the tool flow without granting power.
- Normative choice identifies who may choose what, under which jurisdiction, term, and value premises. **Evaluations, recommendations, and draft rules for deliberation may be formed here once N premises and conflicts, affected positions, costs, and the no-action option are explicitly registered.** Actual adoption runs `SEL-AGT` or `SEL-GOV` and passes C12 and O1-O3; legal validity, normative legitimacy, and J authorization are verified separately; majority, stability, survival, efficiency, and model confidence never substitute.
- Intervention only consumes an existing choice and authorization; it never manufactures either. In Ariadne's formal record it binds one `selected_action`, all ten C12 components, runtime explicit N premises, O1-O4, the full protection floor, and one currently valid, independently reviewed atomic J tuple. Missing substantive authority or protection blocks the dependent intervention; missing Ariadne fields blocks Ariadne's formal endorsement, while independently verified equivalent procedures are assessed on their substance. Existing lawful duties remain in scope. Writing "we have explained it clearly", "the problem is serious", or "the goal is good" as a reason for action skips levels.

Four operational transformations (§14.1):

| Stage | Freeze | Prevent |
|---|---|---|
| O1 | Descriptive claims, evidence, scale, uncertainty, and descriptive ceiling. | Editing facts, thresholds, or evidence grades after seeing options. |
| O2 | Explicit runtime N premises, premise roles, conflicts, dissent, beneficiaries, and burden bearers. | Hiding value selection inside analysis. |
| O3 | Options including an explicit no-action baseline, choosing subject, authority source, jurisdiction, duration, J axis, and conflicts of interest; a separate normative selection record freezes the decision. | Treating influence or expertise as permission. |
| O4 | Bounded execution: reversible, monitorable, stoppable, appealable, rollback-capable, expiring. | Letting a finite choice become indefinite or irreversible. |

There is no path from "the diagnosis is severe" to direct action, or from "confidence is high" to wider authority; stronger evidence can raise the descriptive ceiling but never by itself the action ceiling. C12 does not choose values for anyone, and least harm and proportionality are selected, explained, and reviewed explicitly in the choice record rather than hidden in C12.

For a choice request, make facts, values, feasible options, the no-action baseline, affected positions and current recommendation explicit. If execution is in scope, also establish the actual jurisdiction, authority, stop conditions and remedy. State unresolved material honestly. A finite analysis does not require universal machine fields.

## 2. Two Identities: Analytic Recommendation and Authorized Choice

The source separates two outputs that older practice merged (§12.1, §12.8, §12.15, §12.16, §13.10 DF7):

| Identity | What it is | What it needs | What it never does |
|---|---|---|---|
| Analytic recommendation | A refutable preference for deliberation: the current choice, why, at what cost, the objections to it, and what would change it | Explicit normative premises, current evidence, affected positions, the option set including no action, costs and distribution | Grant execution, bind anyone, or pose as an executable decision |
| Authorized choice record | A qualified subject's selection of one option within its authority | Everything above plus C12, PF-1 to PF-10, one atomic J tuple, O1-O4, stopping, appeal, rollback, remedy, expiry | Arise from the model, from urgency, or from forecast accuracy |

**Form the analytic recommendation whenever its premises are in hand.** It does not require that a not-yet-taken execution already be authorized. Withhold it only for the specific missing norm, protection, or option that blocks it, and say which; an analysis already supported by evidence is never sent back to a question list merely because nobody has authority to execute. When norms are only N1, or no positive norm is stated, the recommendation is limited to no action, more evidence, or continued deliberation, and independent evaluations and conditional advice under stated premises remain.

Open with the current recommendation, then explain the reasons for accepting and rejecting the alternatives, costs, objections and change conditions. Report actual external adoption and authorization: preserve valid existing authority with its limits, and identify what is absent or unverified. The recommendation itself supplies no authority, and the analyst's recommendation is not the actor's adoption.

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

Keep conflicts (fast loss-stopping versus full participation, public benefit versus minority rights risk, short pilots versus long-term stability) under stable IDs with the conflicting premises, affected positions, dissent, decision rule, and status. Never flatten them into an unexplained total score or "resolve" one by deleting dissent. A conflict can pause or narrow the dependent adoption, but unavoidable losses still call for the limited recommendation described below. `rights_floor` registers the active PF IDs, which never trade against efficiency: N says what a choice rests on, PF says what no basis may cross.

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

**Every finite-choice comparison includes an explicit `no_action` baseline**: the path of not carrying out the proposed new action. If that baseline has several conditional scenarios, retain their conditions rather than assuming inaction has one certain outcome. Register existing maintenance, legal duties, and actions already under way with their continuing conditions; choosing no action does not discharge existing duties; actively maintaining the status quo is a separate option. Account in the same window for the baseline path's natural change, risk accumulation, opportunity cost, and distribution; deleting no action usually writes "something must be done" into the premises. For `no_action`, state the baseline time, expected path, observation plan, reopening conditions, and responsible subject; never model it as zero consequence. When no choice was requested, do not force an action list. For `SEL-SYS`, the extra kind `system_variant` compares outcomes under different environments or retention mechanisms; it never enters `authorized` or converts into `external_action`.

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

**From an identifiable answer to a feasible choice** (§12.10.1). A question can have an adequate answer while no action is feasible, and an action can be acceptable in every state consistent with the material before the state is identified (F3: the intersection of qualifying action sets is non-empty; see [representation-and-closure.md](representation-and-closure.md)). When the intersection is empty, check whether more evidence, waiting, narrowing the task, or a grounded protective action changes the conditions. The intersection covers only the listed credible states and explicit constraints. Risk probabilities, costs, and normative tolerance may support other selection rules, stated explicitly; never smuggle the worst-case rule in as the only rational one. Randomized or sequential strategies are analyzed separately.

**Joint feasibility of several options** (§12.10.2). Options feasible one by one may share capacity, budget, staff, or stop channels; check them together. Capacity added next period cannot recover a deadline missed this period; adding same-period capacity or obtaining an approved deadline change forms a new option and never rewrites the old task as completed. Account jointly for resource use, task dependencies, and key deadlines so departments do not promise the same resource twice; serial steps of finding, authorizing, implementing, and taking effect still need to connect. Treating the first node's completion as protection of the last affected person misjudges both time and coverage.

## 7. Compare Consequences and Distribution

Register consequences along all nine axes `SP=<A,X,T,O,C,R,I,N,J>`: immediate local benefit is not long-term system benefit, average improvement does not cover local exclusion zones, and upper-level stability does not replace lower-level loss. Keep a distribution ledger per position: benefit, cost, risk, rights impact, burden transfer, and power position (`low`, `medium`, `high`, `unknown`), covering direct, indirect, second-order, cross-domain, and intergenerational positions, with `low_power_position_ids`. Every option answers who benefits, who bears, who decides, who cannot refuse, whether costs move from high power to low power, and whether unobservable positions are being treated as absent (§14.4, §14.9). Improvement in a main circle never offsets rights harm in another; averages never cover people who cannot exit; overlapping members may bear costs twice; bridges bear translation and conflict risk; dissolved temporary circles may leave responsibility and history.

**Bound the identification responsibility** (§14.4.1). List every directly affected position, every known or pointed-out low-power position, and every position the applicable domain contract requires separately. For other indirect, second-order, cross-domain and intergenerational positions, trace the declared channels and scale axes proportionately to severity, irreversibility, population, accumulation and low power. Stop extending the search when it can no longer reasonably change the judgment, option comparison or protection arrangement. Record the searched channels, positions consulted, remaining unknowns and stopping boundary. A newly proposed channel is investigated or receives a reasoned rejection; a party benefiting from a narrower boundary cannot determine it alone. Make the grounds challengeable and obtain independent review for high impact or conflict.

Separate two kinds of unknown. A grounded possibility of protection failure or a changed option comparison blocks the affected adoption until evidence, narrowing or independently grounded protection addresses it. Other unknowns stay visible with monitoring and reopening conditions. Later-identified positions receive equal appeal, correction and remedy without proving they were foreseeable. Apply the same search responsibility to no action and maintenance of the status quo; inability to exhaust remote effects never postpones protection against known harm.

Compare each option's worst acceptable outcome on the same baseline; never substitute average benefit or aggregate net value, and keep the protection floor and low-probability high-consequence paths beside it. Least harm and proportionality are two explicit selection principles, each recorded with principle ID and version, selected option, all compared options, assessment dimensions, reasons, evidence, reviewer, review time, and state:

- `NSP-LEAST-HARM`: among all feasible options including no action, which harms are avoidable and why the selected option is the narrowest.
- `NSP-PROPORTIONALITY`: suitability, necessity, benefit against rights cost, intensity, scope, and duration, checked separately; it is not another name for "the goal is good".

The reviewer is separate from the deciding subject, reviews before any authorization transition, cites only the current registered version, and PF validity and re-review cover the selected option's validity period.

**When every feasible option leaves loss** (§14.9.1). Do not invent a costless option or return only unresolved questions. Give a reasoned recommendation for deliberation under the evidence and explicit N premises, recording:

- the preferred option, decision rule, who proposes the rule and who would have to adopt it;
- the people bearing each unmet legitimate claim or irreversible loss, why the claim remains valid, and the continuing mitigation, remedy, explanation and review duties with their owners;
- the evidence, resources or authority that would change the recommendation, and the reassessment time.

If the decision rule is disputed, give conditional recommendations under the competing rules without choosing a binding rule for the qualified subject. Before calling scarcity unavoidable, examine who controls it, whether an earlier decision or the frozen question can be challenged (§2.14), whether options costly to the decision maker were omitted, and whether the real gap is authority that could be referred to its holder. These grounds remain appealable and independently reviewable. Nonwaivable law and protection remain binding. If independent review confirms that even those cannot all be preserved together, Ariadne still cannot endorse an `authorized` option; all preservable protection continues, and a responsible external subject acts only under its own lawful or emergency authority with narrow scope, expiry and later review. Selection never cancels the losing positions' claims.

## 8. Resources, Status, Representation, and Non-Domination

Ask together about actual control of resources, equal standing within institutions, and agenda and representation, and how they support one another: do resources provide the capacity to refuse dependence; does status change entry and evidential rules; can representation actually change budgets and execution (§14.10)? The three can diverge: payments rise behind humiliating thresholds, identity is affirmed while resources stay unreachable, or same-identity representation grows while internal dissent is excluded. **Improvement in one never closes the other two.** Domination can exist without actual interference: when one side keeps power to change another's key options at will, the other pre-emptively pleases, falls silent, or limits itself. Adopting non-domination as a principle states which power is constrained how, whether decisions can be contested, and how the constrainers are held to account; it is never inferred from low conflict rates or present satisfaction, and it does not make all lawful interference domination. The range affected, the range bound by a governance structure, legal membership, and formal representation may differ: the first two find omissions and protection needs, the last two are fixed by specific institutions and authorization, and no principle by itself generates voting rights or jurisdiction. The framework's own review gates are its bounded action contract, not the only legitimate decision system for any community.

## 9. Audit Choice Quality and Governance

Before a subject says yes, check the conditions for saying no (§14.5). For `SEL-AGT` and `SEL-GOV`, the `coercion_and_choice` record states, each with status, reason, and evidence: direct or indirect coercion; whether defaults lock in through inertia, complexity, or penalty; whether information is comprehensible and symmetric; decision capacity; safe refusal; and real, affordable exit. `unknown` is not a pass. Default design is not a neutral background, and coercion includes more than orders: tied key resources, relational retaliation, identity exposure, information blockades, unbearable exit costs, and moralized care duties.

Check consent at entry and choice conditions now separately. If entry interrupted skills or tied housing, services, debt or care to staying, later non-exit has weaker evidential value; it does not renew consent. Independently grounded finite commitments remain, but past agreement never closes refusal, stopping or exit protections.

For `SEL-GOV`, the `governance_procedure` record states agenda formation (who may propose, who may exclude, when emergency procedure ends), representation (source, scope, recallability, the unrepresented), participation (safe, accessible, informed, able to change outcomes), minority protection (rights a majority cannot cancel, local exclusion zones, pause conditions), conflicts of interest among deciders, executors, evaluators, and beneficiaries, and execution accountability. **Formal participation is not real participation.** Give each dissent a stable ID, claim, position, evidence, disposition reasons, response deadline, and safe channel. Before `authorized`, material dissent that could change key facts, the protection floor, option feasibility, or valid authority is answered proportionately, or the affected part pauses; dissent is never excluded for being small or inconvenient. Value disagreement that remains after reasoned answers is kept as minority opinion under the explicit decision rule; **never fake unanimity to pass**. `authorized` is the framework's internal state for its own scope of adoption and never replaces legal validity, office, or the consent of the people concerned; emergencies need explicit temporary authority, narrowest scope, expiry, and later review.

Record separately whether people can reject a proposal, offer an alternative, challenge agenda rules, and replace or independently review the final adjudicator. Response within a fixed agenda is real response, but does not prove rule-level correction. In a high-impact or conflicted case, an unchallengeable final authority without external independent review fails N3 and PF-7. Publish the triggers for rule-level review in advance. Keep **dissent exists**, **material reasons remain unanswered**, and **protection fails** as separate findings; only the latter two block their dependent adoption. Reasoned maintenance of a correct decision is a valid review outcome and needs no symbolic concession.

## 10. Pass the C12 Bridge

This section owns the C12 component enumeration for this library, and section 11 owns the J tuple; other references cite these instead of restating them. Require all ten components:

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

Verify external authority through locatable records and appropriate independent evidence. Check the subject, object, action, territory, full validity period, revocation conditions and conflicts; a job title or a self-declared "passed" status is not sufficient. Match authority to each consequential step rather than demanding that one person possess all powers in a lawful composite procedure.

## 12. Bind PF-1-PF-10

Create exactly ten unique protection bindings (§14.8). For each, record applicability, reason, evidence, mechanism reference (resolving to a mechanism in the same record whose owner matches the responsible subject), owner, stop trigger, appeal, review, rollback, remedy, and expiry. Bare strings, ghost references, or self-declared independence are not protection.

| PF | Required protection |
|---|---|
| PF-1 | List all mandatory positions and the further positions identified under the proportionate, challengeable §14.4.1 boundary in options and distribution. |
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

Preserving protection does not promise that every person's resources, opportunities or life outcomes can remain unchanged (§14.8). Preserve actual pre-action protection arrangements as well as the named mechanisms. If an arrangement's classification as protection or outcome is disputed, treat it as protection pending review. Assess outcome losses under explicit norms, least harm, proportionality and the per-position burden ledger; aggregate gains do not erase burdens on low-power or unable-to-exit positions. Use the unavoidable-loss procedure above when no feasible option meets all legitimate claims.

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

For formal execution records, preserve the order, authority and choice in force at each consequential step, actual receipt and result, stop/expiry events and unresolved consequences. Keep completed, withdrawn, expired and rolled-back histories; a new execution requires current authority and cannot rewrite old failure. A hash chain can detect some saved-content changes, but cannot prove events occurred or that a whole log was not rewritten. Exact legacy serialization is a compatibility concern.

| Type | Task | Allowed direction | Immediate stop or reroute |
|---|---|---|---|
| T0 | Make evidence, counterexamples, refusal, and help-seeking able to enter safely; not psychological comfort and no demand to keep talking. | Anonymous, encrypted, proxy, staged submission; identity separated from facts; refusal, withdrawal, emergency stop, independent review; connection to outside professional, safety, or statutory support. | Identity exposure, retaliation, lost receiver independence, contact raising immediate risk, or lapsed authority. Without a minimum safe receiver, only low-exposure preservation and referral; never report T0 as complete. |
| T1 | Stop identifiable harm, preserve evidence and key supports, restore minimum communication and essential services while diagnosis continues. | Safe separation, reduced coupling, evidence preservation, short auto-expiring measures that are low-risk, observable, and reversible. | Growing harm, lost reversibility, unauthorized extension, rising low-power cost, suppressed appeal, or lapsed J. |
| T2 | Repair an evidence-located breakpoint in cost bearing, resource return, transmission, bad-news writeback, middle-layer carrying, responsibility, or bounded authority. | Restore oversight and feedback, support middle carriers, bounded replacement or gradual node restructuring, minimal verifiable test cuts; **old channels are never dismantled faster than replacements are built**. | Replacement not running, benefits not reaching burdened positions, bad news unable to change the plan, falling middle or end-of-chain margin, group harm over threshold, or lapsed authority. |
| T3 | Maintain slow variables, succession, multiple carriers, redundancy, and recovery margin once safety, minimum order, and key return chains show sustained evidence. | Deep-time warning, slow-variable monitoring, successors and bounded trial-and-error, multi-center carrying, periodic review, vulnerability drills. | T0-T2 resources squeezed, monitoring turning into unauthorized control, succession copying power, costs outsourced to low-power or future positions, counterexamples never changing rules. |
| T4 | Exit, transfer, or preserve evolutionary memory when staying or repairing is unsafe, infeasible, or unjustified; may be assessed directly. | Safe exit, local buffers, staged transfer, substitute carrying, consent-bounded minimal memory, settlement of care, compensation, and outstanding duties, protection of those who stay or cannot leave. | Retaliation, withdrawn consent, unsafe new carrier, excess data use, or evaded obligations. |

Three T4 clauses apply. A strategic-cost action is a candidate only when the subject is voluntary and informed, the cost is bearable, the experience is explicitly recorded, and it does not exhaust all remaining strength. Never romanticize exit as brave, loyal, mature, or the only right course, and never let it become a unilateral escape for the well-resourced or a way for responsible subjects to evade compensation, care, or legal duties. After entry into a new carrier system, re-register from the new object's T0, scale, and identity criterion; old authorizations do not carry over. Exit is not deletion from the table: wages, care, debts, compensation, knowledge handover, and record custody remain.

Do not let a T type bypass explanation, diagnosis, normative choice, C12, PF, J, or O1-O4. In an emergency, defer to valid external emergency authority for the minimum protective act and restore ordinary review promptly. For a formal intervention application, declare the D0 object, relevant nine-axis scale, identity criterion, time window, sources and affected and low-power positions, then apply the dependent main gates; a method name is not evidence and never grants access to people, data, property, services, employment, public resources, or command.

## Worked Example: Reorganization Under Attrition Risk

Treat this as an illustrative comparison, not a decision for a real workplace. Verified workload material and explicit protection/correctability premises support a recommendation for an eight-week pilot, while actual adoption depends on affected-position review, independent appeal and matching external authority.

### Finite-choice comparison

| Option | Main reason to consider it | Main cost or condition |
|---|---|---|
| Maintain current allocation | Avoid transition cost | Current overload and enforcement burdens continue |
| Mandatory team-wide reorganization | Could relieve overload quickly | Broad impact, unsettled protection and implementation risk |
| Delay while gathering protected evidence | Resolve the decisive uncertainty | Relief is delayed; waiting has a real cost |
| Eight-week workload and independent-appeal pilot | Narrower reversible test of the workload mechanism | Coordination load on burdened members; needs actual appeal capacity and expiry |
| Voluntary transfer | May give some members a safer path | Must prevent retaliation and preserve responsibilities to those who stay |
| No new structural action | Avoid an unjustified intervention | Continue existing protection and duties, observe the baseline and set a reopening date |

Current recommendation for deliberation: the bounded pilot, because it tests the leading workload account while preserving review and an exit from the trial. Count the added coordination cost and delayed relief. Reconsider if verified workload continues to rise, the trial cannot be run without additional harm, or independent appeal cannot be provided. These are reassessment conditions, not automatic authority to choose another action.

The card keeps the urgent reorganization option visible but does not treat urgency as authority. It distinguishes maintaining current rules from no action, prices the harms of delay and of not acting, and gives a current analytic recommendation with its premises, costs, objections, and change conditions. Real adoption still waits for protected participation and a matching external authorization.

Present the result as "the current analytic recommendation, for the team's deliberation, is the eight-week reversible pilot", followed by the reasons for and against every option, costs, objections, and change conditions, and then the external conditions (protection floor, independent appeal owner, atomic J tuple) that must be met before a qualified subject may select and authorize any option. Never phrase it as "Ariadne has decided" or in imperative mood.

## Legacy record compatibility

The retired suite's machine fields and serialized examples are preserved in [legacy/choice-and-authorization.md](../legacy/choice-and-authorization.md). They are for reading or converting old records, not prerequisites for the current work.
