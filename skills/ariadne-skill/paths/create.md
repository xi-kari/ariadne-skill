# Create: build and repair the requested result

## When to use this path

Use this path for a document, plan, rule, schedule, implementation, prototype or repair that the user wants completed. The product is the actual usable artifact, not a handoff saying construction should happen next. The host's tools perform the work within existing authorization; the methodology supplies reasoning and verification, not additional power (§13.8, §13.11.2, §16.9).

Read the [kernel](../references/kernel.md) and [continuity](../references/continuity.md). Add [discover](discover.md) when a candidate must be invented, [decide](decide.md) when normative trade-offs matter, and [review](review.md) when the design or implementation needs challenge. Ordinary straightforward construction does not require a formal research project.

## Define what must be delivered

Identify the intended user and use, output form and destination, required behavior or content, available resources, real constraints and the check that will establish completion. Read the existing artifact before repairing it. Preserve unrelated user work and valid local behavior.

Distinguish fixed requirements from assumptions and preferences that can be reasonably chosen. Use available context and tools to resolve ordinary details. Ask only for a missing decision or information that genuinely changes the deliverable or blocks the next dependent step; continue independent work while waiting.

If a target or constraint is deficient, reopen it explicitly rather than quietly solving a more convenient problem. Keep the original failure and explain the relationship of the revised task (§2.14).

## Construct around the actual need

For a new artifact, develop the smallest adequate design, then add complexity that earns its place. Use a traceable generative move when novelty is needed: condition substitution, mechanism composition, representation refinement, counterfactual branching or parallel normative designs. Make the design concrete enough to test.

For a repair, locate the actual breakpoint:

- If the representation cannot distinguish states requiring different answers, change the representation or explicitly change the query.
- If adequate information is present but the rule uses it incorrectly, repair the rule.
- If information or action arrives late, repair access, timing or a legitimately changeable deadline.
- If tasks compete for a shared resource, find a jointly feasible arrangement; individually feasible plans cannot each claim the same capacity.
- If an implementation departs from a sound design, fix that departure and test it.
- If the missing condition is authority, complete the reviewable design and use the relevant external decision process; extra code or data does not create permission.

Distinguish formation, maintenance, recovery and reproduction conditions. A prototype working once does not prove it can be maintained or repeated elsewhere. A failed replication cannot be saved by inventing a requirement after the outcome (§6.10.1).

## Complete and inspect the artifact

Write the document, implement the code, produce the schedule or perform the authorized repair. Keep important assumptions and unresolved conditions visible in the artifact where a user needs them. Do not bury operationally necessary limitations in a separate record that the artifact's user will never see.

Choose checks that could reveal a meaningful failure:

| Artifact | Useful checks |
|---|---|
| A document or rule | Required content, internal consistency, actual readability, affected positions and whether the terms can be used as written |
| Code or a technical repair | The changed behavior, a relevant failure case, interfaces and appropriate existing regressions |
| A schedule or allocation | Coverage, deadlines, simultaneous demand, individual and shared capacity, and explicit assumptions |
| A design or prototype | A representative task, boundary cases, intended experience, feasibility and known untested effects |
| An external change | The actual resulting state, scope of mutation and any downstream consequence the request includes |

Open or read back saved artifacts. A successful write operation does not prove the contents are correct. A test suite passing establishes only what its tests cover; it does not establish adoption, safety in every context or real-world benefit. A timeout leaves the external outcome uncertain, so inspect before retrying a potentially duplicative change.

## Work through real constraints

When every feasible design has a loss, compare explicitly and give the strongest supported recommendation under the user's criteria and applicable protections. Preserve the losing positions' valid claims and follow-up responsibilities. Do not invent an impossible costless design or stop at a list of questions (§14.9.1).

Use an existing valid permission within its scope. If a consequential step needs new permission, finish the concrete reviewable artifact first; identify the actual action still blocked. A draft is not implementation, and implementation is not evidence of downstream benefit. Conversely, unresolved adoption does not make a completed draft disappear.

## Worked example: a feasible review rota

In a synthetic five-day week, two reviewers are each available every day and may work at most three days. At least one reviewer is needed daily, and both are needed on Wednesday. Total demand is six reviewer-days and total capacity is six. A feasible draft assigns A on Monday, Tuesday and Wednesday, and B on Wednesday, Thursday and Friday.

The task is to deliver a rota, so create the requested file and check every day's coverage and each person's count. Do not merely recommend that someone make the schedule. The mathematical feasibility follows within the supplied assumptions; real availability and organizational adoption are separate questions if the rota is later used outside the exercise.

If the user then says B is unavailable Thursday, reopen the affected allocation. A can cover Thursday only by moving one of A's earlier days to B; recompute the whole week's constraints, update the actual file and retain the reason for the revision. The old draft was feasible under its original assumptions, not under the new one.

## Completion and handoff

Deliver the artifact's location or accessible contents, the important design choice, the checks actually performed and any specific remaining limitation. Keep a complete current version. If the host lacks the required tool, provide the most complete usable alternative and accurately state the unreached endpoint; never claim a file was saved, a system changed or a remedy arrived without evidence.
