---
name: ariadne-evidence
description: "Grade how far existing materials support each claim: freeze an evidence cutoff, keep source, material, observation, evidence, counterevidence, judgment, and authorization apart, and downgrade claim by claim. Use when claims, citations, measures, causal chains, or analogies need support grading, competing explanations, independence checks, and counterevidence. For a multi-module pass, start with ariadne-skill. 适用于：证据够不够、来源核查、这个结论站得住吗、因果与类比检查、反证清点。"
license: MIT
metadata:
  record_schema: "2.0"
---

# Ariadne Evidence

## Overview

Audit how far the available record supports each claim, and only that claim. Preserve the chain from source to material, observation, evidence, counterevidence, judgment, and external authorization without letting one level impersonate the next. Domain studies, archives, testimony, proofs, and texts keep the standing their own design gives them; a gap lowers only the claims that depend on it.

## Procedure

1. **Consume or start the Method Record.** Preserve the object contract and task profile, lineage, evidence cutoff, unknowns, counterevidence, and output ceiling. If no record exists, create a minimum candidate object and keep unresolved fields explicit.
2. **Freeze the audit window.** Record the `evidence_cutoff` before drawing conclusions. Put later material in a child record; never repair a prior result by silently changing its inputs.
3. **Split claims by responsibility.** Label each claim D definition, G empirical question family instance, E epistemic constraint, H human-domain clause, N normative commitment, O operating procedure, or F conditional formal proposition. Split sentences that mix roles. Treat C entries as use contracts over registered results, not as an extra kind of fact.
4. **Separate dependency types.** Mark `inferential_requires`, `protocol_requires`, `specializes`, and `applies_to` independently; only inferential hard prerequisites enter a reasoning chain. Record each claim's in-record prerequisites in `depends_on`.
5. **Keep material identity traceable.** Under the common method constraints 法1-法3, keep report, observation, model belief, formal proof, simulation output, and execution receipt as different identities; say what each inference adds; never count reprocessing of the same data, recursive simulation depth, or file count as new observation.
6. **Apply the relevant contract.** Use the source, measurement, causal, chain, analogy, formal-conclusion, root-instance, or human-instance contract in the reference. Preserve simple baselines, competing explanations (and what they compete over), residuals, and extrapolation limits.
7. **Respect support and zero-result gates.** Definitions, framework text, examples, IDs, field completeness, exploratory work, and post-result changes are not empirical support. A failed positive gate stays unresolved unless a frozen equivalence or sufficiency test, power or sensitivity gate, and tolerance all support the bounded null. Existing domain findings support what their actual design supports; they need no retrofitted pre-result contract and do not automatically become G-instance support.
8. **Downgrade claim by claim.** Lower only the claims whose `depends_on` chain rests on a missing, contradicted, or withdrawn link; keep independently supported claims at their level. Block every related output only when a global source, shared premise, or object boundary fails. Never restore a ceiling by renaming, splitting, or branching.
9. **Set the ceiling and handoff.** Use `description_only` when the chain is incomplete and `diagnostic_only` for a bounded evidence-strength judgment. Use `requirements_only` only when the diagnostic basis already holds and the output adds explicit external process requirements. A child run preserves or lowers its parent unless this version newly admits named external evidence or a fulfilled protocol. Never make an action recommendation or expand authorization. Always set `authorization_effect: none`.

Read [references/evidence-contracts.md](references/evidence-contracts.md) for field-level contracts, 法1-法3, the G1-G4 question families (G1 grouping gain, G2 named channel, G3 historical increment, G4 representation closure or conversion) and H-instance rules, the history three questions, E1-E5 epistemic gates, C1-C12 result contracts with their carried branches, condition trees, and a complete standalone example.

## Method Record Contract

Produce every common field and add an `ariadne-evidence` entry to `module_runs`. Keep claim texts, support IDs, and `depends_on` in `claim_ledger`; a supported claim resolves every `support_id` to an admitted source or earlier in-record claim and every `support_rule_id` to the explicit `rule_registry`; every `depends_on` entry names an earlier claim. Reject ghost sources and invented `RULE:*` labels. Put unresolved observations, missing bridges, competing explanations, and counterevidence in `unknowns_and_counterevidence`. Recommend only modules justified by the audit.

Do not overwrite an upstream record. Create a child version when the cutoff, source set, claim meaning, object, task, scale, success criterion, baseline, or threshold changes. The full schema ships with the suite router at `ariadne-skill/references/method-record.schema.json`; the complete standalone example in [references/evidence-contracts.md](references/evidence-contracts.md) is schema-checked in CI.

## Quick Reference

| Evidence problem | Required move | Maximum result |
|---|---|---|
| Source or quote only | Recover material, observation context, and source relations | Description |
| Indicator moved | Check real change, narrow adaptation, entry or reporting change, and record falsification | Candidate reading per source |
| Pre/post association | Preserve common causes, selection, measurement change, and reverse direction | Candidate relationship |
| Causal claim | Freeze estimand, cause version, result, timing, channel, comparison, and falsifier | Bounded total effect; channel unresolved unless identified |
| Two links each supported | Check same cases, same timing, common support, and joint response | No chain claim from multiplying averages |
| Analogy | Name heuristic, formal instance, or target-tested relation | Target hypothesis unless independently tested |
| Positive gate fails | Check frozen null gates | Unresolved unless all null gates pass |
| One gap among many claims | Lower only dependent claims | Others keep their level |
| Normative or action sentence | Split N and O from empirical claims | No recommendation or authorization |

## Mini Example

Input: "Our new onboarding guide cut support tickets by 30%, right?" Skeleton only, not a complete record:

```yaml
request_type: diagnosis
evidence_cutoff: {as_of: '2026-08-22T00:00:00+08:00'}
claim_ledger:
- {claim_id: E-ticket-count, claim_type: E, status: observed}
- {claim_id: G-guide-cause, claim_type: G, status: unresolved, depends_on: [E-ticket-count]}
output_ceiling: description_only
```

## Stopping Conditions

Stop at description when source provenance or observation context is missing. Stop at an unresolved candidate when competing explanations or counterevidence are not distinguishable. Stop at evidentiary requirements when a concrete instance was not frozen before results. When no reasonable competitor exists, record the search range and failure conditions instead of inventing one. Stop immediately before value, responsibility, sacrifice, choice, or real-world disposition, and route those questions to `ariadne-choice` or `ariadne-audit`.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Common Mistakes

- Treating a document, dashboard, testimony, or dataset as evidence for every claim it could mention.
- Counting method definitions, examples, internal labels, a valid-looking ID, or several reanalyses of one dataset as independent empirical support.
- Calling correlation, sequence, or a plausible story a causal channel, or multiplying two average link effects into a chain effect.
- Using absent, silent, protected, or unobservable material as negative evidence without showing the record should have existed and been findable.
- Switching subtype, outcome, threshold, model, time window, or success criterion after seeing results.
- Calling "not significant" proof of no effect, or closure.
- Stripping an existing study of its findings because it was never converted into a frozen instance.
- Lowering every claim because one dependency failed, or keeping a claim up after its own dependency failed.
- Letting empirical confidence produce a value judgment, responsibility assignment, or action authority.
