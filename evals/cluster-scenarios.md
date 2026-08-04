# Clustered Execution Scenarios

K01 and K02, together with the clustered counterparts for C01-C03, are fully frozen in [fixtures/frozen-scenarios.json](fixtures/frozen-scenarios.json): exact prompts, materials, source IDs, seed parent records, expected invariants, mode contracts, and reference sequential/clustered lineage graphs are machine-checkable.

For a fresh run, give every sibling the exact same seed parent, materials, and cutoff. Create deterministic module output IDs. Audit merges all sibling IDs and versions in canonical order, then later work uses the merge as its parent. Do not average conflicts or treat module text as new evidence.

Compare both modes on:

- exact frozen facts;
- exact explicit unknowns and counterevidence;
- named conflicts;
- resolvable root and module-output lineage semantics;
- the ordered ceiling meet;
- `authorization_effect: none`.

Run:

```powershell
python -X utf8 -B scripts/validate_evals.py
```

The validator resolves complete ID/version pairs, proves every node lies on a root-to-terminal path, and checks exact sequential edges plus the contracted clustered prefix, lanes, merge, and suffix. It rejects unresolved or version-drifted references, skipped order edges, missing merge parents, noncanonical parent order, duplicate records, cycles, matching orphan nodes, changed facts or unknowns, ceiling drift, and authorization drift.
