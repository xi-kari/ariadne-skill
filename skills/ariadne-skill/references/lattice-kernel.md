# Lattice Kernel

## Contents

1. Purpose
2. Twelve invariants
3. Output classes
4. Claim and dependency classes
5. Evidence and bridge discipline
6. Missing states
7. Output ceilings
8. AI and self-governance boundary
9. Quick reference

## Purpose

The Lattice Kernel is the common discipline behind every Ariadne module. It makes reasoning traceable without treating form completion as truth. Its core movement is:

> fix the request -> declare the candidate object -> freeze evidence -> audit scale and mechanism -> derive paths -> register forecasts -> compare choices -> govern use and writeback

Each arrow is a gate, not an automatic implication.

## Twelve invariants

### 1. Classify output before answering

Keep explanation, diagnosis, dynamic derivation, conditional forecast, finite choice, intervention review, and governance review distinct. A request may need several, but each keeps its own evidence and stopping rule.

Never silently transform:

- explanation into prediction;
- prediction into recommendation;
- recommendation into command;
- command into authorized action.

### 2. Admit objects in two stages

First declare a candidate object:

`S*=<B,X,R,I,T,SP,K>`

- `B`: boundary;
- `X`: state variables;
- `R`: relations or transition constraints;
- `I`: interfaces;
- `T`: time window;
- `SP`: scale profile;
- `K`: identity criterion.

Completeness makes the candidate discussable. It does not establish empirical independence or validity. Strong object claims require a frozen comparison against an appropriate simple or zero model.

### 3. Separate claim responsibilities

| Class | Responsibility | Cannot establish by itself |
|---|---|---|
| D - definition | Fix a term's local meaning | A real-world fact |
| G - empirical hypothesis | State a testable relationship | Support without a frozen instance |
| E - epistemic constraint | Limit observation and inference | A causal mechanism |
| H - human-domain clause | Specialize for structured human worlds | A universal human essence |
| N - normative commitment | Declare what is protected or preferred | An empirical fact |
| O - operating procedure | Freeze, review, authorize, stop, correct | The truth or legitimacy of its input |

Split a sentence that mixes classes.

### 4. Separate dependency types

| Relation | Meaning | Enters the inference graph |
|---|---|---|
| `inferential_requires` | Hard premise without which the conclusion does not follow | Yes |
| `protocol_requires` | Evidence, causal, source, analogy, or review gate | No |
| `specializes` | Narrows a general rule to a domain or subtype | No |
| `applies_to` | Names the target of a norm or procedure | No |

Passing a protocol gate permits publication at a stated ceiling; it does not become an extra empirical cause.

### 5. Preserve the evidence chain

Keep these as separate records:

`source -> material -> observation -> evidence -> counterevidence -> judgment -> external authorization`

A source can be genuine while its interpretation is weak. Evidence can support association without causality. A causal conclusion can remain normatively silent. A value judgment can exist without jurisdiction or authorization.

### 6. Use contracts for bridges

Before a strong bridge, register what could break it:

- **Causal:** cause, effect, order, channel, object, scale, window, target variable, counterfactual, competitors, falsifiers.
- **Analogy:** source domain, target domain, shared structure, differences, non-transferable elements, mapping, discriminating tests.
- **Source:** provenance, case type, time/region, support range, external boundary, counterexamples, raw/interpretive/framework links.
- **Scale/translation:** source and target, preserved/changed/lost items, operator, error, applicability, return path.

If the bridge is incomplete, retain a candidate relation and lower the ceiling.

### 7. Register scale loss

Track aggregation, space, time, organization, causal layer, observation resolution, impact scope, network scope, and jurisdiction separately. Compare each axis as equal, expands, contracts, incomparable, unknown, or not applicable.

Expansion on any axis never expands jurisdiction automatically. A shared word across scales does not prove the object stayed the same.

### 8. Prefer the simplest adequate model

Add a circle, variable, mechanism, or layer only when it addresses a named residual through a plausible channel and provides recoverable benefit over a simple baseline. Complexity is a cost to justify, not evidence of depth.

### 9. Make forecasts fail visibly

Freeze target, deadline, object, scale, input cutoff, simple baseline, expression, calibration metric, early signals, reverse signals, pause/retirement rules, and result writeback before the outcome. A retrospective explanation is not a forecast hit.

### 10. Cross the normative bridge explicitly

Real-world choice needs, at minimum:

`bounded descriptive conclusion + explicit normative premises + current evidence + affected positions + jurisdiction + external authorization + action ceiling + stopping/withdrawal conditions`

Missing components produce description, requirements, non-action, or reversible information-gathering proposals. They do not produce permission.

### 11. Keep AI in the candidate layer

AI may organize materials, find missing fields, propose competing paths, check contract consistency, and calculate registered measures. It may not verify an external event, infer personality from sparse behavior, disclose for a person, choose values, manufacture consent, set jurisdiction, convert simulation into fact, or issue authorization.

### 12. Govern and retire the framework

Internal consistency, validation, reports, and stress tests do not prove real-world safety or effectiveness. Preserve external evidence, affected-party challenge, failures, downgrades, alternative methods, version writeback, and orderly retirement.

## Output classes

| Output | Question | Required stopping point |
|---|---|---|
| Explanation | Why did this happen? | Mechanisms and competitors; no future or action claim by default. |
| Diagnosis | Where is the bounded structural problem? | Evidence-graded location and residuals. |
| Dynamic derivation | What paths follow under stated events and conditions? | Branches, thresholds, signals, and unknowns. |
| Conditional forecast | Which dated path is currently better supported? | Pre-registered comparison and calibration. |
| Finite choice | How do action, delay, experiment, exit, and inaction compare? | Explicit norms and external decision handoff. |
| Intervention review | Is a proposed action within its authority and safety ceiling? | Requirements, prohibition, stopping, rollback. |
| Governance review | Should a claim, process, model, or framework be challenged or retired? | Contestability, writeback, downgrade, replacement. |

Request-type adjudication: auditing how well existing evidence supports an already stated claim is explanation work with a ceiling of at most `diagnostic_only`, even when the claim is public. Governance review is reserved for the withdrawal, downgrade, or retirement decision about an already published claim, process, or model. Contrast pair: "Do these two papers support this causal conclusion?" routes to explanation and stops at a bounded diagnostic comparison; "Should we retract our published causal conclusion after this counterevidence?" routes to governance review and stops at contestability, downgrade, or retirement conditions.

## Missing states

Use one of these labels instead of fluent completion:

- `unknown`: knowable in principle, unsupported now;
- `not_applicable`: no legitimate counterpart under this contract, with reason;
- `not_observable`: blocked by measurement, time window, or channel;
- `withheld_for_protection`: known material is not disclosed for a stated protection, minimal scope, duration, and trusted review route.

Silence is not absence. Non-observation is not nonexistence. Protected withholding is not permission to raise confidence.

## Output ceilings

The ceilings form the total order `description_only < diagnostic_only < requirements_only`. Each higher ceiling includes everything permitted below it.

| Ceiling | May produce | May not produce |
|---|---|---|
| `description_only` | Facts/materials as bounded, questions, missing fields, candidate objects | Mechanism ranking, forecast, action requirement |
| `diagnostic_only` | Description plus candidate or comparative mechanisms, bounded diagnosis, conditional paths, and eligible forecast evaluation | Normative/process requirements, recommendation, instruction, authorization |
| `requirements_only` | Description and diagnosis plus conditions an external choice/authorization process would need | Ariadne selecting an action, permission, execution, or self-reported authorization |

Every root record starts at `description_only`; a higher ceiling is never an initial value. For an ordinary child, take the minimum of the inherited ceiling and the module's locally supported ceiling. A module run never raises the ceiling. A `lower` records its downgrade reason in the ceiling transition. A child may raise only after newly admitting external evidence or recording fulfillment of a declared protocol; register the basis ID in the Method Record, and when the lineage was previously lowered, state how the basis resolves that recorded reason. A merge takes the minimum ranked parent ceiling. More modules, votes, simulations, or confident prose never raise it.

## AI and self-governance boundary

Every run keeps `authorization_effect: none`. External choice, jurisdiction, consent, or authorization records can be linked and checked; Ariadne does not create them.

Apply the same discipline to Ariadne:

- keep source and interpretation separate;
- compare against simpler methods;
- record failures and harms;
- accept affected-party challenge;
- narrow claims after counterexamples;
- pause high-harm use;
- replace or retire modules that do not add value.

## Quick reference

Before a strong conclusion, ask:

1. What exact output is requested?
2. What is the candidate object and identity criterion?
3. What evidence existed by the cutoff?
4. What scale or translation bridge is used?
5. What competing mechanism could explain the same observations?
6. What simple baseline must the added complexity beat?
7. What would reverse or falsify the judgment?
8. Who is affected, who has jurisdiction, and where is external authorization?
9. How can the result be challenged, stopped, corrected, rolled back, and retired?
