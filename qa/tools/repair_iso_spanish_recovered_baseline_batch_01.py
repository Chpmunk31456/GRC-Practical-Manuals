#!/usr/bin/env python3
"""Clean high-confidence structural defects in the recovered ISO Spanish baseline."""
from pathlib import Path
import re

PATH = Path("02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def normalize_toc(text: str) -> tuple[str, int]:
    start = text.find("# Tabla de contenidos")
    body = text.find("\n# 1. ", start)
    if start < 0 or body < 0:
        raise SystemExit("Could not identify Spanish TOC boundary")
    prefix, toc, suffix = text[:start], text[start:body], text[body:]
    patterns = [
        re.compile(r"^\[(?P<label>.+?)\s+\[(?P<page>\d+)\]\s*\(\s*#(?P<inner>[^)]+)\s*\)\]\s*\(\s*#(?P<outer>[^)]+)\s*\)\s*$"),
        re.compile(r"^\[(?P<label>.+?)\s+\[(?P<page>\d+)\]\]\s*\(\s*#(?P<outer>[^)]+)\s*\)\s*$"),
    ]
    output = []
    changes = 0
    for line in toc.splitlines():
        m = patterns[0].match(line)
        if m:
            if m.group("inner").strip() != m.group("outer").strip():
                raise SystemExit(f"Mismatched TOC anchors: {line}")
            line = f"[{m.group('label')} [{m.group('page')}]](#{m.group('outer').strip()})"
            changes += 1
        output.append(line)
    if changes < 50:
        raise SystemExit(f"Expected at least 50 nested TOC links; normalized {changes}")
    return prefix + "\n".join(output) + suffix, changes


def main() -> None:
    before = PATH.read_text(encoding="utf-8")
    text, toc_changes = normalize_toc(before)

    exact = [
        ("Contenido de la palabra:** Este documento contiene un campo de mesa de contenido de Word nativo y una guía de capítulo verificada. Después de editar, haga clic con el botón derecho en el contenido y elija el campo de actualización, luego actualice toda la tabla.",
         "| **Tabla de contenido de Word:** Este documento contiene un campo nativo de tabla de contenido de Word y una guía de capítulos verificada. Después de editar, haga clic con el botón derecho en la tabla de contenido, seleccione **Actualizar campo** y luego **Actualizar toda la tabla**. |",
         "Word TOC instruction"),
        ("- En el anexo A se enumeran 93 controles de referencia en cuatro temas: 37 orgánicos, 8 personas, 14 físicos y 34 tecnológicos.",
         "- En el Anexo A se enumeran 93 controles de referencia en cuatro temas: 37 organizativos, 8 relacionados con personas, 14 físicos y 34 tecnológicos.",
         "Annex A counts"),
        ("- Considerar si el cambio climático es relevante para la eficacia del SIV y si las partes interesadas tienen requisitos relacionados con el clima; documentar el razonamiento.",
         "- Considerar si el cambio climático es relevante para la eficacia del SGSI y si las partes interesadas tienen requisitos relacionados con el clima; documentar el razonamiento.",
         "SGSI climate line"),
        ("Figure 3. Statement of Applicability workflow", "Figura 3. Flujo de trabajo de la Declaración de Aplicabilidad", "Figure 3 caption"),
        ("Figure 4. Requirement-to-evidence chain", "Figura 4. Cadena de requisitos a evidencia", "Figure 4 caption"),
        ("Figure 7. Security-incident management", "Figura 7. Gestión de incidentes de seguridad", "Figure 7 caption"),
        ("Lectura de certificación", "Preparación para la certificación", "certification readiness"),
        ("Laboratorio de Ficción y Cartera", "Laboratorio ficticio y portafolio", "fictional lab"),
        ("Valor de los empleadores de habilidades", "Habilidades que valoran los empleadores", "skills employers value"),
        ("Uso electrónico y autorizado", "Uso ético y autorizado", "ethical use"),
    ]
    for old, new, label in exact:
        if old in text:
            text = text.replace(old, new)

    # Restore the one missing major section heading without touching TOC links.
    text = re.sub(r"(?m)^6\. Cláusula 4 — Contexto de la organización$", "# 6. Cláusula 4 — Contexto de la organización", text, count=1)

    # Remove known conversion artifacts only as standalone tokens or placeholder rows.
    text = re.sub(r"(?m)^\|\. \|\s*$\n?", "", text)
    text = re.sub(r"\bSilencioso\b", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\bTENCIÓN\b|\bTENENCIA\b|\bTEN\b|\btención\b", "", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r" +\n", "\n", text)

    if text == before:
        raise SystemExit("No Spanish cleanup changes produced")
    PATH.write_text(text, encoding="utf-8")
    print(f"Spanish recovered-baseline cleanup complete; normalized {toc_changes} TOC links")


if __name__ == "__main__":
    main()
