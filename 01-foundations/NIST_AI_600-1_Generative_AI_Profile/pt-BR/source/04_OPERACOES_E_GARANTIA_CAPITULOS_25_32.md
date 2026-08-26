# Manual 04 — Implementação do Perfil de IA Generativa NIST AI 600-1
## Fonte controlada em português brasileiro — Capítulos 25–32

> Tradução assistida por máquina para revisão controlada. Este conjunto apoia a gestão contínua de riscos de IA generativa e não reproduz o texto do NIST. A aprovação semântica humana continua obrigatória antes da publicação.

## Capítulo 25 — Controles de implantação e liberação

A implantação deveria usar um registro controlado vinculado ao artefato testado, configuração, versão do modelo, estado de dados/recuperação, ferramentas, guardrails e condições operacionais aprovadas. Desvio material entre o candidato testado e o sistema implantado invalida a evidência de liberação até ser avaliado.

Os registros deveriam identificar aprovadores responsáveis, exceções abertas, limites de monitoramento, autoridade de reversão e datas de revisão.

## Capítulo 26 — Monitoramento e limites operacionais

O monitoramento deveria estar ligado a riscos conhecidos e limites de decisão, não a telemetria genérica. Medidas relevantes podem incluir taxas de saídas nocivas, respostas sem suporte, eventos de segurança, sinais de vazamento de dados, reclamações de usuários, falhas de ferramentas, indicadores de drift do modelo, latência/disponibilidade, mudanças de fornecedores e volume de exceções.

Violações de limite deveriam mapear para ações predefinidas: investigar, restringir, aumentar revisão humana, desabilitar função, reverter ou parar o sistema.

## Capítulo 27 — Gestão de mudanças e reavaliação

Mudanças em modelos, prompts, instruções do sistema, fontes de recuperação, ferramentas, permissões, tratamento de dados, fornecedores, guardrails, interfaces ou uso de negócio podem alterar risco. Registros de mudança deveriam classificar materialidade e identificar quais evidências anteriores permanecem válidas.

Mudanças materiais reabrem gates afetados de risco, teste, segurança, privacidade, acessibilidade, revisão humana e liberação. Mudanças emergenciais exigem revisão retrospectiva e conclusão de evidências dentro de período definido.

## Capítulo 28 — Resposta a incidentes e contenção

A resposta a incidentes de IA generativa deveria integrar-se à gestão corporativa de incidentes preservando evidência específica de IA. As equipes deveriam capturar prompts, saídas, identificadores de modelo/configuração, contexto de recuperação, chamadas de ferramentas, identidades, horários, logs, registros afetados, avisos de fornecedores e estado de controles quando lícito e viável.

Opções de contenção podem incluir desabilitar ferramentas, reduzir permissões, isolar fontes de recuperação, reverter configuração, limitar usuários, aumentar revisão humana ou suspender o serviço.

## Capítulo 29 — Ação corretiva e validação de remediação

A ação corretiva deveria tratar causas raiz e não apenas suprimir a saída observada. Registros deveriam identificar achado, causa, responsável, ação planejada, data-alvo, método de validação, evidência, risco residual e decisão de encerramento.

Uma correção não deve ser considerada encerrada apenas porque um caso de teste agora passa. O reteste deveria avaliar variantes prováveis e risco de regressão.

## Capítulo 30 — Revisão periódica e relatórios gerenciais

A revisão periódica deveria avaliar se o caso de uso permanece apropriado, controles continuam efetivos, premissas de risco permanecem válidas, evidência está atualizada, fornecedores ou componentes mudaram e resultados operacionais permanecem dentro da tolerância.

Relatórios gerenciais deveriam distinguir fatos, tendências, premissas, riscos não resolvidos, exceções aceitas e decisões exigidas. Questões de alto risco deveriam ser visíveis ao responsável pelo risco, não ocultas em relatórios técnicos.

## Capítulo 31 — Desativação, disposição de dados e saída

O planejamento de desativação deveria tratar endpoints de modelo, credenciais, prompts, índices de recuperação, armazenamentos vetoriais, logs, dados de usuários, caches, integrações, acesso de fornecedores, evidência retida e obrigações contratuais.

A organização deveria verificar devolução ou exclusão de dados quando exigida, revogar acessos e segredos, desabilitar integrações, preservar registros exigidos, documentar obrigações não resolvidas e registrar a decisão de desativação.

## Capítulo 32 — Garantia, limitações e limite final de liberação

A garantia é cumulativa e específica ao escopo. QA do repositório, testes automatizados, red teaming, documentação ou checklist concluído não garantem que um sistema de IA generativa seja seguro, protegido, conforme, preciso, justo ou adequado a todos os contextos.

Antes da publicação deste manual, o pacote controlado deve concluir verificação de fontes, revisão técnica/editorial, revisão semântica `es-419` e `pt-BR`, verificação de gráficos/acessibilidade, geração DOCX/PDF, QA por página, proveniência e checksums, revisão de repositório/segurança e Aprovação Humana Final de Liberação explícita.

Qualquer mudança material de conteúdo após aprovação humana reabre o gate de revisão afetado.
