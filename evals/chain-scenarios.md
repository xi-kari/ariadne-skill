# Sequential Chain Scenarios

The authoritative prompts, material text, source IDs, seed parent Method Records, and expected facts/unknowns/ceilings are frozen in [fixtures/frozen-scenarios.json](fixtures/frozen-scenarios.json). Do not paraphrase or supplement them during a scored run.

Run C01-C03 with only each scenario's `prompt`, `materials`, `source_ids`, and `seed_parent_record`. Every scenario contains actual sequential and clustered `mode_results` plus an independent `mode_contract`. Preserve the exact declared sequential module order and parent ID/version edge. In clustered mode, preserve the prefix, same-parent lanes, canonical multi-parent audit merge, and exact downstream suffix. A module may organize the frozen label but may not promote it to an observation, add outside facts, or raise the ceiling merely because it completed.

Validate the fixtures before use:

```powershell
python -X utf8 -B scripts/validate_evals.py
```

Score each result against `expected.frozen_facts`, `expected.unknowns`, `expected.conflicts`, `expected.output_ceiling`, and `expected.authorization_effect`. The comparator indexes every root, node, edge, and terminal by `record_id` plus `record_version`, and rejects drift, skipped order edges, dropped merge parents, disconnection, cycles, and orphan nodes. Store any new run outside the frozen fixture until a separately authorized fixture revision.
