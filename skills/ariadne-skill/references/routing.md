# Ariadne Routing

## Contents

1. Intake
2. Depth selection
3. Module map
4. Routing algorithm
5. Order, restarts, and stop-loss

Clustered execution, continuation, merge and stop rules, and the worked route live in [clustering.md](clustering.md).

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
| L0 | Low impact, reversible, single judgment-type output, and the user asked a question rather than for a method run | Direct bounded answer; no module run and no record | Bounded answer plus a one-line boundary declaration |
| L1 | Low impact, reversible, limited material | Framing plus one relevant module | Description, questions, next observation |
| L2 | Comparative diagnosis or derivation with reviewable impact | Framing, evidence, relevant modules, audit | Bounded diagnostic comparison |
| L3 | Public, automated, institutional, high-power, or hard-to-reverse use | Framing, evidence, all affected lanes, choice when applicable, full audit | Strong-judgment candidate or requirements-only handoff |

L0 is a routing outcome, not a record profile: answer directly, name the main gap or assumption in one line, and offer the full method only when the user asks for a record, the impact rises, or the answer would otherwise cross an output ceiling. When in doubt between L0 and L1, use L1.

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
10. For `synthesis_design`, run framing to freeze the design constraints and success criteria, evidence for any load-bearing empirical claim, and choice's comparison discipline over the candidate designs (options, trade-offs, explicit inaction analogue: keep the current design). The deliverable is a bounded proposal with its constraint record; construction and adoption return to the host workflow and any external decision process, and no ceiling permits Ariadne to build or execute the artifact.

A triggered module carries one of two strengths. A trigger is required when the module's responsibility carries the conclusion: leaving it out would leave a load-bearing object, claim, bridge, or affected position unaudited. A trigger is optional when the dimension is present but bounded and its variation cannot overturn the conclusion. At L1 and L2, an optional module may be discharged with a single-line declaration instead of a full module run: state the bounded finding and its explicit gap in the record (claim ledger or unknowns), mark the module run `not_run` with a reason naming this declaration, and keep or lower the ceiling. At L3 every triggered module is required.
## Order, restarts, and stop-loss

Run lanes in the dependency order `framing -> evidence -> [scale, mechanism, human] -> dynamics -> forecast -> choice -> audit`, skipping non-applicable lanes. If a module changes the object, evidence cutoff, scale, or purpose, restart at the earliest affected dependency. The restart budget is binding: the same dependency may be restarted at most twice in one run. When a third restart would be needed, do not restart; close the run at the current ceiling as a downgrade and record the oscillation cause in `unknowns_and_counterevidence.unknowns`.

Apply a stop-loss to the run as a whole: when the projected record work is clearly disproportionate to the question's stakes, or two consecutive module runs have left the bounded conclusion unchanged, close the run at the current ceiling, state the remaining gaps, and hand the next evidence step back instead of adding module runs.

Child-record mechanics, clustered execution, continuation events, merge and stop rules, and the worked route are specified in [clustering.md](clustering.md); read it when running parallel lanes, merging sibling records, or continuing an earlier run.
