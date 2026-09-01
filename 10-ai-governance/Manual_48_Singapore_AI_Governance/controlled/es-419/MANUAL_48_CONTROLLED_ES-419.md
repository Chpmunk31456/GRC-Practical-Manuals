# Manual 48 — Gobernanza de IA de Singapur: MGF, GenAI, AI Verify e IA Agéntica

**Estado:** DESARROLLO CONTROLADO  
**Idioma:** Español latinoamericano (`es-419`)  
**Línea base de fuentes:** 1 de septiembre de 2026

## Objetivo

Convertir el ecosistema práctico de gobernanza de IA de Singapur en un modelo operativo empresarial. El manual distingue claramente entre orientación de gobernanza, herramientas de aseguramiento/pruebas, ejemplos de implementación, trabajos de normalización propuestos y obligaciones jurídicas de otras jurisdicciones. La alineación con un marco no se presenta como certificación ni como cumplimiento jurídico automático.

## Módulo 1 — Ecosistema de gobernanza de IA de Singapur

Distinguir las funciones del Model AI Governance Framework, el marco para IA generativa, AI Verify y el Model AI Governance Framework for Agentic AI. Para cada fuente registrar versión/fecha, estado, propósito y limitaciones.

**Evidencia:** inventario de marcos, registro de fuentes/versiones, nota de aplicabilidad y declaración de no equivalencia.

## Módulo 2 — Gobernanza organizacional y responsabilidad

Establecer estructura de gobierno, responsable ejecutivo, propietario del sistema, propietarios de controles, inventario de IA, criterios de riesgo y autoridades de decisión.

**Evidencia:** carta de gobernanza, RACI, política de IA, inventario de sistemas, decisiones y excepciones.

## Módulo 3 — Participación humana significativa

La participación humana debe corresponder al impacto y permitir intervención real. Evaluar autoridad, competencia, información disponible, tiempo de intervención y riesgo de sesgo de automatización.

**Evidencia:** matriz de derechos de decisión, umbrales de aprobación, registros de anulación/rechazo y capacitación del revisor.

## Módulo 4 — Gestión operativa durante el ciclo de vida

Controlar datos, validación, robustez, monitoreo, cambios, incidentes y retiro. Definir criterios de aceptación, disparadores de revalidación y capacidad de recuperación.

**Evidencia:** plan de ciclo de vida, linaje/calidad de datos, informes de prueba, monitoreo, cambios e incidentes.

## Módulo 5 — Interacción y comunicación con partes interesadas

Comunicar el uso de IA, su función y sus limitaciones de forma comprensible. Mantener canales de retroalimentación cuando correspondan y evitar afirmaciones que excedan la evidencia.

## Módulo 6 — Gobernanza de IA generativa

Aplicar controles a datos, prompts, RAG, modelos/proveedores, seguridad, privacidad, procedencia de contenido, pruebas y monitoreo. Evaluar alucinación/confabulación, fuga de datos, contenido dañino, robustez y cambios del proveedor.

**Preguntas clave:**
- ¿Qué fuentes pueden entrar al sistema?
- ¿Cómo se restringen datos sensibles?
- ¿Qué conjunto de evaluación demuestra rendimiento aceptable?
- ¿Cómo se detectan cambios de modelo/proveedor?
- ¿Qué información de salida requiere transparencia o calificación?

## Módulo 7 — AI Verify y aseguramiento

AI Verify se utiliza como mecanismo de pruebas y aseguramiento. No debe interpretarse como prueba universal de seguridad, ausencia de sesgo, cumplimiento jurídico o certificación.

**Flujo:** definir afirmaciones → seleccionar comprobaciones/pruebas → registrar condiciones y limitaciones → ejecutar → analizar fallas → remediar → volver a probar después de cambios materiales.

## Módulo 8 — IA agéntica: evaluar y limitar riesgos

Registrar propósito, autonomía, herramientas/APIs, datos, acciones, comunicaciones externas, ejecución de código, transacciones, sistemas externos, interacciones multiagente y reversibilidad.

**Controles:** identidad separada, mínimo privilegio, allowlists/denylists, límites de transacción/volumen, segmentación y estado seguro ante incertidumbre.

## Módulo 9 — IA agéntica: responsabilidad humana

Definir puntos de control humanos significativos antes de acciones de alto impacto o irreversibles, por ejemplo: paso a producción, nueva herramienta privilegiada, pago, cambio de configuración crítica, eliminación irreversible o excepción de seguridad.

**Evidencia:** catálogo de puntos de aprobación, identidad del aprobador, contexto, hora, decisiones rechazadas y escalamiento.

## Módulo 10 — Controles técnicos y de proceso para agentes

- identidad autenticada del agente/servicio;
- mínimo privilegio y credenciales limitadas;
- herramientas/APIs autorizadas explícitamente;
- validación de entradas, salidas y acciones;
- protección de límites prompt/herramienta/datos;
- aislamiento o sandbox cuando corresponda;
- registro completo y procedencia de acciones;
- monitoreo de anomalías;
- límites de tasa/recursos;
- mecanismo de parada y contención;
- inventario de dependencias;
- control de terceros;
- cambios y revalidación.

## Módulo 11 — Sistemas multiagente

Documentar cadenas de delegación, permisos entre agentes, memoria compartida, identidad, conflictos y responsabilidad. Evitar propagación implícita de privilegios y conservar trazabilidad extremo a extremo.

## Módulo 12 — Terceros y cadena de suministro

Evaluar modelos, agentes, herramientas y proveedores externos. Contratar controles de seguridad/privacidad, cambios, incidentes, evidencia y salida. Revalidar cuando cambien capacidades, APIs, modelos o políticas del proveedor.

## Módulo 13 — Sesgo de automatización

Medir cuándo usuarios/revisores aceptan resultados sin juicio independiente. Analizar tasas de anulación/desacuerdo, diseñar comprobaciones independientes y capacitar a quienes deben supervisar.

## Módulo 14 — Evidencia y auditabilidad

Para cada control mantener:

**Concepto fuente → interpretación organizacional → objetivo de control → propietario → implementación → evidencia → método de prueba → resultado → hallazgo → remediación → riesgo residual.**

## Módulo 15 — Mapeo entre marcos sin equivalencia falsa

Relacionar controles con Manual 46, Ley de IA de la UE, ISO/IEC 42001 y NIST AI RMF solo cuando exista una relación defendible. Clasificarla como directa, parcial, de apoyo o contextual y registrar diferencias de alcance, actores, estatus jurídico y evidencia.

## Módulo 16 — Hoja de ruta empresarial

### Primeros 30 días
- propietario de gobernanza e inventario;
- clasificación de casos de uso;
- identificación de agentes de mayor riesgo;
- puntos humanos significativos;
- repositorio de evidencia.

### 60 días
- controles del ciclo de vida;
- revisiones de acceso y terceros;
- programa de pruebas/aseguramiento;
- respuesta a incidentes/contención;
- capacitación.

### 90 días
- pruebas independientes según riesgo;
- revisión de permisos de agentes;
- análisis de sesgo de automatización;
- cierre de hallazgos;
- tablero de gobernanza.

## Escenarios prácticos

1. asistente GenAI de atención al cliente con datos confidenciales;
2. agente financiero con autoridad de pagos;
3. agente de selección de personal y sesgo de automatización;
4. agente de programación de terceros con acceso a repositorios/CI/CD;
5. operación de viajes multiagente;
6. chatbot público de asesoría sin autoridad decisoria;
7. ejercicio de afirmaciones de AI Verify;
8. ampliación de capacidades después de una actualización de proveedor;
9. revisión ejecutiva de hallazgos de agentes;
10. desafío de mapeo entre marcos.

## Dominios mínimos de control

- gobernanza y responsabilidad;
- inventario y riesgo;
- participación humana;
- ciclo de vida;
- datos/RAG;
- pruebas y aseguramiento;
- identidad de agentes;
- autorización/mínimo privilegio;
- límites de herramientas/APIs;
- procedencia de acciones;
- multiagente;
- terceros;
- monitoreo;
- contención/incidentes;
- cambios/revalidación;
- transparencia al usuario;
- no equivalencia entre marcos.

## Criterio de finalización

La persona que complete el Manual 48 debe poder tomar un concepto de gobernanza de Singapur y convertirlo en un control empresarial defendible, con propietario, evidencia, método de prueba, tratamiento de fallas y nota de limitación, sin afirmar certificación o equivalencia jurídica no sustentada.