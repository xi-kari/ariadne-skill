from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema.exceptions import ValidationError

try:
    from scripts.validate_repo import validate_method_record, validate_record_semantics
except ModuleNotFoundError:
    from validate_repo import validate_method_record, validate_record_semantics


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "evals" / "fixtures" / "frozen-scenarios.json"
SCHEMA_PATH = ROOT / "schemas" / "method-record.schema.json"
EXPECTED_IDS = ["C01", "C02", "C03", "K01", "K02"]
CANONICAL_MODE_CONTRACTS = {
    "C01": {
        "sequential_order": ["ariadne-framing", "ariadne-evidence", "ariadne-scale", "ariadne-mechanism", "ariadne-dynamics", "ariadne-forecast"],
        "clustered": {
            "prefix_order": ["ariadne-framing", "ariadne-evidence"],
            "parallel_modules": ["ariadne-scale", "ariadne-mechanism"],
            "merge_module": "ariadne-audit",
            "suffix_order": ["ariadne-dynamics", "ariadne-forecast"],
        },
    },
    "C02": {
        "sequential_order": ["ariadne-framing", "ariadne-evidence", "ariadne-human", "ariadne-mechanism", "ariadne-dynamics", "ariadne-choice", "ariadne-audit"],
        "clustered": {
            "prefix_order": ["ariadne-framing", "ariadne-evidence"],
            "parallel_modules": ["ariadne-human", "ariadne-mechanism"],
            "merge_module": "ariadne-audit",
            "suffix_order": ["ariadne-dynamics", "ariadne-choice", "ariadne-audit"],
        },
    },
    "C03": {
        "sequential_order": ["ariadne-framing", "ariadne-evidence", "ariadne-scale", "ariadne-human", "ariadne-choice", "ariadne-audit"],
        "clustered": {
            "prefix_order": ["ariadne-framing", "ariadne-evidence"],
            "parallel_modules": ["ariadne-scale", "ariadne-human"],
            "merge_module": "ariadne-audit",
            "suffix_order": ["ariadne-choice", "ariadne-audit"],
        },
    },
    "K01": {
        "sequential_order": ["ariadne-evidence", "ariadne-scale", "ariadne-mechanism", "ariadne-human", "ariadne-audit"],
        "clustered": {
            "prefix_order": ["ariadne-evidence"],
            "parallel_modules": ["ariadne-scale", "ariadne-mechanism", "ariadne-human"],
            "merge_module": "ariadne-audit",
            "suffix_order": [],
        },
    },
    "K02": {
        "sequential_order": ["ariadne-evidence", "ariadne-scale", "ariadne-mechanism", "ariadne-dynamics", "ariadne-forecast", "ariadne-choice", "ariadne-audit"],
        "clustered": {
            "prefix_order": ["ariadne-evidence"],
            "parallel_modules": ["ariadne-scale", "ariadne-mechanism"],
            "merge_module": "ariadne-audit",
            "suffix_order": ["ariadne-dynamics", "ariadne-forecast", "ariadne-choice", "ariadne-audit"],
        },
    },
}
INVARIANT_FIELDS = [
    "frozen_facts",
    "unknowns",
    "conflicts",
    "output_ceiling",
    "authorization_effect",
]


def _ref_key(item: dict) -> tuple[str, int]:
    return item["record_id"], item["record_version"]


def _plain_ref(item: dict) -> dict:
    return {"record_id": item["record_id"], "record_version": item["record_version"]}


def _validate_record_version(item: dict, label: str, errors: list[str]) -> None:
    if type(item.get("record_version")) is not int:
        errors.append(f"{label} record_version must be an integer")


def _validate_lineage_graph(result: dict) -> tuple[list[str], dict[tuple[str, int], dict]]:
    errors: list[str] = []
    lineage = result["lineage"]
    roots = lineage["root_records"]
    for root in roots:
        _validate_record_version(root, "lineage root", errors)
    _validate_record_version(lineage["terminal_record"], "lineage terminal", errors)
    for node in lineage["nodes"]:
        _validate_record_version(node, "lineage node", errors)
        for reference in node["input_records"]:
            _validate_record_version(reference, "lineage input", errors)
    root_keys = [_ref_key(root) for root in roots]
    if len(root_keys) != len(set(root_keys)):
        errors.append("lineage root record references must be unique by ID and version")

    nodes: dict[tuple[str, int], dict] = {}
    for node in lineage["nodes"]:
        key = _ref_key(node)
        if key in nodes or key in set(root_keys):
            errors.append(f"duplicate lineage record reference: {key[0]}@{key[1]}")
        nodes[key] = node
    terminal_key = _ref_key(lineage["terminal_record"])
    if terminal_key not in nodes:
        errors.append("terminal record is absent from lineage nodes")
    known = set(root_keys) | set(nodes)
    for node in nodes.values():
        node_key = _ref_key(node)
        if not node["input_records"]:
            errors.append(f"non-root lineage node has no parent edge: {node_key[0]}@{node_key[1]}")
            continue
        input_keys = [_ref_key(ref) for ref in node["input_records"]]
        if len(input_keys) != len(set(input_keys)):
            errors.append(f"lineage node has duplicate parent edges: {node_key[0]}@{node_key[1]}")
        canonical = sorted(node["input_records"], key=_ref_key)
        if len(input_keys) > 1 and node["input_records"] != canonical:
            errors.append(f"multi-parent lineage inputs are not canonical: {node_key[0]}@{node_key[1]}")
        for ref in node["input_records"]:
            key = _ref_key(ref)
            if key not in known:
                errors.append(f"unresolved lineage input: {key[0]}@{key[1]}")
        if input_keys and node["record_version"] != max(version for _, version in input_keys) + 1:
            errors.append(
                f"lineage node version must equal highest parent version plus one: {node_key[0]}@{node_key[1]}"
            )

    reachable = set(root_keys)
    changed = True
    while changed:
        changed = False
        for key, node in nodes.items():
            if key in reachable:
                continue
            input_keys = {_ref_key(ref) for ref in node["input_records"]}
            if input_keys and input_keys <= reachable:
                reachable.add(key)
                changed = True
    if terminal_key not in reachable:
        errors.append("terminal record is not reachable from every declared root edge")

    ancestors = {terminal_key}
    changed = True
    while changed:
        changed = False
        for key in list(ancestors):
            node = nodes.get(key)
            if node is None:
                continue
            for ref in node["input_records"]:
                parent_key = _ref_key(ref)
                if parent_key not in ancestors:
                    ancestors.add(parent_key)
                    changed = True
    for key in set(nodes) - ancestors:
        errors.append(f"orphan lineage node does not lead to terminal: {key[0]}@{key[1]}")
    for key in set(root_keys) - ancestors:
        errors.append(f"declared root does not lead to terminal: {key[0]}@{key[1]}")
    return errors, nodes


def _seed_ref_and_module(scenario: dict) -> tuple[dict, str | None]:
    seed = scenario["seed_parent_record"]
    seed_ref = _plain_ref(seed)
    modules = [
        run["module"]
        for run in seed["module_runs"]
        if run["status"] == "completed" and run["output_record"] == seed_ref
    ]
    return seed_ref, modules[0] if len(modules) == 1 else None


def _walk_linear_contract(
    nodes: dict[tuple[str, int], dict],
    start_ref: dict,
    modules: list[str],
    label: str,
) -> tuple[list[str], dict]:
    errors: list[str] = []
    current = start_ref
    for module in modules:
        matches = [
            node
            for node in nodes.values()
            if node["module"] == module and node["input_records"] == [current]
        ]
        if len(matches) != 1:
            errors.append(f"{label} requires exactly one {module} child of {_ref_key(current)}")
            break
        current = _plain_ref(matches[0])
    return errors, current


def _validate_mode_contract(scenario: dict, mode: str, result: dict) -> list[str]:
    errors, nodes = _validate_lineage_graph(result)
    lineage = result["lineage"]
    seed_ref, seed_module = _seed_ref_and_module(scenario)
    if lineage["root_records"] != [seed_ref]:
        errors.append(f"{mode} root record must exactly equal the seed ID and version")
    contract = scenario["mode_contract"]

    if mode == "sequential":
        order = contract["sequential_order"]
        if not order or order[0] != seed_module:
            errors.append("sequential contract must begin with the seed-producing module")
            return errors
        if len(nodes) != len(order) - 1:
            errors.append("sequential lineage node count differs from exact module order")
        walk_errors, terminal = _walk_linear_contract(
            nodes, seed_ref, order[1:], "sequential order"
        )
        errors.extend(walk_errors)
    else:
        cluster = contract["clustered"]
        prefix = cluster["prefix_order"]
        if not prefix or prefix[0] != seed_module:
            errors.append("clustered prefix must begin with the seed-producing module")
            return errors
        prefix_errors, branch_parent = _walk_linear_contract(
            nodes, seed_ref, prefix[1:], "clustered prefix"
        )
        errors.extend(prefix_errors)

        siblings: list[dict] = []
        for module in cluster["parallel_modules"]:
            matches = [
                node
                for node in nodes.values()
                if node["module"] == module and node["input_records"] == [branch_parent]
            ]
            if len(matches) != 1:
                errors.append(f"clustered lane requires exactly one {module} child")
            else:
                siblings.append(_plain_ref(matches[0]))
        canonical_siblings = sorted(siblings, key=_ref_key)
        merge_matches = [
            node
            for node in nodes.values()
            if node["module"] == cluster["merge_module"]
            and node["input_records"] == canonical_siblings
            and len(node["input_records"]) >= 2
        ]
        if len(merge_matches) != 1:
            errors.append("clustered lineage requires one exact multi-parent merge")
            terminal = branch_parent
        else:
            merge_ref = _plain_ref(merge_matches[0])
            suffix_errors, terminal = _walk_linear_contract(
                nodes, merge_ref, cluster["suffix_order"], "clustered suffix"
            )
            errors.extend(suffix_errors)
        expected_node_count = (
            len(prefix) - 1
            + len(cluster["parallel_modules"])
            + 1
            + len(cluster["suffix_order"])
        )
        if len(nodes) != expected_node_count:
            errors.append("clustered lineage node count differs from exact topology contract")

    if lineage["terminal_record"] != terminal:
        errors.append(f"{mode} terminal record does not end the exact contracted path")
    return errors


def compare_mode_results(scenario: dict, sequential: dict, clustered: dict) -> list[str]:
    errors: list[str] = []
    expected = scenario["expected"]
    for field in INVARIANT_FIELDS:
        if sequential[field] != expected[field]:
            errors.append(f"sequential {field} differs from frozen expectation")
        if clustered[field] != expected[field]:
            errors.append(f"clustered {field} differs from frozen expectation")
        if sequential[field] != clustered[field]:
            errors.append(f"cross-mode {field} differs")

    seq_lineage = sequential["lineage"]
    clu_lineage = clustered["lineage"]
    if seq_lineage["root_records"] != clu_lineage["root_records"]:
        errors.append("cross-mode lineage roots differ")
    errors.extend(
        f"sequential {error}" for error in _validate_mode_contract(scenario, "sequential", sequential)
    )
    errors.extend(
        f"clustered {error}" for error in _validate_mode_contract(scenario, "clustered", clustered)
    )
    return errors


def validate_frozen_scenarios(data: dict) -> list[str]:
    errors: list[str] = []
    scenarios = data.get("scenarios", [])
    if [scenario.get("id") for scenario in scenarios] != EXPECTED_IDS:
        errors.append("fixtures must contain C01-C03 and K01-K02 in order")
        return errors

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    for scenario in scenarios:
        scenario_id = scenario["id"]
        for field in (
            "kind",
            "prompt",
            "materials",
            "source_ids",
            "seed_parent_record",
            "expected",
            "mode_contract",
            "mode_results",
        ):
            if not scenario.get(field):
                errors.append(f"{scenario_id} missing {field}")
        material_ids = [material["source_id"] for material in scenario["materials"]]
        if scenario["source_ids"] != material_ids:
            errors.append(f"{scenario_id} source_ids do not exactly match materials")
        try:
            validate_method_record(scenario["seed_parent_record"], schema)
        except ValidationError as exc:
            errors.append(f"{scenario_id} seed parent is schema-invalid: {exc.message}")
        else:
            for error in validate_record_semantics(scenario["seed_parent_record"]):
                errors.append(f"{scenario_id} seed parent semantics: {error}")
        expected = scenario["expected"]
        if expected.get("authorization_effect") != "none":
            errors.append(f"{scenario_id} authorization_effect must be none")
        if not expected.get("frozen_facts") or not expected.get("unknowns"):
            errors.append(f"{scenario_id} expected facts and unknowns must be explicit")
        if scenario.get("mode_contract") != CANONICAL_MODE_CONTRACTS[scenario_id]:
            errors.append(f"{scenario_id} mode_contract differs from the canonical mode contract")
        if set(scenario.get("mode_results", {})) != {"sequential", "clustered"}:
            errors.append(f"{scenario_id} mode_results must contain sequential and clustered")
        elif not isinstance(scenario.get("mode_contract"), dict):
            errors.append(f"{scenario_id} mode_contract must be an object")
        else:
            errors.extend(
                f"{scenario_id} {error}"
                for error in compare_mode_results(
                    scenario,
                    scenario["mode_results"]["sequential"],
                    scenario["mode_results"]["clustered"],
                )
            )
    return errors


def main() -> int:
    data = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    errors = validate_frozen_scenarios(data)
    if errors:
        print("Ariadne frozen evaluation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Ariadne frozen evaluation validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
