# 9. Cláusula 6.1.4: Avaliação de impacto de sistemas de IA

*A avaliação de impacto de sistemas de IA examina como um sistema de IA pode afetar indivíduos, grupos e a sociedade ao longo de seu ciclo de vida.*

<img src="../../../assets/English/media/image4.png" style="width:6.15in;height:3.23274in" alt="A ISO/IEC 42005:2025 fornece orientação atual que complementa a ISO/IEC 42001." />

Figura 4. Avaliação de impacto de sistemas de IA

> **Explicação acessível:** A avaliação parte da finalidade e do contexto do sistema, identifica pessoas e grupos afetados, examina benefícios e efeitos adversos diretos, indiretos e sociais, avalia gravidade, escala, duração, reversibilidade e incerteza e converte mitigações em decisões, supervisão, transparência, reparação e monitoramento.

## 9.1 Processo de avaliação de impacto

- Defina gatilhos, escopo, papéis, independência, métodos, participação das partes afetadas, aprovação, retenção, revisão e relação com tratamento de riscos e decisões.
- Descreva finalidade, usuários, pessoas afetadas, decisões/conteúdo, grau de automação, alternativas, dados, modelo, fornecedores, geografia, escala, duração e usos proibidos ou previsíveis.
- Identifique benefícios pretendidos e impactos adversos sobre direitos, equidade, privacidade, segurança funcional, cibersegurança, saúde, acessibilidade, emprego, finanças, crianças/grupos vulneráveis, meio ambiente, cultura, serviços públicos, democracia e condições sociais/econômicas, conforme relevante.
- Considere impactos diretos, indiretos, cumulativos, tardios, reversíveis/irreversíveis, individuais, de grupo e sociais.
- Avalie probabilidade, gravidade, escala, duração, reversibilidade, distribuição, incerteza e opiniões das partes afetadas.
- Selecione mitigações, supervisão humana, avisos, escolhas, reparação, monitoramento, limites e critérios de interrupção; obtenha aprovação responsável.
- Atualize antes de mudanças importantes e após incidentes, reclamações, novas evidências, drift ou expansão do uso.

## 9.2 Avaliação de riscos versus avaliação de impacto

| **Avaliação de riscos** | **Avaliação de impacto** |
|---|---|
| Gerencia incerteza que afeta objetivos, incluindo organização, pessoas e sociedade | Foca especificamente efeitos potenciais de um sistema de IA sobre indivíduos, grupos e sociedade |
| Pode agregar risco de portfólio e processos | Deve permanecer ligada ao sistema/uso específico e ao contexto afetado |
| Alimenta tratamento, controles e aceitação residual | Alimenta projeto, implantação, uso, transparência, supervisão, reparação e monitoramento |
| Ambas devem trocar constatações e permanecer coerentes | Ambas exigem métodos documentados, evidências, decisões e revisão |

# 10. Cláusulas 6.2 e 6.3: Objetivos e planejamento de mudanças

*Os objetivos transformam decisões de política e risco em resultados mensuráveis; mudanças devem ser planejadas e controladas.*

## 10.1 Registro de objetivos

- Objetivo e resultado pretendido, vinculados à política/risco/requisito e ao escopo.
- Medida, cálculo, fonte de dados, população, linha de base, meta, limite, frequência, proprietário, reporte e limitação.
- Ações, recursos, responsabilidades, cronograma, dependências, evidências e método de avaliação.
- Resposta quando o desempenho não atinge a meta; reavaliação quando a métrica cria incentivos prejudiciais.

| **Exemplo de objetivo** | **Medida melhor** |
|---|---|
| Completar inventário de IA | Sistemas ativos com proprietário, uso, dados/modelo/fornecedor, nível de risco, avaliação e status validados ÷ sistemas ativos reconciliados |
| Melhorar tempestividade da avaliação | Mediana e dias vencidos desde admissão/mudança material até decisão aprovada de risco e impacto, por nível |
| Fortalecer avaliação | Sistemas de alto impacto que atendem limites definidos e semelhantes à produção, incluindo subgrupos e falhas graves |
| Melhorar controle de fornecedores | Fornecedores críticos de IA com revisão atual e delimitada, obrigações contratuais, evidências e lacunas materiais encerradas ÷ fornecedores críticos |
| Melhorar remediação | Constatações corrigidas e retestadas quanto à eficácia dentro da meta baseada em risco, com idade e impacto das exceções |

## 10.2 Planejamento de mudanças do SGIA

- Defina finalidade, consequências, integridade do SGIA, recursos, responsabilidades, cronograma, transição, comunicação, evidências e rollback.
- Gatilhos incluem escopo, entidade, produto, uso, modelo, dados, fornecedor, lei, certificação, processo, organização, ferramentas, método de auditoria e objetivos.

# 11. Cláusula 7.1: Recursos

*A organização deve determinar e fornecer os recursos necessários para estabelecer, operar, avaliar e melhorar o SGIA.*

| **Recurso** | **Exemplos** | **Evidência** |
|---|---|---|
| Pessoas | SGIA, domínio, dados, ML, produto, segurança, privacidade, jurídico, segurança funcional, auditoria e fatores humanos | Plano de capacidade, papéis, competência, independência e carga de trabalho |
| Dados | Treinamento/validação/teste/produção, rótulos, metadados, direitos e conjuntos de referência | Inventário, linhagem, qualidade, acesso, retenção e proveniência |
| Ferramentas | Desenvolvimento, anotação, avaliação, monitoramento, segurança e documentação | Inventário aprovado, versões, validação, acesso e suporte |
| Computação/sistema | Nuvem/local/borda, armazenamento, rede, registro, logging e sandbox | Arquitetura, propriedade, capacidade, resiliência e impacto ambiental |
| Finanças/tempo | Orçamento, custo de avaliação, revisão de fornecedores, participação de partes e remediação | Planos, aprovações, realizados, restrições e decisões |

## 11.1 Decisões sobre recursos

- Ajuste a profundidade dos recursos ao escopo, risco, complexidade do sistema, escala, deveres legais e pessoas afetadas.
- Separe desenvolvimento, validação, aprovação e auditoria o suficiente para gerenciar conflitos de interesse.
- Monitore sobrecarga de revisores, cobertura de avaliação, lacunas de dados, limites de fornecedores, licenças vencendo, descontinuação de modelos e dívida técnica.
- Documente restrições aceitas e seu efeito sobre objetivos e risco residual.

# 12. Cláusulas 7.2–7.4: Competência, conscientização e comunicação

*Competência, conscientização e comunicação tornam políticas e controles utilizáveis em decisões reais.*

## 12.1 Competência

- Defina educação, treinamento, habilidade, experiência, independência, comportamento e autoridade necessários por papel e nível de risco.
- Avalie a competência atual; forneça treinamento, mentoria, prática supervisionada, apoio especializado ou realocação.
- Avalie eficácia por observação, revisão do produto de trabalho, exercícios de cenário, testes e resultados — não apenas presença.
- Preserve evidências e reavalie após mudanças de papel, sistema, risco, lei, método ou incidente.

## 12.2 Conscientização

- As pessoas entendem a política, sua contribuição, benefícios de melhoria de desempenho, consequências da não conformidade, canal de preocupações e escalonamento.
- Usuários entendem uso aprovado/proibido, restrições de dados, verificação, supervisão humana, limitações, tratamento de incidentes/reclamações e condições de interrupção.

## 12.3 Plano de comunicação

| **Campo** | **Pergunta** |
|---|---|
| O quê | Política, sistema/uso, limites, impactos, incidentes, resultados, mudanças e deveres |
| Por quê/público | Tomador de decisão, trabalhador, usuário, pessoa afetada, cliente, fornecedor, regulador ou público |
| Quando | Marco do ciclo de vida, intervalo planejado, incidente, reclamação, mudança ou gatilho legal |
| Como | Treinamento, aviso, ficha do sistema, relatório, contrato, painel, reunião ou alerta |
| Proprietário/aprovação | Quem prepara, valida, aprova, entrega e registra? |
| Feedback | Como são tratados dúvidas, acessibilidade, compreensão, preocupações e correção? |

# 13. Cláusula 7.5: Informação documentada

*A informação documentada deve ser controlada o suficiente para ser confiável, localizável, protegida, atual, retida e utilizável.*

## 13.1 Ciclo de vida do controle documental

- Criar/identificar: título, proprietário, ID, versão, data, formato, classificação, escopo, sistema/modelo/dados relacionados e aprovação.
- Revisar/aprovar: revisor competente, conflitos, critérios, comentários, disposição e autorização.
- Publicar/utilizar: público correto, acesso, treinamento, data de vigência, disponibilidade no ponto de uso e retirada de versões obsoletas.
- Alterar: motivo, requisitos/processos/sistemas afetados, aprovações, histórico de versões, transição e rollback.
- Proteger: confidencialidade, integridade, disponibilidade, privacidade, segurança, backup, recuperação e preservação de evidências.
- Reter/descartar: período legal/comercial, retenções, arquivo, exclusão, cópias de fornecedores, dados derivados e verificação.

| **Registros exigidos/importantes** | **Exemplo** |
|---|---|
| Base do SGIA | Contexto, partes interessadas, escopo, política, mapa de processos e papéis |
| Planejamento | Método/avaliação de risco, tratamento, Declaração de Aplicabilidade, processo/registros de impacto, objetivos e mudanças |
| Operações | Inventário de IA, recursos, ciclo de vida, dados, fornecedor/uso, comunicação e incidentes |
| Avaliação | Métricas, análise, auditoria interna e análise crítica pela direção |
| Melhoria | Não conformidade, correção, causa-raiz, ação corretiva e eficácia |
| Rastreabilidade do sistema | Versões de modelo/dados/prompt/ferramenta/configuração, aprovações, avaliações, logs e decisões |

# 14. Cláusula 8.1: Planejamento e controle operacional

*O planejamento operacional transforma requisitos do SGIA em controles repetíveis para admissão, projeto, aquisição, implantação, uso, mudança, incidente e retirada de IA.*

## 14.1 Controle operacional

- Defina critérios e controles para processos; opere-os como planejado; retenha evidências suficientes para demonstrar desempenho.
- Controle mudanças planejadas e revise mudanças não intencionais; reduza efeitos adversos.
- Controle processos, produtos e serviços fornecidos externamente conforme risco e responsabilidade.
- Use níveis de risco e marcos do ciclo de vida para ajustar revisão, independência, testes, aprovação, monitoramento e escalonamento ao impacto.

| **Marco** | **Evidência necessária para a decisão** |
|---|---|
| Admissão | Finalidade, proprietário, papel de IA, pessoas afetadas, dados, fornecedor, risco preliminar e verificação de uso proibido |
| Projeto/aquisição | Requisitos, risco/impacto, arquitetura, recursos, dados, deveres do fornecedor, controles e testes |
| Construção/configuração | Versões, linhagem, desenvolvimento seguro, documentação e prontidão para avaliação |
| Validação | Testes representativos, limites, falhas, contestação independente, limitações e ação corretiva |
| Implantação | Aprovação, condições, informação ao usuário, supervisão, monitoramento, incidente, rollback e suporte |
| Operação/mudança | Desempenho, drift, reclamações, incidentes, mudanças do fornecedor, regressão e reavaliação |
| Retirada | Substituição, comunicação a usuários/partes, acesso, integrações, dados, modelos, registros e exclusão |

# 15. Cláusulas 8.2–8.4: Risco operacional, tratamento e avaliação de impacto

*A organização deve executar avaliação de riscos, tratamento de riscos e avaliação de impacto em intervalos planejados e quando ocorrer mudança significativa.*

## 15.1 Gatilhos operacionais

- Sistema de IA novo ou alterado, uso pretendido, população afetada, geografia, escala, automação, autoridade de decisão, modelo, dados, prompt, ferramenta, integração, fornecedor ou infraestrutura.
- Nova lei, contrato, incidente, reclamação, constatação de auditoria, vulnerabilidade, inteligência de ameaças, preocupação de segurança, drift, falha de avaliação, impacto inesperado ou aviso de fornecedor.
- Mudanças nos critérios de risco, objetivos, controles, monitoramento, propriedade organizacional, escopo de certificação ou capacidade de recursos.

## 15.2 Evidência operacional

- Avaliação atual e aprovada ligada à versão exata de sistema/modelo/dados/configuração/uso.
- Plano de tratamento e Declaração de Aplicabilidade concordam com controles implementados, lacunas, exceções, aprovação residual e monitoramento.
- Avaliação de impacto inclui partes afetadas, efeitos diretos/indiretos e sociais, mitigações, reparação e gatilhos de revisão.
- Ações são integradas a fluxos de produto, dados, segurança, privacidade, fornecedores, usuários, incidentes e mudanças.
- Resultados e mudanças são preservados como informação documentada controlada.

# 16. Cláusula 9.1: Monitoramento, medição, análise e avaliação

*A avaliação de desempenho determina se o SGIA e seus controles alcançam os resultados pretendidos.*

## 16.1 Projeto da medição

- Decida o que monitorar/medir, métodos, momento, responsabilidade, critérios de aceitação, análise, avaliação, reporte e retenção.
- Verifique fontes de dados, definições, populações, completude, precisão, tempo, acesso, transformações e limitações.
- Use indicadores antecedentes e consequentes em governança, risco, impacto, ciclo de vida, dados, fornecedores, uso, reclamações, incidentes, auditoria e melhoria.
- Evite médias que ocultem falhas graves ou efeitos em subgrupos; combine evidências quantitativas e qualitativas.
- Avalie tendências e causas, compare com objetivos e gere decisões/ações quando limites não forem atingidos.

| **Medida do SGIA** | **Decisão habilitada** |
|---|---|
| Cobertura de inventário/controles | Uso de IA desconhecido ou sem proprietário e lacunas de avaliação |
| Idade de risco/impacto e cobertura de mudanças | Se decisões continuam atuais após mudança de sistema/contexto |
| Resultados de avaliação | Liberar, restringir, reprojetar, reverter ou adicionar supervisão |
| Reclamações/incidentes/reparação | Impactos sobre pessoas, recorrência, comunicação e ação corretiva |
| Mudanças/evidências de fornecedores | Reavaliação, ação contratual, alternativa ou saída |
| Idade de auditoria/não conformidade | Fraqueza de controle, causa-raiz, recursos e atenção da direção |
