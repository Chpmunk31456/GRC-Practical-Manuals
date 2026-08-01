# NIST CSF 2.0 — Reescrita revisada em português brasileiro

## Capítulos 16–24

**Status:** conteúdo-fonte revisado para integração.  
**Idioma:** português brasileiro.  
**Regra editorial:** preservar os identificadores NIST, os nomes próprios das ferramentas, os endereços oficiais e os limites de autorização.

# 16. Ferramentas de código aberto para trabalho com o CSF

*Links oficiais, inícios rápidos seguros, possível apoio ao CSF, evidências e limitações.*

<img src="media/image7_pt-BR.png" style="width:6.15in;height:3.39605in" alt="Autorização, validação, ação corretiva e novos testes transformam resultados técnicos em evidências úteis." />

Figura 7. Do resultado da ferramenta à evidência útil

| **Ferramenta** | **Finalidade** | **Possível apoio ao CSF** |
|---|---|---|
| CISO Assistant | GRC, Perfis, riscos, controles e evidências | GV, ID e relatórios |
| Wazuh | SIEM, monitoramento de endpoints e integridade | DE.CM, DE.AE e RS.MA |
| osquery | Inventário de endpoints e evidências por consultas | ID.AM, PR.PS e PR.AA |
| OpenSCAP | Avaliação de configuração Linux | PR.PS e ID.IM |
| Greenbone Community Edition | Avaliação de vulnerabilidades | ID.RA e ID.IM |
| Trivy | Análise de código, imagens, dependências, segredos e configuração | ID.RA e PR.PS |
| OWASP ZAP | Avaliação autorizada de aplicações web | ID.RA e ID.IM |
| Keycloak | Identidade, funções, autenticação e MFA | PR.AA |
| DefectDojo | Recebimento de achados e acompanhamento de correção | ID.RA, ID.IM e GV.OV |
| Velociraptor | Visibilidade de endpoints e resposta a incidentes | DE.CM e RS.AN |
| Open Policy Agent | Política como código | GV.PO, PR.AA e PR.PS |
| OpenSearch | Busca, análise, painéis e monitoramento de segurança | DE.CM, DE.AE e GV.OV |

## 16.1 Lista de verificação para validação de ferramentas

- Aprovar finalidade, responsável, escopo, dados, sistemas, hospedagem, acesso de suporte e retenção.
- Verificar fonte oficial, versão, dependências, integridade, método de atualização e configuração segura.
- Testar uma condição conhecida que a ferramenta deve detectar ou bloquear.
- Testar uma condição permitida conhecida para identificar falhas desnecessárias.
- Comparar a cobertura com uma população independente de ativos, agentes, repositórios ou identidades.
- Restringir administração, proteger credenciais e relatórios, registrar alterações e testar backup ou recuperação da ferramenta.
- Definir validação humana, escalonamento, exceções, correção e novos testes.
- Revalidar após atualizações relevantes, mudanças de integração ou configuração, ou falhas.

## 16.2–16.13 Orientação comum para as ferramentas

Para CISO Assistant, Wazuh, osquery, OpenSCAP, Greenbone Community Edition, Trivy, OWASP ZAP, Keycloak, DefectDojo, Velociraptor, Open Policy Agent e OpenSearch:

1. Usar somente sistemas próprios ou expressamente autorizados por escrito.
2. Registrar versão, configuração, escopo, população-alvo, data, operador e revisor.
3. Preservar resultados brutos, decisões, exceções, ações corretivas e novos testes.
4. Validar pelo menos uma condição conhecida e uma condição permitida.
5. Não apresentar o resultado de uma ferramenta como certificação, conformidade legal, cobertura completa ou conclusão de auditoria.

### Inícios rápidos revisados

- **CISO Assistant:** criar uma organização fictícia, selecionar cinco resultados do CSF, atribuir responsáveis, anexar evidências higienizadas, registrar uma lacuna e criar um plano de ação.
- **Wazuh:** conectar um endpoint autorizado de laboratório, gerar um evento inofensivo, revisar o alerta e preservar o evento e o ticket.
- **osquery:** consultar usuários, software, serviços, criptografia ou processos em um endpoint de laboratório e registrar consulta, host, horário, saída e revisão.
- **OpenSCAP:** avaliar um Linux autorizado em relação a um perfil apropriado, corrigir uma configuração aprovada e comparar relatórios antes e depois.
- **Greenbone Community Edition:** analisar somente um alvo autorizado, validar um achado, corrigi-lo, executar nova análise e documentar limitações.
- **Trivy:** analisar uma imagem fixada ou repositório de teste, proteger o relatório, validar um resultado, corrigi-lo e repetir a análise.
- **OWASP ZAP:** usar uma aplicação local de treinamento, iniciar com análise passiva e preservar o escopo e os resultados aprovados.
- **Keycloak:** criar um realm de laboratório, usuários, funções e MFA; testar privilégio mínimo, acesso negado e remoção.
- **DefectDojo:** importar um relatório de laboratório, validar e atribuir um achado, registrar a correção, testar novamente e encerrar com evidência.
- **Velociraptor:** usar um cliente isolado, coletar um artefato inofensivo autorizado e registrar finalidade, escopo, revisão e preservação.
- **Open Policy Agent:** escrever uma regra de laboratório que exija responsável, classificação e ambiente aprovado; testar entradas permitidas e negadas.
- **OpenSearch:** carregar eventos sintéticos, criar uma busca e um painel, e documentar cobertura, acesso, retenção e limitações.

## 16.14 Ferramentas oficiais do NIST

- **Ferramenta de referência do CSF 2.0:** explorar e exportar o Núcleo oficial.
- **Perfis Organizacionais:** usar a orientação e os modelos oficiais do NIST.

# 17. Guia prático do CSF para gestores

## 17.1 Perguntas mensais

- O que mudou na missão, sistemas, dados, ameaças, obrigações, fornecedores ou apetite a risco?
- Quais riscos excedem a tolerância e quem tem autoridade para decidir?
- As conclusões do Perfil Atual são sustentadas por evidências confiáveis?
- Quais planos de ação estão atrasados, bloqueados, subfinanciados ou dependem de terceiros?
- Fornecedores críticos são monitorados e incluídos em resposta e recuperação?
- Falhas, incidentes, exercícios, testes e quase incidentes resultaram em melhorias?
- Os serviços críticos conseguem se recuperar dentro dos objetivos aprovados?
- Quais limitações a liderança deve compreender antes de confiar no painel?

## 17.2 Painel

| **Área** | **Pergunta de gestão** | **Status** |
|---|---|---|
| Governança | Estratégia, política, funções, recursos e supervisão estão alinhados ao risco? | Verde / Amarelo / Vermelho |
| Perfil | O escopo está atualizado e o Perfil-Alvo está aprovado? | Verde / Amarelo / Vermelho |
| Risco | Quais riscos residuais excedem a tolerância? | Verde / Amarelo / Vermelho |
| Ativos | Ativos, dados, fluxos e fornecedores críticos são conhecidos? | Verde / Amarelo / Vermelho |
| Proteção | Controles de identidade, dados, plataforma, treinamento e resiliência estão funcionando? | Verde / Amarelo / Vermelho |
| Detecção | O monitoramento é completo, revisado e conectado a critérios de incidente? | Verde / Amarelo / Vermelho |
| Resposta | Incidentes são classificados, analisados, comunicados, contidos e erradicados? | Verde / Amarelo / Vermelho |
| Recuperação | A integridade da restauração e os objetivos de serviço foram comprovados? | Verde / Amarelo / Vermelho |
| Melhoria | Achados foram corrigidos e submetidos a novos testes independentes? | Verde / Amarelo / Vermelho |

## 17.3 Erros comuns

- Tratar o CSF como lista de verificação de TI, e não como trabalho de risco corporativo.
- Começar por ferramentas antes de missão, escopo, risco e resultados.
- Marcar resultados como alcançados apenas porque existe uma política.
- Usar uma única pontuação que oculte fraquezas críticas e diferenças de escopo.
- Chamar os Níveis de níveis de maturidade sem considerar o contexto pretendido pelo NIST.
- Copiar um Perfil-Alvo sem adaptá-lo ao risco da organização.
- Ignorar fornecedores, nuvem, OT, dados, pessoas, instalações e dependências.
- Encerrar achados sem novos testes.
- Descrever alinhamento ao CSF como conformidade legal ou certificação do NIST.

# 18. De iniciante a analista júnior

<img src="media/image8_pt-BR.png" style="width:6.15in;height:3.20335in" alt="Aprender, mapear, testar, relatar e se candidatar com evidências honestas de portfólio." />

Figura 8. Caminho para analista júnior

## 18.1 Funções de entrada

Analista Júnior de GRC; Analista de Risco de Cibersegurança; Analista de Conformidade; Analista de Controles de Segurança; Analista de Risco de Terceiros; Analista de Asseguração de Segurança; Analista de Programa de Cibersegurança; Analista Júnior de Segurança; Analista de Preparação para Auditoria.

## 18.2 Trabalho que um analista júnior pode realizar

- Manter inventários de ativos, dados, sistemas, riscos, obrigações, fornecedores e evidências.
- Coletar e organizar evidências para resultados do CSF com escopo definido.
- Revisar amostras de acesso, vulnerabilidades, treinamento, logs, backups, fornecedores e incidentes.
- Documentar status do Perfil, lacunas, limitações, responsáveis e planos de ação.
- Acompanhar ações corretivas, exceções, aceitações de risco e novos testes.
- Preparar painéis claros sem ocultar incerteza.
- Apoiar exercícios, cronologias de incidentes, lições aprendidas e atualizações de planos.
- Proteger informações confidenciais e respeitar limites de autorização.

## 18.3 Evidências de portfólio

| **Competência** | **Item fictício de portfólio** |
|---|---|
| Escopo | Declaração de escopo e premissas do Perfil |
| Mapeamento do Núcleo | Matriz de aplicabilidade e evidências de todos os resultados |
| Gestão de ativos | Inventário de sistemas, dados, fornecedores e fluxos |
| Risco | Registro com apetite, tolerância, resposta e decisão residual |
| Perfis | Perfis Atual e Alvo com lacunas priorizadas |
| Testes | Planilhas de teste de acesso, vulnerabilidades, backups, logs e fornecedores |
| Resposta a incidentes | Linha do tempo sintética, registro de evidências, comunicação e lições |
| Comunicação executiva | Painel de uma página e declaração executiva de risco |

# 19. Laboratório fictício e portfólio

Harbor Light Services é uma organização fictícia. Toda pessoa, conta, endereço, ativo, evento, registro de cliente e fornecedor é inventado.

- **Projeto 1 — Escopo e contexto:** missão, partes interessadas, obrigações, serviços críticos, dependências, exclusões e responsáveis.
- **Projeto 2 — Mapa de ativos e dados:** inventários e diagrama autorizado de fluxo de dados.
- **Projeto 3 — Risco:** registro de ameaças, vulnerabilidades, probabilidade, impacto, tratamento e risco residual.
- **Projeto 4 — Perfis:** Perfil Atual baseado em evidências e Perfil-Alvo baseado em risco.
- **Projeto 5 — Controles e testes:** testes fictícios de acesso, vulnerabilidades, logs, backups e fornecedores.
- **Projeto 6 — Incidente:** analisar eventos sintéticos, declarar incidente, preservar evidências, conter, erradicar, restaurar e aprender.
- **Projeto 7 — Ferramentas:** usar três ferramentas do Capítulo 16 em laboratório isolado e registrar autorização, versão, escopo, correção e novos testes.
- **Projeto 8 — Relatório executivo:** painel, principais riscos, plano de ação, decisões e limitações.

> **Ética do portfólio:** identificar todo o trabalho como treinamento fictício. Nunca publicar informações reais de empregadores, clientes, pacientes, funcionários, fornecedores, arquiteturas, vulnerabilidades, credenciais ou incidentes sem autorização expressa.

# 20. Plano de aprendizagem de trinta dias

| **Semana** | **Foco** | **Entrega obrigatória** |
|---|---|---|
| 1 | Finalidade do CSF, Núcleo, seis Funções, contexto e ativos | Memorando de escopo, mapa de partes interessadas e inventário de ativos e dados |
| 2 | Risco, Perfis, Níveis, governança e cadeia de suprimentos | Registro de riscos, Perfis Atual e Alvo e classificação de fornecedores |
| 3 | Salvaguardas, monitoramento, resposta, recuperação, evidências e testes | Cinco testes de controle, arquivo de incidente e evidências de recuperação |
| 4 | Ferramentas, relatórios, portfólio e entrevistas | Portfólio higienizado, painel e respostas praticadas |

## 20.1 Hábito diário

Ler uma seção oficial do NIST ou grupo de resultados; explicar em linguagem simples sem alterar o significado; criar uma evidência fictícia; verificar integridade, escopo, data, responsabilidade e confiabilidade; escrever uma conclusão, ação corretiva ou lição.

# 21. Preparação para entrevistas

- **O que é o NIST CSF 2.0?** Um framework flexível e orientado a resultados para compreender, avaliar, priorizar e comunicar risco de cibersegurança por meio do Núcleo, Perfis, Níveis e recursos de apoio.
- **Quais são as seis Funções?** Governar, Identificar, Proteger, Detectar, Responder e Recuperar.
- **Por que Governar foi adicionado?** Para tornar explícitas a responsabilidade da liderança, política, estratégia de risco, integração com ERM, supervisão e risco da cadeia de suprimentos.
- **O que é um Perfil Atual?** Uma descrição dos resultados que um escopo definido alcança ou tenta alcançar atualmente, incluindo como e em que medida.
- **O que é um Perfil-Alvo?** Os resultados priorizados selecionados para um estado futuro conforme missão, risco, obrigações, partes interessadas e recursos.
- **O que são os Níveis?** Contexto para o rigor da governança e gestão do risco: Parcial, Informado pelo Risco, Repetível e Adaptável.
- **O CSF certifica conformidade?** Não. O alinhamento não cria conformidade legal nem certificação do NIST.
- **Como verificar um resultado?** Definir escopo e critérios, avaliar o desenho, obter população completa, amostrar por risco, inspecionar e reproduzir, registrar exceções, corrigir, testar novamente e concluir com evidências.
- **Como as ferramentas devem ser usadas?** Somente com autorização e como uma fonte de evidência; validar cobertura e resultados, proteger saídas, corrigir lacunas e testar novamente.
- **Como priorizar lacunas?** Conforme impacto na missão, ameaça, probabilidade, criticidade, obrigações, exposição, dependências, controles existentes, custo, viabilidade e apetite a risco.

> **Resposta de 60 segundos para gestores:** Uso o CSF 2.0 para conectar cibersegurança ao risco corporativo. Definimos escopo e partes interessadas, selecionamos resultados aplicáveis, construímos Perfis Atual e Alvo, priorizamos lacunas, financiamos planos, testamos evidências operacionais, incluímos fornecedores e comunicamos decisões e limitações. As ferramentas apoiam o trabalho, mas as pessoas continuam responsáveis por escopo, julgamento, correção e risco residual.

# 22. Modelos e listas de verificação

## 22.1 Registro de Perfil

Escopo, finalidade, responsável, patrocinador, partes interessadas, data, gatilho de revisão; identificador de Função, Categoria e Subcategoria; aplicabilidade; status atual; implementação; evidência; teste; exceção; limitação; status-alvo; prioridade; lacuna; risco; ação; proteção provisória; recursos; data; dependência; novo teste; contexto de Nível; aprovação e histórico de versões.

## 22.2 Registro de riscos

Objetivo, ativo, serviço, dados, fornecedor e responsável; ameaça, vulnerabilidade, cenário e resultados afetados; controles e evidências; probabilidade, impacto e risco inerente; resposta, ação, recursos e data; risco residual, comparação com apetite/tolerância e autoridade de aceitação; indicador, gatilho de revisão, vencimento de exceção e novo teste.

## 22.3 Planilha de teste de controle

Resultado, risco, controle, responsável, frequência, sistemas, locais e período; critérios de desenho; evidência esperada; população completa; verificação de completude; método de amostragem; procedimento; evidência inspecionada; reprodução; exceções; causa; impacto; ação; proteção provisória; novo teste; conclusão; limitações; revisor e aprovação.

## 22.4 Revisão de fornecedores

Serviço, responsável, criticidade, acesso, dados, locais, subcontratados, dependências e alternativas; due diligence, autenticidade, desenvolvimento seguro, vulnerabilidades, resiliência, histórico de incidentes e situação financeira/operacional; requisitos contratuais, direitos de evidência, notificação, recuperação, devolução/destruição e saída; monitoramento, achados, exceções, ações, exercícios, incidentes, mudanças, renovação e encerramento.

## 22.5 Lista de preparação para gestores

Patrocinador, funções, recursos, política e estratégia aprovados; escopo, partes interessadas, obrigações, serviços críticos, dependências e fornecedores atualizados; populações reconciliadas; Perfis sustentados e aprovados; plano financiado; evidências testadas; controles de fornecedores operando; métricas ligadas a risco; exceções, aceitações, limitações e novos testes visíveis.

# 23. Glossário e índice temático

**Categoria:** grupo de resultados relacionados dentro de uma Função.  
**Perfil da Comunidade:** linha de base publicada para necessidades compartilhadas de setor, tecnologia, ameaça ou caso de uso.  
**Núcleo:** hierarquia de Funções, Categorias e Subcategorias.  
**Perfil Atual:** resultados que um escopo alcança ou tenta alcançar atualmente.  
**Risco de cibersegurança:** possível efeito da incerteza sobre informação, tecnologia e objetivos organizacionais.  
**Função:** nível mais alto do CSF.  
**Exemplo de Implementação:** ilustração orientada à ação de uma possível forma de apoiar um resultado.  
**Referência Informativa:** mapeamento entre um resultado e outra norma, orientação, regulamentação ou fonte.  
**Perfil Organizacional:** mecanismo para descrever a postura Atual e/ou Alvo.  
**Risco residual:** risco que permanece após considerar controles e respostas.  
**Apetite a risco:** quantidade e tipo amplo de risco que uma organização está disposta a buscar ou reter.  
**Tolerância a risco:** variação aceitável em torno de objetivos específicos.  
**Subcategoria:** resultado específico dentro de uma Categoria.  
**Perfil-Alvo:** resultados selecionados e priorizados que um escopo pretende alcançar.  
**Nível:** contexto do rigor da governança e gestão de riscos.

## 23.1 Índice temático

| **Tema** | **Capítulos** | **Tema** | **Capítulos** |
|---|---:|---|---:|
| Controle de acesso | 6, 15–16, 22 | Métricas | 14, 17 |
| Inventário de ativos | 5, 15, 22 | Ferramentas de código aberto | 16 |
| Preparação para auditoria | 14–15, 22 | Perfis Organizacionais | 2–3, 10 |
| Conformidade | 1, 15 | Proteger | 6 |
| Núcleo | 2, 4–9 | Recuperar | 9 |
| Detectar | 7 | Apetite a risco | 4, 12 |
| Evidências | 14–16 | Avaliação de riscos | 5, 12, 22 |
| Governar | 4, 12–13, 17 | Cadeia de suprimentos | 4, 13, 15, 22 |
| Identificar | 5 | Níveis | 2, 11 |
| Resposta a incidentes | 8, 15, 19 | Verificação | 14–16 |
| Analista júnior | 18–21 | Gestão de vulnerabilidades | 5, 15–16 |

# 24. Referências oficiais e estudos adicionais

- NIST Cybersecurity Framework 2.0 — CSWP 29
- Site oficial do NIST Cybersecurity Framework
- Ferramenta de referência do CSF 2.0
- Perguntas frequentes do CSF 2.0
- Perfis do CSF 2.0
- Referências Informativas do CSF 2.0
- SP 1299 — Guia de recursos e visão geral
- SP 1301 — Guia rápido de Perfis Organizacionais
- SP 1302 — Guia rápido de Níveis
- SP 1303 — Guia rápido de gestão de riscos corporativos
- SP 1300 — Guia rápido para pequenas empresas
- NIST SP 800-53 Rev. 5
- NIST SP 800-61 Rev. 3 — Resposta a incidentes
- NIST SP 800-218 — Secure Software Development Framework
- NIST NICE Workforce Framework

> **Lembrete final:** o Núcleo do CSF é estável, mas Exemplos de Implementação, Referências Informativas, orientações, mapeamentos, ameaças, tecnologias e obrigações podem mudar. Verifique sempre as fontes oficiais atuais do NIST e os requisitos específicos da organização antes de agir.
