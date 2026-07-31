# Apêndice K ndice de documentação técnica

**Estado legal: **Mestre inglês corrigido. Para provedores de sistemas de IA de alto risco, use esse índice para apoiar a documentação do Artigo 11 e do Anexo IV. Para outros atores ou sistemas, use-o como evidência de governança e não o represente como documentação legal do Anexo IV, a menos que o gatilho legal se aplique.

## Finalidade

Use este índice para organizar, controlar, reconciliar e evidenciar a documentação técnica necessária para explicar o projeto, desenvolvimento, dados, operação, testes, controles de risco, supervisão, monitoramento, mudanças e status de conformidade de um sistema de IA.

O índice deve estar vinculado à versão de produção exata e atualizado antes do lançamento, após mudança material e sempre que os requisitos legais ou de conformidade forem alterados.

## 1. Aplicabilidade e controle de documentos

| Campo | Resposta |
|---|---|
| Sistema/modelo |  |
| ID do inventário |  |
| Pessoa jurídica e papel de ator |  |
| Base jurídica de alto risco |  |
| Propósito pretendido |  |
| Versão/configuração da produção |  |
| Fornecedor/fornecedor |  |
| Aplica-se o anexo IV? |  |
| Rota de conformidade aplicável |  |
| Fonte legal atual e data de aplicação |  |
| Proprietário da documentação |  |
| Repositório/sistema de registo |  |
| Data de versão e revisão do índice |  |

## 2. Passarela do anexo IV, quando aplicável

| Área do anexo IV | Conteúdo Necessário | Referência de documento/evidência | Proprietário | Versão | Estado | Gap/ação |
|---|---|---|---|---|---|---|
| Descrição geral | Nome do sistema, fornecedor, versão, finalidade pretendida, usuários, contexto operacional, interfaces, dependências de hardware/software |  |  |  |  |  |
| Elementos do sistema e processo de desenvolvimento | Decisões de design, métodos, ferramentas, ambientes, arquitetura, componentes, recursos de computação, dependências |  |  |  |  |  |
| Especificações e pressupostos de design | Opções de design, suposições, trade-offs, limitações, uso previsível e uso proibido |  |  |  |  |  |
| Governança de dados e dados | Fontes, origem, coleção, preparação, anotação, qualidade, representatividade, viés, linhagem, retenção |  |  |  |  |  |
| Treinamento, tuning e desenvolvimento | Métodos, parâmetros, execuções, recursos, versionamento, reprodutibilidade |  |  |  |  |  |
| Validação e teste | Métricas, cenários, critérios de aceitação, subgrupo, idioma, acessibilidade, robustez, uso indevido e testes de segurança |  |  |  |  |  |
| Precisão, robustez, segurança cibernética e resiliência | Desempenho, incerteza, estresse, ataque, recuperação, continuidade e evidências de retorno |  |  |  |  |  |
| Supervisão humana | Funções, competência, informação, autoridade, sobreposição, parada, recuo, escalada e evidência de teste |  |  |  |  |  |
| Transparência e instruções | Instruções de uso, limitações, avisos, divulgação, acessibilidade, idioma, informações do usuário |  |  |  |  |  |
| Registo e manutenção de registos | Eventos capturados, retenção, acesso, integridade, vinculação de versão e exportação |  |  |  |  |  |
| Sistema de gestão de riscos | Riscos, cenários, controles, riscos residuais, decisões e atualizações |  |  |  |  |  |
| Sistema de gestão da qualidade | Políticas, procedimentos, propriedade, liberação, fornecedor, incidente, ação corretiva e controle de mudanças |  |  |  |  |  |
| Mudanças predeterminadas e histórico de versões | Plano de mudança aprovado, histórico de lançamento, modificações, reavaliação, reversão |  |  |  |  |  |
| Normas e conformidade | Normas harmonizadas, especificações comuns, rota de conformidade, registos de organismos notificados, declarações, registo, marcação |  |  |  |  |  |
| Monitoramento pós-comercialização | Plano de monitoramento, métricas, limiares, reclamações, incidentes, tendências, ações corretivas |  |  |  |  |  |
| Evidência de fornecedores e componentes | Contratos, cartões de modelo/sistema, atestados, licenças, dependências, avisos de alteração, evidência de auditoria |  |  |  |  |  |
| Inci incidente e remediação | Cronologia de incidentes, notificação, contenção, causa raiz, ação corretiva, validação, lições aprendidas |  |  |  |  |  |

## 3. documentação de apoio à governança

Se relevante, índice:

- aplicabilidade, papel, prática proibida e avaliações de alto risco;
- FRIA, DPIA, governança de dados, segurança, fornecedor e avaliações de risco;
- Registos de controlo e de provas;
- Liberação, risco residual, exceção e aprovações executivas;
- handoff, instruções, treinamento e provas de competência;
- autoridade, organismo notificado, auditor, cliente e correspondência do fornecedor.

## 4. Reconciliação da produção-versão

| Componente de produção | Versão/checksum | Versão da documentação | localização da evidência | Combinado? | Resolução/proprietário |
|---|---|---|---|---|---|
| Modelo |  |  |  |  |  |
| Código do sistema |  |  |  |  |  |
| Instruções do sistema/prompts |  |  |  |  |  |
| Ferramentas/agentes/integrações |  |  |  |  |  |
| Datasets/fontes de recuperação |  |  |  |  |  |
| Configuração/limiares |  |  |  |  |  |
| Interface do usuário/notificações |  |  |  |  |  |
| Configuração de monitoramento/logging |  |  |  |  |  |

Nenhuma liberação pode depender de documentação que descreva um sistema, modelo, conjunto de dados, configuração ou processo de supervisão materialmente diferente.

## 5. Verificações da evidência-qualidade

Para cada item indexado, confirme:

- autêntico e atribuível a um proprietário responsável;
- completo para a finalidade legal aplicável;
- atual, aprovado e vinculado à versão implantada;
- internamente consistente com outra documentação;
- apoiados por evidências de origem e reproduzíveis quando necessário;
- protegido de alterações não autorizadas;
- acessíveis apenas a pessoas autorizadas enquanto disponíveis para auditores, organismos notificados e autoridades, conforme legalmente exigido;
- Recuperável dentro dos prazos necessários;
- retidos sob o cronograma legal, contratual, operacional e legal aplicável;
- disponível na língua e formato requeridos.

## 6. Gaps e decisão de liberação

| Gap | Impacto jurídico/operacional | Controle Interino | Proprietário | Data de vencimento | Validação | Libertador? |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

- [ ] Completo para fins legais aplicáveis
- [ ] Completo com condições aprovadas
- [ ] ndice de governança somente; Anexo IV não aplicável
- [ ] Incompleto liberação ou revisão de conformidade bloqueada
- [ ] Revisão legal ou de conformidade qualificada exigida

Motivo da decisão: **
**Condições abertas:****
**Implicações de conformidade:**

## 7. Mudança e gatilhos de revisão

Atualização após:

- modelo, sistema, código, prompt, ferramenta, dados, limiar ou mudança de infraestrutura;
- propósito pretendido, ator-papel, população, jurisdição ou mudança de produto;
- mudança de fornecedor, componente, licença ou dependência;
- validação, monitoramento, incidente, reclamação ou descoberta de auditoria;
- uso de plano de mudança predeterminado ou modificação substancial;
- conformidade, registro, declaração, marcação, autoridade ou desenvolvimento legal;
- suspensão, reversão, retirada, recall ou aposentadoria.

## Exemplo de GlobalWay Travel Services

A GlobalWay concilia a documentação técnica de um sistema de alocação de funcionários com a produção. A revisão conclui que o modelo de fornecedor implantado e a interface multilíngue diferem das versões documentadas. A liberação permanece bloqueada até que a versão do modelo, testes de dados, instruções de supervisão, avisos de transparência, limiares de monitoramento e evidências de conformidade sejam atualizadas e reconciliadas de forma independente.

## Homologação

| Papel | Nome | Decisão | Data |
|---|---|---|---|
| Fornecedor/proprietário técnico |  |  |  |
| Qualidade/Conformidade |  |  |  |
| Proprietário legal/conformidade |  |  |  |
| Segurança/Dados/Privacidade, conforme aplicável |  |  |  |

**Referências de evidências:**
**Residuais lacunas e restrições:**
Próximo comentário trigger/date:**
**Versão do índice:****

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, conforme alterado: Artigo 11.o, Anexo IV, e disposições aplicáveis de gestão de risco, dados, registo, transparência, supervisão, precisão, robustez, cibersegurança, gestão da qualidade, conformidade, monitorização, incidentes e acesso à autoridade.
- Regulamento (UE) 2026/1744, se aplicável.
- Legislação aplicável do produto anexo I e requisitos de conformidade.
- Textos oficiais consolidados atuais controlam esse índice.
