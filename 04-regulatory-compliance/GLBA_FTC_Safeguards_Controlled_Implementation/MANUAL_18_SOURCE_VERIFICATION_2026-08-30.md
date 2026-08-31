# Manual 18 — GLBA / FTC Safeguards Rule Authoritative Source Verification

**Manual:** 18 — GLBA / FTC Safeguards Controlled Implementation  
**Verification date:** 2026-08-30  
**State:** controlled-build source verification; not publication authorization

## Authoritative source set

Primary implementation authority for the FTC Safeguards Rule lane shall be anchored to the current rule text and official FTC guidance. Current FTC guidance confirms that the Safeguards Rule applies to financial institutions subject to FTC jurisdiction, requires a written information security program with administrative, technical, and physical safeguards, and reflects the 2021 amendments plus the 2023 security-event reporting amendment.

Verified official sources:
- https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know
- https://www.ftc.gov/business-guidance/blog/2024/05/safeguards-rule-notification-requirement-now-effect
- https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act/safeguards-rule-form

## Current regulatory consequence

The security-event reporting requirement is in effect. Official FTC guidance states that covered financial institutions must notify the FTC as soon as possible and no later than 30 days after discovery of a notification event involving unauthorized acquisition of unencrypted customer information affecting at least 500 consumers, subject to the rule's definitions and conditions.

Manual 18 architecture shall therefore keep these layers distinct:

1. statutory GLBA context;
2. 16 CFR Part 314 Safeguards Rule requirements;
3. FTC amendments and effective-date consequences;
4. official FTC compliance guidance and examples;
5. organization-specific implementation practices and evidence objects.

Informal guidance shall not be represented as if it were regulatory text, and FTC jurisdiction shall not be generalized to institutions supervised by other GLBA regulators.

## Controlled-build requirements enabled by this verification

The existing 32-topic architecture may continue into source-mapped controlled construction. Each substantive requirement statement must preserve applicability, rule/guidance provenance, owner, implementation procedure, evidence, test method, exception/remediation path, and reassessment trigger. The notification-event workflow must preserve the current 500-consumer threshold and 30-day outer reporting period without turning either into a broader incident-notification rule outside the Rule's scope.

## Release-time gates

Before candidate freeze, reverify the current text of 16 CFR Part 314 and official FTC amendment/effective-date status. Publication remains fail-closed behind authoritative-source reconciliation, competent semantic/legal-regulatory review, controlled-English freeze, locale semantic review, trilingual parity, rendered/accessibility QA, security/provenance checks, durable artifact staging, exact-head QA, and sequential catalog/release-registry reconciliation.