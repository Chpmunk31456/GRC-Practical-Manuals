# Manual 07 — Authoritative Source Verification

**Manual:** AI Security and Lifecycle Controls  
**Verification date:** 2026-08-26  
**Controlled branch:** `build/ai-security-lifecycle-manual-07-2026`

## Verified source state

- **ISO/IEC 27090** is **not yet a published International Standard** as of this verification date. ISO lists it as **under publication**, stage **60.00**, first edition. Manual 07 must not represent it as a currently published final standard or as a source of mandatory requirements. Until ISO records publication at stage 60.60, it may be used only as a source-state watch / near-final reference with explicit status labeling.
- **ISO/IEC 5338:2023** is published, edition 1, December 2023, and defines AI system life-cycle processes.
- **ISO/IEC 42001:2023** is published, edition 1, December 2023, and remains the controlled AI management-system governance reference.
- **NIST AI RMF 1.0 / NIST AI 100-1** remains the current published AI Risk Management Framework baseline. NIST states that AI RMF 1.0 is being revised; Manual 07 must perform impact analysis before adopting any replacement baseline.
- **NIST AI 600-1** remains the published Generative AI Profile companion resource to AI RMF 1.0, published July 26, 2024.
- **NIST SP 800-218**, Secure Software Development Framework (SSDF) Version 1.1, remains a final NIST publication, published February 2022.
- **NIST SP 800-207**, Zero Trust Architecture, remains a final NIST publication, published August 2020.

## Controlled official sources

1. ISO — ISO/IEC 27090
   - https://www.iso.org/standard/56581.html
   - Current state: under publication, stage 60.00.

2. ISO — ISO/IEC 5338:2023
   - https://www.iso.org/standard/81118.html
   - Current state: published, stage 60.60.

3. ISO — ISO/IEC 42001:2023
   - https://www.iso.org/standard/42001
   - Current state: published.

4. NIST — AI Risk Management Framework (AI RMF 1.0)
   - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
   - https://www.nist.gov/itl/ai-risk-management-framework
   - Current state: AI RMF 1.0 remains published and is under revision.

5. NIST — AI RMF Generative AI Profile, NIST AI 600-1
   - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
   - Current state: published.

6. NIST — SP 800-218, Secure Software Development Framework
   - https://csrc.nist.gov/pubs/sp/800/218/final
   - Current state: final.

7. NIST — SP 800-207, Zero Trust Architecture
   - https://csrc.nist.gov/pubs/sp/800/207/final
   - Current state: final.

## Release implications

- Correct the shared authoritative-source registry before Manual 07 release so `iso-iec-27090` is not labeled `final` while ISO still reports stage 60.00.
- Preserve ISO/IEC 27090 as a watched source only until publication is confirmed; do not reproduce copyrighted ISO text.
- No baseline rewrite is required for ISO/IEC 5338:2023, ISO/IEC 42001:2023, NIST AI RMF 1.0, NIST AI 600-1, NIST SP 800-218, or NIST SP 800-207 based on this verification.
- Reverify all source states at the exact final candidate head. Any material source-state change reopens affected terminology, mappings, technical review, localization, graphics, QA, and release approval.

## Assurance boundary

This record verifies source state only. It does not establish that any AI system is secure, compliant, safe, certified, conformant, or free from exploitable weaknesses, and it does not create an audit opinion.
