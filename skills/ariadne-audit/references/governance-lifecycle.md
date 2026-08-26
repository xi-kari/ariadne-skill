# Governance and Lifecycle Contract

Sections 10-16 of the audit contract: consensus and version authority, lifecycle and retirement, registries and writeback, challenge protection, capture detection, appeal and rollback testing, and orderly death. The gate flow itself (sections 1-9 and the worked example) lives in [gates-core.md](gates-core.md). These sections carry the source governance numbering family `GOV-01`-`GOV-24`; the shipped text instantiates a qualified reference where a specific clause is applied (for example `GOV-07` in the observation-recursion cap) and otherwise keeps the family as source-document numbering rather than re-deriving all twenty-four clauses.

## 10. Govern Consensus and Version Authority

Require seven steps for a governance change:

1. Register the issue, proposed concept, major rewrite, root change, misuse, or counterexample.
2. Publish cases, counterexamples, user feedback, external research, practice failures, and ethical risks.
3. Identify affected users, judged subjects, low-power positions, and scenarios.
4. Provide a safe dissent channel for affected, low-power, nonexpert, and external critics.
5. Match decision authority to the change class; do not use one permission level for minor edits and root changes.
6. Preserve unaccepted minority positions as counterexamples or unresolved issues.
7. Write the introduction, deletion, restriction, downgrade, reason, withdrawal evidence, and downstream effects to the version log.

Give every dissent a disposition, reason, and concrete effect on text, process, or action ceiling. Bind accepted effects to actual `change_id` entries. Keep a change proposed, nominal, or suspended when dissent cannot alter it or when all dissent is rejected, ignored, or unresolved.

Resolve canonical actors, evidence, interests, authorization, external review, dissent, and structured VERSION-LOG entries through runtime registries. Do not use aliases as identity, self-declared independence, internal signatures as external approval, or an issuer who is also the holder or proposer.

## 11. Apply Lifecycle, Downgrade, and Retirement Rules

Use append-only lifecycle transitions:

| Subject | In-service states | Terminal states |
|---|---|---|
| Root hypothesis | `normal_use`, `boundary_restricted`, `suspended`, `replacement_competition` | `retired_from_core` |
| Public assertion | `internal_draft`, `open_assertion`, `publishable`, `downgraded`, `suspended`, `publication_blocked` | `withdrawn`, `replaced` |
| Framework | `active`, `boundary_restricted`, `suspended`, `replacement_competition` | `replaced`, `retired` |

Do not create an edge from a terminal state back to active service. Give any successor a new identity, new external authority, and a link to the preserved terminal history.

Trigger review for repeated counterexamples, stable misclassification of a class, scope expansion, evasive exception-patching, high-harm misuse, capture, inaccessible correction, calibration decline, or a safer simpler replacement. Apply consequences:

- Let a minor counterexample tighten a boundary.
- Let repeated counterexamples downgrade a claim.
- Let a high-harm counterexample suspend use.
- Let a systematic counterexample open replacement competition.
- Let misuse block publication.
- Let an irreparable application enter exit or transfer review.

Do not archive counterexamples without changing text, process, ceiling, or lifecycle.

## 12. Maintain Authoritative Registries and Writeback

Keep these records distinct:

- `COUNTEREXAMPLE-REGISTRY`: object, scale, observable facts, non-noise basis, old and alternative explanations, required disposition, and follow-up signals.
- `CASE-REGISTRY`: successes, failures, early dissipations, open processes, counterexamples, indeterminate cases, and exclusions; question whether missing data reveals a blind spot.
- `CLAIM-REGISTRY`: claim text and type, object, scale, affected positions, evidence, counterevidence, alternatives, withdrawal conditions, ceiling, and public state.
- `FORECAST-REGISTRY`: target, window, trigger, early and reverse signals, competitors, and all deadline outcomes.
- `VERSION-LOG`: restriction, downgrade, suspension, publication block, withdrawal, replacement, retirement, rollback, remedy, and downstream synchronization.

For every VERSION-LOG entry, bind the governance record, subject, canonical source and target versions, transition, old and new states, event type, time, owner, evidence, counterexample, text effect, process effect, ceiling effect, and downstream writeback. Require a strictly increasing numeric target version. For an applied change, require at least one real text, process, or ceiling change and distinct before and after hashes.

Correct a log with a new entry. Never delete the original or its failure path. Treat a persistently empty log as a possible feedback-channel failure, not proof of perfection.

## 13. Protect Challenge, Opacity, and Weak Signals

Run a pre-concept gate before mapping a subject into framework language. In plain language, ask whether it can be observed together, has a minimum boundary, contains repeat interactions, shares a problem or constraint, has identifiable maintenance costs, and can change after results or bad news. If this gate fails, keep only phenomenon description, risk registration, or narrative analysis.

Cap concepts at expression, exploration, diagnosis, strong judgment, or disposition. Require external review, appeal, anti-retaliation, remedy, and withdrawal in addition to normative choice, J, and O for disposition use.

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

Ask who is protected, who benefits, who reviews independently, and when opacity ends. Block publication and trigger external review when suppressive opacity appears.

Require all six weak-signal protections: anonymous or low-exposure entry, independent carrier, retaliation tracking, group calibration, delayed publication when safety requires it, and proof that accepted signals changed rules, resources, responsibility, or authoritative records. A weak signal does not prove a conclusion, but low frequency, anonymity, emotion, or imperfect form do not erase it.

### Stage-6 operation and observation-recursion cap

This cap instantiates the qualified reference `governance.module.GOV-07 -> hsp.domain.human_intentional_collective -> hsp.state.S6`. Apply it only to an object that an independent runtime record confirms as a human intentional collective whose state includes `hsp.state.S6`. Do not apply it to an individual human, a nonhuman system, or a human collective that has not met S6; Stage 6 is not a universal layer of the wider world.

Stage 6 does not mean transcending entropy or reaching a perfect system. It means only that, within a bounded time window, discovery, repair, writeback, and carrier reproduction temporarily outpace loss accumulation. Never claim Stage 6 because the object currently runs well; record five operating measures: discovery lag, repair lag, recurrence rate, repair by-products, and repair-load distribution.

Expand observation recursion only when a new reaction changes boundary, identity, resources, action channels, carrying relations, feedback writeback, risk, or public memory, or supplies a new high-cost signal. Close the recursion when any of five triggers appears: two consecutive rounds produce only same-kind reactions; the object starts manipulating the diagnostic rules; continued tracking increases exposure; the information gain falls below the structural disturbance; or the diagnoser can no longer distinguish the object's state from observation artifacts.

After closure, stop asking what the object really is. State only that, under current observation conditions, a certain reaction pattern can be confirmed, and that further judgment requires external review or new high-cost evidence.

## 14. Detect Capture and Provide Special Safeguards

Check ten malicious-compliance signals: single-source control; counterexamples dismissed as noise or emotion; open assertions used as labels; appeals never changing results; “independent” reviewers under the same power chain; AI reports without raw material or external verification; diagnosis used to justify inaction or evade responsibility; phase, field, complexity, or entropy used to excuse inaction; love, mission, expertise, or the greater good used to extract low-power positions; and appellants relabeled irrational. At three or more signals, block strong judgment. At five or more, record high malicious-compliance risk and allow only risk registration, external-review requests, and protective probes.

Use special safeguards:

| Condition | Audit requirement |
|---|---|
| No institutional infrastructure | Permit only a protective open assertion with material, pattern, prohibited uses, escalation and withdrawal signals, and low-risk next steps. Do not use it for punishment, files, qualification, publicity, or resource loss. |
| Unable to exit | Prioritize safety, trusted proxy, minimum choice and information, low-exposure records, local buffers, substitute exits, and a ban on romanticizing captivity as love, loyalty, maturity, sacrifice, or collective need. |
| No healthy baseline or complex trauma | Distinguish deterioration, hollow nominal anchor, never-built healthy support, and trauma-built rules. For the last two types, ask the six replacement questions below instead of asking how to return. Do not invent a healthy past; refer clinical, care, child-protection, or legal judgments externally. |
| Open undertaking or love language | Separate structural incentives from voluntary avoidable cost. Require real gains in safety, refusal, and appeal for affected positions; never use love to cancel responsibility. |
| Cross-domain metaphor | Label metaphor, analogy, mechanism candidate, evidence, formal model, or validated rule; record similarity, difference, misuse risk, and stopping evidence. |
| Accessibility debt | Identify six threshold debts first: learning takes time and cognitive resources; plain language and terminology lose content in translation; evidence is hard to collect safely; external review may not exist; the more is invested, the harder exit becomes; and framework-mastery identity carries interpretive power and social capital. Then provide plain language, graded ceilings, proxy expression, non-text material, equal appeal, and protection without framework mastery. Internal certification or payment never creates external qualification. |

Audit courses, consulting, AI tools, scoring systems, organization software, standards, and branches for commercialization, weaponization, evidence control, qualification monopoly, and selective publication. Require each branch to state retained roots, abandoned boundaries, changed concepts, and new misuse risks.

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

Build interoperability interfaces with other theories. Do not write this framework as a master framework that swallows every theory.

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

Treat personality hypotheses and automated risk inference as high-misuse material. Audit purpose, authority, privacy, allowed use, cross-circle spread, appeal, deletion or correction, model version, and downstream effects. Prohibit clinical diagnosis, essence judgments, discriminatory screening, unauthorized risk scores, and silence-as-evidence. Require a human reviewer to see evidence, counterevidence, and uncertainty and possess genuine veto power.

For final retirement, preserve necessary provenance, responsibility, failure, appeal, and remedy records; stop using the retired model for new decisions; publish which conclusions remain boundedly usable, which are downgraded, and which cannot migrate. Keep scenario-specific consensus, observation, channel, remedy, AI-risk, and cross-domain thresholds external, evidenced, time-bounded, and reviewable. Leave missing parameters downgraded, suspended, or in competition; never let the framework fill them itself.
