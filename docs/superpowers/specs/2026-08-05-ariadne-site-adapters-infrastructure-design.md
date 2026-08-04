# Ariadne 官网、多智能体适配与基础设施设计

## 状态

- 外部名称：Ariadne
- 仓库与主 Skill：`ariadne-skill`
- 方法论内核：Lattice Kernel
- 官网：公开部署到 `https://xi-kari.github.io/ariadne-skill/`
- 许可证：MIT License
- 视觉方向：C「理性格点」与已批准的长页编辑式阅读节奏
- 建设顺序：完整建设全部内容，再统一审查、集中修复和发布

## 目标

本次扩展形成三个彼此隔离、共同验证的子系统：

1. 一个中文静态官网，完整介绍 Ariadne、十个方法论模块、协作方式、输出边界和安装入口。
2. 一套基于 Agent Skills 开放格式的多宿主分发说明与验证合同。
3. 一套适合当前仓库规模的最小公共仓库基础设施。

最终交付必须让读者能够理解 Ariadne，让支持 Skill 的 Agent 能从同一权威内容安装，让维护者能在合并前重复验证仓库、官网和适配合同。

## 非目标

- 不修改十个 Skill 的方法论职责、Method Record 语义或输出上限。
- 不复制 CrossFrame 的品牌、运行链、统计数字、校验印章或产品定位。
- 不引入 Astro、React、Vite、Node 构建链、外部字体、CDN、分析脚本或 Cookie。
- 不生成 Release、tag、PyPI/npm 包、自动版本号或发布声明。
- 不把 CI 通过、网站上线或格式兼容写成方法论有效、现实事实或行动授权。
- 不在本轮再次改写当前电脑的全局 Skill 目录。

## 总体架构

```text
skills/                    唯一方法论权威源
site/                      官网源文件
scripts/build_site.py      组装静态部署产物
scripts/validate_repo.py   仓库、站点与适配统一校验入口
docs/                      设计、适配矩阵与维护文档
.github/                   CI、Pages、依赖与协作入口
```

官网与适配文档只描述 `skills/` 中已经存在的能力。它们不得成为第二套方法论定义。部署构建从 `site/` 复制页面资源，并从现有 `docs/assets/` 复制已批准的 SVG；构建产物不提交到 Git。

## 官网设计

### 页面结构

官网使用单页中文长页，顺序为：

1. Hero：Ariadne、Lattice Kernel 与“一套让 AI Agent 思考和处理复杂问题的方法论集群”。
2. 事实概览：10 个 Skill、`1 + 9` 架构、5 种协作模式、`authorization_effect: none`。
3. Ariadne 是什么及不是什么。
4. Lattice Kernel 方法地图与“按需选取”说明。
5. 十个方法论模块：负责什么、可以完成、适合任务、典型产出、边界。
6. 单独、连续、集群、持续与完整运行。
7. Method Record、未知项、冲突、输出上限和授权边界。
8. 多智能体兼容矩阵与安装命令。
9. 验证、来源、许可证与仓库入口。

### 视觉与交互

- 使用 `#EDF2EF`、`#173532`、`#B7CBC4`、`#8B62AD`、`#C4874F`；紫色和铜色不用于不满足对比度的小号正文。
- 延续参考页的吸顶导航、阅读进度、章节眉题、编辑式分隔、复制命令按钮和渐进显现。
- 宽屏提供“方法导航 · 按需选取”侧栏。侧栏表达阅读位置，不暗示十个模块必须依次执行。
- 移动端隐藏侧栏并压缩导航；正文、表格和卡片保持单列可读。
- JavaScript 只负责阅读进度、复制按钮和可选显现；禁用 JavaScript 后所有内容仍可访问。
- 尊重 `prefers-reduced-motion`，提供键盘焦点、语义标题、替代文本和文本版方法地图。
- 不加载第三方字体或徽章。favicon、分享图和 404 页面均由仓库本地资源提供。

### 构建与部署

`scripts/build_site.py` 仅使用 Python 标准库，将 `site/` 和共享 SVG 组装到临时输出目录。所有页面资源使用相对路径，保证本地预览和 `/ariadne-skill/` 项目站路径一致。

单个 GitHub Actions 工作流先运行完整验证，再仅在 `main` 成功验证后部署 Pages。部署 job 单独获得 `pages: write` 与 `id-token: write`；验证 job 只有 `contents: read`。部署失败时保留上一版站点，回滚通过回退提交并重新运行工作流完成。

## 多智能体适配

### 权威源与兼容等级

十个 `skills/ariadne-*/` 目录是唯一权威源。现有基础 frontmatter 继续只要求 `name` 和 `description`；`agents/openai.yaml` 是 OpenAI 扩展，不得成为其他宿主的依赖。

| 宿主 | 兼容等级 | 主要发现位置 | 验证重点 |
|---|---|---|---|
| Codex / OpenAI | 原生 Agent Skills | `.agents/skills`、用户 Skill 目录 | OpenAI metadata 与显式调用 |
| Claude Code | 原生 Agent Skills | `.claude/skills` | 目录发现、引用文件和斜杠调用 |
| Gemini CLI | 原生 Agent Skills | `.gemini/skills` 或 `.agents/skills` | 激活授权与全部十个模块发现 |
| Cursor | 原生 Agent Skills | `.cursor/skills` 或 `.agents/skills` | 自动发现与显式调用 |
| GitHub Copilot | 原生 Agent Skills | `.github/skills` 或 `.agents/skills` | 云端、CLI 和编辑器表面差异 |
| Reasonix | 目录兼容子集 | `.reasonix/skills`、`.agents/skills` 等 | JSON reference、peer 路由和上下文增长 |

### 分发方式

- 官网和 README 提供现有 Agent Skills 安装工具的命令，不编写 Ariadne 专用复制器。
- 默认安装完整十个 Skill；仅安装主路由属于显式降级方式，必须说明 peer 不可用时会记录 `module_unavailable`。
- 同时说明项目级与用户级安装。项目级用于审查和试用，用户级用于跨项目长期使用。
- Windows 公共说明默认使用复制，不依赖 Git 符号链接。
- 没有稳定 tag 前，安装命令明确属于跟随 `main` 的滚动安装；不得伪装为固定版本。

### Reasonix 专项合同

Reasonix 不声明完整 Agent Skills 语义等价。专项冒烟测试至少覆盖：

1. 十个模块全部可发现。
2. Markdown reference 可读取。
3. `source-navigation.json`、人类变量卡和审计应用合同等 JSON reference 可按 Skill 指令读取。
4. 主路由可以点名九个 peer，缺失模块会诚实降级。
5. 多模块运行不会把目录兼容误写成隐式路由等价。

## 仓库基础设施

### 必须建设

- 根 `LICENSE` 使用 MIT License。
- `requirements-dev.txt` 固定 `pytest`、`jsonschema` 与 `PyYAML` 的可复现开发版本。
- `.editorconfig` 与 `.gitattributes` 统一 UTF-8、最终换行和文本行尾。
- CI 在 pull request、`main` push 和手动触发时运行测试、仓库校验、评测校验与站点构建。
- Action 使用实施时核验的官方版本并固定完整提交 SHA，权限遵循最小化原则。
- 扩展现有 Python 校验，覆盖 Markdown/HTML 相对链接、显式锚点、SVG XML 与可访问文本、UTF-8、最终换行和尾随空白。
- `CONTRIBUTING.md`、`SECURITY.md`、bug/validator issue form、methodology/counterexample issue form 和 PR 模板。
- Dependabot 每月检查 `pip` 和 `github-actions`。
- CI 首次成功后，为 `main` 建立最小 ruleset：必须通过 PR、要求唯一验证检查、禁止 force push 和删除；单维护者阶段不要求第二人审批。
- 启用 GitHub Pages 与 private vulnerability reporting，关闭没有内容的 Wiki 和 Projects。

### 明确不建设

- 不增加 CodeQL、覆盖率门槛、多操作系统矩阵、pre-commit、stale bot、CLA/DCO、CODEOWNERS 或自动 Release。
- 不让实时外链可用性阻塞每个 PR；外链只在发布前或低频维护时检查。
- 不为提高 community profile 百分比添加没有真实执行方式的行为准则。

## 数据流与失败处理

```text
skills + site + docs
        ↓
本地测试与统一校验
        ↓
CI validate ──失败──> 阻止合并与部署
        ↓ 成功
Pages deploy ─失败──> 保留上一版线上站点
        ↓ 成功
公开官网
```

- 缺失源文件、失效相对链接、错误锚点、非法 SVG、构建路径逃逸或适配矩阵缺项必须使本地构建与 CI 明确失败。
- 外链暂时不可用只生成维护信息，不让普通 PR 随网络波动失败。
- 复制按钮失败时保留可手工选择的命令文本。
- Pages 失败不改变方法论内容或 Release 状态。
- 发现宿主行为不同于文档时，先降低兼容等级并记录差异，不修改 Skill 核心来迎合单一宿主。

## 外部合同依据

- Agent Skills 开放规范：<https://agentskills.io/specification>
- Codex Skills：<https://developers.openai.com/codex/skills>
- Claude Code Skills：<https://code.claude.com/docs/en/slash-commands>
- Gemini CLI Skills：<https://geminicli.com/docs/cli/using-agent-skills/>
- Cursor Skills：<https://cursor.com/docs/context/skills>
- GitHub Copilot Skills：<https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills>
- Agent Skills 安装工具：<https://github.com/vercel-labs/skills>
- GitHub Pages 工作流：<https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages>
- GitHub 仓库许可证：<https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository>

这些链接只冻结施工时应核对的上游合同。实施时仍须重新读取当前官方版本，不能把本设计中的路径或命令当作永久不变的接口。

## 实施与审查顺序

严格遵守“先完整建设，后统一审查”：

1. 先写覆盖站点、适配与基础设施合同的失败测试。
2. 一次性完成官网全部内容、构建器、多宿主文档、MIT、CI 与社区基础设施。
3. 确认 `ARIADNE_EXTENSION_CONTENT_COMPLETE`，此时所有计划文件都必须存在。
4. 只在完整边界之后并行启动三类审查：官网/可访问性、宿主兼容、CI/安全。
5. 汇总审查结果并集中修复，不按模块逐个审定。
6. 运行完整本地验证，创建 PR，等待 CI 与 Pages 预部署检查。
7. 合并后启用 Pages、ruleset 与安全设置，再验证线上地址和仓库设置。

测试驱动开发属于实现验证，不等同于提前内容审查。内容、视觉、兼容性和治理判断的正式审查只能在完整门之后开始。

## 验收标准

- 官网在桌面与移动视口完整可读，无 JavaScript 时核心内容不丢失。
- 网站无第三方运行时资源请求，内部链接、锚点、SVG 与复制控件通过校验。
- 十个 Skill 均出现在兼容矩阵、安装说明和发现验证中。
- Codex、Claude Code、Gemini CLI、Cursor、GitHub Copilot 的原生标准兼容有真实文档依据；Reasonix 以专项结果标注兼容上限。
- 现有 37 项测试与新增测试全部通过，两项现有验证器继续通过。
- CI 权限最小、Action 固定、Pages 只在验证成功后部署。
- `main` 受 ruleset 保护，private vulnerability reporting 已启用，Wiki/Projects 状态与设计一致。
- 线上地址为 `https://xi-kari.github.io/ariadne-skill/`，不影响 `/crossframe-skill/`。
- `RELEASE` 继续为 `not_authorized`，仓库没有新 tag 或软件包发布。
