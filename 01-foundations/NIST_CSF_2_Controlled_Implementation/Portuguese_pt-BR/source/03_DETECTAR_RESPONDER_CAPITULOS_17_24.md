# Manual 09 — Implementação Controlada do NIST CSF 2.0
## Fonte controlada em português `pt-BR` — Capítulos 17–24

> Rascunho de localização. Exige revisão semântica humana antes da publicação. O desenho de monitoramento e resposta deve refletir contexto, exposição a ameaças, criticidade, necessidades de evidência e autoridade de decisão.

## Capítulo 17 — Estratégia de monitoramento contínuo
Defina quais condições, eventos, ativos, identidades, serviços, fornecedores e sinais de controle exigem monitoramento. Estabeleça fontes de telemetria, responsáveis, cobertura, retenção, proteção, cadência de revisão e pontos cegos conhecidos.

A evidência deve identificar fontes ausentes ou pouco confiáveis; a simples implantação de uma ferramenta não demonstra visibilidade efetiva.

## Capítulo 18 — Detecção de eventos adversos
Use sinais técnicos e operacionais para identificar possíveis eventos de segurança cibernética. A lógica de detecção deve ser orientada por risco, testada, ajustada, versionada quando apropriado e conectada a processos responsáveis de triagem.

Registre cobertura, preocupações com falsos positivos e falsos negativos, limiares de escalonamento e lacunas materiais.

## Capítulo 19 — Análise e correlação de eventos
Analise eventos usando contexto relevante, como criticidade do ativo, identidade, comportamento, inteligência de ameaças, vulnerabilidades, impacto de negócio e atividades relacionadas. Preserve evidência suficiente para decisões e revisão posterior.

Correlação automatizada ou análise apoiada por IA não deve ocultar incerteza, inferência sem suporte, lacunas de procedência ou a necessidade de escalonamento humano.

## Capítulo 20 — Declaração e coordenação de incidentes
Defina critérios e autoridade para declarar incidentes, atribuir severidade, ativar estruturas de resposta e coordenar segurança, tecnologia, negócio, jurídico, privacidade, comunicações, resiliência e fornecedores.

O registro deve capturar quem tomou decisões materiais, quando, com base em quais evidências e com quais premissas não resolvidas.

## Capítulo 21 — Contenção e mitigação
Contenha e mitigue incidentes usando ações predefinidas e específicas da situação que considerem consequências operacionais, de segurança, legais, probatórias e de recuperação.

Registre responsável, horário, justificativa, sistemas afetados, validação, necessidades de rollback e risco residual.

## Capítulo 22 — Comunicações de incidentes
Planeje comunicações internas e externas, escalonamento, coordenação com partes interessadas, análise de notificações regulatórias ou contratuais e interação com fornecedores/clientes conforme aplicável.

Automação pode apoiar roteamento e redação, mas não deve tomar decisões legais de notificação sem revisão humana.

## Capítulo 23 — Evidência de resposta e lições aprendidas
Preserve cronologias, alertas, logs, evidência forense, decisões, comunicações, ações de contenção, achados, perguntas em aberto e ações de acompanhamento. Realize revisão de lições proporcional à importância do incidente.

As lições devem alimentar governança, avaliação de risco, arquitetura, detecção, treinamento, supervisão de fornecedores e recuperação.

## Capítulo 24 — Gate fail-closed de DETECTAR e RESPONDER
DETECTAR e RESPONDER estão incompletos quando pontos cegos materiais não são reconhecidos, a autoridade de incidente é incerta, alertas críticos não são triados, a preservação de evidência é inadequada ou ações significativas não podem ser reconstruídas.

A QA do repositório pode validar registros esperados e controles estruturais; efetividade de incidentes e obrigações legais exigem avaliação humana competente.

**Status da localização:** rascunho controlado; revisão semântica humana obrigatória antes de aprovação ou publicação.
