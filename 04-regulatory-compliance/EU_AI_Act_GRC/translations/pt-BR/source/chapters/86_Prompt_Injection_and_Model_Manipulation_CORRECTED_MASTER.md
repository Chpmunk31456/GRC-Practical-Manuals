# Capítulo 86 Injeção e Manipulação de Modelos

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla o conflito anterior Capítulo 86 linguagem de rascunho.

## Exigência

Os sistemas de IA que processam instruções, conteúdo recuperado, saídas de ferramentas, arquivos, conteúdo da web ou dados fornecidos pelo usuário devem implementar controles proporcionados contra injeção rápida, seqestro de instruções, fugas de prisão, manipulação de contexto, execução de ferramentas inseguras e ataques relacionados à manipulação de modelos.

## Explicação em linguagem simples

Um sistema de IA pode tratar o conteúdo hostil como instruções confiáveis. Os controles devem impedir que informações não confiáveis mudem o propósito pretendido do sistema, substituindo salvaguardas, expondo informações confidenciais ou causando ações não autorizadas.

## Requisitos de controlo

Implementar conforme apropriado:

1. Separação de sistema, desenvolvedor, usuário, recuperado e conteúdo gerado por ferramentas;
2. ferramenta de menor privilégio e acesso a dados;
3. Listas de permissões, aplicação de políticas e confirmação de ações;
4. Procedência de conteúdo e rotulagem de confiança;
5. filtragem de entrada e saída com limitações conhecidas documentadas;
6. isolamento ou sandboxing de conteúdo não confiável;
7. aprovação humana para ações consequentes ou irreversíveis;
8. detecção de anomalias, registro de registros, limites de taxa e controles de sessão;
9. Testes contraditórios para injeção direta e indireta;
10. falha segura, reversão, resposta a incidentes e escalada do fornecedor.

## Exemplo GlobalWay

O assistente de viagem da GlobalWay lê descrições externas de hotéis e e-mails. Uma página maliciosa contém instruções ocultas pedindo ao agente para revelar os dados do viajante e alterar uma reserva. O sistema trata o conteúdo externo como não confiável, bloqueia o acesso a dados não relacionados, requer confirmação do usuário para alterações de reserva e registra a tentativa de manipulação.

## Atividade de controlo

Os sistemas habilitados para prompt devem passar por testes documentados de injeção e manipulação antes do lançamento e após o modelo material, pronta, ferramenta, recuperação ou alterações de integração. Caminhos de alto impacto não resolvidos devem bloquear o uso da produção.

## Provas

- arquitetura de prompt e ferramenta;
- design de confiança e privilégio;
- casos de teste e resultados contraditórios;
- política e configuração de filtragem;
- Registros de ação-confirmação;
- registros de ataques e registros de incidentes;
- Remediação e reteste de evidências.

## Teste de auditoria

Selecione sistemas habilitados para prompt e verifique se os cenários de injeção direta e indireta foram testados, os privilégios são limitados, as ações conseqentes exigem autorização apropriada, as tentativas de ataque são detectáveis e a correção foi validada.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com as alterações que lhe foram introduzidas: gestão de riscos, supervisão humana, precisão, robustez, cibersegurança, registo, monitorização e disposições relativas a incidentes.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
