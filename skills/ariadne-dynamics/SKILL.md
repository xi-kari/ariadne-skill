---
name: ariadne-dynamics
description: "Derive conditional event paths from a frozen state: propagation along declared channels, clocks, thresholds, feedback, branch graphs, counterfactual and recursive simulation, and stopping conditions. Use when events, cascades, or institutional transitions need bounded path derivation; for a dated, evaluable future claim use ariadne-forecast instead. Part of the Ariadne methodology suite. 适用于：事件传播推演、条件分支、级联与阈值、情景与反事实模拟。"
license: MIT
metadata:
  record_schema: "1.2"
---

# Ariadne Dynamics

## Overview

Derive conditional event paths from a frozen state. Preserve event fact status, mechanism provenance, asynchronous clocks, branches, residuals, and the rule that simulation depth never creates evidence.

## Standalone Contract

Create or extend a schema-valid Method Record. Preserve complete parent ID/version lineage, trace this module's input and output records, record the ceiling transition, and use the typed dynamics payload for event fact status, sources, windows, observation position, and model version.

Set `authorization_effect` to `none`. A module run preserves or lowers its parent ceiling; only a child with newly admitted external evidence or a newly fulfilled protocol may raise it. Use `description_only` when the starting state, event, or mechanism is inadequate, `diagnostic_only` for bounded conditional paths, and `requirements_only` only when a retained diagnosis is accompanied by explicit external process requirements.

## Procedure

1. Classify the requested result as dynamic derivation. Separate it from factual verification, forecast registration, choice, intervention, and authorization.
2. Freeze the joint starting state, object identities, evidence cutoff, model version, mechanism assumptions, parameter ranges, five clocks, propagation policy, unknowns, and stopping conditions. Do not backfill the start with later information.
3. Create a separate event contract for every observed, reported, planned, hypothetical, or simulated event. Preserve its fact status, source, time, affected actors and circles, channel, direct change, dispute, reversibility, duration, and follow-up observation.
4. Update `Omega(t)`, the frozen joint state snapshot, without mixing direct observation, supported mechanism inference, scenario value, and unexplained residual. Treat an unapproved action only as a hypothetical input.
5. Run the nine-step loop: freeze state; identify actors and circles; separate material and experience-meaning conditions; declare clocks, thresholds, capacity, and delay; inject events; propagate only along declared channels; branch; register signals, residuals, and variable candidates; plan result writeback.
6. Build a directed acyclic path graph. Time-expand feedback loops, keep mutually exclusive and parallel paths distinct, merge only under explicit equivalence conditions, and retain fact, mechanism, choice, and disturbance uncertainty separately.
7. Run scenarios, counterfactuals, or simulations only with explicit rules and comparable conditions. Preserve parent lineage and inherited unknowns for every recursive re-entry.
8. Use three orders as the default exploratory recursion ceiling. Keep the principal path, strongest competitor, low-probability high-consequence path, and residual exit. Apply declared pruning and early-stop rules.
9. Return the frozen snapshot, event status, assumptions, path graph, clocks, conditions, support states, early and reverse signals, residuals, variable candidates, stop record, and writeback plan. Preserve unranked branches when evidence cannot compare them.

Stop when identity or scale fails, a key event or channel is unresolved, branches lack discriminating signals, sensitivity or residuals exceed the use threshold, a deeper order adds no value over a shallower run or simple baseline, privacy or safety costs dominate, or the request crosses prediction or authorization boundaries. Route preregistered future claims to `ariadne-forecast` and action questions onward without answering them here.

If a routed peer skill is unavailable in this installation, record the handoff in module_runs as not_run with reason module_unavailable, keep that responsibility's outputs unknown, preserve or lower the output ceiling, and do not execute the peer's responsibility inline or claim it ran.

## Quick Reference

| Need | Apply |
|---|---|
| Admit an input | Event type and fact-status contract |
| Freeze a start | `Omega(t)` joint snapshot plus evidence cutoff |
| Propagate a change | Channel, direction, capacity, delay, threshold, loss, and recovery |
| Represent uncertainty | Conditional DAG with typed branch sources and signals |
| Add a missing variable | Residual-driven candidate ledger and minimum discriminating test |
| Re-enter a simulated future | Parent lineage, translation audit, inherited unknowns, and unchanged evidence ceiling |

## Mini Example

```yaml
# Input: "What could follow if the lead engineer resigns next week?"
request_type: dynamic_derivation
event: {event_id: E1, fact_status: hypothetical, channel: resignation notice to team}
branches: [notice-only, delayed-backfill, second-exit-cascade]
output_ceiling: description_only
```

## Common Mistakes

- Treating a report, plan, hypothetical, or simulated event as an observed fact.
- Letting a formula or coherent story substitute for a mechanism and channel.
- Updating all variables at once or collapsing immediate, interaction, organizational, institutional, and long-term clocks.
- Treating signal arrival as state change, feedback as learning, or a local change as a complete cascade.
- Forcing one path, one probability, or one ranking when current evidence supports multiple branches.
- Deleting residuals, inventing a variable value, or using post-result candidates to support the original path.
- Treating deeper recursion, more samples, or narrower assumptions as stronger real-world evidence.
- Pruning a low-probability high-consequence branch solely because it is unlikely.

Read [dynamic-derivation.md](references/dynamic-derivation.md) for the event, state, clock, branch, recursion, stopping, and worked-example contracts.
