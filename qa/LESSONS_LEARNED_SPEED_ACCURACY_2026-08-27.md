# Lessons Learned — Speed, Accuracy, and Immediate Issue Resolution

**Date:** 2026-08-27

## Lesson learned

Known machine-fixable issues must never sit idle. If a defect, stale dependency, failed check, reconciliation gap, metadata mismatch, or workflow problem is already known and can be resolved by repository automation or controlled engineering work, it should be corrected immediately rather than deferred to a later review cycle.

The objective is first-pass correctness with minimum rework: detect state before generating work, preserve already-green exact-head evidence, avoid unnecessary rebuilds, and spend compute only on real unresolved defects.

## Immediately implemented action

Effective immediately for the controlled manual series and reusable release pipeline:

1. **Resolve known machine-fixable issues immediately.** Human-only gates are the only acceptable intentional hold points.
2. **Inspect exact candidate state before mutation.** Confirm branch/base SHA, dependency chain, diff scope, workflow status, and release artifact binding first.
3. **Preserve green evidence whenever possible.** Do not modify a candidate SHA merely to record status; use PR-side reconciliation evidence when content does not need to change.
4. **Fail closed with precise diagnostics.** A failed workflow should identify the smallest objective defect needed for remediation rather than trigger broad rebuild/rework.
5. **Do not rerun already-green expensive workflows without cause.** Rebuild only when a material content, source-state, workflow, security, or publication change invalidates prior evidence.
6. **Correct state metadata immediately.** Completed work must not remain marked open, because stale metadata causes duplicate generation, wasted compute, and confusion.
7. **Use clean restacks instead of patching contaminated branches.** When a downstream branch is stale or polluted, rebuild a narrow overlay on the exact current upstream head rather than spending cycles repairing an unreliable history.
8. **Reconcile dependencies immediately after upstream change.** Retarget or restack downstream candidates as soon as the upstream release changes their valid base.
9. **Separate machine completion from human approval.** Automation may complete all machine-side reconciliation, but semantic, accessibility, legal, or other mandatory human gates remain fail-closed.
10. **Optimize for readable outputs.** Diagnostics, QA reports, and release records should be concise, actionable, and understandable by a practitioner without unnecessary internal noise.

## Expected benefit

This rule is intended to improve speed and accuracy while lowering compute cost, repeated CI runs, human rework, and energy use. It must never be used to bypass source verification, security, provenance, accessibility, localization, human review, or Final Human Release Approval.

## Evidence of immediate use

The rule has already been applied to Manuals 05–07:

- Manual 05 and Manual 06 reconciliation preserved their exact green publication-candidate SHAs instead of creating bookkeeping commits that would invalidate publication artifacts.
- Manual 07 stale localization status was corrected immediately so completed `es-419` and `pt-BR` drafts are not regenerated unnecessarily; the remaining human semantic review is now represented separately.
- Manual 08 has been identified as stale/non-mergeable and is assigned to clean-restack treatment rather than incremental repair of a contaminated branch.

This lesson is reusable for all later manuals, repository-wide modernization work, and the future training-manual repository.