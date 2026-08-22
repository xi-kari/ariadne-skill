---
name: ariadne-human
description: "Constrain human-domain analysis so people are never reduced to fixed labels: roles, circles, power, privacy, responsibility, and meaning stay separate, evidence-bounded records. Use when analyzing people, relationships, teams, organizations, institutions, or multi-circle joint objects without personality or clinical diagnosis. Part of the Ariadne methodology suite. 适用于：人际与组织分析、角色与圈层、权力与隐私、责任与意义边界。"
license: MIT
metadata:
  record_schema: "1.2"
---

# Ariadne Human

## Overview

Apply human-domain clauses without turning people into fixed labels or collectives into persons. Preserve roles, power, privacy, responsibility, meaning, multiple membership, and material conditions as separate, evidence-bounded records.

## Standalone Contract

Create or extend a schema-valid Method Record. Preserve complete parent ID/version lineage, trace this module's input and output records, record the ceiling transition, and use the typed human payload for observation position, privacy, purpose, affected positions, alternatives, and responsible human review. `affected_positions` is a closed object with all four keys: `direct`, `indirect`, `low_power`, and `no_exit`. Each key records status, positions, and reason; use explicit `unknown`, `not_applicable`, or `withheld_for_protection` rather than one free-text substitute.

Set `authorization_effect` to `none`. A module run preserves or lowers its parent ceiling; only a child with newly admitted external evidence or a newly fulfilled protocol may raise it. Use `description_only` for observations and candidate classifications, `diagnostic_only` for bounded human-system explanations, and `requirements_only` only when a retained diagnosis is accompanied by explicit privacy, protection, appeal, evidence, or external authorization requirements.

## Procedure

1. Classify the requested result. Separate human description or diagnosis from clinical assessment, personality adjudication, forecast, normative choice, intervention, and authorization.
2. Freeze the human object, boundary, `SP/T/K` (nine-axis scale profile, time window, and identity criterion), observation position, evidence cutoff, affected positions, and allowed use. Distinguish an actor, a circle, and a multi-circle joint object.
3. Preserve missing information as `not_collected`, `not_observable`, `not_applicable`, `conflicted`, `unknown`, or `withheld_for_protection`. Treat refusal and silence as no available information, not as evidence of intent, risk, consent, or character.
4. Separate the H1 (meaning and coordination), H4 (power, mediation, and reflexivity), and H5 (historical trace carrier) empirical hypotheses from the H2 (carrying and responsibility separation) and H3 (institutional writeback) classification rules and the H6 (open-ended bearing) normative boundary. Require eligible H-instances for empirical elevation.
5. Separate GC, GS, GE, CV, RS, IS, IM, and IB (the eight strong types: generation condition, generating subject, generation event, carrying vehicle, responsible subject, instability source, instability mechanism, and instability behavior). Require independent evidence for each strong type; never infer responsibility, intent, or mechanism from visibility or behavior alone.
6. Route only applicable HV01-HV11 interfaces (the eleven human-variable cards: structural domain, boundary and interface, directional anchor, generation node, carrying layer, motive-carrying chain, feedback writeback, conditional field, structural load, evolutionary phase, and open-ended bearing action). Fill their common field contract, choose one conditional support route at a time, and keep U01-U11 (the general structural primitives owned by `ariadne-mechanism`) and HV01-HV11 distinct.
7. For an actor, record roles; slow, medium, and fast variables; material and experience-meaning conditions; evidence state; privacy; and permitted use. Prefer role and circle conditions before adding a personality hypothesis.
8. Use S0-S6 only as reversible prototypes for intentional human collectives (S0 anchor condensation, S1 generative-core foundation, S2 first expansion and carrying differentiation, S3 development under connected constraints, S4 structural-reconfiguration window, S5 efficient coordination and elastic expansion, S6 adaptive dynamic balance). Before classifying a collective, load the [state-prototype cards](references/state-prototypes.json) and register every face of each candidate — entry, exit, observables, counterexamples, falsifiers, scale boundary, evidence elevation, contract links, and non-authorization — in the runtime classification record. Allow `single_dominant`, `mixed`, `parallel`, or `unknown`; keep nonlinear paths and X0 (orderly exit) separate; never assign a collective prototype to an individual.
9. For multiple circles, register each `C*` (candidate circle), the joint `MC*` (multi-circle joint object), six relation types, multiple membership, material and experience-meaning channels, five asynchronous clocks, boundary sensitivity, and the simple-model comparison.
10. Write only supported observations, candidate hypotheses, bounded classifications, competing explanations, privacy limits, and next evidence needs into the record. For every high-impact output, include at least two distinct alternative explanations, the privacy state, and the four separately closed affected-position classes. An identified class names at least one position; an unknown, non-applicable, or protected class has an empty positions list and a reason. Add a named responsible human review with status. Preserve counterevidence and identify only necessary handoffs.

Stop before clinical inference, personality essence, value ranking, punishment, compelled disclosure, resource redistribution, responsibility assignment beyond available evidence, or real-world authorization. Route propagation to `ariadne-dynamics`, evidence repair to `ariadne-evidence`, and value or action questions onward without deciding them here.

If a routed peer skill is unavailable in this installation, record the handoff in module_runs as not_run with reason module_unavailable, keep that responsibility's outputs unknown, preserve or lower the output ceiling, and do not execute the peer's responsibility inline or claim it ran.

## Quick Reference

| Need | Apply |
|---|---|
| Meaning, power, history, carrying, or writeback | H1-H6 with their distinct roles |
| Conditions, actors, events, carriers, responsibility, or instability | GC/GS/GE/CV/RS/IS/IM/IB |
| Human variable interface | HV01-HV11 common card and one support route |
| Individual state | Actor snapshot with slow/medium/fast variables and use limits |
| Collective configuration | S0-S6, nonlinear path, or X0 without rank or destiny |
| Interacting circles | `C*`, `MC*`, six relations, dual channels, five clocks, complexity gate |

## Mini Example

```yaml
# Input: "Is this five-person volunteer project one working collective, and in what state?"
request_type: human_domain_analysis
object: {object_id: C-volunteers-01, kind: circle}
state_classification: {mode: single_dominant, candidates: [S1]}
affected_positions: {direct: identified, low_power: unknown}
output_ceiling: description_only
```

## Common Mistakes

- Turning one behavior, role response, silence, or refusal into personality or diagnosis.
- Applying S0-S6 to a person, or treating a larger number as better, more mature, or more authorized.
- Collapsing a carrier into a responsible subject, an instability behavior into a source, or a person into a mechanism.
- Treating public language as shared meaning, membership as consent, visibility as representativeness, or receipt as institutional writeback.
- Filling protected or absent information by inference, or reusing sensitive material outside its allowed purpose.
- Averaging away low-power positions, role conflicts, disputed evidence, dual-channel differences, or asynchronous clocks.
- Adding circles that do not explain a residual or improve on the simple baseline.

Read [human-domain.md](references/human-domain.md) for H contracts, actor and collective boundaries, multi-circle contracts, and protection rules. In the [HV01-HV11 interface cards](references/human-variable-cards.json), read the file-header `toc` and the common field contract first, then read only the cards your route actually hit; do not reconstruct a card from summaries. Load the [S0-S6 and X0 state-prototype cards](references/state-prototypes.json) before any collective state classification.
