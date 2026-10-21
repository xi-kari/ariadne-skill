"""Execute the behavioral eval scenarios through a host CLI and collect transcripts.

The repository gates only lint structure; this harness runs the actual prompts.
It shells each scenario prompt out to a host command template, saves the raw
transcript, and writes a rubric scoring sheet (F1-F11 from evals/rubric.md) with
null scores for a human or judge model to fill in. Scoring is deliberately not
automated and this script is not a CI gate.

Examples:

    python scripts/run_evals.py --list
    python scripts/run_evals.py --dry-run
    python scripts/run_evals.py --host-command "claude -p {prompt}" --only ariadne-framing
    python scripts/run_evals.py --host-command "codex exec {prompt}"

The host must already discover the skills (project-level install in the working
directory you launch from, or a global install of a released copy). Outputs go
to evals/runs/<UTC timestamp>/ which is gitignored; move a finished, scored
sheet next to the scenarios only when you want to freeze it as evidence.
"""
from __future__ import annotations

import argparse
import datetime as _dt
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
)
RUBRIC_ITEMS = ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11")
TABLE_ROW = re.compile(r"^\|\s*`?([^|`]+)`?\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$")


def load_scenarios() -> list[dict]:
    scenarios: list[dict] = []
    for path in SCENARIO_FILES:
        if not path.is_file():
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
                }
            )
    return scenarios


def run_scenario(scenario: dict, host_command: str, timeout: int) -> dict:
    command = [
        part.replace("{prompt}", scenario["prompt"]) for part in shlex.split(host_command)
    ]
    try:
        completed = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout, encoding="utf-8"
        )
        return {
            "command": command,
            "exit_code": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }
    except FileNotFoundError:
        return {"command": command, "exit_code": None, "error": "host command not found"}
    except subprocess.TimeoutExpired:
        return {"command": command, "exit_code": None, "error": f"timeout after {timeout}s"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--host-command", help='template with {prompt}, e.g. "claude -p {prompt}"')
    parser.add_argument("--only", help="run only scenarios whose skill or id contains this text")
    parser.add_argument("--timeout", type=int, default=300, help="seconds per scenario")
    parser.add_argument("--list", action="store_true", help="list scenarios and exit")
    parser.add_argument("--dry-run", action="store_true", help="show commands without executing")
    args = parser.parse_args()

    scenarios = load_scenarios()
    if args.only:
        needle = args.only.lower()
        scenarios = [
            scenario
            for scenario in scenarios
            if needle in scenario["skill"].lower() or needle in scenario["id"].lower()
        ]
    if not scenarios:
        print("no scenarios matched")
        return 1
    if args.list:
        for scenario in scenarios:
            print(f"{scenario['id']}  {scenario['skill']}  {scenario['prompt'][:60]}")
        return 0
    if not args.host_command:
        parser.error("--host-command is required unless --list is used")
    if args.dry_run:
        for scenario in scenarios:
            rendered = args.host_command.replace("{prompt}", scenario["prompt"])
            print(f"{scenario['id']}: {rendered}")
        return 0

    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = ROOT / "evals" / "runs" / stamp
    run_dir.mkdir(parents=True, exist_ok=False)
    sheet = []
    for scenario in scenarios:
        print(f"running {scenario['id']} ({scenario['skill']}) ...")
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
                "scores": {item: None for item in RUBRIC_ITEMS},
                "scored_by": None,
                "notes": "",
            }
        )
    (run_dir / "scoring-sheet.json").write_text(
        json.dumps(
            {
                "host_command": args.host_command,
                "run": stamp,
                "rubric": "evals/rubric.md (score each item 0/1/2; scoring stays human or judge-model work)",
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
