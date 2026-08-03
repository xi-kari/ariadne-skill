---
name: ariadne-dynamics
description: Use when a task asks how events propagate through states, clocks, thresholds, feedback loops, circles, branches, scenarios, or recursive simulations.
---

# Ariadne Dynamics

## Overview

Derive conditional event paths from a frozen state. Preserve event fact status, mechanism provenance, asynchronous clocks, branches, residuals, and the rule that simulation depth never creates evidence.

## Standalone Contract

Create a minimal common Method Record when none is supplied. Preserve an incoming record and its lineage when one is supplied. Populate `record_id`, `schema_version`, `record_version`, `parent_record_id`, `request_type`, `object_contract`, `evidence_cutoff`, `scale_scope`, `claim_ledger`, `unknowns_and_counterevidence`, `output_ceiling`, `module_runs`, `recommended_next_modules`, and `authorization_effect`.

Set `authorization_effect` to `none`. Keep or lower an inherited ceiling. Use `description_only` when the starting state, event, or mechanism is inadequate, `diagnostic_only` for bounded conditional paths, and `requirements_only` when only the missing conditions for a valid derivation can be reported.

## Procedure

1. Classify the requested result as dynamic derivation. Separate it from factual verification, forecast registration, choice, intervention, and authorization.
2. Freeze the joint starting state, object identities, evidence cutoff, model version, mechanism assumptions, parameter ranges, five clocks, propagation policy, unknowns, and stopping conditions. Do not backfill the start with later information.
3. Create a separate event contract for every observed, reported, planned, hypothetical, or simulated event. Preserve its fact status, source, time, affected actors and circles, channel, direct change, dispute, reversibility, duration, and follow-up observation.
4. Update `Omega(t)` without mixing direct observation, supported mechanism inference, scenario value, and unexplained residual. Treat an unapproved action only as a hypothetical input.
5. Run the nine-step loop: freeze state; identify actors and circles; separate material and experience-meaning conditions; declare clocks, thresholds, capacity, and delay; inject events; propagate only along declared channels; branch; register signals, residuals, and variable candidates; plan result writeback.
6. Build a directed acyclic path graph. Time-expand feedback loops, keep mutually exclusive and parallel paths distinct, merge only under explicit equivalence conditions, and retain fact, mechanism, choice, and disturbance uncertainty separately.
7. Run scenarios, counterfactuals, or simulations only with explicit rules and comparable conditions. Preserve parent lineage and inherited unknowns for every recursive re-entry.
8. Use three orders as the default exploratory recursion ceiling. Keep the principal path, strongest competitor, low-probability high-consequence path, and residual exit. Apply declared pruning and early-stop rules.
9. Return the frozen snapshot, event status, assumptions, path graph, clocks, conditions, support states, early and reverse signals, residuals, variable candidates, stop record, and writeback plan. Preserve unranked branches when evidence cannot compare them.

Stop when identity or scale fails, a key event or channel is unresolved, branches lack discriminating signals, sensitivity or residuals exceed the use threshold, a deeper order adds no value over a shallower run or simple baseline, privacy or safety costs dominate, or the request crosses prediction or authorization boundaries. Route preregistered future claims to `ariadne-forecast` and action questions onward without answering them here.

## Quick Reference

| Need | Apply |
|---|---|
| Admit an input | Event type and fact-status contract |
| Freeze a start | `Omega(t)` joint snapshot plus evidence cutoff |
| Propagate a change | Channel, direction, capacity, delay, threshold, loss, and recovery |
| Represent uncertainty | Conditional DAG with typed branch sources and signals |
| Add a missing variable | Residual-driven candidate ledger and minimum discriminating test |
| Re-enter a simulated future | Parent lineage, translation audit, inherited unknowns, and unchanged evidence ceiling |

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
