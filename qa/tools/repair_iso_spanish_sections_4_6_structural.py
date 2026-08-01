#!/usr/bin/env python3
from pathlib import Path

PATH = Path("02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md")

SOA_START = "| **Control** ** Aplicable** |"
SEC5 = "# 5. Documentación y evidencia"
DOC_START = "| **Documento o registro** | **Purpose** | ** Controles de control**"
SEC6_OLD = "# Cláusula 4 - Contexto de la organización"
SEC6_NEW = "# 6. Cláusula 4 - Contexto de la organización"

SOA_TABLE = """| **Control** | **¿Aplicable?** | **Justificación** | **Estado** | **Responsable / evidencia** |
|---|---|---|---|---|
| Ejemplo 8.15: registro de eventos | Sí | Necesario para la detección, la investigación y el cumplimiento de obligaciones | Implementado con acciones abiertas | Operaciones de Seguridad / inventario de fuentes y registros de revisión |
| Ejemplo 7.9: activos fuera de las instalaciones | Sí | El personal remoto y en viaje utiliza dispositivos de la organización | Implementado | Operaciones de TI / inventario y evidencia de cifrado |
| Ejemplo de control específico de la organización | Sí | Un riesgo específico de seguridad del producto exige versiones firmadas | Parcialmente implementado | Ingeniería / registros de la canalización |
| Ejemplo de exclusión | No | La tecnología o el escenario descritos no existen dentro del alcance controlado | No aplicable | Evidencia del alcance y de la arquitectura |

"""

DOC_TABLE = """| **Documento o registro** | **Propósito** | **Comprobaciones de control** |
|---|---|---|
| Alcance del SGSI | Define los límites y las interfaces | Aprobado, vigente y coherente con la realidad |
| Política | Establece la dirección y los compromisos | Aprobada, comunicada y revisada |
| Método y registro de riesgos | Demuestra una evaluación y unas decisiones repetibles | Criterios aplicados de forma coherente; los propietarios aprueban el riesgo residual |
| Plan de tratamiento de riesgos | Registra acciones, responsables, recursos y fechas | Alineado con los riesgos y la Declaración de Aplicabilidad |
| Declaración de Aplicabilidad | Explica la selección y el estado de los controles | Todos los controles del Anexo A están abordados y las justificaciones están sustentadas |
| Objetivos y métricas | Muestra los resultados previstos y su evaluación | Medibles, con responsables, analizados y sujetos a acciones |
| Registros de competencia y concientización | Sustentan la capacidad y la comprensión | Basados en funciones, evaluados y vigentes |
| Evidencia operativa | Demuestra que los controles funcionaron realmente | Completa, auténtica, protegida y conservada |
| Registros de auditoría y revisión | Sustentan la supervisión y las decisiones | Objetivos, completos y con seguimiento |
| Registros de acciones correctivas | Demuestran la causa raíz y una corrección eficaz | Causa abordada, recurrencia considerada y eficacia verificada |

"""


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    for marker in (SOA_START, SEC5, DOC_START, SEC6_OLD):
        if text.count(marker) != 1:
            raise SystemExit(f"Expected exactly one marker: {marker!r}; found {text.count(marker)}")

    soa_start = text.index(SOA_START)
    sec5_start = text.index(SEC5, soa_start)
    text = text[:soa_start] + SOA_TABLE + text[sec5_start:]

    doc_start = text.index(DOC_START)
    sec6_start = text.index(SEC6_OLD, doc_start)
    text = text[:doc_start] + DOC_TABLE + text[sec6_start:]
    text = text.replace(SEC6_OLD, SEC6_NEW, 1)

    if SOA_START in text or DOC_START in text or SEC6_OLD in text:
        raise SystemExit("Legacy malformed structural markers remain")
    if text.count(SEC6_NEW) != 1:
        raise SystemExit("Section 6 heading was not restored exactly once")

    PATH.write_text(text, encoding="utf-8")
    print("Repaired ISO Spanish sections 4-6 structural blocks")


if __name__ == "__main__":
    main()
