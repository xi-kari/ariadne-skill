已完成**合成测试材料**的完整本地流程，实际调用了冻结包的 `scripts/forecast.py`：草稿验证、登记、原件验证、观察草稿验证、追加一次记录、追加件验证，以及再次验证原件。7 次调用全部成功，其中 5 次为验证。

队列及其数值均为虚构测试材料；命令执行、UTC 时间和文件校验是真实本地记录。登记 ID 为 `synthetic-queue-20261117T012633967966Z`。

| 时间项 | UTC |
|---|---|
| 本轮输入截止 | 2026-11-17T01:26:33Z |
| 工具实际登记 | 2026-11-17T01:26:34.403094Z |
| 未来窗口开始 | 2026-11-17T02:26:33Z |
| 目标截止 | 2026-11-18T01:26:33Z |

这些时间由执行时的 `datetime.now(timezone.utc)` 生成。目标规则是截止时同一虚构队列的整数计数 **N > 100**；恰好 100 不算超过，缺失标签不填零。

唯一输入是标为 `assumption` 的快照 80。因此登记表达为 `unknown`，没有概率、权重或排序。保留一个明确有条件的候选：若累计流入等于累计移出且口径不变，计数保持 80。它没有得到流量数据支持，也不穷尽可能未来；净增或净减均未被排除。单候选说明记录了搜索范围、没有其他完整候选的材料原因，以及净流量不为零时持平路径失效、净增超过 20 时越过阈值的条件。独立保留“维持 80”的简单比较基线，待明确合成标签出现后才可计算误差和阈值比较。

已追加一次登记后的缺失标签检查：`actual_result: null`、`status: not_evaluable`、`sources: []`。截止尚在未来，未取得结果标签，基线同样不可评价；此记录不计为预测命中或失败。原始表达已经弃权，即使以后出现目标标签，也不能把它改计为预测命中。后续若有明确合成标签，应使用新观察 ID 追加。本轮即时检查已完成，没有启动后台监控或安排自动复查。

原件在追加前后逐字节一致，SHA-256 均为：

`8b2bea46d0291feedc3b9eacb69c2f3f37d8447ab4c863e5049cc429cfd8e10e`

登记回执、追加回执与对应文件的哈希一致，追加件也正确绑定原件哈希。文件如下：

| 文件 | 路径 |
|---|---|
| 合成登记草稿 | [synthetic-draft.json](synthetic-draft.json) |
| registry 中的登记原件 | [forecast.json](synthetic-registry/synthetic-queue-20261117T012633967966Z/forecast.json) |
| 原样保存的登记回执 | [synthetic-registration-receipt.json](synthetic-registration-receipt.json) |
| 缺失标签观察草稿 | [synthetic-observation.json](synthetic-observation.json) |
| registry 中的追加记录 | [synthetic-missing-label-1.json](synthetic-registry/synthetic-queue-20261117T012633967966Z/resolutions/synthetic-missing-label-1.json) |
| 原样保存的追加回执 | [synthetic-resolution-receipt.json](synthetic-resolution-receipt.json) |
| 完整性核验 | [synthetic-verification.json](synthetic-verification.json) |
| 真实命令与结果 | [execution.json](execution.json) |

工具验证证明本次文件和登记流程满足所检查的格式、时间与完整性条件，不证明任何现实队列事实或预测能力。
