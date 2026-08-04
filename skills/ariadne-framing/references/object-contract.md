# Object and Output Contract

Use this reference to construct or challenge a frame. Keep the user-facing result plain unless the full contract is needed.

## Two-Stage Admission

1. Declare a candidate object as `S*=<B,X,R,I,T,SP,K>`.
2. Send any claim that the grouping is empirically useful to an evidence-bearing G1 instance.

Completing stage 1 makes the object discussable and testable. It does not establish object validity. Do not place a zero model in the candidate object itself; freeze a complexity-matched `N0` only inside the concrete evidence instance that tests a specific claim.

## Request and Output Classification

| Method Record `request_type` | Requested work | Framing boundary |
|---|---|---|
| `explanation` | Explain an observed or reported phenomenon | Do not predict or prescribe |
| `diagnosis` | Locate constraints, instability, or capacity gaps | Report only a requested diagnostic target |
| `dynamic_derivation` | Expand conditional event paths | Preserve branches, residuals, and unknowns |
| `conditional_forecast` | Make a target-and-deadline future claim | Require a later frozen forecast registry |
| `finite_choice` | Compare action, delay, experiment, exit, and inaction | Require explicit values and authorization later |
| `intervention_review` | Review a proposed real-world intervention | Require protection, stopping, rollback, and remedy later |
| `governance_review` | Review rules, public claims, or methodology governance | Require challenge, appeal, downgrade, and retirement later |

If one request contains multiple rows, split it or declare an explicit order. An explanation does not inherit forecast status, and a forecast does not inherit authorization.

## Candidate Object Fields

| Field | Freeze | Do not infer |
|---|---|---|
| `boundary` / B | Included and excluded states, relations, locations, actors, or cases | Closure, naturalness, or moral membership |
| `state_variables` / X | Task-relevant registered variables and their observation positions | The object's complete state |
| `relations_or_transitions` / R | Endpoints, direction, timing, and applicability | Causality from adjacency or correlation |
| `interfaces` / I | Inputs, outputs, filters, delays, conversions, or blocks | Control, consent, or responsibility |
| `time_window` / T | Observation, explanation, forecast, or intervention window | Persistence outside the window |
| `scale_profile` / SP | A, X, T, O, C, R, I, N, and J positions | Transfer between axes or scales |
| `identity_criterion` / K | Changes compatible with retaining the same object | Value, health, maturity, or a duty to persist |
| `status` | `candidate` or `incomplete` during framing | `supported` without an eligible evidence instance |

For groups and circles, also state members, roles, channels, entry and exit conditions, overlap basis, and the residual that motivates the grouping. Keep a group as an environmental condition or variable candidate when it adds no specified gain over a simpler frame.

## State and Structure Vocabulary

Use these terms only with their declared tests:

- **Change:** a detectable difference in a registered variable; do not imply cause, direction, or persistence.
- **Operation:** state transitions while B, R, I, SP, and K remain valid.
- **Persistence:** K continues within T; do not imply health, legitimacy, or desirability.
- **Evolution:** a contract field changes beyond a declared fluctuation window; do not imply progress, selection, or path dependence.
- **Dissolution:** the prior K no longer holds; classify termination or conversion separately.
- **Repair:** a new state satisfies a predeclared target K* or function F*; route its value and authorization to normative and operating procedures.
- **Effective feedback:** a prior state or output returns through a traceable channel and detectably changes a later state, probability, timing, or constraint relative to no return or blockage. Receipt or logging alone is not feedback.
- **Scale transformation:** declare `M(SP0 -> SP1)` with preserved, changed, lost, uncertain, and non-transferable content, operator, error, and applicability range. Route the audit to `ariadne-scale`.
- **Representation or wording translation:** preserve the source, converter or rule, target task, lineage, loss, target-side review, validity period, and withdrawal path. Do not confuse it with scale change, propagation, compression, or analogy.

## Minimum Structural Closure

| Primitive | Framing question | Boundary |
|---|---|---|
| U01 candidate object | Can all D0 fields be stated? | Does not prove G1 |
| U02 boundary and interface | What is inside, outside, filtered, delayed, or blocked? | Boundary is not closure or control |
| U03 state and observable | What is registered, from which measurement position, with what error? | Observable is not the whole state |
| U04 component, carrier, substrate | What composes, carries, or enables the process? | Carrier is not a responsible subject |
| U05 relation and constraint | What repeatably narrows feasible states or transitions? | Relation is not causality or legitimacy |
| U06 flow, channel, transmission | What moves, where, at what rate and loss? | A named channel is not an evidenced effect |
| U07 feedback and update | What returns and which later field changes? | Feedback is not learning or repair |
| U08 condition and environment | Which outside variable acts through which interface? | Environment is not a total cause |
| U09 load, capacity, recovery margin | What comparable demand and capacity share units, window, and location? | Overload is not cumulative damage or duty |
| U10 trace, memory, path | What persists and re-enters later transitions? | A trace is not path dependence |
| U11 phase, transition, dissolution | Which criteria distinguish regimes under the same K? | A phase is not a maturity rank |

Mark a primitive `not_applicable` with a reason when the current object has no lawful counterpart. Otherwise keep missing content visible.

## Missing and Visibility States

Use one of four explicit prefixes in string-valued Method Record fields and unknown lists:

- `unknown:` knowable in principle, currently unsupported.
- `not_applicable:` no lawful counterpart in the current contract, with reason.
- `not_observable:` unavailable through the current channel or window.
- `withheld_for_protection:` available but not disclosed; state basis, minimum scope, duration, and trusted review path.

Never translate any of these into “does not exist.” Lower the output to a candidate frame, question list, or description when a critical field cannot be responsibly resolved.

## Strong-Judgment and Protection Screen

Before handing off a high-impact frame, ask:

1. Is the candidate object established rather than merely named?
2. What evidence supports the claim?
3. Is there a causal bridge?
4. Has scale been changed or collapsed?
5. Which competing explanations remain?
6. Whose rights or protected interests may be affected?
7. What is the actual authorization and jurisdiction?
8. Can the proposed process be stopped?
9. Can harms be remedied or rolled back?
10. Can affected parties challenge or appeal?

Record gaps; do not fill them. Preserve subject status, dissent, exit where possible, minimum harm, traceable responsibility, and genuine rollback as the protection floor. Broad observation, influence, organizational rank, or technical ability never expands J authorization.

## Method Record Mapping

- Put the seven frozen object fields and status in `object_contract`.
- Put the material cutoff in `evidence_cutoff`; do not call included material empirical evidence merely because it is listed.
- Summarize current source and target positions in `scale_scope`; use `not_needed` when no transformation is claimed.
- Put definitions and framed claims in `claim_ledger` with D/G/E/H/N/O types.
- Put unresolved fields, protection gaps, and strong-judgment gaps in `unknowns_and_counterevidence`.
- Add `ariadne-framing` to `module_runs` and route only applicable next modules.
- Use `output_ceiling: description_only` for standalone framing and `authorization_effect: none` in every run.

## Strong Example

Request: “Incident reports rose after a school changed its reporting app. Should the district install cameras everywhere?”

Frame the reporting question before the intervention question. Do not equate reported incidents with incident occurrence, and do not treat the proposed camera system as already inside the observed object.

<!-- method-record-example:start -->
```yaml
record_id: ariadne:school-reporting-frame-001
schema_version: '1.1'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: intervention_review
object_contract:
  boundary: The incident-reporting workflow in three named district schools after the app change; excludes unreported events
    and the proposed camera system.
  state_variables:
  - reported incident count by school and week
  - reporting participation by role
  - report classification and duplicate rate
  - response time after a report
  relations_or_transitions:
  - app access and prompts may change report submission; causal status unknown
  - submitted reports enter review, classification, and response stages
  interfaces:
  - student, staff, and parent submission channels
  - school review and escalation channel
  time_window: 2025-08-01 through 2026-07-31, with the app-change date retained
  scale_profile:
    A: individual reports to school-level summaries
    X: three named schools
    T: weekly observations across one school year
    O: school workflows within one district
    C: candidate reporting-channel effect only
    R: report-level records plus weekly summaries
    I: students, staff, parents, and school response units
    N: submission and escalation network
    J: 'unknown: camera authorization and district jurisdiction not audited'
  identity_criterion: The same reporting workflow while submission, classification, and escalation rules remain materially
    unchanged.
  status: candidate
evidence_cutoff:
  as_of: '2026-08-04T00:00:00+08:00'
  included_source_ids:
  - source:user-request
  excluded_after_cutoff: true
scale_scope:
  source: report-level events
  target: school and district summaries
  transform_status: candidate
claim_ledger:
- claim_id: D1
  claim_type: D
  text: The current object is the reporting workflow, not all incidents and not the proposed camera intervention.
  status: candidate
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
rule_registry: []
unknowns_and_counterevidence:
  unknowns:
  - 'unknown: whether underlying incident occurrence changed'
  - 'unknown: reporting participation and duplicate-classification changes'
  - 'unknown: camera necessity, privacy effects, alternatives, jurisdiction, stopping, remedy, and appeal'
  counterevidence: []
output_ceiling: description_only
ceiling_transition:
  operation: root
  inputs: []
  basis: []
  result: description_only
module_runs:
- module: ariadne-framing
  status: completed
  input_records: []
  output_record:
    record_id: ariadne:school-reporting-frame-001
    record_version: 1
module_payloads: []
recommended_next_modules:
- ariadne-evidence
- ariadne-scale
- ariadne-human
- ariadne-choice
- ariadne-audit
authorization_effect: none
```
<!-- method-record-example:end -->

This frame permits an evidence audit of reporting and incident measures. It does not diagnose the cause of the increase or authorize cameras.
