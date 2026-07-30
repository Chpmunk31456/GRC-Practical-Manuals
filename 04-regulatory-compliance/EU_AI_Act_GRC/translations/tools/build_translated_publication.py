#!/usr/bin/env python3
"""Assemble a translated EU AI Act edition and verify structural parity."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT_REL = Path("04-regulatory-compliance/EU_AI_Act_GRC")
TRANS_REL = ROOT_REL / "translations"
LANG_META = {
    "es-419": {
        "title": "Manual de Cumplimiento GRC de la Ley de Inteligencia Artificial de la UE",
        "subtitle": "Guía práctica de gobernanza, riesgos, cumplimiento, controles, evidencia, auditoría e implementación",
        "status": "Edición controlada en español para revisión",
        "disclaimer": "Este manual es un recurso educativo y operativo de gobernanza. No sustituye asesoría jurídica calificada, una evaluación de conformidad, la revisión de un organismo notificado, instrucciones de una autoridad competente, obligaciones sectoriales ni el texto consolidado vigente de la legislación aplicable.",
        "how": "Use cada capítulo para identificar el requisito aplicable, comprenderlo en lenguaje claro, aplicar el ejemplo de GlobalWay Travel Services, definir la actividad de control, conservar evidencia y realizar una prueba de auditoría.",
        "appendices": "Apéndices",
        "lang": "es-419",
    },
    "pt-BR": {
        "title": "Manual de Conformidade GRC da Lei de Inteligência Artificial da UE",
        "subtitle": "Guia prático de governança, riscos, conformidade, controles, evidências, auditoria e implementação",
        "status": "Edição controlada em português brasileiro para revisão",
        "disclaimer": "Este manual é um recurso educacional e operacional de governança. Não substitui assessoria jurídica qualificada, avaliação de conformidade, análise de organismo notificado, orientação de autoridade competente, obrigações setoriais ou o texto consolidado vigente da legislação aplicável.",
        "how": "Use cada capítulo para identificar o requisito aplicável, compreendê-lo em linguagem clara, aplicar o exemplo da GlobalWay Travel Services, definir a atividade de controle, manter evidências e executar um teste de auditoria.",
        "appendices": "Apêndices",
        "lang": "pt-BR",
    },
}


@dataclass(frozen=True)
class Record:
    item: str
    path: str
    sha256: str
    bytes: int
    lines: int


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_builder(repo_root: Path):
    path = repo_root / ROOT_REL / "tools" / "build_english_publication.py"
    spec = importlib.util.spec_from_file_location("english_builder_for_translation", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load canonical selector: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def demote_heading(text: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            lines[index] = "## " + line[2:]
            break
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--language", choices=sorted(LANG_META), required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    lang = args.language
    meta = LANG_META[lang]
    source_root = repo_root / TRANS_REL / lang / "source"
    chapters_dir = source_root / "chapters"
    appendices_dir = source_root / "appendices"
    out_dir = repo_root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    builder = load_builder(repo_root)
    english_root = repo_root / ROOT_REL
    english_chapter_map: dict[int, list[Path]] = {}
    for path in sorted((english_root / "chapters").glob("*.md")):
        match = builder.CHAPTER_RE.match(path.name)
        if match:
            english_chapter_map.setdefault(int(match.group("number")), []).append(path)
    english_appendix_map: dict[str, list[Path]] = {}
    for path in sorted((english_root / "appendices").glob("*.md")):
        match = builder.APPENDIX_RE.match(path.name)
        if match:
            english_appendix_map.setdefault(match.group("letter"), []).append(path)

    selected_english_chapters = [builder.choose_chapter(english_chapter_map.get(n, []), n) for n in range(1, 139)]
    selected_english_appendices = [
        builder.choose_appendix(english_appendix_map.get(chr(code), []), chr(code))
        for code in range(ord("A"), ord("Z") + 1)
    ]

    translated_chapters: list[Path] = []
    for number, english in enumerate(selected_english_chapters, start=1):
        translated = chapters_dir / english.name
        if not translated.exists() or not translated.read_text(encoding="utf-8").strip():
            raise ValueError(f"Missing translated Chapter {number}: {translated}")
        translated_chapters.append(translated)

    translated_appendices: list[Path] = []
    for code, english in zip(range(ord("A"), ord("Z") + 1), selected_english_appendices):
        translated = appendices_dir / english.name
        if not translated.exists() or not translated.read_text(encoding="utf-8").strip():
            raise ValueError(f"Missing translated Appendix {chr(code)}: {translated}")
        translated_appendices.append(translated)

    front = f'''---
title: "{meta['title']}"
subtitle: "{meta['subtitle']}"
author: "Al Leiva, con apoyo de redacción y revisión asistida por IA"
date: "30 de julio de 2026"
lang: {meta['lang']}
toc: true
toc-depth: 3
numbersections: true
---

# {meta['title']}

> **Estado de publicación:** {meta['status']}. La edición conserva la estructura y las referencias jurídicas de la fuente inglesa controlada.

## Aviso jurídico y educativo

{meta['disclaimer']}

## Cómo utilizar este manual

{meta['how']}

## Base jurídica controlada

- Reglamento (UE) 2024/1689, con sus modificaciones.
- Reglamento (UE) 2026/1744.
- Texto consolidado vigente de EUR-Lex.
- Material oficial de la Comisión Europea y de la Oficina de IA de la UE, identificado como orientación no vinculante salvo que se incorpore mediante un instrumento vinculante.

'''
    if lang == "pt-BR":
        front = front.replace("con apoyo de redacción y revisión asistida por IA", "com apoio de redação e revisão assistida por IA")
        front = front.replace("30 de julio de 2026", "30 de julho de 2026")
        front = front.replace("Estado de publicación", "Status de publicação")
        front = front.replace("La edición conserva la estructura y las referencias jurídicas de la fuente inglesa controlada.", "A edição preserva a estrutura e as referências jurídicas da fonte inglesa controlada.")
        front = front.replace("Aviso jurídico y educativo", "Aviso jurídico e educacional")
        front = front.replace("Cómo utilizar este manual", "Como utilizar este manual")
        front = front.replace("Base jurídica controlada", "Base jurídica controlada")
        front = front.replace("Reglamento (UE)", "Regulamento (UE)")
        front = front.replace("con sus modificaciones", "conforme alterado")
        front = front.replace("Texto consolidado vigente de EUR-Lex", "Texto consolidado vigente do EUR-Lex")
        front = front.replace("Material oficial de la Comisión Europea y de la Oficina de IA de la UE, identificado como orientación no vinculante salvo que se incorpore mediante un instrumento vinculante.", "Material oficial da Comissão Europeia e do Gabinete Europeu de IA, identificado como orientação não vinculante, salvo quando incorporado por instrumento vinculante.")

    parts = [front]
    records: list[Record] = []
    for number, path in enumerate(translated_chapters, start=1):
        text = path.read_text(encoding="utf-8")
        records.append(Record(f"Chapter {number}", str(path.relative_to(repo_root)), digest(text), len(text.encode("utf-8")), len(text.splitlines())))
        parts.append("\n\\newpage\n\n" + demote_heading(text))

    parts.append(f"\n\\newpage\n\n# {meta['appendices']}\n")
    for code, path in zip(range(ord("A"), ord("Z") + 1), translated_appendices):
        text = path.read_text(encoding="utf-8")
        records.append(Record(f"Appendix {chr(code)}", str(path.relative_to(repo_root)), digest(text), len(text.encode("utf-8")), len(text.splitlines())))
        parts.append("\n\\newpage\n\n" + demote_heading(text))

    master = "\n".join(parts).rstrip() + "\n"
    stem = f"EU_AI_Act_GRC_Compliance_Manual_{lang}_Controlled_Master"
    master_path = out_dir / f"{stem}.md"
    master_path.write_text(master, encoding="utf-8")
    manifest = {
        "language": lang,
        "chapter_count": 138,
        "appendix_count": 26,
        "record_count": len(records),
        "master_sha256": digest(master),
        "records": [asdict(record) for record in records],
    }
    (out_dir / f"CANONICAL_BUILD_MANIFEST_{lang}.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {master_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"BUILD ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
