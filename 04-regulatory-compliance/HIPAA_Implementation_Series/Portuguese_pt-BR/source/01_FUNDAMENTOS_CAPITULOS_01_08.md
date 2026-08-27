# Manual 06 — Implementação e Auditoria de HIPAA
## Fonte localizada pt-BR — Capítulos 01–08

> Rascunho de localização para revisão semântica humana. Orientação educacional de implementação baseada na linha de base controlada da HIPAA vigente. Este material não fornece aconselhamento jurídico, não determina o status de entidade coberta ou parceiro de negócios, não estabelece conformidade e não determina se um incidente constitui uma violação sujeita a notificação. As mudanças propostas à Regra de Segurança são apenas para preparação até que o HHS emita uma regra final e a linha de base controlada seja atualizada.

## Capítulo 01 — Escopo, papel da entidade e responsabilidade

Comece determinando quais unidades organizacionais, sistemas, serviços e relacionamentos estão dentro do escopo de implementação da HIPAA. Registre a base para o tratamento como entidade coberta, plano de saúde, prestador de assistência à saúde, clearinghouse, parceiro de negócios ou subcontratado, conforme aplicável, e identifique responsáveis por privacidade, segurança, jurídico, conformidade, operações e negócio.

O registro de implementação deve distinguir fatos confirmados de premissas que exigem interpretação jurídica ou regulatória. Decisões de escopo devem ser datadas, sustentadas por evidência e reavaliadas após mudanças materiais organizacionais, de serviços, fluxos de dados, aquisições ou regulação.

## Capítulo 02 — Inventário de PHI e ePHI

As organizações devem manter um inventário de informações de saúde protegidas (PHI) e informações de saúde protegidas eletrônicas (ePHI) que identifique onde as informações são criadas, recebidas, mantidas, transmitidas, armazenadas, copiadas em backup, exportadas ou descartadas.

Os registros devem identificar sistemas, aplicações, endpoints, bancos de dados, serviços em nuvem, interfaces, mídias removíveis, processos em papel quando relevantes, proprietários, custodiantes, classificações de dados, requisitos de retenção e destinatários externos. Repositórios desconhecidos e exportações não gerenciadas devem ser tratados como lacunas de controle que exigem investigação.

## Capítulo 03 — Mapeamento de fluxo de dados e limites

Mapeie como PHI e ePHI se movimentam entre membros da força de trabalho, aplicações, instalações, serviços em nuvem, fornecedores, parceiros de negócios, pacientes, planos de saúde, prestadores e outros destinatários autorizados. Inclua limites de confiança, pontos de autenticação, interfaces, APIs, transferências de arquivos, mensagens, acesso remoto e caminhos de backup ou arquivamento.

Mapas de fluxo de dados apoiam análise de riscos, revisão de mínimo necessário, desenho de controles de acesso, investigação de incidentes, governança de parceiros de negócios e avaliação de violações. Os mapas devem ser versionados e vinculados aos sistemas e processos que representam.

## Capítulo 04 — Governança de privacidade e mínimo necessário

A governança de privacidade deve definir quem pode usar ou divulgar PHI, para qual finalidade, sob qual autoridade e com qual aprovação ou verificação. Onde o padrão de mínimo necessário se aplicar, os processos devem limitar acesso, uso, divulgação e solicitações à quantidade razoavelmente necessária para a finalidade permitida.

Desenho de papéis, aprovações de fluxo de trabalho, relatórios, exportações, analytics, acesso de suporte e privilégios administrativos devem ser revisados quanto a exposição desnecessária. Exceções devem identificar justificativa, autoridade, escopo, responsável, duração e controles compensatórios.

## Capítulo 05 — Análise de riscos da Regra de Segurança

A análise de riscos deve ser precisa e abrangente para o ambiente de ePHI da organização. Deve identificar ativos, fluxos de dados, ameaças, vulnerabilidades, salvaguardas existentes, probabilidade, impacto potencial e risco resultante usando um método repetível apropriado ao tamanho, complexidade, capacidades, infraestrutura técnica e contexto de risco da organização.

Uma análise de riscos não está completa apenas porque um checklist foi preenchido ou uma varredura de vulnerabilidades foi executada. A evidência deve mostrar os sistemas e ePHI considerados, premissas, métodos, achados, limitações, revisores responsáveis e data da análise.

## Capítulo 06 — Gestão e tratamento de riscos

A gestão de riscos deve converter riscos identificados em decisões de tratamento com responsabilidades definidas. Para cada risco material, registre a salvaguarda ou ação corretiva planejada, responsável, data-alvo, dependências, controles provisórios, risco residual, aprovação e evidência de conclusão.

Itens de alto risco não devem permanecer indefinidamente abertos sem escalonamento ou aceitação documentada por um proprietário de risco autorizado. A remediação concluída deve ser validada e não encerrada apenas com declaração da administração.

## Capítulo 07 — Salvaguardas administrativas

As salvaguardas administrativas devem traduzir responsabilidades de segurança da HIPAA em governança operacional. Controles relevantes incluem responsabilidade de segurança atribuída, autorização e supervisão da força de trabalho, gestão de acesso à informação, conscientização e treinamento de segurança, procedimentos de incidentes de segurança, planejamento de contingência, avaliação e acordos com parceiros de negócios quando aplicável.

A implementação deve mostrar quem executa cada controle, com que frequência, qual evidência é retida, quais exceções existem e como falhas são escaladas.

## Capítulo 08 — Gate de implementação fail-closed

Um pacote de implementação ou auditoria HIPAA deve falhar de forma fechada quando o escopo material não estiver resolvido, faltar análise necessária da lei vigente, os limites de ePHI forem desconhecidos, permanecerem lacunas significativas de análise de riscos, a evidência não sustentar as salvaguardas alegadas ou uma revisão humana, jurídica ou de conformidade exigida estiver incompleta.

O QA automatizado do repositório pode confirmar estrutura, registros de estado de fontes, links e evidência de publicação. Ele não pode determinar status jurídico, eficácia de controles, conformidade ou obrigações de notificação de violações. Mudanças materiais reabrem os gates de revisão afetados.