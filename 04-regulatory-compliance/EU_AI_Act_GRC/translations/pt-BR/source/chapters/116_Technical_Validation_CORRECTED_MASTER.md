# Capítulo 116 Validação técnica

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla o conflito anterior Capítulo 116 linguagem de rascunho.

## Exigência

Os fornecedores de sistemas de IA de alto risco devem estabelecer e documentar a validação e os testes adequados ao propósito e aos riscos pretendidos do sistema, incluindo as informações exigidas pelo artigo 11 e pelo anexo IV e os requisitos de desempenho, robustez, segurança cibernética e supervisão humana aplicáveis ao sistema. Outras organizações que desenvolvem, adquirem, integram ou implantam sistemas de IA materiais devem aplicar validação técnica proporcional antes da liberação e após a mudança material, para que possam demonstrar que a configuração de produção opera dentro dos limites aprovados e que suas próprias funções operacionais podem ser cumpridas.

## Explicação em linguagem simples

A Lei de IA da UE não impõe um procedimento de validação universal em todos os sistemas e atores de IA. O dever exato depende da classificação e do papel. Para sistemas de IA de alto risco, os provedores devem manter o gerenciamento de risco, documentação técnica, testes, precisão, robustez, segurança cibernética e evidência de gerenciamento de qualidade. Os agentes e outros atores da cadeia de valor precisam de evidências de validação suficientes para usar o sistema de acordo com instruções, supervisão de exercícios, operação de monitoramento e reavaliar alterações. A validação não deve testar apenas a produção real, a produção do laboratório.

## Requisitos de validação

O plano de validação deve abordar, conforme aplicável:

1. o ator regulamentado, a classificação, o propósito pretendido e o gatilho legal;
2. sistema, modelo, dados, prompt, ferramenta, software, firmware e versão de configuração;
3. mau uso e condições operacionais razoavelmente previsíveis;
4. precisão, robustez, confiabilidade, consistência e limites de erro;
5. dados de teste representativos e contextualmente apropriados e métricas de desempenho;
6. Subgrupo, acessibilidade e desempenho específico do contexto, quando relevante;
7. Supervisão humana, superação, parada, escalada e controles de falha segura;
8. Segurança cibernética, abuso, vazamento, manipulação e resistência à dependência;
9. registro, rastreabilidade, monitoramento, captura de evidências e vinculação de versão;
10. integração, latência, disponibilidade, failover e comportamento de modo degradado;
11. Critérios de aceitação, limitações não resolvidas, ação corretiva e risco residual;
12. revisão independente e decisão de liberação autorizada.

## Exemplo GlobalWay

A GlobalWay valida um sistema de recomendação de interrupção de viagens usando dados equivalentes à produção, condições de rede degradadas, itinerários incomuns, entradas multilíngues, cenários de ultrapassagem humana e simulações de falha do fornecedor. Ele registra as funções do provedor e do implantador, a versão de produção testada, instruções aplicáveis, limitações, critérios de aceitação, desvios não resolvidos e a base para a liberação.

## Atividade de controlo

Um sistema de IA de alto risco não deve ser liberado por seu provedor até que os requisitos aplicáveis de gerenciamento de risco, documentação, teste, conformidade e gerenciamento de qualidade sejam satisfeitos. A GlobalWay não deve colocar nenhum sistema de IA material em produção até que obtenha e avalie evidências de validação suficientes para seu papel real, uso pretendido, responsabilidades de supervisão e risco. As mudanças materiais exigem reavaliação proporcional e, quando aplicável, revalidação e atividade de conformidade renovada.

## Provas

- Avaliação legal-função e classificação;
- Plano de validação aprovado;
- versão e registro de configuração;
- dados de teste, justificativa de representatividade e descrição do ambiente;
- métricas, resultados de testes, logs e registros de defeitos;
- critérios de aceitação, limitações e exceções;
- Revisão e aprovação independentes;
- Provas de conformidade e de libertação, se aplicável;
- Registros de monitoramento e revalidação pós-lançamento.

## Teste de auditoria

Confirme que a validação cobriu a versão de produção real, correspondeu ao ator e à classificação, usou dados e métricas apropriados, testou riscos legais e operacionais relevantes, limitações e desvios documentados e vinculou os resultados às decisões de conformidade, liberação, monitoramento e reavaliação, conforme aplicável.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com a redação que lhe foi dada, incluindo os artigos 9.o-15.o, 16.o, 26.o, 43.o, 72.o e o anexo IV, conforme aplicável.
- Regulamento (UE) n.o 2026/1744, sempre que as suas alterações afectem os requisitos, datas de aplicação ou procedimentos pertinentes.
- Normas harmonizadas aplicáveis e especificações comuns, quando legalmente disponíveis e relevantes; caso contrário, não devem ser descritas como leis vinculativas apenas porque são referências de validação úteis.
- O texto consolidado atual do EUR-Lex controla resumos e rascunhos mais antigos.
