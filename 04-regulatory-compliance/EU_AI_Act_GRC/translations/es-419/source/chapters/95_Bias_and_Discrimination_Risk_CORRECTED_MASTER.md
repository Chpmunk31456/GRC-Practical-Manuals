# Capítulo 95 — Riesgos de sesgo y discriminación

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador del Capítulo 95 anterior en conflicto.

## Requisito

Las organizaciones deben identificar y mitigar los riesgos de que un sistema de IA pueda producir discriminación ilícita, desventajas injustificadas, exclusión, resultados inaccesibles o resultados sistemáticamente peores para los grupos protegidos o vulnerables. La evaluación debe reflejar el contexto jurídico y fáctico aplicable en lugar de basarse en una única métrica estadística.

## Explicación en lenguaje sencillo

La Bias puede surgir de datos, etiquetas, muestreo, proxies, objetivos, comportamiento del modelo, umbrales, prácticas de usuario, barreras de accesibilidad, bucles de retroalimentación, o el proceso de decisión circundante. La igual exactitud agregada no prueba la igualdad de trato, mientras que una disparidad numérica no determina por sí misma la ilegalidad legal.

## Necesidades de evaluación

Evaluar como mínimo:

1. grupos protegidos y vulnerables pertinentes para la jurisdicción y el caso de uso;
2. representación, medición, etiquetado y riesgos de prejuicios históricos;
3. variables proxy y características correlacionadas;
4. rendimiento de subgrupos, tasas de error, calibración y efectos interseccionales;
5. la accesibilidad y los requisitos de alojamiento razonable;
6. las consecuencias sobre el umbral, la clasificación y el flujo de trabajo;
7. sesgo de calidad y automatización de la revisión humana;
8. mecanismos de denuncia, impugnación, explicación y reparación;
9. bucles de retroalimentación y deriva después del despliegue;
10. revisión legal de las métricas, mitigaciones y disparidades residuales propuestas.

## Ejemplo de GlobalWay

GlobalWay prueba un sistema de clasificación de reclutamiento en grupos relevantes de solicitantes y familias de empleos. Revisa las tasas de falsos negativos, variables indirectas, barreras de acceso a la discapacidad, umbrales de clasificación, patrones de anulación humana y si hay alojamientos disponibles. Un resultado estadísticamente mejorado no es aceptado hasta que Legal y HR confirmen que el proceso sigue siendo legal y operacionalmente justo.

## Actividad de control

Los sistemas de alto impacto deben someterse a pruebas de subgrupos documentadas antes del despliegue y recurrentes utilizando métodos apropiados desde el punto de vista jurídico y técnico. Las disparidades de materiales requieren análisis de causas profundas, mitigación, validación y aprobación.

## Pruebas

- análisis de grupos protegidos y de contexto jurídico;
- los datos y la revisión por variantes indirectas;
- pruebas de subgrupos e intersecciones;
- la accesibilidad y la evaluación del alojamiento;
- resultados de mitigación y validación;
- análisis de revisión y anulación humana;
- quejas y tendencias de seguimiento;
- aprobaciones legales y de gestión.

## Prueba de auditoría

Algunos sistemas que afectan al empleo, la educación, el crédito, los seguros, los servicios esenciales u otras decisiones consiguientes. Verificar que se identificaron los grupos pertinentes y los requisitos legales, las pruebas abarcaron subgrupos y resultados significativos, se validaron las medidas de mitigación, se abordó la accesibilidad y la vigilancia detectó nuevas disparidades.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, en su versión modificada: disposiciones aplicables sobre prácticas prohibidas, alto riesgo, gobernanza de los datos, supervisión humana, precisión, supervisión y derechos fundamentales.
- Carta de los Derechos Fundamentales de la Unión Europea.
- Igualdad aplicable entre la Unión y los Estados miembros, empleo, discapacidad, protección de los consumidores y legislación sectorial.
