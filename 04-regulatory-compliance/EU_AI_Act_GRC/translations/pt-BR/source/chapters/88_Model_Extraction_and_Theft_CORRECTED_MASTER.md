# Capítulo 88 Extração e Roubo de Modelo

** Status legal: ** Corrigido o mestre inglês para consolidação. Este arquivo controla sobre o conflito anterior Capítulo 88 linguagem de rascunho.

## Exigência

As organizações devem implementar salvaguardas proporcionadas contra cópia de modelos não autorizados, extração, inversão, roubo de peso, divulgação do sistema confidencial e consultas abusivas que possam comprometer a propriedade intelectual, segurança, privacidade, segurança ou conformidade regulamentar.

## Explicação em linguagem simples

Os atacantes podem recriar o comportamento do modelo através de consultas repetidas, roubar pesos ou artefatos, inferir informações de treinamento confidenciais ou explorar o acesso privilegiado. A proteção requer controles técnicos, contratuais, de monitoramento e incidentes compatíveis com o valor e o risco do modelo.

## Requisitos de controlo

Implementar conforme apropriado:

1. acesso mínimo-privilegiado a pesos, pontos de verificação, código, prompts e configuração;
2. autenticação forte, gerenciamento de segredos, criptografia e isolamento do ambiente;
3. Controles de taxa de consulta, volume, padrão e abuso de conta;
4. Detecção de anomalias para extração e comportamento de inversão;
5. Controlos de minimização e de informação de confiança, sempre que justificados;
6. Técnicas de marca d'água, impressão digital, canário ou proveniência, quando eficazes;
7. Controles seguros de distribuição e acesso de fornecedores;
8. monitoramento de funcionários e contratados de acordo com a lei aplicável;
9. preservação, contenção, rotação de credenciais e resposta a violações;
10. escalada legal, contratual e regulatória.

## Exemplo GlobalWay

A GlobalWay opera um modelo proprietário de preços de viagem por meio de uma API. O monitoramento identifica uma conta recém-criada fazendo consultas sistemáticas de limites em alto volume. A conta é limitada e suspensa, os registros são preservados, as credenciais e os caminhos de acesso são revisados e o incidente é avaliado para roubo de modelo, exposição à privacidade e notificação do fornecedor.

## Atividade de controlo

Os proprietários de segurança devem monitorar indicadores de extração, testar controles de acesso privilegiado e manter um manual de incidentes cobrindo artefatos roubados, endpoints expostos e consultas suspeitas.

## Provas

- Classificação de modelos de ativos;
- Registros de controle de acesso e privilégio;
- API e configuração de limite de taxa;
- Regras e alertas de detecção de anomalias;
- resultados dos testes de extração;
- Incidente e registros forenses;
- Evidência de rotação e contenção de credenciais;
- Registros de resposta contratual e legal.

## Teste de auditoria

Selecione modelos de alto valor e verifique se os pesos e artefatos são controlados por acesso, os endpoints são monitorados quanto ao comportamento de extração, a atividade anormal é investigada, os procedimentos de incidentes são testados e o risco residual é documentado.

## Referências jurídicas primárias

- Regulamento (UE) 2024/1689, conforme alterado: segurança cibernética aplicável, robustez, confidencialidade, gerenciamento de riscos, monitoramento, incidentes e disposições de risco sistêmico.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
