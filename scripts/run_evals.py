"""Execute the behavioral eval scenarios through a host CLI and collect transcripts.

The repository gates only lint structure; this harness runs the actual prompts.
It shells each scenario prompt out to a host command template, saves the raw
transcript, and writes a scoring sheet referring to each suite's rubric with
null scores for a human or judge model to fill in. Cases with follow-up turns
are recorded as skipped: they require a separate session-preserving execution.
Scoring is deliberately not automated and this script is not a CI gate.

Examples:

    python scripts/run_evals.py --list
    python scripts/run_evals.py --dry-run --host-command "claude -p {prompt}"
    python scripts/run_evals.py --host-command "claude -p {prompt}" --only composable-paths:T01
    python scripts/run_evals.py --host-command "codex exec {prompt}"

Use a disposable task directory with the single Ariadne package available to
the host. Prepare any fixtures required by the case before execution; the runner
does not create them or verify artifacts. Do not globally install this clone.
The host command inherits the directory you launch from. Outputs go
to evals/runs/<UTC timestamp>/ which is gitignored; move a finished, scored
sheet next to the scenarios only when you want to freeze it as evidence.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIO_FILES = (
    ROOT / "evals" / "standalone-scenarios.md",
    ROOT / "evals" / "chain-scenarios.md",
    ROOT / "evals" / "v2-methodology-scenarios.md",
    ROOT / "evals" / "composable-paths-prompts.json",
)
RUBRIC_ITEMS = ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11")
TABLE_ROW = re.compile(r"^\|\s*`?([^|`]+)`?\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$")


def load_scenarios() -> list[dict]:
    scenarios: list[dict] = []
    for path in SCENARIO_FILES:
        if not path.is_file():
            continue
        if path.suffix == ".json":
            raw = path.read_bytes()
            data = json.loads(raw)
            for item in data["scenarios"]:
                scenarios.append(
                    {
                        "id": f"composable-paths:{item['id']}",
                        "source": path.name,
                        "source_sha256": hashlib.sha256(raw).hexdigest(),
                        "suite": data["suite"],
                        "skill": "ariadne-skill",
                        "prompt": item["prompt"],
                        "followup": item.get("followup"),
                        "requires_multi_turn": bool(item.get("followup")),
                        "required_product": f"Case {item['id']} in evals/composable-paths-rubric.md",
                        "rubric": "evals/composable-paths-rubric.md",
                    }
                )
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            match = TABLE_ROW.match(line.strip())
            if match is None:
                continue
            skill, prompt, product = (cell.strip() for cell in match.groups())
            if skill in {"Skill", "Scenario", "---"} or set(skill) <= {"-", " "}:
                continue
            prompt = prompt.strip("“”\"")
            scenarios.append(
                {
                    "id": f"{path.stem}:{len(scenarios) + 1:02d}",
                    "source": path.name,
                    "skill": skill,
                    "prompt": prompt,
                    "required_product": product,
                    "rubric": "evals/rubric.md",
                }
            )
    return scenarios


def run_scenario(scenario: dict, host_command: str, timeout: int) -> dict:
    if scenario.get("requires_multi_turn") or scenario.get("followup"):
        return {
            "status": "skipped",
            "skip_reason": "requires_multi_turn",
            "note": "Run the initial prompt and follow-up in one persistent session; this single-call runner executed neither turn.",
        }
    command = [
        part.replace("{prompt}", scenario["prompt"]) for part in shlex.split(host_command)
    ]
    try:
        completed = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout, encoding="utf-8"
        )
        return {
            "status": "completed" if completed.returncode == 0 else "failed",
            "command": command,
            "exit_code": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }
    except FileNotFoundError:
        return {"status": "failed", "command": command, "exit_code": None, "error": "host command not found"}
    except subprocess.TimeoutExpired:
        return {"status": "failed", "command": command, "exit_code": None, "error": f"timeout after {timeout}s"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--host-command", help='template with {prompt}, e.g. "claude -p {prompt}"')
    parser.add_argument("--only", help="filter skill, id, or source (e.g. composable-paths:T01); multi-turn cases are recorded as skipped")
    parser.add_argument("--timeout", type=int, default=300, help="seconds per scenario")
    parser.add_argument("--list", action="store_true", help="list scenarios and exit")
    parser.add_argument("--dry-run", action="store_true", help="show single-turn commands and multi-turn skip notices without executing")
    args = parser.parse_args()

    scenarios = load_scenarios()
    if args.only:
        needle = args.only.lower()
        scenarios = [
            scenario
            for scenario in scenarios
            if any(needle in scenario[key].lower() for key in ("skill", "id", "source"))
        ]
    if not scenarios:
        print("no scenarios matched")
        return 1
    if args.list:
        for scenario in scenarios:
            mode = " [requires_multi_turn]" if scenario.get("requires_multi_turn") else ""
            print(f"{scenario['id']}  {scenario['skill']}{mode}  {scenario['prompt'][:60]}")
        return 0
    if not args.host_command:
        parser.error("--host-command is required unless --list is used")
    if args.dry_run:
        for scenario in scenarios:
            if scenario.get("requires_multi_turn") or scenario.get("followup"):
                print(f"{scenario['id']}: SKIP requires_multi_turn; use a persistent session for both turns")
                continue
            rendered = args.host_command.replace("{prompt}", scenario["prompt"])
            print(f"{scenario['id']}: {rendered}")
        return 0

    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = ROOT / "evals" / "runs" / stamp
    run_dir.mkdir(parents=True, exist_ok=False)
    sheet = []
    for scenario in scenarios:
        activity = "skipping" if scenario.get("requires_multi_turn") or scenario.get("followup") else "running"
        print(f"{activity} {scenario['id']} ({scenario['skill']}) ...")
        result = run_scenario(scenario, args.host_command, args.timeout)
        slug = scenario["id"].replace(":", "-")
        (run_dir / f"{slug}.json").write_text(
            json.dumps({**scenario, **result}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        sheet.append(
            {
                "id": scenario["id"],
                "skill": scenario["skill"],
                "required_product": scenario["required_product"],
                "transcript": f"{slug}.json",
                "status": result["status"],
                "skip_reason": result.get("skip_reason"),
                "source_sha256": scenario.get("source_sha256"),
                "rubric": scenario["rubric"],
                "scores": {} if result["status"] == "skipped" else (
                    {"result": None} if scenario["rubric"] == "evals/composable-paths-rubric.md"
                    else {item: None for item in RUBRIC_ITEMS}
                ),
                "scored_by": None,
                "notes": result.get("note", ""),
            }
        )
    (run_dir / "scoring-sheet.json").write_text(
        json.dumps(
            {
                "host_command": args.host_command,
                "run": stamp,
                "scoring": "Use each scenario's rubric: F1-F11 use 0/1/2; composable paths use pass/partial/fail. Completed means the CLI returned zero, not that behavior passed. Skipped cases have no scores.",
                "scenarios": sheet,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"transcripts and scoring sheet written to {run_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
