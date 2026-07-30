# Capítulo 57 Avaliação de Modelo e Teste Adversarial

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla a linguagem de rascunho do capítulo 57 anterior.

## Exigência

Os fornecedores de modelos de IA de uso geral com risco sistêmico devem realizar avaliações de modelo de acordo com protocolos e ferramentas padronizados que reflitam o estado da arte, incluindo testes contraditórios, quando apropriado, para identificar e mitigar riscos sistêmicos.

## Explicação em linguagem simples

A avaliação não é um exercício de benchmark único. O provedor deve testar o que o modelo pode fazer, onde falha, como pode ser mal utilizado, como as salvaguardas podem ser contornadas e se novos lançamentos ou ajuste fino mudam materialmente o risco. Os testes adversos devem incluir tentativas realistas de derrotar controles e expor capacidades perigosas ou não.

## Programa de avaliação

O provedor deve definir:

1. objetivos de avaliação ligados a riscos sistêmicos identificados;
2. capacidade, segurança, robustez, uso indevido e domínios de teste de autonomia;
3. Pontos de avaliação pré-lançamento, pós-lançamento e desencadeados por mudanças;
4. Ensaios independentes ou funcionalmente separados, quando proporcionados;
5. cenários representativos e de teste de stress;
6. Qualificações da equipe vermelha, controles de conflitos e regras de engajamento;
7. critérios de exploração, reprodutibilidade e risco residual;
8. limiares de remediação, reteste e bloqueio de liberação;
9. Manuseio confidencial de descobertas sensíveis;
10. documentação suficiente para supervisão e revisão regulatória.

## Exemplo GlobalWay

Antes de integrar um modelo GPAI de risco sistêmico em sua plataforma de assistência de viagem, a GlobalWay revisa o resumo de avaliação do provedor, testa resistência à injeção imediata, geração prejudicial de documentos de viagem, vazamento de dados sensíveis, orientação de emergência falsa e salvaguardas em torno de conteúdo proibido e registra limitações a jusante e controles de compensação.

## Atividade de controlo

O provedor GPAI deve manter uma avaliação documentada e um programa de testes contraditórios vinculado à governança de liberação. Uma liberação não deve prosseguir onde as descobertas não resolvidas excedem os limiares de risco aprovados ou onde os testes não cobrem riscos sistêmicos identificados.

## Provas

- plano de avaliação e catálogo de testes;
- Racionalidade de referência e cenário;
- relatórios de testes contraditórios;
- Qualificações da equipe vermelha e registros de independência;
- constatações e classificações de gravidade;
- Remediação e reteste de provas;
- decisão de liberação e aprovação de risco residual;
- Resultados de avaliação pós-lançamento.

## Teste de auditoria

Confirme que as avaliações abordaram a avaliação de risco atual, incluíram testes contraditórios realistas, usaram critérios de aceitação definidos, resultaram em correção controlada e foram concluídas antes da aprovação da liberação.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com a redação que lhe foi dada: Artigo 55.o, n.o 1, alínea a).
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
- As orientações aplicáveis da Comissão e do AI Office devem ser identificadas como não vinculativas, a menos que sejam legalmente adotadas.
