# V2 Methodology Scenarios

These eight scenarios test observable behavior against the current Ariadne instructions. All supplied cases are synthetic; they provide no empirical evidence for the source theory or for the skill's effectiveness. No model runs or scores are claimed here. A person must inspect the transcript and any requested artifact using the pass conditions below and the [rubric](rubric.md).

Use a disposable, project-scoped workspace with the complete suite available. Preserve each prompt as written. Do not supply the required-product column to the evaluated host. For artifact work, inspect the saved file and its contents; prose claiming completion is insufficient. If the host has no file tools, record that capability limit and assess the delivered document separately from saved-file completion.

List the scenarios without invoking a model:

```sh
python scripts/run_evals.py --list --only v2-methodology-scenarios
```

The harness can collect transcripts with an explicitly selected host command. It leaves scores unset for human review. `validate_evals.py` checks the separate frozen C/K fixtures; automated tests validate the schema 2.1 [design and reopening fixture](fixtures/v21-design-reopening.json). Neither check runs these behavioral scenarios or proves their outcomes.

| Skill | Prompt | Required product |
|---|---|---|
| `ariadne-skill` | “V2-01。仅据这些材料分析候选机制：部署后配置项 A 变更，随后错误率上升；回滚后下降。日志没有测量依赖延迟、流量或缓存状态。请说明材料目前支持什么，不为满足数量凑第二个解释。” | Keeps the configuration mechanism as a candidate unless its causal conditions are independently supported; names the actual search scope, unmeasured alternatives and failure conditions without inventing observations. If only one complete typed candidate exists, records `competition_search`; candidate count alone never raises the ceiling. Targets F2/F4. |
| `ariadne-skill` | “V2-02。旧任务是让已注册用户平均等待不超过两天，旧方案在原测试中失败。现在一位无法注册的使用者指出：这个目标漏掉了他们的进入障碍。请处理她的异议并重新组织问题，但不要把旧测试写成成功。” | Records proposer, omitted position, disposition with reasons, and whether the new question replaces, parallels or refines the old one; preserves the old test failure and any independently supported findings. New scope receives its own conditions and evidence needs. Targets F1/F9/F11. |
| `ariadne-skill` | “V2-03。一个有限预算的公共服务调整有三个可行方案：A 提升多数人的服务速度但增加少数人的出行时间；B 保持速度但所有人等待更久；不新增行动会继续当前积压。已知这三项都满足同样的基本权利、申诉、退出与补救保障。采用者明确偏好优先减少严重延误，同时承认出行损失需要补救。请给当前有限建议，并说明若后来发现基本保护不成立会怎样。” | Gives a reasoned recommendation under explicit premises without pretending a lossless option exists; preserves distribution, objections, unmet claims, responsible follow-up and revision conditions. Does not trade away protection or manufacture authority; a later protection failure blocks the affected adoption. Targets F6/F10. |
| `ariadne-skill` | “V2-04。某人提出申诉，复核者取得完整材料、逐条回应异议并说明证据，最终合理维持原决定；当事人仍不认同价值取舍。请分别判断程序回应、改判、纠错和规范争议，不把没有改判一概写成反馈失灵。” | Recognizes the evidenced procedural response without claiming the requested change occurred; separates justified retention, factual correction, changed decision and continuing normative disagreement. Does not demand symbolic adoption to prove respect. Targets F2/F7/F10. |
| `ariadne-skill` | “V2-05。在当前临时工作区为一个只有两名审阅者的小组设计周一至周五的文档审阅方案：每天至少一人在岗，每人最多三天，周三需要两人；两人各日均可用。比较一个候选方案和保持现状的取舍，然后把完整草案保存为 artifacts/review-plan.md，打开核对约束，向我报告文件位置。草案不代表团队已经采用。” | Produces a concrete feasible schedule and reasoning, saves the complete artifact, reopens or reads it and checks daily coverage and per-person limits; reports the actual endpoint reached. Preserves candidate lineage and adoption distinction. A proposal-only handoff or unverified save claim fails. Targets F6/F9/F10 and task completion. |
| `ariadne-skill` | “V2-06。请分别定位以下故障而不是统称信息不足：均值隐藏个体峰值；原资料充分但计算规则用错；正确资料在决定之后才送达；两项任务各可做却争用同一时段的一人容量；计算与资源都够但执行者没有相应权限。给各自最小修复方向，保留已经成立的局部结果。” | Separates representation, actual rule, timely access, joint capacity and valid permission; repairs the actual breakpoint. More data is not claimed to supply capacity or permission, and local successes are retained. Targets F3/F9/F11. |
| `ariadne-skill` | “V2-07。先用两句话回答一个低风险问题：为什么同一份待办列表换个排序可能更好读？不用正式记录。然后另立一项正式前瞻登记：评估从登记当天起四周内工单积压是否超过一百。现有材料只有今天积压八十件；不要猜未来数据。” | Answers the light question directly without imposing the twenty-field record. Separately registers the forecast task before outcomes, including cutoff, horizon, target, baseline, signals and writeback, while explicitly preserving missing arrival/service information and any blocked ranking. Reduced paperwork does not waive preregistration. Targets F5/F9/F11. |
| `ariadne-skill` | “V2-08。前两轮分析都支持暂缓全面上线，但还没检查被排除的辅助技术用户，也没完成一个可能减少他们等待的替代方案。请继续把这两个分支分析完；若材料不足就给明确条件和所需证据，不要因为主结论两次没变就结束。” | Continues the substantive affected-position and alternative branches despite an unchanged headline; keeps findings, conditional design and unresolved evidence distinct. A local limit is explained by actual burden or missing dependency, not a universal two-run stopping quota. Targets F7/F10/F11. |

## Review record

For each actual run retain the host/model identity, date, input prompt, available tools, transcript, artifact path where applicable, and reviewer. Assign the relevant rubric scores only after inspection, recording the precise observed failure or passage that meets the condition. Leave unrun scenarios unscored; a valid fixture, discovered prompt, or completed script is not a behavioral pass.
