# Legacy Mechanism Contracts

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/mechanism-contracts.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## For a standalone run,

For a standalone run, create the common Method Record and make these module-specific additions:

- Set `request_type` to the actual output class, normally `explanation` or `diagnosis`.
- Put `S*=<B,X,R,I,T,SP,K>`, the task profile, and the target residual in `object_contract`.
- Freeze source and observation availability in `evidence_cutoff`.
- Put the active scale profile, transform kind, and generalization unit in `scale_scope`.
- Put bounded claims in `claim_ledger` with `depends_on`; put every mechanism candidate's temporal route, channel observation, discriminating prediction, reverse or falsifier, and residual comparison rule in the typed mechanism payload.
- Preserve missing fields and competing accounts in `unknowns_and_counterevidence`.
- Apply the ordered ceiling transition algebra. A normal module child preserves or lowers; only newly admitted external evidence or protocol fulfillment in a child can raise.
- Append this run to `module_runs`, name only useful handoffs in `recommended_next_modules`, and set `authorization_effect: none`.

Create a child record instead of overwriting a parent whenever evidence, scope, task, object identity, or a frozen comparison changes.

## Legacy candidate payload

Retain multiple candidates when present evidence cannot distinguish them. Prefer the simple baseline when added mechanisms do not improve out-of-sample explanation or intervention performance. In the typed payload, every candidate separately fills `temporal_route`, `channel_observation`, `discriminating_prediction`, `reverse_or_falsifier`, and `residual_comparison_rule`. Candidate IDs and the four-field test signatures must be distinct; relabeling the same story does not create a competitor.

## Legacy mechanism output mapping

Record the result as follows: put the receipt and any field-version evidence in `claim_ledger`; put blocked-channel comparison, execution, retention, repeated-round evidence, and the competing instruction in `unknowns_and_counterevidence`; set `output_ceiling: diagnostic_only`; recommend evidence repair or human-domain writeback analysis only if needed; and set `authorization_effect: none`. The result may distinguish arrival, feedback, writeback, and a learning candidate. It cannot certify institutional legitimacy, assign blame, require a remedy, or authorize a rule change.
