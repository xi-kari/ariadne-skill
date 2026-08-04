---
name: ariadne-framing
description: Use when a problem has an unclear object, boundary, time window, scale, identity criterion, task type, or requested output level.
---

# Ariadne Framing

## Overview

Define what is being asked and what candidate object is being discussed before judging it. Treat a complete frame as a testable declaration, not as proof that the object, mechanism, or grouping exists.

## Procedure

1. **Consume or start the Method Record.** Preserve every supplied fact, unknown, counterexample, record ID, version, and ceiling. If reframing changes scope, create a child version and retain `parent_record_id`; never overwrite the prior record.
2. **Classify the request.** Select exactly one `request_type`: `explanation`, `diagnosis`, `dynamic_derivation`, `conditional_forecast`, `finite_choice`, `intervention_review`, or `governance_review`. Split a mixed request into separate records or state which output comes first.
3. **Freeze the candidate object.** Declare boundary, registered state variables, relations or transitions, interfaces, time window, nine-axis scale profile, and identity criterion. Keep `status` as `candidate` or `incomplete` until evidence work supports more.
4. **Separate the task layers.** Distinguish description, structural diagnosis, future derivation, forecast, choice, and real-world intervention. Do not let an explanation silently become a prediction or a requested action.
5. **Mark visibility and risk.** Encode every missing field as `unknown`, `not_applicable`, `not_observable`, or `withheld_for_protection`, with a reason. Escalate the next-module recommendation when evidence is thin, power is asymmetric, consequences are hard to reverse, or the setting is high pressure.
6. **Apply the strong-judgment screen.** Surface unanswered questions about object validity, evidence, causal bridge, scale, alternatives, rights, authorization, stopping, remedy, and appeal. Do not answer them by completing the frame.
7. **Return a bounded frame.** Give a short plain-language object statement, the unresolved boundary choices, and the updated Method Record. Set a standalone run to `description_only`; preserve or lower an incoming ceiling, never raise it. Always set `authorization_effect: none`.

Read [references/object-contract.md](references/object-contract.md) when a field is disputed, a structure term needs precise use, a high-impact request needs escalation, or a complete standalone example is useful.

## Method Record Contract

Produce every schema field, including `lineage_kind`, complete `parent_records`, `ceiling_transition`, traceable module input/output records, and `module_payloads`. Keep `parent_record_id` only as the sole-parent alias for a linear child.

When no upstream record exists, create the minimum valid record and identify user-provided material as material, not empirical evidence. When an upstream record exists, add an `ariadne-framing` module run and preserve lineage.

## Quick Reference

| Signal | Do | Stop at |
|---|---|---|
| “What exactly are we analyzing?” | Freeze the seven object fields | Candidate object |
| Explanation mixed with action | Split request types | Separate records or ordered outputs |
| Group or system asserted by name | Keep it candidate; request an evidence audit | No object-validity claim |
| Scale or vocabulary changes | Record source and target; route to `ariadne-scale` | No transfer claim |
| High-impact or irreversible use | Expose protection and strong-judgment gaps | No action or authorization |

## Stopping Conditions

Stop at an exploratory question list when boundary, time window, scale, or identity cannot be stated. Stop at a candidate frame when object validity, causality, or source support has not been audited. Route evidence questions to `ariadne-evidence`, scale changes to `ariadne-scale`, mechanisms to `ariadne-mechanism`, human-domain risks to `ariadne-human`, action comparisons to `ariadne-choice`, and high-impact gates to `ariadne-audit`.

## Common Mistakes

- Treating a complete object contract as proof of a real, stable system.
- Writing every imaginable variable instead of registering only task-relevant variables.
- Using the same word across scales as evidence that the object stayed identical.
- Marking unavailable or protected information as absent.
- Letting broad observation, organizational rank, or model confidence imply jurisdiction.
- Ending a framing run with a diagnosis, recommendation, or real-world permission.
