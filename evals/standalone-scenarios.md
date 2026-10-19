# Standalone Module Scenarios

Invoke only the named module for each prompt.

| Skill | Prompt | Required product |
|---|---|---|
| `ariadne-framing` | “我们要研究平台生态恶化，先把对象说清楚。” | The difference to explain, task profile, candidate object contract, request type, domain-atlas entry, missing fields, output ceiling. |
| `ariadne-evidence` | “这些访谈和三篇报道能证明算法导致创作者退出吗？” | Claim/evidence ledger, causal ceiling, competitors, next evidence. |
| `ariadne-scale` | “把十个用户的体验推广到全国平台会损失什么？” | Source/target scale record and translation-loss audit. |
| `ariadne-mechanism` | “团队交付变慢可能通过哪些机制发生？” | Competing mechanisms, channels, baseline, falsifiers, residuals. |
| `ariadne-human` | “员工拒绝披露原因时，组织还能判断什么？” | Human-domain boundaries, privacy state, affected positions, allowed use. |
| `ariadne-dynamics` | “一次政策变化如何沿平台、商家和用户传播？” | Frozen event, clocks, thresholds, branches, signals, stopping. |
| `ariadne-forecast` | “登记未来六个月客户流失判断。” | Frozen forecast record, baseline, calibration, reverse signals, writeback. |
| `ariadne-choice` | “比较立即上线、灰度试验、延期和不做。” | Structured options with exactly one no action, normative premises, an analytic recommendation for deliberation (or the named premise that blocks it), authorization gaps, limits. |
| `ariadne-audit` | “审查这份将影响员工资格的自动化判断。” | Gates, challenge, appeal, rollback, downgrade, AI boundary. |
| `ariadne-skill` | “完整分析一个证据不足但影响重大的组织改革问题。” | Routed multi-module record with bounded plain-language synthesis. |
| `ariadne-framing` | “帮我设计一套新的 on-call 轮值方案。” | `synthesis_design` classification, frozen design constraints and success criteria, no constructed artifact. |
| `ariadne-skill` | “给我们的 API 设计一个版本化策略，比较取舍后给建议。” | `synthesis_design` pass: constraint record, compared candidate designs including keep-current, bounded proposal with external adoption handoff. |
| `ariadne-scale` | “周报只保留各队列的平均等待时长，够不够判断哪里过载？” | Task-relative sufficiency check: static recovery, dynamic closure, and intervention sufficiency separated; minimal repairing variable named; no claim that all detail must be recovered. |
| `ariadne-mechanism` | “新人第一年的培训经历还影响他们现在的绩效吗？” | History three questions separated (formation, current carrier, increment beyond current skill); carried route versus G3; no G3 gain made by omitting current skill. |
| `ariadne-audit` | “这份 AI 写的政策评论只在内部讨论，需要走强判断八件套吗？” | Strong-judgment status decided by use; IG6 `not_applicable` with a reason when no handling, eligibility, allocation, reputational, or automated use; clear conclusions with proportionate review. |
