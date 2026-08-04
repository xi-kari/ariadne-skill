# 参与 Ariadne

感谢你改进 Ariadne。请让每次变更保持可复现、可审计，并尊重方法论合同和行动边界。

## 开始之前

- 使用 Python 3.10。
- 从仓库根目录安装固定的开发依赖：

    python -m pip install -r requirements-dev.txt

- 不要把仓库复制、链接或安装到本机全局 Skill 目录进行测试；请显式点名 Skill 或直接使用仓库路径。
- 安全漏洞请按 SECURITY.md 使用 GitHub Private Vulnerability Reporting，不要创建公开 Issue。

## 变更边界

- skills/ 是十个 Ariadne Skills 的唯一方法论来源，不得创建宿主镜像或复制合同。
- 保持 Ariadne、ariadne-skill 和 Lattice Kernel 的固定身份，不引入 CrossFrame 或其他仓库的合同。
- authorization_effect 必须保持 none；工具输出不构成事实确认、价值选择或行动授权。
- RELEASE: not_authorized 必须保持不变。贡献不得创建 tag、GitHub Release、软件包发布或隐式全局安装。
- 文件中不要加入迭代过程、开发日志或版本逐项解说。

若同一次工作横跨多个模块或整个扩展，应先完成计划范围内的全部正文、元数据、适配器、网站和验证器，再声明 ARIADNE_EXTENSION_CONTENT_COMPLETE。正式的内容、视觉、兼容性和治理审查只能在该门之后开始；实现期间的自动测试不等同于正式审查。

## 测试与验证

先为行为变更增加能失败的测试，再做最小实现。提交前运行：

    python -X utf8 -B -m pytest -q -p no:cacheprovider
    python -X utf8 -B scripts/validate_repo.py
    python -X utf8 -B scripts/validate_evals.py
    python -X utf8 -B scripts/validate_adapters.py
    python -X utf8 -B scripts/build_site.py --output build/site
    git diff --check

若某项无法运行，请在 Pull Request 中准确写明未运行原因，不要把未验证状态表述为通过。

## Issue 与 Pull Request

- 缺陷报告应包含版本、Agent Host、具体 Skill、最小复现、预期与实际行为，以及必要的已脱敏日志。
- 方法论争议应指出来源条款、反例、受影响模块和建议降级。
- Pull Request 应列出实际测试证据、合同变化、网站影响、兼容性影响和 Release 边界确认。
- 不要在 Issue、Pull Request、日志或案例中提交秘密、凭据、个人资料或未经授权披露的材料。
