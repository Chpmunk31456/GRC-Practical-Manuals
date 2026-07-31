# 11. Control 6 — Gestión del control de acceso

*Las 8 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

<img src="media/image6.png" style="width:6.15in;height:3.03192in" alt="Las cuentas y los privilegios requieren creación aprobada, autenticación sólida, revisión y revocación oportuna." />

Figura 6. Ciclo de vida de identidad y acceso

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la gestión del control de acceso. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 6.1 | Establecer un proceso de concesión de acceso | Definir un proceso aprobado, trazable y basado en necesidad para otorgar acceso. | Confirmar solicitud, aprobación, implementación, plazo y excepciones. | Solicitudes, aprobaciones, tickets, registros y revisiones. |
| 6.2 | Establecer un proceso de revocación de acceso | Retirar acceso oportunamente cuando cambien las funciones o termine la relación. | Verificar disparadores, tiempos, cobertura y seguimiento. | Tickets de baja, registros de directorio, listas de terminación y pruebas. |
| 6.3 | Exigir MFA para aplicaciones expuestas externamente | Proteger aplicaciones accesibles desde Internet mediante autenticación multifactor. | Confirmar cobertura, métodos, excepciones y pruebas. | Configuración de identidad, reportes de cobertura y excepciones. |
| 6.4 | Exigir MFA para acceso remoto a la red | Aplicar MFA a conexiones remotas hacia recursos empresariales. | Revisar VPN, ZTNA, cobertura, excepciones y registros. | Configuración, registros de autenticación y reportes. |
| 6.5 | Exigir MFA para acceso administrativo | Aplicar MFA a toda actividad con privilegios administrativos. | Confirmar población, sistemas, métodos y excepciones. | Inventario de administradores, políticas y registros. |
| 6.6 | Establecer y mantener un inventario de sistemas de autenticación y autorización | Mantener una lista completa de sistemas que gestionan identidades, autenticación y autorización. | Verificar propietario, alcance, actualidad y conciliación. | Inventario, diagramas, responsables y revisiones. |
| 6.7 | Centralizar el control de acceso | Gestionar identidades y autorizaciones mediante plataformas centralizadas cuando sea viable. | Confirmar integración, cobertura y cuentas locales excepcionales. | Directorios, IAM, SSO, integraciones y excepciones. |
| 6.8 | Definir y mantener control de acceso basado en roles | Asignar permisos mediante roles aprobados y revisados periódicamente. | Revisar diseño, propietarios, asignaciones, recertificación y separación de funciones. | Catálogo de roles, matrices, aprobaciones y revisiones. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 12. Control 7 — Gestión continua de vulnerabilidades

*Las 7 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

<img src="media/image7.png" style="width:6.15in;height:3.14547in" alt="La cobertura completa y la remediación verificada importan más que la producción de informes de escaneo." />

Figura 7. Gestión continua de vulnerabilidades

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la gestión continua de vulnerabilidades. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 7.1 | Establecer y mantener un proceso de gestión de vulnerabilidades | Definir alcance, responsabilidades, frecuencia, priorización y seguimiento de vulnerabilidades. | Confirmar aprobación, cobertura, métricas, excepciones y revisión. | Política, procedimientos, responsables, métricas y registros. |
| 7.2 | Establecer y mantener un proceso de remediación | Corregir vulnerabilidades según riesgo y verificar el cierre. | Revisar plazos, prioridades, excepciones, nuevas pruebas y escalamiento. | Tickets, planes, excepciones, resultados de nuevas pruebas y métricas. |
| 7.3 | Realizar gestión automatizada de parches del sistema operativo | Identificar, probar y desplegar parches del sistema operativo mediante un proceso administrado. | Confirmar cobertura, frecuencia, fallos, excepciones y cumplimiento. | Consolas, inventarios, reportes de despliegue y tickets. |
| 7.4 | Realizar gestión automatizada de parches de aplicaciones | Identificar, probar y desplegar actualizaciones de aplicaciones. | Verificar cobertura, versiones, fallos y excepciones. | Inventarios, consolas, resultados y planes correctivos. |
| 7.5 | Realizar escaneos automatizados de vulnerabilidades de activos empresariales internos | Escanear activos internos con cobertura y credenciales adecuadas. | Confirmar alcance, autenticación, frecuencia, exclusiones y resultados. | Configuración de escáner, resultados, cobertura y excepciones. |
| 7.6 | Realizar escaneos automatizados de vulnerabilidades de activos empresariales expuestos externamente | Evaluar de forma periódica los activos accesibles desde Internet. | Verificar inventario, alcance, frecuencia, hallazgos y seguimiento. | Inventario externo, resultados, tickets y nuevas pruebas. |
| 7.7 | Corregir las vulnerabilidades detectadas | Priorizar, corregir y volver a probar vulnerabilidades identificadas. | Confirmar riesgo, plazo, propietario, evidencia de cierre y excepciones. | Tickets, cambios, resultados de nueva prueba y aprobaciones. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.
