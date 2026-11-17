---
name: ariadne-choice
description: "Compare action, delay, probing, exit, and no action on one baseline, then give an analytic recommendation for deliberation under explicit norms, with costs, objections, and change conditions, keeping rights, jurisdiction, and authorization separate and issuing no permissions. Use when a decision, pilot, exit, or act-or-not question needs a bounded option comparison; run ariadne-forecast first if it hinges on an unregistered future claim. For a multi-module pass, start with ariadne-skill. 适用于：该不该做、方案比较与推荐、不行动也是选项。"
license: MIT
metadata:
  record_schema: "2.1"
---

# Ariadne Choice

## Overview

Compare a finite option set and, when explicit normative premises and evidence allow, say which option the analysis currently recommends and why. Keep two identities apart: an analytic recommendation for deliberation, which the module may form, and an authorized choice, which only a qualified subject with valid authority can make. Never turn facts, forecasts, efficiency, survival, or model confidence into an instruction, and never send a supported analysis back to a question list merely because no one has authority to execute.

Apply v2's three layers separately: argument principles govern recommendations; substantive authority and protection govern real adoption; Ariadne's field names and exact binding counts govern its own record format. A different procedure may provide equivalent safeguards after independent verification. A format failure is not itself proof that an external act lacks authority. These methods remain derived candidates, not item-by-item author confirmation.

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
5. Compare every option against the same baseline across consequences, distribution, nine-axis scale, affected and low-power positions, worst acceptable outcome, information value, reversibility, lock-in, resources, joint feasibility with other options, and residual harm. Identify all direct, known or pointed-out low-power, and domain-required positions; trace further effects proportionately under §14.4.1, with a recorded and challengeable search boundary. Distinguish unknowns that could change protection or comparison from those monitored with reopening conditions. Preserve protection without promising every outcome will be no worse; a disputed protection/outcome classification is treated as protection first.
6. Check coercion, defaults, information, capacity, safe refusal, and real exit at entry and now. For `SEL-GOV`, distinguish responding to proposals from changing agenda rules or challenging final authority. Keep dissent, unanswered material reasons, and failed protection separate; reasoned disagreement is not automatic veto and a response receipt is not correction. Ask separately about resources, standing, and representation.
7. Form the analytic recommendation when premises allow: the recommended option, explicit N premises, reasons, costs, objections, change conditions, and `adoption_status: deliberation_only`. If all options leave loss, still give a finite judgment: record the decision rule and its proposer/adopter, unmet legitimate claims, loss bearers, continuing duties and owners, and reassessment time. Compare disputed decision rules conditionally. Challenge asserted scarcity, omitted options and authority gaps before saying there is no alternative. Withhold only for the specific missing premise that blocks the recommendation; with only N1 or no positive premise, limit it to no action, more evidence or continued deliberation.
8. For adoption represented in Ariadne, freeze O3 and C12 (the ten-component validity bridge from description to normative choice): selected option, N premises, all ten bridge components, least-harm and proportionality reviews, protection, atomic J tuple, jurisdiction, validity period, and external verification. Independently verify substantively equivalent external formats rather than declaring them invalid by name. Then freeze O4: cap execution at the narrowest intersection of evidence, values, rights, selected option, J authority, reversibility, trial scope, and expiry, with prohibited acts, monitoring, stopping, appeal, anti-retaliation, independent review, rollback, remedy, and reauthorization.
9. Assign the record state and append every transition. Never erase `paused`, `stopped`, `rolled_back`, or expired history. Keep `authorization_effect` equal to `none`, including when the module verifies an external authorization record.

## Record mode

For low-impact, reversible work, a concise task, evidence, finding and boundary statement can be sufficient. The machine-record instructions below apply when a structured record is selected, requested or needed for handoff; they do not require twenty fields before an ordinary answer. Preserve known facts and existing authorization, marking only actual gaps unknown. Formal forecast registration and safeguards for consequential use remain required by their own contracts; brevity does not waive them.

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

Block the dependent adoption when substantive norms, protection, action-covering authority, safe dissent or correction capacity are absent; incomplete Ariadne fields block its formal endorsement. Preserve independent lawful duties and any supported deliberative recommendation. When all feasible options leave harm, no action is assessed with the same care as action. If nonwaivable protections cannot all be preserved even after independent review, do not endorse an `authorized` option: preserve what can be protected and refer to the responsible subject's own lawful or emergency authority, with narrow scope, expiry and later review.

Do not choose values for the subject, infer consent from silence or non-exit, sign authorization, execute an option, or guarantee success. Lead with the current analytic recommendation and its scope, then the full comparison: reasons for accepting and rejecting each option, costs and their distribution, objections, change conditions, and what real adoption still needs. Never phrase a recommendation in imperative mood or as an executable decision.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Quick Reference

| Condition | Maximum response |
|---|---|
| `SEL-SYS` differential retention | Description only; no external-action option or authorization. |
| Facts ready, values unresolved | Show conflicts and consequences; retain no action; recommendation withheld for the named missing premise. |
| Values stated, options and costs registered | Analytic recommendation for deliberation, with the actual external authorization state reported separately; the recommendation itself grants none. |
| Values stated, PF or J incomplete | Recommendation plus requirements, protection, and referral; no execution. |
| External authorization exists but mismatches one action field | Treat the option as unauthorized. |
| Evidence weak and action reversible with clear authority | Consider only a bounded information-gathering trial. |
| Every feasible option leaves irreversible loss | Limited recommendation under explicit rules; retain losses, claims, duties and reassessment. |
| Failed substantive protection or authority | Block dependent adoption; keep supported analysis and existing duties. |

## Common Mistakes

- **Deriving "ought" from "is":** Freeze facts in O1 and values in O2 as separate records.
- **Withholding a supported recommendation for lack of execution authority:** Register the premises and give it as `deliberation_only`.
- **Dressing a recommendation as a decision:** Keep adoption status, imperative-free wording, and the authorization gap explicit.
- **Deleting no action:** Include exactly one `no_action` and price its continuing harms and responsibilities.
- **Treating status quo as no action:** Record the resources and enforcement required to maintain the status quo.
- **Aggregating away burden:** Preserve low-power, overlapping, bridge, cross-domain, and long-horizon positions.
- **Reading separately feasible options as jointly feasible:** Check shared capacity, budget, staff, and deadlines.
- **Hiding a worst-case rule:** State any selection rule explicitly instead of treating it as the only rational one.
- **Calling protection a guarantee of lossless outcomes:** Preserve protections and separately justify each outcome loss; an adopted choice never extinguishes unmet claims.
- **Stopping at tragic conflict:** Give the supported conditional recommendation, retain continuing duties, and reopen constraints that may be challengeable.
- **Patching authority:** Require one atomic J tuple to cover subject, object, action, territory, full period, and authority source.
- **Calling formal participation consent:** Test safe refusal, exit, dissent effect, and anti-retaliation.
- **Using a pilot as an ethics exemption:** Apply the same protection, stop, appeal, rollback, data-use, and remedy duties.
- **Letting the module authorize:** Verify external records only and keep `authorization_effect: none`.

## Load Detailed Guidance

Read [references/choice-and-authorization.md](references/choice-and-authorization.md) when defining the two identities, N, PF, J, O1-O4, C12, options, the comparison card, joint feasibility, distribution, non-domination, selection states, correction endpoints, action ceilings, when not to act, T0-T4 tasks (the five intervention task types: T0 safety and trust carrier, T1 reversible minimum order, T2 carrying-and-return chain repair, T3 deep-time maintenance, T4 exit, transfer, and memory preservation), or the worked example. Read [references/intervention-levels.json](references/intervention-levels.json) for the T0-T4 machine contract covering entry conditions, success scope, exit continuity, and the hash-chained execution-state log. Hand any domain application to `ariadne-audit` for its matching Part 15 APP contract (APP-REL through APP-ULS, the nine domain application contracts) before external use.
