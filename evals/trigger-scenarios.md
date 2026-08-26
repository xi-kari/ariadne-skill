# Trigger Scenarios

Regression baseline for the description layer: real user requests and the skill that should activate, with the deciding cue. Re-run this table by hand (or with a host's skill-selection trace) after any `description` edit; a change that flips an expectation must be deliberate and recorded here.

Judging rules: "expected" names the single skill whose description should win the first activation. Requests marked `router` must reach `ariadne-skill` before any module. Requests marked `none` must activate nothing - over-triggering on them is a regression even though every module stays technically applicable.

| # | User request | Expected | Deciding cue |
|---|---|---|---|
| T01 | 帮我全面复盘一下这次产品发布:哪里出了问题、接下来怎么办、要不要追加预算 | router | 解释+决策+预测混合,多面请求 |
| T02 | Analyze our churn problem end to end and give me an auditable conclusion | router | "end to end"+"auditable" |
| T03 | 这个"用户流失"问题到底该怎么定义分析范围? | ariadne-framing | 对象与口径未定 |
| T04 | 这两篇报告能不能支撑"涨价导致流失"这个结论? | ariadne-evidence | 材料对结论的支持度 |
| T05 | 我们在一个城市试点成功了,能推断全国也会成功吗? | ariadne-scale | 试点到全国的跨尺度迁移 |
| T06 | 给上季度事故写一份正式的根因复盘,要有竞争解释 | ariadne-mechanism | 复盘级根因+竞争解释 |
| T07 | 为什么这个单元测试挂了?帮我修一下 | none | 日常交互式调试,mechanism 的负触发 |
| T08 | 分析一下我们团队最近的协作问题,别给人贴标签 | ariadne-human | 团队/组织人域分析 |
| T09 | 如果核心工程师下月离职,接下来会怎么发展? | ariadne-dynamics | 无日期的路径推演 |
| T10 | 立一个可以事后验证的预测:年底前流失率会不会超过 8%? | ariadne-forecast | 有目标有期限可评估 |
| T11 | 该不该现在做一个可回滚的小范围试点?不做行不行? | ariadne-choice | 行动/不行动的有限比较 |
| T12 | 这个自动化评分结论能不能公开并接入人事流程? | ariadne-audit | 高影响公开/自动化使用 |
| T13 | Predict next year's market and tell us the one correct action | router | 预测+行动指令混合 |
| T14 | 把这份周报改写得更简洁 | none | 生成型任务,整体出界 |
| T15 | Why did deployments slow down this quarter? (随口一问) | none | L0 直接回答;仅当用户要求方法级分析时进入 router/mechanism |
| T16 | 我们组织的问题同时涉及人、证据和该不该重组,请系统分析 | router | 人+证据+决策,总控词面 |
