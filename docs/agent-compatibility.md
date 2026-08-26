# Ariadne 多智能体兼容与安装

Ariadne 以仓库中的十个 `skills/ariadne-*/` 目录为唯一方法论权威源。宿主目录只是安装目标；本仓库不保存 `.agent/skills`、`.agents/skills`、`.claude/skills`、`.codex/skills`、`.cursor/skills`、`.gemini/skills`、`.github/skills` 或 `.reasonix/skills` 镜像。

兼容等级描述 Skill 格式、发现位置与调用入口，不代表已在每个宿主、版本和运行表面完成真实任务验证。默认安装完整十 Skill；只安装总路由是有记录的降级模式。

## 默认完整包

完整包包括：

1. `ariadne-skill`
2. `ariadne-framing`
3. `ariadne-evidence`
4. `ariadne-scale`
5. `ariadne-mechanism`
6. `ariadne-human`
7. `ariadne-dynamics`
8. `ariadne-forecast`
9. `ariadne-choice`
10. `ariadne-audit`

项目级安装把 Skill 复制到当前项目的宿主发现目录，适合审查和试用：

```powershell
npx skills add xi-kari/ariadne-skill --skill '*' --copy -a codex -a claude-code -a gemini-cli -a cursor -a github-copilot
```

全局安装让同一用户在多个项目中发现 Skill：

```powershell
npx skills add xi-kari/ariadne-skill --skill '*' --copy --global -a codex -a claude-code -a gemini-cli -a cursor -a github-copilot
```

Windows 示例固定使用 `--copy`，不依赖符号链接权限。运行安装命令前应检查来源；运行后应使用目标宿主的 Skill 列表或发现界面确认十个名称全部出现。

仓库目前没有稳定 tag。以上 GitHub 简写跟随默认分支 `main`，属于滚动安装，不是可复现的固定版本。更新前应查看仓库差异；需要可复现输入时，先固定经人工确认的提交，再从该提交安装。

## 六宿主矩阵

| 宿主 | 兼容等级 | 项目级发现路径 | 全局发现路径 | 调用差异 | 官方依据 |
|---|---|---|---|---|---|
| Codex | `native-agent-skills` | `.agents/skills` | `~/.agents/skills`；安装工具也可写入 `~/.codex/skills` | 可用 `$ariadne-skill` 显式点名，也可按 `description` 路由 | [Codex Skills](https://developers.openai.com/codex/skills) |
| Claude Code | `native-agent-skills` | `.claude/skills` | `~/.claude/skills` | `/ariadne-skill` 是显式斜杠调用，也支持按描述加载 | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| Gemini CLI | `native-agent-skills` | `.gemini/skills`、`.agents/skills` | `~/.gemini/skills`、`~/.agents/skills` | 用自然语言点名；用 `/skills list` 核对发现，激活时遵循宿主授权提示 | [Gemini CLI Skills](https://geminicli.com/docs/cli/using-agent-skills/) |
| Cursor | `native-agent-skills` | `.cursor/skills`、`.agents/skills`、`.claude/skills`、`.codex/skills` | `~/.cursor/skills`、`~/.agents/skills`、`~/.claude/skills`、`~/.codex/skills` | 可从斜杠菜单调用 `/ariadne-skill`，也可自动发现 | [Cursor Skills](https://cursor.com/docs/context/skills) |
| GitHub Copilot | `native-agent-skills` | `.github/skills`、`.claude/skills`、`.agents/skills` | `~/.copilot/skills`、`~/.agents/skills` | 云端、CLI 与编辑器表面不承诺统一斜杠入口；用自然语言点名并核对所在表面的发现结果 | [GitHub Copilot Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| Reasonix | `directory-compatible-subset` | `.reasonix/skills`、`.agents/skills`、`.agent/skills`、`.claude/skills` | `~/.reasonix/skills`、`~/.agents/skills`、`~/.claude/skills` | 候选显式入口为 `/ariadne-skill`；必须先用 `/skills` 核对发现并完成下列专项冒烟 | [Reasonix Docs](https://reasonix.io/docs/) |

`SKILL.md` 的基础合同来自 [Agent Skills 开放规范](https://agentskills.io/specification)，安装参数与目标适配器来自 [`npx skills`](https://github.com/vercel-labs/skills)。宿主官方文档与安装工具的兼容别名可能不同；以宿主实际发现结果为准，出现差异时先降低兼容声明，不改写 Ariadne 核心合同迎合单一宿主。

## Reasonix 兼容上限

Reasonix 只标记为 `directory-compatible-subset`，且不出现在默认安装命令中：手动把 `skills/ariadne-*` 目录复制进 `.reasonix/skills`（或其全局对应目录），用 `/skills` 核对发现，然后完成本节的专项冒烟。`npx skills` 能复制到 `.reasonix/skills`，以及目录中出现 `SKILL.md`，都不能证明 Reasonix 与原生 Agent Skills 在渐进加载、引用解析、peer 路由或上下文控制上语义等价。

用于真实任务前至少完成三项专项冒烟：

- `json-references`：按 Skill 指令读取 `source-navigation.json`、`human-variable-cards.json` 与 `application-contracts.json`，并确认 Markdown reference 可达。
- `peer-routing`：总路由能点名九个 peer；peer 缺失时记录 `module_unavailable`，不得假装已经运行。
- `context-growth`：多模块连续与集群运行时检查渐进加载和上下文增长，不把目录可见性误写成隐式路由等价。

冒烟失败时保留失败证据，并把该宿主降级为未验证；不要复制或改写十个权威 Skill 来隐藏差异。

## Router-only 降级

只有在宿主或任务明确限制安装数量时，才只安装总路由：

```powershell
npx skills add xi-kari/ariadne-skill --skill ariadne-skill --copy -a codex -a claude-code -a gemini-cli -a cursor -a github-copilot
```

这种安装不是完整 Ariadne。总路由仍可做边界化分流，但九个 peer 均可能不可用；每个未运行模块必须记录 `module_unavailable`，输出不能假装来自完整方法运行，也不能提高 `output_ceiling` 或改变 `authorization_effect: none`。

## 单 peer 安装

安装器同样允许只装某一个执行模块，例如：

```powershell
npx skills add xi-kari/ariadne-skill --skill ariadne-evidence --copy -a codex -a claude-code -a gemini-cli -a cursor -a github-copilot
```

这是与 Router-only 方向相反的降级模式：当前模块在场，但它正文里点名的转交目标（总路由或其他 peer）可能不在本机。此模式的降级语义固定如下：

- 转交目标 Skill 缺失时，在 `module_runs` 把该次转交记为 `not_run`，`reason` 写 `module_unavailable`。
- 该转交目标负责的产出保持 `unknown`，当前记录维持或降低 `output_ceiling`，不得因缺件而升档。
- 当前 Skill 不得代跑缺失 peer 的职责，也不得把未运行的模块表述为已运行；`authorization_effect: none` 不变。
- 源文编号（如 Part 15、Appendix A）依赖总路由的 `source-navigation.json` 才能解析；单 peer 安装读不到时，把对应引用当作未解析记入 unknowns，不自行猜测其内容。

## 本仓库的本地验证边界

本机开发与评测继续只按显式 Skill 名或直接仓库路径运行，不把开发仓库安装进任何全局目录。仓库验证只检查清单、frontmatter、路径、证据 URL、Reasonix 冒烟合同和无镜像边界：

```powershell
python -X utf8 -B scripts/validate_adapters.py
```

该命令不启动六个外部宿主，也不产生 Release、发布或现实授权。

## 验证状态与通用冒烟合同

兼容等级描述的是格式与入口，不是已完成的宿主实测。`adapters/compatibility.json` 为每个宿主维护 `verification` 字段：`unverified`（默认，六宿主当前状态）或 `smoke-passed`（附 `last_verified` 日期）。把任何宿主升级为 `smoke-passed` 前，在一次性容器或虚拟机中完成三项通用冒烟——`json-references`（JSON 引用可读取）、`peer-routing`（路由能点名 peer 并拿到降级记录）、`context-growth`（渐进加载不整包注入）——并把命令输出存入 `evals/` 的宿主冒烟记录。

## 宿主扩展文件

仅 Codex 使用宿主扩展文件 `agents/openai.yaml`（控制展示名、短描述与隐式调用开关）；其余宿主按 Agent Skills 规范零配置发现 `SKILL.md`，不需要任何扩展文件。本套 Skill 是纯方法论，不声明工具依赖，因此也不需要 Claude Code 的 `allowed-tools` 一类字段。

## 单文件捆绑版

没有 Agent Skills 目录的宿主（网页版 ChatGPT/Gemini/Claude、自定义 GPT、纯系统提示场景）使用 `dist/ariadne-bundle.md`：由 `scripts/build_bundle.py` 按依赖序拼接十个 SKILL.md 正文生成，附方法记录字段清单与人工校验清单；CI 以 `--check` 校验它与 skills/ 永不漂移。该形态没有渐进加载与 peer 派发，整份文本一次性进入上下文（约 78KB），适合长上下文模型或手工节选。

## Router-only 交付物

Router-only 安装下的交付物是固定的：请求分类、候选对象与边界初判、证据截止点、模块缺席清单与安装指引，加上一份 peer 职责全部 `not_run`/`module_unavailable`、上限保持 `description_only` 的降级根记录。主 SKILL.md 的 Stop and downgrade 一节是该形态的权威定义。
