# Legacy Governance Lifecycle

> Compatibility archive for the retired multi-module suite and Method Record 2.0/2.1. These instructions describe the historical interface only; they do not govern current work or impose a linear output ceiling. Use the current [library reference](../library/governance-lifecycle.md) for substantive methods.

## Legacy governance registry binding

Resolve canonical actors, evidence, interests, authorization, external review, dissent, and structured VERSION-LOG entries through runtime registries. Do not use aliases as identity, self-declared independence, internal signatures as external approval, or an issuer who is also the holder or proposer.

## Legacy version-log encoding

For every VERSION-LOG entry, bind the governance record, subject, canonical source and target versions, transition, old and new states, event type, time, owner, evidence, counterexample, text effect, process effect, ceiling effect, and downstream writeback. Require a strictly increasing numeric target version. For an applied change, require at least one real text, process, or ceiling change and distinct before and after hashes.

## Legacy contestability payload

Every high-impact audit writes the typed `contestability` payload. `owner` must contain a tested reachable contact, not a role label; `deadline` is an RFC 3339 response deadline; `original_record_retention` stays true; `downstream_correction_target` names every registry or decision surface to correct; `rollback_recovery_target` names the state, rights, resources, services, access, and records to restore; and `remedy` names restitution plus residual-harm tracking. If any field is missing or the owner is unreachable, fail the relevant gate and pause high-impact use.
