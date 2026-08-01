# 24. Ferramentas de código aberto

*Links oficiais, inícios seguros, evidências e limitações.*

| Ferramenta | Finalidade | Controles que pode apoiar |
|---|---|---|
| CIS Controls Navigator | Selecionar Grupos de Implementação e consultar mapeamentos oficiais. | Todos |
| CIS Controls Assessment Specification | Aplicar a orientação oficial de medição. | Todos |
| CIS-CAT Lite | Avaliar configurações de benchmarks CIS disponíveis. | 4, 7 |
| CISO Assistant | Gerenciar controles, riscos, evidências e achados. | Todos |
| Wazuh | Monitoramento de endpoints, SIEM, FIM e alertas. | 1, 4, 8, 10, 13, 17 |
| osquery | Consultar ativos, software, contas e configurações. | 1, 2, 4, 5, 8 |
| OpenSCAP | Avaliar configurações seguras em Linux. | 4, 7 |
| Lynis | Auditar segurança de sistemas Linux. | 4, 7 |
| Nmap | Descobrir ativos e serviços autorizados. | 1, 2, 12 |
| Greenbone Community Edition | Avaliar vulnerabilidades. | 7 |
| Trivy | Analisar repositórios, imagens, dependências, segredos e IaC. | 2, 7, 16 |
| OWASP ZAP | Testar aplicações web autorizadas. | 16, 18 |
| Suricata | Detectar intrusões e observar tráfego de rede. | 13 |
| Keycloak | Gerenciar identidade, funções, MFA, sessões e eventos. | 5, 6, 8 |
| DefectDojo | Gerenciar achados, deduplicação, correção e reteste. | 7, 16, 18 |
| Velociraptor | Obter visibilidade de endpoints e apoiar resposta a incidentes. | 1, 8, 13, 17 |

**Limitação crítica:** Uma ferramenta pode apoiar Salvaguardas, mas não escolhe o Grupo de Implementação, não define tolerância ao risco, não garante cobertura completa, não substitui procedimentos ou revisão humana e não comprova conformidade por si só.

## 24.1 CIS Controls Navigator

Projeto oficial: https://www.cisecurity.org/controls/cis-controls-navigator

Use a versão 8.1, selecione o Grupo de Implementação e os mapeamentos necessários e preserve a configuração exportada como evidência.

## 24.2 CIS Controls Assessment Specification

Documentação oficial: https://cas.docs.cisecurity.org/en/latest/

Identifique entradas, premissas, operações, medidas, métricas e revisão de procedimentos para cada Salvaguarda avaliada.

## 24.3 CIS-CAT Lite

Projeto oficial: https://learn.cisecurity.org/cis-cat-lite

Execute somente em sistemas autorizados, preserve o relatório, valide achados, corrija e reavalie.

## 24.4 CISO Assistant

Projeto oficial: https://intuitem.github.io/ciso-assistant-community/

Crie um projeto com escopo definido, atribua responsáveis, anexe evidências e acompanhe achados e ações.

## 24.5 Wazuh

Projeto oficial: https://wazuh.com/

Inscreva endpoints autorizados, gere eventos seguros de teste, confirme coleta e alertas e preserve evidências de cobertura e resposta.

## 24.6 osquery

Projeto oficial: https://www.osquery.io/

Execute consultas somente leitura em laboratório ou ambiente autorizado e compare resultados com inventários aprovados.

## 24.7 OpenSCAP

Projeto oficial: https://www.open-scap.org/

Selecione um perfil apropriado, avalie sistemas autorizados, valide resultados, documente exceções e repita a avaliação.

## 24.8 Lynis

Projeto oficial: https://cisofy.com/lynis/

Audite hosts autorizados, compare os resultados com padrões aprovados e documente correções e novos testes.

## 24.9 Nmap

Projeto oficial: https://nmap.org/

Utilize varreduras limitadas a intervalos autorizados por escrito e preserve escopo, comandos, resultados e conciliação.

## 24.10 Greenbone Community Edition

Projeto oficial: https://greenbone.github.io/docs/latest/

Atualize feeds, utilize alvos autorizados, valide cobertura, corrija achados e execute nova varredura.

## 24.11 Trivy

Projeto oficial: https://trivy.dev/

Analise repositórios ou imagens autorizados, valide achados, documente exceções e repita a análise após correções.

## 24.12 OWASP ZAP

Projeto oficial: https://www.zaproxy.org/

Utilize aplicações de treinamento ou aplicações autorizadas; execute testes ativos somente com aprovação explícita.

## 24.13 Suricata

Projeto oficial: https://suricata.io/

Use sensores autorizados, valide interfaces e regras, gere tráfego de teste aprovado e ajuste alertas com controle de mudanças.

## 24.14 Keycloak

Projeto oficial: https://www.keycloak.org/

Configure um ambiente de laboratório, funções, MFA e eventos e teste cenários de entrada, mudança e saída de usuários.

## 24.15 DefectDojo

Projeto oficial: https://www.defectdojo.org/

Importe resultados autorizados, valide deduplicação, atribua responsáveis e encerre achados somente após reteste confirmado.

## 24.16 Velociraptor

Projeto oficial: https://docs.velociraptor.app/

Utilize apenas ambientes autorizados, limite a coleta ao necessário e proteja os dados obtidos.

# 25. Guia dos CIS Controls para gestores

*Perguntas, indicadores, responsabilidades e decisões que gestores devem controlar.*

1. O Grupo de Implementação selecionado continua adequado ao risco, aos dados, aos serviços e às obrigações?
2. Os inventários essenciais são completos, atuais, atribuídos e conciliados?
3. Quais Salvaguardas apresentam cobertura incompleta, revisão atrasada ou dados não confiáveis?
4. A exposição de acessos privilegiados, ativos externos, software sem suporte e falhas de recuperação aumentou?
5. Alertas resultam em investigação e resposta ou apenas em volume de painel?
6. Responsabilidades de prestadores, incidentes, subcontratados e saída estão claras?
7. Testes e exercícios são autorizados, adequadamente definidos e acompanhados até o reteste?
8. Quais decisões de orçamento, pessoal ou prioridade bloqueiam a correção?

| Área | Pergunta de gestão | Estado sugerido |
|---|---|---|
| Grupo e escopo | Priorização, acréscimos, exclusões e obrigações estão documentados? | Verde, amarelo ou vermelho |
| Inventários | Ativos, software, dados, contas, fornecedores, aplicações e registros estão completos? | Verde, amarelo ou vermelho |
| Proteção | Configuração, acesso, correções, e-mail, malware e proteção de dados funcionam? | Verde, amarelo ou vermelho |
| Detecção | Cobertura de registros e rede é suficiente e alertas são analisados? | Verde, amarelo ou vermelho |
| Recuperação | Backups estão protegidos e restaurações são testadas? | Verde, amarelo ou vermelho |
| Resposta | Papéis, contatos, limiares, exercícios e revisões estão atualizados? | Verde, amarelo ou vermelho |
| Medição | Entradas são confiáveis e exceções são corrigidas? | Verde, amarelo ou vermelho |
| Garantia | Testes, limitações, resultados e retestes são defensáveis? | Verde, amarelo ou vermelho |

# 26. Guia profissional para analistas juniores

*Uma rota prática para funções de controles, vulnerabilidades, garantia, GRC e operações de segurança.*

<img src="media/image10.png" style="width:6.15in;height:3.39605in" alt="Aprender a estrutura, mapear Salvaguardas, medir evidências, relatar lacunas e construir um portfólio honesto." />

Figura 10. Caminho profissional para analistas juniores de CIS Controls

Funções comuns incluem analista júnior de controles de segurança, analista de GRC, analista de gestão de vulnerabilidades, analista de garantia de segurança, analista de operações de segurança, analista de conformidade de TI, analista de risco de terceiros e analista de programa de cibersegurança.

## 26.1 Trabalho júnior típico

- Manter inventários de ativos, software, dados, contas, redes, fornecedores, aplicações, achados e evidências.
- Coletar evidências sem alterar registros de origem e validar a completude da população.
- Relacionar Salvaguardas a responsáveis, sistemas, procedimentos, configurações, métricas, exceções e ações.
- Executar ferramentas autorizadas sob procedimentos aprovados.
- Calcular métricas de cobertura e exceção utilizando a estrutura oficial de avaliação.
- Acompanhar achados até a correção e o reteste.
- Escrever conclusões claras sem exceder o suporte das evidências.

| Competência | Evidência de portfólio |
|---|---|
| Estrutura | Explicar os 18 Controles, Grupos de Implementação, classes de ativos e funções. |
| Inventário | Conciliar duas fontes independentes e explicar diferenças. |
| Medição | Demonstrar entradas, operações, medidas, métrica, exceções e conclusão. |
| Alfabetização técnica | Interpretar configuração, identidade, varredura, registros, recuperação e evidências de aplicação. |
| Correção | Acompanhar responsável, prazo, correção e reteste verificado. |
| Comunicação | Produzir resumo executivo e papel de trabalho detalhado. |
| Ética | Utilizar dados sintéticos, autorização, limites de escopo e alegações honestas. |

