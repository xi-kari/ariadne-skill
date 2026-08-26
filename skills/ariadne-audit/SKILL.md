---
name: ariadne-audit
description: "Gate high-impact use of completed Ariadne records: transformation and main gates, appeal, rollback, downgrade, pause, withdrawal, retirement, and the merge point for clustered runs. Use when conclusions face public, automated, institutional, or hard-to-reverse use, or when clustered module records must be merged and their conflicts preserved. For a multi-module pass, start with ariadne-skill. 适用于：结论公开或上线前的审查、能不能这么用、申诉与回滚、降级与退役、集群合并终审。"
license: MIT
metadata:
  record_schema: "1.3"
---

# Ariadne Audit

## Overview

Audit whether a bounded methodology record may retain its current judgment and use ceiling. Treat completed forms, fluent prose, automated scores, internal tests, and framework consistency as process artifacts, never as proof of reality, safety, consent, effectiveness, or authorization.

## Route the Audit

- Audit a high-impact, public, automated, organizational, institutional, or difficult-to-reverse judgment before use.
- Audit any Ariadne chain that crosses from observation to evidence, judgment, forecast, finite choice, intervention requirements, or governance change.
- Separate the audit subject into text or template, concept relations, actual practice, and governing community. Do not issue one undifferentiated “framework health” verdict.
- Treat a changed object, evidence version, affected population, use, scale, or authority scope as a trigger to rerun from the earliest affected gate.

## Run the Audit

1. Freeze the audit subject, version, owner, object contract, scale, evidence cutoff, intended use, affected and low-power positions, challenge path, and current output ceiling.
2. Run IT1-IT4 in order: structure to observable signal, signal to evidence strength, evidence to judgment level, and judgment to action requirements and ceiling. On failure, mark every later transformation `not_run`. An IT1 failure fixes `output_ceiling: description_only`; describe missing requirements or a protective pause without issuing requirements.
3. Run IG1-IG7 in order as the only main gate flow: object, evidence trace, affected positions, power and anti-retaliation, mediation and reflexivity, strong-judgment procedure, and action ceiling. Mark every gate after the first failure `not_run`. An IG1 failure fixes `output_ceiling: description_only`; do not let later paperwork repair or elevate it.
4. Expand with FG1-FG5 (the five expansion gates: object, evidence, scale, responsibility, and observation) and DS01-DS13 (the thirteen diagnostic steps: problem entry, object and boundary, signal layers, observation participation, dominant constraint, state and window, core structure, protected variables, carrying and repayment, hazard and boundary type, competing mechanisms, branch outlook, and output and writeback) when the object is complex, high-responsibility, or highly reflexive. Treat the expansion as evidence for the main gates, not a competing approval flow.
5. Require SJ1-SJ8 (the strong-judgment eight: reverse conditions, repair window, evidence requirements, appeal entry, anti-retaliation, evidence supplementation, external-review trigger, and rollback and writeback) for every L3 judgment (the highest of the L1-L3 responsibility levels) that can affect disposition, qualification, reputation, resources, rights, public memory, or automated or institutional use. If any component fails, fail IG6 and downgrade the output. SJ4-SJ8 re-verify the choice-level PF bindings; SJ1-SJ3 are the audit-specific increment, as the gates reference maps them.
6. Add DF1-DF9 (the nine dynamic gates: fact freeze, joint object, channels and clocks, mechanism propagation, path branching, forecast registration, normative choice, authorization and execution, and result writeback) when the record includes dynamic derivation, conditional forecast, finite choice, or intervention. Do not let the dynamic gates bypass the seven main gates.
7. Apply the AI boundary. Mark model-generated variables and paths as candidates; require source disclosure, missing-material disclosure, a responsible human, allowed and prohibited uses, uncertainty, review, appeal, and withdrawal. Block any promotion from `candidate` to `observed`, from `simulated` to real, or from forecast to authorization without external evidence.
8. Audit governance: preserve dissent, anti-retaliation, external review, authoritative version writeback, downgrade, suspension, publication blocking, withdrawal, replacement, rollback, remedy, and retirement. Require an externally verifiable approval for an applied governance change.
9. Return findings, failed or not-run gates, affected claims, the lowered output ceiling, and a typed contestability payload with a reachable owner, deadline, retained original record, downstream correction target, rollback recovery target, and remedy. Keep `authorization_effect` equal to `none`.

## Method Record

Create or extend a schema-valid Method Record with complete parent references, traced module inputs/output, and the ceiling transition. A merge lists every sibling parent in canonical order and uses the ceiling meet. Put reachable contestability, correction, rollback-recovery, retention, deadline, and remedy fields in the typed audit payload. Keep detailed gate registers beside the record under stable IDs.

Use `intervention_review` for a proposed or active real-world intervention and `governance_review` for claim, process, model, or framework governance. Preserve failed gates and terminal states in child versions. Keep `authorization_effect: none`.

## Mini Example

Input question: "May this automated attrition score keep its staffing use?" Skeleton only, not a complete record:

```yaml
request_type: governance_review
gate_register: {IT1: failed, IG1: failed}
output_ceiling: description_only
authorization_effect: none
```

## Stop and Downgrade

Stop at `description_only` when the object or evidence chain fails. Stop at `diagnostic_only` when you can describe a bounded defect but cannot specify a safely governed correction. Use `requirements_only` to state conditions for external correction, review, or withdrawal; do not issue execution commands.

Block public strong judgment when any required publication gate fails. Pause high-impact use when appeal, anti-retaliation, independent review, rollback, or authoritative writeback is not real. Withdraw or retire a claim, module, or framework when repeated or high-harm counterexamples, capture, calibration failure, identity change, or a safer simpler replacement defeats its current scope.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Quick Reference

| Audit surface | Required gate family | Failure response |
|---|---|---|
| Any judgment | IT1-IT4 plus IG1-IG7 | Mark later gates `not_run`; lower the ceiling. |
| Complex or reflexive diagnosis | FG1-FG5 plus DS01-DS13 | Feed findings back into IG gates; do not create a second pass state. |
| High-impact L3 judgment | SJ1-SJ8 | Fail IG6 and downgrade if any item is missing. |
| Dynamics, forecast, choice, or intervention | DF1-DF9 after IG gates | Keep scenario, forecast, choice, and execution boundaries separate. |
| Public strong claim | Nine publication gates | Block publication on any failure. |
| Applied governance change | External approval, dissent effects, and VERSION-LOG writeback | Keep proposed or suspended; never self-approve. |
| Replaced or retired subject | Terminal-state rule | Preserve history; require a new identity for any successor. |

## Common Mistakes

- **Treating gate completion as truth:** Report only that the process requirement passed; keep empirical support separate.
- **Running later gates after failure:** Mark them `not_run` and preserve the earliest failure's ceiling.
- **Using the thirteen steps as a second approval path:** Map them back to the seven main gates.
- **Calling a named reviewer independent:** Resolve canonical identity and material conflicts; require real access and veto power.
- **Offering an appeal that cannot change anything:** Treat it as no appeal and block high-impact use.
- **Calling a new version rollback:** Restore state, records, downstream effects, remedies, and residual-harm tracking.
- **Archiving counterexamples without consequences:** Bind them to text, process, ceiling, and lifecycle changes.
- **Letting AI verify itself:** Require external evidence and accountable human review.
- **Reviving a terminal state:** Create a new successor identity; never move `withdrawn`, `replaced`, or `retired` back to active.
- **Letting audit authorize:** Keep every audit record at `authorization_effect: none`.

## Load Detailed Guidance

Read [gates-core.md](references/gates-core.md) for the gate flow, AI boundary, publication, and intervention contracts (sections 1-9 plus the worked example with its schema-checked record). Read [governance-lifecycle.md](references/governance-lifecycle.md) for consensus and version authority, registries, challenge protection, capture detection, appeal and rollback testing, and retirement (sections 10-16). For any relationship, family, organization, platform, institution, public-opinion, space, emergency, or ultra-large application, also read the direct [Part 15 application contracts](references/application-contracts.json) and enforce the matching domain stop and handoff; read its `common_rule` first, then only the matched contract entry (search by ID, for example `"id": "APP-ORG"`) instead of the whole file.
