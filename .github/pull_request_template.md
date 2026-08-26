## 变更摘要

说明变更对象、动机和边界。

## 验证

- [ ] 已运行与变更直接相关的聚焦测试
- [ ] 已运行完整 pytest 测试
- [ ] 已运行仓库、评测与适配器验证器
- [ ] 涉及网站时已构建 build/site
- [ ] 已运行 git diff --check

请附上实际命令、通过数量和仍未运行的检查：

## 合同变更

列出新增、修改或删除的 Skill、Method Record、验证器或其他公共合同；若无，请写“无”。

## 网站影响

说明内容、链接、资源、可访问性或构建产物的影响；若无，请写“无”。

## 兼容性影响

说明 Codex、Claude Code、Gemini CLI、Cursor、GitHub Copilot 或 Reasonix 的发现、安装和调用影响；若无，请写“无”。

## 边界确认

- [ ] authorization_effect 仍为 none
- [ ] 发布状态（RELEASE 阶段、tag、包发布）未在本 PR 中变更
- [ ] 本 PR 不创建或授权 tag、GitHub Release、软件包发布或全局安装
- [ ] 本 PR 不含秘密、凭据、个人资料或未经授权披露的案例材料
