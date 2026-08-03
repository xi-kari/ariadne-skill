---
name: ariadne-evidence
description: Use when claims, sources, observations, causal stories, analogies, counterevidence, or evidence strength must be separated and audited.
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
8. **Set the ceiling and handoff.** Use `description_only` when the chain is incomplete, `diagnostic_only` for a bounded evidence-strength judgment, and `requirements_only` when only pre-evidence requirements are justified. Never make an action recommendation or expand authorization. Always set `authorization_effect: none`.

Read [references/evidence-contracts.md](references/evidence-contracts.md) for field-level contracts, G1-G4 and H-instance rules, E1-E5, conditional inference ceilings, and a complete standalone example.

## Method Record Contract

Produce every common field and add an `ariadne-evidence` entry to `module_runs`. Keep claim texts and support IDs in `claim_ledger`; put unresolved observations, missing bridges, alternative explanations, and counterevidence in `unknowns_and_counterevidence`. Recommend only modules justified by the audit.

Do not overwrite an upstream record. Create a child version when the cutoff, source set, claim meaning, object, scale, success criterion, baseline, or threshold changes.

## Quick Reference

| Evidence problem | Required move | Maximum result |
|---|---|---|
| Source or quote only | Recover material and observation context | Description |
| Pre/post association | Preserve common causes, selection, measurement change, and reverse direction | Candidate relationship |
| Causal claim | Freeze cause, result, timing, channel, counterfactual, controls, and falsifier | Candidate mechanism unless identified |
| Analogy | State source, target, mapping, differences, and target test | Target hypothesis |
| Positive gate fails | Check frozen null gates | Unresolved unless all null gates pass |
| Normative or action sentence | Split N and O from empirical claims | No recommendation or authorization |

## Stopping Conditions

Stop at description when source provenance or observation context is missing. Stop at an unresolved candidate when alternatives or counterevidence are not distinguishable. Stop at evidentiary requirements when a concrete instance was not frozen before results. Stop immediately before value, responsibility, sacrifice, choice, or real-world disposition, and route those questions to `ariadne-choice` or `ariadne-audit`.

## Common Mistakes

- Treating a document, dashboard, testimony, or dataset as evidence for every claim it could mention.
- Counting method definitions, examples, internal labels, or a valid-looking ID as external empirical support.
- Calling correlation, sequence, or a plausible story a causal channel.
- Using absent, silent, protected, or unobservable material as negative evidence.
- Switching subtype, outcome, threshold, model, time window, or success criterion after seeing results.
- Calling “not significant” proof of no effect.
- Letting empirical confidence produce a value judgment, responsibility assignment, or action authority.
