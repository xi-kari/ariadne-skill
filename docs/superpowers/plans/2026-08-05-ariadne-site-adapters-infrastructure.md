# Ariadne Site, Agent Adapters, and Infrastructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Testing may run throughout; formal content, visual, compatibility, and governance review begins only after `ARIADNE_EXTENSION_CONTENT_COMPLETE`.

**Goal:** Publish the Chinese Ariadne website, distribute the ten canonical Skills across six agent hosts, and add a minimal reproducible repository delivery pipeline.

**Architecture:** Keep `skills/` as the only methodology source. Build a dependency-free static site from `site/` plus shared SVG assets with Python, describe host differences in one machine-readable adapter manifest and one Chinese guide, and gate Pages deployment behind the repository's existing Python validation layer.

**Tech Stack:** HTML5, CSS, progressive JavaScript, Python 3.10 standard library, pytest 9.1.1, jsonschema 4.26.0, PyYAML 6.0.2, GitHub Actions, GitHub Pages.

## Global Constraints

- Work only in `codex/ariadne-site-adapters-infra` at `E:\世界模型\skill\ariadne-skill\.worktrees\ariadne-site-adapters-infra`.
- Preserve all ten `skills/ariadne-*` directories as the unique methodology authority; do not duplicate or rewrite their contracts.
- Use MIT License with `Copyright (c) 2026 xi-kari`.
- Do not add Node, a frontend framework, third-party runtime assets, analytics, cookies, a Release, a tag, or a package publication.
- Keep `authorization_effect: none` and `RELEASE: not_authorized` unchanged.
- Default public installation is the complete ten-Skill bundle; a router-only install is an explicitly documented degraded mode.
- Test while building, but do not begin formal module-by-module review. Build every planned site, adapter, documentation, workflow, and governance file first.
- After content completion, run three independent read-only reviews in parallel, then make one consolidated repair pass.

---

### Task 1: Freeze extension contracts in RED tests

**Files:**
- Create: `tests/test_extension_contracts.py`
- Create: `tests/test_content_quality.py`

**Interfaces:**
- Consumes: current ten-Skill repository at `main@8d632c4`.
- Produces: required interfaces `build_site(repo_root: Path, output_root: Path) -> Path`, `validate_content(repo_root: Path) -> list[str]`, and `validate_adapters(repo_root: Path) -> list[str]`.

- [ ] **Step 1: Write the failing site and build contract**

```python
from pathlib import Path

from scripts.build_site import build_site

ROOT = Path(__file__).resolve().parents[1]


def test_build_site_emits_complete_static_artifact(tmp_path: Path) -> None:
    output = build_site(ROOT, tmp_path / "site")
    expected = {
        "index.html",
        "404.html",
        "assets/site.css",
        "assets/site.js",
        "assets/favicon.svg",
        "assets/og-cover.svg",
        "assets/readme-hero.svg",
        "assets/lattice-kernel-map.svg",
    }
    assert expected <= {
        path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file()
    }
```

- [ ] **Step 2: Write the failing adapter and infrastructure contracts**

```python
EXPECTED_HOSTS = {"codex", "claude-code", "gemini-cli", "cursor", "github-copilot", "reasonix"}
EXPECTED_SKILLS = {"ariadne-skill", "ariadne-framing", "ariadne-evidence", "ariadne-scale", "ariadne-mechanism", "ariadne-human", "ariadne-dynamics", "ariadne-forecast", "ariadne-choice", "ariadne-audit"}


def test_adapter_manifest_is_complete() -> None:
    data = json.loads((ROOT / "adapters" / "compatibility.json").read_text(encoding="utf-8"))
    assert {host["id"] for host in data["hosts"]} == EXPECTED_HOSTS
    assert set(data["skills"]) == EXPECTED_SKILLS
    assert data["default_bundle"] == "complete"


def test_delivery_files_exist() -> None:
    for relative in REQUIRED_DELIVERY_FILES:
        assert (ROOT / relative).is_file(), relative
```

- [ ] **Step 3: Write focused quality fixtures**

Test a missing relative target, a missing explicit anchor, a link inside a code fence, invalid SVG XML, missing SVG accessible text, trailing whitespace, a missing final newline, an external runtime asset, and a path that escapes the repository. Each fixture must assert the exact error code returned by `validate_content`.

- [ ] **Step 4: Run RED tests**

Run:

```powershell
python -X utf8 -B -m pytest -q -p no:cacheprovider tests/test_extension_contracts.py tests/test_content_quality.py
```

Expected: FAIL during collection because `scripts.build_site` and `scripts.content_quality` do not exist.

- [ ] **Step 5: Commit the RED boundary**

```powershell
git add tests/test_extension_contracts.py tests/test_content_quality.py
git commit -m "test: freeze Ariadne extension contracts"
```

---

### Task 2: Build the complete static website

**Files:**
- Create: `site/index.html`
- Create: `site/404.html`
- Create: `site/assets/site.css`
- Create: `site/assets/site.js`
- Create: `site/assets/favicon.svg`
- Create: `site/assets/og-cover.svg`
- Create: `scripts/build_site.py`
- Modify: `.gitignore`

**Interfaces:**
- Consumes: `docs/assets/readme-hero.svg`, `docs/assets/lattice-kernel-map.svg`, and the ten canonical Skill contracts.
- Produces: `build_site(repo_root: Path, output_root: Path) -> Path`; output is a self-contained static directory with no external runtime dependency.

- [ ] **Step 1: Implement the safe builder**

```python
SHARED_ASSETS = ("readme-hero.svg", "lattice-kernel-map.svg")


def build_site(repo_root: Path, output_root: Path) -> Path:
    repo_root = repo_root.resolve()
    source = repo_root / "site"
    output_root = output_root.resolve()
    if output_root == repo_root or repo_root in output_root.parents and output_root.name == ".git":
        raise ValueError("unsafe site output path")
    if output_root.exists():
        shutil.rmtree(output_root)
    shutil.copytree(source, output_root)
    for name in SHARED_ASSETS:
        shutil.copy2(repo_root / "docs" / "assets" / name, output_root / "assets" / name)
    return output_root
```

Add a CLI with `--output` defaulting to `build/site`; reject an output outside the repository unless the caller passes an explicit temporary path through the Python function.

- [ ] **Step 2: Write the complete Chinese page in one content pass**

Include Hero, the `10 / 1+9 / 5 / 0` fact ledger, the Lattice Kernel map, all ten five-field module cards, five execution modes, Method Record and ceilings, the six-host compatibility table, project/global installation blocks, boundaries, sources, MIT, and GitHub links. Preserve the approved phrase “一套让 AI Agent 思考和处理复杂问题的方法论集群。”

- [ ] **Step 3: Implement the approved visual system**

Use the exact palette from the spec, system serif/monospace fallbacks, sticky navigation, a reading-progress line, an optional wide-screen “方法导航 · 按需选取” rail, responsive single-column cards, visible focus, and `prefers-reduced-motion`. Purple and copper are decorative accents, not small body text.

- [ ] **Step 4: Add progressive JavaScript**

```javascript
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
document.querySelectorAll("[data-copy]").forEach((button) => {
  button.addEventListener("click", async () => {
    const value = button.getAttribute("data-copy");
    if (navigator.clipboard?.writeText) await navigator.clipboard.writeText(value);
  });
});
```

Also update reading progress through `requestAnimationFrame` and reveal sections only when motion is allowed. Text remains visible by default so a JavaScript failure cannot hide content.

- [ ] **Step 5: Add local assets and error page**

Create an Ariadne “A” lattice favicon, an SVG Open Graph cover, and a Chinese 404 page linking back with `./`. Do not copy the CrossFrame seal, numbers, runtime chain, or colors.

- [ ] **Step 6: Run the website contract**

```powershell
python -X utf8 -B scripts/build_site.py --output build/site
python -X utf8 -B -m pytest -q -p no:cacheprovider tests/test_extension_contracts.py -k site
```

Expected: build succeeds and the site artifact test passes.

- [ ] **Step 7: Commit the complete website content**

```powershell
git add .gitignore site scripts/build_site.py
git commit -m "feat: build Ariadne methodology website"
```

---

### Task 3: Add the complete multi-agent adapter layer

**Files:**
- Create: `adapters/compatibility.json`
- Create: `docs/agent-compatibility.md`
- Create: `scripts/validate_adapters.py`
- Modify: `README.md`

**Interfaces:**
- Consumes: ten canonical Skill directories and official host documentation links frozen in the design spec.
- Produces: `validate_adapters(repo_root: Path) -> list[str]` and a six-host installation matrix.

- [ ] **Step 1: Create the machine-readable compatibility manifest**

Use this shape for every host:

```json
{
  "id": "reasonix",
  "name": "Reasonix",
  "compatibility": "directory-compatible-subset",
  "project_paths": [".reasonix/skills", ".agents/skills", ".agent/skills", ".claude/skills"],
  "global_paths": ["~/.reasonix/skills", "~/.agents/skills", "~/.claude/skills"],
  "invocation": "/ariadne-skill",
  "evidence_url": "https://reasonix.io/docs/",
  "required_smoke_checks": ["json-references", "peer-routing", "context-growth"]
}
```

Mark Codex, Claude Code, Gemini CLI, Cursor, and GitHub Copilot as `native-agent-skills`; Reasonix remains the subset level.

- [ ] **Step 2: Implement adapter validation**

Validate exact host and Skill sets, unique IDs, existing Skill directories, valid basic frontmatter, HTTPS evidence URLs, complete project/global paths, and the three Reasonix smoke checks. Reject any copied `.agents/skills`, `.claude/skills`, or `.reasonix/skills` mirror inside this source repository.

- [ ] **Step 3: Write the Chinese compatibility guide**

Document discovery paths, invocation differences, full-bundle installation, router-only degradation, Windows `--copy`, rolling `main` semantics, and Reasonix's non-equivalence. Use the public commands:

```powershell
npx skills add xi-kari/ariadne-skill --skill '*' --copy -a codex -a claude-code -a gemini-cli -a cursor -a github-copilot -a reasonix
npx skills add xi-kari/ariadne-skill --skill '*' --copy --global -a codex -a claude-code -a gemini-cli -a cursor -a github-copilot -a reasonix
```

- [ ] **Step 4: Add website and adapter entry points to README**

Add the public website URL, compatibility guide, install commands, and a clear statement that no stable tag exists. Preserve the current explicit local-testing and Release boundaries.

- [ ] **Step 5: Run adapter tests**

```powershell
python -X utf8 -B scripts/validate_adapters.py
python -X utf8 -B -m pytest -q -p no:cacheprovider tests/test_extension_contracts.py -k adapter
```

Expected: both commands pass and no mirror directory is created.

- [ ] **Step 6: Commit the adapter layer**

```powershell
git add adapters docs/agent-compatibility.md scripts/validate_adapters.py README.md
git commit -m "feat: document Ariadne agent compatibility"
```

---

### Task 4: Add repository delivery infrastructure

**Files:**
- Create: `LICENSE`
- Create: `requirements-dev.txt`
- Create: `.editorconfig`
- Create: `.gitattributes`
- Create: `.github/workflows/validate-and-deploy.yml`
- Create: `.github/dependabot.yml`
- Create: `.github/ISSUE_TEMPLATE/config.yml`
- Create: `.github/ISSUE_TEMPLATE/bug.yml`
- Create: `.github/ISSUE_TEMPLATE/methodology.yml`
- Create: `.github/pull_request_template.md`
- Create: `CONTRIBUTING.md`
- Create: `SECURITY.md`

**Interfaces:**
- Consumes: `requirements-dev.txt`, the three validation commands, and `build/site`.
- Produces: required `validate` status check and conditional `deploy` job.

- [ ] **Step 1: Add reproducible local metadata**

Pin exactly:

```text
jsonschema==4.26.0
PyYAML==6.0.2
pytest==9.1.1
```

Use UTF-8, LF in Git, four-space Python indentation, two-space YAML/JSON indentation, final newlines, and `build/` ignored.

- [ ] **Step 2: Add MIT License and contribution/security entry points**

Use the standard MIT text and `Copyright (c) 2026 xi-kari`. `SECURITY.md` directs private security reports to GitHub private vulnerability reporting and forbids including secrets or personal case material in public issues. `CONTRIBUTING.md` requires tests, contract boundaries, and whole-suite review timing.

- [ ] **Step 3: Add focused issue and PR templates**

The bug form requests version, host, exact Skill, reproduction, expected/actual behavior, and redacted logs. The methodology form requests source clause, counterexample, affected module, proposed downgrade, and privacy confirmation. Disable blank issues. The PR template records tests, changed contracts, site impact, compatibility impact, and Release-boundary confirmation.

- [ ] **Step 4: Add pinned CI and Pages deployment**

Use these immutable Action commits:

```yaml
- uses: actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803 # v6
- uses: actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1 # v6
- uses: actions/configure-pages@983d7736d9b0ae728b81ab479565c72886d7745b # v5
- uses: actions/upload-pages-artifact@7b1f4a764d45c48632c6b24a0339c27f5614fb0b # v4
- uses: actions/deploy-pages@d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e # v4
```

The `validate` job runs Python 3.10, installs the pinned requirements, runs all tests and validators, and builds `build/site` with `contents: read`. The `deploy` job has `needs: validate`, runs only for a `push` to `main`, uploads only `build/site`, and owns `pages: write` plus `id-token: write` in the `github-pages` environment.

- [ ] **Step 5: Add monthly Dependabot**

Configure separate monthly groups for `pip` at `/` and `github-actions` at `/`; limit open pull requests to two per ecosystem.

- [ ] **Step 6: Run infrastructure static contracts**

```powershell
python -X utf8 -B -m pytest -q -p no:cacheprovider tests/test_extension_contracts.py -k infrastructure
python -X utf8 -B scripts/build_site.py --output build/site
```

Expected: delivery files exist, action pins and permissions match, and the build succeeds.

- [ ] **Step 7: Commit infrastructure**

```powershell
git add LICENSE requirements-dev.txt .editorconfig .gitattributes .github CONTRIBUTING.md SECURITY.md .gitignore
git commit -m "ci: add Ariadne delivery infrastructure"
```

---

### Task 5: Integrate whole-repository quality gates

**Files:**
- Create: `scripts/content_quality.py`
- Modify: `scripts/validate_repo.py`
- Modify: `tests/test_content_quality.py`
- Modify: `tests/test_extension_contracts.py`

**Interfaces:**
- Consumes: the completed site, adapter manifest, README, docs, SVG, workflow, and community files.
- Produces: `validate_content(repo_root: Path) -> list[str]`; `validate_repo.py` is the single local/CI repository entry point.

- [ ] **Step 1: Implement deterministic content validation**

Return stable codes for `missing-target`, `missing-anchor`, `invalid-svg`, `missing-svg-accessibility`, `external-runtime-asset`, `path-escape`, `invalid-utf8`, `trailing-whitespace`, and `missing-final-newline`. Ignore Markdown links inside fenced and inline code. Check local HTML `href`/`src`, explicit HTML anchors, and Markdown heading slugs used by README/docs.

- [ ] **Step 2: Wire all validators into the repository entry point**

```python
from build_site import build_site
from content_quality import validate_content
from validate_adapters import validate_adapters


def validate_extension_contracts() -> list[str]:
    errors = validate_content(ROOT)
    errors.extend(validate_adapters(ROOT))
    with tempfile.TemporaryDirectory() as temp_dir:
        build_site(ROOT, Path(temp_dir) / "site")
    return errors
```

Append these errors to the existing repository errors without changing existing Skill, Method Record, source-coverage, or Release checks.

- [ ] **Step 3: Complete false-positive tests**

Verify code-fence and inline-code pseudo-links do not fail, query strings and fragments resolve correctly, external HTTPS links are recorded but not fetched, and generated `build/` is excluded from source scans.

- [ ] **Step 4: Run focused GREEN tests**

```powershell
python -X utf8 -B -m pytest -q -p no:cacheprovider tests/test_content_quality.py tests/test_extension_contracts.py
python -X utf8 -B scripts/validate_repo.py
```

Expected: all focused tests pass and repository validation includes site and adapter checks.

- [ ] **Step 5: Commit integrated gates**

```powershell
git add scripts/content_quality.py scripts/validate_repo.py tests/test_content_quality.py tests/test_extension_contracts.py
git commit -m "test: validate Ariadne site and adapters"
```

---

### Task 6: Cross the whole-extension content-complete gate

**Files:**
- Modify only if a missing item is found: files listed in Tasks 2–5.

**Interfaces:**
- Consumes: all completed content from Tasks 2–5.
- Produces: the process gate `ARIADNE_EXTENSION_CONTENT_COMPLETE`; it is not a truth, Release, or authorization claim.

- [ ] **Step 1: Verify every planned path exists**

Run a repository script or PowerShell list against every Create path in Tasks 2–5. Expected: zero missing files and no platform mirror directories.

- [ ] **Step 2: Run the complete pre-review suite**

```powershell
python -X utf8 -B -m pytest -q -p no:cacheprovider
python -X utf8 -B scripts/validate_repo.py
python -X utf8 -B scripts/validate_evals.py
python -X utf8 -B scripts/validate_adapters.py
python -X utf8 -B scripts/build_site.py --output build/site
git diff --check
```

Expected: every command passes. Only after this result declare `ARIADNE_EXTENSION_CONTENT_COMPLETE` in the task progress report.

- [ ] **Step 3: Commit any completion-only corrections**

If Step 1 or 2 required corrections, commit them together as:

```powershell
git add site scripts/build_site.py adapters docs/agent-compatibility.md scripts/validate_adapters.py README.md LICENSE requirements-dev.txt .editorconfig .gitattributes .github CONTRIBUTING.md SECURITY.md .gitignore scripts/content_quality.py scripts/validate_repo.py tests/test_content_quality.py tests/test_extension_contracts.py
git commit -m "fix: complete Ariadne extension content"
```

Do not start formal review before this gate.

---

### Task 7: Run unified parallel review after content completion

**Files:**
- Read-only review of all branch changes against `8d632c4`.

**Interfaces:**
- Consumes: the content-complete branch and full passing evidence.
- Produces: three evidence-backed finding lists, with severity and exact file/line references.

- [ ] **Step 1: Dispatch website review**

Review semantic HTML, responsive behavior, keyboard access, reduced motion, contrast, external requests, progressive enhancement, brand isolation, and fidelity to the approved reference rhythm.

- [ ] **Step 2: Dispatch adapter review**

Re-read current official contracts for Codex, Claude Code, Gemini CLI, Cursor, GitHub Copilot, Reasonix, and the selected install CLI. Check every path, command, compatibility ceiling, and evidence link without editing files.

- [ ] **Step 3: Dispatch infrastructure/security review**

Review Action pins, permissions, triggers, artifact scope, dependency pins, templates, private-reporting instructions, license, validators, path handling, and Release boundary without editing files.

- [ ] **Step 4: Merge findings without voting**

Deduplicate exact findings, preserve disagreements, reject scope expansion, and create one repair ledger ordered by P0/P1/P2/P3. A clean reviewer must explicitly state no actionable findings.

---

### Task 8: Repair, verify, publish, and enable repository settings

**Files:**
- Modify: only files tied to accepted Task 7 findings.
- Create no Release/tag/package files.

**Interfaces:**
- Consumes: unified repair ledger.
- Produces: reviewed branch, PR, merged `main`, live Pages site, and verified repository settings.

- [ ] **Step 1: Add regression tests for every accepted behavioral finding**

Run each focused test to RED before its fix; documentation-only wording findings may use an exact text assertion instead of a runtime test.

- [ ] **Step 2: Apply one consolidated repair pass**

Use `apply_patch` for edits. Do not reopen completed content for unrelated redesign.

- [ ] **Step 3: Run final local verification**

```powershell
python -X utf8 -B -m pip install -r requirements-dev.txt
python -X utf8 -B -m pytest -q -p no:cacheprovider
python -X utf8 -B scripts/validate_repo.py
python -X utf8 -B scripts/validate_evals.py
python -X utf8 -B scripts/validate_adapters.py
python -X utf8 -B scripts/build_site.py --output build/site
git diff --check
git status --short --branch
```

- [ ] **Step 4: Verify the built site in the in-app browser**

Serve `build/site` on localhost, then check desktop and mobile viewports, section navigation, three copy buttons, zero console errors, and no non-GitHub external runtime requests. Keep screenshots as task evidence, not committed artifacts.

- [ ] **Step 5: Commit repairs and push the branch**

```powershell
git add site scripts adapters docs/agent-compatibility.md README.md LICENSE requirements-dev.txt .editorconfig .gitattributes .github CONTRIBUTING.md SECURITY.md .gitignore tests
git commit -m "fix: close Ariadne extension review findings"
git push -u origin codex/ariadne-site-adapters-infra
```

- [ ] **Step 6: Create the PR and wait for `validate`**

Create a ready PR describing RED/GREEN evidence, content-complete-before-review timing, six-host compatibility, and unchanged Release boundary. Verify with `gh pr checks --watch` and `gh run view --exit-status`.

- [ ] **Step 7: Merge only after the required check passes**

Merge the PR, update local `main`, and verify local/remote SHA parity. Do not create a tag or Release.

- [ ] **Step 8: Enable Pages and repository settings**

```powershell
'{"build_type":"workflow"}' | gh api --method POST repos/xi-kari/ariadne-skill/pages --input -
gh api --method PUT repos/xi-kari/ariadne-skill/private-vulnerability-reporting
gh repo edit xi-kari/ariadne-skill --enable-wiki=false --enable-projects=false --homepage='https://xi-kari.github.io/ariadne-skill/'
```

Create an active repository ruleset for `~DEFAULT_BRANCH` with `deletion`, `non_fast_forward`, `pull_request` with zero required approvals, and `required_status_checks` containing context `validate` with strict checks enabled. Use the current repository rules API schema from the official documentation at execution time.

- [ ] **Step 9: Verify live state**

Confirm the Pages API reports `build_type: workflow`, the site returns HTTP 200, the homepage URL is correct, the ruleset is active, private vulnerability reporting is enabled, Wiki/Projects are disabled, CrossFrame Pages remains unchanged, tests on `main` pass, and tags/releases remain empty.
