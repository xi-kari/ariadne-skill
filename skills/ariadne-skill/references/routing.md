# Ariadne Routing

## Contents

1. Intake
2. Depth selection
3. Module map
4. Routing algorithm
5. Retrieval order for mechanisms and paths
6. Order, restarts, and stop-loss

Clustered execution, continuation, merge and stop rules, and the worked route live in [clustering.md](clustering.md).

## Intake

Start from the request in ordinary language, before any framework vocabulary (source §13.4 DS01). Record:

- the difference or puzzle that needs explaining, deciding, or protecting;
- the requester, the question, and the intended and foreseeable use of the answer;
- the affected object or population;
- evidence cutoff and time horizon;
- the requested output (explanation, derivation, forecast, choice, intervention review, governance review, or design synthesis);
- whether the output could be used for handling, eligibility, rights, resource allocation, reputation, public memory, safety, or an automated, organizational, or institutional decision.

Ask a question only when the missing answer would select a materially different object, task, value premise, jurisdiction, or irreversible action. Otherwise mark the field and continue at a lower ceiling. Never require the person to learn Ariadne's vocabulary before their experience or need is acknowledged (source §1.5.2, §16.16).

## Depth selection

The source defines three diagnostic tiers; Ariadne adds L0 as its own routing outcome for questions that need no method run (source §13.6).

| Level | Conditions | Minimum route | Maximum result |
|---|---|---|---|
| L0 | Low impact, reversible, a single judgment-type output, and the user asked a question rather than for a method run | Direct bounded answer; no module run and no record | Bounded answer plus a one-line boundary declaration |
| L1 | Light description and probing questions: low complexity, low impact, reversible, limited material | Framing plus one relevant module | Description, questions, next observation |
| L2 | Standard reviewable judgment: structural comparison is needed but the output does not enter high-responsibility handling | Framing, evidence, relevant modules, audit when merging | Bounded comparative judgment or mechanism candidates; analytic recommendation when the choice module registers explicit premises |
| L3 | High-responsibility strong-judgment candidate: substantive high impact or embedding in automated, organizational, or institutional decisions | Framing, evidence, all affected lanes, choice when applicable, full audit with IG1-IG7 and SJ1-SJ8 | Strong-judgment candidate or requirements handoff; never authorization |

Strong judgment is set by use and foreseeable impact, not by tone, length, or confidence. A judgment intended or reasonably foreseeable to be used for handling, eligibility, rights, resource allocation, or material effects on a specific subject's reputation or public memory, or embedded in automated, organizational, or institutional decisions, is L3. Intermediate scores, recommendations, or screening that later feed such decisions count by their actual use. Public dissemination raises scrutiny according to the evaluated subject, factual allegation, identifiability, reach, and consequence, but does not by itself turn every analysis into a strong judgment. Ordinary argument evaluation, mechanism explanation, or normative opinion that touches none of these uses may state clear conclusions with proportionate evidence and review. Calling an output "commentary", "research", or "draft" does not exempt it when it actually meets the strong-judgment condition (source §13.5).

L0 is a routing outcome, not a record profile: answer directly, name the main gap or assumption in one line, and offer the full method only when the user asks for a record, the impact rises, or the answer would otherwise cross an output ceiling. When in doubt between L0 and L1, use L1.

A higher level means more record responsibility, not greater truth. Downgrade when evidence coverage falls, the object converts, reflexivity escapes control, or appeal or anti-retaliation fails. Urgency never deletes the object, protection, or stop conditions; when waiting is costly, offer only the narrowest, revocable, monitorable action requirement outside any authorization Ariadne could claim (source §13.6).

## Module map

| Observable need | Module | Consumes | Produces |
|---|---|---|---|
| Object, task, or representation ambiguity | `ariadne-framing` | Raw request or parent record | Object contract with task profile and request type |
| Claim, source, or evidence ambiguity | `ariadne-evidence` | Object contract and materials | Evidence/claim ledger, support ceilings, dependency map |
| Cross-scale, cross-circle, or representation move | `ariadne-scale` | Object and evidence records | Scale, circle-relation, or translation record; closure check |
| Why/how mechanism question | `ariadne-mechanism` | Bounded observations | Competing mechanism records with temporal routes |
| Human roles, privacy, power, meaning, actors, circles | `ariadne-human` | Human-domain object | Affected positions, HV routes, actor and circle boundaries |
| Event propagation, clocks, paths | `ariadne-dynamics` | Frozen state and mechanisms | Branch graph, state differences, signals, stops |
| Dated future claim | `ariadne-forecast` | Eligible paths and baseline | Forecast registry record |
| Real-world options or an action request | `ariadne-choice` | Bounded conclusions and explicit norms | Option comparison, distribution, analytic recommendation or requirements |
| High-impact use, merge, or governance | `ariadne-audit` | Complete child records | Gate results, strong-judgment register, conflicts, ceiling meet, writeback |

## Routing algorithm

1. Run framing for every new object, task, or changed purpose.
2. Run evidence before any comparative mechanism, forecast, or choice.
3. Add scale when an inference changes aggregation, space, time, organization, causal level, observation resolution, impact, network, jurisdiction, domain, circle relation, representation, or vocabulary, and only when that change can alter the conclusion's validity. Non-triggering counterexamples: restating one team's quarterly delay in hours instead of days changes representation but not what the claim asserts; citing last quarter's report as background while every claim stays inside the current quarter touches time without any cross-time inference.
4. Add human when a claim concerns people, roles, institutions, meaning, power, privacy, responsibility, consent, appeal, or refusal, and only when that dimension can alter the conclusion's validity or affect a real position. Non-triggering counterexamples: tuning a database index where people appear only as request volume makes no claim about any person; quoting an engineer's published talk as a technical source uses a person as provenance without a claim about people.
5. Add mechanism for explanation, diagnosis, every causal route, and every analogy route. Require at least two competitors when the material allows them, a simple baseline, channel observations, discriminating predictions, reverse or falsifying conditions, a residual comparison rule, and a temporal route for every cross-time claim. When no reasonable competitor exists, record the search range and failure conditions instead of inventing one (source §4.8.4, §13.4 DS11).
6. Add dynamics only when events, transitions, clocks, thresholds, feedback, or branch paths matter.
7. Add forecast only when the request needs an evaluable future judgment. Without registration, keep scenarios and avoid predictive phrasing such as "will" or "expected hit" (source §13.10 DF6).
8. Add choice for every action request, and pick its depth explicitly. An action request that meets every L1 condition may emit a compressed boundary card: one declaration line recording that facts, values, options, jurisdiction, authorization, stop conditions, and rollback are unknown and that no option is selected. Every other action request runs at L2 or higher and emits the typed card with facts, values, structured options including exactly one no-action option, jurisdiction, authorization, stop conditions, rollback plan, and either an analytic recommendation or an explicit `null`. Write `unknown` rather than omitting a field. A recommendation is withheld only for the specific missing norm, protection, or option that blocks it; an analysis already supported by evidence is not sent back to a question list merely because execution is unauthorized (source §12.16, §13.10 DF7).
9. Add audit for L2 merging and every L3 use. Audit is mandatory for public, automated, institutional, eligibility, allocation, safety, or difficult-to-reverse output.
10. For `synthesis_design`, run framing to freeze design constraints, success criteria, and the task profile; evidence for any load-bearing empirical claim; and choice's comparison discipline over the candidate designs (options, trade-offs, keep-current as the no-action analogue). The deliverable is a bounded proposal with its constraint record; construction and adoption return to the host workflow and any external decision process.

A triggered module carries one of two strengths. A trigger is required when the module's responsibility carries the conclusion: leaving it out would leave a load-bearing object, claim, bridge, or affected position unaudited. A trigger is optional when the dimension is present but bounded and its variation cannot overturn the conclusion. At L1 and L2, an optional module may be discharged with a single-line declaration: state the bounded finding and its gap in the record, mark the module run `not_run` with a reason naming this declaration, and keep or lower the ceiling. At L3 every triggered module is required.

## Retrieval order for mechanisms and paths

When a concrete problem arrives, first screen candidate mechanisms by object, scale, window, and requested output, then search paths from the observed state differences (source §6.14). Enter from four kinds of material:

1. the object's currently confirmable state;
2. directly confirmable changes after the event;
3. channels, capacities, and clocks able to carry later change;
4. mechanisms and external disturbances not yet distinguished.

Propose path candidates from state exit conditions and mechanism candidates from observed changes; then check each one's enabling conditions, propagation links, and minimum evidence. The order is only a search order: what is found first is not more likely true. Keep a competing candidate and a simple baseline beside every candidate: a returned signal against learning, local overload against a temporary demand rise, a capacity drop, or a common cause, and a cross-circle cascade against synchronized exposure. For every candidate path, write the conditions that keep it alive, the observable changes the mechanism should produce first, the opposite signals, and its stop. An early signal is not the outcome restated smaller. Shared evidence across paths adds no independent support.

## Order, restarts, and stop-loss

Run lanes in the dependency order `framing -> evidence -> [scale, mechanism, human] -> dynamics -> forecast -> choice -> audit`, skipping non-applicable lanes. If a module changes the object, task, evidence cutoff, scale, affected positions, or purpose, restart at the earliest affected dependency (source §13.3). The restart budget is binding: the same dependency may be restarted at most twice in one run. When a third restart would be needed, do not restart; close the run at the current ceiling as a downgrade and record the oscillation cause in `unknowns_and_counterevidence.unknowns`.

Apply a stop-loss to the run as a whole: when the projected record work is clearly disproportionate to the question's stakes, or two consecutive module runs have left the bounded conclusion unchanged, close the run at the current ceiling, state the remaining gaps, and hand the next evidence step back instead of adding module runs. Procedures cost time, care, privacy, and expression; prioritize the gaps that would change the current judgment or a protection arrangement, and keep the partial conclusions existing material already supports (source §1.5.2).

Child-record mechanics, clustered execution, continuation events, merge and stop rules, and the worked route are specified in [clustering.md](clustering.md); read it when running parallel lanes, merging sibling records, or continuing an earlier run.
