# AG-05 — Credential Separation and Secure Handoff

**Control objective:** Prevent AI agents from receiving, storing, or exposing reusable human secrets when safer delegated authentication mechanisms are available.

**Control owner:** ____________________  
**System / use case:** ____________________  
**Review frequency:** At least quarterly and after authentication changes.

## Implementation
- Prefer scoped tokens, service identities, passkeys, or human takeover for authentication.
- Prohibit plaintext passwords, recovery codes, and private keys in prompts or agent memory.
- Separate human and agent identities where feasible.
- Rotate and revoke delegated credentials on schedule and after incidents.

## Required evidence
- authentication architecture;
- secret-handling standard;
- token/service-account inventory;
- rotation and revocation records;
- secret-scanning or DLP results;
- incident records.

## Audit test
1. Inspect representative authentication flows.
2. Verify reusable human secrets do not transit the agent.
3. Confirm agent tokens are scoped and time-bounded where possible.
4. Verify rotation and revocation controls operate.
5. Review logs for accidental secret exposure.

## Exceptions / findings
| Date | Exception or finding | Risk | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Framework mapping
- EU AI Act: security, governance, and oversight implementation support where applicable.
- ISO/IEC 42001: map after licensed-source verification.
- NIST AI RMF: Govern / Manage.
- NIST CSF 2.0: Protect.
