# AG-04 — Immediate Revocation and Kill Capability

**Control objective:** Ensure authorized personnel can promptly suspend or revoke AI-agent access and execution authority when risk, misuse, error, incident, or business need requires it.

**Control owner:** ____________________  
**System / use case:** ____________________  
**Review frequency:** Test at least semiannually and after material platform change.

## Implementation
- Provide documented pause, disable, and revoke mechanisms.
- Define who may invoke emergency suspension.
- Ensure revocation propagates to connected tools and credentials.
- Define escalation and recovery procedures.
- Test kill capability without relying solely on the agent itself.

## Required evidence
- revocation procedure;
- IAM/tool disablement configuration;
- test results and timestamps;
- incident revocation records;
- recovery and reauthorization records.

## Audit test
1. Select representative agent integrations.
2. Trigger an authorized test suspension.
3. Confirm access and execution cease within the defined target.
4. Confirm downstream tokens/sessions are invalidated where applicable.
5. Verify restoration requires explicit authorization.

## Exceptions / findings
| Date | Exception or finding | Risk | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Framework mapping
- EU AI Act: human intervention/stop and governance implementation support where applicable.
- ISO/IEC 42001: map after licensed-source verification.
- NIST AI RMF: Manage.
- NIST CSF 2.0: Protect / Respond.
