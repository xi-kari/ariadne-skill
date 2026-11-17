# 参与 Ariadne

感谢你改进 Ariadne。请让每次变更保持可复现、可审计，并尊重方法论合同和行动边界。

## 开始之前

- 使用 Python 3.10。
- 从仓库根目录安装固定的开发依赖：

    python -m pip install -r requirements-dev.txt

- 不要把仓库复制、链接或安装到本机全局 Skill 目录进行测试；请显式点名 Skill 或直接使用仓库路径。
- 安全漏洞请按 SECURITY.md 使用 GitHub Private Vulnerability Reporting，不要创建公开 Issue。

## 变更边界

- `skills/ariadne-skill/` 是唯一安装包与方法论来源。内部路径可组合；新增资源须登记到 `architecture.json` 并从入口可达，不得创建宿主镜像或复制合同。
- 方法内容依据《Xikari-条件结构与转化论》v2（2026-11-16；SHA-256 `6ef2e508…0149c`）；新增或修改的方法条目应标注原文锚点（§），并保持“派生候选、非作者逐条确认”的身份。方法论争议请指出原文条款。
- Method Record 2.0/2.1 仅用于显式选择的旧格式兼容。修改其 schema 时，同步 `schemas/method-record.schema.json` 与 `skills/ariadne-skill/references/method-record.schema.json`（须字节一致）；语义规则只在安装包的 `scripts/validate_record.py` 实现，由仓库包装器复用。当前路径不必输出统一旧记录。
- 保持 Ariadne、ariadne-skill 和 Lattice Kernel 的固定身份，不引入 CrossFrame 或其他仓库的合同。
- 生成记录的 `authorization_effect` 必须保持 `none`：记录本身不新增行动权限。用户已经给予的授权与宿主权限继续有效；应据此完成已授权工作，而不是反复要求同一许可。工具输出也不自动构成事实确认或替用户作出价值选择。
- RELEASE 已于 2026-08-26 经评审解封为 complete（tag `v1.0.0`）。贡献不得再次变更发布状态、创建新 tag、GitHub Release、软件包发布或隐式全局安装；这些动作需要维护者的单独评审变更。
- 文件中不要加入迭代过程、开发日志或版本逐项解说。

若同一次工作横跨多个模块或整个扩展，应先完成计划范围内的全部正文、元数据、适配器、网站和验证器，再声明 ARIADNE_EXTENSION_CONTENT_COMPLETE。正式的内容、视觉、兼容性和治理审查只能在该门之后开始；实现期间的自动测试不等同于正式审查。

## 测试与验证

先为行为变更增加能失败的测试，再做最小实现。提交前运行：

    python -X utf8 -B -m pytest -q -p no:cacheprovider
    python -X utf8 -B scripts/validate_repo.py
    python -X utf8 -B scripts/validate_evals.py
    python -X utf8 -B scripts/validate_adapters.py
    python -X utf8 -B scripts/build_bundle.py --check
    python -X utf8 -B scripts/build_site.py --output build/site
    git diff --check

完整验证使用 Python 3.10 与 Linux（Windows 使用 WSL）：forecast 登记工具依赖 POSIX `dir_fd` 和 `O_NOFOLLOW` 安全文件操作，原生 Windows 不具备这些能力时会明确失败，不能宣称登记已保存。符号链接安全用例在无法创建链接的环境会跳过，由 Linux CI 覆盖；仅开启 Windows 开发者模式不能补足 forecast 的 POSIX 依赖。

改动 `architecture.json` 中 `bundle` 列出的任何文件后运行 `python scripts/build_bundle.py` 重新生成单文件版；深库、旧格式、schema 与可执行工具只链接，不内嵌。行为评测用 `python scripts/run_evals.py`（转录落盘 `evals/runs/`，已在 .gitignore 中；评分不自动化）。

若某项无法运行，请在 Pull Request 中准确写明未运行原因，不要把未验证状态表述为通过。

## Issue 与 Pull Request

- 缺陷报告应包含版本、Agent Host、具体 Skill、最小复现、预期与实际行为，以及必要的已脱敏日志。
- 方法论争议应指出来源条款、反例、受影响模块和建议降级。
- Pull Request 应列出实际测试证据、合同变化、网站影响、兼容性影响和 Release 边界确认。
- 不要在 Issue、Pull Request、日志或案例中提交秘密、凭据、个人资料或未经授权披露的材料。
