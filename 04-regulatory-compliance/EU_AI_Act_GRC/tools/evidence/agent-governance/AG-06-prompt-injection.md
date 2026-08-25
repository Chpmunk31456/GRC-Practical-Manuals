# AG-06 — Prompt-Injection and Untrusted-Instruction Handling

**Control objective:** Prevent AI agents from treating instructions embedded in untrusted content as authorized commands without validation and appropriate human review.

**Control owner:** ____________________  
**System / use case:** ____________________  
**Review frequency:** Quarterly and after material model/tool changes or incidents.

## Implementation
- Identify untrusted instruction sources such as web pages, email, uploaded files, third-party tool output, and retrieved content.
- Separate data from authoritative instructions wherever technically feasible.
- Flag suspicious or conflicting instructions to the user or operator.
- Require explicit approval before acting on instructions originating from untrusted content when consequential actions are possible.
- Apply allowlists, sandboxing, policy enforcement, and tool constraints where appropriate.
- Record injection detections, blocked actions, overrides, and incidents.

## Required evidence
- prompt-injection threat model;
- trusted/untrusted source classification;
- tool allowlists and execution constraints;
- test cases and adversarial-evaluation results;
- blocked-action logs;
- incident and corrective-action records.

## Audit test
1. Review the system's trust-boundary design.
2. Test representative malicious or conflicting embedded instructions.
3. Verify untrusted content cannot silently expand agent authority.
4. Confirm consequential actions require the intended approval path.
5. Verify detections and blocked attempts are logged and reviewed.

## Exceptions / findings
| Date | Exception or finding | Risk | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Framework mapping
- EU AI Act: risk-management, cybersecurity, human-oversight, and logging implementation support where applicable.
- ISO/IEC 42001: map after licensed-source verification.
- NIST AI RMF: Map / Measure / Manage.
- NIST CSF 2.0: Protect / Detect / Respond.

> This is a defensive governance control. It does not imply that prompt injection can be eliminated completely.
