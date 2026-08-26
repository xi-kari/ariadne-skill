---
name: ariadne-choice
description: "Compare action, delay, reversible experiment, exit, and inaction on one baseline, keeping facts, values, rights, jurisdiction, and authorization separate and issuing no permissions. Use when a real-world decision, pilot, exit, or act-or-not question needs a bounded option comparison with external requirements; when the decision hinges on an unregistered future claim, run ariadne-forecast first. For a multi-module pass, start with ariadne-skill. 适用于：该不该做、方案比较、试点与退出、不行动也是选项、授权边界。"
license: MIT
metadata:
  record_schema: "1.3"
---

# Ariadne Choice

## Overview

Compare a finite option set without turning facts, forecasts, efficiency, survival, or model confidence into an instruction. Keep value premises, protection, jurisdiction, procedure, authorization, execution, and correction separately inspectable.

## Route the Request

- Use this module when a subject must compare active action, delay, a reversible experiment, exit or transfer, and explicit inaction.
- Use `SEL-SYS` only to describe differential retention without intention or legitimacy. Do not include an external-action option or an `authorized` state.
- Use `SEL-AGT` for an identifiable subject choosing only within that subject's actual rights, territory, and time.
- Use `SEL-GOV` for a collective decision with agenda, representation, participation, minority protection, conflicts, accountability, and expiring public authority.
- Return to framing, evidence, forecast, or audit when the object, facts, future consequences, or governance integrity are not ready.

## Run the Choice

1. Freeze O1 (O1-O4 are the four operational freezes: O1 facts, O2 values, O3 subject and authority, O4 bounded execution): the descriptive claims, evidence status, uncertainty, scale, forecast references, and descriptive output ceiling. Do not repair them after seeing attractive options.
2. Classify the process as `SEL-SYS`, `SEL-AGT`, or `SEL-GOV`. Reject language that gives a system intent, extends one person's choice over others, or turns governance into a large personal preference.
3. Freeze O2: the runtime N1-N5 premises (N1 explanation does not authorize disposition, N2 protection must not degrade, N3 high-impact judgments must be correctable, N4 do not requisition love or care, N5 survival and selection are not legitimacy), each premise's role as goal, constraint, or veto, all value conflicts, dissent, beneficiaries, and burden bearers. Keep the PF-1-PF-10 rights floor (the ten protection bindings: affected positions, low-exposure submission, effective refusal, timed appeal, anti-retaliation, evidence correction, external review, operational rollback, real exit or proxy support, and a frozen action ceiling) separate from tradable preferences.
4. Create stable option IDs. Include exactly one `no_action` option and distinguish it from maintaining the status quo. Include active action, delay, reversible experiment, and exit or transfer when applicable.
5. Compare every option against the same baseline across consequences, distribution, nine-axis scale, affected and low-power positions, information value, reversibility, lock-in, resources, and residual harm. Keep incomparable dimensions and conflicts visible.
6. Check coercion, defaults, information, capacity, safe refusal, and real exit. For `SEL-GOV`, also check agenda control, representation, participation, minority protection, dissent, conflicts of interest, and execution accountability.
7. Freeze O3 and C12 (the ten-component validity bridge from description to normative choice): bind the selected option, explicit N premises, all ten bridge components, least-harm and proportionality reviews, protection floor, atomic J tuple, jurisdiction, validity period, and external verification references.
8. Freeze O4: cap execution at the narrowest intersection of evidence, values, rights, selected option, J authority, reversibility, trial scope, and expiry. Register prohibited actions, monitors, stop authority, appeal, anti-retaliation, independent review, rollback, remedy, and reauthorization.
9. Assign the record state and append every transition. Never erase `paused`, `stopped`, `rolled_back`, or expired history. Keep `authorization_effect` equal to `none`, including when the module verifies an external authorization record.

## Method Record

Create or extend a schema-valid Method Record with complete parent references, traced module inputs/output, and the ceiling transition (full schema: `ariadne-skill/references/method-record.schema.json`, shipped with the suite router; the standalone example in [references/choice-and-authorization.md](references/choice-and-authorization.md) is schema-checked in CI). For every action request, write the typed choice payload with facts, values, options including inaction, jurisdiction, authorization, stop conditions, and rollback plan. Use `unknown` rather than omit any boundary.

Use `description_only` for incomplete facts, `diagnostic_only` for bounded consequence comparison, and `requirements_only` only when lower permissions remain satisfied and external process requirements are explicit. Keep `authorization_effect: none`.

## Mini Example

Input question: "May we run a reversible workload pilot now, or must we not act?" Skeleton only, not a complete record:

```yaml
selection_type: SEL-AGT
options: [active_action, reversible_experiment, delay, no_action]
authorization: unknown
output_ceiling: description_only
```

## Stop and Handoff

Stop at inaction, evidence collection, protective preservation, continued review, or external referral whenever a positive N premise, a C12 component, a PF binding, atomic J coverage, O1-O4, safe dissent, or rollback capacity is absent. In an emergency, identify only the minimum protective action allowed by an external emergency rule, then require prompt review, appeal, and rollback.

Do not choose values for the subject, infer consent from silence or non-exit, sign authorization, execute an option, or guarantee success. Return plain-language comparison first, followed by the compact Method Record and, for high-impact cases, the detailed choice card.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Quick Reference

| Condition | Maximum response |
|---|---|
| `SEL-SYS` differential retention | Description only; no external-action option or authorization. |
| Facts ready, values unresolved | Show conflicts and consequences; retain inaction. |
| Values stated, PF or J incomplete | Requirements, protection, and referral only. |
| External authorization exists but mismatches one action field | Treat the option as unauthorized. |
| Evidence weak and action reversible with clear authority | Consider only a bounded information-gathering trial. |
| Irreversible harm, failed protection, or no rollback | Pause or choose protective inaction. |

## Common Mistakes

- **Deriving “ought” from “is”:** Freeze facts in O1 and values in O2 as separate records.
- **Deleting inaction:** Include exactly one `no_action` and price its continuing harms and responsibilities.
- **Treating status quo as no action:** Record the resources and enforcement required to maintain the status quo.
- **Aggregating away burden:** Preserve low-power, overlapping, bridge, cross-domain, and long-horizon positions.
- **Patching authority:** Require one atomic J tuple to cover subject, object, action, territory, full period, and authority source, as section 8 of the reference enumerates.
- **Calling formal participation consent:** Test safe refusal, exit, dissent effect, and anti-retaliation.
- **Using a pilot as an ethics exemption:** Apply the same protection, stop, appeal, rollback, data-use, and remedy duties.
- **Letting the module authorize:** Verify external records only and keep `authorization_effect: none`.

## Load Detailed Guidance

Read [choice-and-authorization.md](references/choice-and-authorization.md) when defining N, PF, J, O1-O4, C12, boundary cards, options, distribution, selection states, intervention ceilings, T0-T4 tasks (the five intervention task types: T0 safety carrier, T1 reversible minimum order, T2 carrying-return repair, T3 deep-time maintenance, T4 exit and memory preservation), or the worked example. Read [intervention-levels.json](references/intervention-levels.json) for the T0-T4 machine contract covering entry conditions and the hash-chained execution-state log. Handoff any domain application to `ariadne-audit` for its matching Part 15 APP contract (APP-REL through APP-ULS, the nine domain application contracts) before external use.
