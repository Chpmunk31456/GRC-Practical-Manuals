# Capítulo 97 Risco de Cibersegurança

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla o conflito anterior Capítulo 97 linguagem de rascunho.

## Exigência

As organizações devem identificar, avaliar, mitigar, testar e monitorar os riscos de segurança cibernética que afetam os sistemas de IA, modelos, dados, interfaces, infraestrutura, usuários e serviços dependentes durante todo o ciclo de vida. Os controles devem abordar ameaças de segurança convencionais e caminhos de ataque específicos da IA.

## Explicação em linguagem simples

Os sistemas de IA expandem a superfície de ataque. Os atacantes podem manipular prompts, dados de veneno, evitar a detecção, extrair modelos, roubar credenciais, explorar APIs, comprometer dependências ou induzir ações de ferramentas inseguras. A segurança, portanto, requer controles coordenados entre software, modelos, dados, identidade, infraestrutura, fornecedores e operações.

## Requisitos de avaliação

Avaliar no mínimo:

1. ativos, limites de confiança, usuários, privilégios e fluxos de dados;
2. injeção imediata, injeção imediata indireta, jailbreaks e uso de ferramentas inseguras;
3. envenenamento por dados de treinamento, manipulação de fontes de recuperação e abuso de loop de feedback;
4. exemplos contraditórios, evasão, extração de modelo, inversão e inferência de associação;
5. segredos, credenciais, APIs, plugins, agentes e integrações privilegiadas;
6. confidencialidade, integridade, disponibilidade, autenticidade e resiliência;
7. vulnerabilidades de modelo, biblioteca, contêiner, nuvem e fornecedor;
8. registro, detecção, resposta a incidentes, reversão e preservação de evidências;
9. negação de serviço, exaustão de capacidade e falha de dependência;
10. desenvolvimento seguro, controle de mudanças, patches e divulgação de vulnerabilidades;
11. vazamento de dados, memorização de modelos, filtragem de saída e controle de acesso;
12. mudança de material e gatilhos de reavaliação pós-incidente.

## Exemplo GlobalWay

GlobalWay ameaça-modelos um agente de assistência de viagens que pode ler itinerários e iniciar alterações de reserva. Ele identifica injeção imediata indireta através de conteúdo externo, contas de serviço superprivilegiadas, vazamento de dados sensíveis, plugins maliciosos e interrupções do provedor de modelo. A liberação é bloqueada até que a redução de privilégio, isolamento de conteúdo, confirmação de transação, monitoramento e controles de fallback sejam validados.

## Atividade de controlo

Os sistemas de IA de materiais devem passar por revisão de arquitetura de segurança baseada em risco, modelagem de ameaças, desenvolvimento seguro, testes contraditórios, gerenciamento de vulnerabilidades e verificações de prontidão de incidentes antes da produção e após mudanças significativas. Achados críticos não resolvidos exigem escalada executiva documentada e proibição de liberação, a menos que uma exceção legal e limitada por tempo seja aprovada.

## Provas

- modelo de ameaça e inventário de superfície de ataque;
- arquitetura de segurança e diagramas de fluxo de dados;
- Registros de desenvolvimento seguro e revisão de código;
- scans de vulnerabilidade e inventários de dependência;
- resultados contraditórios e de testes de penetração;
- Evidência de identidade, acesso e gerenciamento de segredos;
- Procedimentos de monitorização e de resposta a incidentes;
- registros de remediação, reteste e fechamento.

## Teste de auditoria

Sistemas de IA de materiais selecionados e verificar se os modelos de ameaça cobrem ataques específicos e convencionais de IA, controles correspondem à arquitetura e privilégios reais, descobertas críticas foram remediadas e retestadas, monitoramento detecta eventos relevantes e mudanças materiais desencadearam reavaliação.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, alterado: disposições aplicáveis em matéria de gestão de riscos, gestão de dados, precisão, robustez, cibersegurança, monitorização, incidentes e GPAI.
- Requisitos aplicáveis em matéria de cibersegurança e sector da União e dos Estados-Membros.
- Textos oficiais consolidados atuais controlam resumos mais antigos.
