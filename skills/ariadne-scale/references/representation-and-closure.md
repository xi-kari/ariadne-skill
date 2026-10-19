# Representation, Closure, and Joined Judgments

Use this reference when a question turns on whether a coarser or translated representation is enough for a stated task, whether it can advance itself over time or under allowed actions, whether several locally successful steps really join, and how error propagates. It distills the conditional formal propositions F1-F6 and the worked examples of the source's Appendix C (§4.18-4.19, C.5-C.12). Each F proposition is a necessary relation inside a declared model: it is established by proof, not by observation, and it never certifies that a real object satisfies its premises.

## Contents

1. Standing of formal results
2. Setup and notation
3. F1 task recovery and worst-case error
4. F2 closure under dynamics and allowed actions
5. F3 common feasible action under limited information
6. F4 successive conversions and execution correctness
7. F5 approximate closure and error propagation
8. F6 task families and the coarsest sufficient partition
9. Worked example: two queues
10. History increments created by representation omission
11. Three composition boundaries
12. Mathematical scale-bridge discipline
13. Cross-text difference retention
14. Method Record use

## Standing of Formal Results

Formal results answer formal questions. Keep six judgments apart, each with its own grounds (§2.1.2): formally feasible, an algorithm exists, computable within budget, data available in time, executed correctly in fact, and authorized to adopt. A proof states its state space, mappings, target, allowed operations, and premises; exhaustive enumeration can check a finite domain; numerical computation states precision, boundary decisions, and implementation error. Repeating a computation adds no independent empirical support. Applying a result to a real object additionally states how real quantities map to model variables, which premises have material, the error and validity interval, and which counterexample breaks the mapping. A formal proof of exact closure and a finite dataset that found no deviation are different evidence identities, and neither grants G4-instance support by itself.

## Setup and Notation

Let X be a non-empty set of source states, pi: X -> Y a deterministic representation with Y = pi(X), and q: X -> V the target query. For each y in Y the fiber X_y = {x : pi(x) = y} collects the source states the representation cannot tell apart. A decoder g may use only y: it may not secretly read the source state, an identity label, or undeclared history. A task fixes the target query, horizon, environment, allowed operations, and error tolerance (method constraint 法1); every sufficiency claim below is relative to that task.

## F1 Task Recovery and Worst-Case Error

**F1.** A decoder g with q = g o pi exists exactly when q is constant on every fiber; when it exists, g is unique on Y. In words: one representation value cannot merge states the task must distinguish. The proposition gives set-function existence only; computability on an infinite domain and sufficiency of a finite budget are separate questions.

**Finite scalar recovery.** With X finite, q real-valued, unrestricted real output, and worst-case absolute error over the whole domain, the best achievable error is half the largest within-fiber amplitude: inf over g of max over x of |q(x) - g(pi(x))| = (1/2) max over y of (b_y - a_y), where a_y and b_y are the fiber's minimum and maximum target values. The fiber midpoint attains it. A decoder within tolerance epsilon exists exactly when every fiber's amplitude is at most 2*epsilon. Infinite domains need suprema and boundedness checks; vector targets, restricted outputs, average loss, and probability weighting are different optimization problems. Half-amplitude is never a cross-domain information-loss score.

**Binary target.** With a binary target, zero-one loss, and a uniform finite source distribution, the minimum error rate is |X|^-1 times the sum over fibers of min(n_y0, n_y1): each fiber gets one label, and the majority label leaves the smaller count wrong; randomizing cannot do better. This describes the stated distribution, not the error frequency of any real population.

## F2 Closure Under Dynamics and Allowed Actions

**F2.** For a one-step deterministic dynamic F: X -> X, a coarse dynamic Fbar with pi o F = Fbar o pi exists exactly when pi(x) = pi(x') implies pi(F(x)) = pi(F(x')). If this holds on the whole domain, the commutation holds for every number of steps. Holding on a few visited states does not extrapolate.

With an allowed action set U, check the condition for every action's F_u separately before composing arbitrary action sequences. When an action's feasibility depends on folded detail, either show the coarse action is implementable for every relevant source state in the fiber or restrict where it may be used; when several micro implementations share one coarse action name, check separately that they give the same coarse response within tolerance.

For a finite stochastic system with kernel P, a coarse kernel exists for every initial distribution exactly when, within each block, every source state sends the same total probability into each target block. Matching only the next-step mean, or coinciding under one initial mixture, does not meet that requirement.

Static recovery (F1), dynamic closure (F2), and closure under allowed interventions are three separate checks with no automatic progression: a total answers a total question yet can miss local overload; restoring one static answer can still drop the position identity a targeted operation needs. Adding a composition share can fix one time-point's one-step prediction without supplying that share's own update law or closure under every operation.

## F3 Common Feasible Action Under Limited Information

**F3.** For a finite, single-round, deterministic task, let X_y be the states consistent with the current material and A_ok(x) the set of qualifying actions in state x, already restricted by the target, protection requirements, resources, and valid authority. A single action that qualifies for every consistent state, chosen without knowing which state holds, exists exactly when the intersection of A_ok(x) over X_y is non-empty.

Each state having its own remedy is only necessary: with sets {left} and {right}, every state has a way out but no common action exists. If both also allow an authorized safeguarding action, the intersection becomes non-empty while the state remains unidentified. So **identifying the full state is not a universal precondition of finite action, and having a remedy in every state is not the same as being able to choose correctly now**. The qualifying sets must already include the resources, protection, and authority the task requires; writing an action down mathematically never substitutes for those conditions. The proposition covers only the listed consistent states and cannot guarantee that no unknown state appears. Lawful additional observation, waiting, or safeguarding can change the information and strategy sets but does not happen automatically; risk-tolerant probabilistic choice, randomization, and sequential strategies are analyzed against their own targets.

## F4 Successive Conversions and Execution Correctness

**F4.** Given f: X -> Z with q = g o f, a further conversion h: Z -> W still recovers q exactly when g is constant on every fiber of h restricted to the reachable set f(X). Only reachable intermediate values matter.

Example: X = {0,1}^2. The first stage keeps both positions; the second stores only their sum; the final query still asks for the first position. Each stage completes its own local task (preserve, count), yet the composition merges (0,1) and (1,0) and cannot answer the final query. Keeping one Boolean for the first position repairs it without restoring every source detail; changing the final question to "count" is a different task that succeeds, never a completion of the original one.

**Representation sufficiency and execution correctness are tested separately.** Take three source states with representation f = (0,0,1), required answers q = (0,1,1), and actual rule g_actual = (0,0). The first two states share representation 0 yet need different answers, which proves the representation insufficient: no deterministic rule could be right on both. The third state's representation 1 uniquely requires 1 while the rule outputs 0, which is an independent witness of a rule error. Fixing the rule to (0,1) cures the second error without removing the representational conflict, and locally correct states keep their correctness despite failures elsewhere. When the internal representation, the input at the time, or the actual rule is unknown, keep the gap open. An original that always existed is not evidence that the reviewer obtained it in time; being reviewable after an error is not the same as being available as input before the action.

## F5 Approximate Closure and Error Propagation

**F5.** Suppose every reachable x satisfies d(pi(F(x)), Fbar(pi(x))) <= epsilon and Fbar is L-Lipschitz on the reachable region. Starting from y_0 = pi(x_0), the error e_t = d(pi(x_t), y_t) obeys e_{t+1} <= epsilon + L*e_t, so e_t <= epsilon * sum_{j=0}^{t-1} L^j. With L < 1 the bound tends to epsilon/(1-L); with L = 1 it grows as t*epsilon; with L > 1 it grows quickly. If the step error or L varies over time, recompute the recursion instead of reusing the fixed-parameter formula. Whether an empirical model meets the per-state bound, leaves its working range, or meets an intervention outside the original action set cannot be answered by the proposition. An approximate bridge always carries its horizon.

## F6 Task Families and the Coarsest Sufficient Partition

Let X be finite, Q a set of target queries, U a set of allowed actions, and H a horizon. Define x ~_H x' when every query in Q gives the same answer after every action sequence of length at most H. The classes of ~_H keep exactly the answers of all tasks within the horizon, and ~_H is the unique coarsest partition that does so. **F6.** A fixed-horizon sufficient partition need not be closed under the dynamics over that horizon; the coarsest partition closed under every F_u (written ~_*) is also unique, and on a complete finite table it can be computed by Moore-style partition refinement.

The simplification principle follows: merge states that the asked targets and allowed actions cannot distinguish, and keep a difference only when a task or operation actually separates the states. Adding targets or actions leaves the partition unchanged or refines it; shortening the horizon, narrowing the use, or restricting operations can make a simpler representation sufficient. Adjusting the task forms a new legitimate question but never shows the original task was completed. Epsilon-tolerance is not transitive, so approximate similarity cannot stand in for an equivalence relation. Which targets must be kept, which actions are allowed, and which errors are acceptable are fixed by domain facts, normative reasons, and real authority respectively; the result never declares a uniquely correct natural level and never shrinks a person's legitimate claim into an existing prediction target.

## Worked Example: Two Queues

Two ordered queues (q1, q2) in {0,...,30}^2 give 961 states, taken as equally likely only to compute expected error. The task is local overload, max(q1, q2) > 15.

- Keeping only the mean m merges (0,20) and (10,10), which differ on overload. The minimum classification error is exactly 85 of 961 states (about 8.84%).
- The rule "report overload only when the mean exceeds 15" errs on 240 states. The extra 155 errors come from rule choice, not from unavoidable aggregation loss.
- If the task becomes recovering the maximum queue length, the mean-15 fiber contains (0,30) and (15,15), so the best real-valued output 22.5 has worst error 7.5; forcing integer output raises the best radius to 8. The output constraint itself changes the answer.
- Adding the maximum M answers overload and maximum exactly. Under symmetric service of up to c items per queue per round with no arrivals, (m, M) closes dynamically. Under an operation that binds capacity by position, (15, 10), the same-representation states (0,20) and (20,0) become (0,10) and (5,0), and closure fails. With three queues, (20,20,5) and (20,15,10) share mean 15 and maximum 20 yet leave totals 10 and 5 after serving 15 each, so the two-queue result does not extrapolate.

The example keeps positive and negative results together: a total answers total questions exactly, adding one task-relevant variable repairs part of the shortfall, and the same addition may not suit positional intervention, heterogeneous dynamics, or higher dimensions. Recovering all micro information is not the success condition of every task.

## History Increments Created by Representation Omission

On the same 961 initial states, serve up to 5 items per queue per round with no arrivals and predict the mean after round two (Appendix C.11). Minimum mean squared error: current mean 0.579; current mean plus initial mean 0.271; full current two-queue state 0; full current state plus initial mean 0. (0,20) and (10,15) both have current mean 7.5 after round one but different futures; the initial mean helps only because the current projection folded a difference that the full current state already carries. A historical predictive increment can therefore arise from what the current representation omits; it does not show that the real system has no memory, and when the full current carrier is unavailable no one may claim to have excluded a historical increment. Report total historical effect, current carrier, and conditional residual separately, as `ariadne-evidence` requires for G3.

## Three Composition Boundaries

Whether conversions compose into one final answer, whether causal effects chain, and whether actions can be executed jointly within resources are questions about functions, joint responses, and constraint sets respectively (Appendix C.12). They can appear in one workflow, and **no single generic "connected" status may stand in for the others**.

- **Function boundary** (F4): each stage completing its local task does not make the final query recoverable.
- **Joint-response boundary** (§2.4.2): with types s in {0,1} at equal weight, m(a) = a(1-s), y(a,m) = s*m, both link averages are 1/2 while the chain effect is 0, because different types carry the two links. Edge averages are never multiplied unconditionally; an independently identified total effect is not withdrawn by this counterexample.
- **Resource boundary**: two unit tasks each need one full period and must both finish before the end of period one, whose capacity is 1. Each is feasible alone; jointly no schedule exists. Capacity 2 in period one, or lawfully moving one deadline to period two when period two has capacity 1, restores joint feasibility; with both original deadlines fixed, extra capacity in period two cannot recover them. The conclusion follows from the given constraints and certifies no real demand, capacity, or authorization.

Representation sufficiency, computability, accessibility, implementability, resource availability, and the right to adopt are argued separately along the concrete use. At chain level, also check that the final task matches the stepwise tasks and that no shared resource has been promised twice. When a chain breaks, name the breakpoint type (representation, identification, clock, capacity, rule, material reach, authority), revise that breakpoint, and keep the finite results earned upstream (§1.11).

## Mathematical Scale-Bridge Discipline

Approximate commutation between a coarse-graining M, a micro dynamic F, and a macro dynamic Fbar, ||M(F_t(x)) - Fbar_t(M(x))|| <= epsilon, may be discussed only within stated initial conditions, parameter domain, error norm, and time interval (Appendix C.5). Agreement on one statistic is not equivalence of the whole state; a proof states limit order, error control, and valid time; long-run conclusions do not follow from short-run approximation alone. A bridge that claims more than a descriptive translation carries all eight fields together: `source_object`, `target_object`, `limit_or_scale_law`, `initial_conditions`, `history_structure`, `error`, `valid_time`, and `failure_boundary`. Missing fields leave a candidate bridge or test requirements, never a strong transfer claim.

This discipline does not show that every scale transfer loses task-relevant information; it does not import a kinetic equation or physical model into a social or psychological object; and it never treats the loss in a social translation as physical entropy. That the mathematics holds, that a real object satisfies the premises, and which option is actually chosen are three different responsibilities.

## Cross-Text Difference Retention

When a run uses this source together with another contract text, align reasoning responsibilities and boundaries while each text keeps its own definitions, objects, arguments, operating form, chapter order, artifact count, and numbering (Appendix C.4). Check correspondence item by item: proposition layering, question-family contracts, null results, scale closure, non-commutation tests, inference dependencies, information identity, artifact systems, typed unknowns, experimental evaluation, capability evidence, and model lifecycle. A name, analogy, example, or familiar step sequence never replaces the other text's complete contract; the nine scale operators are not forced into one-to-one alignment with another text's operator steps; the fourteen-section scale record is not merged with another closed artifact system. Only the minimum semantics are shared: preserved, changed, collapsed, omitted, new unknowns, source lineage, applicability, residuals, and stopping. Agreement between the two texts is one shared lineage, never two independent pieces of evidence. When only one text is supplied, mark this work `not_applicable` with the reason.

## Method Record Use

- Put the task the representation must serve in `object_contract.task_profile`; record whether static recovery, dynamic closure, or intervention sufficiency is being claimed in the claim text.
- Register formal results as F claims with the model premises in the text, and keep any real-world mapping as a separate G or E claim that `depends_on` the F claim.
- Record joins the conclusion needs, their boundary type, and breakpoints in `unknowns_and_counterevidence` until each is evidenced.
- Set `scale_scope.transform_kind` to the move actually made; a pure formal analysis with no transfer uses `none` with `not_needed`.
- Keep `authorization_effect: none`: F3's qualifying sets presuppose authority; they never create it.
