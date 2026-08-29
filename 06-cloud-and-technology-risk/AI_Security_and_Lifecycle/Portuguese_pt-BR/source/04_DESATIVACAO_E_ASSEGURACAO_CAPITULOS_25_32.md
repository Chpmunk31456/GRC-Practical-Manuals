# Manual 07 — Segurança de IA e Controles do Ciclo de Vida
## Fonte controlada em português brasileiro — Capítulos 25–32

> Tradução de trabalho sujeita à revisão semântica humana. Esta orientação defensiva original não garante segurança nem substitui revisão específica da organização.

## Capítulo 25 — Mudança de fornecedores e dependências

Mudanças de fornecedor ou dependência devem ser avaliadas quanto ao efeito em segurança antes da adoção. Mudanças relevantes incluem hospedagem, versão do modelo, arquitetura de serviço, processamento de dados, subprocessadores, métodos de acesso, logging, controles de segurança e compromissos contratuais de notificação.

## Capítulo 26 — Resiliência e operação degradada

O planejamento de segurança deve considerar como o sistema se comporta quando modelos, APIs, recuperação, monitoramento ou serviços externos estão degradados ou indisponíveis. Modos alternativos não devem contornar silenciosamente controles de segurança, aprovação ou proteção de dados.

## Capítulo 27 — Considerações de backup e recuperação

O planejamento de recuperação deve identificar quais configurações, prompts, políticas, índices, credenciais, evidências e dependências são necessários para restaurar um estado controlado conhecido. Procedimentos de recuperação devem ser validados proporcionalmente à criticidade.

## Capítulo 28 — Desativação e decomissionamento

A desativação deve revogar identidades, credenciais e integrações; desabilitar endpoints; remover ou arquivar dados conforme requisitos; preservar evidências obrigatórias; encerrar acesso de fornecedores; e documentar obrigações não resolvidas.

## Capítulo 29 — Métricas de segurança e reporte gerencial

Métricas devem estar vinculadas a decisões. Relatórios úteis podem incluir achados materiais, exceções, estado de reavaliação, tendências de incidentes, mudanças de dependências, cobertura de validação, remediação vencida e indicadores de saúde de controles.

## Capítulo 30 — Limitações da asseguração de segurança

Nenhuma suíte automatizada de testes, checklist de controles, revisão de segurança ou workflow de repositório pode estabelecer que um sistema de IA esteja livre de fraquezas. Declarações de asseguração devem identificar escopo, período, evidências e limitações que as sustentam.

## Capítulo 31 — Melhoria contínua

Lições de incidentes, quase incidentes, testes, mudanças de fornecedores, feedback de usuários e falhas de controles devem retroalimentar modelos de ameaças, planos de validação, controles operacionais e treinamento.

## Capítulo 32 — Limite de liberação do manual

Antes da publicação deste manual devem ser concluídas a verificação de fontes, o mestre controlado completo em inglês, revisão técnica/de segurança, revisão semântica de `es-419` e `pt-BR`, revisão de gráficos/acessibilidade, QA documental e por página, proveniência, auditoria de segurança do repositório e Aprovação Humana Final de Liberação.

Mudanças materiais de conteúdo após aprovação humana reabrem os gates afetados.
