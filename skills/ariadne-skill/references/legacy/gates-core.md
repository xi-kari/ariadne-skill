# Legacy Gates Core

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/gates-core.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## Legacy Method Record serialization

<!-- method-record-example:start -->
```yaml
record_id: ariadne:hr-risk-score:root:v1
schema_version: '2.0'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: governance_review
object_contract:
  boundary: The named score, model version, input pipeline, proposed staffing and promotion use, and downstream records; exclude
    any claim about employee personality.
  state_variables:
  - source traceability
  - proxy validity
  - affected positions
  - appeal effectiveness
  - rollback capacity
  - use state
  relations_or_transitions:
  - score generation
  - manager use
  - record writeback
  - appeal
  - suspension
  - correction
  interfaces:
  - data source
  - model output
  - manager decision
  - protected appeal
  - external review
  - authoritative record
  time_window: Audit current use and all score-derived records since deployment.
  scale_profile:
    aggregation: individual scores within one employer
    impact: employment and household spillover
    jurisdiction: no verified authority for automated disposition
  identity_criterion: A model, input, use, population, or authority change requires a new audit.
  task_profile:
    target_query: Whether the risk score may keep its proposed staffing and promotion use
    horizon: Current use and all score-derived records since deployment
    environment: The named model version, input pipeline, and employer process
    allowed_operations: Audit and protective-pause description only
    error_tolerance: Gate-level pass, fail, or not-run findings
  status: candidate
evidence_cutoff:
  as_of: '2026-08-04T12:00:00+08:00'
  included_source_ids:
  - SRC-SCORE-REPORT
  - SRC-USE-PROPOSAL
  - SRC-APPEAL-PROCESS
  excluded_after_cutoff: true
scale_scope:
  source: model and proposed employer use
  target: high-impact employee disposition
  transform_kind: composite
  transform_status: failed
claim_ledger:
- claim_id: AUD-CLAIM-TRACE
  claim_type: E
  text: The available material does not support an auditable evidence chain for the risk score.
  status: supported
  support_ids:
  - SRC-SCORE-REPORT
  counterevidence_ids: []
  support_rule_ids: []
- claim_id: AUD-CLAIM-USE
  claim_type: O
  text: The audit records a protective pause while external evidence, protection, appeal, and rollback remain missing.
  status: candidate
  support_ids:
  - AUD-CLAIM-TRACE
  - SRC-APPEAL-PROCESS
  counterevidence_ids: []
  support_rule_ids: []
  depends_on:
  - AUD-CLAIM-TRACE
rule_registry: []
unknowns_and_counterevidence:
  unknowns:
  - 'unknown: training provenance'
  - 'unknown: error by group'
  - 'withheld_for_protection: protected-position testimony'
  - 'unknown: independent review'
  counterevidence:
  - A future externally verified study could support a narrower research-only use under a new record.
conflicts: []
output_ceiling: description_only
ceiling_transition:
  operation: root
  inputs: []
  basis: []
  result: description_only
module_runs:
- module: ariadne-audit
  status: completed
  input_records: []
  output_record:
    record_id: ariadne:hr-risk-score:root:v1
    record_version: 1
module_payloads:
- module: ariadne-audit
  payload:
    gate_register:
      transformations:
        IT1: {status: failed, finding: No frozen observable protocol; silence is used as a proxy.}
        IT2: {status: not_run, finding: Stopped after IT1.}
        IT3: {status: not_run, finding: Stopped after IT1.}
        IT4: {status: not_run, finding: Stopped after IT1.}
      main_gates:
        IG1: {status: failed, finding: 'Person, role, team, and model-version boundaries are mixed.'}
        IG2: {status: not_run, finding: Stopped after IG1.}
        IG3: {status: not_run, finding: Stopped after IG1.}
        IG4: {status: not_run, finding: Stopped after IG1.}
        IG5: {status: not_run, finding: Stopped after IG1.}
        IG6: {status: not_run, finding: Stopped after IG1.}
        IG7: {status: not_run, finding: Stopped after IG1.}
    strong_judgment:
      status: triggered
      reason: The score is intended for staffing and promotion decisions, an eligibility and allocation use.
      components:
        SJ1: {status: not_run, finding: Stopped after IG1.}
        SJ2: {status: not_run, finding: Stopped after IG1.}
        SJ3: {status: not_run, finding: Stopped after IG1.}
        SJ4: {status: not_run, finding: Stopped after IG1.}
        SJ5: {status: not_run, finding: Stopped after IG1.}
        SJ6: {status: not_run, finding: Stopped after IG1.}
        SJ7: {status: not_run, finding: Stopped after IG1.}
        SJ8: {status: not_run, finding: Stopped after IG1.}
    contestability:
      owner:
        contact: independent-review@example.invalid
        status: reachable
      deadline: '2026-08-18T12:00:00+08:00'
      original_record_retention: true
      downstream_correction_target: all score-derived staffing, promotion and personnel records
      rollback_recovery_target: the last verified pre-score employment and access state
      remedy: restore affected rights and resources, correct propagated records, and record residual harm
recommended_next_modules: []
authorization_effect: none
```
<!-- method-record-example:end -->

## Legacy transformation stop and ceiling

Run IT1-IT4 in order. On failure, mark every later transformation `not_run`, preserve the break, and lower the output ceiling. IT1 failure is a hard `description_only` ceiling: the record may name missing requirements and a protective pause, but it may not issue a `requirements_only` result.

## Legacy main-gate stop and ceiling

Treat IG1-IG7 as the only main flow, run in the order of the specific proposition and its dependencies (§13.3). Use `passed`, `failed`, `not_run`, or a reasoned `not_applicable` only where permitted. Never admit that an object or evidence failed a gate while letting later gates self-report a pass; a material change in object, evidence version, affected positions, or use reruns from the earliest affected gate. After the first `failed`, every later gate is exactly `not_run`. IG1 failure is a hard `description_only` ceiling with the same missing-requirement/protective-pause distinction.

## Legacy strong-judgment payload

After a failed gate, mark later gates `not_run`; do not self-report them as passed. **IG6 applicability rule:** a normal L1 or L2 record may mark IG6 `not_applicable` only with a concrete reason why the strong-judgment condition is not triggered, and this does not block IG7; IG6 `passed` binds all eight SJ items as individually `passed` in the same run. A "checked" string or empty reason never substitutes. In the Method Record this is the typed audit payload's `strong_judgment` register: `not_triggered` with a reason and all SJ items `not_applicable` when IG6 is `not_applicable`; `triggered` with every SJ item `passed` when IG6 is `passed`; and a triggered register with any failed SJ item never accompanies a passed IG6.

## Legacy L1-L3 record levels

Use levels only as responsibility levels:

- Let L1 produce description, questions, and next observations for low-impact reversible work.
- Let L2 produce a bounded comparison or mechanism candidate when no high-responsibility use follows.
- Let L3 produce only a strong-judgment candidate after the seven gates and SJ1-SJ8 pass.

A higher level is more record responsibility, not closeness to truth (§13.6). Downgrade whenever evidence coverage, object identity, reflexivity control, appeal, or anti-retaliation deteriorates. Urgency never deletes the object, protection, or stop conditions; when waiting is costly, offer only the narrowest, revocable, monitorable action requirement outside any authorization.

## Legacy audit gate-register encoding

In every execution record, keep `passed`, `failed`, and `not_run` distinct. Put the complete IT1-IT4 and IG1-IG7 status maps in the typed audit `gate_register`; semantic validation enforces the first-failure stop. Keep `unknown`, `not_applicable`, `not_observable`, and `withheld_for_protection` distinct. Use only `description_only`, `diagnostic_only`, or `requirements_only`; set `can_authorize=false`, `can_execute=false`, and `authorization_effect=none` in any companion register.

## Legacy choice wrapper and runtime-reference validation

When real action is represented by Ariadne's formal format, attach the complete 17-field choice record wrapper and bind it field by field to the structured `selected_action`, the C12 bridge, explicit runtime N premises, O1-O4, the unique atomic J authorization, stop, anonymous or proxy appeal, anti-retaliation monitoring, rollback, and the execution state log. Resolve every evidence, position, channel, and owner reference, including in diagnosis-only module records, to the runtime registry: a `GHOST`, `none`, `self`, or `self:*` summary never replaces an external record, and the appeal, independent-review, and rollback owners must not be the deciding subject. A separately verified equivalent external implementation retains its own format and authority; do not claim Ariadne schema validation for it.

## Legacy gate-register example

### Gate register

```yaml
audit_id: AUD-AI-HR-009
subject: AI-generated “attrition risk” report proposed for staffing and promotion decisions
subject_type: [practice, automated_output]
intended_use: high-impact qualification and resource allocation
IT1: failed  # “commitment” has no frozen observable protocol; silence is used as a proxy.
IT2: not_run
IT3: not_run
IT4: not_run
IG1: failed  # Person, role, team, and model-version boundaries are mixed.
IG2: not_run
IG3: not_run
IG4: not_run
IG5: not_run
IG6: not_run
IG7: not_run
AI_boundary: failed
malicious_compliance_signals: 5
publication_state: publication_blocked
use_state: suspended
missing_requirements_and_protective_pause:
  - Protective pause description: high-impact use remains suspended while the first gates are failed.
  - Missing requirement: a frozen observable protocol and traceable evidence chain.
  - Missing requirement: a protected independent appeal, correction, rollback, and external-review path.
  - Missing requirement: verified downstream correction and remedy before any new bounded proposal.
contestability:
  owner: {contact: independent-review@example.invalid, status: reachable}
  deadline: '2026-08-18T12:00:00+08:00'
  original_record_retention: true
  downstream_correction_target: all score-derived staffing, promotion, and personnel records
  rollback_recovery_target: last verified pre-score employment and access state
  remedy: restore affected rights and resources, correct propagated records, and record residual harm
authorization_effect: none
```

IT1 is the first failed transformation, so IT2-IT4 are `not_run`. IG1 is the first failed main gate, so IG2-IG7 are `not_run`; the unavailable evidence and protection facts remain findings outside those unrun gate results. Because the intended use is eligibility and allocation, the strong-judgment register is `triggered`, and its SJ items are `not_run` behind the IG1 failure. A polished later template cannot repair either break. Five malicious-compliance signals justify high-risk classification. The result may describe missing requirements and the protective pause, but the first-gate failures cap the Method Record at `description_only`; it does not issue requirements, personnel decisions, or authorization.
