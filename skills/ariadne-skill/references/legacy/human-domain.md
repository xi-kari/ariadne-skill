# Legacy Human Domain

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/human-domain.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## For a standalone run,

For a standalone run, create the common Method Record and record:

- the actor, circle, or joint object, its `B/X/R/I/T/SP/K`, and the task profile in `object_contract`;
- only the source cutoff timestamp, admitted source IDs, and after-cutoff exclusion flag in `evidence_cutoff`;
- source scale, target scale, transform kind, and transformation status in `scale_scope`;
- observed behavior, candidate variables, H-instance state, HV route, circle relations, and bounded conclusions in `claim_ledger`, with `depends_on` where a conclusion rests on another;
- missing states, refusals, conflicts, counterexamples, local exclusion zones, and competing explanations in `unknowns_and_counterevidence`;
- observation position, privacy state, allowed purpose, reasonable alternatives and responsible human review in the typed `ariadne-human` module payload; fewer than two alternatives requires `competition_search` with `search_scope`, `reason_no_alternative` and `failure_conditions`, not an invented competitor;
- `affected_positions` as a closed four-class object: `direct`, `indirect`, `low_power`, and `no_exit`; every class contains `status`, `positions`, and `reason`, and an unknown, protected, or non-applicable class remains explicit with an empty list rather than collapsing into free text;
- the ceiling transition, traceable module input/output records, necessary handoffs, and `authorization_effect: none`.

Create a child record rather than overwriting a parent when the object, evidence, permitted use, identity, task, or scale changes. Do not let a fuller form raise the empirical or action status of its contents.

## Legacy human output mapping

Report in layers: confirmed behavior and role facts; supported circle conditions; candidate state hypotheses with their support; the two-way channels; the next most discriminating observation; and the unknowns. Place confirmed behavior, role facts, and supported circle conditions in `claim_ledger`. Put personality, intent, hidden constraints, dissent, protected information, alternative role and resource explanations, and unobserved downstream effects in `unknowns_and_counterevidence`. Use `output_ceiling: diagnostic_only` only if the object and evidence support the bounded actor-circle diagnosis; otherwise lower it to `description_only`. Recommend `ariadne-dynamics` only if event propagation is requested. Set `authorization_effect: none`. The result may identify discriminating observations; it may not diagnose, punish, compel disclosure, or authorize a management action.

## Legacy prototype reviewer validation

- Record the reviewer as `reviewer_id + independent + reviewed_at + material_version + outcome`, and bind appeal and rollback each to a structured procedure ID and status. After NFKC, whitespace, and case normalization, `reviewer_id` must not equal the object ID or any derived alias. None of these may be self-declaration strings such as "reviewed" or "appealable".
- Keep `normative_status=descriptive_only` and `action_authorization=none` whatever the outcome. When a label is withdrawn or rewritten, preserve the original evidence, dissent, and version chain.
