# Review: challenge, correct, and continue

Use this path to test a judgment, model, draft, implementation, decision, or the method itself; incorporate new evidence; repair a failed result; or decide whether to pause, narrow, or retire a practice. Deliver the review's conclusion and, when authorized, the actual correction. A review that sustains the existing judgment with reasons is also a valid result.

Use the [kernel](../references/kernel.md), [responsibility](../references/responsibility.md), and [continuity](../references/continuity.md). The [detailed gates](../references/library/gates-core.md), [governance lifecycle](../references/library/governance-lifecycle.md), and [application contracts](../references/library/application-contracts.json) support demanding cases. Their specialized responsibilities do not require every ordinary review to reproduce a universal form.

## Set a target that can fail

Identify the artifact or judgment, version, intended use, claimed result, and what the review must establish. Distinguish a wrong conclusion, incomplete evidence, an invalid inference, implementation departure, failure of actual delivery, and an unresolved value disagreement. A test that checks only whether the expected fields exist does not establish that the result is correct or useful.

Ask the strongest relevant contrary question. What observation, counterexample, competing interpretation, domain baseline, excluded position, changed condition, or execution trace could make this conclusion wrong? Give a reviewer enough common context to examine it without feeding a preferred verdict. Independent workers can investigate independent subquestions, but agent count, consensus, or varied wording does not create independent evidence.

Preserve the scope of review. Checking source alignment is not a test of real-world effectiveness; running a simulation is not an empirical replication; a schema check is not a semantic review; a local smoke test is not proof of broad reliability. Say exactly what passed, failed, or was not examined.

## Attack the dependence, not everything at once

Trace the important claim to its material, inference, bridge, and operating conditions. For a source problem, check what was read and whether the cited material says what the claim needs. For a causal problem, check the target effect, identification, competitors, and relevant changes in measurement or selection. For a formal problem, test assumptions and boundary cases or examine the proof. For an artifact, exercise the user-visible behavior and failure conditions that matter.

Try the smallest meaningful disturbance: a boundary change, a plausible competitor, a reversed assumption, an unavailable interface, a delayed resource, or a different but relevant case. Ask which conclusion changes and which remains. Distinguish a representation that cannot recover the required distinction from a sound representation used with the wrong rule. A proposed grouping's failure is not evidence that independently observed objects never existed (§2.9, §4.18, §5.10.2).

Apply a defect only along its dependencies. If one source fails, remove or qualify claims that need it; retain independent observations, successful local results, proofs under intact premises, and criticism with separate support. A broader synthesis may need revision without erasing its sound components. Do not average incompatible claims or replace disagreement with a compromise score.

The review can be generative. Turn a counterexample into a refined representation; locate a failed interface and draft a minimal repair; replace a questionable condition and derive a new option; identify the observation that would distinguish remaining mechanisms. If the question itself excludes the decisive issue, reopen it openly while retaining the original result and failure. Follow [discover](discover.md), [understand](understand.md), or [project](project.md) as needed rather than merely issuing a red flag.

## Test real products and claimed benefits

For a requested artifact, verify the endpoint the user actually asked for: a saved complete draft, a working local program, a functioning prototype, an externally adopted change, or a delivered remedy. The endpoint determines the evidence needed. A command issued is not proof of its effect; an unobserved timeout remains unknown until resolved. A completed local artifact need not await every distant social outcome to count as delivered (§13.11.2).

Choose tests that could catch meaningful failure. A calculation needs an independently checkable case or invariant; a parser needs realistic inputs and a relevant malformed case; a policy needs cases exposing power, resource, and correction failures; a decision needs sensitivity to decisive facts and normative premises. Fix an observed defect and rerun the affected checks. Broaden testing when the defect, changed implementation, intended use, or unresolved uncertainty justifies it. Do not accumulate redundant checks to signal rigor.

When claiming that Ariadne or any derived procedure improves performance, compare against adequate simpler or domain methods on comparable tasks, information, and resources. Include result quality and the burden on the user, maintainer, and collaborators. Separate an individual success, coverage of a class of questions, and net benefit of the framework. A collection of polished examples, field counts, full reading, or passing format tests proves none of these (§4.17.4, §16.16, §16.24).

## Review choices without making dissent a veto ritual

Distinguish disagreement that remains, a material reason not yet answered, and a failed protection. Test whether an objection was safely received and understood, whether the decision should change, and whether any resulting rights or resources actually reached their destination. Recognition without necessary correction is insufficient. A reasoned decision can remain unchanged when the objection does not overturn it; a cosmetic concession is not a requirement (§14.5, §14.7, §16.19).

Where review reveals a protection or authority failure, pause or narrow the affected adoption or action and route correction to the competent actor. Preserve independently grounded duties and safe ongoing support. A pause in the challenged intervention does not authorize abandoning people who depend on continuing care, maintenance, or handoff. Do not demand that a protected person expose private material or bear new risk merely to demonstrate a failure.

## Continue with a changed state

After a review, say what changed: the evidence, interpretation, representation, rule, artifact, permission, responsibility, or the degree of confidence. Record only the state needed to continue accurately. Preserve failures and pre-outcome commitments; add a new version rather than overwriting an inconvenient result. A later repair does not convert an earlier failed forecast into a success.

Resume the useful work that is now supported. A source correction may permit a revised explanation; an implementation fix may permit delivery; a reopened question may yield a new design. Repetition is warranted when new evidence, a failed check, or an unresolved material concern can change the answer. There is no automatic two-round stop and no obligation to repeat a full review after every harmless edit. When further work cannot reasonably change the requested conclusion or artifact within the available resources, deliver the result, its remaining limits, and the concrete trigger for reopening.

Retire a model or procedure when its applicability has expired, drift invalidates its use, a better adequate method replaces it, or its burden is not justified. Preserve the evidence and independent local achievements, identify affected users and continuing duties, and provide a usable transition. Retiring a framework is not a judgment that its former users lacked competence (§16.16, §16.24).

## Worked route: a promising policy with a failed appeal channel

Suppose a draft allocation policy improves average turnaround but allows only the allocating manager to dismiss objections. Review first preserves the measured turnaround result. It separately tests whether the affected people can challenge the agenda and final decision, especially when that manager benefits. If required independent review is absent, the average gain does not cure the adoption defect.

Produce a corrected appeal clause, name an independent reviewer with the necessary scope, preserve protected disclosure, and set a response deadline and remedy path. Test a concrete disputed case through the draft procedure. If an objection has been fairly examined and does not change the justified allocation, the final allocation can remain unchanged with reasons. If the objection identifies an actual wrong allocation, verify the resulting correction or resource delivery before calling that remedy complete.

## Deliver a usable conclusion

State the verdict at the right scope, the findings that determine it, the corrected result or artifact when in scope, checks actually performed, and the remaining material issue. Distinguish “no defect found in these checks” from “verified effective everywhere.” Link or provide the deliverable; do not make the user reconstruct it from review comments. Follow [composition](../references/composition.md) when separate branches need different outcomes.

Source basis: §§2.9, 2.14, 4.17.4, 4.18, 5.10.2, 6.10.1, 13.11.2, 14.5-14.7; Part 16. This path is a derived critical and corrective practice, not certification of reality or of the source theory.
