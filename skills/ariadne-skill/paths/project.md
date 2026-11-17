# Project: derive paths and register eligible forecasts

Use this path to work out what follows from conditions, explore possible futures, find robust choices across uncertain states, or issue a dated conditional forecast when its evidence and evaluation contract permit it. Return the actual paths, model results, or forecast. A well-developed conditional derivation is a complete result even when a formal forecast is not justified.

Read the [kernel](../references/kernel.md), [responsibility](../references/responsibility.md), and the relevant [dynamic derivation](../references/library/dynamic-derivation.md), [mechanism](../references/library/mechanism-contracts.md), [scale](../references/library/scale-transformations.md), or [representation](../references/library/representation-and-closure.md) reference. Formal forecasts also use the [forecast contract](../contracts/forecast.md) and its [detailed theory](../references/library/forecast-contract.md).

## Fix what the projection is about

State the target difference, object, horizon, relevant environment, allowed operations, and starting information. Keep an observed event separate from a later discovery about that event. A new report can change the analyst's belief without changing the system at the reporting instant. Technical, organizational, physiological, and institutional processes can run on different clocks; align their actual interfaces rather than imposing one universal step (§11.3).

Clarify whether the user needs a conditional implication, a plausible scenario, an ordered forecast, a probability, or an action robust to uncertainty. These carry different burdens. A simulation demonstrates consequences inside its model. It does not establish that the world is in that state, that its mechanisms are correct, or that a feasible intervention is authorized.

Use an initial representation sufficient for the target. When cases that look identical in the representation can evolve differently in a way the task needs to distinguish, refine the state, history carrier, action constraint, or time resolution. Check whether the problem is lost representation, unavailable information, computation, or incorrect execution before adding variables. An exact but inaccessible model may not help the actual decision (§4.18-§4.19, §5.10.2).

## Construct paths from mechanisms and interfaces

Start with the supported relations and explicitly conditional mechanisms. For each material branch, explain the initiating condition, transmission route, delay, intermediate change, feedback, and relevant endpoint. Include thresholds only where a model, evidence, or a declared exploratory assumption supplies them. If several circles interact, identify the interface through which a change reaches another circle and what may stop, amplify, reroute, or delay it.

Use counterfactuals productively. Replace one condition while holding the needed background fixed, then ask which link changes and which result survives. A breakpoint can identify a minimal repair; an enabling condition can become a design lever; two compatible mechanisms can produce a new capability. Keep clear which premises were observed, inferred, or deliberately imagined. A counterfactual model does not automatically identify a causal effect.

Search material-supported competitors and residual paths. Consider whether the main account, a competing mechanism, a rare but consequential event, or an unmodeled residual could change the judgment. These are applicability questions, not required slots or a fixed number of scenarios. Do not invent an alternative or an unlikely catastrophe to fill a table. If only one path or mechanism survives a reasonable search, state its search scope, the reason, and failure conditions (§4.8.4, §11.9.3).

Prune by the task, not by convenience. A branch can be merged only if the retained identity, relevant state equivalence, history, and action constraints make it equivalent for this task. Keep a low-probability path when its consequences materially change protection or choice; low probability alone does not justify deleting it. Declare pruning and stopping rules before evaluating outcomes when making a formal evaluable claim. New evidence can reopen them with a preserved prior version.

Do not treat longer recursion, additional agents, or agreement among simulations as independent support. Each simulation round can reveal a further conditional consequence; its source and model lineage stay the same. Where a bridge across scales is needed, state what it preserves, changes, merges, or omits and the valid initial conditions, error, and time range. Short-run agreement in one statistic does not establish equivalence of whole states or long-run behavior (Appendix C.5).

## Decide which result the work earns

| Result | Required basis | How to present it |
|---|---|---|
| Conditional path | Declared premises and a defensible derivation. | “If these conditions hold, this path follows in this model”; identify unresolved premises. |
| Exploratory scenario | Coherent constructed conditions with their speculative status exposed. | A candidate future useful for discovery or design, without an implied likelihood. |
| Directional or ordered forecast | Evidence that supports the direction or ranking for the stated target and horizon. | The actual supported ordering, reference basis, uncertainty, and reversal conditions. |
| Quantitative forecast | Justified model and uncertainty treatment, relevant evaluation basis, and a pre-outcome registration. | The defined target, estimate or distribution, validity conditions, evaluation and update rules. |

Every formal conditional forecast, including an eligible directional one, needs a persistent registration before its target outcome is known, as specified in the [forecast contract](../contracts/forecast.md). Without this, deliver a derivation or an explicitly retrospective estimate; do not retroactively label it a registered forecast. Removing numbers does not make an unsupported direction or rank justified. When material cannot discriminate directions, return unranked conditional paths (§12.2).

For formal forecasting, use the provided [forecast tool](../scripts/forecast.py) or an equivalent externally maintained, reviewable, append-only registration. The record must preserve the target and outcome definition, issuance and evidence cutoff, conditions, relevant competitors and search limits, forecast, evaluation and failure rules, and update history. Registration makes the claim evaluable; it does not certify calibration or empirical validity. Preserve the complete registration history, including failed, expired, invalid, unresolved, and not-yet-due entries. Report the denominator appropriate to each evaluation, its population and exclusions, and missing outcomes separately; a missing label is not zero or a failed prediction. Do not discard an evaluable failure because a later model is better (§12.5).

## Turn uncertainty into useful work

Derive what would change the judgment: a measurable threshold, a distinct event, a resource arrival, a changed interface, or an assumption found false. This may generate a monitoring plan, a discriminating experiment, a reversible probe, or a condition-dependent policy. Some uncertain states share a common admissible action; if so, explain why the same action works across them instead of demanding full identification first (§12.10.1).

Continue in [discover](discover.md) when projections reveal a new mechanism or question; [create](create.md) when they specify a prototype, simulation, dashboard, test, or repair; [decide](decide.md) when comparing actions, burdens, and authority. Pass along actual derivations and unresolved premises, not just a scenario label. Use [composition](../references/composition.md) for dependencies and [continuity](../references/continuity.md) for later observations and revisions.

## Worked route: repair a delayed handoff

Suppose an observed workflow has two queues with different clocks. A file completed after 16:00 misses the receiving team's daily intake, adding a day even when both teams' local processing is fast. Derive three candidate changes only if feasible: move the handoff cutoff, add an intake window, or create an asynchronous acceptance check. Show which condition each removes, the added labor, and the cases each leaves unresolved. If a common acceptance check prevents the delay under both plausible arrival patterns, it may be a robust candidate despite uncertainty about their frequencies.

Build a small event model or a schedule prototype and test its boundary cases when requested. Deliver the candidate workflow and verification results. Predicting a measured reduction in actual delays requires a separately justified forecast; adopting the workflow needs the appropriate operational authority and safeguards. Neither requirement blocks completing the model or authorized prototype.

## Failure boundaries

A failed bridge narrows the cross-scale conclusion; a failed mechanism narrows the dependent path. Preserve independently supported events and valid local implications. If changed resources or powers make an old path infeasible, update that condition and its downstream results. Do not silently substitute the new task for the registered old one.

End projection when the question has been answered, added branches cannot materially change the requested result, the relevant resource budget is exhausted, or a specific unresolved premise makes further dependent work uninformative. State the remainder and deliver the useful result. There is no universal iteration count. A separate safety or legal trigger can require an immediate pause in an affected action; it does not erase the rest of the analysis.

Source basis: §§1.11, 2.14, 4.8.4, 4.18-4.19, 5.10.2; Parts 9-12; §§12.2, 12.10.1, 13.10; Appendix C.5. This path is a derived method; formal forecasting retains its own responsibility contract.
