# Manual 06 — Implementación y Auditoría de HIPAA
## Fuente localizada es-419 — Capítulos 01–08

> Borrador de localización para revisión semántica humana. Guía educativa de implementación basada en la línea base controlada de HIPAA vigente. Este material no brinda asesoría legal, no determina el estatus de entidad cubierta o asociado de negocios, no establece cumplimiento ni determina si un incidente constituye una brecha notificable. Los cambios propuestos a la Regla de Seguridad son únicamente para preparación hasta que HHS emita una regla final y se actualice la línea base controlada.

## Capítulo 01 — Alcance, función de la entidad y responsabilidad

Comience determinando qué unidades organizacionales, sistemas, servicios y relaciones están dentro del alcance de implementación de HIPAA. Registre la base para el tratamiento como entidad cubierta, plan de salud, proveedor de atención médica, cámara de compensación, asociado de negocios o subcontratista, según corresponda, e identifique responsables de privacidad, seguridad, asuntos legales, cumplimiento, operaciones y negocio.

El registro de implementación debe distinguir los hechos confirmados de los supuestos que requieren interpretación legal o regulatoria. Las decisiones de alcance deben estar fechadas, respaldadas por evidencia y reevaluarse después de cambios materiales organizacionales, de servicios, flujos de datos, adquisiciones o regulación.

## Capítulo 02 — Inventario de PHI y ePHI

Las organizaciones deben mantener un inventario de información de salud protegida (PHI) e información de salud protegida electrónica (ePHI) que identifique dónde la información se crea, recibe, mantiene, transmite, almacena, respalda, exporta o elimina.

Los registros deben identificar sistemas, aplicaciones, endpoints, bases de datos, servicios cloud, interfaces, medios removibles, procesos en papel cuando corresponda, propietarios, custodios, clasificaciones de datos, requisitos de retención y destinatarios externos. Los repositorios desconocidos y las exportaciones no administradas deben tratarse como brechas de control que requieren investigación.

## Capítulo 03 — Mapeo de flujos de datos y límites

Mapee cómo PHI y ePHI se desplazan entre miembros de la fuerza laboral, aplicaciones, instalaciones, servicios cloud, proveedores, asociados de negocios, pacientes, planes de salud, proveedores de atención y otros destinatarios autorizados. Incluya límites de confianza, puntos de autenticación, interfaces, APIs, transferencias de archivos, mensajería, acceso remoto y rutas de respaldo o archivo.

Los mapas de flujo de datos apoyan el análisis de riesgos, la revisión de mínimo necesario, el diseño de controles de acceso, la investigación de incidentes, la gobernanza de asociados de negocios y la evaluación de brechas. Los mapas deben estar versionados y vinculados a los sistemas y procesos que representan.

## Capítulo 04 — Gobernanza de privacidad y mínimo necesario

La gobernanza de privacidad debe definir quién puede usar o divulgar PHI, con qué propósito, bajo qué autoridad y con qué aprobación o verificación. Cuando aplique el estándar de mínimo necesario, los procesos deben limitar el acceso, uso, divulgación y solicitudes a la cantidad razonablemente necesaria para el propósito permitido.

El diseño de roles, aprobaciones de flujo de trabajo, informes, exportaciones, analítica, acceso de soporte y privilegios administrativos deben revisarse para detectar exposición innecesaria. Las excepciones deben identificar justificación, autoridad, alcance, propietario, duración y controles compensatorios.

## Capítulo 05 — Análisis de riesgos de la Regla de Seguridad

El análisis de riesgos debe ser preciso y exhaustivo para el entorno de ePHI de la organización. Debe identificar activos, flujos de datos, amenazas, vulnerabilidades, salvaguardas existentes, probabilidad, impacto potencial y riesgo resultante mediante un método repetible apropiado para el tamaño, complejidad, capacidades, infraestructura técnica y contexto de riesgo de la organización.

Un análisis de riesgos no está completo simplemente porque se llenó una lista de verificación o se ejecutó un escaneo de vulnerabilidades. La evidencia debe mostrar los sistemas y ePHI considerados, supuestos, métodos, hallazgos, limitaciones, revisores responsables y fecha del análisis.

## Capítulo 06 — Gestión y tratamiento de riesgos

La gestión de riesgos debe convertir los riesgos identificados en decisiones de tratamiento con responsables definidos. Para cada riesgo material, registre la salvaguarda o acción correctiva prevista, responsable, fecha objetivo, dependencias, controles interinos, riesgo residual, aprobación y evidencia de cierre.

Los elementos de alto riesgo no deben permanecer abiertos indefinidamente sin escalamiento o aceptación documentada por un propietario de riesgo autorizado. La remediación completada debe validarse y no cerrarse únicamente con una declaración de la administración.

## Capítulo 07 — Salvaguardas administrativas

Las salvaguardas administrativas deben traducir las responsabilidades de seguridad de HIPAA en gobernanza operativa. Los controles pertinentes incluyen responsabilidad de seguridad asignada, autorización y supervisión de la fuerza laboral, administración del acceso a la información, concientización y capacitación de seguridad, procedimientos de incidentes de seguridad, planificación de contingencia, evaluación y acuerdos con asociados de negocios cuando corresponda.

La implementación debe mostrar quién ejecuta cada control, con qué frecuencia, qué evidencia se conserva, qué excepciones existen y cómo se escalan las fallas.

## Capítulo 08 — Puerta de implementación fail-closed

Un paquete de implementación o auditoría de HIPAA debe fallar de forma cerrada cuando el alcance material no esté resuelto, falte análisis requerido de la ley vigente, se desconozcan límites de ePHI, persistan brechas significativas del análisis de riesgos, la evidencia no respalde las salvaguardas afirmadas o esté incompleta una revisión humana, legal o de cumplimiento requerida.

El QA automatizado del repositorio puede confirmar estructura, registros de estado de fuentes, enlaces y evidencia de publicación. No puede determinar estatus legal, eficacia de controles, cumplimiento ni obligaciones de notificación de brechas. Los cambios materiales reabren las puertas de revisión afectadas.