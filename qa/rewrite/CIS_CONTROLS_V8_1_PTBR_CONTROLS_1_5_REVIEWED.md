# 6. Controle 1 — Inventário e controle de ativos empresariais

*As 5 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

<img src="media/image4.png" style="width:6.15in;height:3.38991in" alt="Descoberta, conciliação, resposta e revisão mantêm atualizadas as populações fundamentais." />

Figura 4. Ciclo de inventário de ativos e software

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de inventário e controle de ativos empresariais. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 1.1 | Estabelecer e manter um inventário detalhado de ativos empresariais | Manter um inventário completo, atualizado e com responsável definido. | Confirmar escopo, população, responsável, frequência, cobertura, exceções, correção e novo teste. | Inventário de ativos, responsáveis, estado de aprovação, descoberta ativa e passiva, registros DHCP/IPAM e tickets de ativos não autorizados. |
| 1.2 | Tratar ativos não autorizados | Detectar, investigar e remover, isolar ou autorizar formalmente ativos não autorizados. | Verificar que alertas geram ações rastreáveis e tempestivas. | Alertas, tickets, registros de isolamento, autorizações e evidências de encerramento. |
| 1.3 | Utilizar uma ferramenta de descoberta ativa | Executar descoberta ativa para identificar ativos conectados e conciliar os resultados com o inventário. | Confirmar cobertura, programação, exclusões e conciliação. | Configuração de varredura, resultados, inventário atualizado e exceções aprovadas. |
| 1.4 | Utilizar registros DHCP para atualizar o inventário de ativos empresariais | Integrar registros DHCP ao processo de atualização e conciliação do inventário. | Verificar ingestão, frequência, cobertura e tratamento de divergências. | Registros DHCP, integrações, relatórios de conciliação e tickets. |
| 1.5 | Utilizar uma ferramenta de descoberta passiva de ativos | Monitorar tráfego ou telemetria para identificar ativos sem gerar varredura ativa. | Confirmar sensores, segmentos cobertos, alertas e conciliação. | Configuração de sensores, resultados, cobertura de rede e atualizações do inventário. |

Consulte os CIS Controls v8.1 e a CIS Controls Assessment Specification oficiais para confirmar linguagem exata, classe de ativo, função de segurança, Grupo de Implementação, dependências, entradas, operações, medidas, métricas e revisão de procedimentos.

# 7. Controle 2 — Inventário e controle de ativos de software

*As 7 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de inventário e controle de ativos de software. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 2.1 | Estabelecer e manter um inventário de software | Manter um inventário autorizado, atualizado e com responsáveis definidos. | Confirmar escopo, responsável, frequência, cobertura e exceções. | Inventário, versões, responsáveis, estado de suporte e resultados de descoberta. |
| 2.2 | Assegurar que o software autorizado tenha suporte vigente | Identificar software sem suporte e atualizá-lo, substituí-lo ou tratá-lo por meio de exceção aprovada. | Verificar datas de fim de suporte e ações corretivas. | Inventário, boletins de fornecedores, planos de atualização e exceções. |
| 2.3 | Tratar software não autorizado | Detectar e remover, bloquear ou aprovar formalmente software não autorizado. | Confirmar que os achados geram ações rastreáveis. | Alertas, tickets, registros de desinstalação, bloqueios e aprovações. |
| 2.4 | Utilizar ferramentas automatizadas de inventário de software | Automatizar a detecção de software instalado e conciliá-la com o inventário autorizado. | Verificar cobertura, frequência e tratamento de divergências. | Configuração das ferramentas, resultados e relatórios de conciliação. |
| 2.5 | Criar uma lista de software autorizado | Permitir a execução apenas de software aprovado conforme o risco e a necessidade do negócio. | Confirmar política, cobertura, exceções e eventos de bloqueio. | Política de allowlisting, regras, exceções e registros de eventos. |
| 2.6 | Criar uma lista de bibliotecas autorizadas | Restringir bibliotecas e componentes carregados a versões aprovadas. | Verificar regras, cobertura e exceções. | Configuração, inventário de bibliotecas, eventos e aprovações. |
| 2.7 | Criar uma lista de scripts autorizados | Restringir a execução de scripts aos aprovados e controlados. | Confirmar assinatura, regras, cobertura e exceções. | Repositório aprovado, assinaturas, regras de execução e eventos. |

Consulte os recursos oficiais do CIS para confirmar a linguagem e os critérios de avaliação.

# 8. Controle 3 — Proteção de dados

*As 14 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

<img src="media/image5.png" style="width:6.15in;height:3.39605in" alt="Descobrir, classificar, proteger, reter e eliminar dados conforme sua sensibilidade e necessidade." />

Figura 5. Ciclo de vida da proteção de dados

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de proteção de dados. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 3.1 | Estabelecer e manter um processo de gestão de dados | Definir como os dados são identificados, classificados, protegidos, retidos e eliminados. | Confirmar escopo, responsável, revisão e aplicação. | Política, procedimentos, responsáveis e registros de revisão. |
| 3.2 | Estabelecer e manter um inventário de dados | Manter inventário de conjuntos de dados, localização, responsável, sensibilidade e uso. | Verificar cobertura, atualidade e conciliação. | Inventário, catálogos, responsáveis e resultados de descoberta. |
| 3.3 | Configurar listas de controle de acesso a dados | Limitar o acesso a dados de acordo com a necessidade e a autorização. | Revisar permissões, funções, exceções e recertificações. | ACLs, funções, aprovações e revisões de acesso. |
| 3.4 | Aplicar a retenção de dados | Reter dados durante o período aprovado e exigido. | Comparar regras, sistemas e resultados. | Cronograma de retenção, configurações e registros. |
| 3.5 | Eliminar dados de forma segura | Destruir ou apagar dados de modo verificável quando não forem mais necessários. | Confirmar método, cobertura e evidência de eliminação. | Certificados, registros, tickets e testes de apagamento. |
| 3.6 | Criptografar dados em dispositivos de usuários finais | Proteger dados armazenados em dispositivos por meio de criptografia gerenciada. | Verificar cobertura, chaves, exceções e estado. | Console de criptografia, inventário, políticas e exceções. |
| 3.7 | Estabelecer e manter um esquema de classificação de dados | Definir níveis de sensibilidade e regras de tratamento. | Confirmar critérios, aprovação, comunicação e uso. | Esquema, etiquetas, procedimentos e treinamento. |
| 3.8 | Documentar fluxos de dados | Manter diagramas e registros de como os dados são coletados, processados, armazenados e transferidos. | Verificar integridade, atualidade e responsáveis. | Diagramas, registros de tratamento e interfaces. |
| 3.9 | Criptografar dados em mídias removíveis | Exigir criptografia para dados armazenados em mídias removíveis. | Confirmar política, configuração e exceções. | Configuração, inventário de mídias e registros. |
| 3.10 | Criptografar dados sensíveis em trânsito | Proteger comunicações que transportam dados sensíveis. | Revisar protocolos, certificados, cobertura e exceções. | Configuração TLS/VPN, certificados e resultados de testes. |
| 3.11 | Criptografar dados sensíveis em repouso | Proteger dados sensíveis armazenados em bancos, arquivos e cópias de segurança. | Confirmar algoritmos, chaves, cobertura e exceções. | Configuração, KMS/HSM, inventários e testes. |
| 3.12 | Segmentar o processamento e o armazenamento de dados de acordo com a sensibilidade | Separar ambientes e repositórios conforme a classificação e o risco. | Revisar arquitetura, regras e fluxos permitidos. | Diagramas, segmentação, regras e resultados de testes. |
| 3.13 | Implementar uma solução de prevenção contra perda de dados | Detectar e controlar transferências não autorizadas de dados sensíveis. | Verificar cobertura, regras, alertas, exceções e resposta. | Políticas DLP, eventos, tickets e métricas. |
| 3.14 | Registrar o acesso a dados sensíveis | Manter registros suficientes para identificar quem acessou dados sensíveis e quais ações foram realizadas. | Confirmar fontes, detalhamento, retenção e revisão. | Registros de acesso, SIEM, alertas e revisões. |

Consulte os recursos oficiais do CIS para confirmar a linguagem e os critérios de avaliação.

# 9. Controle 4 — Configuração segura de ativos empresariais e software

*As 12 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de configuração segura de ativos empresariais e software. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 4.1 | Estabelecer e manter um processo de configuração segura | Definir, aprovar, implementar e revisar configurações seguras para ativos e software. | Confirmar padrões, responsáveis, frequência, cobertura e exceções. | Padrões, linhas de base, resultados de avaliação e exceções. |
| 4.2 | Estabelecer e manter um processo de configuração segura para a infraestrutura de rede | Aplicar linhas de base seguras a dispositivos e serviços de rede. | Revisar cobertura, mudanças, desvios e correções. | Configurações, backups, comparações e tickets. |
| 4.3 | Configurar o bloqueio automático de sessão em ativos empresariais | Bloquear sessões inativas após o período aprovado. | Verificar política, configuração e cobertura. | GPO/MDM, resultados de consulta e exceções. |
| 4.4 | Implementar e gerenciar um firewall em servidores | Habilitar e gerenciar regras de firewall em servidores. | Revisar cobertura, regras, mudanças e exceções. | Configuração, inventário, regras e registros. |
| 4.5 | Implementar e gerenciar um firewall em dispositivos de usuários finais | Habilitar e gerenciar o firewall local em endpoints. | Confirmar cobertura e estado centralizado. | Console, políticas e relatórios de conformidade. |
| 4.6 | Gerenciar de forma segura ativos empresariais e software | Utilizar protocolos e canais administrativos seguros. | Revisar métodos de administração, autenticação e registros. | Configuração, listas de administradores e registros. |
| 4.7 | Gerenciar contas padrão em ativos empresariais e software | Desabilitar, alterar ou controlar contas padrão. | Confirmar inventário, estado e exceções. | Resultados de varredura, configuração e tickets. |
| 4.8 | Desinstalar ou desabilitar serviços desnecessários | Reduzir a superfície de ataque removendo serviços não exigidos. | Comparar linhas de base, serviços ativos e exceções. | Inventário de serviços, configuração e aprovações. |
| 4.9 | Configurar servidores DNS confiáveis em ativos empresariais | Forçar o uso de resolvedores DNS aprovados. | Verificar configuração, cobertura e desvios. | GPO/MDM, configuração de rede e registros DNS. |
| 4.10 | Aplicar bloqueio automático do dispositivo em equipamentos portáteis de usuários finais | Bloquear dispositivos portáteis após inatividade ou tentativas malsucedidas. | Confirmar política, configuração e cobertura. | MDM, políticas e relatórios. |
| 4.11 | Aplicar capacidade de apagamento remoto em dispositivos portáteis de usuários finais | Permitir apagamento remoto gerenciado quando o risco exigir. | Verificar cobertura, autorização e testes. | Console MDM, procedimentos e registros de testes. |
| 4.12 | Separar espaços de trabalho empresariais em dispositivos móveis de usuários finais | Separar dados e aplicações empresariais dos pessoais. | Revisar perfis, políticas e cobertura. | Configuração MDM/MAM, inventário e relatórios. |

Consulte os recursos oficiais do CIS para confirmar a linguagem e os critérios de avaliação.

# 10. Controle 5 — Gestão de contas

*As 6 Salvaguardas, seu significado claro, o enfoque de verificação e exemplos de evidências.*

| **Finalidade do Controle:** Fortalecer a organização por meio da implementação e medição das Salvaguardas de gestão de contas. |
|---|

| ID | Salvaguarda | Significado claro | Enfoque de verificação | Exemplos de evidências |
|---|---|---|---|---|
| 5.1 | Estabelecer e manter um inventário de contas | Manter uma população completa de contas com responsável, tipo, estado e datas relevantes. | Confirmar cobertura, atualidade, responsáveis e conciliação. | Inventários, diretórios, relatórios e revisões. |
| 5.2 | Utilizar senhas exclusivas | Impedir a reutilização de senhas entre contas gerenciadas. | Revisar política, configuração, exceções e testes. | Política, configuração de identidade e resultados de auditoria. |
| 5.3 | Desabilitar contas inativas | Desabilitar oportunamente contas que ultrapassem o período de inatividade aprovado. | Confirmar limite, execução, exceções e acompanhamento. | Relatórios, tickets, registros e aprovações. |
| 5.4 | Restringir privilégios administrativos a contas administrativas dedicadas | Separar atividades administrativas das contas de uso normal. | Revisar população, privilégios, uso e exceções. | Diretórios, grupos privilegiados, PAM e registros de atividade. |
| 5.5 | Estabelecer e manter um inventário de contas de serviço | Manter responsável, finalidade, dependências, credenciais e revisão para cada conta de serviço. | Confirmar cobertura, rotação, uso e exceções. | Inventário, cofre de segredos, registros de rotação e revisões. |
| 5.6 | Centralizar a gestão de contas | Utilizar sistemas centrais de identidade para criar, alterar, desabilitar e revisar contas. | Verificar integrações, cobertura, processos e divergências. | Diretórios, IAM, fluxos de provisionamento e relatórios de conciliação. |

Consulte os recursos oficiais do CIS para confirmar a linguagem e os critérios de avaliação.

