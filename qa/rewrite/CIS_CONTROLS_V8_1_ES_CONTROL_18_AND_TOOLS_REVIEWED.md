# CIS Controls v8.1 — Reescritura revisada en español

## Alcance controlado

Este archivo contiene el reemplazo revisado para las secciones 23 y 24 de la edición en español latinoamericano del manual CIS Controls v8.1.

Fuente autoritativa utilizada:

`01-foundations/CIS_Controls_v8.1/English_Source_CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md`

Destino previsto:

`01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md`

Este bloque no debe integrarse parcialmente. Después de la integración, deben regenerarse y validarse el DOCX y el PDF.

---

# 23. Control 18 — Pruebas de penetración

*Las cinco Salvaguardas, su significado en lenguaje claro, el enfoque de verificación y ejemplos de evidencia.*

| **Objetivo del control:** Fortalecer la organización mediante la implementación y medición de Salvaguardas para las pruebas de penetración. |
|---|

| **ID** | **Salvaguarda** | **Significado en lenguaje claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 18.1 | Establecer y mantener un programa de pruebas de penetración | Implementar un proceso repetible, con un responsable definido, para establecer y mantener un programa de pruebas de penetración; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |
| 18.2 | Realizar pruebas periódicas de penetración externa | Implementar un proceso repetible, con un responsable definido, para realizar pruebas periódicas de penetración externa; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |
| 18.3 | Corregir los hallazgos de las pruebas de penetración | Implementar un proceso repetible, con un responsable definido, para corregir los hallazgos de las pruebas de penetración; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |
| 18.4 | Validar las medidas de seguridad | Implementar un proceso repetible, con un responsable definido, para validar las medidas de seguridad; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |
| 18.5 | Realizar pruebas periódicas de penetración interna | Implementar un proceso repetible, con un responsable definido, para realizar pruebas periódicas de penetración interna; después, verificar su cobertura y sus excepciones. | Confirmar alcance, población, responsabilidad, implementación, frecuencia, cobertura, excepciones, corrección y repetición de pruebas. | reglas de compromiso aprobadas, alcance, evaluadores cualificados, informes, remediación, repetición de pruebas y evidencia de validación |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación para la Evaluación de Controles para consultar el lenguaje exacto de cada Salvaguarda, la clase de activo, la función de seguridad, el Grupo de Implementación, las dependencias, las entradas, las operaciones, las medidas, las métricas y la revisión de procedimientos.

# 24. Herramientas de código abierto

*Enlaces oficiales, inicios rápidos seguros, evidencia y limitaciones.*

| **Herramienta** | **Propósito** | **Controles posibles** |
|---|---|---|
| CIS Controls Navigator | Seleccionar Grupos de Implementación y explorar correspondencias oficiales | Todos |
| CIS Controls Assessment Specification | Orientación oficial para la medición | Todos |
| CIS-CAT Lite | Evaluación de determinados CIS Benchmarks | 4 |
| CISO Assistant | Controles, riesgos, evidencia y hallazgos | Todos |
| Wazuh | Monitoreo de endpoints, SIEM, FIM y alertas | 1, 4, 8, 10, 13, 17 |
| osquery | Consultas sobre activos, software, cuentas y configuración | 1, 2, 4, 5, 8 |
| OpenSCAP | Evaluación de configuración segura en Linux | 4, 7 |
| Lynis | Auditoría de seguridad en Linux | 4, 7 |
| Nmap | Descubrimiento autorizado de activos y servicios | 1, 12 |
| Greenbone Community Edition | Evaluación de vulnerabilidades | 7 |
| Trivy | Repositorios, imágenes, dependencias, secretos e infraestructura como código | 2, 4, 7, 16 |
| OWASP ZAP | Pruebas autorizadas de seguridad web | 16, 18 |
| Suricata | Detección de intrusiones en red y visibilidad del tráfico | 8, 13, 17 |
| Keycloak | Identidades, roles, MFA, sesiones y eventos | 5, 6, 8 |
| DefectDojo | Ingesta de hallazgos, deduplicación, remediación y repetición de pruebas | 7, 16, 18 |
| Velociraptor | Visibilidad de endpoints y respuesta a incidentes | 1, 8, 13, 17 |

| **Limitación crítica:** Una herramienta puede respaldar una o más Salvaguardas, pero no puede seleccionar por sí sola el Grupo de Implementación de una organización, definir su tolerancia al riesgo, garantizar una cobertura completa, sustituir los procedimientos y la revisión humana, autorizar pruebas de penetración ni demostrar por sí sola el cumplimiento de otro marco. |
|---|

## Criterios de aceptación para la integración

- No quedan tokens `TEN`, `TEN TODO`, `tención`, `Silencioso` ni `tóxico` en las secciones reemplazadas.
- Las cinco Salvaguardas del Control 18 aparecen en filas completas y separadas.
- La tabla de herramientas contiene tres columnas válidas y 16 herramientas.
- No quedan fragmentos descriptivos en inglés, salvo nombres oficiales de productos o proyectos.
- El Markdown se representa sin tablas rotas.
- El DOCX se abre sin reparación y conserva la estructura de las tablas.
- El PDF es buscable y no presenta texto cortado, superpuesto ni fuera de página.
- Los enlaces oficiales y la terminología CIS se verifican antes de la aprobación final.
