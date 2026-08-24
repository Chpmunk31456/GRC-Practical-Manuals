# AG-03 — Standing Authority and Permission Duration

**Control objective:** Ensure persistent AI-agent authority is explicitly approved, narrowly scoped, time-bounded, visible, and periodically revalidated.

**Control owner:** ____________________  
**System / use case:** ____________________  
**Review frequency:** Monthly for high-impact standing authority; otherwise at least quarterly.

## Implementation
- Default permissions to one-time, session, or task scope.
- Require explicit approval for persistent authority.
- Define expiration and reauthorization periods.
- Maintain a register of active standing grants.
- Surface last-used date and business justification.

## Required evidence
- standing-authority register;
- approval records;
- expiration configuration;
- periodic recertification records;
- dormant-authority removal records.

## Audit test
1. Sample standing grants.
2. Verify each grant has owner, purpose, scope, approval, and expiry.
3. Check that dormant grants are removed.
4. Verify reauthorization occurred when required.
5. Confirm one-time authority was not silently converted to persistent authority.

## Exceptions / findings
| Date | Exception or finding | Risk | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Framework mapping
- EU AI Act: human oversight and governance implementation support where applicable.
- ISO/IEC 42001: map after licensed-source verification.
- NIST AI RMF: Govern / Manage.
- NIST CSF 2.0: Govern / Protect.
