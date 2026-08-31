# Manual 22 — Implementação Controlada de Segurança em Nuvem

**Localização controlada pt-BR — tradução não oficial do projeto**  
**Ordem da série:** 22  
**Estado de referência principal atual:** Cloud Security Alliance Cloud Controls Matrix (CCM) v4.1  
**Limite:** Orientação original de implementação. Orientação nativa de provedores serve como evidência de implementação, não substitui lei aplicável, padrões independentes nem a intenção dos controles da CSA. Crosswalks são mapeamentos, não equivalências. Este manual não implica registro, atestação ou certificação CSA STAR.

## 1. Governança de nuvem e modelo operacional
Definir accountability executiva, ownership de segurança em nuvem, responsabilidades de plataforma e aplicações, aceitação de risco, autoridade de arquitetura, onboarding de serviços e hierarquia de políticas. Estabelecer direitos decisórios entre segurança, engenharia de plataforma, aplicações, privacidade, resiliência, compras, finanças e fornecedores. Evidências incluem charter de governança, RACI, políticas, padrões, autoridades de exceção e decisões gerenciais.

## 2. Escopo, tenancy, contas, assinaturas, projetos e landing zones
Manter escopo autorizado de organizações, tenants, grupos de gestão, contas, assinaturas, projetos, pastas, landing zones, regiões, ambientes e responsáveis. Usar provisionamento, nomenclatura e tagging governados para evitar ativos não gerenciados. Evidências incluem inventários, ownership, diagramas hierárquicos, definições de landing zone, estado de ciclo de vida e reconciliação com APIs do provedor.

## 3. Responsabilidade compartilhada e alocação contratual
Documentar responsabilidades por modelo de serviço, implantação, capacidade do provedor, contrato, serviço gerenciado e configuração do cliente. Não depender de matrizes genéricas quando o serviço ou contrato real distribui deveres de forma diferente. Evidências: matrizes, cláusulas, declarações do provedor, obrigações do cliente, lacunas e gatilhos de reavaliação.

## 4. Avaliação de risco em nuvem e registros de decisão de arquitetura
Avaliar riscos considerando sensibilidade de dados, criticidade, caminhos de identidade, exposição à Internet, dependência do provedor, concentração regional, supply chain, resiliência, restrições legais e mudanças operacionais. Registrar decisões materiais e alternativas rejeitadas. Evidências: avaliações, threat models, ADRs, premissas, risco residual e aprovações.

## 5. Federação de identidade, autenticação e acesso privilegiado
Centralizar identidade quando viável, exigir autenticação forte, limitar privilégios, separar planos administrativos, usar elevação temporária quando suportada e revisar acessos de alto risco. Proteger identidades break-glass separadamente. Evidências: configuração de federação, MFA, inventários privilegiados, registros de elevação, revisões e testes de contas de emergência.

## 6. Identidade de workloads e contas de serviço
Governar service accounts, identidades gerenciadas, workload federation, service principals, identidades de API, certificados e credenciais automatizadas. Preferir mecanismos de curta duração ou gerenciados pelo provedor a segredos estáticos. Evidências: inventário, responsável, permissões, idade de credenciais, políticas de confiança, rotação, identidades sem uso e exceções.

## 7. Arquitetura de rede, segmentação, ingresso e egresso
Definir padrões aprovados de rede, segmentação, roteamento, ingresso da Internet, egresso, conectividade privada, endpoints, DNS, acesso administrativo e comunicação entre ambientes. Aplicar conectividade mínima ou deny-by-default quando viável. Evidências: diagramas, matrizes de fluxo, firewalls/security groups, rotas, controles de egresso, testes e exceções.

## 8. Padrões Zero Trust e confiança serviço a serviço
Autenticar e autorizar conexões com identidade verificada, contexto do workload, política e menor privilégio, não apenas localização de rede. Governar service mesh, mTLS, API gateways, proxies conscientes de identidade e pontos de aplicação. Evidências: arquitetura de confiança, identidades, políticas de autorização, certificados, testes e acessos negados.

## 9. Classificação, residência, soberania e ciclo de vida de dados
Classificar dados e mapear onde são criados, armazenados, processados, replicados, copiados, transferidos, arquivados e excluídos. Avaliar residência, soberania, contrato, setor e privacidade conforme a aplicabilidade real. Evidências: inventários, classificações, localizações, rotas de transferência, retenção e decisões aprovadas.

## 10. Criptografia, gestão de chaves, HSMs e segredos
Definir criptografia em repouso e trânsito, ownership de chaves, KMS/HSM, rotação, acesso, segregação de funções, recuperação e gestão de segredos. Evitar segredos de longa duração em código ou templates. Evidências: inventários, políticas, configurações KMS/HSM, secret stores, rotações, logs e exceções.

## 11. Logs, telemetria, trilhas de auditoria e integridade de tempo
Habilitar eventos administrativos, de identidade, rede, dados, workloads, serviços de segurança e plataforma conforme o risco. Proteger logs contra alteração, manter retenção adequada e referências de tempo consistentes. Evidências: padrões, fontes habilitadas, saúde de ingestão, retenção, destinos protegidos, tempo e acessos.

## 12. Engenharia de detecção e monitoramento de ameaças
Criar detecções para abuso de credenciais, escalada de privilégio, API suspeita, recursos expostos, workloads maliciosos, exfiltração, mudanças de política e persistência. Usar ferramentas nativas sem presumir que sua mera ativação constitui controle efetivo. Evidências: regras, cobertura, testes, investigações, tuning e métricas.

## 13. Baselines de configuração e policy as code
Definir baselines seguros e aplicá-los ou avaliá-los por motores de políticas. Separar políticas preventivas, detectivas e consultivas e governar exceções. Evidências: baselines, repositórios, assignments, resultados, implantações bloqueadas, waivers e remediação de drift.

## 14. Infrastructure as Code e controle de drift
Gerenciar infraestrutura por repositórios controlados, revisão, testes, aprovações, pipelines protegidos e histórico de versões. Detectar divergência entre estado declarado e implantado e governar mudanças manuais ou emergenciais. Evidências: repositórios IaC, reviews, pipelines, planos, relatórios de drift e reconciliações.

## 15. Vulnerabilidades, patches, imagens e dependências
Inventariar vulnerabilidades de sistemas, pacotes, imagens, bibliotecas, serviços gerenciados, appliances e dependências. Priorizar por exposição, explorabilidade, criticidade, salvaguardas e responsabilidade do provedor. Evidências: cobertura de scanners, findings, patches, alertas, tickets, exceções, retestes e avisos do provedor.

## 16. Segurança de containers, Kubernetes e orquestração
Proteger clusters, control planes, nós, registries, admission, RBAC, namespaces, network policies, segredos, workloads, imagens e runtime. Separar privilégios de operadores de plataforma e administradores de workloads. Evidências: inventários, baselines, admission policies, proveniência de imagens, revisões RBAC, alertas e remediação.

## 17. Serverless, PaaS, serviços gerenciados e APIs
Aplicar controles específicos a functions, bancos gerenciados, filas, analytics, serviços de IA, APIs e demais PaaS. Governar identidade, exposição, configuração, dados, logging, versionamento, quotas e responsabilidades do provedor. Evidências: inventários, políticas de API, configurações, logs, ajustes de dados e decisões de risco.

## 18. Segurança SaaS e assurance de configuração do tenant
Inventariar tenants SaaS e governar administradores, federação, MFA, compartilhamento, colaboração externa, retenção, integrações, audit logs, aplicações e configurações globais. Evidências: inventário SaaS, revisões de roles, assessments, apps conectados, sharing settings, logs e planos de remediação.

## 19. DevSecOps, CI/CD, assinatura e integridade de build
Proteger repositórios, runners, sistemas de build, identidades de deployment, artefatos, registries e aprovações. Aplicar branch protection, controles de dependência, secret detection, isolamento quando apropriado, assinatura/proveniência e promoção controlada. Evidências: pipelines, access reviews, scans, artefatos assinados, attestations e release records.

## 20. Backup, recuperação, imutabilidade e resiliência a ransomware
Definir cobertura de backup, isolamento, imutabilidade quando apropriado, retenção, estratégias entre contas/regiões, prioridades de restore e separação de credenciais. Testar restauração, não apenas sucesso do job. Evidências: políticas, inventários, restore tests, configurações imutáveis, acessos, tempos observados e remediação.

## 21. Disponibilidade, resiliência regional e domínios de falha
Projetar workloads conforme requisitos de resiliência entre zonas, regiões, serviços, identidades, redes, DNS, dados e terceiros. Identificar single points of failure e premissas de recuperação. Evidências: arquitetura, dependências, failover tests, capacidade, service limits e ações corretivas.

## 22. Resposta a incidentes, forense e preservação de evidências em nuvem
Preparar playbooks para comprometimento de identidade, exposição de dados, workloads maliciosos, ransomware, cryptomining, abuso do control plane e eventos do provedor. Preservar snapshots, logs, histórico de API, identidades e evidência volátil respeitando as capacidades do provedor. Evidências: playbooks, timelines, evidências preservadas, casos com provedor, exercícios e lições aprendidas.

## 23. Inventário, descoberta, ownership e tagging de ativos
Identificar continuamente recursos, ativos efêmeros, endpoints públicos, data stores, chaves, workloads, imagens, integrações SaaS e contas não gerenciadas. Exigir responsável e estado de ciclo de vida. Evidências: feeds de inventário, compliance de tags, recursos órfãos, attestations de ownership e registros de limpeza.

## 24. Risco de terceiros, marketplace e serviços gerenciados
Governar imagens de marketplace, integrações SaaS, MSPs, APIs externas, plugins e componentes de terceiros. Avaliar acesso a dados, privilégios, dependência operacional, suporte, vulnerabilidades, incidentes e exit options. Evidências: registro de fornecedores/componentes, assessments, permissões, contratos, monitoramento e encerramento.

## 25. Assurance de provedores de nuvem e evidência contratual
Coletar assurance proporcional ao risco: relatórios independentes, certificações relevantes, compromissos de serviço, arquitetura, obrigações de incidentes e subprocessadores. Validar escopo e período, sem tratar badges como assurance universal. Evidências: relatórios, mapeamentos, contratos, findings, bridge letters quando aplicável e decisões de revisão.

## 26. Privacidade, registros, retenção e exclusão
Configurar capacidades que suportem obrigações aplicáveis de privacidade e records management, incluindo purpose limitation, acesso, retenção, legal holds, exclusão, exportação e evidência de disposal. Separar capacidade técnica de determinação legal. Evidências: configurações, deletion jobs, holds, privacy assessments e testes do ciclo de vida.

## 27. Interfaces de segurança com custo, capacidade, abuso e governança de recursos
Tratar custos inesperados, exaustão, abuso de quota, cryptomining, denial-of-wallet e provisionamento descontrolado como sinais de segurança ou resiliência quando relevante. Estabelecer budgets, quotas, detecção de anomalias e escalonamento sem confundir governança financeira com controle cibernético. Evidências: thresholds, alertas, capacidade, investigações e ações gerenciais.

## 28. Consistência de controles multi-cloud e híbridos
Definir quais controles são corporativos e quais são específicos de provedor entre cloud, SaaS, on-premises e edge. Normalizar evidências sem ocultar diferenças materiais. Evidências: matriz cross-cloud, padrões de identidade/rede/dados, desvios, cobertura, gaps e planos de migração.

## 29. Métricas, saúde de controles, monitoramento contínuo e exceções
Medir exposição privilegiada, recursos públicos, policy violations, gaps de logging, risco sem patch, identidades obsoletas, falhas de backup, findings e idade de exceções. Evidências: dashboards, fontes, thresholds, tendências, decisões, registros de exceção e remediação.

## 30. Assessment, assurance, testes e amostragem de evidências
Definir escopo, amostragem, validação técnica, revisão de configuração, testes de controle, reliance em controles herdados e interfaces com assessors. Automação pode coletar e testar evidência, mas não cria certificação nem substitui julgamento profissional externo quando ele for genuinamente exigido. Evidências: planos, amostras, workpapers, findings, remediação e retestes.

## 31. Migração, modernização, saída, portabilidade e descomissionamento
Planejar migrações para a nuvem, entre provedores e de saída. Cobrir transferência de dados, identidades, chaves, conversão de configuração, dependências, saída contratual, retenção de evidência e descomissionamento seguro. Evidências: planos, portability tests, reconciliação de inventário, confirmação de exclusão, revogação de acessos e decisões sobre dados residuais.

## 32. Pacote de evidências, roadmap, mudança de fontes e melhoria contínua
Para cada salvaguarda registrar responsável, escopo, procedimento, frequência/gatilho, objeto de evidência, método de teste, findings, remediação e gatilho de reavaliação. Revalidar versão CCM/CAIQ, datas de transição, mapeamentos, orientação relevante do provedor e dependências STAR no release. Congelar o inglês exato antes da localização es-419 e pt-BR; marcar traduções como não oficiais; exigir paridade, geração reproduzível dos seis binários, QA de renderização/acessibilidade, proveniência SHA-256, segurança de workflows, staging exato, publicação do predecessor e reconciliação de catálogo/registro.

## Limite de release controlado
Este manual não estabelece compliance, equivalência legal, certificação do provedor ou status CSA STAR. CCM v4.1 é o estado de referência CSA atual registrado pelo source gate; informações de transição v4.0.x devem ser revalidadas antes do release. Pela regra canônica do repositório, um candidato limpo, com todos os gates objetivos aplicáveis verdes e predecessor publicado, avança sob autorização permanente salvo existência de um assunto especialista específico, documentado e genuinamente não determinístico.