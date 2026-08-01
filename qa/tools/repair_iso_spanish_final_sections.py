#!/usr/bin/env python3
from pathlib import Path
import re

p = Path('02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md')
text = p.read_text(encoding='utf-8')
original = text

replacements = {
    '**CYBERSECURITY, PRIVACY &amp; COMPLIANCE SERIES**': '**SERIE DE CIBERSEGURIDAD, PRIVACIDAD Y CUMPLIMIENTO**',
    '| **Inside:** Cláusulas 4–10 • todos los 93 controles del Anexo A • riesgo • Declaración de aplicabilidad • auditoría • certificación • evidencia • herramientas • laboratorios • preparación de la carrera |': '| **Contenido:** Cláusulas 4–10 • los 93 controles del Anexo A • riesgo • Declaración de Aplicabilidad • auditoría • certificación • evidencia • herramientas • laboratorios • preparación profesional |',
    'Contenido de la palabra:** Este documento contiene un campo de mesa de contenido de Word nativo y una guía de capítulo verificada. Después de editar, haga clic con el botón derecho en el contenido y elija el campo de actualización, luego actualice la tabla completa.': '**Tabla de contenido en Word:** Este documento contiene un campo nativo de tabla de contenido y una estructura de capítulos verificada. Después de editarlo, haga clic con el botón derecho en la tabla de contenido, seleccione **Actualizar campo** y luego **Actualizar toda la tabla**.',
    '[1. ISO/IEC 27001 y 27002 Foundations [7]](#isoiec-27001-and-27002-foundations)': '[1. Fundamentos de ISO/IEC 27001 y 27002 [7]](#isoiec-27001-and-27002-foundations)',
    '[2. ISMS Scope and Interested Parties [8]](#isms-scope-and-interested-parties)': '[2. Alcance del SGSI y partes interesadas [8]](#isms-scope-and-interested-parties)',
    '# 1. ISO/IEC 27001 y 27002 Foundations': '# 1. Fundamentos de ISO/IEC 27001 y 27002',
    '**Distinción importante:** ISO/IEC 27002 proporciona orientación. La organización sigue siendo responsable de seleccionar y diseñar controles que traten sus riesgos y cumplan los requisitos aplicables. |': '| **Distinción importante:** ISO/IEC 27002 proporciona orientación. La organización sigue siendo responsable de seleccionar y diseñar controles que traten sus riesgos y cumplan los requisitos aplicables. |\n|---|',
}
for old, new in replacements.items():
    if text.count(old) != 1:
        raise SystemExit(f'Expected exactly one occurrence: {old[:80]!r}; found {text.count(old)}')
    text = text.replace(old, new)

section25 = '''# 25. Laboratorio ficticio y portafolio

*Un entorno seguro de práctica con datos sintéticos y sistemas de laboratorio autorizados.*

| **Regla del laboratorio:** Utilice una organización ficticia, datos sintéticos, sistemas aislados y herramientas que esté autorizado a operar. No afirme que un proyecto de portafolio sea una certificación real ni una auditoría de cliente. |
|---|

1. Cree una empresa ficticia con dos productos, un servicio en la nube, una fuerza laboral remota y tres proveedores.

2. Redacte un análisis de contexto de una página, un registro de partes interesadas, una determinación de pertinencia climática y una declaración de alcance.

3. Cree criterios de riesgo y un registro de diez escenarios con propietarios y decisiones de tratamiento.

4. Cree un plan de tratamiento y una Declaración de Aplicabilidad que aborde los 93 controles del Anexo A con justificaciones concisas y un estado de implementación honesto.

5. Elabore políticas, procedimientos, objetivos, métricas, registros de activos y proveedores, un registro de capacitación, un registro de incidentes y un ejercicio de continuidad.

6. Utilice algunas herramientas de código abierto en laboratorios aislados y conserve evidencia del alcance, la configuración, los resultados, la validación, la remediación y la repetición de pruebas.

7. Diseñe y ejecute un plan de auditoría interna sobre cláusulas y controles seleccionados.

8. Redacte dos no conformidades, registros de causa raíz, acciones correctivas y pruebas de eficacia.

9. Prepare actas de revisión por la dirección que muestren entradas, decisiones, propietarios, recursos y plazos.

10. Publique únicamente artefactos depurados y sintéticos con una declaración clara de limitaciones.

| **Artefacto del portafolio** | **Qué demuestra** |
|---|---|
| Contexto, partes interesadas y alcance | Razonamiento y límites de la cláusula 4 |
| Método, registro y tratamiento de riesgos | Cláusula 6 y propiedad del riesgo |
| Declaración de Aplicabilidad | Decisiones de control trazables |
| Papel de trabajo de prueba de controles | Evidencia, muestreo, excepciones y conclusión |
| Paquete de auditoría interna | Programa, plan, criterios, informe y seguimiento |
| Actas de revisión por la dirección | Evaluación y decisiones de liderazgo |
| Registro de acción correctiva | Causa raíz y eficacia |
| Memorando de evidencia de herramientas | Conocimientos técnicos y limitaciones |

'''
text, n = re.subn(r'# 25\. Laboratorio Ficcional y Portfolio\n.*?(?=# 26\. Plan de aprendizaje de 30 días)', section25, text, flags=re.S)
if n != 1:
    raise SystemExit(f'Expected one section 25 replacement; found {n}')

section28_open = '''# 28. Plantillas, glosario, índice y referencias

*Estructuras de trabajo reutilizables, términos importantes y puntos de partida autorizados.*

## 28.1 Registro mínimo de riesgos

| **Campo** | **Entrada** |
|---|---|
| ID del riesgo y propietario | ________________________________ |
| Objetivo o activo | ________________________________ |
| Evento de amenaza y condición | ________________________________ |
| Consecuencia | ________________________________ |
| Controles existentes | ________________________________ |
| Probabilidad e impacto | ________________________________ |
| Riesgo actual | ________________________________ |
| Tratamiento y propietario de la acción | ________________________________ |
| Riesgo residual y aceptación | ________________________________ |
| Fecha de revisión | ________________________________ |

## 28.2 Papel de trabajo de prueba de controles

| **Campo** | **Entrada** |
|---|---|
| Criterios y control | ________________________________ |
| Alcance y período | ________________________________ |
| Propietario y sistemas | ________________________________ |
| Población y comprobación de integridad | ________________________________ |
| Muestra y justificación | ________________________________ |
| Procedimiento realizado | ________________________________ |
| Evidencia examinada | ________________________________ |
| Excepciones | ________________________________ |
| Conclusión y limitación | ________________________________ |
| Corrección y repetición de la prueba | ________________________________ |

## 28.3 Glosario

| **Término** | **Significado** |
|---|---|
| Anexo A | Conjunto de referencia de 93 controles de seguridad de la información en ISO/IEC 27001:2022. |
| CIA | Confidencialidad, integridad y disponibilidad. |
| Conformidad | Cumplimiento de un requisito. |
| Control | Medida que modifica o mantiene el riesgo. |
| Acción correctiva | Acción que aborda la causa de una no conformidad para evitar su recurrencia. |
| Información documentada | Información que la organización debe controlar y mantener o conservar. |
| Parte interesada | Persona u organización que puede afectar, verse afectada o percibirse afectada por una decisión o actividad. |
| SGSI | Sistema de gestión de la seguridad de la información. |
| No conformidad | Incumplimiento de un requisito. |
| Riesgo residual | Riesgo que permanece después del tratamiento. |
| Propietario del riesgo | Persona o entidad responsable y autorizada para gestionar un riesgo. |
| SoA | Declaración de Aplicabilidad. |
| Alta dirección | Persona o grupo que dirige y controla la organización al más alto nivel dentro del alcance. |

'''
text, n = re.subn(r'# 28\. Plantillas, Glosario, Índice y Referencias\n.*?(?=## 28\.4 Índice de asunto)', section28_open, text, flags=re.S)
if n != 1:
    raise SystemExit(f'Expected one section 28 opening replacement; found {n}')

index = '''## 28.4 Índice temático

| **Tema** | **Secciones** |
|---|---|
| Controles del Anexo A | 13–16 |
| Auditoría | 19 |
| Certificación | 21 |
| Cambio climático | 2, 6, 20 |
| Acción correctiva | 12, 20 |
| Evidencia | 5, 18 |
| Partes interesadas | 2, 6 |
| Analista junior | 24–27 |
| Revisión por la dirección | 20 |
| Métricas | 11, 18 |
| Herramientas de código abierto | 22 |
| Evaluación y tratamiento de riesgos | 3, 8 |
| Alcance | 2, 6 |
| Declaración de Aplicabilidad | 4 |
| Proveedores | 13, 18, 23 |

'''
text, n = re.subn(r'## 28\.4 Índice de asunto\n.*?(?=## 28\.5 Referencias oficiales)', index, text, flags=re.S)
if n != 1:
    raise SystemExit(f'Expected one section 28.4 replacement; found {n}')

for forbidden in ('Conformity | Fulfillment of a requirement.', 'Silenciosas partes interesadas', 'TENIDA Metrics', 'Contenido de la palabra'):
    if forbidden in text:
        raise SystemExit(f'Forbidden corruption remains: {forbidden}')

if text == original:
    raise SystemExit('No changes applied')
p.write_text(text, encoding='utf-8')
print('Repaired final ISO Spanish sections 1, 17, 25, and 28')
