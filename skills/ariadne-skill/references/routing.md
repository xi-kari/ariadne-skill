# Ariadne Routing

## Contents

1. Intake
2. Depth selection
3. Module map
4. Routing algorithm
5. Sequential, clustered, and continuous execution
6. Merge and stop rules
7. Worked route

## Intake

Start from the request in ordinary language. Record:

- requester's question and intended use;
- affected object or population;
- evidence cutoff;
- time horizon;
- requested output;
- whether the output can affect rights, resources, reputation, safety, public memory, or automated decisions.

Ask a question only when the missing answer would select a materially different object, value premise, jurisdiction, or irreversible action. Otherwise mark the field and continue at a lower ceiling.

## Depth selection

| Level | Conditions | Minimum route | Maximum result |
|---|---|---|---|
| L1 | Low impact, reversible, limited material | Framing plus one relevant module | Description, questions, next observation |
| L2 | Comparative diagnosis or derivation with reviewable impact | Framing, evidence, relevant modules, audit | Bounded diagnostic comparison |
| L3 | Public, automated, institutional, high-power, or hard-to-reverse use | Framing, evidence, all affected lanes, choice when applicable, full audit | Strong-judgment candidate or requirements-only handoff |

A higher level means more record responsibility, not greater truth.

## Module map

| Observable need | Module | Consumes | Produces |
|---|---|---|---|
| Object or task ambiguity | `ariadne-framing` | Raw request or parent record | Object contract and request type |
| Claim or evidence ambiguity | `ariadne-evidence` | Object contract and materials | Evidence/claim ledger and support ceiling |
| Cross-scale or cross-domain move | `ariadne-scale` | Object and evidence records | Scale/translation record |
| Why/how mechanism question | `ariadne-mechanism` | Bounded observations | Competing mechanism records |
| Human roles, privacy, power, meaning | `ariadne-human` | Human-domain object | Affected positions and human boundaries |
| Event propagation or paths | `ariadne-dynamics` | Frozen state and mechanisms | Branch graph and signals |
| Dated future claim | `ariadne-forecast` | Eligible paths and baseline | Forecast registry record |
| Real-world options | `ariadne-choice` | Bounded conclusions and explicit norms | Option comparison and external requirements |
| High-impact use or merge | `ariadne-audit` | Complete child records | Gate results, conflicts, ceiling meet, writeback |

## Routing algorithm

1. Run framing for every new object or changed purpose.
2. Run evidence before any comparative mechanism, forecast, or choice.
3. Add scale when an inference changes aggregation, space, time, organization, causal level, observation resolution, impact, network, jurisdiction, domain, representation, or vocabulary, and only when that change can alter the conclusion's validity. Non-triggering counterexamples: restating one team's quarterly delay in hours instead of days changes representation but not what the claim asserts, so scale is not triggered; citing last quarter's report as background while every claim stays inside the current quarter touches time without any cross-time inference, so scale is not triggered.
4. Add human when a claim concerns people, roles, institutions, meaning, power, privacy, responsibility, consent, appeal, or refusal, and only when that human dimension can alter the conclusion's validity or affect a real position. Non-triggering counterexamples: tuning a database index where people appear only as request volume makes no claim about any person or role, so human is not triggered; quoting an engineer's published conference talk as a technical source uses a person as provenance without making a claim about people, so human is not triggered.
5. Add mechanism for explanation, diagnosis, every causal route, and every analogy route. Require at least two competitors, a simple baseline, channel observations, discriminating predictions, reverse or falsifying conditions, and a residual comparison rule.
6. Add dynamics only when events, transitions, clocks, thresholds, feedback, or branch paths matter.
7. Add forecast only when the request needs an evaluable future judgment. Without registration, keep scenarios.
8. Add choice for every action request, and pick its depth explicitly. An action request that meets every L1 condition (low impact, reversible, limited material) may emit a compressed boundary card: one declaration line recording that facts, values, options, jurisdiction, authorization, stop conditions, and rollback are unknown and that no option is selected. The compressed card stays within the L1 maximum result because it selects nothing. Every other action request runs at L2 or higher and emits the complete typed boundary card with facts, values, options including inaction, jurisdiction, authorization, stop conditions, and rollback plan; write `unknown` rather than omitting a field. Neither form generates external authorization.
9. Add audit for L2 merging and every L3 use. Audit is mandatory for public, automated, institutional, eligibility, allocation, safety, or difficult-to-reverse output.

A triggered module carries one of two strengths. A trigger is required when the module's responsibility carries the conclusion: leaving it out would leave a load-bearing object, claim, bridge, or affected position unaudited. A trigger is optional when the dimension is present but bounded and its variation cannot overturn the conclusion. At L1 and L2, an optional module may be discharged with a single-line declaration instead of a full module run: state the bounded finding and its explicit gap in the record (claim ledger or unknowns), mark the module run `not_run` with a reason naming this declaration, and keep or lower the ceiling. At L3 every triggered module is required.

## Sequential execution

Use this dependency order, skipping only non-applicable lanes:

`framing -> evidence -> [scale, mechanism, human] -> dynamics -> forecast -> choice -> audit`

Each module creates a linear child with one parent reference. Its module run copies that reference into `input_records` and names the child in `output_record`. If a module changes the object, evidence cutoff, scale, or purpose, restart at the earliest affected dependency. The restart has a budget: the same dependency may be restarted at most twice in one run. When a third restart would be needed, do not restart; close the run at the current ceiling as a downgrade and record the oscillation cause in `unknowns_and_counterevidence.unknowns`.

## Clustered execution

After framing and evidence are frozen, scale, mechanism, and human lanes may run independently. Parallel admission is machine-checkable: two lanes may run in parallel only when their parent references carry the same `{record_id, record_version}` and the parent's `evidence_cutoff` fields (`as_of`, `included_source_ids`, `excluded_after_cutoff`) are equal item by item. Give every worker:

- the same parent record;
- the same raw materials and cutoff;
- only its assigned responsibility;
- no preferred answer;
- the required Method Record fields.

Each sibling creates a child of the same frozen parent. Derive its record ID deterministically with the normative syntax `ariadne:<case>:<module>:v<N>` defined in the Method Record reference. Do not let one sibling consume another sibling's output.

Do not parallelize:

- forecast before eligible dynamic paths exist;
- choice before bounded conclusions and explicit normative premises exist;
- audit as a peer whose vote can be averaged with the analyzed modules.

Audit merges after the lanes complete. Create `lineage_kind: merge`, set `parent_record_id: null`, list every sibling ID and version in `parent_records` sorted by ID then version, copy that list into the audit run's `input_records`, and name the merge record in `output_record`. Never select one sibling as a surrogate parent.

## Continuous execution

Treat a follow-up as one of four events:

| Event | Record action |
|---|---|
| New evidence within same object and purpose | Create child version from evidence onward. |
| Changed object, boundary, scale, identity, or purpose | Restart framing with a new lineage or explicit fork. |
| Outcome arrives for a forecast | Preserve forecast; append result and calibration writeback. |
| External choice or authorization arrives | Link its external identifier; keep Ariadne's authorization effect as none. |

Never rewrite the parent record to make a later result appear expected.

## Merge rules

1. Union compatible source IDs, unknowns, counterevidence, and module runs while retaining each run's exact input and output record references.
2. Preserve incompatible object contracts, scale mappings, causal explanations, and value premises as named entries in the record's `conflicts` field, each with a `conflict_id`, a `kind` (`object_contract`, `scale_mapping`, `causal_explanation`, or `value_premise`), the involved `record_refs`, and a description; never average them.
3. Prefer no conclusion over a false synthesis.
4. Apply the ceiling `meet`: `description_only < diagnostic_only < requirements_only`, so the result is the minimum ranked parent ceiling. A merge never raises.
5. Mark a missing required lane `not_run`, not `passed`.
6. Keep external authorization references outside empirical claim support.

## Stop rules

| Broken dependency | Stop at |
|---|---|
| Candidate object incomplete | Questions or `description_only` |
| Evidence chain cannot be traced | Material organization or candidate claim |
| Scale bridge fails | Source-scale statement only |
| Mechanisms not distinguishable | Parallel candidates |
| Dynamic inputs not frozen | Qualitative scenario outline |
| Forecast not pre-registered | Scenario, not forecast |
| Norms or affected positions missing | Options and requirements, not recommendation |
| Jurisdiction or authorization missing | External handoff, no execution |
| Appeal/rollback missing in L3 | Pause or downgrade |

## Worked route

Request: “Use three employee interviews to prove the whole company is culturally broken and replace managers.”

- Framing declares the interviews' team, time window, and intended organization-wide use; the company-wide object remains incomplete.
- Evidence separates interview sources, statements, observations, interpretations, and counterevidence.
- Scale audits the move from three individuals to team and company claims.
- Human identifies power, retaliation risk, privacy, missing positions, and role/responsibility distinctions.
- Mechanism compares manager behavior, workload, incentives, selection effects, and reporting-channel trust.
- Choice can compare investigation, reversible pilot, delay, protection, or inaction only after explicit values and jurisdiction.
- Audit blocks organization-wide personnel action while preserving a requirements-only path for independent review.
