"""The optional host runner must not misreport a continuation as executed."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from scripts import run_evals


def test_composable_scenarios_include_frozen_prompts_and_continuation() -> None:
    source = run_evals.ROOT / "evals/composable-paths-prompts.json"
    frozen = json.loads(source.read_text(encoding="utf-8"))
    loaded = [scenario for scenario in run_evals.load_scenarios() if scenario["source"] == source.name]
    assert len(loaded) == len(frozen["scenarios"])
    assert [item["prompt"] for item in loaded] == [item["prompt"] for item in frozen["scenarios"]]
    assert all(item["skill"] == "ariadne-skill" for item in loaded)
    assert all(item["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest() for item in loaded)
    continuation = next(item for item in loaded if item["id"].endswith(":T03"))
    assert continuation["followup"] == frozen["scenarios"][2]["followup"]
    assert continuation["requires_multi_turn"] is True
    assert continuation["rubric"] == "evals/composable-paths-rubric.md"


def test_runner_never_starts_a_host_for_multi_turn_scenario(monkeypatch) -> None:
    def unexpected_host(*args, **kwargs):
        raise AssertionError("multi-turn scenario must not start a single-call host")
    monkeypatch.setattr(run_evals.subprocess, "run", unexpected_host)
    result = run_evals.run_scenario({"prompt": "First turn", "followup": "Correction", "requires_multi_turn": True}, "host {prompt}", 30)
    assert result["status"] == "skipped"
    assert result["skip_reason"] == "requires_multi_turn"
    assert "stdout" not in result


def test_skipped_continuation_is_recorded_without_a_score(tmp_path: Path, monkeypatch) -> None:
    scenario = {
        "id": "composable-paths:T03", "source": "composable-paths-prompts.json",
        "skill": "ariadne-skill", "prompt": "First turn", "followup": "Correction",
        "required_product": "A changed artifact and preserved history",
        "requires_multi_turn": True, "rubric": "evals/composable-paths-rubric.md",
        "source_sha256": "a" * 64,
    }
    monkeypatch.setattr(run_evals, "ROOT", tmp_path)
    monkeypatch.setattr(run_evals, "load_scenarios", lambda: [scenario])
    monkeypatch.setattr(sys, "argv", ["run_evals.py", "--host-command", "unused {prompt}"])
    assert run_evals.main() == 0
    run_dir = next((tmp_path / "evals/runs").iterdir())
    transcript = json.loads((run_dir / "composable-paths-T03.json").read_text(encoding="utf-8"))
    assert transcript["status"] == "skipped"
    assert transcript["followup"] == "Correction"
    sheet = json.loads((run_dir / "scoring-sheet.json").read_text(encoding="utf-8"))
    entry = sheet["scenarios"][0]
    assert entry["status"] == "skipped"
    assert entry["scores"] == {}
    assert entry["rubric"] == scenario["rubric"]
    assert entry["source_sha256"] == scenario["source_sha256"]


def test_list_and_dry_run_explicitly_mark_continuations(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["run_evals.py", "--list", "--only", "T03"])
    assert run_evals.main() == 0
    assert "requires_multi_turn" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["run_evals.py", "--dry-run", "--host-command", "host {prompt}", "--only", "T03"])
    assert run_evals.main() == 0
    assert "SKIP requires_multi_turn" in capsys.readouterr().out
