# Capítulo 43 — Precisión, solidez, ciberseguridad y resiliencia

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador anterior del Capítulo 43.

## Requisito

Los sistemas de IA de alto riesgo deben alcanzar un nivel adecuado de precisión, robustez y seguridad cibernética y funcionar de manera consistente a lo largo de su ciclo de vida. El diseño debe abordar errores, fallas, inconsistencias, interferencias maliciosas, bucles de retroalimentación y mal uso razonablemente previsible a la luz del propósito y riesgo previstos.

## Explicación en lenguaje sencillo

El cumplimiento no requiere un rendimiento perfecto. Requiere objetivos de rendimiento defendibles, pruebas basadas en riesgos, limitaciones transparentes, diseño seguro, monitoreo y acción correctiva. Las métricas deben reflejar el contexto real de implementación en lugar de solo promedios de laboratorio.

## Zonas de control necesarias

El proveedor debe dirigirse, según proceda:

1. la precisión definida y las métricas de rendimiento vinculadas a la finalidad prevista;
2. los umbrales de aceptación y los límites de decisión;
3. resultados de subgrupos y contextos específicos;
4. robustez al ruido, falta de datos, desplazamiento de distribución y fallo de componentes;
5. resistencia a errores, fallas, interrupciones del servicio y fallos de dependencia;
6. protección contra envenenamiento de datos, ejemplos contradictorios, inyección rápida, manipulación de modelos, extracción y acceso no autorizado;
7. garantizar el desarrollo, las pruebas, la gestión de la vulnerabilidad y el control del cambio;
8. riesgos de bucle de retroalimentación para los sistemas que siguen aprendiendo o influyen en los datos futuros;
9. Retroceso, degradación, retroceso y comportamiento seguro;
10. seguimiento, respuesta a incidentes y desencadenantes de medidas correctivas.

## Métricas y divulgación

Las métricas de precisión y robustez deben documentarse en el archivo técnico e instrucciones de uso cuando sea necesario. Las puntuaciones agregadas no deben ocultar los modos de fallo material, las disparidades entre grupos afectados, las condiciones de funcionamiento inseguras o la incertidumbre.

## Ejemplo de GlobalWay

GlobalWay valida su sistema de contratación utilizando conjuntos de datos relevantes para las funciones y mide patrones falsos positivos y falsos negativos en los grupos de solicitantes pertinentes. También prueba la falta de información, formatos de currículum inusuales, contenido rápido malicioso, interrupciones del proveedor, cambios de modelos y procedimientos de reversión.

## Actividad de control

El proveedor debe aprobar requisitos medibles de rendimiento, robustez y ciberseguridad antes de lanzar y repetir pruebas después de cambios materiales o amenazas emergentes.El implementador debe monitorear el rendimiento en el mundo real, mantener las condiciones de operación requeridas, reportar anomalías graves y suspender el uso cuando se infrinjan umbrales definidos.

## Pruebas

- requisitos de rendimiento y umbrales;
- la validación y los planes de ensayo;
- resultados de subgrupos y casos extremos;
- la robustez y los resultados de las pruebas de resistencia;
- modelo de amenaza y arquitectura de seguridad;
- registros de vulnerabilidad y pruebas de penetración;
- pruebas de dependencia y resiliencia;
- los tableros de control;
- registros de incidentes y medidas correctivas;
- homologaciones de liberación y reversión.

## Prueba de auditoría

Seleccione un sistema de alto riesgo y verifique que se documentan los requisitos de rendimiento y seguridad, las pruebas reflejan el contexto de despliegue previsto, se revelan los modos de fallo de materiales, se rastrean las vulnerabilidades y anomalías y se investigan, corrigen, restringen o suspenden los umbrales.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, en su versión modificada: artículo 15 y obligaciones relacionadas con el ciclo de vida, el seguimiento y el proveedor/desplegador.
- Los actuales controles consolidados de texto EUR-Lex sobre los resúmenes antiguos.
