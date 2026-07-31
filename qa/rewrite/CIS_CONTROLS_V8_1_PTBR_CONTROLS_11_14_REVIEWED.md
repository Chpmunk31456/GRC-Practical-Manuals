# 16. Controle 11 — Recuperação de dados

*As 5 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de recuperação de dados. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 11.1 | Estabelecer e manter um processo de recuperação de dados | Definir responsabilidades, escopo, prioridades, dependências, objetivos e procedimentos para recuperar dados e serviços. | Confirmar aprovação, responsáveis, cobertura, revisão e alinhamento com necessidades de negócio. | Política, plano de recuperação, inventário de sistemas, RTO/RPO, responsáveis e registros de revisão. |
| 11.2 | Executar backups automatizados | Realizar cópias de segurança de dados e configurações conforme uma programação aprovada. | Verificar cobertura, frequência, falhas, alertas e tratamento de exceções. | Configuração de backup, relatórios de execução, alertas, tickets e métricas de sucesso. |
| 11.3 | Proteger os dados de recuperação | Proteger backups contra acesso, alteração, exclusão e criptografia não autorizados. | Revisar acesso, criptografia, imutabilidade, segregação e monitoramento. | ACLs, KMS, armazenamento imutável, registros de acesso e alertas. |
| 11.4 | Estabelecer e manter uma instância isolada de dados de recuperação | Manter pelo menos uma cópia de recuperação separada do ambiente de produção. | Confirmar isolamento lógico ou físico, credenciais separadas e resistência a ransomware. | Diagramas, configuração, inventário de cópias isoladas e testes de acesso. |
| 11.5 | Testar a recuperação de dados | Executar testes periódicos de restauração e confirmar integridade, tempo e completude. | Comparar resultados com critérios aprovados e verificar correções por novo teste. | Planos de teste, resultados de restauração, evidências de integridade, achados e retestes. |

Consulte os recursos oficiais do CIS para confirmar a linguagem e os critérios de avaliação.

# 17. Controle 12 — Gestão da infraestrutura de rede

*As 8 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de gestão da infraestrutura de rede. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 12.1 | Assegurar que a infraestrutura de rede esteja atualizada | Manter hardware, software e serviços de rede em versões suportadas e aprovadas. | Verificar inventário, versões, fim de suporte, exceções e planos de atualização. | Inventário, matrizes de suporte, configurações, tickets e exceções. |
| 12.2 | Estabelecer e manter uma arquitetura de rede segura | Definir zonas, fluxos, confiança, segmentação e controles de acesso conforme o risco. | Revisar arquitetura, aprovações, mudanças, fluxos permitidos e testes. | Diagramas, padrões, regras, análises de fluxo e resultados de testes. |
| 12.3 | Gerenciar com segurança a infraestrutura de rede | Utilizar canais, protocolos, autenticação e estações administrativas seguras. | Confirmar métodos administrativos, MFA, registros e restrições de origem. | Configuração, listas de administradores, bastions, PAM e registros. |
| 12.4 | Estabelecer e manter diagramas de arquitetura | Manter diagramas atuais da infraestrutura, conexões, zonas e dependências. | Verificar abrangência, responsáveis, revisão e conciliação com a configuração real. | Diagramas, CMDB, revisões e tickets de atualização. |
| 12.5 | Centralizar autenticação, autorização e auditoria de rede | Utilizar serviços centrais para identidade administrativa e registro de atividades. | Verificar cobertura, integrações, disponibilidade, contas locais e exceções. | RADIUS/TACACS+, diretórios, logs, inventário e exceções. |
| 12.6 | Utilizar protocolos seguros de gestão e comunicação de rede | Desabilitar protocolos inseguros e utilizar alternativas criptografadas e autenticadas. | Revisar configuração, cobertura, certificados e desvios. | Configurações SSH, HTTPS, SNMPv3, VPN, certificados e resultados de varredura. |
| 12.7 | Assegurar que dispositivos remotos utilizem VPN e AAA corporativo | Exigir canais seguros e autenticação corporativa para acesso remoto à rede. | Confirmar cobertura, MFA, políticas, registros e exceções. | Configuração VPN, AAA, relatórios de conexão, políticas e tickets. |
| 12.8 | Manter recursos computacionais dedicados para trabalho administrativo | Separar atividades administrativas de navegação, e-mail e uso comum. | Verificar população, configuração, uso, monitoramento e exceções. | Inventário de estações administrativas, políticas, registros e controles de acesso. |

Consulte os recursos oficiais do CIS para confirmar a linguagem e os critérios de avaliação.

# 18. Controle 13 — Monitoramento e defesa da rede

*As 11 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

<img src="media/image8.png" style="width:6.15in;height:3.39in" alt="Contexto centralizado, detecção ajustada, investigação humana e resposta formam uma defesa útil." />

Figura 8. Fluxo de monitoramento até resposta

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de monitoramento e defesa da rede. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 13.1 | Centralizar alertas de eventos de segurança | Reunir alertas relevantes em uma plataforma ou processo central de triagem. | Verificar fontes, cobertura, roteamento, prioridade e tratamento. | SIEM, integrações, filas, tickets, métricas e procedimentos. |
| 13.2 | Implantar uma solução de detecção de intrusão baseada em host | Detectar comportamentos e eventos suspeitos em endpoints e servidores. | Confirmar cobertura, estado dos agentes, regras, alertas e exceções. | Console EDR/HIDS, inventário, políticas, alertas e tickets. |
| 13.3 | Implantar uma solução de detecção de intrusão de rede | Monitorar tráfego de rede para identificar atividades suspeitas. | Verificar sensores, segmentos, regras, visibilidade e tratamento de alertas. | Configuração NIDS, diagramas, cobertura, eventos e investigações. |
| 13.4 | Realizar filtragem de tráfego entre segmentos de rede | Permitir somente fluxos necessários e aprovados entre zonas. | Revisar regras, justificativas, recertificação, mudanças e testes. | Regras de firewall, matrizes de fluxo, aprovações e resultados de testes. |
| 13.5 | Gerenciar o controle de acesso para ativos remotos | Aplicar identidade, postura, autorização e monitoramento ao acesso remoto. | Confirmar população, políticas, MFA, restrições e exceções. | VPN/ZTNA, MDM, IAM, registros e relatórios. |
| 13.6 | Coletar registros de fluxo de tráfego de rede | Manter telemetria suficiente para analisar comunicações e anomalias. | Verificar fontes, campos, retenção, sincronização e uso em investigações. | NetFlow/IPFIX, registros, retenção e casos de investigação. |
| 13.7 | Implantar uma solução de prevenção de intrusão baseada em host | Bloquear ou conter atividades maliciosas em endpoints quando apropriado. | Confirmar modo de prevenção, políticas, cobertura, exceções e testes. | Console HIPS/EDR, políticas, eventos bloqueados e testes. |
| 13.8 | Implantar uma solução de prevenção de intrusão de rede | Bloquear tráfego malicioso conhecido conforme regras aprovadas. | Verificar posicionamento, modo, regras, exceções e impactos. | Configuração NIPS, alterações, eventos, exceções e testes. |
| 13.9 | Implantar controle de acesso em nível de porta | Controlar dispositivos e identidades que podem se conectar à rede. | Confirmar cobertura, autenticação, quarentena, exceções e falhas. | NAC/802.1X, inventário, políticas, registros e tickets. |
| 13.10 | Realizar filtragem na camada de aplicação | Restringir tráfego por aplicação, conteúdo ou contexto conforme o risco. | Revisar políticas, cobertura, exceções, alertas e mudanças. | Proxy, NGFW, WAF, regras, eventos e aprovações. |
| 13.11 | Ajustar limiares de alertas de eventos de segurança | Afinar regras para reduzir ruído sem perder detecções relevantes. | Confirmar responsáveis, critérios, histórico, testes e revisão periódica. | Registros de tuning, métricas, casos de teste e aprovações. |

Consulte os recursos oficiais do CIS para confirmar a linguagem e os critérios de avaliação.

# 19. Controle 14 — Conscientização e capacitação em segurança

*As 9 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de conscientização e capacitação em segurança. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 14.1 | Estabelecer e manter um programa de conscientização em segurança | Definir conteúdo, público, frequência, responsabilidades, avaliação e melhoria. | Verificar aprovação, cobertura, atualidade, conclusão e exceções. | Programa, currículo, população, registros de conclusão e métricas. |
| 14.2 | Capacitar a força de trabalho para reconhecer ataques de engenharia social | Ensinar identificação e comunicação de phishing, fraude, pretexting e manipulação. | Confirmar conteúdo, frequência, simulações, resultados e acompanhamento. | Materiais, simulações, relatórios, tickets e ações corretivas. |
| 14.3 | Capacitar a força de trabalho em boas práticas de autenticação | Ensinar uso de MFA, senhas exclusivas, gestores de senhas e proteção de credenciais. | Verificar conteúdo, população, conclusão e avaliação. | Treinamento, registros, avaliações e campanhas. |
| 14.4 | Capacitar a força de trabalho em boas práticas de tratamento de dados | Ensinar classificação, compartilhamento, armazenamento, retenção e descarte seguros. | Confirmar alinhamento com políticas e cobertura de funções relevantes. | Materiais, políticas, registros de conclusão e avaliações. |
| 14.5 | Capacitar a força de trabalho sobre causas de exposição não intencional de dados | Explicar erros comuns, destinatários incorretos, links públicos, dispositivos e serviços não aprovados. | Verificar exemplos, público, conclusão e resultados. | Conteúdo, campanhas, registros e incidentes correlacionados. |
| 14.6 | Capacitar a força de trabalho para reconhecer e comunicar incidentes de segurança | Ensinar sinais, canais, urgência e informações necessárias para reporte. | Confirmar canais, exercícios, conhecimento e acompanhamento. | Materiais, contatos, exercícios, tickets e métricas de reporte. |
| 14.7 | Capacitar a força de trabalho para identificar e comunicar atualizações de segurança ausentes | Ensinar como reconhecer sistemas desatualizados e reportar desvios. | Verificar conteúdo, população e integração com suporte. | Treinamento, procedimentos, tickets e exemplos. |
| 14.8 | Capacitar a força de trabalho sobre riscos de redes inseguras | Ensinar uso seguro de Wi-Fi, VPN, hotspots e redes públicas. | Confirmar cobertura de trabalhadores remotos e viajantes. | Materiais, políticas, registros e avaliações. |
| 14.9 | Conduzir conscientização e capacitação específicas por função | Fornecer treinamento adicional para funções com riscos ou privilégios específicos. | Verificar matriz de funções, conteúdo, conclusão, competência e atualização. | Matriz, cursos, avaliações, certificações internas e registros. |

Consulte os recursos oficiais do CIS para confirmar a linguagem e os critérios de avaliação.

