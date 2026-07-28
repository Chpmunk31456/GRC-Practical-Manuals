#!/usr/bin/env python3
"""Apply deterministic editorial corrections identified during Issue #4 QA."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMON = {
    "Plain meaning": {"Espanol": "Significado claro", "Portugues_BR": "Significado claro"},
    "Manager or analyst verification": {
        "Espanol": "Verificación del gerente o analista",
        "Portugues_BR": "Verificação do gerente ou analista",
    },
    "Manager or analista verification": {
        "Espanol": "Verificación del gerente o analista",
        "Portugues_BR": "Verificação do gerente ou analista",
    },
    "Example evidence": {"Espanol": "Evidencia de ejemplo", "Portugues_BR": "Evidência de exemplo"},
    "Verification focus": {"Espanol": "Enfoque de verificación", "Portugues_BR": "Foco da verificação"},
    "Quick start": {"Espanol": "Inicio rápido", "Portugues_BR": "Início rápido"},
    "Evidence and limitation": {
        "Espanol": "Evidencia y limitación",
        "Portugues_BR": "Evidência e limitação",
    },
    "Table of Contents": {"Espanol": "Tabla de contenido", "Portugues_BR": "Sumário"},
    "Clause": {"Espanol": "Cláusula", "Portugues_BR": "Cláusula"},
    "Group": {"Espanol": "Grupo", "Portugues_BR": "Grupo"},
    "Role": {"Espanol": "Rol", "Portugues_BR": "Função"},
    "Deployment": {"Espanol": "Implementación", "Portugues_BR": "Implantação"},
}

KNOWN = {
    "Significado liso": "Significado claro",
    "Gerente ou verificação do analista": "Verificação do gerente ou analista",
    "Conteúdo verdadeiro da palavra": "Conteúdo",
    "COMPLIANÇA": "CONFORMIDADE",
    "Función del PROTECTO": "Función PROTECT",
}


def clean(path: Path) -> bool:
    language = "Espanol" if "Espanol" in path.parts else "Portugues_BR"
    original = path.read_text(encoding="utf-8")
    text = original
    for source, localized in COMMON.items():
        text = text.replace(source, localized[language])
    for source, replacement in KNOWN.items():
        text = text.replace(source, replacement)

    # Argos translated Markdown table pipes into literal extraction artifacts.
    text = re.sub(r"\bSilencio\b", "|", text)
    text = re.sub(r"\bTENIDO\b", "|", text)
    text = re.sub(r"\bTEN\b(?=\s*$)", "|", text, flags=re.MULTILINE)
    text = re.sub(r"^La vida(-{3,})$", r"|\1|", text, flags=re.MULTILINE)
    text = re.sub(r"[ \t]+\|[ \t]*$", " |", text, flags=re.MULTILINE)
    text = re.sub(r"\|[ \t]*\|", "| |", text)
    text = "\n".join(
        f"{line} |" if line.startswith("|") and line.count("|") < 2 else line
        for line in text.splitlines()
    ) + ("\n" if text.endswith("\n") else "")

    if text == original:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    targets = sorted(
        path
        for path in ROOT.rglob("*.md")
        if any(part in {"Espanol", "Portugues_BR"} for part in path.parts)
        and "qa" not in path.parts
    )
    changed = [path.relative_to(ROOT) for path in targets if clean(path)]
    print(f"Corrected {len(changed)} localized Markdown files.")
    for path in changed:
        print(path)


if __name__ == "__main__":
    main()
