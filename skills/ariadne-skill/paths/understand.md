# Understand: make the question answerable

Use this path to explain a concept, interpret a text or situation, prove a bounded formal result, diagnose a difference, or build an empirical explanation. The product is the answer or explanation itself, with the distinctions and support that make it useful. It can be a complete result without a forecast, recommendation, or formal record.

Read the [kernel](../references/kernel.md) for shared reasoning operations and [responsibility](../references/responsibility.md) for evidence, people, and use boundaries. Add only the detailed references the question needs: [objects and tasks](../references/library/object-contract.md), [evidence contracts](../references/library/evidence-contracts.md), [mechanisms](../references/library/mechanism-contracts.md), [representation and closure](../references/library/representation-and-closure.md), [human material](../references/library/human-domain.md), or the [domain atlas](../references/library/domain-atlas.md).

## Begin with the difference that matters

Ask what the user needs to understand and what a satisfactory answer would distinguish. “Why did this fail?” may mean why an outcome occurred, why a rule permits it, why a participant experienced it that way, or whether it was legitimate. These questions can share material without sharing an answer. In institutional work, distinguish constituted status, participants' understanding, actual realization, and normative legitimacy: a right can exist while its delivery fails; successful delivery does not establish legitimacy (§2.4.3).

Use the user's question as a working frame, not as an untouchable premise. If the target, loss measure, population, time span, permitted actions, or assumed scarcity excludes a material issue, state a better question and why. Keep what the original question established, identify whether the new one replaces, refines, or accompanies it, and say which evidence transfers. Anyone affected, excluded, or analyzing the task may raise the issue; changing an institution's actual rules still requires its competent process. A disappointing answer alone does not justify moving the goalposts (§2.14).

Choose a representation by what the task needs to retain. A short verbal distinction may suffice. A table, causal graph, state model, close reading, calculation, or program is useful when it exposes a relevant relation. More fields and a wider boundary do not automatically improve understanding. Where compression merges cases needing different answers, refine that distinction; where it retains everything relevant, do not manufacture information loss.

## Match the reasoning to the question

| Question | Work that earns an answer | A complete useful result |
|---|---|---|
| Conceptual | Clarify usage, contrast neighboring concepts, test boundary cases and counterexamples. | A definition or distinction, examples, limits, and its consequence for the user's question. |
| Textual or interpretive | Read the relevant material, establish context and speaker position, compare plausible readings, identify what the text leaves open. | A defensible interpretation with passages and reasons; unresolved ambiguity can remain. |
| Formal | State premises, definitions, target, and domain; give a proof, exhaustive finite argument, or checked computation appropriate to the claim. | The result and argument, including where a premise or mapping fails. |
| Empirical descriptive | Establish what was observed or reported, by whom, under which measurement and selection conditions. | A bounded factual account that separates disagreement, absence, and uncertainty. |
| Empirical explanatory | Define the difference or effect, compare plausible mechanisms and alternatives, identify what the design distinguishes. | The supported explanation, competing accounts that remain, and observations that could change the judgment. |

These tasks may combine. A model can prove that a scheduling policy meets a constraint under specified inputs while empirical work asks whether those inputs describe a workplace. The proof is valuable before that mapping is resolved. An interpretation does not need an invented prediction benchmark. Ordinary experience, meaning, care, and recognition are not exhausted by their measured functional effects (§1.3, §1.10, §2.1.1, §4.17).

For empirical claims, inspect how material came into being: collection, access, reporting, missingness, measurement changes, common data, and incentives. Read original material to the depth needed for the claim and state the actual reading scope when it matters. Reanalysis can produce a better argument without producing a new independent sample. Absence is evidence only when the event should have left a retrievable trace (§2.5-§2.7).

## Build explanations that can discriminate

Move from a label to an accountable link: under which conditions does what change, through which channel or carrier, on what time scale, producing which difference? A feedback diagram needs an actual return channel; a learning explanation needs a carrier and a change attributable to the relevant experience. “History matters” can mean a historical cause, a presently carried effect, or an increment from history beyond current carriers. Support for one does not settle the others.

Search for competitors that matter to this question. These may include a simpler mechanism, common cause, selection, changed measurement, execution error, or a domain explanation. Do not manufacture a second candidate to satisfy a quota. If a reasonable search leaves one candidate, state the search scope, why no alternative was retained, and what would defeat it. A candidate that fits the observed result may still be underdetermined; identify the observation, intervention, comparison, or formal argument that would discriminate it (§4.8.4, §13.4).

Treat the G1-G4 question families as specific empirical questions, not an admission gate for all knowledge. A source-supported fact about an object does not disappear because its proposed grouping has no demonstrated predictive gain. A credible total treatment effect can stand while the mechanism is unresolved; causal strength, mechanism resolution, and transfer range need separate judgments (§2.4.1, Part 4). Use the detailed [evidence contracts](../references/library/evidence-contracts.md) when formally claiming one of these instance results.

Formation, maintenance, recovery, and replication ask different questions. A practice that helps recovery may not explain original formation; support-dependent functioning remains real functioning. When a replication fails, distinguish a model failure from a documented implementation departure, a separately checkable missing enabling condition, or a change in scale that changed the treatment or object. An explanation invented after seeing the failure is a new candidate, not a rescue of the original test (§6.3, §6.6, §6.10.1).

## Deliver and open the next useful move

Lead with the answer the material supports. Explain the decisive distinction or mechanism, give the relevant evidence and competitors, and identify the specific uncertainty or change condition. If no explanation wins, deliver the established facts, the remaining candidates, and the best discriminating next step. Do not replace the answer with a list of unavailable information.

Understanding can generate a new capability:

- An explanation exposes an unasked question or hidden assumption: continue in [discover](discover.md).
- A representation identifies exactly what must change for a result: derive alternative paths in [project](project.md).
- A formal counterexample reveals a missing state variable or interface: build the revised model, algorithm, or test in [create](create.md).
- A supported explanation changes the option comparison: use [decide](decide.md) without treating explanation as authorization.

The handoff carries the question, the useful result, the materials and premises it depends on, the unresolved issue, and the next operation. Use whatever prose or artifact makes that dependence inspectable; a universal packet is unnecessary. Follow [composition](../references/composition.md) and keep useful state under [continuity](../references/continuity.md).

## Worked route: a slow deployment queue

Suppose release timestamps show that elapsed time doubled, while code review time did not. Trace data places most additional delay after review and before a scarce deployment window. This supports a location of delay; it does not yet prove why the window became scarce. Compare an increased arrival rate, reduced window capacity, and a new approval requirement against the actual logs and process history. If a new approval rule explains the observed discontinuity and the other accounts do not, give that bounded explanation while retaining concurrent causes the material cannot separate.

The analysis can then produce a queue diagram and a measurement query, project the effects of alternative window schedules, or implement a local scheduling simulation. The simulation tests the model and can reveal missing conditions; it is not a second observation of the deployment system. If the user wanted only the explanation, that explanation is already a complete deliverable.

## Failure boundaries

Do not infer a person's motive, trait, diagnosis, or consent from a group pattern or outcome. A report of experience remains evidence of the reported experience even when its causal interpretation is disputed. Do not require disclosure or a full human-variable card to offer help. Use only the human route and material the task needs.

When a source, measurement, bridge, or premise fails, revise the claims that depend on it. Keep independently supported facts, local successes, valid proofs, and legitimate criticism. Neither a framework label nor a completed form supplies missing evidence; neither a missing framework form nor a failed ambitious explanation erases an ordinary warranted conclusion (§2.9, §5.10.2, §7.3, §16.16).

Source basis: §§1.3, 1.10-1.11; §§2.1-2.9, 2.14; Part 4; §§5.10.2, 6.3, 6.6, 6.10.1, 7.3; Appendix C and Appendix D. This path is Ariadne's derived organization, not a claim of item-by-item author confirmation.
