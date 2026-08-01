# Manual práctico de recopilación y auditoría de pruebas

**Estado de traducción:** candidato de publicación asistido por máquina; no se presenta como revisión lingüística nativa.

**Author:** Alberto “Al” Leiva
**Edition:** English v1.0
** Fecha de construcción controlada:** 2026-08-01

ChatGPT ayudó bajo la dirección del autor. El autor sigue siendo responsable de las decisiones editoriales y de liberación.

> **Notificación educativa** Este manual proporciona orientación profesional general. No constituye asesoramiento jurídico, reglamentario, contable, de certificación ni de auditoría formal. Adaptarlo a los criterios, contratos, sistemas, datos, riesgos y obligaciones de retención aplicables.

---

# 1. Governance and Principles

## 1.1 Propósito

La prueba apoya las decisiones sobre si un requisito, control, proceso o compromiso está diseñado adecuadamente, aplicado, operando según lo previsto y produciendo el resultado esperado. La evidencia no se recoge simplemente para llenar una carpeta o satisfacer una lista de verificación. Debe apoyar una conclusión definida contra los criterios identificados.

## 1.2 Gobernanza de pruebas

La organización debería definir:

- quién puede solicitar pruebas;
- que posee cada elemento de prueba;
- quién puede aprobar la divulgación;
- cuando se puedan almacenar pruebas;
- cómo se clasifica y protege el material sensible;
- cómo se preserva la autenticidad y la integridad;
- cuánto tiempo se mantiene la evidencia;
- cómo se intensifican las excepciones y las controversias; y
- que aprueba las respuestas finales de auditoría.

El jefe de auditoría o evaluación sigue siendo responsable de la estrategia de pruebas. Los propietarios de control siguen siendo responsables de suministrar registros precisos y completos. Los custodios de pruebas protegen los sistemas y registros de fuentes. Legal, privacy, human-resources, security, and records-management specialists should be involved when evidence creates confidentiality, privilege, labour, cross-border, or retention concerns.

## 1.3 Características básicas de las pruebas

La evidencia útil es:

- **Relevant** — se ocupa directamente del objetivo de criterio y evaluación;
- ** fiable** - se origina de una fuente confiable y puede ser corroborada;
- **suficiente** - existen suficientes pruebas para apoyar la conclusión y el período de muestreo;
- **apropiado**: la naturaleza y la calidad de las pruebas se ajustan al riesgo y al objetivo;
- **auténtico** - la evidencia es lo que afirma ser;
- **completo** — contexto necesario, alcance, fechas, poblaciones y limitaciones están presentes;
- **actual**: las pruebas reflejan el período o punto pertinente en el tiempo;
- **Traceable** - el revisor puede identificar la solicitud, fuente, propietario, criterio, revisión y conclusión;
- **Protegida**: se mantienen la confidencialidad, la integridad, la disponibilidad, la privacidad y las restricciones legales; y
- **reproducible** — un revisor calificado puede entender cómo se produjo la evidencia y llegar a una conclusión favorable.

## 1.4 jerarquía de pruebas

Ninguna jerarquía universal se aplica a cada auditoría, pero la evidencia generada directamente de sistemas autorizados es generalmente más fuerte que la autoatestización sola. Un orden práctico de preferencia es:

1. registros generados o corroborados externamente;
2. exportaciones generadas por el sistema con parámetros fuente, horario, alcance y consulta;
3. registros aprobados creados durante operaciones normales;
4. observación directa o reperformance documentado por el evaluador;
5. entrevistas corroboradas por registros o observaciones;
6. representación de la gestión o autoatestización.

La evidencia de menor rango no es automáticamente inválida. Requiere una mayor corroboración y limitaciones más claras.

## 1.5 Sentencia profesional

La evaluación de pruebas requiere juicio profesional. El examinador debería considerar el riesgo, la materialidad, el tamaño de la población, la frecuencia de control, la automatización, el cambio, las conclusiones anteriores, el riesgo de fraude, el riesgo de seguridad de la información y las consecuencias de una conclusión incorrecta. El documento de trabajo debe registrar juicios significativos en lugar de dejarlos implícitos.

## 1.6 Prácticas prohibidas

No:

- crear o alterar las pruebas después del hecho sin revelarlas;
- eliminar los registros desfavorables de una población;
- represent screenshots as complete system evidence when underlying data is unavailable;
- compartir credenciales o acceso a la producción sin restricciones con los auditores;
- colocar evidencia regulada, privilegiada o altamente sensible en repositorios no aprobados;
- overwrite original evidence files;
- basarse en declaraciones verbales como único apoyo a conclusiones de alto riesgo; o
- etiqueta automatizada como aprobación legal, reguladora, certificación o auditoría humana.

---

# 2. Planificación, solicitudes y responsabilidades

## 2.1 Comience con el objetivo de evaluación

Antes de solicitar pruebas, defina:

- el objetivo de auditoría, evaluación, examen o certificación;
- los criterios y la versión autorizados;
- el ámbito organizativo, técnico, geográfico y temporal;
- los sistemas, procesos, entidades y poblaciones de alcance;
- el control o el requisito de ser probado;
- el tipo de prueba esperado;
- el método de evaluación: examinar, entrevistar, probar, observar, inspeccionar o repercutir;
- el solicitante responsable, propietario, revisor y aprobador; y
- la fecha de terminación requerida.

Una solicitud sin un criterio o objetivo definido crea carga innecesaria y debilita la trazabilidad.

## 2.2 Estructura de la solicitud de pruebas

Cada solicitud debe incluir:

- solicitud única ID;
- auditoría o identificación de compromiso;
- criterio o referencia de control;
- descripción de las solicitudes de idiomas;
- la razón por la que se necesita la evidencia;
- período requerido y población;
- formatos aceptables;
- metadatos o contexto requeridos;
- canal de comunicación seguro;
- propietario asignado y propietario de respaldo;
- d) Fecha y prioridad debidas;
- c) Clasificación de la confidencialidad;
- criterios de aceptación de los examinadores; y
- dependencias o solicitudes previas.

Evite combinar pruebas no relacionadas con una sola solicitud. Dividir grandes solicitudes en artículos manejables con criterios de aceptación claros.

## 2.3 Funciones

### Patrocinador de auditoría

Aprueba el alcance, resuelve controversias importantes y apoya la cooperación oportuna.

### Jefe de auditoría o evaluación

Posee la estrategia de pruebas, lista de solicitudes, enfoque de muestreo, asignaciones de revisores, calidad de conclusión y escalada.

### Coordinador de pruebas

Mantiene el rastreador de solicitudes, las preguntas de rutas, monitorea las fechas debidas y evita duplicaciones o solicitudes conflictivas.

### Propietario de control o proceso

Explica el proceso, valida el alcance y asegura que las pruebas reflejen con precisión las operaciones normales.

### Custodio de pruebas

Extracts or supplies records from the authoritative source while preservation integrity and metadata.

### Revisor o probador

Evalua la pertinencia, fiabilidad, suficiencia, idoneidad, excepciones y limitaciones y registra la conclusión.

### Especialistas en asuntos jurídicos, privacidad, seguridad, recursos humanos y registros

Asesoramiento sobre privilegios, datos personales, investigaciones delicadas, información de los empleados, restricciones a la exportación, límites contractuales, litigios y retención segura.

## 2.4 Solicitar ciclo de vida

Use los siguientes estados:

1. Proyecto
2. Aprobado para cuestiones
3. Publicada
4. Recibido
5. En curso
6. Presentado
7. En examen
8. Aclaración requerida
9. Aceptado
10. Rechazado o sustituido
11. Cerrado
12. Retenidos o eliminados

Los cambios en la situación deben ser datados y atribuibles. Las solicitudes reabridas deben preservar las presentaciones anteriores y el historial de examen.

## 2.5 Fechas y escalada debidas

Establecer las fechas debidas basadas en la complejidad, el riesgo, la disponibilidad y el calendario de compromiso. La escalada debe ser proporcional:

- recordatorio al propietario;
- coordinación con el propietario del respaldo;
- notificación al administrador del proceso;
- :: La intensificación de la participación en la dirección;
- a) La intensificación del patrocinio o el órgano de gobernanza; y
- limitación formal de alcance cuando no se pueden obtener pruebas.

Las pruebas tardías no deben tratarse en silencio como satisfactorias. Recordar el retraso, el impacto, la mitigación y la conclusión revisada.

## 2.6 Solicitudes duplicadas y excesivas

El coordinador de pruebas debe comparar las solicitudes de auditoría interna, auditoría externa, cumplimiento, seguridad del cliente, privacidad y actividades de certificación. Reutilizar la evidencia sólo cuando el período, alcance, criterio, integridad, confidencialidad y frescura siguen siendo apropiados. La reutilización debe ser documentada; no debe ocultar cambios ni nuevas excepciones.

---

# 3. Colección, integridad y protección

## 3.1 Recopilación de fuentes autorizadas

Identificar el sistema de registro, propietario de registros, método de extracción, fecha y hora, parámetros de consulta o filtro, tamaño de la población y persona que realiza la extracción. Preserve archivos de fuente cruda cuando sea práctico y crear copias de trabajo para su revisión.

## 3.2 Exportaciones de sistemas

Un sistema de exportación debe incluir suficiente contexto para interpretar los datos:

- sistema y nombre del medio ambiente;
- informe o nombre de consulta;
- tiempo de extracción y zona horaria;
- período de presentación de informes;
- filtros y exclusiones;
- definición de campo cuando no está claro;
- población total y renglón;
- cuenta de usuario o servicio que produjo la exportación; y
- limitaciones conocidas.

Cuando una exportación se transforma manualmente, conserva el original, registra cada transformación, y reconcilia los totales antes y después del procesamiento.

## 3.3 Captura de Pantalla

Capturas de pantalla son útiles para la configuración puntual, flujo de trabajo y evidencia de interfaz, pero son fácilmente incompletos. Captura:

- aplicación y medio ambiente;
- fecha del sistema visible o un horario de captura documentado
- URL, objeto, arrendatario, cuenta o identificador de registro pertinente sin exponer secretos innecesarios;
- el entorno completo y el contexto circundante;
- paginación, filtros y alcance; y
- el operador y el método de captura.

No recortar el contexto que afecta la interpretación. La Redacción debe utilizar un método aprobado y no debe alterar las pruebas sustantivas.

## 3.4 Documentos y actas

Confirme el estado de aprobación, propietario, versión, fecha efectiva, fecha de revisión, historial de cambios y aplicabilidad. Una política demuestra la intención documentada; no prueba por sí misma la aplicación o la operación.

## 3.5 Entrevistas y observaciones

Funciones de los participantes en el documento, fecha, preguntas, declaraciones clave, actividades observadas, limitaciones y registros corroborativos. Proporcionar al entrevistado la oportunidad de corregir los malentendidos fácticos cuando proceda. Las entrevistas no deben presentarse como prueba independiente cuando deben existir pruebas operacionales más sólidas.

## 3.6 Reperformance and testing

Grabar el procedimiento, insumos, herramientas, probador, fecha, medio ambiente, resultado esperado, resultado real, excepciones y salida retenida. Los exámenes deben ser autorizados y diseñados para evitar daños operacionales, violaciones de privacidad o acceso no autorizado.

## 3.7 Autenticidad e integridad

Use controles proporcionales tales como:

- sólo recuperación de lectura;
- - Repositorios de pruebas restringidos;
- fichero hashes;
- firmas digitales o timetamps de confianza;
- almacenamiento inmutable o versionado;
- acceso y descarga de registros;
- - La reconciliación de los sistemas fuente;
- confirmación independiente; y
- cadena de custodia documentada.

Un hash ayuda a detectar cambios de archivo después de la piratería; no prueba que el contenido original fue exacto o completo.

## 3.8 Cadena de custodia

Para material de alto riesgo, investigación, legal o forense, registre cada transferencia, manejador, tiempo, ubicación, propósito, acción y control de integridad. Utilice almacenamiento sellado o controlado por el acceso y preservar los originales. Escale inmediatamente si la custodia o la integridad es incierta.

## 3.9 Confidencialidad y minimización

Recoger las pruebas mínimas necesarias. Redactar o tokenizar datos personales, secretos, credenciales, claves privadas, información de salud, datos de pago, asesoramiento jurídico e información de empleados no relacionada cuando el objetivo de evaluación no requiere divulgación. Nunca email credenciales no limitadas o coloque evidencia sensible en almacenamiento personal.

## 3.10 Pruebas transfronterizas y de terceros

Confirme los derechos contractuales, residencia de datos, restricciones de transferencia, obligaciones de confidencialidad, requisitos de regulador y consentimiento de terceros antes de la recogida o divulgación. Registrar cualquier limitación que impida el acceso directo y la garantía alternativa obtenida.

---

# 4. Revisión, muestreo y conclusiones

## 4.1 Secuencia de revisión

Para cada presentación, el examinador debe determinar:

1. ¿Responde a la solicitud y el criterio?
2. ¿Es la fuente autorizada e identificable?
3. ¿Cubre la entidad correcta, sistema, período, población y frecuencia de control?
4. ¿La evidencia es completa, auténtica, protegida e internamente consistente?
5. ¿Se puede corroborar o reproducir el resultado?
6. ¿Se registran excepciones, lagunas, hipótesis y limitaciones?
7. ¿Se requieren pruebas adicionales antes de llegar a una conclusión?

## 4.2 Efectos del examen de la prueba

Use resultados controlados como:

- aceptado;
- aceptada con limitación;
- aclaración necesaria;
- pruebas adicionales necesarias;
- sustitución necesaria;
- no aplicable con la justificación aprobada;
- rechazado; y
- limitación de alcance.

El examinador debe registrar la base para el resultado, no sólo la situación.

## 4.3 Población y muestreo

Define la población antes de seleccionar muestras. Documento:

- fuente de población y propietario;
- período comprendido;
- población;
- - Normas de inclusión y exclusión;
- estratificación o factores de riesgo;
- método de muestreo;
- tamaño de la muestra y racionalidad;
- procedimiento de semilla o selección al azar cuando sea aplicable;
- sustituciones y razones; y
- limitaciones que afectan la representatividad.

El muestreo puede ser estadístico o crítico. No implica confianza estadística cuando se utilizó una muestra de juicio.

## 4.4 Consideraciones de diseño de muestra

Aumentar la cobertura cuando el riesgo, la materialidad, la frecuencia de control, el volumen de transacción, el cambio, la falla de automatización, los hallazgos previos, la exposición al fraude o la variabilidad de la población es alta. Considerar la selección:

- artículos de alto valor o alto riesgo;
- transacciones inusuales o fallidas;
- nuevos sistemas o procesos;
- diferentes lugares, unidades de negocios, administradores y períodos de tiempo;
- ítems antes y después de los cambios importantes; y
- artículos ordinarios seleccionados al azar.

## 4.5 Excepciones

Una excepción es una diferencia entre el criterio y la condición observada. Grabación:

- muestra o identificador de población;
- criterio;
- condición esperada;
- condición observada;
- b) Referencia de pruebas;
- causa, cuando se sabe;
- consecuencia o riesgo;
- si la excepción es aislada o sistémica;
- - Controles compensatorios;
- respuesta del propietario; y
- requiere seguimiento.

No eliminar una excepción del registro simplemente porque se corrige durante la auditoría. Grabar la condición original y la remediación verificada por separado.

## Corroboración

Corroborate evidencia débil o de alto riesgo utilizando otra fuente, método, período de tiempo o parte independiente. Entre los ejemplos figuran la comparación de los requisitos de política con la configuración del sistema, la conciliación de las exportaciones con los totales de las fuentes, la observación de un proceso descrito en una entrevista o el rastreo de una muestra mediante la iniciación, aprobación, ejecución y vigilancia.

## 4.7 Conclusiones

Las conclusiones deben indicar:

- el criterio y el objetivo;
- y período;
- procedimientos realizados;
- - Examen de las pruebas;
- muestra y limitaciones de población;
- excepciones y su importancia;
- - Controles compensatorios;
- desacuerdos no resueltos;
- la conclusión del revisor; y
- acción requerida o escalada.

Evite afirmaciones absolutas, como “totalmente compatibles” o “seguras” cuando los procedimientos y pruebas apoyen sólo una conclusión más estrecha.

## 4.8 Examen y control de calidad

Las conclusiones importantes deben recibir un examen de supervisión. El revisor debe confirmar que los documentos de trabajo son comprensibles sin explicación oral, las referencias resuelven las pruebas retenidas, los cálculos son correctos, las excepciones son rastreables y la conclusión sigue de las pruebas.

---

# 5. Coordinación y Remediación del Auditor

## 5.1 Canal único de coordinación

Utilice un coordinador de pruebas o portal controlado para tramitar solicitudes, presentaciones, preguntas y actualizaciones de estado. Esto reduce las solicitudes duplicadas, las respuestas inconsistentes, la divulgación incontrolada y la pérdida del historial de auditoría.

## 5.2 Ajuste de apertura

Al comienzo del compromiso, confirme:

- alcance y criterios;
- período de auditoría y hitos;
- proceso de solicitud y escalada;
- método de intercambio de pruebas seguro;
- tiempos de respuesta esperados;
- formatos de prueba permitidos;
- muestreo y expectativas de progreso;
- normas para material privilegiado, regulado, personal o restringido;
- reunión de cadencia; y
- proceso de observaciones preliminares y correcciones fácticas.

## 5.3 Aclaraciones

Cuando una solicitud es ambigua, pida al solicitante que aclare el criterio, el período, la población, el sistema y las pruebas esperadas. No adivine y proporcione datos excesivos. Record agreed interpretations in the request log.

## 5.4 Acceso de los auditores

Preferir demostraciones supervisadas, cuentas solo lectura, acceso limitado a tiempo, datos enmascarados, exportaciones controladas o salas de datos virtuales seguras. Aplicar menos privilegios y supervisar el acceso. Nunca proporcionar credenciales de administrador compartidas, credenciales personales, claves privadas o acceso de producción sin restricciones.

## 5.5 Observaciones preliminares

Una observación preliminar debe identificar el criterio, condición, evidencia, riesgo y alcance afectado. La administración debe distinguir las correcciones fácticas del desacuerdo con el juicio del auditor. Las correcciones deben ser respaldadas por pruebas y no deben reescribir la historia.

## Respuestas de la administración

Una respuesta completa incluye:

- acuerdo, acuerdo parcial o desacuerdo;
- contextual;
- causa raíz;
- evaluación del riesgo;
- contención inmediata;
- la acción correctiva;
- propietario responsable;
- fecha prevista;
- recursos y dependencias;
- Controles provisionales;
- método de validación; y
- pruebas que demostrarán el cierre.

Evite respuestas que simplemente prometen “revisión”, “considerar”, o “recordar personal. ”

## 5.7 Seguimiento de la acción correctiva

Seguimiento de cada hallazgo a través de:

1. observación registrada;
2. validación fáctica;
3. calificación de riesgo acordada o disputada formalmente;
4. Plan de acción aprobado;
5. la aplicación en curso;
6. pruebas de gestión presentadas;
7. validación independiente realizada;
8. cierre aprobado; o
9. riesgo formalmente aceptado o escalado.

Las fechas revisadas y los cambios de alcance deben preservar el historial original de compromiso y aprobación.

## 5.8 Pruebas de clausura

El cierre requiere pruebas de que la acción acordada se implementó y está funcionando eficazmente. Dependiendo de la conclusión, esto puede requerir documentación actualizada, pruebas de configuración, poblaciones terminadas, resultados de pruebas, registros de capacitación, informes de monitoreo o un período de operación sostenida.

Una tarea completa no significa automáticamente que el riesgo subyacente se reduce.

## 5.9 Disacuerdos y limitaciones de alcance

Document unresolved disagreements, unavailable evidence, access restrictions, management refusals, and timing constraints. Escale a los patrocinadores del compromiso o a los órganos de gobernanza. El informe final debe explicar cómo la limitación afecta los procedimientos y la confianza en la conclusión.

---

# 6. Retención, cierre y mejora continua

## 6.1 Repositorio de pruebas

Utilice un repositorio aprobado con acceso basado en roles, cifrado, historial de versiones, respaldo, registro y controles de retención. Organizar evidencia por compromiso, criterio, solicitud de identificación y versión de presentación. No dependa de buzones personales, descargas locales, archivos adjuntos o enlaces temporales como el registro oficial.

## 6.2 Nombre de archivo e índice

Una convención práctica de nominación incluye:

`Engagement_RequestID_Criterion_Period_Source_Version`

El índice debe mapear cada archivo a:

- Solicitud de identificación;
- criterio;
- Propietario;
- sistema fuente;
- período;
- Fecha de presentación;
- clasificación;
- revisor;
- resultados del examen;
- encontrar o hacer referencia al documento de trabajo; y
- fecha de retención o eliminación.

## 6.3 Calendario de retención

Aplicar el calendario de registros de la organización, obligaciones contractuales, requisitos de regulador, litigios, necesidades de investigación y metodología de auditoría. Retener pruebas ya no justificadas, pero no destruir registros sujetos a una retención legal, investigación abierta, solicitud de preservación regulatoria, hallazgo no resuelto o recurso activo.

El registro de compromisos debe determinar la autoridad de control de la norma de retención y eliminación.

## 6.4 Eliminación segura

Cuando la retención autorizada expira:

- confirmar que no se aplica ninguna retención o dependencia no resuelta;
- obtener la aprobación necesaria;
- eliminar copias de trabajo y conjuntos de datos exportados;
- utilizar un método de destrucción aprobado;
- preservar un registro de eliminación; y
- verificar la supresión de los sitios de colaboración y los lugares de transferencia temporal cuando sea posible.

## 6.5 Cierre de participación

Antes de cerrar, confirme:

- todas las solicitudes tienen un estatuto definitivo;
- Las pruebas aceptadas son indizadas y accesibles;
- Las comunicaciones rechazadas y sustituidas siguen siendo rastreables cuando sea necesario;
- - Los documentos de trabajo se refieren a las versiones correctas de pruebas;
- se ultiman las conclusiones y las respuestas de la administración;
- se denuncian limitaciones no resueltas;
- las acciones correctivas se transfieren al rastreador oficial;
- se eliminan o reducen los derechos de acceso;
- expiran los vínculos temporales compartidos;
- se asignan fechas de retención y eliminación; y
- se registran las lecciones aprendidas.

## 6.6 métricas

Las medidas útiles incluyen:

- solicitudes emitidas, aceptadas, rechazadas, atrasadas y reabiertadas;
- tiempo medio para reconocer, presentar, revisar y cerrar;
- tasa de aceptación del primer paso;
- Tasa de duplicación de solicitudes;
- Número de incidentes de confidencialidad o acceso;
- Porcentaje de pruebas de sistemas autorizados;
- Porcentaje de conclusiones con planes de acción completos;
- medidas correctivas indebidas;
- y la repetición de conclusiones anteriores; y
- correcciones de control de calidad del revisor.

Las métricas deben mejorar el proceso, no recompensar la aceptación prematura o desalentar el desafío legítimo.

## 6.7 Experiencia adquirida

Después de cada compromiso principal, documento:

- solicitudes poco claras o excesivas;
- fallos recurrentes de calidad de la evidencia;
- limitaciones del sistema;
- trabajo manual innecesario;
- problemas de acceso o confidencialidad;
- confusión repetida de control-propietario;
- oportunidades de reutilizar informes o pruebas automatizadas; y
- cambios necesarios en políticas, capacitación, sistemas o plantillas.

## 6.8 Composición de pruebas continua

Las organizaciones deben integrar la generación de pruebas en operaciones normales. Los propietarios de control deben saber qué registros demuestran el rendimiento, dónde se retienen, y cómo se revisan. La recopilación automática de pruebas puede reducir el esfuerzo, pero debe preservar el contexto, el control de acceso, la integridad, la trazabilidad de las fuentes y la rendición de cuentas humana.

## 6.9 Principio final de funcionamiento

El objetivo no es producir el mayor paquete de pruebas. El objetivo es producir un cuerpo controlado, proporcional y trazable de pruebas que apoye una conclusión honesta y permita la acción responsable.

---

# Apéndice A - Plantillas operacionales

El paquete de publicación incluye las siguientes herramientas editables de CSV:

- **Audit_Request_and_Response_Log.csv** — 21 campos.
- **Corrective_Action_Tracker.csv** — 32 campos.
- **Evidence_Quality_Review_Checklist.csv** — 36 campos.
- **Evidence_Request_Tracker.csv** — 38 campos.

# Autoritative Source Register

Verificado 1 de agosto de 2026.

## Fuentes primarias

1. **NIST SP 800-53A Rev. 5 — Evaluar los controles de seguridad y privacidad en los sistemas y organizaciones de información** Enero 2022, con la versión 5.2.0 actualizaciones de procesamiento de la evaluación emitida 27 de agosto de 2025. Proporciona procedimientos de evaluación personalizables, orientación de planes de evaluación y métodos para analizar los resultados de la evaluación.
2. **NIST SP 800-53 Rev. 5 - Controles de seguridad y privacidad para sistemas y organizaciones de información** Septiembre 2020, con el lanzamiento 5.2.0 actualizaciones publicadas 27 agosto 2025. Proporciona los objetivos de control y el contexto de garantía contra los cuales se pueden evaluar pruebas.
3. **ISO 19011:2026 — Directrices para los sistemas de gestión de auditoría.** Edición 4, publicada en mayo de 2026. Supera la edición retirada ISO 19011:2018 y aborda los principios de auditoría, gestión de programas de auditoría, auditorías y competencia de auditor.
4. **U.S. GAO, Standards for Internal Control in the Federal Government (2025 Green Book), GAO-25-107721.** Publicado 15 Mayo 2025 y comienzo efectivo año fiscal 2026. Pone de relieve la documentación de evaluación de riesgos, diseño de control, ejecución, operación y respuestas a cambios significativos.
5. **El Instituto de Auditores Internos, Global Internal Audit Standards.** Edición 9 de enero de 2024 y efectiva 9 de enero de 2025. Establece requisitos basados en principios y ejemplos de pruebas de conformidad con la práctica profesional de auditoría interna.

## Reglas de control de fuentes

- Verifique las versiones actuales antes de cada versión importante.
- Distinguir criterios obligatorios de orientación y ejemplos.
- No reproduzca los estándares copyrighted más allá de los resúmenes y citas permitidos.
- Grabar el criterio, versión, fecha de publicación y fecha de acceso en los documentos de trabajo de auditoría.
- Cuando los criterios de conflicto, se intensifican al patrocinador de auditoría, abogado, propietario del cumplimiento o especialista calificado en lugar de seleccionar silenciosamente uno.
