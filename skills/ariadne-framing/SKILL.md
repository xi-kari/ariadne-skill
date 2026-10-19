---
name: ariadne-framing
description: "Freeze what an analysis is about: the difference to explain, the task (query, horizon, environment, allowed operations, error), and the candidate object's boundary, variables, relations, interfaces, window, scale profile, and identity criterion, plus request type and domain entry. Use when the object, task, or request type is ambiguous, or a named group, system, or phase is treated as real without being established. For a multi-module pass, start with ariadne-skill. 适用于：问题定界、对象与口径先说清楚、任务类型分类。"
license: MIT
metadata:
  record_schema: "2.0"
---

# Ariadne Framing

## Overview

Define what is being asked, for which task, and which candidate object is being discussed before judging it. Start from the concrete difference that puzzles the requester rather than from a favorite vocabulary. A complete frame is a testable declaration; it never proves that the object, mechanism, or grouping exists, and it never makes a representation sufficient for tasks it was not declared for.

## Procedure

1. **Consume or start the Method Record.** Preserve every supplied fact, unknown, counterexample, record ID, version, and ceiling. If reframing changes scope or task, create a child version and keep the lineage; never overwrite the prior record.
2. **Name the difference in plain words.** Restate the requester's question, the requester, and the intended and foreseeable use without framework terms. Say which difference needs explaining, deciding, or protecting. Do not require the person to learn Ariadne's vocabulary before their experience is acknowledged.
3. **Classify the request.** Select one `request_type`: `explanation`, `diagnosis`, `dynamic_derivation`, `conditional_forecast`, `finite_choice`, `intervention_review`, `governance_review`, or `synthesis_design`. Split a mixed request into ordered outputs; each later output adds its own conditions. For a build request, classify only its judgment core as `synthesis_design`; with no judgment core, declare it out of scope.
4. **Declare the task profile.** Freeze the target query, horizon, environment, allowed operations, and error tolerance. Sufficiency is always relative to this task: a representation may answer a static query yet fail to advance the dynamics or to evaluate an allowed intervention.
5. **Freeze the candidate object.** Declare boundary, registered state variables, relations or transitions, interfaces, time window, scale profile, and identity criterion. Check the nine axes A/X/T/O/C/R/I/N/J owned by `ariadne-scale` and register the informative ones (at least one). Keep `status` `candidate` or `incomplete` until evidence work supports more. Records may already support bounded facts about specific people, institutions, events, or relations; those facts do not wait for a grouping test, and they do not prove a grouping gain, a unified subject, or a common will.
6. **Run the pre-concept gate before structural vocabulary.** Ask in plain words: can it be observed together, does it have a minimal boundary, do actions inside it repeatedly affect one another, is there a shared problem or constraint, who bears the cost of keeping it going, and can results or bad news change what happens next? If not, stop at phenomenon description, risk registration, or narrative analysis.
7. **Open the domain entry.** When the question sits in a recognizable field, read the matching entry in the domain atlas and keep that field's own terms, measurements, and professional boundaries. Let an adequate domain method answer; add only the checks it lacks.
8. **Mark visibility and risk.** Encode every missing field as `unknown`, `not_applicable`, `not_observable`, or `withheld_for_protection`, with a reason. Escalate the next-module recommendation when evidence is thin, power is asymmetric, consequences are hard to reverse, the setting is high pressure, or the answer may be used for handling, eligibility, rights, allocation, reputation, or automated decisions.
9. **Apply the strong-judgment screen.** Surface unanswered questions about object validity, evidence, causal bridge, scale, alternatives, rights, authorization, stopping, remedy, and appeal. Record which judgment connections the task will need (same cases, same representation, same resources, same clock) so later modules know where chains may break. Do not answer any of these by completing the frame.
10. **Return a bounded frame.** Give a short plain-language object and task statement, the unresolved boundary choices, and the updated Method Record. Set a standalone run to `description_only`; preserve or lower an incoming ceiling, never raise it. Always set `authorization_effect: none`.

Read [references/object-contract.md](references/object-contract.md) when a field is disputed, a structure term needs precise use, a high-impact request needs escalation, or a complete standalone example is useful. Read [references/domain-atlas.md](references/domain-atlas.md) when the question belongs to one of the thirty-two mapped domains and its typical separations or traps matter.

## Method Record Contract

Produce every schema field, including `lineage_kind`, complete `parent_records`, `object_contract.task_profile`, `scale_scope.transform_kind`, `ceiling_transition`, traceable module input/output records, and `module_payloads`. Keep `parent_record_id` only as the sole-parent alias for a linear child.

When no upstream record exists, create the minimum valid record and identify user-provided material as material, not empirical evidence. The full schema ships with the suite router at `ariadne-skill/references/method-record.schema.json`; the complete standalone example in this module's [object contract](references/object-contract.md) is schema-checked in CI. When an upstream record exists, add an `ariadne-framing` module run and preserve lineage.

## Quick Reference

| Signal | Do | Stop at |
|---|---|---|
| "What exactly are we analyzing?" | Name the difference, freeze the task profile and the seven object fields | Candidate object and task |
| Explanation mixed with action | Split request types and order them | Separate records or ordered outputs |
| Group or system asserted by name | Run the pre-concept gate; keep it candidate | No object-validity claim |
| Same object, new query or operation | Re-declare the task profile | No reuse of earlier sufficiency |
| Scale, circle, or vocabulary changes | Record source and target; route to `ariadne-scale` | No transfer claim |
| Recognizable professional field | Open the domain atlas entry | Domain method first, framework checks second |
| High-impact or irreversible use | Expose protection and strong-judgment gaps | No action or authorization |

## Mini Example

Skeleton only, not a complete record; the schema-valid template ships with the suite router as `l1-record-template.md`.

```yaml
# Input: "Is the new-hire onboarding process broken?"
request_type: diagnosis
object_contract:
  boundary: the 2026 onboarding workflow in one named company
  task_profile:
    target_query: which onboarding step delays first productive work
  status: candidate
output_ceiling: description_only
```

## Stopping Conditions

Stop at an exploratory question list when boundary, task, time window, scale, or identity cannot be stated. Stop at a candidate frame when object validity, causality, or source support has not been audited. When a single actor and one stable circle answer the question and neighboring circles add no information, keep the frame small and do not open a joint multi-circle model. Route evidence questions to `ariadne-evidence`, scale and representation changes to `ariadne-scale`, mechanisms to `ariadne-mechanism`, human-domain risks to `ariadne-human`, action comparisons to `ariadne-choice`, and high-impact gates to `ariadne-audit`.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Common Mistakes

- Treating a complete object contract as proof of a real, stable system.
- Leaving the task implicit, then reusing a representation for a query, horizon, or operation it was never checked against.
- Writing every imaginable variable instead of registering only task-relevant variables.
- Using the same word across scales or traditions as evidence that the object stayed identical.
- Letting a narrow named contract (a learning mechanism, a meaning anchor, an open-bearing route) decide whether ordinary learning, meaning, or care exists.
- Marking unavailable or protected information as absent.
- Letting broad observation, organizational rank, or model confidence imply jurisdiction.
- Ending a framing run with a diagnosis, recommendation, or real-world permission.
