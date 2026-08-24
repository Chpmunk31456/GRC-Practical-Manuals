# AG-02 — Least-Privilege Agent Access

**Control objective:** Limit each AI agent to the minimum data, systems, tools, and actions necessary for its approved purpose.

**Control owner:** ____________________  
**System / use case:** ____________________  
**Review frequency:** Quarterly and after scope change.

## Implementation
- Inventory every permission granted to the agent.
- Separate read, write, execute, and delete authority.
- Default to read-only and resource-specific scopes.
- Prohibit access not justified by the approved use case.
- Review dormant or excessive permissions and remove them.

## Required evidence
- permission inventory and approved scope;
- IAM/tool configuration exports;
- access-review records;
- denied-scope records;
- change tickets for permission increases;
- revocation evidence.

## Audit test
1. Compare granted permissions with documented business need.
2. Verify write/delete/execute privileges are explicitly justified.
3. Test whether the agent can access out-of-scope resources.
4. Confirm periodic access reviews occurred.
5. Verify excessive privileges were removed promptly.

## Exceptions / findings
| Date | Exception or finding | Risk | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Framework mapping
- EU AI Act: governance and human-oversight implementation support where applicable.
- ISO/IEC 42001: map after licensed-source verification.
- NIST AI RMF: Govern / Manage.
- NIST CSF 2.0: Govern / Protect, especially identity and access-control practices.

> Crosswalks support implementation and do not establish compliance by themselves.
