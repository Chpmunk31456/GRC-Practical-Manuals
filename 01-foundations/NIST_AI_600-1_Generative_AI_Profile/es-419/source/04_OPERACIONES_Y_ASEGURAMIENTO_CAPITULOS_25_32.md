# Manual 04 — Implementación del Perfil de IA Generativa NIST AI 600-1
## Fuente controlada en español latinoamericano — Capítulos 25–32

> Traducción asistida por máquina para revisión controlada. Este conjunto apoya la gestión continua de riesgos de IA generativa y no reproduce el texto de NIST. La aprobación semántica humana sigue siendo obligatoria antes de la publicación.

## Capítulo 25 — Controles de despliegue y liberación

El despliegue debería usar un registro controlado vinculado al artefacto probado, configuración, versión del modelo, estado de datos/recuperación, herramientas, guardrails y condiciones operativas aprobadas. Una desviación material entre el candidato probado y el sistema desplegado invalida la evidencia de liberación hasta ser evaluada.

Los registros deberían identificar aprobadores responsables, excepciones abiertas, umbrales de monitoreo, autoridad de reversión y fechas de revisión.

## Capítulo 26 — Monitoreo y umbrales operativos

El monitoreo debería vincularse con riesgos conocidos y umbrales de decisión, no con telemetría genérica. Las medidas relevantes pueden incluir tasas de salida dañina, respuestas sin respaldo, eventos de seguridad, señales de fuga de datos, quejas de usuarios, fallas de herramientas, indicadores de drift del modelo, latencia/disponibilidad, cambios de proveedores y volumen de excepciones.

Las violaciones de umbral deberían mapearse a acciones predefinidas: investigar, restringir, aumentar revisión humana, deshabilitar una función, revertir o detener el sistema.

## Capítulo 27 — Gestión de cambios y reevaluación

Los cambios en modelos, prompts, instrucciones del sistema, fuentes de recuperación, herramientas, permisos, tratamiento de datos, proveedores, guardrails, interfaces o uso de negocio pueden alterar el riesgo. Los registros de cambio deberían clasificar materialidad e identificar qué evidencia previa sigue siendo válida.

Los cambios materiales reabren las compuertas afectadas de riesgo, pruebas, seguridad, privacidad, accesibilidad, revisión humana y liberación. Los cambios de emergencia requieren revisión retrospectiva y completar evidencia dentro de un periodo definido.

## Capítulo 28 — Respuesta a incidentes y contención

La respuesta a incidentes de IA generativa debería integrarse con la gestión empresarial de incidentes conservando evidencia específica de IA. Los equipos deberían capturar prompts, salidas, identificadores de modelo/configuración, contexto de recuperación, llamadas de herramientas, identidades, marcas de tiempo, registros, registros afectados, avisos de proveedores y estado de controles cuando sea lícito y factible.

Las opciones de contención pueden incluir deshabilitar herramientas, reducir permisos, aislar fuentes de recuperación, revertir configuración, limitar usuarios, aumentar revisión humana o suspender el servicio.

## Capítulo 29 — Acción correctiva y validación de remediación

La acción correctiva debería abordar causas raíz y no solo suprimir la salida observada. Los registros deberían identificar hallazgo, causa, responsable, acción planificada, fecha objetivo, método de validación, evidencia, riesgo residual y decisión de cierre.

Una corrección no debe considerarse cerrada solo porque un caso de prueba ahora aprueba. La re-prueba debería evaluar variantes probables y riesgo de regresión.

## Capítulo 30 — Revisión periódica e informes de gestión

La revisión periódica debería evaluar si el caso de uso sigue siendo apropiado, los controles siguen siendo efectivos, los supuestos de riesgo siguen siendo válidos, la evidencia está vigente, proveedores o componentes cambiaron y los resultados operativos permanecen dentro de tolerancia.

Los informes de gestión deberían distinguir hechos, tendencias, supuestos, riesgos no resueltos, excepciones aceptadas y decisiones requeridas. Los problemas de alto riesgo deberían ser visibles para el responsable de riesgo y no quedar enterrados en informes técnicos.

## Capítulo 31 — Retiro, disposición de datos y salida

La planificación del retiro debería abordar endpoints de modelos, credenciales, prompts, índices de recuperación, almacenes vectoriales, registros, datos de usuarios, cachés, integraciones, acceso de proveedores, evidencia retenida y obligaciones contractuales.

La organización debería verificar devolución o eliminación de datos cuando corresponda, revocar accesos y secretos, deshabilitar integraciones, conservar registros requeridos, documentar obligaciones no resueltas y registrar la decisión de retiro.

## Capítulo 32 — Aseguramiento, limitaciones y límite final de liberación

El aseguramiento es acumulativo y específico del alcance. QA del repositorio, pruebas automatizadas, red teaming, documentación o una lista de verificación completa no garantizan que un sistema de IA generativa sea seguro, protegido, conforme, exacto, equitativo o apto para todos los contextos.

Antes de publicar este manual, el paquete controlado debe completar verificación de fuentes, revisión técnica/editorial, revisión semántica `es-419` y `pt-BR`, verificación de gráficos/accesibilidad, generación DOCX/PDF, QA a nivel de página, procedencia y checksums, revisión de repositorio/seguridad y Aprobación Humana Final de Liberación explícita.

Cualquier cambio material de contenido posterior a la aprobación humana reabre la compuerta de revisión afectada.
