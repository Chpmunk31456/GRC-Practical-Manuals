# Apêndice J Plano de Supervisão Humana

** Status legal: ** Mestre inglês corrigido. Este arquivo distingue as funções de design do provedor nos termos do Artigo 14 das funções de deployer para atribuir pessoas naturais competentes e operar o sistema de acordo com as instruções aplicáveis. A supervisão humana deve ser significativa na prática e não pode ser reduzida à aprovação nominal ou revisão pós-fato.

## Finalidade

Use este plano para definir como as pessoas qualificadas entenderão, supervisionarão, desafiarão, desconsiderarão, substituirão, interromperão, pararão, suspenderão e escalarão a operação de um sistema de IA.

O plano deve vincular os objetivos de supervisão, papéis, pontos de decisão, informações, autoridade, competência, carga de trabalho, fallback, evidências, testes, monitoramento e revisão de gatilhos para a versão do sistema aprovada e o propósito pretendido.

## 1. registro de aplicabilidade

| Campo | Resposta |
|---|---|
| Sistema/modelo |  |
| Versão/configuração |  |
| ID do inventário |  |
| Pessoa jurídica e papel de ator |  |
| Classificação de alto risco e base legal |  |
| Propósito pretendido |  |
| Uso real ou proposto |  |
| Usuários e pessoas afetadas |  |
| Instruções do fornecedor revistas |  |
| FRIA/DPIA/avaliação de risco relacionada |  |
| Fonte legal atual e data de aplicação |  |
| Plano proprietário/data/versão |  |

## 2. Objetivos de supervisão

Definir a supervisão dos riscos destinada a prevenir ou reduzir, incluindo:

- resultados inseguros ou ilegais;
- viés de automação e excesso de confiança;
- Saídas imprecisas, não confiáveis, discriminatórias ou manipuladas;
- uso fora do propósito pretendido ou da população aprovada;
- falha em reconhecer a incerteza, comportamento anormal, deriva ou limitações do modelo;
- Ação autônoma ou uso inadequado de ferramentas;
- Incidente atrasado, reclamação ou resposta de escalada;
- incapacidade das pessoas afetadas para obter revisão humana, correção, recurso ou remédio;
- retorno inadequado durante interrupções, ataques, falhas de fornecedores ou condições inesperadas.

## 3. Medidas de supervisão concebidas pelo fornecedor

Capacidades de projeto de registro que permitem que pessoas naturais:

- compreender capacidades relevantes, limitações, suposições e uso indevido previsível;
- permanecer ciente de viés de automação e limites de desempenho;
- interpretar corretamente as saídas no contexto;
- Aceder a dados relevantes, informações de origem, indicadores de confiança ou de incerteza sempre que sejam significativos e ações anteriores;
- Desconsiderar, ignorar, reverter ou corrigir saídas;
- Prevenir ou aprovar ações externas;
- interromper ou interromper a operação com segurança;
- detectar anomalias, deriva, mau uso e condições anormais;
- aumentar incidentes, preocupações com direitos, riscos de segurança e falhas de controle;
- Use logs, explicações, informações de versão e evidências necessárias para revisão.

| Medida | Proprietário do projeto | Recurso ou procedimento do sistema | Versão | Evidência de ensaio | Limitação |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 4. modelo operacional do deployer

| Papel | Responsabilidades | Autoridade de decisão | Competência requerida | Carga/tempo de trabalho | Backup Backup | rota de escalação |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Confirme que o pessoal de supervisão:

- São pessoas naturais;
- Ter competência, formação, autoridade, independência, tempo, ferramentas e apoio necessários;
- compreender a finalidade pretendida, instruções, limitações e riscos relevantes;
- pode substituir ou parar o sistema sem retaliação ou pressão de desempenho conflitantes;
- Ter acesso a especialistas e contatos de emergência;
- não são atribuídas cargas de trabalho que tornam impossível uma revisão significativa;
- são apoiados por alternativas e arranjos de continuidade.

## 5. Pontos de decisão e intervenções

| Passo do ciclo de vida/processo | Saída ou ação de IA | Revisão humana necessária | Informação disponível | Método Override/stop | limiar de escala | Evidência criada |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Inclua aprovação de pré-lançamento, operação em tempo real, exceções, recursos, resposta a incidentes, reversão, restauração e aposentadoria, quando aplicável.

## 6. Informações disponíveis aos revisores

Os revisores de confirmação recebem:

- propósito pretendido, uso aprovado e uso proibido ou restrito;
- contexto de entrada e saída;
- informações relevantes sobre fonte, recuperação, ferramenta e ação;
- indicadores de confiança, incerteza, abstenção ou alerta quando significativos;
- precisão conhecida, viés, subgrupo, idioma, acessibilidade, segurança e limitações de robustez;
- Critérios legais, políticos e de decisão aplicáveis;
- substituições prévias, desentendimentos, incidentes, reclamações e recursos;
- instruções para desafio, correção, substituição, suspensão, parada, escalada e recuo;
- versão e informações de alteração;
- rotas de contato e suporte.

## 7. Autoridade, independência e incentivos

Documento se os revisores podem:

- Reverter ou corrigir a saída;
- exigir provas adicionais ou uma segunda revisão;
- adiar ou recusar uma decisão;
- Obter aconselhamento jurídico, técnico, clínico, de RH, de segurança ou de domínio;
- Parar, suspender, reverter ou isolar o sistema;
- escalar sem retaliação;
- dissidência recorde e incerteza não resolvida;
- proteger as pessoas afetadas enquanto a investigação prossegue.

Avalie se as metas de produção, métricas de velocidade, pessoal, incentivos ou pressão de gerenciamento prejudicam a revisão significativa.

## 8. Controles de Automation-bias

Use controles proporcionados, tais como:

- análise independente antes de apresentar a recomendação de IA;
- apresentação encenada de evidências de origem e saída de IA;
- Racionalidade obrigatória para aceitação e substituição em decisões materiais;
- Revisão de qualidade randomizada;
- rotação do revisor e revisão de segundo nível;
- Alertas para altas taxas de aceitação ou baixas taxas de substituição;
- treinamento baseado em cenários e exercícios de desafio;
- Separação das metas de produção de medidas de supervisão-qualidade;
- monitoramento de desentendimentos, apelo e padrões de reversão;
- Testes cegos periódicos do julgamento do revisor.

## 9. Competência e treinamento

| Tópico formação/competência | Audiência | Frequência | Evidência de conclusão | Teste de competência | Acionador de atualização |
|---|---|---|---|---|---|
| Propósito e limitações |  |  |  |  |  |
| Interpretação e incerteza |  |  |  |  |  |
| Vieses de automação |  |  |  |  |  |
| Riscos de direitos, segurança, privacidade e discriminação |  |  |  |  |  |
| Sobreride, stop, fallback e escalada |  |  |  |  |  |
| preservação de incidentes e evidências |  |  |  |  |  |
| Acessibilidade e comunicação pessoa afetada |  |  |  |  |  |

A conclusão do treinamento por si só não demonstra competência. Use observação, simulação, testes e evidências de desempenho.

## 10. Override e procedimento de escalada

1. Identificar a saída questionável, ação ou condição operacional.
2. Prevenir ou conter danos imediatos e usar o fallback aprovado quando necessário.
3. Preservar entradas, saídas, prompts, ferramentas, versões, logs, decisões e contexto relevantes.
4. Aplicar o processo alternativo ou manual aprovado.
5. Registrar a decisão do revisor, evidências, lógica e incerteza.
6. Notificar as pessoas afetadas ou funções responsáveis quando necessário.
7. Escalar materiais, repetidos, sistêmicos, legais, de segurança, direitos ou questões de segurança.
8. Incidente de gatilho, risco, mudança, fornecedor, notificação ou processos de ação corretiva quando necessário.
9. Validar a remediação e restauração antes que a operação normal seja retomada.
10. Comunique resultados e lições aprendidas.

## 11. Validação

Teste:

- compreensão do propósito e limitações do sistema pelo revisor;
- Acesso às informações necessárias;
- autoridade para desconsiderar, substituir, interromper, parar e escalar;
- Eficácia técnica dos mecanismos de substituição e paragem;
- Queda manual e continuidade;
- carga de trabalho, pessoal, fadiga e tempo de resposta;
- resistência ao viés de automação e pressão de gerenciamento;
- suporte linguístico e de acessibilidade;
- detecção de condições anormais, uso indevido, deriva e incerteza;
- escalada e eficácia de resposta a incidentes;
- criação e recuperação de provas.

| Cenário de teste | Critérios de aceitação | Resultado | Defeito | Proprietário | Evidência de reteste |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 12. Monitorização

Faixa:

- taxas de aceitação, substituição, correção e reversão;
- discordância dos revisores e resultados de segunda revisão;
- tempo para revisão e escalada;
- excepcionalmente alta confiança ou baixas taxas de desafio;
- defeitos de qualidade, falsos positivos, falsos negativos e abstenções;
- diferenças de subgrupo, idioma, deficiência e acessibilidade;
- reclamações, recursos, remédios e resultados da pessoa afetada;
- carga de trabalho do revisor, fadiga, rotatividade e lacunas de pessoal;
- Formação e estatuto de competência;
- Intervenções fracassadas, paradas falhas e falhas de fallback;
- Repetir problemas após a ação corretiva.

| Indicador | Lim limiar | Fonte | Frequência | Proprietário | Acção necessária |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 13. Falha e recuo

Documento:

- Suspensão segura e critérios de paragem;
- Processo manual ou alternativo;
- Contatos de emergência e especialistas;
- arranjos de continuidade, recuperação e restauração;
- preservação de evidências;
- comunicação a pessoas, clientes, trabalhadores ou autoridades afetados;
- restrições durante a operação degradada;
- aprovação e validação necessárias antes da restauração.

## 14. Decisão

- [ ] Projeto de supervisão e modelo operacional aprovado
- [ ] Aprovado com condições
- [ ] Apenas piloto restrito
- [ ] Remediação e reteste necessários
- [ ] Implantação bloqueada ou suspensa
- [ ] Revisão legal ou especializada qualificada necessária

Motivo da decisão: **
** Limitações residuais:**
**Condições e restrições:**
Ações abertas e datas de vencimento: **

## 15. gatilhos de revisão

Reavaliar após:

- modelo, dados, prompt, ferramenta, agente, interface, limiar ou mudança de fluxo de trabalho;
- Finalidade pretendida, população, jurisdição ou mudança de automação;
- Instrução do fornecedor ou alteração do fornecedor;
- pessoal, carga de trabalho, competência, incentivo ou mudança de autoridade;
- Incidente, reclamação, recurso, resultado adverso ou intervenção fracassada;
- desempenho, viés, linguagem, acessibilidade ou deriva de segurança;
- modificação substancial, reclassificação ou mudança legal.

## Exemplo de GlobalWay Travel Services

O assistente de interrupção de viajante da GlobalWay recomenda ações de remarcação e reembolso. O plano de supervisão requer um consultor de viagens para confirmar mudanças sensíveis à segurança e todas as ações financeiras externas. Os consultores recebem contexto do itinerário, regras do fornecedor, avisos de incerteza e ações de ferramentas anteriores. O monitoramento detecta taxas de aceitação extraordinariamente altas durante o clima severo. A GlobalWay reduz a carga de trabalho, adiciona revisão independente para ações de alto impacto, treina novamente a equipe e bloqueia a execução automática até que os testes de substituição e escalada passem.

## Homologação

| Papel | Nome | Decisão | Data |
|---|---|---|---|
| Fornecedor/proprietário técnico |  |  |  |
| Deployer/proprietário do negócio |  |  |  |
| Proprietário Supervisão |  |  |  |
| Legal/Conformidade |  |  |  |
| Risco/Privacidade/Segurança/AR, conforme aplicável |  |  |  |

**Referências de evidências:**
** Limitações residuais:**
Próximo comentário trigger/date:**
Versão do plano:****

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com as alterações que lhe foram introduzidas: Artigo 14.o e fornecedor, implementador, gestão de riscos, transparência, registo, monitorização, incidente, ação corretiva e disposições de autoridade aplicáveis.
- Regulamento (UE) 2026/1744, se aplicável.
- Emprego aplicável, igualdade, acessibilidade, privacidade, segurança, proteção ao consumidor e direito do setor.
- Textos oficiais consolidados atuais e controle de instruções do provedor sobre este modelo.
