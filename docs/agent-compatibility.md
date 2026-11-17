# Ariadne 宿主兼容与安装

Ariadne 只安装一个入口：`skills/ariadne-skill/`。这个目录包含主 `SKILL.md`、六条可组合的内部路径、共享方法引用、按需合同库和辅助工具。内部路径不是另外的 Skill；完整安装无需发现或调度其他 `ariadne-*` 入口。

宿主目录只是安装目标。本仓库不保存 `.agent/skills`、`.agents/skills`、`.claude/skills`、`.codex/skills`、`.cursor/skills`、`.gemini/skills`、`.github/skills` 或 `.reasonix/skills` 镜像。兼容等级说明格式、发现位置与调用入口，实际验证状态另行记录。

## 完整单包安装

项目级安装适合审查和试用。只选择自己使用的宿主即可，例如 Codex：

```powershell
npx skills add xi-kari/ariadne-skill --skill ariadne-skill --copy -a codex
```

同时为多个原生宿主安装同一个完整包：

```powershell
npx skills add xi-kari/ariadne-skill --skill ariadne-skill --copy -a codex -a claude-code -a gemini-cli -a cursor -a github-copilot
```

用户希望在多个项目中复用时，可以选择全局安装：

```powershell
npx skills add xi-kari/ariadne-skill --skill ariadne-skill --copy --global -a codex
```

示例使用 `--copy`，Windows 不需要符号链接权限。安装前检查来源；安装后在目标宿主的 Skill 列表或发现界面确认 `ariadne-skill`，并核对包内的路径、引用和工具文件已经复制。只复制 `SKILL.md` 不是完整安装。

不带版本的命令跟随默认分支 `main`。需要复现时，将仓库目标固定到实际审阅的提交。已有稳定 tag `v2.0.0` 是旧十入口版本（2026-10 理论来源、Method Record 2.0），其安装结构与本页的单入口版本不同，应查看对应 tag 的文档。理论版本、记录格式和软件 tag 分别登记；此架构更新本身不创建 tag 或 Release。

## 六宿主矩阵

| 宿主 | 兼容等级 | 项目级发现路径 | 全局发现路径 | 调用差异 | 官方依据 |
|---|---|---|---|---|---|
| Codex | `native-agent-skills` | `.agents/skills` | `~/.agents/skills`；安装工具也可写入 `~/.codex/skills` | 可用 `$ariadne-skill` 显式点名，也可按 `description` 路由 | [Codex Skills](https://developers.openai.com/codex/skills) |
| Claude Code | `native-agent-skills` | `.claude/skills` | `~/.claude/skills` | `/ariadne-skill` 是显式斜杠调用，也支持按描述加载 | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| Gemini CLI | `native-agent-skills` | `.gemini/skills`、`.agents/skills` | `~/.gemini/skills`、`~/.agents/skills` | 用自然语言点名；用 `/skills list` 核对发现，激活时遵循宿主授权提示 | [Gemini CLI Skills](https://geminicli.com/docs/cli/using-agent-skills/) |
| Cursor | `native-agent-skills` | `.cursor/skills`、`.agents/skills`、`.claude/skills`、`.codex/skills` | `~/.cursor/skills`、`~/.agents/skills`、`~/.claude/skills`、`~/.codex/skills` | 可从斜杠菜单调用 `/ariadne-skill`，也可自动发现 | [Cursor Skills](https://cursor.com/docs/context/skills) |
| GitHub Copilot | `native-agent-skills` | `.github/skills`、`.claude/skills`、`.agents/skills` | `~/.copilot/skills`、`~/.agents/skills` | 云端、CLI 与编辑器表面不承诺统一斜杠入口；用自然语言点名并核对所在表面的发现结果 | [GitHub Copilot Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| Reasonix | `directory-compatible-subset` | `.reasonix/skills`、`.agents/skills`、`.agent/skills`、`.claude/skills` | `~/.reasonix/skills`、`~/.agents/skills`、`~/.claude/skills` | 候选显式入口为 `/ariadne-skill`；必须先用 `/skills` 核对发现并完成下列专项冒烟 | [Reasonix Docs](https://reasonix.io/docs/) |

`SKILL.md` 的基础合同来自 [Agent Skills 开放规范](https://agentskills.io/specification)，安装参数与目标适配器来自 [`npx skills`](https://github.com/vercel-labs/skills)。宿主官方文档与安装工具的兼容别名可能不同，以目标宿主实际发现结果为准。格式兼容不证明任务表现或渐进加载已经实测。

## 内部资源加载

唯一入口按当前任务组合 `paths/understand.md`、`discover.md`、`project.md`、`decide.md`、`create.md`、`review.md`。这些路径共享 `references/` 中的方法，并按需读取 `references/library/` 的专业合同。宿主可以直接通过文件工具完成这些读取，不需要跨 Skill 派发。

缺少被选中的内部文件意味着安装或资源访问不完整。应报告具体路径和受影响工作，继续完成独立可完成的部分，并修复安装后再承接依赖；不能宣称缺失内容已经读取或执行。包内 `references/legacy/` 和 Method Record 2.0/2.1 校验工具用于显式旧记录互操作，不要求普通任务填写旧二十字段记录。

## Reasonix 兼容上限

Reasonix 保持 `directory-compatible-subset`，不进入默认 `npx skills` 命令。手动把完整的 `skills/ariadne-skill/` 目录复制到 `.reasonix/skills/ariadne-skill/` 或对应全局位置，再用 `/skills` 核对入口。目录中存在 `SKILL.md` 不能证明渐进读取、内部路径组合或工具运行与原生宿主等价。

用于真实任务前至少完成三项专项冒烟：

- `resource-loading`：能从入口读取包资源清单、共享引用及实际选用的 Markdown/JSON 合同；路径在已安装包内解析。
- `path-routing`：能依据任务选择和组合内部路径；文件不可用时准确说明缺口，不伪造已经运行的步骤。
- `context-growth`：连续工作按需读取相关资源，检查上下文增长和恢复能力，不将整个合同库作为统一前置。

失败时保留实际证据并维持未验证状态，不复制或改写另一套方法内容来隐藏宿主差异。

## 从旧多入口版本迁移

此前安装的九个独立入口可能仍被宿主发现。先确认它们确实来自旧 Ariadne 安装，再使用相应宿主或安装器的卸载方式处理；也可以将这些目录归档到宿主扫描范围之外。旧名称为 `ariadne-framing`、`ariadne-evidence`、`ariadne-scale`、`ariadne-mechanism`、`ariadne-human`、`ariadne-dynamics`、`ariadne-forecast`、`ariadne-choice`、`ariadne-audit`。

新的完整包仍名为 `ariadne-skill`，更新时替换完整目录，并再次核对内部资源。历史任务材料与旧 Method Record 保留在原任务目录，不能当作安装清理对象。开发或验证过程不自动删除用户的全局副本。

## 本仓库的验证边界

开发与评测只按显式入口名或直接仓库路径运行，不把开发副本安装到全局目录。适配器验证检查清单、frontmatter、安装命令、宿主路径、证据 URL、冒烟合同和无镜像边界：

```powershell
python -X utf8 -B scripts/validate_adapters.py
```

该命令不启动外部宿主，也不产生发布或现实授权。工具结果只支持它实际检查的环节。

## 验证状态与通用冒烟合同

`adapters/compatibility.json` 为每个宿主维护 `verification`：当前六宿主均为 `unverified`，`last_verified` 为 null。只有在一次性容器、虚拟机或项目级测试目录中实际完成 `resource-loading`、`path-routing`、`context-growth`，保存命令和观察证据后，才可记录为 `smoke-passed` 并填写日期。模板在 `evals/host-smoke-template.md`。

行为场景可通过 `scripts/run_evals.py` 发送给已配置的宿主并保留转录，评分另行进行。目录发现、格式校验、示例通过和模型实际表现是不同的证据，不互相替代。

## 宿主扩展与工具

`agents/openai.yaml` 提供 Codex 的展示名、短描述和调用策略。其他宿主使用其支持的 Agent Skills 发现方式；本包不附带另一套宿主镜像。Python 辅助工具由实际任务按需调用，运行依赖和可完成范围以工具说明为准；没有运行工具时不声称已经通过工具校验。

## 单文件捆绑版

没有 Agent Skills 目录的宿主可以使用 `dist/ariadne-bundle.md`。它由 `scripts/build_bundle.py` 按架构清单的 bundle 顺序生成，包含主入口、共享方法和六条内部路径；CI 用 `--check` 检查同步。

深层合同库、旧记录资料和 Python 工具不因此自动进入单文件。需要未内嵌资源时，应从可访问的原包读取或说明实际缺口；不能假装已读取合同、保存登记或执行脚本。单文件内容一次性进入上下文，大小以生成文件为准，宿主还需核对可用上下文容量。
