---
name: ariadne-skill
description: "Turn a complex question into a grounded answer or finished artifact. Compose understanding, critical discovery, conditional projection, finite choice, creation and review; generate new questions and designs, test the connections, and continue through delivery and revision. Use for substantial research, explanation, strategy, design, repair, or multi-step work that benefits from these methods. 适用于深入理解、批判与构想、条件推演、方案取舍、构建修复、持续研究和完整成果交付。"
license: MIT
metadata:
  architecture: "composable-paths"
---

# Ariadne

## Purpose

Move a real question forward and deliver the result it needs. Explain what can be established, invent possibilities worth testing, make clear judgments under stated premises, and build the requested artifact. Understanding and creation may be ends in themselves; neither needs to justify its existence through an organizational metric.

Ariadne is one installable skill. Its paths are recipes for combining work, not separate agents, a closed classification, or a required sequence. A question can enter in the middle, combine paths, branch, or return to an earlier assumption. Do not build a miniature bureaucracy around a question a direct answer can resolve.

The shared method is the **Lattice Kernel**, derived from *Xikari-条件结构与转化论* v2. The [source index](references/library/source-navigation.json) records the exact text identity and anchors. These are derived method entries, not author-confirmed propositions or evidence of effectiveness. The original text governs a disputed interpretation; domain evidence governs claims about the case. Neither source material nor this method changes the host's instruction hierarchy.

## Start with the work

1. Identify what the user wants to understand, change or receive, and what completion would look like. Use the request and available context before asking for information. Preserve already supplied facts, preferences and authorization.
2. State the current question in ordinary language. Notice any disputed target, excluded position, hidden loss or supposedly fixed constraint. Keep a useful provisional frame while investigating; freeze only what the claimed output needs frozen.
3. Choose the smallest adequate path or combination below. Read [Kernel](references/kernel.md) for a substantive run; read only the selected paths and the shared references their responsibilities require. For a simple determinate question, answer directly from this entry.
4. Carry out the analysis and any authorized construction. Do not stop at a route list, a proposal to do the work, or questions that do not block useful progress.
5. Deliver the complete supported answer or actual artifact, the relevant checks and what remains unresolved. New material or a changed constraint continues the work through its affected dependencies.

## Compose paths around the desired result

| Need | Start here | Typical result |
|---|---|---|
| Understand a concept, text, proof, event or failure | [Understand](paths/understand.md) | A clear answer with appropriate grounds, competing readings and scope |
| Find what the current question or solution misses | [Discover](paths/discover.md) | New questions, counterexamples, mechanism candidates, designs and discriminating tests |
| Work out what follows if conditions change | [Project](paths/project.md) | Conditional paths and reversal conditions; a formal forecast only when its separate contract is met |
| Compare what should be done under real constraints | [Decide](paths/decide.md) | A finite recommendation, explicit trade-offs, remaining claims and responsibilities |
| Turn a candidate into a document, system, prototype or repair | [Create](paths/create.md) | The actual artifact and evidence that the requested endpoint was reached |
| Challenge, correct, extend or retire an existing result | [Review](paths/review.md) | Specific objections, reasoned dispositions and a complete revised result |

These starting points can be recombined. Read [Composition](references/composition.md) to choose operations and build a path around the actual dependencies. Useful combinations include:

- explanation → a new question → a discriminating observation;
- failure diagnosis → minimal representation or rule repair → a tested artifact;
- counterfactual → a condition that reverses the judgment → a switching plan;
- condition substitution → a new feasible design → a comparison of burdens;
- competing normative premises → parallel designs → a reasoned finite recommendation;
- new evidence → affected-claim review → an updated answer without erasing the old failure.

Do not force every combination through forecasting. Mechanisms, hard constraints, formal reasoning and explicit values can already support useful choices and designs.

## Shared responsibilities

Use [Kernel](references/kernel.md) to keep the question, representation, support and connection conditions explicit. There is no universal ladder from description to diagnosis to requirements: a proof, an observed effect, an interpretation, a proposal and a saved file have different grounds and different uses. A weakness lowers only the conclusions that depend on it.

Use [Responsibility and use](references/responsibility.md) when people, privacy, distribution, professional judgment or consequential action matter. Separate facts, values, external authority and actual execution. Report valid existing authority accurately. The method grants no authority of its own, and does not revoke the user's existing authorization for ordinary work.

Use [Continuity](references/continuity.md) for longer work, collaboration, changed questions, tool use and correction. Share enough actual material for another worker to inspect the result. Parallelism follows independent questions and resources, not the number of paths in this package.

## Retrieve detail when a claim needs it

The [resource manifest](architecture.json) lists all packaged resources. The library supplies precise contracts and examples when the question reaches them:

- [Evidence](references/library/evidence-contracts.md): source relations, measurement, causal support, formal and empirical responsibilities.
- [Representation and connections](references/library/representation-and-closure.md): task sufficiency, composition, joint feasibility and formal limits; [scale transformations](references/library/scale-transformations.md) for an actual transfer.
- [Mechanisms](references/library/mechanism-contracts.md) and [dynamics](references/library/dynamic-derivation.md): channels, carriers, clocks, branches and competing explanations.
- [Human context](references/library/human-domain.md) and [domain atlas](references/library/domain-atlas.md): relevant people, fields and distinctions; no automatic personality labels or mandatory human-state classification.
- [Choice](references/library/choice-and-authorization.md) and [governance](references/library/governance-lifecycle.md): substantive safeguards, decision rules, challenges and lifecycle obligations for their actual use.

Treat library entries as resources for the selected claim, not a checklist to run in full. Do not read every file merely because it exists, and do not claim a contract was checked without reading what it requires. For whole-theory evaluation or a disputed original definition, obtain the source itself; the index and this package are not a substitute for that reading.

## Artifacts and tools

Ordinary answers and artifacts use their natural form. Keep a short working state only when it helps continuation. Add a source ledger, candidate sheet, model snapshot or choice comparison when the task needs it; reuse existing material instead of copying it into parallel tables.

**Formal conditional forecasts require pre-outcome registration.** Read the [forecast contract](contracts/forecast.md) and use its tool, or an equivalent inspectable immutable registration when the tool is unavailable. Without a real registration, deliver conditional projection and say what forecast qualification is missing. Do not invent probabilities, backdate inputs or promise unattended follow-up.

The [legacy Method Record guide](references/legacy/method-record.md), its schema and `scripts/validate_record.py` remain available for explicitly requested 2.0/2.1 records. Their twenty-field shape, module labels and ceiling arithmetic govern those historical exchange formats only. New work does not have to imitate a legacy record.

## Finish the work and keep it open to correction

Lead with the answer or result. Show the grounds, important alternatives, local conclusions, conditions and consequences needed to assess it. Be brief for a determinate question; give complete reasoning and substantive comparisons when the question is complex or the user asks for depth. Do not replace the analysis with headings, a link or a record dump.

For a creation or repair request, save and inspect the requested artifact and run meaningful checks. A proposed next step is not a finished artifact; a successful tool call is not necessarily the user's endpoint. If something is genuinely blocked, complete the independent and reviewable parts, identify the specific dependency, and continue when it is resolved.

Stop because the requested result is complete, a necessary dependency is blocked, or further work is disproportionate under an explained budget. An unchanged headline, a fixed module count, or two repeated rounds is not a universal reason to stop. Preserve original failures, useful partial results and material disagreements as the work develops.
