# 6. Control 1 — Inventario y control de activos empresariales

*Las 5 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

<img src="media/image4.png" style="width:6.15in;height:3.38991in" alt="El descubrimiento, la conciliación, la respuesta y la revisión mantienen actualizadas las poblaciones fundamentales." />

Figura 4. Ciclo de inventario de activos y software

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para el inventario y control de activos empresariales. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 1.1 | Establecer y mantener un inventario detallado de activos empresariales | Establecer un proceso repetible y con responsable definido para mantener un inventario detallado de activos y verificar su cobertura y excepciones. | Confirmar alcance, población, propietario, frecuencia, cobertura, excepciones, corrección y nueva prueba. | Inventario de activos, propietarios, estado de aprobación, descubrimiento activo y pasivo, registros DHCP/IPAM y tickets de activos no autorizados. |
| 1.2 | Abordar los activos no autorizados | Detectar, investigar y retirar, aislar o autorizar formalmente los activos no autorizados. | Verificar que las alertas generan acciones trazables y oportunas. | Alertas, tickets, registros de aislamiento, autorizaciones y evidencia de cierre. |
| 1.3 | Utilizar una herramienta de descubrimiento activo | Ejecutar descubrimiento activo para identificar activos conectados y conciliar los resultados con el inventario. | Confirmar cobertura, programación, exclusiones y conciliación. | Configuración de escaneo, resultados, inventario actualizado y excepciones aprobadas. |
| 1.4 | Utilizar registros DHCP para actualizar el inventario de activos empresariales | Integrar registros DHCP con el proceso de actualización y conciliación del inventario. | Verificar ingestión, frecuencia, cobertura y tratamiento de discrepancias. | Registros DHCP, integraciones, reportes de conciliación y tickets. |
| 1.5 | Utilizar una herramienta de descubrimiento pasivo de activos | Supervisar tráfico o telemetría para identificar activos sin generar exploración activa. | Confirmar sensores, segmentos cubiertos, alertas y conciliación. | Configuración de sensores, resultados, cobertura de red y actualizaciones del inventario. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto, la clase de activo, la función de seguridad, el Grupo de Implementación, las dependencias, las entradas, las operaciones, las medidas, las métricas y la revisión de procedimientos.

# 7. Control 2 — Inventario y control de activos de software

*Las 7 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para el inventario y control de activos de software. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 2.1 | Establecer y mantener un inventario de software | Mantener un inventario autorizado, actualizado y con responsables definidos. | Confirmar alcance, propietario, frecuencia, cobertura y excepciones. | Inventario, versiones, propietarios, estado de soporte y resultados de descubrimiento. |
| 2.2 | Asegurar que el software autorizado tenga soporte vigente | Identificar software sin soporte y actualizarlo, reemplazarlo o gestionarlo mediante una excepción aprobada. | Verificar fechas de fin de soporte y acciones correctivas. | Inventario, boletines de proveedor, planes de actualización y excepciones. |
| 2.3 | Abordar el software no autorizado | Detectar y retirar, bloquear o aprobar formalmente el software no autorizado. | Confirmar que los hallazgos generan acciones trazables. | Alertas, tickets, registros de desinstalación, bloqueos y aprobaciones. |
| 2.4 | Utilizar herramientas automatizadas de inventario de software | Automatizar la detección de software instalado y conciliarla con el inventario autorizado. | Verificar cobertura, frecuencia y tratamiento de discrepancias. | Configuración de herramientas, resultados y reportes de conciliación. |
| 2.5 | Crear una lista de software autorizado | Permitir la ejecución únicamente del software aprobado conforme al riesgo y la necesidad empresarial. | Confirmar política, cobertura, excepciones y eventos de bloqueo. | Política de allowlisting, reglas, excepciones y registros de eventos. |
| 2.6 | Crear una lista de bibliotecas autorizadas | Restringir bibliotecas y componentes cargados a versiones aprobadas. | Verificar reglas, cobertura y excepciones. | Configuración, inventario de bibliotecas, eventos y aprobaciones. |
| 2.7 | Crear una lista de scripts autorizados | Restringir la ejecución de scripts a los aprobados y controlados. | Confirmar firma, reglas, cobertura y excepciones. | Repositorio aprobado, firmas, reglas de ejecución y eventos. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 8. Control 3 — Protección de datos

*Las 14 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

<img src="media/image5.png" style="width:6.15in;height:3.39605in" alt="Descubrir, clasificar, proteger, conservar y eliminar datos según su sensibilidad y necesidad." />

Figura 5. Ciclo de vida de protección de datos

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la protección de datos. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 3.1 | Establecer y mantener un proceso de gestión de datos | Definir cómo se identifican, clasifican, protegen, conservan y eliminan los datos. | Confirmar alcance, propietario, revisión y aplicación. | Política, procedimientos, responsables y registros de revisión. |
| 3.2 | Establecer y mantener un inventario de datos | Mantener un inventario de conjuntos de datos, ubicación, propietario, sensibilidad y uso. | Verificar cobertura, actualidad y conciliación. | Inventario, catálogos, propietarios y resultados de descubrimiento. |
| 3.3 | Configurar listas de control de acceso a datos | Limitar el acceso a datos conforme a necesidad y autorización. | Revisar permisos, roles, excepciones y recertificaciones. | ACL, roles, aprobaciones y revisiones de acceso. |
| 3.4 | Aplicar la retención de datos | Conservar los datos durante el período aprobado y exigido. | Comparar reglas, sistemas y resultados. | Calendario de retención, configuraciones y registros. |
| 3.5 | Eliminar datos de forma segura | Destruir o borrar datos de manera verificable cuando ya no sean necesarios. | Confirmar método, cobertura y evidencia de eliminación. | Certificados, registros, tickets y pruebas de borrado. |
| 3.6 | Cifrar datos en dispositivos de usuario final | Proteger datos almacenados en dispositivos mediante cifrado administrado. | Verificar cobertura, claves, excepciones y estado. | Consola de cifrado, inventario, políticas y excepciones. |
| 3.7 | Establecer y mantener un esquema de clasificación de datos | Definir niveles de sensibilidad y reglas de manejo. | Confirmar criterios, aprobación, comunicación y uso. | Esquema, etiquetas, procedimientos y capacitación. |
| 3.8 | Documentar los flujos de datos | Mantener diagramas y registros de cómo se recopilan, procesan, almacenan y transfieren los datos. | Verificar integridad, actualidad y propietarios. | Diagramas, registros de tratamiento e interfaces. |
| 3.9 | Cifrar datos en medios extraíbles | Exigir cifrado para datos almacenados en medios removibles. | Confirmar política, configuración y excepciones. | Configuración, inventario de medios y registros. |
| 3.10 | Cifrar datos sensibles en tránsito | Proteger comunicaciones que transportan datos sensibles. | Revisar protocolos, certificados, cobertura y excepciones. | Configuración TLS/VPN, certificados y resultados de pruebas. |
| 3.11 | Cifrar datos sensibles en reposo | Proteger datos sensibles almacenados en bases, archivos y respaldos. | Confirmar algoritmos, claves, cobertura y excepciones. | Configuración, KMS/HSM, inventarios y pruebas. |
| 3.12 | Segmentar el procesamiento y almacenamiento de datos según su sensibilidad | Separar entornos y repositorios según clasificación y riesgo. | Revisar arquitectura, reglas y flujos permitidos. | Diagramas, segmentación, reglas y resultados de pruebas. |
| 3.13 | Implementar una solución de prevención de pérdida de datos | Detectar y controlar transferencias no autorizadas de datos sensibles. | Verificar cobertura, reglas, alertas, excepciones y respuesta. | Políticas DLP, eventos, tickets y métricas. |
| 3.14 | Registrar el acceso a datos sensibles | Mantener registros suficientes para identificar quién accedió a datos sensibles y qué acción realizó. | Confirmar fuentes, detalle, retención y revisión. | Registros de acceso, SIEM, alertas y revisiones. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 9. Control 4 — Configuración segura de activos empresariales y software

*Las 12 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la configuración segura de activos empresariales y software. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 4.1 | Establecer y mantener un proceso de configuración segura | Definir, aprobar, implementar y revisar configuraciones seguras para activos y software. | Confirmar estándares, responsables, frecuencia, cobertura y excepciones. | Estándares, líneas base, resultados de evaluación y excepciones. |
| 4.2 | Establecer y mantener un proceso de configuración segura para la infraestructura de red | Aplicar líneas base seguras a dispositivos y servicios de red. | Revisar cobertura, cambios, desviaciones y correcciones. | Configuraciones, respaldos, comparaciones y tickets. |
| 4.3 | Configurar el bloqueo automático de sesión en activos empresariales | Bloquear sesiones inactivas después del período aprobado. | Verificar política, configuración y cobertura. | GPO/MDM, resultados de consulta y excepciones. |
| 4.4 | Implementar y administrar un firewall en servidores | Habilitar y gestionar reglas de firewall en servidores. | Revisar cobertura, reglas, cambios y excepciones. | Configuración, inventario, reglas y registros. |
| 4.5 | Implementar y administrar un firewall en dispositivos de usuario final | Habilitar y gestionar el firewall local en endpoints. | Confirmar cobertura y estado centralizado. | Consola, políticas y reportes de cumplimiento. |
| 4.6 | Administrar de forma segura los activos empresariales y el software | Utilizar protocolos y canales administrativos seguros. | Revisar métodos de administración, autenticación y registros. | Configuración, listas de administradores y registros. |
| 4.7 | Administrar cuentas predeterminadas en activos empresariales y software | Deshabilitar, cambiar o controlar cuentas predeterminadas. | Confirmar inventario, estado y excepciones. | Resultados de escaneo, configuración y tickets. |
| 4.8 | Desinstalar o deshabilitar servicios innecesarios | Reducir superficie de ataque retirando servicios no requeridos. | Comparar líneas base, servicios activos y excepciones. | Inventario de servicios, configuración y aprobaciones. |
| 4.9 | Configurar servidores DNS de confianza en activos empresariales | Forzar el uso de resolutores DNS aprobados. | Verificar configuración, cobertura y desvíos. | GPO/MDM, configuración de red y registros DNS. |
| 4.10 | Aplicar bloqueo automático del dispositivo en equipos portátiles de usuario final | Bloquear dispositivos portátiles tras inactividad o intentos fallidos. | Confirmar política, configuración y cobertura. | MDM, políticas y reportes. |
| 4.11 | Aplicar capacidad de borrado remoto en dispositivos portátiles de usuario final | Permitir borrado remoto administrado cuando el riesgo lo requiera. | Verificar cobertura, autorización y pruebas. | Consola MDM, procedimientos y registros de prueba. |
| 4.12 | Separar espacios de trabajo empresariales en dispositivos móviles de usuario final | Separar datos y aplicaciones empresariales de los personales. | Revisar perfiles, políticas y cobertura. | Configuración MDM/MAM, inventario y reportes. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.

# 10. Control 5 — Gestión de cuentas

*Las 6 Salvaguardas, su significado claro, el enfoque de verificación y ejemplos de evidencia.*

| **Propósito del control:** Fortalecer la empresa mediante la implementación y medición de Salvaguardas para la gestión de cuentas. |
|---|

| **ID** | **Salvaguarda** | **Significado claro** | **Enfoque de verificación** | **Ejemplos de evidencia** |
|---|---|---|---|---|
| 5.1 | Establecer y mantener un inventario de cuentas | Mantener una población completa de cuentas con propietario, tipo, estado y fechas relevantes. | Confirmar cobertura, actualidad, responsables y conciliación. | Inventarios, directorios, reportes y revisiones. |
| 5.2 | Utilizar contraseñas únicas | Impedir la reutilización de contraseñas entre cuentas administradas. | Revisar política, configuración, excepciones y pruebas. | Política, configuración de identidad y resultados de auditoría. |
| 5.3 | Deshabilitar cuentas inactivas | Deshabilitar oportunamente cuentas que superen el período de inactividad aprobado. | Confirmar umbral, ejecución, excepciones y seguimiento. | Reportes, tickets, registros y aprobaciones. |
| 5.4 | Restringir privilegios administrativos a cuentas administrativas dedicadas | Separar las actividades administrativas de las cuentas de uso normal. | Revisar asignaciones, uso, excepciones y registros. | Inventario de administradores, roles y registros de acceso. |
| 5.5 | Establecer y mantener un inventario de cuentas de servicio | Identificar cuentas de servicio, propietarios, propósito, privilegios y ciclo de vida. | Verificar cobertura, revisión y credenciales. | Inventario, propietarios, rotación y revisiones. |
| 5.6 | Centralizar la gestión de cuentas | Administrar cuentas mediante servicios centralizados cuando sea viable. | Confirmar sistemas cubiertos, sincronización, excepciones y monitoreo. | Arquitectura, configuración, directorios y reportes. |

Utilice la guía oficial de CIS Controls v8.1 y la Especificación de Evaluación de Controles para el lenguaje exacto y los criterios de evaluación.
