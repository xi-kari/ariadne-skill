# Governance and Lifecycle Contract

Sections 10-16 of the audit contract: consensus and version authority, lifecycle and retirement, registries and writeback, challenge protection, capture detection, appeal and rollback testing, and orderly death. The gate flow itself (sections 1-9 and the worked example) lives in [gates-core.md](gates-core.md). These sections carry the source governance numbering family `GOV-01`-`GOV-24`; the shipped text instantiates a qualified reference where a specific clause is applied (for example `GOV-07` in the observation-recursion cap) and otherwise keeps the family as source-document numbering rather than re-deriving all twenty-four clauses. Section anchors (§) point to the source text named in `ariadne-skill/references/source-navigation.json`.

The framework never proves its own safety in its own language (§16 opening): internal consistency, passed stress tests and validators, and complete reports prove only that process artifacts exist, not real safety, effective repair, affected people's consent, or any authorization. Implementations turn these boundaries into checkable constraints: internal states cannot self-certify reality, governance records never generate authorization, terminal records never erase history, and formal adoption needs proportionate external review or approval. Whether a rule is actually implemented and running in some software is verified separately; the text's requirement is not implementation evidence. These state and authority rules govern the framework's own texts, modules, formal claims, governance changes, and related high-impact uses; they do not replace any jurisdiction's legal procedure, and an outside institution not using these formats is not thereby nonexistent or invalid.

## 10. Govern Consensus and Version Authority

Require seven steps for a governance change:

1. Register the issue, proposed concept, major rewrite, root change, misuse, or counterexample.
2. Publish cases, counterexamples, user feedback, external research, practice failures, and ethical risks.
3. Identify affected users, judged subjects, low-power positions, and scenarios.
4. Provide a safe dissent channel for affected, low-power, nonexpert, and external critics.
5. Match decision authority to the change class; do not use one permission level for minor edits and root changes.
6. Preserve unaccepted minority positions as counterexamples or unresolved issues.
7. Write the introduction, deletion, restriction, downgrade, reason, withdrawal evidence, and downstream effects to the version log.

Give every dissent a disposition, reason, evidence, and concrete effect on text, process, or action ceiling (§16.2). Bind accepted effects to actual `change_id` entries. A process that excludes the possibility of dissent triggering a necessary correction is `nominal_only` and can never restore a suspended module. `applied` does not require symbolically accepting at least one dissent; it requires that every reason able to change a key judgment, protection, or authority received proportionate handling. Whether a dissent decides the outcome follows criteria published beforehand, appealable, and independently reviewable, never self-certified by the proposer or the majority. Upholding a correct decision with reasons can be a qualified review; a needed correction left undone is never replaced by a response record. `applied` states only internal adoption conditions; it proves no real-world effect and grants no external authority.

Resolve canonical actors, evidence, interests, authorization, external review, dissent, and structured VERSION-LOG entries through runtime registries. Do not use aliases as identity, self-declared independence, internal signatures as external approval, or an issuer who is also the holder or proposer.

## 11. Apply Lifecycle, Downgrade, and Retirement Rules

Correction separates three objects (§16.3, GOV-03). A specific instance claim can be overturned by proportionate counterevidence. A generalization across instances, or a claimed coverage range, can be limited by counterexamples inside that range. **The G1-G4 question families have no independent empirical truth value as a classification**: they are kept, narrowed, or retired according to whether they omit important questions, reduce confusion, impose use burden, and add net benefit over professional or leaner baselines; several positive instances never prove a family exhaustive or the classification optimal.

Use append-only lifecycle transitions:

| Subject | In-service states | Terminal states |
|---|---|---|
| Question family or module | `normal_use`, `boundary_restricted`, `suspended`, `replacement_competition` | `retired_from_core` |
| Public assertion | `internal_draft`, `open_assertion`, `publishable`, `downgraded`, `suspended`, `publication_blocked` | `withdrawn`, `replaced` |
| Framework | `active`, `boundary_restricted`, `suspended`, `replacement_competition` | `replaced`, `retired` |

Management states are use and maintenance policies; they never stand in for a claim's evidence status. Do not create an edge from a terminal state back to active service, and never use rollback to restore an old authorization. Give any successor a new identity, new external authority, and a link to the preserved terminal history.

Trigger review for repeated counterexamples, stable misclassification of a class of subjects, steadily widening interpretation, evasion through "the other side is not a system", "not enough time yet", or "the evidence is not deep enough", high-harm misuse, capture, inaccessible correction, calibration decline, or a safer simpler replacement. Match the disposition to the counterexample's argumentative role:

- Let a local counterexample tighten a boundary.
- Let repeated systematic failure open replacement comparison and downgrade the claim.
- Let a high-harm misuse suspend the use.
- Let misuse block publication.
- Let an irreparable application enter exit or transfer review.
- When review does not refute the original claim, keep the reasons and its failure conditions.

Never force a correct claim to change just to show responsiveness, and never place every counterexample outside the theory. Check object, measurement, auxiliary conditions, mechanism, and extrapolation range before choosing local revision or core replacement; **a local revision needs an independent reason and new testable consequences, never conditions added after the fact only to explain a known failure**. Do not archive counterexamples without changing text, process, ceiling, or lifecycle.

## 12. Maintain Authoritative Registries and Writeback

Keep these records distinct:

- `COUNTEREXAMPLE-REGISTRY`: object, scale, observable facts, non-noise basis, old and alternative explanations, required disposition, and follow-up signals.
- `CASE-REGISTRY`: successes, failures, early dissipations, open processes, counterexamples, indeterminate cases, and exclusions; question whether missing data reveals a blind spot. When cases compare mechanisms or estimate proportions, state the object, outcome, window, and entry rule; keep cases that had the opportunity but did not occur; never fold unrelated non-occurrences into one denominator; never fill missing checkable records with zero; theoretical expectation is never the sole reason to exclude a real counterexample; understanding a single case's text needs no frequency population.
- `CLAIM-REGISTRY`: claim text and type, object, scale, affected positions, evidence, counterevidence, alternatives, withdrawal conditions, ceiling, and public state.
- `FORECAST-REGISTRY`: target, window, trigger, early and reverse signals, competitors, and all deadline outcomes.
- `VERSION-LOG`: restriction, downgrade, suspension, publication block, withdrawal, replacement, retirement, rollback, remedy, and downstream synchronization.

Formal judgments made in this framework's name need a CLAIM-REGISTRY entry before public release or high-impact use; ordinary discussion, independent domain research, and grounded local opinions bear responsibility under their own tasks and lose no knowledge standing for lacking a framework number (§16.4). More recorded cases do not mean more generality, and internal selection is not external validation.

For every VERSION-LOG entry, bind the governance record, subject, canonical source and target versions, transition, old and new states, event type, time, owner, evidence, counterexample, text effect, process effect, ceiling effect, and downstream writeback. Require a strictly increasing numeric target version. For an applied change, require at least one real text, process, or ceiling change and distinct before and after hashes.

Correct a log with a new entry. Never delete the original or its failure path. A counterexample merely archived without effective review is not a closed correction loop; an upheld counterexample changes the affected text, process, or ceiling, and an unadopted one keeps its reasons and review path. Treat a persistently empty log as a possible feedback-channel failure, not proof of perfection, and an unchanged log alone neither proves perfection nor failure.

**Register version identities separately** (§16.19, GOV-19): text identity, theory version, structured-contract version, software version, and the version an actual run consumed. Renaming a theory or a new major version does not reset the software version or prove that installed content has migrated. Text written back, engineering built, run consumed, answers performing adequately, and real tasks benefiting each have their own verification endpoint, and the feedback endpoint matches the problem: a typo correction targets the authoritative text and its spread; a source-number correction also checks the dependent calculations; an overreaching use is traced to actual execution and remedy. Version logs and hashes locate changes; they never replace semantic or real-world effect.

**Derived method entries keep candidate status** (§16.20.1). Usage steps and retrieval entries organized from the source text can be sampled for review within a stated scope: before sampling, state the population, classes, selection basis, and questions; cover different mechanisms, objects, and output types, and include high-impact uses, cross-scale transformations, and theory-boundary entries. A convenient handful never represents uncovered classes. Finding an omitted concept, a widened scope, or source and derived content confused expands review of the related classes and traces the methods and conclusions that depend on the entry. Distinguish entries actually reviewed from those not reviewed item by item. **Permitted sampling, passed program checks, or a sample with no errors found so far never means the author confirmed every item, and never replaces substantive review of real high-impact judgments.** An author's experiential judgment that plays a methodological role belongs in the source text at its proper place (applicable object, grounds, counterexamples, stop conditions); organizing opinions not written into the source keep candidate status and never set up a separate author theory through auxiliary method entries. Ariadne itself is such a derived set of entries.

## 13. Protect Challenge, Opacity, and Weak Signals

Run a pre-concept gate before mapping a subject into framework language. In plain language, ask whether it can be observed together, has a minimum boundary, contains repeat interactions, shares a problem or constraint, has identifiable maintenance costs, and can change after results or bad news. If this gate fails, keep only phenomenon description, risk registration, or narrative analysis.

Cap concepts at five strengths (§16.5): expression (helps say a feeling or similarity), exploration (generates questions and observation signals), diagnosis (external observable material, low-to-medium confidence), strong judgment (object, evidence, scale, responsibility, and observation gates all passed), and disposition (additionally external review, appeal, anti-retaliation, compensation, and withdrawal, and still normative choice, J, and O).

Invisibility is not absence of information. Before classifying opacity, read six absence signals; an absence reading generates candidate questions only, never conclusions:

| Absent signal | Candidate reading |
|---|---|
| Anchor | A shared reference point may never have formed. |
| Feedback | The channel may not exist, or subjects may not dare to speak. |
| Conflict | Fear, dependence, or punishment may be suppressing it. |
| Repair | No repair interface may exist. |
| Exit | The cost of leaving may be unbearable. |
| Language | No usable expression tools may be available. |

Classify opacity:

- `protected`: shields privacy, witnesses, vulnerable people, immature experience, or low-power feedback;
- `functional`: reduces overload or preserves bounded professional or deliberative space, with later review and accountability;
- `suppressive`: hides responsibility, blocks feedback or review, creates fear, monopolizes power, or prevents proof of harm.

Ask who is protected, who benefits, who reviews independently, and when opacity ends; without all four answers, independent review, a time boundary, and release conditions, opacity is never registered as a healthy boundary. Block publication and trigger external review when suppressive opacity appears. Term management means continuing review of the reasons for confidentiality, not mandatory publication of sensitive material at expiry. Not yet confirming that opacity is legitimate is not proof of suppression, and a confidentiality label never covers fabrication, evasion, or blocked verification (§16.6).

Require all six weak-signal protections: anonymous or low-exposure entry, independent carrier, retaliation tracking, group calibration, delayed publication when safety requires it, and proof that accepted signals changed rules, resources, responsibility, or authoritative records. With any of the six missing, say only "weak-signal risk is recognized", never "weak signals are protected" (§16.10). A weak signal does not prove a conclusion, but low frequency, anonymity, emotion, or imperfect form do not erase it.

### Stage-6 operation and observation-recursion cap

This cap instantiates the qualified reference `governance.module.GOV-07 -> hsp.domain.human_intentional_collective -> hsp.state.S6`. Apply it only to an object that an independent runtime record confirms as a human intentional collective whose state includes `hsp.state.S6`. Do not apply it to an individual human, a nonhuman system, or a human collective that has not met S6; Stage 6 is not a universal layer of the wider world.

Stage 6 does not mean transcending entropy or reaching a perfect system. It means only that, within a bounded time window, discovery, repair, writeback, and carrier reproduction temporarily outpace loss accumulation. Never claim Stage 6 because the object currently runs well; record five operating measures: discovery lag, repair lag, recurrence rate, repair by-products, and repair-load distribution.

Expand observation recursion only when a new reaction changes boundary, identity, resources, action channels, carrying relations, feedback writeback, risk, or public memory, or supplies a new high-cost signal. Close the recursion when any of five triggers appears: two consecutive rounds produce only same-kind reactions; the object starts manipulating the diagnostic rules; continued tracking increases exposure; the information gain falls below the structural disturbance; or the diagnoser can no longer distinguish the object's state from observation artifacts.

After closure, stop asking what the object really is. State only that, under current observation conditions, a certain reaction pattern can be confirmed, and that further judgment requires external review or new high-cost evidence.

## 14. Detect Capture and Provide Special Safeguards

Check ten malicious-compliance signals: single-source control; counterexamples dismissed as noise or emotion; open assertions used as labels; appeals never changing results; “independent” reviewers under the same power chain; AI reports without raw material or external verification; diagnosis used to justify inaction or evade responsibility; phase, field, complexity, or entropy used to excuse inaction; love, mission, expertise, or the greater good used to extract low-power positions; and appellants relabeled irrational. At three or more signals, block strong judgment. At five or more, record high malicious-compliance risk and allow only risk registration, external-review requests, and protective probes (§16.8). The audited party never confirms its own reviewers' independence. Three and five are procedural thresholds that start protection and review, not natural constants or calibrated probabilities of bad faith; triggering is not a finding of deliberate deception; changing the thresholds goes through the version procedure, never ad hoc after a case result.

Use special safeguards:

| Condition | Audit requirement |
|---|---|
| No institutional infrastructure | Permit only a protective open assertion with material, pattern, prohibited uses, escalation and withdrawal signals, and low-risk next steps. Do not use it for punishment, files, qualification, publicity, or resource loss. |
| Unable to exit | Prioritize safety, trusted proxy, minimum choice and information, low-exposure records, local buffers, substitute exits, and a ban on romanticizing captivity as love, loyalty, maturity, sacrifice, or collective need. Distinguish proxies who help understanding and expression, submit materials, handle matters by the person's mandate, or decide on the person's behalf, each with its own basis and scope; a proxy statement is never registered as the person's own expression or consent; keep the person's ways of communicating, conflicts of interest, conditions for refusing or changing support, and review of objections; documentation never becomes a reason to interrupt needed support or force disclosure (§16.12). |
| No healthy baseline or complex trauma | Distinguish deterioration, hollow nominal anchor, never-built healthy support, and trauma-built rules. For the last two types, ask the six replacement questions below instead of asking how to return. Do not invent a healthy past; refer clinical, care, child-protection, or legal judgments externally. |
| Open undertaking or love language | Love is neither "the residue structure cannot explain" nor a default motive label. Description holding, effect holding, and being praiseworthy are three questions that can each be affirmed or denied; risks revealed at HV11 R0 form protection needs without waiting for R1 or R2; failing a route never denies inner life or personality; voluntarily bearing a bounded cost never creates unlimited duty; never use love to cancel responsibility (§16.14). A broad utility representation that back-fills payoffs from observed choices makes every outcome optimal and cannot separate competing explanations. |
| Cross-domain metaphor | Label metaphor, analogy, mechanism candidate, evidence, formal model, or validated rule; record similarity, difference, misuse risk, and stopping evidence. |
| Accessibility debt | Say plainly, at the right time: **you do not need to learn the framework to protect yourself first, record facts, and seek support** (§16.16). Identify six threshold debts first: learning takes time and cognitive resources; plain language and terminology lose content in translation; evidence is hard to collect safely; external review may not exist; the more is invested, the harder exit becomes; and framework-mastery identity carries interpretive power and social capital. Then provide plain language, graded ceilings, proxy expression, non-text material, equal appeal, and protection without framework mastery. Internal certification or payment never creates external qualification. Without equivalent appeal, protection, and withdrawal entries, no substantive high-impact or automated-decision use; filling more fields, drawing more charts, or reading everything does not automatically produce understanding or fairness; people who need assisted expression never first have to prove full expressive capacity. |

Audit courses, consulting, AI tools, scoring systems, organization software, standards, and branches for commercialization, weaponization, evidence control, qualification monopoly, and selective publication: never package a light template as a full diagnosis, internal certification as external review, AI output as independent investigation, or client satisfaction as validity, and never force a strong diagnosis to deliver (§16.17). A branch is not betrayal; running a different framework under the same name without saying so is the greater risk. Require each branch to state retained question families, abandoned boundaries, changed concepts, and new misuse risks.

Remove an open assertion from use when it enters assessment, records, discipline, qualification, resources, or public memory; suppresses appeal; becomes a clipped label; creates long exclusion under “observation”; or loses its withdrawal conditions. Mark misuse, correct or remove downstream records, remediate harm, and refuse endorsement when capture cannot be stopped.

### Six replacement questions when no healthy baseline exists

For a never-built object that never formed a healthy anchor, and for a trauma-built object whose rules, identity, boundaries, and relations were built from trauma, do not ask how to return to what was. Ask instead:

1. What is the current minimum safety?
2. Is the subject receiving predictable support for the first time?
3. Is there an expression entry that is not punished?
4. Is there a small, repeatable trust?
5. Which survival strategies once protected the subject and are now becoming limits?
6. Is a new anchor being discovered, or does it need to be built together?

Therapeutic, clinical, care, child-protection, and legal judgments stay with the corresponding professional procedures. The framework never invents a healthy past.

### Knowledge lineage and source transparency

For every traceable concept, register its intellectual kinship, concrete sources, version, what was retained, what was reworked, what was abandoned, its cross-cultural and cross-domain risks, and what the sources can and cannot support. Labeling intellectual kinship does not weaken the framework; it lowers mystification and dogmatization.

Keep four non-substitution boundaries: theoretical material does not replace case evidence; a single case does not replace a general rule; an internal summary does not replace original records; an AI summary does not replace traceable sources.

Build interoperability interfaces with other theories. Do not write this framework as a master framework that swallows every theory. A connection keeps where the disagreement lies (different estimates of an outcome, competing mechanisms for the same outcome, or different value premises) instead of erasing it under a unified name; choosing a method states what distinguishable content it adds for the current task; **when a domain method already suffices, allow using only the domain method** (§16.15).

## 15. Test Appeal, Rollback, and External Review

Treat an appeal as effective only when it is accessible, safe, time-bounded, owned, able to change the record or action, protected from retaliation, and escalatable to an independent reviewer for high impact or conflict.

Every high-impact audit writes the typed `contestability` payload. `owner` must contain a tested reachable contact, not a role label; `deadline` is an RFC 3339 response deadline; `original_record_retention` stays true; `downstream_correction_target` names every registry or decision surface to correct; `rollback_recovery_target` names the state, rights, resources, services, access, and records to restore; and `remedy` names restitution plus residual-harm tracking. If any field is missing or the owner is unreachable, fail the relevant gate and pause high-impact use.

Treat rollback as complete only when it:

1. names the target state and stop authority;
2. stops or reverses the action within the registered scope;
3. restores rights, services, resources, or other acceptable state;
4. corrects authoritative records and synchronizes downstream copies;
5. remediates real harm and tracks residual harm;
6. writes the event and responsible owner to the version and execution logs.

Require external reviewers to use canonical identities, disclose material interests, access the evidence, counterevidence, uncertainty, dissent, and affected-position material, and possess real veto or stop power. Do not let internal pressure tests stand in for external evidence.

For public strong judgment, pass all nine publication gates:

1. traceability completeness;
2. source quality;
3. counterexample handling;
4. affected-position review;
5. burden-transfer review;
6. misuse red team;
7. public-language review;
8. external review;
9. SJ1-SJ8.

Any failure blocks strong publication. All nine passing yields only `publishable`, never authorization.

## 16. Govern Orderly Death, Forecast Debt, and Model Retirement

Open replacement or retirement when a simpler method performs better with lower error and harm; a concept adds learning cost without diagnostic gain; roots survive only by exception patches; users suppress competing theories or real counterexamples; or identity, commercial, or power benefit exceeds judgment benefit.

On replacement, record the old method's valid range and failure boundary, the successor's responsibility, cross-check period, unresolved harms and records to transfer, transition owner, and effective date. Allow `restrict`, `suspend`, `compete`, `replace`, `retire`, or `handoff`. Do not let a creator, maintainer, or beneficiary veto replacement unilaterally or preserve a method by endless concept growth.

Audit five multi-circle forecast debts:

- object debt from reifying named circles;
- variable debt from promoting residual candidates into facts;
- complexity debt without out-of-sample gain;
- calibration debt from publishing without result registration;
- power debt from using forecasts for screening, surveillance, punishment, or manipulation.

Shrink the model, lower the output, pause high-impact use, or retire a module when debt crosses a preregistered threshold. Keep forecast success, failure, unresolved, target-invalid, and non-evaluable states. Automatically downgrade forecast capability when calibration deteriorates, errors concentrate across groups, the complex model no longer beats the baseline, or results depend on post-outcome variables.

Treat personality hypotheses and automated risk inference as high-misuse material (§16.23). Audit purpose, authority, privacy, allowed use, cross-circle spread, appeal, deletion or correction, model version, and downstream effects. Prohibit clinical diagnosis, essence judgments, discriminatory screening, unauthorized risk scores, and silence-as-evidence. Any automated system that promotes `candidate` to `observed`, `simulated` to a real event, or a forecast to authorization is blocked and leaves an audit record. Human review is effective only when the reviewer sees evidence, counterevidence, and uncertainty, has the competence, the time beforehand, and a bearable load, holds real power to refuse, modify, or pause, and the signal reaches the executor in time to change the action rather than leaving one click in an interface. Evaluate human oversight by whether correct suggestions are appropriately adopted, wrong ones stopped, unprompted problems found, and affected people able to correct results; more overrides are not better, and full compliance does not prove reliability. Narrow actions faster than human judgment may use machine-checkable constraints and least privilege, while goal selection, omitted constraints, exception takeover, and remedy keep explicit responsibility; systemic risk is never pushed onto the last person who clicked.

**Replacement comparison** (§16.24, GOV-24) watches judgment quality and total burden together: fix the task, material, input cutoff, resources, and evaluation method; keep a strong enough domain method and accurate citation as controls; check misjudgment, omission, inappropriate abstention, time, disclosure, and maintenance labor. A candidate written into the text shows only editorial adoption; same-source candidates sharing one change are not counted per candidate. Line breaks, character counts, and file counts can be tallied but never measure reader cost or work effect. Without an actual comparison, never claim superiority, equivalence, or uselessness. When theory, software, and material change together, evaluate only the combination.

For final retirement, preserve necessary provenance, responsibility, failure, appeal, and remedy records; stop using the retired model for new decisions; publish which conclusions remain boundedly usable, which are downgraded, and which cannot migrate. Keep scenario-specific consensus, observation, channel, remedy, AI-risk, and cross-domain thresholds external, evidenced, time-bounded, and reviewable. Leave missing parameters downgraded, suspended, or in competition; never let the framework fill them itself. A missing parameter blocks only the judgments and uses that depend on it; protective unknowns, lack of observation capacity, true inapplicability, and pending evidence stay separate; and compare whether added records can change a judgment or reduce harm against the waiting, exposure, and maintenance they cost (§16.25).
