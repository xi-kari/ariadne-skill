---
name: ariadne-choice
description: Use when comparing action, delay, experiment, exit, or inaction while separating facts, values, authorization, limits, stopping, rollback, and remedy.
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

1. Freeze O1: the descriptive claims, evidence status, uncertainty, scale, forecast references, and descriptive output ceiling. Do not repair them after seeing attractive options.
2. Classify the process as `SEL-SYS`, `SEL-AGT`, or `SEL-GOV`. Reject language that gives a system intent, extends one person's choice over others, or turns governance into a large personal preference.
3. Freeze O2: the runtime N1-N5 premises, each premise's role as goal, constraint, or veto, all value conflicts, dissent, beneficiaries, and burden bearers. Keep the PF-1-PF-10 rights floor separate from tradable preferences.
4. Create stable option IDs. Include exactly one `no_action` option and distinguish it from maintaining the status quo. Include active action, delay, reversible experiment, and exit or transfer when applicable.
5. Compare every option against the same baseline across consequences, distribution, nine-axis scale, affected and low-power positions, information value, reversibility, lock-in, resources, and residual harm. Keep incomparable dimensions and conflicts visible.
6. Check coercion, defaults, information, capacity, safe refusal, and real exit. For `SEL-GOV`, also check agenda control, representation, participation, minority protection, dissent, conflicts of interest, and execution accountability.
7. Freeze O3 and C12: bind the selected option, explicit N premises, all ten bridge components, least-harm and proportionality reviews, protection floor, atomic J tuple, jurisdiction, validity period, and external verification references.
8. Freeze O4: cap execution at the narrowest intersection of evidence, values, rights, selected option, J authority, reversibility, trial scope, and expiry. Register prohibited actions, monitors, stop authority, appeal, anti-retaliation, independent review, rollback, remedy, and reauthorization.
9. Assign the record state and append every transition. Never erase `paused`, `stopped`, `rolled_back`, or expired history. Keep `authorization_effect` equal to `none`, including when the module verifies an external authorization record.

## Produce a Standalone Method Record

Create the common record even when no upstream module ran. Put the detailed choice card beside it and link stable IDs; do not add undeclared keys to the Method Record.

```yaml
record_id: ariadne:choice:<stable-id>
schema_version: "1.0"
record_version: 1
parent_record_id: null
request_type: finite_choice
object_contract:
  boundary: <who and what the decision covers and excludes>
  state_variables: [<decision-relevant state>]
  relations_or_transitions: [<option consequences>]
  interfaces: [<participation, authority, execution, appeal channel>]
  time_window: <review and validity window>
  scale_profile: {A: <aggregation>, I: <affected scope>, J: <jurisdiction>}
  identity_criterion: <what change requires a new choice record>
  status: candidate
evidence_cutoff:
  as_of: <RFC-3339 timestamp>
  included_source_ids: [<source-id>]
  excluded_after_cutoff: true
scale_scope: {source: <evidence scope>, target: <choice scope>, transform_status: audited}
claim_ledger: []
unknowns_and_counterevidence: {unknowns: [<unknown>], counterevidence: [<counterevidence>]}
output_ceiling: requirements_only
module_runs: [{module: ariadne-choice, status: completed, record_version: 1}]
recommended_next_modules: [ariadne-audit]
authorization_effect: none
```

Use `description_only` when only a system-selection description is justified. Use `diagnostic_only` when you can compare consequences but cannot complete normative requirements. Use `requirements_only` to state the conditions an external decision and authorization process must satisfy; never turn that ceiling into an executable command.

## Stop and Handoff

Stop at inaction, evidence collection, protective preservation, continued review, or external referral whenever a positive N premise, a C12 component, a PF binding, atomic J coverage, O1-O4, safe dissent, or rollback capacity is absent. In an emergency, identify only the minimum protective action allowed by an external emergency rule, then require prompt review, appeal, and rollback.

Do not choose values for the subject, infer consent from silence or non-exit, sign authorization, execute an option, or guarantee success. Return plain-language comparison first, followed by the compact Method Record and, for high-impact cases, the detailed choice card.

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
- **Patching authority:** Require one atomic J tuple to cover subject, object, action, territory, and full period.
- **Calling formal participation consent:** Test safe refusal, exit, dissent effect, and anti-retaliation.
- **Using a pilot as an ethics exemption:** Apply the same protection, stop, appeal, rollback, data-use, and remedy duties.
- **Letting the module authorize:** Verify external records only and keep `authorization_effect: none`.

## Load Detailed Guidance

Read [choice-and-authorization.md](references/choice-and-authorization.md) when defining N, PF, J, O1-O4, C12, option and distribution cards, selection states, intervention ceilings, T0-T4 tasks, application gates, or the worked example.
