# Legacy Dynamic Derivation

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions and examples describe the old interface only. They do not govern current path selection, require universal fields or cap ordinary work by a linear record ceiling. Use the current [library reference](../library/dynamic-derivation.md) for substantive methods. Old module names are historical labels, not installable dependencies.

## For a standalone run,

For a standalone run, create the common Method Record and record:

- the frozen joint object, identities, and task profile (target query, horizon, environment, allowed operations, error tolerance) in `object_contract`;
- only the source and observation cutoff in `evidence_cutoff`;
- every event ID, fact status, source IDs, window, observation position, and model version in the typed `ariadne-dynamics` payload;
- active actor, circle, network, temporal, impact, and jurisdiction axes in `scale_scope`;
- event contracts, state deltas, mechanism provenance, branches, signals, and stop states in `claim_ledger`;
- disputed facts, missing channels, parameter intervals, residuals, candidate variables, and counterpaths in `unknowns_and_counterevidence`;
- the ordered ceiling transition; a normal child preserves or lowers, and only newly admitted external evidence or protocol fulfillment in a child can raise;
- this run and its parent path in `module_runs`, necessary handoffs in `recommended_next_modules`, and `authorization_effect: none`.

Create a new child record when a later observation, changed scope, altered model, or new event enters. Never pour later outcomes back into the original starting state.

## Legacy dynamics output mapping

Keep the path graph conditional and unranked unless evidence supports comparison. Put the frozen snapshot, event status, mechanisms, branches, clocks, and signals in `claim_ledger`; put disputed content, missing channels, residuals, and candidates in `unknowns_and_counterevidence`; set `output_ceiling: diagnostic_only`; recommend `ariadne-forecast` only if the user separately asks for a preregistered future claim; and set `authorization_effect: none`. The derivation may expose conditions and observations. It may not decide what the company should do or authorize anyone to act.
