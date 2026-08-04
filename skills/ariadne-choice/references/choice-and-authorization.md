# Choice and Authorization Contract

Use this reference to build a finite-choice card and determine its intervention ceiling. Keep the choice card beside the schema-compatible common Method Record; link them by stable IDs.

## 1. Keep Four Tasks Separate

Run this fixed chain:

```text
explanation -> diagnosis -> normative choice -> intervention
```

- Let explanation describe a bounded object and evidence.
- Let diagnosis compare problems, mechanisms, and falsifiers without granting power.
- Let normative choice identify the choosing subject, values, rights, options, distribution, and authority.
- Let intervention consume a valid external choice and authorization; never let it manufacture either.

Use four operational transformations:

| Stage | Freeze | Prevent |
|---|---|---|
| O1 | Descriptive claims, evidence, scale, uncertainty, and descriptive ceiling. | Editing facts after seeing options. |
| O2 | Explicit N premises, premise roles, conflicts, dissent, beneficiaries, and burden bearers. | Hiding value selection inside analysis. |
| O3 | Choosing subject, authority source, jurisdiction, duration, J axis, all options, and exactly one inaction option. | Treating influence or expertise as permission. |
| O4 | Bounded execution, monitoring, stop, appeal, review, rollback, remedy, expiry, and reauthorization. | Letting a finite choice become indefinite or irreversible. |

Do not skip a stage because the diagnosis is severe or forecast confidence is high.

For every action request, populate the typed Method Record choice payload before deciding whether choice work can proceed: `facts`, `values`, `options`, `jurisdiction`, `authorization`, `stop_conditions`, and `rollback_plan`. Include explicit inaction in `options`. Use the literal state `unknown` inside any unresolved field rather than omitting it. Missing fields lower the usable result; they do not excuse an incomplete boundary card.

## 2. Classify the Selection Process

| Type | Required subject and evidence | Hard boundary |
|---|---|---|
| `SEL-SYS` | A unit, environment, retention mechanism, time window, and stochastic baseline. | Describe differential retention only. Do not attribute intention, legitimacy, or authorization; do not include `external_action`. |
| `SEL-AGT` | An identifiable subject, genuine options, information, capacity, safe refusal, real exit, territory, and duration. | Bind only that subject within actual authority. One subject cannot choose for another by default. |
| `SEL-GOV` | A bounded public object plus agenda, representation, participation, minority protection, dissent, conflicts, execution accountability, and expiring authority. | Do not treat majority, volume, efficiency, legal form, or self-declared representation as sufficient authorization. |

Treat these boundaries as non-convertible. A system process does not become a chooser; a personal preference does not become public power; a governance process does not become a magnified personal decision.

## 3. Register N1-N5 at Runtime

List each used premise in `public_value_premises`. Give it a stable ID, role (`goal`, `constraint`, or `veto`), interpretation, beneficiaries, burden bearers, dissent, and review status.

| Premise | Runtime effect |
|---|---|
| N1: explanation does not authorize disposition | Block facts, forecasts, or diagnosis from directly producing action. N1 alone permits only inaction, more evidence, or continued review. |
| N2: protection must not degrade | Preserve or strengthen low-power protection when scale or intervention expands. Shrink action when infrastructure is weak. |
| N3: high-impact judgments must be correctable | Require effective appeal, independent review, stop, withdrawal, rollback, remedy, and version writeback. |
| N4: do not requisition love or care | Reject one-sided, unlimited, or non-exitable sacrifice framed as love, duty, care, loyalty, or system survival. |
| N5: survival and selection are not legitimacy | Keep stability, efficiency, coherence, and retention as consequence evidence, not moral authority. |

Keep conflicts under stable IDs. Do not erase dissent to close a conflict. Let unresolved material conflict pause, narrow, or retain inaction.

## 4. Build a Finite Option Set

Give each option a stable `option_id` and freeze:

- `option_kind` and action type;
- target object, territory, validity period, and identity criterion;
- reversibility, lock-in, resources, executor, and affected positions;
- forecast or consequence references;
- distribution of benefits, costs, risks, rights effects, and delayed burdens;
- information value and what the option can distinguish;
- authority, stop, appeal, rollback, and remedy requirements.

Include exactly one `no_action` option and point to it with `no_action_option_id`. Distinguish it from `maintain_status_quo`: maintaining a rule may require continuous resources and enforcement, while inaction allows the current system and clocks to evolve without the proposed intervention.

Include active action, delay, a reversible experiment, and exit or transfer when applicable. Create a new version or option ID when the action, object, territory, or duration changes.

For `no_action`, state the baseline time, expected path, current allocation, continuing harms, legal or role duties, observation owner, protective minimum, and conditions for reopening review. Never model inaction as zero consequence or zero responsibility.

## 5. Compare Consequences and Distribution

Use the same baseline for every option. Preserve separate dimensions when no justified common unit exists.

Audit consequences across `SP=<A,X,T,O,C,R,I,N,J>`:

- aggregation and distribution;
- physical or digital space;
- horizon, delay, and cycle;
- organizational level;
- causal level;
- observation resolution and compression loss;
- direct, indirect, second-order, cross-domain, and intergenerational impact;
- network topology;
- jurisdiction and authority.

Maintain an affected-position ledger. For each position, record benefit, cost, risk, right impact, timing, power level (`low`, `medium`, `high`, or `unknown`), exit ability, and burden transfer. Pay special attention to overlapping members, bridge actors, temporary-circle residues, silent positions, and people who cannot exit.

Instantiate two review principles rather than naming them:

- For `NSP-LEAST-HARM`, compare all feasible options including inaction and explain which avoidable harms make the selected option the narrowest.
- For `NSP-PROPORTIONALITY`, check suitability, necessity, benefit versus rights cost, intensity, scope, and duration.

Bind each principle version, evidence, reviewer, review time, and state. Separate the reviewer from the decision subject. Ensure the review, PF bindings, and authorization remain valid throughout the option period.

## 6. Audit Choice Quality and Governance

For `SEL-AGT` and `SEL-GOV`, record:

- direct and indirect coercion;
- default setter, switching cost, and meaning assigned to silence;
- comprehensible and symmetric information;
- decision capacity;
- safety of refusal;
- reality and cost of exit.

For `SEL-GOV`, additionally record:

- who can place or exclude an agenda item and when emergency procedure ends;
- each representative's source, scope, recallability, and unrepresented positions;
- safe, accessible participation with real effect;
- minority rights, local exclusion zones, and pause conditions;
- conflicts among deciders, executors, evaluators, and beneficiaries;
- accountable executors who can be reviewed, stopped, and replaced.

Give each dissent a stable ID, position, claim, status, response deadline, safe channel, and effect. Do not enter `authorized` while a material dissent remains `open`, `protected_and_pending`, or `unresolved_action_paused`.

## 7. Pass the C12 Bridge

Require all ten components:

1. `descriptive_or_explanatory_claim_ids`
2. `current_evidence_and_epistemic_constraints`
3. `explicit_normative_premise_ids`
4. `normative_conflict_record`
5. `protection_floor_status`
6. `authorization_and_jurisdiction_record`
7. `options_including_no_action`
8. `operational_procedure_records`
9. `action_ceiling`
10. `stop_review_rollback_and_remedy`

Treat C12 as a validity gate, not a value selector and not an authorization issuer. If any explicit N premise, PF requirement, J record, or O1-O4 record is absent, stop before real-world disposition. If only N1 is present, permit only inaction, additional evidence, or continued review.

## 8. Require Atomic J Coverage

Use one valid J tuple that simultaneously covers:

```text
(decision subject, target object, one action, territory, complete validity interval, authority source)
```

Do not combine partial tuples. Match the selection record, selected option, external `selected_action`, and J tuple field by field. Keep observation range, impact range, technical reach, legal validity, normative legitimacy, and authorization distinct.

Verify external records through stable IDs and independent evidence. The Ariadne record may link and check authorization but must keep `authorization_effect: none`.

## 9. Bind PF-1-PF-10

Create exactly ten unique protection bindings. For each, record applicability, reason, evidence, mechanism reference, owner, stop trigger, appeal, review, rollback, remedy, and expiry.

| PF | Required protection |
|---|---|
| PF-1 | List every affected and low-power position in options and distribution. |
| PF-2 | Provide anonymous, proxy, or low-exposure submission. |
| PF-3 | Make refusal and stopping effective; do not treat past consent as permanent. |
| PF-4 | Provide a timed appeal that can change the result. |
| PF-5 | Protect evidence, dissent, refusal, stopping, appeal, and exit from retaliation. |
| PF-6 | Permit evidence supplementation, dispute annotation, source correction, and downstream synchronization. |
| PF-7 | Trigger external independent review for high impact, conflicts, or failed internal correction. |
| PF-8 | Make withdrawal, rollback, repair, and authoritative writeback operational. |
| PF-9 | Provide real exit or transfer; where exit is impossible, provide proxy and substitute support. |
| PF-10 | Freeze the action ceiling, forbidden acts, stop triggers, responsible subject, and review time. |

Keep all ten active for human, sentient, mixed, or unknown impact. Allow a human-specific mechanism to be `not_applicable` only when both the object and downstream use are evidenced as purely nonhuman; PF-10 and real-world J, responsibility, stopping, review, rollback, and expiry remain mandatory. Reopen applicability when use changes.

## 10. Control State, Ceiling, and Correction

Use only these append-only states:

```text
draft -> under_review -> authorized -> paused -> stopped -> rolled_back -> closed
```

Record the prior state, time, responsible subject, and basis for every transition. Allow `draft` only to gather facts, positions, and options. Allow `under_review` only protective, reversible preservation. Let only `SEL-AGT` or `SEL-GOV` reach `authorized`, and cap it at the one externally selected and authorized option.

Pause when facts, protection, authority, procedure, or monitoring fail. Stop on a registered trigger, revoked authority, expiry, or prohibited action. Roll back only after restoring an acceptable state, correcting authoritative records, synchronizing downstream versions, remediating real harm, and tracking residual harm. Close only after open harms, appeals, remedies, and record duties are completed or formally transferred.

Set the intervention ceiling to the narrowest intersection of:

- descriptive evidence ceiling;
- explicit normative premises;
- protection floor;
- selected option;
- atomic J tuple;
- O4 trial or execution scope;
- reversibility;
- expiry.

Do not average a failed or unknown hard condition against strengths elsewhere.

## 11. Route Intervention Tasks Without Turning Them Into Stages

Treat T0-T4 as intervention task types, not maturity ranks or a mandatory sequence. Re-select the task when the object, scale, identity criterion, time, jurisdiction, affected positions, or action changes. Every non-draft execution record must preserve an append-only state log; terminal `rolled_back`, `completed`, `expired`, and `withdrawn` records never return to active.

| Type | Task | Allowed direction | Immediate stop or reroute |
|---|---|---|---|
| T0 | Establish a safe carrier for evidence, refusal, and help. | Anonymous, proxy, encrypted, staged, independently held evidence and support. | Identity exposure, retaliation, lost independence, or unsafe contact. |
| T1 | Restore reversible minimum order while diagnosis continues. | Safe separation, evidence preservation, essential support, short auto-expiring measures. | Growing harm, lost reversibility, unauthorized extension, or burden shifted downward. |
| T2 | Repair a verified carrying-return chain. | Restore feedback, support middle carriers, parallel replacement channels, bounded resource or responsibility repair. | Replacement fails, return does not reach burdened positions, bad news cannot change the plan, or authority fails. |
| T3 | Maintain slow variables, succession, redundancy, and recovery margin. | Long-horizon monitoring, multiple carriers, limited experimentation, review, and retirement preparation. | Basic protection loses resources, monitoring becomes control, or cost is exported to low-power or future positions. |
| T4 | Exit, transfer, or preserve evolutionary memory when repair is unsafe or unjustified. | Safe exit, staged transfer, substitute support, consent-bounded memory, duty and remedy settlement. | Retaliation, withdrawn consent, unsafe new carrier, excess data use, or evaded obligations. |

Do not let a T type bypass explanation, diagnosis, normative choice, C12, PF, J, or O1-O4. In an emergency, defer to valid external emergency authority for the minimum protective act and restore ordinary review promptly.

Before any domain application, freeze the D0 object, nine-axis scale, identity criterion, time window, sources, affected and low-power positions, then run the seven main gates. State what domain evidence exists, what is missing, and how each gap lowers confidence, pauses a claim, requires external verification or protocol, narrows authority, blocks intervention, or limits output to a reversible trial. A module name is not evidence and never grants access to people, data, property, services, employment, public resources, or command.

## Worked Example: Reorganization Under Attrition Risk

Treat this as an illustrative choice record, not a decision for a real workplace.

### Finite-choice card

```yaml
choice_id: CH-TEAM-022
selection_type: SEL-GOV
record_state: under_review
O1:
  descriptive_claims: [FC-F-TEAM-017]
  evidence_ceiling: diagnostic_only
  uncertainty: The forecast has ordinal support and a small sample; no calibrated probability exists.
O2:
  premises:
    - {id: N2, role: veto, interpretation: Do not lower protection for low-power team members.}
    - {id: N3, role: constraint, interpretation: Any high-impact result must be appealable and reversible.}
    - {id: N5, role: veto, interpretation: Organizational continuity does not justify avoidable rights harm.}
  unresolved_conflicts: [speed-versus-participation, workload-relief-versus-transfer-burden]
options:
  - {option_id: OPT-STATUS, option_kind: maintain_status_quo, summary: Continue current allocation with existing enforcement.}
  - {option_id: OPT-ACT, option_kind: active_action, summary: Immediate team-wide mandatory reorganization.}
  - {option_id: OPT-DELAY, option_kind: delay, summary: Delay structural change while gathering protected evidence.}
  - {option_id: OPT-TRIAL, option_kind: reversible_experiment, summary: Eight-week workload and independent-appeal pilot with automatic expiry.}
  - {option_id: OPT-EXIT, option_kind: exit_or_transfer, summary: Voluntary transfer with no retaliation or record penalty.}
  - {option_id: OPT-NONE, option_kind: no_action, summary: Do not change structure; continue protection, observation, and a fixed reopening review.}
no_action_option_id: OPT-NONE
provisional_comparison: OPT-TRIAL has the narrowest conditional harm only if PF, independent review, and atomic J coverage are verified; no option is selected yet.
C12_status: incomplete
missing_components: [verified protection floor, atomic J tuple, affected-position review, independent appeal owner]
O3: No externally verified selected action or matching J tuple exists.
O4: Limit output to conditions, protective preservation, and continued review.
authorization_effect: none
```

The card keeps the urgent reorganization option visible but does not treat urgency as authority. It distinguishes maintaining current rules from inaction, prices the harms of delay and non-action, and withholds selection until protected participation and a matching external authorization exist.

### Linked common Method Record

<!-- method-record-example:start -->
```yaml
record_id: ariadne:choice:CH-TEAM-022
schema_version: '1.1'
record_version: 1
lineage_kind: root
parent_record_id: null
parent_records: []
request_type: finite_choice
object_contract:
  boundary: Work-allocation and appeal arrangements for the frozen 24-person product team; exclude employment termination
    and compensation changes.
  state_variables:
  - workload distribution
  - appeal access
  - departure notices
  - transfer availability
  relations_or_transitions:
  - status quo
  - mandatory reorganization
  - delay
  - reversible trial
  - transfer
  - no action
  interfaces:
  - protected participation
  - independent appeal
  - management authority
  - execution monitor
  time_window: Review now; any trial may last no more than eight weeks.
  scale_profile:
    A: individual distribution within one team
    I: direct and household spillover
    J: unverified team-level authority
  identity_criterion: A change to team, action, territory, or duration requires a new choice version.
  status: candidate
evidence_cutoff:
  as_of: '2026-08-31T16:00:00+08:00'
  included_source_ids:
  - FC-F-TEAM-017
  - SRC-WORKLOAD
  - SRC-APPEAL
  excluded_after_cutoff: true
scale_scope:
  source: individual and team evidence
  target: bounded team choice
  transform_status: audited
claim_ledger:
- claim_id: CH-N2
  claim_type: N
  text: The choice must not lower protection for low-power positions.
  status: supported
  support_ids: []
  counterevidence_ids: []
  support_rule_ids:
  - RULE:N2
- claim_id: CH-O3
  claim_type: O
  text: No selected action has a verified atomic J authorization.
  status: unresolved
  support_ids: []
  counterevidence_ids: []
  support_rule_ids: []
rule_registry:
- rule_id: RULE:N2
  rule_type: normative
  text: Affected positions and the rights floor must be explicit before a choice handoff.
unknowns_and_counterevidence:
  unknowns:
  - The independent appeal owner and full affected-position distribution are not verified.
  counterevidence:
  - Immediate reorganization may create irreversible burden before protected participation occurs.
output_ceiling: requirements_only
ceiling_transition:
  operation: root
  inputs: []
  basis: []
  result: requirements_only
module_runs:
- module: ariadne-choice
  status: completed
  input_records: []
  output_record:
    record_id: ariadne:choice:CH-TEAM-022
    record_version: 1
module_payloads:
- module: ariadne-choice
  payload:
    facts:
    - Frozen workload, appeal and forecast materials listed in evidence_cutoff
    values:
    - Do not lower protection for low-power positions
    options:
    - status quo
    - delay
    - reversible trial
    - transfer
    - inaction
    jurisdiction: unknown
    authorization: unknown
    stop_conditions:
    - Protection floor, appeal access or rollback capacity fails
    rollback_plan: Restore the pre-trial work and record state; responsible owner remains external and unverified.
recommended_next_modules:
- ariadne-audit
authorization_effect: none
```
<!-- method-record-example:end -->

Do not rewrite this record as “Ariadne recommends the pilot.” State instead which external conditions must be satisfied before a qualified subject may select and authorize any option.
