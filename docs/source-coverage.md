# Lattice Kernel Source Coverage

Primary source: *跨尺度多圈层结构推演框架 v8.2* (July 2026), SHA-256 `608A4E4099B18C96C18ED3C92A2AB5CDACBD737DACA4214C77DEBDD795DA3A20`.

The source document is not included in this public repository. This map assigns every source area to an installable Ariadne owner and records the methodology that must be distilled, not copied wholesale.

| Source area | Primary owner | Required coverage |
|---|---|---|
| Part 1 - Guide | `ariadne-framing`, `ariadne-skill` | Output classification, risk escalation, strong-judgment questions, protection floor, full-chain entry, capability boundary. |
| Part 2 - Boundaries and method | `ariadne-framing`, `ariadne-evidence` | Two-stage object admission; D/G/E/H/N/O claim types; four dependency types; causal, evidence, analogy, and source contracts; missing states and output downgrade. |
| Part 3 - General structural grammar | `ariadne-framing`, `ariadne-mechanism` | D0-D3, U01-U11, object/state/feedback/scale definitions, translation distinction, minimum structural closure. |
| Part 4 - Root hypotheses and conclusions | `ariadne-evidence`, `ariadne-mechanism` | Root and human instance contracts, G1-G4, E1-E5, C1-C12 dependency ceilings, simple-baseline and zero-result discipline. |
| Part 5 - Cross-scale and cross-circle transformations | `ariadne-scale` | Nine-axis scale profile, partial order, M01-M09, three-state transformations, scale records, circle relations, translation-loss audit, closure and residual return. |
| Part 6 - Operation and evolution | `ariadne-mechanism`, `ariadne-dynamics` | Feedback, learning, maintenance, load/capacity/recovery, phase, selection, coevolution, dissolution, repair boundary, asynchronous clocks and cascades. |
| Part 7 - Human structured world | `ariadne-human` | H1-H6 roles, GC/GS/GE/CV/RS/IS/IM/IB type separation, HV01-HV11 interface, evidence and action ceilings. |
| Part 8 - Human state prototypes | `ariadne-human` | State-record contract, S0-S6 as non-destiny prototypes, nonlinear paths, orderly exit, reverse conditions, exclusion rules. |
| Part 9 - Actor state and personality hypotheses | `ariadne-human` | Slow/medium/fast variables, role activation, bidirectional actor-circle effects, evidence grades, privacy, refusal, snapshot limits, no clinical inference. |
| Part 10 - Multi-circle objects and joint state | `ariadne-human`, `ariadne-dynamics` | Circle and joint-object contracts, parallel/nested/overlapping/bridging/competitive/temporary relations, multiple membership, dual-channel conditions, five clocks, complexity gate. |
| Part 11 - Event-driven dynamic derivation | `ariadne-dynamics` | Event contract, joint-state update, nine-step loop, propagation/delay/threshold, feedback cascades, branch graphs, variable candidates, counterfactuals, recursive simulation, pruning and stopping. |
| Part 12 - Conditional forecast and finite choice | `ariadne-forecast`, `ariadne-choice` | Output isolation, forecast registry, local predictability, order-specific evaluation, simple baselines, probability/windows, calibration, signals, failure semantics, option bridge and result writeback. |
| Part 13 - Interfaces and tools | `ariadne-skill`, `ariadne-audit` | Four transformations, seven-gate main flow, five-gate/thirteen-step expansion, strong-judgment eight, levels L1-L3, formal tools, AI boundary, run record and nine dynamic gates. |
| Part 14 - Normative choice | `ariadne-choice` | Fact/value separation, three choice processes, N1-N5, consequences and distribution, coercion/default/agenda/representation/minority protection, J axis, O1-O4, PF-1-PF-10. |
| Part 15 - Intervention and applications | `ariadne-choice` (primary), `ariadne-audit` | Task separation and T0-T4 stay in choice/audit guidance; `ariadne-audit/references/application-contracts.json` supplies all nine APP object/method, protected-position, evidence, output, prohibited-action, stop/failure, and handoff contracts. |
| Part 16 - Governance | `ariadne-audit` | Object/self separation, version authority, falsification/downgrade/pause, case and forecast tracking, pre-concept gate, protected opacity, malicious compliance, AI non-proof, weak signals, no-exit protection, weaponization, capture, writeback, external review, orderly death and model retirement, knowledge lineage and source transparency. |
| Appendix A - Human variable cards | `ariadne-human` | `ariadne-human/references/human-variable-cards.json` is the direct one-to-one map of all 39 registered fields for each HV01-HV11 card; the human-domain reference supplies use rules without replacing card values. |
| Appendix B - Numbering and terminology | `ariadne-skill` | `ariadne-skill/references/source-navigation.json` directly owns the complete stable index for all 22 numbering systems and the four shared notations. It routes each code to its authoritative part and Ariadne owner; the index never redefines a contract. |
| Appendix C - Revision history | `ariadne-audit` | Preserve the governance lesson that version changes do not erase prior records; do not reproduce development narration in Skill files. |
| Appendix D - Shared kernel and mapping | `ariadne-skill` | `source-navigation.json` implements D.4 by retaining the two contract-system differences, forbidding names/examples/shared steps from replacing either complete contract, and limiting mapping to preserved/changed/collapsed/omitted/new-unknown/source-lineage/applicability/residual/stopping semantics. It implements D.5 as an eight-field cross-scale proof heuristic (source object, target object, limit or scale law, initial conditions, history structure, error, valid time, failure boundary) routed to `ariadne-scale`; it explicitly does not prove universal information loss, a Boltzmann law for social or psychological systems, or identity between task loss and physical entropy. |

## Coverage rule

Each row must be represented in the named Skill body or its direct reference. A complete row means the method, admissible output, failure boundary, and next handoff are present. Mentioning a term without those four elements does not count as coverage.
