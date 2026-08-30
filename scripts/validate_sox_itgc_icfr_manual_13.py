#!/usr/bin/env python3
"""Fail-closed structural and source-boundary QA for Manual 13."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "04-regulatory-compliance" / "SOX_ITGC_ICFR_Controlled_Implementation"
BASELINE = ROOT / ".compliance" / "sox-itgc-icfr-manual-13-baseline.json"
SOURCES = ROOT / ".compliance" / "sox-itgc-icfr-manual-13-sources.json"
WATCH = ROOT / ".compliance" / "sox-itgc-icfr-manual-13-release-source-watch.json"

LOCALES = {
    "en": (MANUAL / "English" / "source", re.compile(r"^## Chapter (\d+) — ", re.M)),
    "es-419": (MANUAL / "Spanish_es-419" / "source", re.compile(r"^## Capítulo (\d+) — ", re.M)),
    "pt-BR": (MANUAL / "Portuguese_pt-BR" / "source", re.compile(r"^## Capítulo (\d+) — ", re.M)),
}


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def read_json(path: Path):
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    if not MANUAL.is_dir():
        fail("Manual 13 controlled-build directory missing")

    baseline = read_json(BASELINE)
    sources = read_json(SOURCES)
    watch = read_json(WATCH)

    if baseline.get("series_order") != 13:
        fail("baseline series_order must equal 13")
    if baseline.get("controlled_source_language") != "en":
        fail("controlled source language must be English")

    source_ids = {s.get("id") for s in sources.get("sources", [])}
    required = set(baseline.get("required_source_ids", []))
    if not required.issubset(source_ids):
        fail(f"missing required authoritative sources: {sorted(required - source_ids)}")

    future = next((s for s in sources.get("sources", []) if s.get("id") == "pcaob-as-2201-2026-amended"), None)
    if not future or future.get("status") != "approved-not-yet-effective" or future.get("effective_date") != "2026-12-15":
        fail("future-effective AS 2201 boundary is missing or incorrect")

    if not watch.get("release_gate", {}).get("required"):
        fail("release-time source freshness gate must remain required")

    for locale, (folder, pattern) in LOCALES.items():
        if not folder.is_dir():
            fail(f"missing locale source directory {locale}")
        text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(folder.glob("*.md")))
        chapters = [int(n) for n in pattern.findall(text)]
        if sorted(chapters) != list(range(1, 33)):
            fail(f"{locale} must contain exactly chapters 1-32 once; found {chapters}")
        if locale != "en":
            lowered = text.lower()
            if "assistido" not in lowered and "asistido" not in lowered:
                fail(f"{locale} must retain machine-assisted-draft boundary")

    impl_en = (MANUAL / "MANUAL_13_IMPLEMENTATION_PATHS.md").read_text(encoding="utf-8")
    impl_es = (MANUAL / "Spanish_es-419" / "source" / "RUTAS_DE_IMPLEMENTACION_MANUAL_13.md").read_text(encoding="utf-8")
    impl_pt = (MANUAL / "Portuguese_pt-BR" / "source" / "CAMINHOS_DE_IMPLEMENTACAO_MANUAL_13.md").read_text(encoding="utf-8")
    for locale, text in (("en", impl_en), ("es-419", impl_es), ("pt-BR", impl_pt)):
        if text.count("```mermaid") != 3:
            fail(f"{locale} implementation paths must contain exactly three memory graphics")
        if "Accessible explanation:" not in text and "Explicación accesible:" not in text and "Explicação acessível:" not in text:
            fail(f"{locale} implementation paths missing accessible explanations")

    prohibited = ["SOX certified", "guarantees SOX compliance", "official translation"]
    all_text = "\n".join(p.read_text(encoding="utf-8") for p in MANUAL.rglob("*.md"))
    for phrase in prohibited:
        if phrase.lower() in all_text.lower():
            fail(f"prohibited claim detected: {phrase}")

    print("PASS: Manual 13 controlled-source structure and source boundaries validated")


if __name__ == "__main__":
    main()
