# Manual 08 — Ciclo de Vida de Risco de Fornecedores e Terceiros
## Rascunho controlado pt-BR — Capítulos 01–08

> Rascunho de localização para revisão semântica humana. Esta orientação original operacionaliza a linha de base controlada sem reproduzir texto de normas e não certifica nenhum fornecedor nem elimina risco de terceiros.

## Capítulo 01 — Objetivo e ciclo de vida de TPRM

A gestão de riscos de terceiros deve governar todo o ciclo do relacionamento: entrada, classificação, due diligence, decisão de risco, contratação, onboarding, monitoramento, gestão de incidentes e mudanças, reavaliação e desligamento.

O processo deve ser aplicado proporcionalmente ao que o fornecedor pode acessar, influenciar, processar, hospedar, operar ou interromper.

## Capítulo 02 — Inventário de fornecedores e responsáveis

Mantenha um inventário controlado de fornecedores, prestadores de serviços, subprocessadores, provedores de IA/modelos, provedores de dados, APIs, serviços de hospedagem e outras dependências externas relevantes.

Cada registro deve identificar responsável de negócio, serviço, dados tratados, dependências de sistemas, contrato, criticidade, geografia quando aplicável, exposição a quartas partes, data de renovação, nível de monitoramento e requisitos de saída.

## Capítulo 03 — Criticidade e risco inerente

Criticidade pergunta o que acontece se o fornecedor falhar; risco inerente pergunta qual exposição existe antes de considerar controles. São relacionados, mas não idênticos.

Os fatores podem incluir acesso a dados sensíveis, conectividade privilegiada, acesso a produção, dependência operacional, concentração, substituibilidade, impacto financeiro, exposição regulatória, autonomia de IA, dependência de modelos ou dados e consequências para continuidade de negócios.

## Capítulo 04 — Planejamento da due diligence

A due diligence deve ser baseada em evidências e proporcional. O plano de revisão deve identificar as perguntas a responder, as evidências necessárias, os revisores e os limites de aceitação.

Possíveis evidências incluem políticas, relatórios independentes, certificações, informações de arquitetura, resultados de testes, histórico de incidentes, evidências de resiliência, documentação de privacidade, compromissos contratuais, informações financeiras e entrevistas direcionadas.

Um questionário isolado não constitui asseguração para um fornecedor material.

## Capítulo 05 — Revisão de segurança, privacidade e resiliência

A revisão deve determinar se os controles do fornecedor são adequados ao serviço e à exposição. Segurança, privacidade e resiliência devem ser avaliadas como disciplinas conectadas, e não como questionários isolados.

A revisão deve abordar identidade, acesso, proteção de dados, logs, gestão de vulnerabilidades, resposta a incidentes, capacidade de recuperação, subcontratação, localização, retenção, exclusão e continuidade do serviço quando aplicável.

## Capítulo 06 — Fornecedores de IA e dependências de modelos/componentes

A revisão de fornecedores de IA deve identificar provedores de modelos, inferência hospedada, serviços de fine-tuning, fornecedores de dados, serviços de segurança, fontes de recuperação, provedores de agentes/ferramentas e outros componentes de IA.

Questões-chave incluem uso de dados, comportamento de treinamento ou retenção, notificação de mudança de modelo/versão, limites de segurança, controles de conteúdo e abuso, disponibilidade do serviço, termos de propriedade intelectual, evidência de auditoria, notificação de incidentes e opções de saída.

## Capítulo 07 — Decisão de risco e exceções

Todo resultado material de due diligence deve gerar uma decisão: aprovar, aprovar condicionalmente, exigir remediação, restringir escopo, adiar ou rejeitar.

As exceções devem registrar requisito não atendido, justificativa de negócio, controle compensatório, responsável, risco residual, aprovador, data de expiração e requisito de monitoramento. Exceções permanentes sem revisão periódica devem ser evitadas.

## Capítulo 08 — Gate de onboarding com falha fechada

O onboarding deve falhar fechado quando a due diligence obrigatória estiver incompleta, faltarem evidências críticas, achados de alto risco não tiverem tratamento aprovado, termos contratuais obrigatórios estiverem pendentes ou faltar aprovação humana obrigatória.

Um fornecedor não deve ser apresentado como “aprovado” apenas porque o processo de compras foi concluído. Uma mudança material posterior — como novo subprocessador, modelo de serviço, uso de dados, componente de IA, região de hospedagem ou arquitetura de segurança — pode reabrir a revisão afetada.