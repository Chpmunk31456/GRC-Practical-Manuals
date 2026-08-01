#!/usr/bin/env python3
"""Repair high-confidence residual-English defects in ISO Spanish sections 1 and 4.

This batch intentionally avoids the malformed section-4 table and all later
structural repairs. Every replacement is exact and fail-closed.
"""
from pathlib import Path

PATH = Path("02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md")

REPLACEMENTS = [
    ("# 2. ISMS Scope and Interested Parties", "# 2. Alcance del SGSI y partes interesadas", "section 2 heading"),
    ("<!-- REVISIÓN HUMANA: falta el recurso localizado media/image3.png; texto alternativo conservado: The SoA records reasoned control selection and implementation status. -->", "<!-- REVISIÓN HUMANA: falta el recurso localizado media/image3.png; texto alternativo conservado: La Declaración de Aplicabilidad registra la selección fundamentada de controles y su estado de implementación. -->", "figure 3 alternative text"),
    ("- List the controls necessary to treat identified information-security risks and meet legal, regulatory, contractual, and business requirements.", "- Enumerar los controles necesarios para tratar los riesgos identificados de seguridad de la información y cumplir los requisitos legales, regulatorios, contractuales y empresariales.", "section 4 control-selection sentence"),
    ("- No se pasan por alto los controles seleccionados del anexo A.", "- Comparar los controles seleccionados con el Anexo A para comprobar que no se hayan omitido controles de referencia necesarios.", "section 4 Annex A comparison sentence"),
    ("- Recordar si cada control del Anexo A es aplicable y justificar la inclusión o exclusión.", "- Registrar si cada control del Anexo A es aplicable y justificar su inclusión o exclusión.", "section 4 applicability sentence"),
    ("- Recordar claramente el estado de aplicación y mantenerlo en consonancia con el plan de tratamiento de riesgos y las pruebas de funcionamiento.", "- Registrar claramente el estado de implementación y mantenerlo alineado con el plan de tratamiento de riesgos y la evidencia operativa.", "section 4 implementation-status sentence"),
    ("- Controlar el SoA como información documentada y actualizarla después de cambios de riesgo, alcance, legal, proveedor, tecnología o control.", "- Controlar la Declaración de Aplicabilidad como información documentada y actualizarla después de cambios materiales en el riesgo, el alcance, los requisitos legales, los proveedores, la tecnología o los controles.", "section 4 documented-information sentence"),
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    before = PATH.read_text(encoding="utf-8")
    after = before
    for old, new, label in REPLACEMENTS:
        after = replace_once(after, old, new, label)
    if after == before:
        raise SystemExit("No changes produced")
    PATH.write_text(after, encoding="utf-8")
    print(f"Applied {len(REPLACEMENTS)} ISO Spanish parity batch A replacements")


if __name__ == "__main__":
    main()
