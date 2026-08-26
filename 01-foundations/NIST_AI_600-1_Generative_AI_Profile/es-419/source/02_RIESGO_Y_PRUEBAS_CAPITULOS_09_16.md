# Manual 04 — Implementación del Perfil de IA Generativa NIST AI 600-1
## Fuente controlada en español latinoamericano — Capítulos 09–16

> Traducción asistida por máquina para revisión controlada. Este material operacionaliza la línea base de Manual 04 y no reproduce el texto de NIST. La aprobación semántica humana sigue siendo obligatoria antes de la publicación.

## Capítulo 09 — Confabulación y confiabilidad de resultados

El riesgo de confabulación se gestiona mediante evaluación específica del caso de uso, no con un único porcentaje de exactitud. Los equipos deberían identificar qué afirmaciones deben ser factuales, la tasa de error aceptable, las consecuencias de falsa confianza y los controles usados cuando el modelo carece de respaldo confiable.

Los controles útiles incluyen recuperación con respaldo, visualización de fuentes, generación restringida, comportamiento de abstención, validación humana, verificaciones determinísticas posteriores y restricciones a acciones autónomas de alta consecuencia. La evidencia debería incluir conjuntos de evaluación, umbrales de aceptación, fallas observadas, ejemplos representativos, decisiones de remediación y aprobación del riesgo residual.

## Capítulo 10 — Contenido dañino, abusivo y peligroso

Las organizaciones deberían definir categorías de contenido prohibido, restringido, dependiente del contexto o aceptable para el caso de uso. La política debe distinguir el tratamiento de entradas del usuario del tratamiento de salidas del modelo y abordar intentos adversariales de evadir salvaguardas.

Las pruebas deberían incluir uso esperado, uso indebido, condiciones límite, manipulación de prompts, variación multilingüe cuando corresponda y comportamiento de escalamiento. Un mecanismo de rechazo que pueda evadirse trivialmente no debe tratarse como control efectivo.

## Capítulo 11 — Privacidad de datos e información sensible

La revisión de privacidad debería rastrear datos a través de prompts, almacenes de recuperación, registros, entrenamiento o ajuste, API externas, plataformas de observabilidad, canales de soporte e historial de conversaciones retenido.

El conjunto mínimo de controles debería abordar minimización, limitación de propósito, acceso, retención, eliminación, redacción, manejo de secretos, registro, tratamiento por terceros y divulgación al usuario cuando corresponda. Las pruebas deberían buscar memorización, fuga de datos, sobreexposición por recuperación, contaminación entre usuarios y divulgación no autorizada por herramientas o conectores.

## Capítulo 12 — Sesgo perjudicial, homogeneización e impacto humano

La evaluación de sesgo debería vincularse con decisiones, recomendaciones, clasificaciones, contenido o experiencias producidas por el sistema. Los equipos deberían identificar poblaciones o grupos de interés que puedan experimentar tasas de falla o daños diferentes.

Los controles pueden incluir análisis de datos, pruebas de resultados, evaluación por subgrupos, escalamiento humano, flujos alternativos, monitoreo y restricciones en decisiones consecuenciales. Cuando la medición esté limitada por datos o tamaño de muestra, esa incertidumbre debe documentarse y no presentarse como evidencia de equidad.

## Capítulo 13 — Configuración humano-IA y supervisión

La supervisión humana debe diseñarse, no asumirse. La organización debería determinar qué se espera que detecte la persona, qué evidencia está disponible, si dispone de tiempo y autoridad suficientes para intervenir y cómo se reducirá el sesgo de automatización.

Para usos consecuenciales, defina decisiones que el sistema puede tomar o recomendar, decisiones reservadas a humanos, disparadores de escalamiento, autoridad de anulación, registro de revisión humana, requisitos de competencia y procedimientos alternativos cuando el sistema no esté disponible o sea poco confiable.

## Capítulo 14 — Integridad de la información y procedencia

Los controles de integridad deberían ayudar a distinguir información generada, recuperada, transformada y autoritativa. La procedencia debería preservarse cuando afecte materialmente confianza, revisión, atribución o uso posterior.

La evidencia puede incluir referencias de fuentes, metadatos, artefactos firmados, historial de transformaciones, identificadores de prompt/versión, registros de modelo y trazabilidad desde la salida hasta material de soporte. Las afirmaciones de procedencia deben ser limitadas: metadatos o etiquetas mejoran trazabilidad pero no prueban por sí mismos verdad o autenticidad.

## Capítulo 15 — Seguridad de la información y pruebas adversariales

Las pruebas de seguridad de IA generativa deberían cubrir toda la superficie de ataque: prompts, fuentes de recuperación, bases vectoriales, endpoints de modelo, plugins/herramientas, identidades, secretos, API, interfaces, registros, capas de orquestación e integraciones con proveedores.

Las pruebas deberían incluir prompt injection directo e indirecto, uso no autorizado de herramientas, elevación de privilegios, extracción de datos sensibles, contenido malicioso de recuperación, revelación del prompt del sistema, abuso de acciones externas y escenarios de denegación o degradación cuando corresponda. Los hallazgos deben vincularse con controles, responsables, remediación, evidencia de re-prueba y decisiones de riesgo residual.

## Capítulo 16 — Propiedad intelectual, cadena de valor e integración de componentes

La organización debería identificar componentes licenciados, propietarios, de terceros, open source y alojados externamente que influyen en el sistema. Deben documentarse cuando corresponda términos del proveedor, restricciones de uso, derechos sobre salidas, condiciones de tratamiento de datos y dependencias.

La revisión de cadena de valor debería incluir proveedores de modelos, alojamiento, conjuntos de datos, fuentes de recuperación, plugins, API, servicios de seguridad, monitoreo y subprocesadores. Un cuestionario de proveedor por sí solo no constituye evidencia suficiente para dependencias de alto riesgo. Cambios materiales de proveedor o componente deben activar reevaluación cuando puedan alterar capacidad, tratamiento de datos, exposición contractual, seguridad, disponibilidad o comportamiento de salida.
