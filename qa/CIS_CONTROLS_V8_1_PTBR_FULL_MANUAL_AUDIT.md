# CIS Controls v8.1 Brazilian Portuguese Full-Manual Audit

Target: `01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`

## Result

**FAIL — publication-blocking defects remain**

## Summary

- conversion box glyph: **21**
- double heading marker: **5**
- ellipsis-only table row: **1**
- raw separator line: **5**
- standalone numbered heading without hash: **41**
- unclosed bold heading: **7**
- Missing expected numbered sections: **0**

## Findings

| Category | Line | Excerpt |
|---|---:|---|
| unclosed bold heading | 3 | `**SÉRIE PRÁTICA DE CIBERSEGURANÇA, PRIVACIDADE E CONFORMIDADE**` |
| unclosed bold heading | 5 | `**CIS Critical Security Controls v8.1**` |
| unclosed bold heading | 7 | `**Implementação prática, medição, evidências e ferramentas de código aberto**` |
| unclosed bold heading | 11 | `**Alberto (Al) Leiva**` |
| standalone numbered heading without hash | 54 | `1. Fundamentos dos CIS Controls v8.1` |
| standalone numbered heading without hash | 55 | `2. Grupos de Implementação e priorização` |
| standalone numbered heading without hash | 56 | `3. Governança, escopo e responsabilidades` |
| standalone numbered heading without hash | 57 | `4. Medição com a especificação de avaliação do CIS` |
| standalone numbered heading without hash | 58 | `5. Roteiro de implementação` |
| standalone numbered heading without hash | 60 | `24. Ferramentas de código aberto` |
| standalone numbered heading without hash | 61 | `25. Guia dos CIS Controls para gestores` |
| standalone numbered heading without hash | 62 | `26. Guia profissional para analistas juniores` |
| standalone numbered heading without hash | 63 | `27. Laboratório fictício e portfólio` |
| standalone numbered heading without hash | 64 | `28. Plano de aprendizagem de trinta dias` |
| standalone numbered heading without hash | 65 | `29. Preparação para entrevistas` |
| standalone numbered heading without hash | 66 | `30. Modelos, glossário, índice e referências` |
| standalone numbered heading without hash | 167 | `1. Selecione e documente o Grupo de Implementação inicial e os acréscimos necessários.` |
| standalone numbered heading without hash | 168 | `2. Construa e concilie as populações principais: ativos, software, dados, contas, sistemas de autenticação, redes, fornecedores, aplicações e registros.` |
| standalone numbered heading without hash | 169 | `3. Implemente as Salvaguardas do IG1 com responsáveis, procedimentos, métricas de cobertura, exceções e evidências.` |
| standalone numbered heading without hash | 170 | `4. Proteja identidades e configurações; gerencie vulnerabilidades, e-mail, navegadores, defesas contra malware, cópias de segurança e monitoramento essencial.` |
| standalone numbered heading without hash | 171 | `5. Exercite resposta a incidentes e recuperação antes de uma emergência real.` |
| standalone numbered heading without hash | 172 | `6. Meça cada Salvaguarda aplicável utilizando entradas confiáveis e operações repetíveis.` |
| standalone numbered heading without hash | 173 | `7. Corrija cobertura incompleta e falhas recorrentes; confirme as correções por meio de novos testes.` |
| standalone numbered heading without hash | 174 | `8. Expanda para IG2 ou IG3 conforme o risco, as obrigações, a maturidade e a exposição a ameaças.` |
| standalone numbered heading without hash | 175 | `9. Utilize mapeamentos oficiais para coordenar outras estruturas sem tratar o mapeamento como comprovação automática de conformidade.` |
| unclosed bold heading | 177 | `**Princípio de implementação:** Um conjunto menor de Salvaguardas, com escopo completo, operação consistente, medição e melhoria contínua, é mais defensável do que uma lista extensa marcada como concluída sem evidências ` |
| unclosed bold heading | 595 | `**Limitação crítica:** Uma ferramenta pode apoiar Salvaguardas, mas não escolhe o Grupo de Implementação, não define tolerância ao risco, não garante cobertura completa, não substitui procedimentos ou revisão humana e nã` |
| standalone numbered heading without hash | 697 | `1. O Grupo de Implementação selecionado continua adequado ao risco, aos dados, aos serviços e às obrigações?` |
| standalone numbered heading without hash | 698 | `2. Os inventários essenciais são completos, atuais, atribuídos e conciliados?` |
| standalone numbered heading without hash | 699 | `3. Quais Salvaguardas apresentam cobertura incompleta, revisão atrasada ou dados não confiáveis?` |
| standalone numbered heading without hash | 700 | `4. A exposição de acessos privilegiados, ativos externos, software sem suporte e falhas de recuperação aumentou?` |
| standalone numbered heading without hash | 701 | `5. Alertas resultam em investigação e resposta ou apenas em volume de painel?` |
| standalone numbered heading without hash | 702 | `6. Responsabilidades de prestadores, incidentes, subcontratados e saída estão claras?` |
| standalone numbered heading without hash | 703 | `7. Testes e exercícios são autorizados, adequadamente definidos e acompanhados até o reteste?` |
| standalone numbered heading without hash | 704 | `8. Quais decisões de orçamento, pessoal ou prioridade bloqueiam a correção?` |
| conversion box glyph | 752 | `□---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------` |
| standalone numbered heading without hash | 754 | `1. Crie uma empresa fictícia de 50 pessoas com laptops, servidores, serviços de nuvem, uma aplicação web, pessoal remoto e cinco fornecedores.` |
| standalone numbered heading without hash | 756 | `2. Selecione IG1 e documentar três adições baseadas em risco do IG2 ou IG3.` |
| standalone numbered heading without hash | 758 | `3. Build Enterprise-asset, software, dados, conta, sistema de autenticação, rede, fornecedor, aplicativo e log-source inventários.` |
| standalone numbered heading without hash | 760 | `4. Use Nmap e osquery em um laboratório isolado para conciliar inventários de ativos e software.` |
| standalone numbered heading without hash | 762 | `5. Use OpenSCAP ou Lynis em um host de laboratório; conclusões de configuração do documento, exceções, correções e reavaliação.` |
| standalone numbered heading without hash | 764 | `6. Use Greenbone em alvos de laboratório aprovados; valide cobertura, achados, remediação e rescan.` |
| standalone numbered heading without hash | 766 | `7. Use Wazuh ou Suricata para gerar e investigar um alerta de teste seguro.` |
| standalone numbered heading without hash | 768 | `8. Use Trivy ou ZAP em um repositório de treinamento ou aplicação e corrigir registro e reteste.` |
| standalone numbered heading without hash | 770 | `9. Escreva um teste de backup-restore e incidente registro de mesa.` |
| standalone numbered heading without hash | 772 | `10. Crie cinco trabalhos CIS Assessment Specification com entradas, operações, medidas, métricas, listas de exceções e conclusões.` |
| standalone numbered heading without hash | 774 | `11. Publicar apenas artefatos higienizados e afirmar claramente que o projeto é fictício e não uma avaliação formal CIS.` |
| raw separator line | 777 | `----------------------------------------------------------------------------------------------------------------` |
| conversion box glyph | 778 | `Memorando de seleção □ Priorização e raciocínio de risco` |
| conversion box glyph | 780 | `□ Guardar papel de trabalho ; Estrutura e evidência oficiais de medição` |
| raw separator line | 792 | `------------------------------------------------------------------------------------------------------------------------------------------------------------` |
| conversion box glyph | 793 | `□ 1–4 □ Framework, 18 Controlos, 153 Salvaguardas, IGs, classes de activos, funções` |
| conversion box glyph | 793 | `□ 1–4 □ Framework, 18 Controlos, 153 Salvaguardas, IGs, classes de activos, funções` |
| standalone numbered heading without hash | 803 | `29. Preparação da entrevista` |
| double heading marker | 811 | `# # 29,2 O que é o IG1?` |
| double heading marker | 815 | `# # 29.3 O IG1 se encaixa em todos os requisitos?` |
| double heading marker | 839 | `# # 29.9 Perguntas para perguntar ao empregador` |
| raw separator line | 877 | `--------------------------------------------------------------------------------------------------------------------------------------` |
| double heading marker | 889 | `# # 30.3 Glossário` |
| raw separator line | 892 | `-----------------------------------------------------------------------` |
| conversion box glyph | 893 | `□ Classe de ativos □ Categoria afetada por uma Salvaguarda, como dispositivos, software, dados, rede, usuários ou documentação. □` |
| conversion box glyph | 893 | `□ Classe de ativos □ Categoria afetada por uma Salvaguarda, como dispositivos, software, dados, rede, usuários ou documentação. □` |
| conversion box glyph | 893 | `□ Classe de ativos □ Categoria afetada por uma Salvaguarda, como dispositivos, software, dados, rede, usuários ou documentação. □` |
| conversion box glyph | 894 | `□ CIS Benchmark • Recomendações de configuração segura para uma tecnologia específica.` |
| conversion box glyph | 895 | `Controle CIS □ Uma das 18 áreas de defesa amplas.` |
| conversion box glyph | 896 | `CIS Salvaguarda □ Uma ação focada e implementável dentro de um controle.` |
| conversion box glyph | 897 | `. Cobertura .. Parte da população aplicável na qual a Salvaguarda é devidamente implementada. □` |
| conversion box glyph | 898 | `□ IG1 56 Higiene cibernética essencial` |
| conversion box glyph | 899 | `□ IG2 □ IG1 mais 74 salvaguardas adicionais.` |
| conversion box glyph | 899 | `□ IG2 □ IG1 mais 74 salvaguardas adicionais.` |
| ellipsis-only table row | 900 | `. . . . . .` |
| conversion box glyph | 901 | `□ Medir □ Contagem, lista, data, configuração ou resultado produzidos por operações de avaliação. □` |
| conversion box glyph | 901 | `□ Medir □ Contagem, lista, data, configuração ou resultado produzidos por operações de avaliação. □` |
| conversion box glyph | 901 | `□ Medir □ Contagem, lista, data, configuração ou resultado produzidos por operações de avaliação. □` |
| conversion box glyph | 904 | `• Revisão do procedimento; avaliação manual da existência ou não de um processo necessário e que contenha elementos necessários. □` |
| double heading marker | 907 | `# # 30.4 Índice de assunto` |
| raw separator line | 910 | `---------------------------` |
| conversion box glyph | 916 | `□ Evidências e medições` |
| conversion box glyph | 947 | `**Lembramento final:** Frameworks, mapeamentos, ferramentas, produtos, ameaças, leis, contratos e riscos organizacionais mudam. Confirmar os recursos atuais oficiais e as obrigações aplicáveis antes de uma implementação ` |
| unclosed bold heading | 947 | `**Lembramento final:** Frameworks, mapeamentos, ferramentas, produtos, ameaças, leis, contratos e riscos organizacionais mudam. Confirmar os recursos atuais oficiais e as obrigações aplicáveis antes de uma implementação ` |

## Publication rule

This automated audit is a minimum structural-corruption gate. A PASS does not replace native-language, visual, accessibility, link, or factual review.
