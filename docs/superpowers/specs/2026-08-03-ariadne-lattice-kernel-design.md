# Ariadne and Lattice Kernel Design Specification

## Product identity

- External name: **Ariadne**
- GitHub repository: **`xi-kari/ariadne-skill`**
- Primary installable skill: **`ariadne-skill`**
- Methodology kernel: **Lattice Kernel**
- Canonical namespace: **`ariadne-*`**

## Purpose

Ariadne converts complex work and thought into bounded, inspectable methodology records. It guides agents and people to define the object before judging it, separate materials from evidence, preserve scale and translation losses, compare mechanisms, derive conditional paths, register forecasts before outcomes, and stop normative or action claims at their actual authorization boundary.

The Lattice Kernel is a methodology kernel. It does not claim that a world ontology is complete, turn form completion into empirical support, diagnose personalities, choose values for people, or issue real-world authorization.

## Source boundary

The primary source is *跨尺度多圈层结构推演框架 v8.2* (July 2026), SHA-256:

`608A4E4099B18C96C18ED3C92A2AB5CDACBD737DACA4214C77DEBDD795DA3A20`

The “数学结构概述” conversation is a secondary design index. Its useful synthesis is retained: classify outputs first; declare objects before claims; separate evidence, scale, prediction, choice, and authorization; preserve unknowns, counterexamples, appeal, rollback, and retirement. Where the conversation and source differ, the DOCX governs.

## Architecture

Ariadne uses one router and nine peer modules. Every module must work alone, accept or produce the common method record, and participate in sequential or clustered execution.

| Skill | Responsibility |
|---|---|
| `ariadne-skill` | Route the request, select depth and modules, coordinate sequential or clustered work, and assemble the final result. |
| `ariadne-framing` | Classify the requested output and freeze the candidate object, boundary, variables, interfaces, time window, scale profile, and identity criterion. |
| `ariadne-evidence` | Separate claim types and dependency types; audit sources, materials, observations, evidence, counterevidence, causality, analogy, and support ceilings. |
| `ariadne-scale` | Audit nine-axis scale changes, circle relations, aggregation, nesting, propagation, abstraction, cross-domain transfer, and translation loss. |
| `ariadne-mechanism` | Scan structural primitives, compare channels and conditional mechanisms, retain simple baselines, competing explanations, falsifiers, and residuals. |
| `ariadne-human` | Apply human-domain clauses for actors, roles, circles, power, reflexivity, privacy, responsibility, and meaning without personality or clinical diagnosis. |
| `ariadne-dynamics` | Freeze events and joint states; model clocks, thresholds, feedback, cascades, branches, scenarios, recursive simulation, and stopping conditions. |
| `ariadne-forecast` | Register conditional forecasts with targets, deadlines, input cutoffs, simple baselines, calibration, signals, failure semantics, and result writeback. |
| `ariadne-choice` | Compare action, delay, experiment, exit, and inaction while separating facts, values, protection, jurisdiction, authorization, stopping, rollback, and remedy. |
| `ariadne-audit` | Apply transformation gates, strong-judgment requirements, AI boundaries, challenge, appeal, downgrade, withdrawal, retirement, and framework governance. |

## Lattice Kernel invariants

Every module enforces the same compact invariants:

1. Classify the output before producing it: explanation, diagnosis, dynamic derivation, conditional forecast, finite choice, intervention review, or governance review.
2. Treat every object as a candidate until its boundary, state, relation, interface, time window, scale, and identity criterion are explicit.
3. Keep definitions, empirical hypotheses, epistemic constraints, human-domain clauses, normative commitments, and operating procedures distinct.
4. Keep inferential requirements, protocol requirements, specializations, and applicability relations distinct.
5. Preserve the chain from source to material, observation, evidence, counterevidence, judgment, and external authorization without skipping levels.
6. Register scale or representation changes with preserved, changed, lost, uncertain, and non-transferable content.
7. Prefer the simplest adequate baseline; retain added circles or variables only when they explain a specified residual through a plausible channel.
8. Keep derivation, forecast, recommendation, and authorization separate.
9. Mark missing fields as unknown, not applicable, not observable, or withheld for protection; never silently fill them.
10. Preserve counterexamples, reverse conditions, stopping, appeal, rollback, writeback, downgrade, and retirement.
11. Treat AI output as candidate organization and reasoning, not real-world verification, consent, value selection, diagnosis, or authorization.
12. Subject the methodology itself to external evidence, failure records, replacement, and retirement.

## Common method record

Every standalone or clustered run uses a human-readable record with a machine-checkable core:

```text
record_id
schema_version
record_version
parent_record_id
request_type
object_contract
evidence_cutoff
scale_scope
claim_ledger
unknowns_and_counterevidence
output_ceiling
module_runs
recommended_next_modules
authorization_effect
```

`authorization_effect` is always `none`. Valid output ceilings are `description_only`, `diagnostic_only`, and `requirements_only`. A downstream module may lower an upstream ceiling but may not raise it without a new evidence-bearing record version.

## Execution modes

- **Standalone:** one module creates the minimum record required for its responsibility and returns a bounded result.
- **Sequential:** `framing -> evidence -> scale/mechanism/human -> dynamics -> forecast -> choice -> audit` as required by the request.
- **Clustered:** after object and evidence cutoffs are frozen, scale, mechanism, and human-domain work may run in parallel. Audit merges their records and reports conflicts instead of averaging them away.
- **Continuous:** later modules consume the prior record. New evidence or changed scope creates a new version and preserves the parent.
- **Full-suite:** the router runs every applicable module; applicability is not the same as blindly running every human-domain or action module.

If the runtime lacks multi-agent support, clustered execution degrades to the same modules in sequence without changing contracts or output ceilings.

## Trigger and installation policy

All skills set `policy.allow_implicit_invocation: true` for global distribution. Descriptions remain specific enough to trigger only on their methodological responsibility. The primary `ariadne-skill` triggers on full-method requests and complex tasks spanning multiple modules.

On the current workstation, development and evaluation use explicit `$ariadne-*` invocation or direct repository paths. The implementation must not write to a global skill directory.

## Progressive disclosure

- Keep each `SKILL.md` focused on routing, core procedure, input/output contract, and failure boundaries.
- Put detailed contracts and field definitions in one-level `references/` files.
- Do not duplicate the complete Lattice Kernel across all modules. Repeat only the minimum invariants needed for standalone safety.
- Default user output is plain-language reasoning followed by a compact record only when useful. High-impact judgment, forecast, choice, and audit tasks expose the fuller record.

## Source coverage

| v8.2 source area | Ariadne owner |
|---|---|
| Parts 1-3: outputs, boundaries, structure grammar | `ariadne-framing` |
| Parts 2 and 4: claims, evidence, root instances, conditional conclusions | `ariadne-evidence` |
| Parts 3, 4, and 6: primitives and conditional mechanisms | `ariadne-mechanism` |
| Part 5: scale, circles, and translation | `ariadne-scale` |
| Parts 7-10 and Appendix A: human domain, actors, states, circles | `ariadne-human` |
| Part 11: event-driven derivation | `ariadne-dynamics` |
| Part 12: conditional forecast and calibration | `ariadne-forecast` |
| Parts 14-15: normative choice and intervention boundary | `ariadne-choice` |
| Parts 13 and 16: tools, gates, AI boundary, and governance | `ariadne-audit` |
| Appendices B-D: terminology and shared kernel mapping | `ariadne-skill` plus repository coverage tests |

## Repository shape

```text
ariadne-skill/
├── AGENTS.md
├── README.md
├── docs/
├── evals/
├── schemas/
├── scripts/
├── tests/
└── skills/
    ├── ariadne-skill/
    ├── ariadne-framing/
    ├── ariadne-evidence/
    ├── ariadne-scale/
    ├── ariadne-mechanism/
    ├── ariadne-human/
    ├── ariadne-dynamics/
    ├── ariadne-forecast/
    ├── ariadne-choice/
    └── ariadne-audit/
```

Each installable directory contains `SKILL.md`, `agents/openai.yaml`, and only the references it actually needs.

## Acceptance criteria

- All ten skills are complete, independently invocable, and namespace-isolated.
- The full group covers every v8.2 source area through a checked coverage matrix.
- Standalone, sequential, clustered, continuous, and full-suite scenarios preserve facts, unknowns, record lineage, and output ceilings.
- Clustered and sequential execution may differ in presentation but not in frozen facts or authorization effect.
- No skill depends on another repository or a global local installation.
- No skill presents methodology completion as empirical truth or real-world authority.
- Integrated review starts only after the complete-content gate passes for the entire group.
