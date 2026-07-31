# 18. Control 13 — Monitoreo y defensa de la red

*Las 11 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

<img src="media/image8.png" style="width:6.15in;height:3.20094in" alt="El contexto centralizado, la detección ajustada, la investigación humana y la respuesta crean una defensa útil." />

Figura 8. Monitoreo y defensa de la red

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para el monitoreo y la defensa de la red. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 13.1 | Centralizar las alertas de eventos de seguridad | Consolidar alertas relevantes en una capacidad central para su análisis y respuesta. | Confirmar fuentes, cobertura, responsables, priorización, retención y seguimiento. | Inventario de fuentes, configuración SIEM, alertas, tickets y métricas. |
| 13.2 | Implementar una solución de detección de intrusiones basada en host | Detectar actividad sospechosa en activos empresariales mediante sensores administrados. | Verificar cobertura, estado, reglas, excepciones y respuesta. | Consola HIDS/EDR, inventario, políticas, alertas y tickets. |
| 13.3 | Implementar una solución de detección de intrusiones de red | Supervisar tráfico de red para identificar actividad maliciosa o anómala. | Revisar ubicación de sensores, cobertura, reglas, alertas y excepciones. | Diagramas, configuración NIDS, registros, alertas y casos. |
| 13.4 | Realizar filtrado de tráfico entre segmentos de red | Restringir comunicaciones entre segmentos conforme al riesgo y la necesidad empresarial. | Confirmar arquitectura, reglas, cambios, pruebas y excepciones. | Diagramas, reglas, resultados de pruebas y tickets de cambio. |
| 13.5 | Administrar el control de acceso para activos remotos | Aplicar controles de acceso, autenticación y monitoreo a conexiones remotas. | Verificar población, métodos, MFA, registros y excepciones. | Configuración VPN/ZTNA, inventario, registros y revisiones. |
| 13.6 | Recopilar registros de flujo de tráfico de red | Conservar telemetría de flujo suficiente para investigación y análisis. | Confirmar fuentes, campos, cobertura, sincronización, retención y acceso. | NetFlow/IPFIX, inventario de fuentes, almacenamiento y consultas. |
| 13.7 | Implementar una solución de prevención de intrusiones basada en host | Bloquear o contener actividad maliciosa en activos empresariales. | Verificar modo de prevención, cobertura, reglas, excepciones y eventos. | Configuración HIPS/EDR, eventos de bloqueo, tickets y excepciones. |
| 13.8 | Implementar una solución de prevención de intrusiones de red | Detectar y bloquear tráfico malicioso en puntos de control de red. | Confirmar ubicación, cobertura, políticas, pruebas y respuesta. | Configuración NIPS, reglas, alertas, bloqueos y métricas. |
| 13.9 | Implementar control de acceso a nivel de puerto | Restringir el acceso a la red mediante autenticación o políticas de puerto. | Verificar alcance, configuración, excepciones y eventos de denegación. | Configuración 802.1X/NAC, inventario, registros y tickets. |
| 13.10 | Realizar filtrado de capa de aplicación | Inspeccionar y controlar tráfico según aplicaciones, protocolos y riesgo. | Revisar políticas, cobertura, excepciones, eventos y pruebas. | Reglas de firewall/proxy, registros, alertas y aprobaciones. |
| 13.11 | Ajustar los umbrales de alerta de eventos de seguridad | Revisar y ajustar reglas para reducir ruido sin perder detecciones relevantes. | Confirmar frecuencia, responsables, métricas, cambios y validación. | Historial de ajustes, casos de uso, métricas y aprobaciones. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 19. Control 14 — Concienciación y capacitación en habilidades de seguridad

*Las 9 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la concienciación y capacitación en habilidades de seguridad. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 14.1 | Establecer y mantener un programa de concienciación sobre seguridad | Mantener un programa aprobado, periódico y basado en riesgos para toda la fuerza laboral. | Confirmar alcance, responsables, frecuencia, finalización, excepciones y mejora. | Plan, contenidos, calendario, registros de finalización y métricas. |
| 14.2 | Capacitar para reconocer ataques de ingeniería social | Enseñar a identificar y reportar phishing, suplantación y otras tácticas sociales. | Verificar contenidos, población, simulaciones, resultados y seguimiento. | Materiales, campañas, resultados, reportes y acciones correctivas. |
| 14.3 | Capacitar sobre mejores prácticas de autenticación | Explicar contraseñas, MFA, protección de credenciales y reporte de anomalías. | Confirmar cobertura, comprensión, frecuencia y excepciones. | Contenido, evaluaciones, registros y métricas. |
| 14.4 | Capacitar sobre mejores prácticas de manejo de datos | Enseñar clasificación, almacenamiento, transferencia, retención y eliminación segura. | Revisar alineación con políticas, población, evaluación y seguimiento. | Materiales, políticas, evaluaciones y registros. |
| 14.5 | Capacitar sobre causas de exposición involuntaria de datos | Explicar errores comunes y controles preventivos para reducir divulgaciones accidentales. | Verificar escenarios, población, evaluación y lecciones aprendidas. | Casos, contenidos, resultados y acciones de mejora. |
| 14.6 | Capacitar para reconocer y reportar incidentes de seguridad | Enseñar indicadores, canales de reporte y acciones iniciales. | Confirmar claridad, disponibilidad, pruebas y tiempos de reporte. | Procedimientos, ejercicios, registros y métricas. |
| 14.7 | Capacitar para identificar y reportar actualizaciones de seguridad faltantes | Enseñar a reconocer activos o aplicaciones desactualizados y reportarlos. | Verificar contenidos, canales, población y seguimiento. | Materiales, reportes, tickets y métricas. |
| 14.8 | Capacitar sobre los riesgos de redes inseguras | Explicar riesgos de redes públicas, acceso remoto y medidas de protección. | Confirmar cobertura, escenarios, evaluación y excepciones. | Contenidos, evaluaciones y registros. |
| 14.9 | Realizar capacitación específica por función | Proporcionar formación adicional según responsabilidades y exposición al riesgo. | Verificar perfiles, requisitos, frecuencia, finalización y eficacia. | Matriz de funciones, rutas formativas, registros y evaluaciones. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 20. Control 15 — Gestión de proveedores de servicios

*Las 7 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la gestión de proveedores de servicios. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 15.1 | Establecer y mantener un inventario de proveedores de servicios | Mantener una población completa de proveedores, propietarios, servicios, datos y criticidad. | Confirmar cobertura, actualidad, responsables y conciliación. | Inventario, contratos, propietarios, clasificaciones y revisiones. |
| 15.2 | Establecer y mantener una política de gestión de proveedores de servicios | Definir requisitos de selección, evaluación, contratación, monitoreo y terminación. | Verificar aprobación, alcance, responsabilidades, revisión y aplicación. | Política, procedimientos, RACI y registros de revisión. |
| 15.3 | Clasificar a los proveedores de servicios | Asignar niveles de riesgo y criticidad mediante criterios documentados. | Confirmar metodología, datos de entrada, aprobación y actualización. | Metodología, evaluaciones, clasificaciones y aprobaciones. |
| 15.4 | Asegurar que los contratos incluyan requisitos de seguridad | Incorporar obligaciones proporcionales al riesgo, incluidos incidentes, auditoría y terminación. | Revisar cláusulas, excepciones, aprobaciones y cobertura contractual. | Plantillas, contratos, anexos, excepciones y revisiones legales. |
| 15.5 | Evaluar a los proveedores de servicios | Evaluar controles y riesgos antes y durante la relación. | Confirmar alcance, evidencia, hallazgos, planes y aceptación de riesgo. | Cuestionarios, informes, certificaciones, hallazgos y planes. |
| 15.6 | Monitorear a los proveedores de servicios | Supervisar cambios, desempeño, incidentes y exposición durante la relación. | Verificar frecuencia, fuentes, umbrales, escalamiento y seguimiento. | Paneles, alertas, revisiones, tickets y métricas. |
| 15.7 | Retirar proveedores de servicios de forma segura | Revocar accesos, recuperar activos, transferir o eliminar datos y cerrar obligaciones. | Confirmar lista de cierre, responsables, evidencia y excepciones. | Tickets, revocaciones, certificados, actas y aprobaciones. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 21. Control 16 — Seguridad del software de aplicaciones

*Las 14 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la seguridad del software de aplicaciones. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 16.1 | Establecer y mantener un proceso seguro de desarrollo de aplicaciones | Integrar requisitos, responsabilidades, revisiones y controles de seguridad en el ciclo de vida. | Confirmar aprobación, cobertura, funciones, puertas de control y excepciones. | SDLC, estándares, RACI, listas de control y registros. |
| 16.2 | Establecer y mantener un proceso para aceptar y abordar vulnerabilidades de software | Recibir, priorizar, corregir y comunicar vulnerabilidades reportadas. | Verificar canales, SLA, propietarios, seguimiento y divulgación. | Política, buzón o portal, tickets, métricas y comunicaciones. |
| 16.3 | Realizar análisis de causa raíz de vulnerabilidades de seguridad | Identificar causas sistémicas y prevenir recurrencias. | Confirmar criterios, profundidad, acciones, propietarios y cierre. | Informes RCA, acciones correctivas, tickets y nuevas pruebas. |
| 16.4 | Establecer y administrar un inventario de componentes de software de terceros | Mantener componentes, versiones, dependencias, licencias y estado de soporte. | Verificar cobertura, actualización, propietarios y conciliación. | SBOM, inventarios, escaneos y registros de revisión. |
| 16.5 | Utilizar componentes de software de terceros actualizados y confiables | Seleccionar y mantener componentes compatibles, aprobados y con riesgo aceptable. | Confirmar criterios, versiones, fuentes, excepciones y actualización. | Repositorios, listas aprobadas, escaneos y excepciones. |
| 16.6 | Establecer y mantener un sistema de clasificación de gravedad y un proceso de tratamiento | Clasificar vulnerabilidades y definir plazos y acciones según riesgo. | Revisar metodología, SLA, excepciones, métricas y escalamiento. | Matriz, tickets, métricas y aprobaciones. |
| 16.7 | Utilizar plantillas de configuración segura para infraestructura de aplicaciones | Aplicar configuraciones aprobadas y repetibles a plataformas de aplicación. | Verificar plantillas, cobertura, desviaciones, cambios y pruebas. | IaC, imágenes, líneas base, resultados y tickets. |
| 16.8 | Separar sistemas de producción y no producción | Aislar entornos, datos, credenciales y accesos para reducir exposición. | Confirmar arquitectura, controles, excepciones y pruebas. | Diagramas, reglas, cuentas, resultados y aprobaciones. |
| 16.9 | Capacitar a desarrolladores en conceptos de desarrollo seguro | Proporcionar formación pertinente a tecnologías y riesgos utilizados. | Verificar población, contenidos, frecuencia, finalización y eficacia. | Rutas formativas, registros, evaluaciones y métricas. |
| 16.10 | Aplicar principios de diseño seguro en arquitecturas de aplicaciones | Incorporar mínimo privilegio, defensa en profundidad, validación y manejo seguro de fallos. | Revisar decisiones, modelos de amenaza, excepciones y aprobaciones. | Diseños, ADR, modelos de amenaza y revisiones. |
| 16.11 | Utilizar módulos o servicios examinados para componentes de seguridad | Preferir componentes aprobados para identidad, cifrado, registro y otras funciones críticas. | Confirmar catálogo, uso, excepciones y revisión. | Bibliotecas aprobadas, servicios, dependencias y pruebas. |
| 16.12 | Implementar comprobaciones de seguridad a nivel de código | Integrar análisis estático, revisión y controles equivalentes en el flujo de desarrollo. | Verificar cobertura, reglas, puertas, hallazgos y excepciones. | SAST, revisiones, resultados de CI/CD y tickets. |
| 16.13 | Realizar pruebas de penetración de aplicaciones | Evaluar aplicaciones según riesgo antes y durante su operación. | Confirmar alcance, metodología, independencia, hallazgos y nuevas pruebas. | Planes, informes, tickets, excepciones y resultados de cierre. |
| 16.14 | Realizar modelado de amenazas de aplicaciones | Identificar activos, límites de confianza, amenazas y mitigaciones durante el diseño. | Verificar alcance, participantes, actualización y seguimiento. | Modelos, diagramas, registros de riesgos y acciones. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.
