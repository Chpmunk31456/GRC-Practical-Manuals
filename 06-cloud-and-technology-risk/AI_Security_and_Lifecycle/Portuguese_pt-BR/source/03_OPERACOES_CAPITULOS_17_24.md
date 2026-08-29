# Manual 07 — Segurança de IA e Controles do Ciclo de Vida
## Fonte controlada em português brasileiro — Capítulos 17–24

> Tradução de trabalho sujeita à revisão semântica humana. Esta orientação defensiva original não garante segurança nem substitui decisões de risco específicas da organização.

## Capítulo 17 — Hardening de implantação

A implantação deve usar configurações aprovadas, identidades de privilégio mínimo, segredos protegidos, caminhos de rede controlados, logging, monitoramento e capacidade de rollback proporcionais ao risco.

O sistema implantado deve ser comparado com o candidato de liberação validado para evitar que drift relevante para segurança seja introduzido durante a promoção.

## Capítulo 18 — Monitoramento e alertas

O monitoramento deve se concentrar em indicadores ligados a riscos conhecidos: acesso incomum, mudanças de permissões, falhas repetidas de controles, atividade inesperada de ferramentas, tratamento de dados sensíveis, mudanças de dependências, degradação de disponibilidade e exceções de política.

Alertas devem ter responsáveis, regras de severidade, caminhos de escalonamento e expectativas documentadas de resposta.

## Capítulo 19 — Logging e preservação de evidências

Logs relevantes para segurança devem preservar contexto suficiente para apoiar investigações, respeitando privacidade e minimização de dados. Registros úteis podem incluir identidades, timestamps, referências de modelo/configuração, invocações de ferramentas, decisões de política, referências de recuperação e eventos de mudança.

A retenção deve ser definida e o acesso aos logs controlado.

## Capítulo 20 — Resposta a incidentes

Eventos de segurança relacionados à IA devem integrar-se ao processo de incidentes da organização. Os planos de resposta devem identificar opções de contenção, evidências a preservar, contatos de fornecedores, caminhos de notificação, etapas de recuperação e critérios para suspender ou restringir o serviço.

## Capítulo 21 — Mecanismos de rollback e parada

Sistemas com impacto operacional ou de segurança material devem possuir mecanismos de rollback ou parada testados. A autoridade para acioná-los deve ser explícita.

Um controle que exista apenas no papel não deve receber crédito até ser validado técnica e operacionalmente.

## Capítulo 22 — Gestão de mudanças e configuração

Mudanças em modelos, recuperação, prompts, instruções do sistema, ferramentas, permissões, fontes de dados, hospedagem, guardrails ou fornecedores podem alterar a postura de segurança. Os registros de mudança devem classificar materialidade e identificar qual validação anterior permanece válida.

## Capítulo 23 — Governança de exceções

Exceções de segurança devem registrar o requisito não atendido, justificativa de negócio, controles compensatórios, responsável, risco residual, aprovador, data de expiração e requisito de monitoramento.

Exceções de alto risco não devem tornar-se permanentes por extensões administrativas repetidas sem reavaliação.

## Capítulo 24 — Reavaliação periódica de segurança

A reavaliação periódica deve examinar se ameaças, dependências, acessos, uso de dados, estado de fornecedores, comportamento operacional e premissas anteriores continuam válidos.

A evidência deve mostrar o que foi revisado, o que mudou, o que continua aceitável e qual ação adicional é necessária.
