---
name: ariadne-evidence
description: "Grade how far existing materials can support each claim: freeze an evidence cutoff, then separate source, material, observation, evidence, counterevidence, judgment, and external authorization. Use when claims, citations, causal or analogy arguments need support grading, competing explanations, and counterevidence checks. For a multi-module pass, start with ariadne-skill. 适用于：证据够不够、来源核查、这个结论站得住吗、因果与类比检查、反证清点。"
license: MIT
metadata:
  record_schema: "1.2"
---

# Ariadne Evidence

## Overview

Audit how far the available record supports each claim. Preserve the full chain from source to material, observation, evidence, counterevidence, judgment, and external authorization without letting one level impersonate the next.

## Procedure

1. **Consume or start the Method Record.** Preserve the object contract, lineage, evidence cutoff, unknowns, counterevidence, and output ceiling. If no record exists, create a minimum candidate object and keep unresolved fields explicit.
2. **Freeze the audit window.** Record the `evidence_cutoff` before drawing conclusions. Put later material in a child record; never repair a prior result by silently changing its inputs.
3. **Split claims by responsibility.** Label each claim D definition, G empirical root, E epistemic constraint, H human-domain clause, N normative commitment, or O operating procedure. Split sentences that mix types.
4. **Separate dependency types.** Mark `inferential_requires`, `protocol_requires`, `specializes`, and `applies_to` independently. Put only inferential hard prerequisites in a reasoning chain.
5. **Build the evidence chain.** Identify source, material, observation, evidential use, counterevidence, judgment, and any external authorization as distinct records. Link each claim to supporting and contradicting IDs.
6. **Apply the relevant contract.** Use the source, causal, analogy, root-instance, or human-instance contract in the reference. Preserve simple baselines, alternative explanations, residuals, and extrapolation limits.
7. **Respect support and zero-result gates.** Treat definitions, framework text, examples, IDs, field completeness, exploratory work, and post-result changes as non-support. Treat a failed positive gate as unresolved unless a frozen equivalence or sufficiency test, power or sensitivity gate, and tolerance all support the bounded null.
8. **Set the ceiling and handoff.** Use `description_only` when the chain is incomplete and `diagnostic_only` for a bounded evidence-strength judgment. Use `requirements_only` only when the diagnostic basis already holds and the output adds explicit external process requirements. A child module run preserves or lowers its parent unless this version newly admits named external evidence or a fulfilled protocol. Never make an action recommendation or expand authorization. Always set `authorization_effect: none`.

Read [references/evidence-contracts.md](references/evidence-contracts.md) for field-level contracts, G1-G4 root rules (G1 candidate grouping, G2 specified channel, G3 historical increment, G4 scale closure or conversion) and H-instance rules, E1-E5 epistemic gates (E1 object declaration, E2 observation position, E3 conditional observation participation, E4 alternatives and residuals, E5 cross-scale transfer), conditional inference ceilings, and a complete standalone example.

## Method Record Contract

Produce every common field and add an `ariadne-evidence` entry to `module_runs`. Keep claim texts and support IDs in `claim_ledger`; a supported claim resolves every `support_id` to an admitted source or earlier in-record claim and every `support_rule_id` to the explicit `rule_registry`. Reject ghost sources and invented `RULE:*` labels. Put unresolved observations, missing bridges, alternative explanations, and counterevidence in `unknowns_and_counterevidence`. Recommend only modules justified by the audit.

Do not overwrite an upstream record. Create a child version when the cutoff, source set, claim meaning, object, scale, success criterion, baseline, or threshold changes. The full schema ships with the suite router at `ariadne-skill/references/method-record.schema.json`; the complete standalone example in [references/evidence-contracts.md](references/evidence-contracts.md) is schema-checked in CI.

## Quick Reference

| Evidence problem | Required move | Maximum result |
|---|---|---|
| Source or quote only | Recover material and observation context | Description |
| Pre/post association | Preserve common causes, selection, measurement change, and reverse direction | Candidate relationship |
| Causal claim | Freeze cause, result, timing, channel, counterfactual, controls, and falsifier | Candidate mechanism unless identified |
| Analogy | State source, target, mapping, differences, and target test | Target hypothesis |
| Positive gate fails | Check frozen null gates | Unresolved unless all null gates pass |
| Normative or action sentence | Split N and O from empirical claims | No recommendation or authorization |

## Mini Example

Input: "Our new onboarding guide cut support tickets by 30%, right?" Skeleton only, not a complete record:
```yaml
request_type: diagnosis
evidence_cutoff: {as_of: '2026-08-22T00:00:00+08:00'}
claim_ledger:
- {claim_id: G-guide-cause, claim_type: G, status: unresolved}
output_ceiling: description_only
```

## Stopping Conditions

Stop at description when source provenance or observation context is missing. Stop at an unresolved candidate when alternatives or counterevidence are not distinguishable. Stop at evidentiary requirements when a concrete instance was not frozen before results. Stop immediately before value, responsibility, sacrifice, choice, or real-world disposition, and route those questions to `ariadne-choice` or `ariadne-audit`.

Peer unavailable -> not_run/module_unavailable, outputs unknown, ceiling preserve-or-lower, never inline (full clause: lattice-kernel.md, Peer unavailability clause).

## Common Mistakes

- Treating a document, dashboard, testimony, or dataset as evidence for every claim it could mention.
- Counting method definitions, examples, internal labels, or a valid-looking ID as external empirical support.
- Calling correlation, sequence, or a plausible story a causal channel.
- Using absent, silent, protected, or unobservable material as negative evidence.
- Switching subtype, outcome, threshold, model, time window, or success criterion after seeing results.
- Calling “not significant” proof of no effect.
- Letting empirical confidence produce a value judgment, responsibility assignment, or action authority.
