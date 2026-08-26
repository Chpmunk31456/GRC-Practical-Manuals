#!/usr/bin/env python3
"""Reusable fail-closed release preflight for Manuals 05-08.

Purpose:
- catch affirmative compliance/certification overclaims without flagging required negative disclaimers;
- verify core release-boundary language early;
- verify HIPAA current-law vs proposed-rule separation;
- inspect localized sources when present, without pretending automated checks are semantic approval;
- regression-test detector behavior so known false-positive classes cannot silently return.

This preflight is intentionally narrower than human semantic review. A PASS means the
machine-detectable boundary checks passed; it does not constitute human approval.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MANUALS = {
    "05": ROOT / "03-assurance-and-audit" / "AI_Auditing_and_Assurance",
    "06": ROOT / "04-regulatory-compliance" / "HIPAA_Implementation_Series",
    "07": ROOT / "06-cloud-and-technology-risk" / "AI_Security_and_Lifecycle",
    "08": ROOT / "07-third-party-risk" / "Vendor_Risk_Lifecycle",
}

LOCALES = ("English", "es-419", "pt-BR")

# Detect affirmative overclaims only. Required negative disclaimers are filtered first.
AFFIRMATIVE_OVERCLAIMS = {
    "English": [
        r"\b(?:this manual|this framework|this guidance|NIST AI 600-1|AI RMF|AAIA)\s+(?:is|provides|guarantees|certifies)\s+(?:a\s+)?(?:certification|legal compliance|compliance|conformity|audit opinion)\b",
    ],
    "es-419": [
        r"\b(?:este manual|este marco|esta guía|NIST AI 600-1|AI RMF|AAIA)\s+(?:es|proporciona|garantiza|certifica)\s+(?:una?\s+)?(?:certificación|cumplimiento legal|cumplimiento|conformidad|opinión de auditoría)\b",
    ],
    "pt-BR": [
        r"\b(?:este manual|esta estrutura|esta orientação|NIST AI 600-1|AI RMF|AAIA)\s+(?:é|fornece|garante|certifica)\s+(?:uma?\s+)?(?:certificação|conformidade legal|conformidade|parecer de auditoria)\b",
    ],
}

NEGATION_MARKERS = {
    "English": ("does not", "do not", "not a", "not certification", "cannot", "doesn't"),
    "es-419": ("no crea", "ni crea", "no constituye", "no es", "no garantiza", "no certifica"),
    "pt-BR": ("não cria", "não constitui", "não é", "não garante", "não certifica", "nem cria"),
}

REQUIRED_BOUNDARY_FILES = (
    "qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md",
    "qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md",
    "qa/RELEASE_READINESS_PRESTAGE.md",
)


def iter_markdown(directory: Path):
    if not directory.exists():
        return []
    return sorted(directory.glob("*.md"))


def overclaim_hits(locale: str, text: str) -> list[str]:
    hits: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        lowered = line.casefold()
        if any(marker.casefold() in lowered for marker in NEGATION_MARKERS[locale]):
            continue
        for pattern in AFFIRMATIVE_OVERCLAIMS[locale]:
            if re.search(pattern, line, re.I):
                hits.append(f"line {lineno}: {pattern!r}")
    return hits


def scan_overclaims(locale: str, text: str, label: str, errors: list[str]) -> None:
    for hit in overclaim_hits(locale, text):
        errors.append(f"{label}: {hit}")


def self_test_detector(errors: list[str]) -> None:
    fixtures = [
        ("English", "NIST AI 600-1 is a certification.", True),
        ("English", "This text does not create certification or legal compliance.", False),
        ("es-419", "NIST AI 600-1 es una certificación.", True),
        ("es-419", "Este texto no reproduce el texto de NIST ni crea certificación.", False),
        ("pt-BR", "NIST AI 600-1 é uma certificação.", True),
        ("pt-BR", "Este texto não reproduz o texto do NIST nem cria certificação.", False),
    ]
    for locale, text, should_hit in fixtures:
        hit = bool(overclaim_hits(locale, text))
        if hit != should_hit:
            expectation = "detect" if should_hit else "ignore"
            errors.append(f"detector regression: {locale} fixture should {expectation}: {text!r}")


def check_manual(number: str, base: Path, errors: list[str], notes: list[str]) -> None:
    if not base.exists():
        errors.append(f"Manual {number}: directory missing: {base.relative_to(ROOT)}")
        return

    for rel in REQUIRED_BOUNDARY_FILES:
        path = base / rel
        if not path.is_file():
            errors.append(f"Manual {number}: required release-boundary file missing: {rel}")

    for locale in LOCALES:
        source_dir = base / locale / "source"
        files = iter_markdown(source_dir)
        if not files:
            if locale == "English":
                errors.append(f"Manual {number}: English controlled source missing")
            else:
                notes.append(f"Manual {number} {locale}: localized source not staged yet; preflight deferred")
            continue
        text = "\n".join(p.read_text(encoding="utf-8") for p in files)
        scan_overclaims(locale, text, f"Manual {number} {locale}", errors)

    # Manual 06 has an additional legal-status boundary. Require explicit separation
    # in release-readiness/source-verification material and reject wording that turns
    # the Security Rule NPRM into current law.
    if number == "06":
        boundary_text = "\n".join(
            p.read_text(encoding="utf-8")
            for p in [base / "qa/RELEASE_READINESS_PRESTAGE.md", base / "qa/SOURCE_VERIFICATION_2026-08-26.md"]
            if p.is_file()
        )
        lowered = boundary_text.casefold()
        if "current law" not in lowered or "proposed" not in lowered:
            errors.append("Manual 06: current-law/proposed-rule separation is not explicit")
        bad_patterns = [
            r"security rule nprm\s+(?:is|became|constitutes)\s+current law",
            r"proposed rule\s+(?:is|became|constitutes)\s+current law",
        ]
        for pattern in bad_patterns:
            if re.search(pattern, boundary_text, re.I):
                errors.append(f"Manual 06: legal-status overclaim matched {pattern!r}")


def main() -> int:
    errors: list[str] = []
    notes: list[str] = []

    self_test_detector(errors)
    for number, base in MANUALS.items():
        check_manual(number, base, errors, notes)

    print("Manuals 05-08 reusable release preflight")
    for note in notes:
        print(f"  NOTE: {note}")
    for error in errors:
        print(f"  ERROR: {error}")

    if errors:
        print("FAIL: machine-detectable release boundaries did not pass")
        print("Human semantic approval remains mandatory and is not replaced by this check.")
        return 1

    print("PASS: machine-detectable release boundaries passed")
    print("Automated QA does NOT constitute localization semantic approval or Final Human Release Approval.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
