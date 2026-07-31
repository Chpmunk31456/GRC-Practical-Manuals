# Capítulo 43 Precisão, Robustez, Cibersegurança e Resiliência

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla o conflito anterior Capítulo 43 linguagem de rascunho.

## Exigência

Os sistemas de IA de alto risco devem atingir um nível adequado de precisão, robustez e segurança cibernética e ter um desempenho consistente durante todo o ciclo de vida. O projeto deve abordar erros, falhas, inconsistências, interferência maliciosa, ciclos de feedback e uso indevido razoavelmente previsível à luz do propósito e risco pretendidos.

## Explicação em linguagem simples

A conformidade não requer desempenho perfeito. Requer metas de desempenho defensáveis, testes baseados em risco, limitações transparentes, design seguro, monitoramento e ação corretiva. As métricas devem refletir o contexto real de implantação, em vez de apenas médias de laboratório.

## Áreas de controle necessárias

O provedor deve abordar, conforme aplicável:

1. Métricas de precisão e desempenho definidas ligadas à finalidade pretendida;
2. Limites de aceitação e limites de decisão;
3. subgrupo e desempenho específico do contexto;
4. robustez ao ruído, dados ausentes, mudança de distribuição e falha de componentes;
5. resiliência a erros, falhas, interrupções e falhas de dependência;
6. proteção contra envenenamento de dados, exemplos contraditórios, injeção imediata, manipulação de modelos, extração e acesso não autorizado;
7. desenvolvimento seguro, testes, gerenciamento de vulnerabilidades e controle de mudanças;
8. Riscos de ciclo de feedback para sistemas que continuam aprendendo ou influenciam dados futuros;
9. Retrocesso, degradação, reversão e comportamento de parada segura;
10. monitoramento, resposta a incidentes e gatilhos de ação corretiva.

## Métricas e divulgação

As métricas de precisão e robustez devem ser documentadas no arquivo técnico e instruções de uso quando necessário. As pontuações agregadas não devem ocultar os modos de falha material, as disparidades entre grupos afetados, as condições de operação inseguras ou a incerteza.

## Exemplo GlobalWay

A GlobalWay valida seu sistema de recrutamento usando conjuntos de dados relevantes para o papel e mede padrões falso-positivos e falso-negativos em grupos candidatos relevantes. Também testa informações ausentes, formatos de currículo incomuns, conteúdo rápido malicioso, interrupções do fornecedor, alterações de modelo e procedimentos de reversão.

## Atividade de controlo

O provedor deve aprovar requisitos mensuráveis de desempenho, robustez e segurança cibernética antes de liberar e repetir os testes após mudanças materiais ou ameaças emergentes. O implantador deve monitorar o desempenho do mundo real, manter as condições operacionais necessárias, relatar anomalias graves e suspender o uso quando os limites definidos forem violados.

## Provas

- Requisitos e limiares de desempenho;
- Planos de validação e teste;
- Resultados de subgrupos e casos extremos;
- resultados de robustez e teste de estresse;
- modelo de ameaça e arquitetura de segurança;
- Registros de vulnerabilidade e de testes de penetração;
- Testes de dependência e resiliência;
- dashboards de monitoramento;
- Registros de incidentes e ações corretivas;
- aprovações de liberação e reversão.

## Teste de auditoria

Selecione um sistema de alto risco e verifique se os requisitos de desempenho e segurança estão documentados, os testes refletem o contexto de implantação pretendido, os modos de falha de material são divulgados, vulnerabilidades e anomalias são rastreadas e violações de limiares desencadeiam investigação, correção, restrição ou suspensão.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com as alterações que lhe foram introduzidas: artigo 15.o e respetivas obrigações de ciclo de vida, monitorização e prestador/empregador.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
