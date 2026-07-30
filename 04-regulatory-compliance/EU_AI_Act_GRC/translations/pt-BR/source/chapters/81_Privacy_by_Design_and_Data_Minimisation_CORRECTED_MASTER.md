# Capítulo 81 Privacidade por Design e Minimização de Dados

** Status legal: ** Corrigido o mestre inglês para consolidação. Este arquivo controla o conflito anterior Capítulo 81 linguagem de rascunho.

## Exigência

Os sistemas de IA que processam dados pessoais devem incorporar princípios de privacidade e proteção de dados em design, desenvolvimento, configuração, implantação, monitoramento e aposentadoria. Os dados pessoais devem ser adequados, relevantes e limitados ao que é necessário para o propósito documentado, enquanto os requisitos de governança, precisão, gerenciamento de riscos e evidências do AI Act são atendidos.

## Explicação em linguagem simples

Mais dados não são automaticamente melhores ou legais. As equipes devem justificar por que cada elemento de dados, recurso, campo alerta, log, anotação e período de retenção é necessário. O design de aprimoramento de privacidade deve ser considerado antes da coleta e antes das alterações do modelo ou do fluxo de trabalho, não adicionado apenas após a implantação.

## Controles de design

A organização deve implementar:

1. Testes de propósito e necessidade documentados para cada elemento de dados pessoais;
2. recurso e revisão proxy-variável;
3. Limites de recolha e retenção;
4. acesso baseado em funções e menos privilégio;
5. pseudonimização, agregação, mascaramento ou dados sintéticos, quando apropriado;
6. separação de dados de treinamento, validação, teste e produção;
7. preservação da privacidade de logs e monitoramento;
8. controles contra memorização, divulgação ou reidentificação não intencionais;
9. fluxos de trabalho de eliminação, correção, restrição e portabilidade, quando aplicável;
10. reavaliação após novas fontes de dados, recursos, atualizações de modelo, integrações ou propósitos.

## Exemplo GlobalWay

O sistema de assistência de viagem da GlobalWay não retém números de passaporte, dados de cartão de pagamento ou informações de saúde em prompts apenas porque esses campos existem em sistemas upstream. A revisão do projeto confirma quais atributos são necessários, mascara valores sensíveis, limita o conteúdo do log e define períodos de retenção alinhados com as necessidades legais e operacionais.

## Atividade de controlo

A Engenharia de Privacidade e a Governança de IA devem aprovar uma revisão de privacidade por design antes do lançamento da produção e após mudanças materiais. A revisão deve documentar a necessidade, a proporcionalidade, as decisões de minimização, as salvaguardas técnicas, os riscos residuais e as trocas não resolvidas.

## Provas

- inventário de dados e mapa de fluxo;
- avaliação de propósito e necessidade;
- Racionalidade de seleção de características;
- cronograma de retenção;
- projeto do acesso-controle;
- pseudonimização ou ocultação de provas;
- resultados dos testes de privacidade;
- Procedimentos de eliminação e tratamento de direitos;
- aprovações de design-revisão e histórico de mudanças.

## Teste de auditoria

Confirme que a necessidade foi documentada, dados excessivos ou obsoletos foram removidos, as salvaguardas funcionam como projetadas e as mudanças materiais desencadearam uma revisão renovada.

## Referências jurídicas primárias

- Regulamento (UE) 2016/679: artigos 5.o, n.o 1, alíneas c), 25.o e 32.o, com outras disposições aplicáveis.
- Regulamento (UE) n.o 2024/1689, alterado: artigos 9.o, 10.o, 12.o, 15.o, 26.o e anexo IV, conforme aplicável.
- Textos EUR-Lex consolidados atuais controlam resumos e rascunhos anteriores.
