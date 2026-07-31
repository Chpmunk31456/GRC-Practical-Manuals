# 11. Controle 6 — Gestão do controle de acesso

*As 8 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

<img src="media/image6.png" style="width:6.15in;height:3.38991in" alt="Contas e privilégios exigem concessão aprovada, autenticação forte, revisão e revogação tempestiva." />

Figura 6. Ciclo de vida de identidade e acesso

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de gestão do controle de acesso. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 6.1 | Estabelecer um processo de concessão de acesso | Autorizar e provisionar acesso com base em necessidade, função e aprovação documentada. | Confirmar escopo, população, aprovadores, segregação de funções, prazo e exceções. | Solicitações, aprovações, registros de provisionamento, funções e revisões. |
| 6.2 | Estabelecer um processo de revogação de acesso | Remover ou ajustar acessos quando pessoas mudam de função, saem ou deixam de necessitar deles. | Verificar tempestividade, cobertura, integrações e exceções. | Tickets, registros de desligamento, relatórios de revogação e conciliações. |
| 6.3 | Exigir MFA para aplicações expostas externamente | Proteger aplicações acessíveis pela internet com autenticação multifator. | Confirmar cobertura por aplicação, usuários, métodos permitidos e exceções. | Configurações de identidade, relatórios de MFA, inventário de aplicações e exceções. |
| 6.4 | Exigir MFA para acesso remoto à rede | Proteger VPN e outros métodos de acesso remoto com MFA. | Verificar cobertura, protocolos, grupos e exceções. | Configuração VPN, políticas de identidade, registros e testes. |
| 6.5 | Exigir MFA para acesso administrativo | Exigir MFA para contas e operações privilegiadas. | Confirmar população administrativa, plataformas cobertas e métodos resistentes a fraude quando aplicável. | PAM, diretórios, políticas, registros de autenticação e exceções. |
| 6.6 | Estabelecer e manter um inventário de sistemas de autenticação e autorização | Manter uma lista atualizada dos sistemas que autenticam usuários ou concedem permissões. | Verificar responsável, finalidade, integrações, criticidade e revisão. | Inventário, diagramas, responsáveis, integrações e revisões. |
| 6.7 | Centralizar o controle de acesso | Utilizar serviços centrais de identidade e autorização sempre que viável. | Confirmar cobertura, integrações, contas locais residuais e tratamento de divergências. | Diretórios, IAM, SSO, relatórios de integração e exceções. |
| 6.8 | Definir e manter controle de acesso baseado em funções | Associar permissões a funções aprovadas e revisar sua adequação. | Verificar catálogo de funções, proprietários, conflitos, revisões e exceções. | Matriz de funções, aprovações, recertificações e relatórios de conflito. |

Consulte os recursos oficiais do CIS para confirmar a linguagem exata e os critérios de avaliação.

# 12. Controle 7 — Gestão contínua de vulnerabilidades

*As 7 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

<img src="media/image7.png" style="width:6.15in;height:3.39605in" alt="Cobertura completa e remediação verificada importam mais do que apenas produzir relatórios de varredura." />

Figura 7. Gestão contínua de vulnerabilidades

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de gestão contínua de vulnerabilidades. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 7.1 | Estabelecer e manter um processo de gestão de vulnerabilidades | Definir escopo, responsáveis, fontes, frequência, priorização, correção e novos testes. | Confirmar cobertura, critérios, exceções e governança. | Política, procedimento, inventários, métricas e atas de revisão. |
| 7.2 | Estabelecer e manter um processo de remediação | Priorizar e corrigir vulnerabilidades conforme risco e prazo aprovado. | Verificar SLAs, responsáveis, exceções, compensações e escalonamento. | Tickets, planos, exceções, aprovações e métricas. |
| 7.3 | Realizar gestão automatizada de correções do sistema operacional | Automatizar a distribuição e verificação de correções de sistemas operacionais. | Confirmar cobertura, anéis de teste, falhas, prazos e exceções. | Console de patch, relatórios, registros de mudança e tickets. |
| 7.4 | Realizar gestão automatizada de correções de aplicações | Automatizar a atualização de aplicações e componentes gerenciados. | Verificar inventário, cobertura, versões, falhas e exceções. | Ferramentas de gestão, relatórios, inventário e registros de mudança. |
| 7.5 | Executar varreduras automatizadas de vulnerabilidades em ativos internos | Avaliar periodicamente ativos internos, preferencialmente com autenticação. | Confirmar população, credenciais, frequência, exclusões e qualidade dos resultados. | Configurações de varredura, resultados, cobertura e exceções. |
| 7.6 | Executar varreduras automatizadas de vulnerabilidades em ativos expostos externamente | Avaliar ativos voltados à internet com frequência e escopo definidos. | Verificar inventário externo, cobertura, frequência, validação e exceções. | Inventário, resultados, relatórios de exposição e tickets. |
| 7.7 | Corrigir vulnerabilidades detectadas | Remediar ou tratar formalmente vulnerabilidades identificadas. | Confirmar prioridade, ação, prazo, evidência de correção e novo teste. | Tickets, alterações, exceções, rescans e evidências de encerramento. |

Consulte os recursos oficiais do CIS para confirmar a linguagem exata e os critérios de avaliação.

# 13. Controle 8 — Gestão de registros de auditoria

*As 12 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de gestão de registros de auditoria. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 8.1 | Estabelecer e manter um processo de gestão de registros de auditoria | Definir fontes, requisitos, responsáveis, proteção, retenção e revisão de logs. | Confirmar escopo, inventário, padrões, exceções e atualização. | Política, procedimento, inventário de fontes e registros de revisão. |
| 8.2 | Coletar registros de auditoria | Habilitar e coletar eventos necessários nos sistemas aplicáveis. | Verificar cobertura, tipos de evento, falhas de coleta e exceções. | Configurações, amostras de logs, relatórios de ingestão e alertas. |
| 8.3 | Garantir armazenamento adequado dos registros de auditoria | Dimensionar e proteger armazenamento para evitar perda ou alteração indevida. | Confirmar capacidade, integridade, acesso, monitoramento e exceções. | Configuração, métricas de capacidade, controles de acesso e alertas. |
| 8.4 | Padronizar a sincronização de tempo | Sincronizar relógios com fontes aprovadas para permitir correlação confiável. | Verificar fontes, cobertura, deriva, alertas e exceções. | Configuração NTP, inventário, métricas e registros. |
| 8.5 | Coletar registros detalhados de auditoria | Registrar detalhes suficientes para investigação e responsabilização. | Confirmar campos, identidade, ação, objeto, resultado, origem e horário. | Configurações, amostras de eventos e validações. |
| 8.6 | Coletar registros de consultas DNS | Registrar consultas DNS relevantes para detecção e investigação. | Verificar resolvedores cobertos, campos, retenção e ingestão. | Logs DNS, configuração, SIEM e relatórios de cobertura. |
| 8.7 | Coletar registros de solicitações de URL | Registrar solicitações web relevantes em proxies, gateways ou serviços equivalentes. | Confirmar fontes, campos, privacidade, retenção e ingestão. | Logs de proxy, gateway, SIEM e testes. |
| 8.8 | Coletar registros de linha de comando | Registrar execução de comandos onde aplicável ao risco. | Verificar plataformas, usuários, integridade, privacidade e cobertura. | Políticas de auditoria, EDR, amostras de eventos e exceções. |
| 8.9 | Centralizar registros de auditoria | Enviar logs relevantes a uma plataforma central protegida. | Confirmar fontes, disponibilidade, atrasos, falhas e exceções. | SIEM, coletores, painéis de ingestão e alertas. |
| 8.10 | Reter registros de auditoria | Manter logs pelo período definido por risco e obrigações. | Verificar política, configuração, armazenamento e descarte. | Política de retenção, configurações, testes e relatórios. |
| 8.11 | Realizar revisões de registros de auditoria | Revisar eventos e alertas com frequência e responsabilidade definidas. | Confirmar casos de uso, responsáveis, frequência, escalonamento e evidências. | Procedimentos, tickets, investigações, métricas e atas. |
| 8.12 | Coletar registros de prestadores de serviços | Obter logs necessários de serviços terceirizados e em nuvem. | Verificar contratos, fontes, acesso, retenção, integração e lacunas. | Contratos, configurações de exportação, logs, SIEM e exceções. |

Consulte os recursos oficiais do CIS para confirmar a linguagem exata e os critérios de avaliação.

# 14. Controle 9 — Proteções de e-mail e navegador web

*As 7 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de proteção de e-mail e navegador web. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 9.1 | Garantir o uso apenas de navegadores e clientes de e-mail com suporte vigente | Permitir somente versões suportadas e atualizadas. | Confirmar inventário, versões, bloqueios, exceções e atualização. | Inventário, políticas, relatórios de versão e tickets. |
| 9.2 | Utilizar serviços de filtragem DNS | Bloquear domínios maliciosos ou não autorizados por meio de resolvedores aprovados. | Verificar cobertura, políticas, bypass, eventos e exceções. | Configuração DNS, políticas, logs e relatórios. |
| 9.3 | Manter e aplicar filtros de URL baseados em rede | Controlar acesso a categorias e destinos web conforme política. | Confirmar cobertura, regras, atualização, eventos e exceções. | Gateway web, proxy, políticas, logs e tickets. |
| 9.4 | Restringir extensões desnecessárias ou não autorizadas de navegadores e clientes de e-mail | Permitir somente extensões aprovadas e necessárias. | Verificar listas permitidas, aplicação, eventos e exceções. | GPO/MDM, catálogo aprovado, relatórios e tickets. |
| 9.5 | Implementar DMARC | Configurar SPF, DKIM e política DMARC apropriada para domínios de e-mail. | Confirmar cobertura de domínios, alinhamento, política, relatórios e exceções. | Registros DNS, relatórios DMARC, inventário de domínios e mudanças. |
| 9.6 | Bloquear tipos de arquivo desnecessários | Impedir anexos e downloads de tipos de arquivo não necessários ou de alto risco. | Verificar regras, cobertura, quarentena, eventos e exceções. | Políticas de gateway, registros, amostras e aprovações. |
| 9.7 | Implantar e manter proteção antimalware em servidores de e-mail | Verificar mensagens e anexos com mecanismos atualizados. | Confirmar cobertura, atualização, detecção, quarentena e resposta. | Configuração, relatórios, alertas, tickets e métricas. |

Consulte os recursos oficiais do CIS para confirmar a linguagem exata e os critérios de avaliação.

# 15. Controle 10 — Defesas contra malware

*As 7 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de defesa contra malware. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 10.1 | Implantar e manter software antimalware | Proteger ativos aplicáveis com solução antimalware gerenciada. | Confirmar cobertura, estado, políticas, alertas e exceções. | Console, inventário, relatórios de cobertura e tickets. |
| 10.2 | Configurar atualizações automáticas de assinaturas antimalware | Atualizar automaticamente mecanismos, assinaturas e inteligência. | Verificar frequência, falhas, cobertura e exceções. | Configuração, relatórios de atualização e alertas. |
| 10.3 | Desabilitar execução automática e reprodução automática em mídias removíveis | Impedir execução automática de conteúdo de mídias removíveis. | Confirmar política, plataformas, cobertura e exceções. | GPO/MDM, configuração, testes e relatórios. |
| 10.4 | Configurar varredura antimalware automática de mídias removíveis | Verificar mídias removíveis antes ou durante o uso. | Confirmar política, eventos, bloqueios, cobertura e exceções. | Configuração, logs, alertas e testes. |
| 10.5 | Habilitar recursos antiexploração | Ativar proteções contra exploração de memória e comportamento malicioso. | Verificar plataformas, políticas, compatibilidade, eventos e exceções. | EDR, políticas, relatórios e testes. |
| 10.6 | Gerenciar software antimalware de forma centralizada | Administrar políticas, atualizações, alertas e resposta em console central. | Confirmar cobertura, acesso administrativo, monitoramento e exceções. | Console, funções, políticas, alertas e métricas. |
| 10.7 | Utilizar software antimalware baseado em comportamento | Detectar atividades suspeitas além de assinaturas conhecidas. | Verificar cobertura, regras, alertas, investigação e ajuste. | EDR, eventos, casos de investigação, tickets e métricas. |

Consulte os recursos oficiais do CIS para confirmar a linguagem exata e os critérios de avaliação.

