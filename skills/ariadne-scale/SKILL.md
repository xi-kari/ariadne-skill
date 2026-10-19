---
name: ariadne-scale
description: "Audit what survives a move between scales, circles, representations, or vocabularies: what is preserved, changed, collapsed, lost, or incomparable, and whether a coarser representation still answers the task, closes over time, survives allowed actions, and joins with other steps. Use when reasoning crosses individual and collective levels, local and global scopes, short and long windows, or domains. For a multi-module pass, start with ariadne-skill. 适用于：个体结论能否推到群体、试点能否推广、换个说法丢了什么、汇总够不够用。"
license: MIT
metadata:
  record_schema: "2.0"
---

# Ariadne Scale

## Overview

Audit what happens when an object, observation, claim, or action moves between scale profiles, circles, representations, or vocabularies. Register what is preserved, changed, collapsed, lost, uncertain, and non-transferable instead of treating a shared label as a bridge. Judge every representation against the declared task: never presume a move is lossless, and never presume it must lose what the task needs.

## Procedure

1. **Consume or start the Method Record.** Preserve its object contract and task profile, cutoff, claim ledger, unknowns, lineage, and ceiling. If no record exists, create a minimum candidate object before comparing scales.
2. **Freeze both endpoints and the task.** Declare source and target `SP=<A,X,T,O,C,R,I,N,J>` profiles, the target query, horizon, environment, allowed operations, error tolerance, time window, identity criteria, and evidence cutoff. The nine axes are A aggregation, X spatial scope, T temporal span, O organizational level, C causal level, R observation resolution, I influence scope, N network-topology scope, and J jurisdiction and authorization. Use an explicit missing state for every unavailable or inapplicable axis.
3. **Separate transformation kinds.** Distinguish scale transformation, circle-relation change, and representation or wording translation, and record the kind in `scale_scope.transform_kind`. Split a combined process into an ordered chain whose adjacent endpoints match.
4. **Compare each axis.** Assign exactly one relation: `equal`, `expands`, `contracts`, `incomparable`, or `unknown`. Require a reproducible, axis-specific witness for every non-unknown relation.
5. **Classify the profile change.** Apply the fixed precedence: any incomparable axis gives `horizontal_or_incomparable`; otherwise expansions plus contractions give `mixed`; otherwise any unknown gives `unresolved`; then `all_equal`, `elevation`, or `reduction`. Use "scale elevation" only for the strict product-order case.
6. **Choose one atomic operator.** Select exactly one of M01-M09 and one compatible branch and claim mode for each atomic record: M01 aggregation, M02 nesting, M03 network propagation, M04 temporal accumulation, M05 institutionalization, M06 emergence, M07 delegation or representation, M08 compression or abstraction, and M09 horizontal transfer. Do not switch branch or mode after seeing results.
7. **Check sufficiency for the task.** Test separately whether the target representation answers the static query (F1), advances its own dynamics over the horizon (F2), and still suffices under the allowed operations. When it falls short, prefer the minimal repair: add the distinction the task needs, keep composition or history, restrict the action set, shorten the horizon, or narrow the use. Changing the task is a new question, never completion of the old one.
8. **Audit identity, evidence, loss, and joins.** Record source and target K, mapping, preserved and allowed changes, collapsed distinctions, omissions, additions, error, alternatives, residuals, and independent evidence on both sides. Keep representation loss apart from rule misuse. At chain level, check function composition, joint causal response, and joint resource feasibility separately. Treat three evaluated outcomes (`supported`, `unsupported_or_undecided`, `null_supported`) separately from `not_evaluated`.
9. **Update the Method Record.** Use `description_only` for an incomplete mapping and `diagnostic_only` for a bounded transfer audit. Add `requirements_only` only after that diagnostic basis when an external process must satisfy named bridge requirements. Apply the inherited-ceiling transition algebra. Never transfer values, responsibility, or authority. Keep `authorization_effect: none`.

Read [references/scale-transformations.md](references/scale-transformations.md) for axis contracts, operator signatures, chain-level evaluation, identity mapping, circle relations, protection applicability, translation-loss auditing, and a complete standalone example. Read [references/representation-and-closure.md](references/representation-and-closure.md) for the formal propositions F1-F6, worked closure examples, the three composition boundaries, the mathematical scale-bridge discipline, and cross-text difference retention.

## Method Record Contract

Produce every common field (full schema: `ariadne-skill/references/method-record.schema.json`, shipped with the suite router; the standalone example in [references/scale-transformations.md](references/scale-transformations.md) is schema-checked in CI), summarize the endpoints, transform kind, and status in `scale_scope`, add an `ariadne-scale` module run, and put failed mappings, collapsed distinctions, residuals, unknown axes, and chain breakpoints in `unknowns_and_counterevidence`. Create a child version when an endpoint, operator, mapping, identity criterion, task, cutoff, or loss tolerance changes.

Do not loosen an incoming output ceiling. Never change `authorization_effect` from `none`; a broader geographic, organizational, observational, causal, influence, or network scope does not expand J jurisdiction.

## Quick Reference

| Situation | Use | Stop at |
|---|---|---|
| Individuals to a group statistic | M01 aggregation with a fixed estimand + distribution-loss audit | No inference back to each member |
| Unit contained in a larger unit | M02 nesting, one branch | No upper-level priority, duty, or causality from membership |
| Effect moves through a graph | M03 propagation + path, delay, loss, shared sources, alternatives | No intent, responsibility, or authority |
| Short to long window | M04 temporal accumulation + baseline and lag | No accumulation or path claim without evidence |
| Rich material to a summary | M08 compression + F1 sufficiency and task invariants | No collapse of missing states into absence |
| Summary used for a new query or operation | F1/F2 checks against the new task | No reuse of earlier sufficiency |
| Steps each succeed | Function, joint-response, and resource checks | No generic "connected" status |
| Source domain to target domain | M09 horizontal transfer + target-side evidence | Target hypothesis only |

## Mini Example

Skeleton only, not a complete record; the schema-valid template ships with the suite router as `l1-record-template.md`.

```yaml
# Input: "Our one-city pilot worked, so the national rollout will work."
scale_scope:
  source: one-city pilot cohort
  target: national rollout population
  transform_kind: scale
  transform_status: candidate
output_ceiling: description_only
```

## Stopping Conditions

Stop at parallel descriptions when an endpoint, bridge, or identity mapping is missing. Mark the transformation `failed` when a prohibited mapping occurs. Return to the source scale when task-relevant loss exceeds tolerance. Keep a simple representation when it already answers the task and neighboring detail adds nothing. Route channel identification to `ariadne-evidence` or `ariadne-mechanism`, human protection to `ariadne-human`, action comparisons to `ariadne-choice`, and high-impact transfer review to `ariadne-audit`.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Common Mistakes

- Calling any move toward a larger unit, area, window, or organization "scale elevation."
- Inferring individual properties from a group statistic or a group will from membership.
- Treating nesting, overlap, contact, propagation, representation, and authorization as the same relation.
- Reusing a word at two scales without a mapping and identity audit.
- Assuming every translation loses meaning, or that a round trip proves none was lost.
- Blaming the representation for a rule error, or the rule for a representation that cannot carry the distinction.
- Treating static adequacy as dynamic closure, or closure under routine conditions as closure under intervention.
- Multiplying two link averages, or reading separately feasible options as jointly feasible.
- Calling a failed positive test proof of no cross-scale effect.
- Treating more observation, influence, rank, or network centrality as more jurisdiction.
- Compressing `unknown`, `not_applicable`, `not_observable`, or `withheld_for_protection` into "absent."
