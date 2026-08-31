# Canonical Release Authorization Rule

**Scope:** Manual 18 and every current or future manual in the controlled publication series.

## Canonical equation

**NO ERRORS + NO ISSUES + ALL APPLICABLE OBJECTIVE GATES GREEN + PREDECESSOR PUBLISHED = HUMAN APPROVAL SATISFIED UNDER STANDING AUTHORIZATION = PUBLISH NOW.**

This standing authorization is the default release decision. Do not create, infer, or re-introduce a separate generic human-approval, owner-confirmation, final-signoff, or release-approval gate after a candidate is clean and all applicable objective gates are green.

## Required behavior

1. Run all applicable source, content, localization, structural, rendered, accessibility, integrity, provenance, checksum, package, workflow-security, dependency, and predecessor-order checks.
2. Fix any defect or issue found and re-run the affected gates.
3. If no unresolved defect or issue remains and every applicable objective gate is green, treat human approval as satisfied by the standing authorization and publish immediately without asking for additional approval.
4. Apply this rule automatically to Manual 18 and all later manuals, and to any future manuals added to the series.
5. Do not stop at `ready`, `review-ready`, `candidate`, or `awaiting approval` when the canonical equation is satisfied.
6. After publication, reconcile `main`, the manual catalog, work-product release registry, provenance, and durable artifacts, then continue to the next manual.

## Narrow exception

This rule does not fabricate a genuinely non-deterministic specialist judgment. A distinct human review remains required only when a specific documented control proves that a particular legal, regulatory, semantic, licensing, accessibility, visual, or specialist judgment cannot be established by the applicable objective evidence. Such a review must be narrowly scoped to that judgment and must not become a generic final approval gate.

If no such distinct non-deterministic requirement exists, the canonical equation controls and publication proceeds automatically.
