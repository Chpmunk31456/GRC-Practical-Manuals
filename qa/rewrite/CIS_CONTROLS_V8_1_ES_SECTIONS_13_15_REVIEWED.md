# 13. Control 8 — Gestión de registros de auditoría

*Las 12 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la gestión de registros de auditoría. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 8.1 | Establecer y mantener un proceso de gestión de registros de auditoría | Definir alcance, responsables, fuentes, almacenamiento, revisión y conservación de registros. | Confirmar aprobación, cobertura, frecuencia, excepciones y mejora. | Política, procedimientos, responsables, inventario de fuentes y métricas. |
| 8.2 | Recopilar registros de auditoría | Recopilar los registros necesarios de activos, aplicaciones, servicios e infraestructura. | Verificar fuentes, cobertura, integridad, frecuencia y fallos de ingestión. | Configuración, inventario de fuentes, registros recibidos y alertas de fallos. |
| 8.3 | Garantizar almacenamiento adecuado de registros de auditoría | Dimensionar y proteger el almacenamiento para cumplir los períodos de conservación. | Revisar capacidad, crecimiento, disponibilidad, protección y alertas. | Métricas de capacidad, configuración, alertas y planes de ampliación. |
| 8.4 | Estandarizar la sincronización horaria | Utilizar fuentes horarias autorizadas y consistentes en los sistemas. | Confirmar servidores, configuración, cobertura, desviaciones y excepciones. | Configuración NTP, inventario, alertas y resultados de consulta. |
| 8.5 | Recopilar registros de auditoría detallados | Registrar eventos con suficiente detalle para investigación y trazabilidad. | Verificar campos, identidades, marcas de tiempo, acciones y resultados. | Muestras de registros, esquema, configuración y resultados de prueba. |
| 8.6 | Recopilar registros de consultas DNS | Registrar consultas DNS relevantes para detección e investigación. | Confirmar fuentes, cobertura, detalle, conservación y revisión. | Registros DNS, configuración, SIEM y alertas. |
| 8.7 | Recopilar registros de solicitudes URL | Registrar solicitudes web relevantes conforme al riesgo y la privacidad. | Verificar cobertura, detalle, conservación, acceso y uso analítico. | Registros proxy/SWG, configuración, SIEM y casos de uso. |
| 8.8 | Recopilar registros de línea de comandos | Registrar la ejecución de comandos donde el riesgo lo justifique. | Confirmar sistemas cubiertos, detalle, protección y revisión. | Registros EDR, auditoría del sistema, SIEM y alertas. |
| 8.9 | Centralizar los registros de auditoría | Consolidar registros en una plataforma administrada para análisis y protección. | Verificar fuentes, ingestión, normalización, disponibilidad y excepciones. | Arquitectura, conectores, paneles, alertas y reportes de cobertura. |
| 8.10 | Conservar los registros de auditoría | Mantener registros durante períodos definidos por riesgo, operación y obligaciones. | Comparar requisitos, configuración y evidencia de eliminación. | Calendario de conservación, configuración y reportes. |
| 8.11 | Realizar revisiones de registros de auditoría | Revisar registros y alertas con frecuencia definida y seguimiento documentado. | Confirmar responsables, frecuencia, criterios, hallazgos y cierre. | Procedimientos, tickets, reportes de revisión y métricas. |
| 8.12 | Recopilar registros de proveedores de servicios | Obtener registros relevantes de servicios externos y plataformas administradas. | Verificar contratos, acceso, cobertura, formato, conservación y fallos. | Contratos, configuraciones, registros recibidos y tickets. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 14. Control 9 — Protecciones de correo electrónico y navegador web

*Las 7 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para las protecciones de correo electrónico y navegador web. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 9.1 | Asegurar el uso de navegadores y clientes de correo con soporte vigente | Permitir únicamente productos y versiones que reciben soporte de seguridad. | Revisar inventario, versiones, fechas de soporte, excepciones y corrección. | Inventario, versiones, boletines de proveedor y tickets. |
| 9.2 | Utilizar servicios de filtrado DNS | Bloquear dominios maliciosos o no permitidos mediante resolutores y políticas administradas. | Confirmar cobertura, reglas, registros, excepciones y pruebas. | Configuración DNS, políticas, eventos y resultados de prueba. |
| 9.3 | Mantener y aplicar filtros URL basados en red | Controlar el acceso web conforme al riesgo y la política. | Verificar cobertura, categorías, reglas, excepciones y eventos. | Configuración SWG/proxy, políticas, registros y tickets. |
| 9.4 | Restringir extensiones innecesarias o no autorizadas de navegador y correo | Permitir solo extensiones aprobadas y administradas. | Confirmar listas, despliegue, cobertura, excepciones y bloqueos. | Políticas, inventarios, eventos y aprobaciones. |
| 9.5 | Implementar DMARC | Configurar SPF, DKIM y DMARC para reducir la suplantación de dominios. | Revisar registros DNS, alineación, política, reportes y evolución. | Registros DNS, reportes DMARC, tickets y métricas. |
| 9.6 | Bloquear tipos de archivo innecesarios | Impedir archivos adjuntos o descargas de alto riesgo no requeridos. | Confirmar política, cobertura, excepciones, eventos y pruebas. | Reglas, registros de bloqueo, excepciones y resultados de prueba. |
| 9.7 | Implementar y mantener protección antimalware del servidor de correo | Analizar mensajes y archivos mediante controles administrados y actualizados. | Verificar cobertura, configuración, actualizaciones, alertas y respuesta. | Consola, políticas, eventos, tickets y métricas. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 15. Control 10 — Defensas contra malware

*Las 7 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para las defensas contra malware. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 10.1 | Implementar y mantener software antimalware | Proteger los activos aplicables mediante soluciones antimalware administradas. | Confirmar cobertura, estado, configuración, excepciones y respuesta. | Consola, inventario, políticas, alertas y tickets. |
| 10.2 | Configurar actualizaciones automáticas de firmas antimalware | Mantener firmas, motores y componentes actualizados automáticamente. | Verificar frecuencia, éxito, fallos, cobertura y excepciones. | Reportes de actualización, configuración, alertas y tickets. |
| 10.3 | Deshabilitar Autorun y Autoplay para medios extraíbles | Impedir la ejecución automática de contenido desde medios removibles. | Confirmar política, configuración, cobertura y excepciones. | GPO/MDM, resultados de consulta y reportes. |
| 10.4 | Configurar análisis antimalware automático de medios extraíbles | Analizar medios removibles al conectarse o antes de su uso. | Verificar configuración, cobertura, eventos y tratamiento de fallos. | Consola, políticas, registros y tickets. |
| 10.5 | Habilitar funciones contra explotación | Activar controles que dificulten la explotación de vulnerabilidades. | Confirmar configuración, cobertura, compatibilidad, excepciones y alertas. | Políticas, consola, inventario y resultados de prueba. |
| 10.6 | Administrar centralmente el software antimalware | Utilizar una plataforma central para configuración, supervisión y respuesta. | Verificar cobertura, comunicación, permisos, alertas y métricas. | Consola, roles, paneles, reportes y tickets. |
| 10.7 | Utilizar software antimalware basado en comportamiento | Detectar actividad maliciosa mediante análisis de comportamiento, no solo firmas. | Confirmar cobertura, reglas, alertas, ajustes y respuesta. | Configuración EDR, eventos, casos, tickets y métricas. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.
