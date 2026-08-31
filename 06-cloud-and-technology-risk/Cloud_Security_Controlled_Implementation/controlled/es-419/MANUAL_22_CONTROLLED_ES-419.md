# Manual 22 — Implementación Controlada de Seguridad en la Nube

**Localización controlada es-419 — traducción no oficial del proyecto**  
**Orden de la serie:** 22  
**Estado de referencia principal actual:** Cloud Security Alliance Cloud Controls Matrix (CCM) v4.1  
**Límite:** Guía original de implementación. La guía nativa de proveedores sirve como evidencia de implementación, no sustituye la ley aplicable, estándares independientes ni la intención de los controles de CSA. Los cruces son mapeos, no equivalencias. Este manual no implica registro, atestación ni certificación CSA STAR.

## 1. Gobierno de nube y modelo operativo
Definir responsabilidad ejecutiva, propiedad de seguridad en nube, funciones de plataforma y aplicaciones, aceptación de riesgo, autoridad de arquitectura, incorporación de servicios y jerarquía de políticas. Establecer derechos de decisión entre seguridad, ingeniería de plataforma, aplicaciones, privacidad, resiliencia, compras, finanzas y proveedores. Evidencia: estatuto de gobierno, RACI, políticas, estándares, autoridades de excepción y decisiones de gestión.

## 2. Alcance, tenencia, cuentas, suscripciones, proyectos y landing zones
Mantener un alcance autorizado de organizaciones, tenants, grupos de administración, cuentas, suscripciones, proyectos, carpetas, landing zones, regiones, entornos y propietarios. Usar aprovisionamiento, nombres y etiquetas gobernados para evitar activos no administrados. Evidencia: inventarios, propiedad, diagramas jerárquicos, definiciones de landing zone, estado de ciclo de vida y conciliación con APIs del proveedor.

## 3. Responsabilidad compartida y asignación contractual
Documentar responsabilidades por modelo de servicio, despliegue, capacidad del proveedor, contrato, servicio gestionado y configuración del cliente. No depender de matrices genéricas si el servicio o contrato real asigna deberes de otra manera. Evidencia: matrices, cláusulas, declaraciones del proveedor, obligaciones del cliente, brechas y disparadores de reevaluación.

## 4. Evaluación de riesgo en nube y registros de decisión de arquitectura
Evaluar riesgos considerando sensibilidad de datos, criticidad, rutas de identidad, exposición a Internet, dependencia del proveedor, concentración regional, cadena de suministro, resiliencia, restricciones legales y cambios operativos. Registrar decisiones materiales y alternativas descartadas. Evidencia: evaluaciones, modelos de amenaza, ADR, supuestos, riesgo residual y aprobaciones.

## 5. Federación de identidad, autenticación y acceso privilegiado
Centralizar identidad cuando sea práctico, aplicar autenticación fuerte, restringir privilegios, separar planos administrativos, usar elevación temporal y revisar accesos de alto riesgo. Proteger identidades de emergencia por separado. Evidencia: configuración de federación, políticas MFA, inventarios privilegiados, registros de elevación, revisiones y pruebas de cuentas break-glass.

## 6. Identidad de cargas de trabajo y cuentas de servicio
Gobernar cuentas de servicio, identidades administradas, federación de cargas, service principals, identidades API, certificados y credenciales automáticas. Preferir mecanismos de corta duración o administrados por el proveedor frente a secretos estáticos. Evidencia: inventario, propietario, permisos, antigüedad, políticas de confianza, rotación, identidades inactivas y excepciones.

## 7. Arquitectura de red, segmentación, ingreso y egreso
Definir patrones de red aprobados, segmentación, enrutamiento, ingreso de Internet, egreso, conectividad privada, endpoints, DNS, acceso administrativo y comunicación entre entornos. Aplicar conectividad mínima o denegación por defecto cuando sea viable. Evidencia: diagramas, matrices de flujo, políticas de firewall/grupos de seguridad, rutas, controles de egreso, pruebas y excepciones.

## 8. Patrones Zero Trust y confianza entre servicios
Autenticar y autorizar conexiones con identidad verificada, contexto de carga, política y mínimo privilegio, no solo ubicación de red. Gobernar service mesh, mTLS, gateways API, proxies conscientes de identidad y puntos de aplicación. Evidencia: arquitectura de confianza, identidades, políticas de autorización, certificados, pruebas y accesos denegados.

## 9. Clasificación, residencia, soberanía y ciclo de vida de datos
Clasificar datos y mapear dónde se crean, almacenan, procesan, replican, respaldan, transfieren, archivan y eliminan. Evaluar residencia, soberanía, contrato, sector y privacidad según aplicabilidad real. Evidencia: inventarios, clasificaciones, ubicaciones, rutas de transferencia, calendarios de retención y decisiones aprobadas.

## 10. Cifrado, gestión de claves, HSM y secretos
Definir cifrado en reposo y tránsito, propiedad de claves, KMS/HSM, rotación, acceso, segregación de funciones, recuperación y gestión de secretos. Evitar secretos de larga duración en código o plantillas. Evidencia: inventarios, políticas, configuraciones KMS/HSM, almacenes de secretos, rotaciones, registros y excepciones.

## 11. Registros, telemetría, auditoría e integridad temporal
Habilitar eventos administrativos, de identidad, red, datos, cargas, servicios de seguridad y plataforma según riesgo. Proteger registros, mantener retención adecuada y referencias de tiempo consistentes. Evidencia: estándares, fuentes habilitadas, salud de ingestión, retención, destinos protegidos, tiempo y controles de acceso.

## 12. Ingeniería de detección y monitoreo de amenazas
Desarrollar detecciones para abuso de credenciales, escalamiento de privilegios, API sospechosa, recursos expuestos, cargas maliciosas, exfiltración, cambios de políticas y persistencia. Usar herramientas nativas sin asumir que habilitarlas por sí solas equivale a control efectivo. Evidencia: reglas, cobertura, pruebas, investigaciones, ajustes y métricas.

## 13. Líneas base de configuración y policy as code
Definir líneas base seguras y aplicarlas o evaluarlas mediante motores de políticas. Separar políticas preventivas, detectivas y asesoras y gobernar excepciones. Evidencia: líneas base, repositorios, asignaciones, resultados, despliegues bloqueados, exenciones y remediación de drift.

## 14. Infraestructura como código y control de drift
Gestionar infraestructura mediante repositorios controlados, revisión, pruebas, aprobaciones, pipelines protegidos e historial de versiones. Detectar divergencia entre estado declarado y desplegado y gobernar cambios manuales o de emergencia. Evidencia: repositorios IaC, revisiones, pipelines, planes, reportes de drift y conciliaciones.

## 15. Vulnerabilidades, parches, imágenes y dependencias
Inventariar vulnerabilidades de sistemas, paquetes, imágenes, bibliotecas, servicios gestionados, appliances y dependencias. Priorizar por exposición, explotabilidad, criticidad, salvaguardas y responsabilidad del proveedor. Evidencia: cobertura de escaneo, hallazgos, parches, alertas, tickets, excepciones, re-pruebas y avisos del proveedor.

## 16. Seguridad de contenedores, Kubernetes y orquestación
Proteger clústeres, planos de control, nodos, registros, admisión, RBAC, namespaces, políticas de red, secretos, cargas, imágenes y comportamiento runtime. Separar privilegios de plataforma y de cargas. Evidencia: inventarios, líneas base, políticas de admisión, procedencia de imágenes, revisiones RBAC, alertas y remediación.

## 17. Serverless, PaaS, servicios gestionados y APIs
Aplicar controles específicos a funciones, bases gestionadas, colas, analítica, servicios de IA, APIs y demás PaaS. Gobernar identidad, exposición, configuración, datos, logging, versiones, cuotas y responsabilidades del proveedor. Evidencia: inventarios, políticas API, configuraciones, registros, ajustes de datos y decisiones de riesgo.

## 18. Seguridad SaaS y aseguramiento de configuración del tenant
Inventariar tenants SaaS y gobernar administradores, federación, MFA, compartición, colaboración externa, retención, integraciones, registros, aplicaciones y configuraciones globales. Evidencia: inventario SaaS, revisiones de roles, evaluaciones, aplicaciones conectadas, ajustes de compartición, registros y remediación.

## 19. DevSecOps, CI/CD, firma e integridad de compilación
Proteger repositorios, runners, sistemas de compilación, identidades de despliegue, artefactos, registros y aprobaciones. Aplicar protección de ramas, dependencias, detección de secretos, aislamiento, firma/procedencia y promoción controlada. Evidencia: pipelines, revisiones, escaneos, artefactos firmados, attestations y registros de release.

## 20. Respaldo, recuperación, inmutabilidad y resiliencia ante ransomware
Definir cobertura, aislamiento, inmutabilidad cuando corresponda, retención, estrategias entre cuentas/regiones, prioridades de restauración y separación de credenciales. Probar restauración, no solo éxito de jobs. Evidencia: políticas, inventarios, pruebas, configuraciones inmutables, acceso, tiempos observados y remediación.

## 21. Disponibilidad, resiliencia regional y dominios de falla
Diseñar según requisitos de resiliencia entre zonas, regiones, servicios, identidades, redes, DNS, datos y proveedores externos. Identificar puntos únicos de falla y supuestos de recuperación. Evidencia: arquitectura, dependencias, pruebas de failover, capacidad, límites y acciones correctivas.

## 22. Respuesta a incidentes, forense y preservación de evidencia en nube
Preparar playbooks para compromiso de identidad, exposición de datos, cargas maliciosas, ransomware, cryptomining, abuso del control plane y eventos del proveedor. Preservar snapshots, logs, historial API, identidades y evidencia volátil respetando capacidades del proveedor. Evidencia: playbooks, cronologías, evidencia preservada, casos con proveedor, ejercicios y lecciones.

## 23. Inventario, descubrimiento, propiedad y etiquetado de activos
Identificar continuamente recursos, activos efímeros, endpoints públicos, almacenes de datos, claves, cargas, imágenes, integraciones SaaS y cuentas no administradas. Exigir propietario y estado de ciclo de vida. Evidencia: fuentes de inventario, cumplimiento de etiquetas, huérfanos, atestaciones y registros de limpieza.

## 24. Riesgo de terceros, marketplace y servicios gestionados
Gobernar imágenes de marketplace, integraciones SaaS, MSP, APIs externas, plugins y otros componentes. Evaluar acceso a datos, privilegios, dependencia, soporte, vulnerabilidades, incidentes y salida. Evidencia: registro de proveedores/componentes, evaluaciones, permisos, contratos, monitoreo y terminación.

## 25. Aseguramiento de proveedores de nube y evidencia contractual
Recopilar evidencia proporcional al riesgo: informes independientes, certificaciones relevantes, compromisos de servicio, arquitectura, obligaciones de incidentes y subprocesadores. Validar alcance y período, no tratar insignias como aseguramiento universal. Evidencia: informes, mapeos, contratos, hallazgos, bridge letters cuando aplique y decisiones.

## 26. Privacidad, registros, retención y eliminación
Configurar capacidades que apoyen obligaciones aplicables de privacidad y registros: limitación de propósito, acceso, retención, legal holds, eliminación, exportación y evidencia de disposición. Separar capacidad técnica de determinación legal. Evidencia: configuraciones, jobs de borrado, holds, evaluaciones y pruebas de ciclo de vida.

## 27. Interfaces de seguridad con costo, capacidad, abuso y gobierno de recursos
Tratar costos inesperados, agotamiento, abuso de cuotas, cryptomining, denial-of-wallet y aprovisionamiento descontrolado como señales de seguridad o resiliencia cuando corresponda. Establecer presupuestos, cuotas, anomalías y escalamiento sin confundir gobierno financiero con control cibernético. Evidencia: umbrales, alertas, capacidad, investigaciones y acciones.

## 28. Consistencia de controles multi-cloud e híbridos
Definir qué controles son empresariales y cuáles dependen del proveedor entre nube, SaaS, on-premises y edge. Normalizar evidencia sin ocultar diferencias materiales. Evidencia: matriz cross-cloud, patrones de identidad/red/datos, desviaciones, cobertura, brechas y planes de migración.

## 29. Métricas, salud de controles, monitoreo continuo y excepciones
Medir exposición privilegiada, recursos públicos, violaciones de políticas, brechas de logging, riesgo sin parchear, identidades obsoletas, fallas de backup, hallazgos y antigüedad de excepciones. Evidencia: dashboards, fuentes, umbrales, tendencias, decisiones, registros y remediación.

## 30. Evaluación, aseguramiento, pruebas y muestreo de evidencia
Definir alcance, muestreo, validación técnica, revisión de configuración, pruebas de control, confianza en controles heredados e interfaces con evaluadores. La automatización puede recolectar y probar evidencia, pero no crea certificación ni reemplaza juicio profesional externo cuando sea realmente requerido. Evidencia: planes, muestras, workpapers, hallazgos, remediación y re-pruebas.

## 31. Migración, modernización, salida, portabilidad y retiro
Planificar migraciones de entrada, entre proveedores y de salida. Cubrir transferencia de datos, identidades, claves, conversión de configuración, dependencias, salida contractual, retención de evidencia y retiro seguro. Evidencia: planes, pruebas de portabilidad, conciliación de inventario, confirmación de borrado, revocación y decisiones sobre datos residuales.

## 32. Paquete de evidencia, roadmap, cambio de fuentes y mejora continua
Para cada salvaguarda registrar propietario, alcance, procedimiento, frecuencia/disparador, objeto de evidencia, método de prueba, hallazgos, remediación y disparador de reevaluación. Revalidar versión CCM/CAIQ, fechas de transición, mapeos, guía relevante del proveedor y dependencias STAR al liberar. Congelar inglés exacto antes de localización es-419 y pt-BR; marcar traducciones como no oficiales; exigir paridad, generación reproducible de seis binarios, QA de renderizado/accesibilidad, procedencia SHA-256, seguridad de workflows, staging exacto, publicación del predecesor y conciliación de catálogo/registro.

## Límite de liberación controlada
Este manual no establece cumplimiento, equivalencia legal, certificación del proveedor ni estado CSA STAR. CCM v4.1 es el estado de referencia CSA actual registrado por la compuerta de fuentes; la transición v4.0.x debe revalidarse antes de liberar. Bajo la regla canónica del repositorio, un candidato limpio con todas las compuertas objetivas aplicables en verde y su predecesor publicado avanza bajo autorización permanente salvo que exista un asunto especialista específico, documentado y genuinamente no determinístico.