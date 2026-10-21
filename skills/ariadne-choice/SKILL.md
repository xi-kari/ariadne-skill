---
name: ariadne-choice
description: "Compare action, delay, probing, exit, and no action on one baseline, then give an analytic recommendation for deliberation under explicit norms, with costs, objections, and change conditions, keeping rights, jurisdiction, and authorization separate and issuing no permissions. Use when a decision, pilot, exit, or act-or-not question needs a bounded option comparison; run ariadne-forecast first if it hinges on an unregistered future claim. For a multi-module pass, start with ariadne-skill. 适用于：该不该做、方案比较与推荐、不行动也是选项。"
license: MIT
metadata:
  record_schema: "2.0"
---

# Ariadne Choice

## Overview

Compare a finite option set and, when explicit normative premises and evidence allow, say which option the analysis currently recommends and why. Keep two identities apart: an analytic recommendation for deliberation, which the module may form, and an authorized choice, which only a qualified subject with valid authority can make. Never turn facts, forecasts, efficiency, survival, or model confidence into an instruction, and never send a supported analysis back to a question list merely because no one has authority to execute.

## Route the Request

- Use this module when a subject must compare active action, delay, a reversible probe, exit or transfer, maintaining the status quo, and explicit no action.
- Use `SEL-SYS` only to describe differential retention without intention or legitimacy. Do not include an external-action option or an `authorized` state.
- Use `SEL-AGT` for an identifiable subject choosing only within that subject's actual rights, territory, and time.
- Use `SEL-GOV` for a collective decision with agenda, representation, participation, minority protection, conflicts, accountability, and expiring public authority.
- Return to framing, evidence, forecast, or audit when the object, facts, future consequences, or governance integrity are not ready.

## Run the Choice

1. Freeze O1 (O1-O4 are the four operational freezes: O1 facts, O2 values, O3 options, subject, and authority, O4 bounded execution): the descriptive claims, evidence status, uncertainty, scale, forecast references, and descriptive output ceiling. Do not repair them after seeing attractive options.
2. Classify the process as `SEL-SYS`, `SEL-AGT`, or `SEL-GOV`. Reject language that gives a system intent, extends one person's choice over others, or turns governance into a large personal preference.
3. Freeze O2: the runtime N1-N5 premises (N1 explanation does not authorize disposition, N2 protection must not degrade, N3 high-impact judgments must be correctable, N4 do not requisition love or bearing, N5 survival and selection are not legitimacy), each premise's role as goal, constraint, or veto, all value conflicts, dissent, beneficiaries, and burden bearers. Keep the PF-1-PF-10 rights floor (the ten protection bindings: affected positions, low-exposure submission, effective refusal, timed appeal, anti-retaliation, evidence correction, external review, operational rollback, real exit or proxy support, and a frozen action ceiling) separate from tradable preferences.
4. Create stable option IDs with kinds. Include exactly one `no_action` option and distinguish it from `maintain_status_quo`. Check active action, delay, probing, and exit or transfer for applicability and give reasons for any omitted.
5. Compare every option against the same baseline across consequences, distribution, nine-axis scale, affected and low-power positions, worst acceptable outcome, information value, reversibility, lock-in, resources, joint feasibility with other options, and residual harm. Keep incomparable dimensions and conflicts visible; never sum them away.
6. Check coercion, defaults, information, capacity, safe refusal, and real exit. For `SEL-GOV`, also check agenda control, representation, participation, minority protection, dissent, conflicts of interest, and execution accountability. Ask separately about resources, standing, and representation.
7. Form the analytic recommendation when premises allow: the recommended option, the explicit N premises it rests on, reasons, costs, objections, change conditions, and `adoption_status: deliberation_only`. Withhold it only for the specific missing norm, protection, or option that blocks it, and say which. With only N1 or no positive premise, the recommendation is limited to no action, more evidence, or continued deliberation.
8. For real adoption, freeze O3 and C12 (the ten-component validity bridge from description to normative choice): the selected option, explicit N premises, all ten bridge components, least-harm and proportionality reviews, protection floor, atomic J tuple, jurisdiction, validity period, and external verification references. Then freeze O4: cap execution at the narrowest intersection of evidence, values, rights, selected option, J authority, reversibility, trial scope, and expiry, with prohibited actions, monitors, stop authority, appeal, anti-retaliation, independent review, rollback, remedy, and reauthorization.
9. Assign the record state and append every transition. Never erase `paused`, `stopped`, `rolled_back`, or expired history. Keep `authorization_effect` equal to `none`, including when the module verifies an external authorization record.

## Method Record

Create or extend a schema-valid Method Record with complete parent references, traced module inputs/output, and the ceiling transition (full schema: `ariadne-skill/references/method-record.schema.json`, shipped with the suite router; the lineage example in [references/choice-and-authorization.md](references/choice-and-authorization.md) is schema-checked in CI). For every action request, write the typed choice payload with facts, values, structured options (`option_id`, `kind`, `description`, exactly one `no_action`), jurisdiction, authorization, stop conditions, rollback plan, and `analytic_recommendation` as an object or explicit `null`. Use `unknown` rather than omit any boundary.

Use `description_only` for incomplete facts, `diagnostic_only` for bounded consequence comparison, and `requirements_only` when lower permissions remain satisfied and external process requirements are explicit; a non-null analytic recommendation requires `requirements_only`, and each of its premise IDs must resolve to an N claim or normative rule in the record. Because a root record always starts at `description_only`, a recommendation lives in a child that admits its basis. Keep `authorization_effect: none`.

## Mini Example

Input question: "May we run a reversible workload pilot now, or must we not act?" Skeleton only, not a complete record:

```yaml
selection_type: SEL-AGT
options: [{id: OPT-TRIAL, kind: probing_action}, {id: OPT-DELAY, kind: delayed_action}, {id: OPT-NONE, kind: no_action}]
analytic_recommendation: {option_id: OPT-TRIAL, adoption_status: deliberation_only}
authorization: unknown
output_ceiling: requirements_only
```

## Stop and Handoff

Stop real adoption at no action, evidence collection, protective preservation, continued review, or external referral whenever a positive N premise, a C12 component, a PF binding, atomic J coverage, O1-O4, safe dissent, or rollback capacity is absent; the analytic comparison and any supported recommendation remain. In an emergency, identify only the minimum protective action allowed by an external emergency rule, then require prompt review, appeal, and rollback.

Do not choose values for the subject, infer consent from silence or non-exit, sign authorization, execute an option, or guarantee success. Lead with the current analytic recommendation and its scope, then the full comparison: reasons for accepting and rejecting each option, costs and their distribution, objections, change conditions, and what real adoption still needs. Never phrase a recommendation in imperative mood or as an executable decision.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Quick Reference

| Condition | Maximum response |
|---|---|
| `SEL-SYS` differential retention | Description only; no external-action option or authorization. |
| Facts ready, values unresolved | Show conflicts and consequences; retain no action; recommendation withheld for the named missing premise. |
| Values stated, options and costs registered | Analytic recommendation for deliberation, with execution marked not authorized. |
| Values stated, PF or J incomplete | Recommendation plus requirements, protection, and referral; no execution. |
| External authorization exists but mismatches one action field | Treat the option as unauthorized. |
| Evidence weak and action reversible with clear authority | Consider only a bounded information-gathering trial. |
| Irreversible harm, failed protection, or no rollback | Pause or choose protective no action. |

## Common Mistakes

- **Deriving "ought" from "is":** Freeze facts in O1 and values in O2 as separate records.
- **Withholding a supported recommendation for lack of execution authority:** Register the premises and give it as `deliberation_only`.
- **Dressing a recommendation as a decision:** Keep adoption status, imperative-free wording, and the authorization gap explicit.
- **Deleting no action:** Include exactly one `no_action` and price its continuing harms and responsibilities.
- **Treating status quo as no action:** Record the resources and enforcement required to maintain the status quo.
- **Aggregating away burden:** Preserve low-power, overlapping, bridge, cross-domain, and long-horizon positions.
- **Reading separately feasible options as jointly feasible:** Check shared capacity, budget, staff, and deadlines.
- **Hiding a worst-case rule:** State any selection rule explicitly instead of treating it as the only rational one.
- **Patching authority:** Require one atomic J tuple to cover subject, object, action, territory, full period, and authority source.
- **Calling formal participation consent:** Test safe refusal, exit, dissent effect, and anti-retaliation.
- **Using a pilot as an ethics exemption:** Apply the same protection, stop, appeal, rollback, data-use, and remedy duties.
- **Letting the module authorize:** Verify external records only and keep `authorization_effect: none`.

## Load Detailed Guidance

Read [references/choice-and-authorization.md](references/choice-and-authorization.md) when defining the two identities, N, PF, J, O1-O4, C12, options, the comparison card, joint feasibility, distribution, non-domination, selection states, correction endpoints, action ceilings, when not to act, T0-T4 tasks (the five intervention task types: T0 safety and trust carrier, T1 reversible minimum order, T2 carrying-and-return chain repair, T3 deep-time maintenance, T4 exit, transfer, and memory preservation), or the worked example. Read [references/intervention-levels.json](references/intervention-levels.json) for the T0-T4 machine contract covering entry conditions, success scope, exit continuity, and the hash-chained execution-state log. Hand any domain application to `ariadne-audit` for its matching Part 15 APP contract (APP-REL through APP-ULS, the nine domain application contracts) before external use.
