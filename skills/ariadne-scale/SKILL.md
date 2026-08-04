---
name: ariadne-scale
description: Use when reasoning crosses individual and collective levels, short and long time windows, local and global scopes, nested circles, representations, or vocabularies.
---

# Ariadne Scale

## Overview

Audit what happens when an object, observation, claim, or action moves between scale profiles, circles, representations, or vocabularies. Register what is preserved, changed, lost, uncertain, and non-transferable instead of treating a shared label as a bridge.

## Procedure

1. **Consume or start the Method Record.** Preserve its object contract, cutoff, claim ledger, unknowns, lineage, and ceiling. If no record exists, create a minimum candidate object before comparing scales.
2. **Freeze both endpoints.** Declare source and target `SP=<A,X,T,O,C,R,I,N,J>` profiles, task, time window, identity criteria, and evidence cutoff. Use an explicit missing state for every unavailable or inapplicable axis.
3. **Compare each axis.** Assign exactly one relation: `equal`, `expands`, `contracts`, `incomparable`, or `unknown`. Require a reproducible, axis-specific witness for every non-unknown relation.
4. **Classify the profile change.** Apply the fixed precedence: any incomparable axis gives `horizontal_or_incomparable`; otherwise expansions plus contractions give `mixed`; otherwise any unknown gives `unresolved`; then `all_equal`, `elevation`, or `reduction`. Use “scale elevation” only for the strict product-order case.
5. **Separate transformation kinds.** Distinguish scale transformation, circle-relation change, and representation or wording translation. Split a combined process into an ordered chain.
6. **Choose one atomic operator.** Select exactly one of M01-M09 and one compatible branch and claim mode for each atomic record. Do not switch branch or mode after seeing results.
7. **Audit identity, evidence, and loss.** Record source and target K, mapping, preserved and allowed changes, lost or collapsed distinctions, error, alternatives, residuals, and independent evidence on both sides. Treat three evaluated outcomes (`supported`, `unsupported_or_undecided`, `null_supported`) separately from `not_evaluated`.
8. **Update the Method Record.** Use `description_only` for an incomplete mapping and `diagnostic_only` for a bounded transfer audit. Add `requirements_only` only after that diagnostic basis when an external process must satisfy named bridge requirements. Apply the inherited-ceiling transition algebra. Never transfer values, responsibility, or authority. Keep `authorization_effect: none`.

Read [references/scale-transformations.md](references/scale-transformations.md) for axis contracts, operator signatures, identity mapping, circle relations, translation-loss auditing, and a complete standalone example.

## Method Record Contract

Produce every common field, summarize the endpoints and status in `scale_scope`, add an `ariadne-scale` module run, and put failed mappings, lost distinctions, residuals, and unknown axes in `unknowns_and_counterevidence`. Create a child version when an endpoint, operator, mapping, identity criterion, task, cutoff, or loss tolerance changes.

Do not loosen an incoming output ceiling. Never change `authorization_effect` from `none`; a broader geographic, organizational, observational, causal, influence, or network scope does not expand J jurisdiction.

## Quick Reference

| Situation | Use | Stop at |
|---|---|---|
| Individuals to a group statistic | M01 aggregation + distribution-loss audit | No inference back to each member |
| Unit contained in a larger unit | M02 nesting + membership/interface basis | No upper-level priority or causality |
| Effect moves through a graph | M03 propagation + path, delay, loss, alternatives | No intent, responsibility, or authority |
| Short to long window | M04 temporal accumulation + baseline and lag | No accumulation or path claim without evidence |
| Rich material to a summary | M08 compression + recoverability and task invariants | No collapse of missing states into absence |
| Source domain to target domain | M09 horizontal transfer + target-side evidence | Target hypothesis only |

## Stopping Conditions

Stop at parallel descriptions when an endpoint, bridge, or identity mapping is missing. Mark the transformation `failed` when a prohibited mapping occurs. Return to the source scale when task-relevant loss exceeds tolerance. Route channel identification to `ariadne-evidence` or `ariadne-mechanism`, human protection to `ariadne-human`, action comparisons to `ariadne-choice`, and high-impact transfer review to `ariadne-audit`.

## Common Mistakes

- Calling any move toward a larger unit, area, window, or organization “scale elevation.”
- Inferring individual properties from a group statistic or a group will from membership.
- Treating nesting, overlap, contact, propagation, representation, and authorization as the same relation.
- Reusing a word at two scales without a mapping and identity audit.
- Calling a failed positive test proof of no cross-scale effect.
- Treating more observation, influence, rank, or network centrality as more jurisdiction.
- Compressing `unknown`, `not_applicable`, `not_observable`, or `withheld_for_protection` into “absent.”
