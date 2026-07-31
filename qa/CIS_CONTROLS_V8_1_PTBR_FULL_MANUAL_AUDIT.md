# CIS Controls v8.1 Brazilian Portuguese Full-Manual Audit

Target: `01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`

## Result

**FAIL — publication-blocking defects remain**

## Summary

- conversion box glyph: **47**
- double heading marker: **20**
- ellipsis-only table row: **1**
- raw separator line: **8**
- standalone numbered heading without hash: **41**
- unclosed bold heading: **6**
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
| raw separator line | 577 | `----------------------------------------------------` |
| conversion box glyph | 581 | `□ CISO Assistant □ Controles, riscos, evidências e achados` |
| conversion box glyph | 581 | `□ CISO Assistant □ Controles, riscos, evidências e achados` |
| conversion box glyph | 589 | `OWASP ZAP □ Testes de segurança da web autorizados` |
| conversion box glyph | 590 | `□ Suricata □ Detecção de intrusão de rede e visibilidade de tráfego` |
| conversion box glyph | 590 | `□ Suricata □ Detecção de intrusão de rede e visibilidade de tráfego` |
| conversion box glyph | 595 | `Limitação crítica: ** Uma ferramenta pode suportar uma ou mais Salvaguardas, mas não pode escolher o GI da organização, definir tolerância ao risco, garantir cobertura completa, substituir procedimento e revisão humana, ` |
| conversion box glyph | 596 | `□---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------` |
| double heading marker | 598 | `# # 24,1 CIS Controla Navegador` |
| double heading marker | 606 | `# # 24.2 CIS Especificação de Avaliação de Controles` |
| double heading marker | 614 | `# # 24,3 CIS-CAT Lite` |
| double heading marker | 622 | `# # 24.4 Assistente CISO` |
| double heading marker | 638 | `# # 24.6 Osquery` |
| double heading marker | 646 | `# # 24.7 OpenSCAP` |
| double heading marker | 662 | `# # 24.9 Nmap` |
| double heading marker | 670 | `# # 24.10 Greenbone Community Edition` |
| double heading marker | 678 | `# # 24.11 Trivy` |
| double heading marker | 686 | `# # 24.12 OWASP ZAP` |
| double heading marker | 694 | `# # 24.13 Suricata` |
| double heading marker | 702 | `# # 24.14 Keycloak` |
| double heading marker | 710 | `# # 24.15 DefectDojo` |
| double heading marker | 718 | `# # 24.16 Velociraptor` |
| standalone numbered heading without hash | 730 | `1. O GI escolhido ainda é adequado para dados sensíveis, serviços críticos, exposição à ameaça, obrigações, escala e habilidades?` |
| standalone numbered heading without hash | 732 | `2. As populações centrais são completas, atuais, possuídas e reconciliadas com a descoberta independente?` |
| standalone numbered heading without hash | 734 | `3. Quais salvaguardas IG1 têm cobertura incompleta, revisão atrasada, dados de entrada não confiáveis, ou repetidas exceções?` |
| standalone numbered heading without hash | 736 | `4. O acesso administrativo, sistemas expostos externamente, software não suportado, vulnerabilidades críticas e falhas de recuperação aumentaram?` |
| standalone numbered heading without hash | 738 | `5. Os alertas resultam em investigação e resposta, ou apenas no volume do painel?` |
| standalone numbered heading without hash | 740 | `6. As responsabilidades dos prestadores de serviços, as provas, as obrigações em matéria de incidentes, os subcontratantes e os planos de saída estão entendidos?` |
| standalone numbered heading without hash | 742 | `7. Os testes de penetração e os exercícios são autorizados de forma segura, adequadamente explorados, realizados independentemente quando necessário, e seguidos através do reteste?` |
| standalone numbered heading without hash | 744 | `8. Que financiamento, pessoal, tempo de engenharia, ou decisão de negócios está bloqueando correção?` |
| raw separator line | 747 | `-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------` |
| conversion box glyph | 748 | `□ GI e escopo □ Priorização, adições, exclusões e obrigações estão documentadas? Verde / Amarelo / Vermelho` |
| conversion box glyph | 748 | `□ GI e escopo □ Priorização, adições, exclusões e obrigações estão documentadas? Verde / Amarelo / Vermelho` |
| conversion box glyph | 749 | `□ Inventários □ Os ativos, software, dados, contas, fornecedores, aplicativos e logs estão completos? Verde / Amarelo / Vermelho` |
| conversion box glyph | 749 | `□ Inventários □ Os ativos, software, dados, contas, fornecedores, aplicativos e logs estão completos? Verde / Amarelo / Vermelho` |
| conversion box glyph | 750 | `□ Proteção □ A configuração, o acesso, o patching, o email, o malware e os controles de dados estão funcionando? Verde / Amarelo / Vermelho` |
| conversion box glyph | 750 | `□ Proteção □ A configuração, o acesso, o patching, o email, o malware e os controles de dados estão funcionando? Verde / Amarelo / Vermelho` |
| conversion box glyph | 751 | `□ Detecção □ A cobertura de log e rede é completa e os alertas são revistos? Verde / Amarelo / Vermelho` |
| conversion box glyph | 751 | `□ Detecção □ A cobertura de log e rede é completa e os alertas são revistos? Verde / Amarelo / Vermelho` |
| conversion box glyph | 753 | `□ Resposta □ São atuais os papéis, contatos, limiares, exercícios e revisões? Verde / Amarelo / Vermelho` |
| conversion box glyph | 753 | `□ Resposta □ São atuais os papéis, contatos, limiares, exercícios e revisões? Verde / Amarelo / Vermelho` |
| conversion box glyph | 754 | `□ Medição □ Os insumos são confiáveis e as populações de exceção corrigidas? Verde / Amarelo / Vermelho` |
| conversion box glyph | 754 | `□ Medição □ Os insumos são confiáveis e as populações de exceção corrigidas? Verde / Amarelo / Vermelho` |
| double heading marker | 781 | `# # 26.1 Típico trabalho júnior` |
| raw separator line | 798 | `----------------------------------------------------------------------------------------------------------------------------` |
| conversion box glyph | 799 | `□ Framework □ Explique os 18 Controles, IGs, classes de ativos e funções` |
| conversion box glyph | 799 | `□ Framework □ Explique os 18 Controles, IGs, classes de ativos e funções` |
| conversion box glyph | 801 | `□ Medição □ Mostrar entradas, operações, medidas, métrica, lista de exceções e conclusão □` |
| conversion box glyph | 801 | `□ Medição □ Mostrar entradas, operações, medidas, métrica, lista de exceções e conclusão □` |
| conversion box glyph | 801 | `□ Medição □ Mostrar entradas, operações, medidas, métrica, lista de exceções e conclusão □` |
| conversion box glyph | 802 | `□ Alfabetização técnica □ Configuração de intérpretes, identidade, digitalização, log, recuperação e evidência de aplicativos` |
| conversion box glyph | 802 | `□ Alfabetização técnica □ Configuração de intérpretes, identidade, digitalização, log, recuperação e evidência de aplicativos` |
| conversion box glyph | 812 | `□---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------` |
| standalone numbered heading without hash | 814 | `1. Crie uma empresa fictícia de 50 pessoas com laptops, servidores, serviços de nuvem, uma aplicação web, pessoal remoto e cinco fornecedores.` |
| standalone numbered heading without hash | 816 | `2. Selecione IG1 e documentar três adições baseadas em risco do IG2 ou IG3.` |
| standalone numbered heading without hash | 818 | `3. Build Enterprise-asset, software, dados, conta, sistema de autenticação, rede, fornecedor, aplicativo e log-source inventários.` |
| standalone numbered heading without hash | 820 | `4. Use Nmap e osquery em um laboratório isolado para conciliar inventários de ativos e software.` |
| standalone numbered heading without hash | 822 | `5. Use OpenSCAP ou Lynis em um host de laboratório; conclusões de configuração do documento, exceções, correções e reavaliação.` |
| standalone numbered heading without hash | 824 | `6. Use Greenbone em alvos de laboratório aprovados; valide cobertura, achados, remediação e rescan.` |
| standalone numbered heading without hash | 826 | `7. Use Wazuh ou Suricata para gerar e investigar um alerta de teste seguro.` |
| standalone numbered heading without hash | 828 | `8. Use Trivy ou ZAP em um repositório de treinamento ou aplicação e corrigir registro e reteste.` |
| standalone numbered heading without hash | 830 | `9. Escreva um teste de backup-restore e incidente registro de mesa.` |
| standalone numbered heading without hash | 832 | `10. Crie cinco trabalhos CIS Assessment Specification com entradas, operações, medidas, métricas, listas de exceções e conclusões.` |
| standalone numbered heading without hash | 834 | `11. Publicar apenas artefatos higienizados e afirmar claramente que o projeto é fictício e não uma avaliação formal CIS.` |
| raw separator line | 837 | `----------------------------------------------------------------------------------------------------------------` |
| conversion box glyph | 838 | `Memorando de seleção □ Priorização e raciocínio de risco` |
| conversion box glyph | 840 | `□ Guardar papel de trabalho ; Estrutura e evidência oficiais de medição` |
| raw separator line | 852 | `------------------------------------------------------------------------------------------------------------------------------------------------------------` |
| conversion box glyph | 853 | `□ 1–4 □ Framework, 18 Controlos, 153 Salvaguardas, IGs, classes de activos, funções` |
| conversion box glyph | 853 | `□ 1–4 □ Framework, 18 Controlos, 153 Salvaguardas, IGs, classes de activos, funções` |
| standalone numbered heading without hash | 863 | `29. Preparação da entrevista` |
| double heading marker | 871 | `# # 29,2 O que é o IG1?` |
| double heading marker | 875 | `# # 29.3 O IG1 se encaixa em todos os requisitos?` |
| double heading marker | 899 | `# # 29.9 Perguntas para perguntar ao empregador` |
| raw separator line | 937 | `--------------------------------------------------------------------------------------------------------------------------------------` |
| double heading marker | 949 | `# # 30.3 Glossário` |
| raw separator line | 952 | `-----------------------------------------------------------------------` |
| conversion box glyph | 953 | `□ Classe de ativos □ Categoria afetada por uma Salvaguarda, como dispositivos, software, dados, rede, usuários ou documentação. □` |
| conversion box glyph | 953 | `□ Classe de ativos □ Categoria afetada por uma Salvaguarda, como dispositivos, software, dados, rede, usuários ou documentação. □` |
| conversion box glyph | 953 | `□ Classe de ativos □ Categoria afetada por uma Salvaguarda, como dispositivos, software, dados, rede, usuários ou documentação. □` |
| conversion box glyph | 954 | `□ CIS Benchmark • Recomendações de configuração segura para uma tecnologia específica.` |
| conversion box glyph | 955 | `Controle CIS □ Uma das 18 áreas de defesa amplas.` |
| conversion box glyph | 956 | `CIS Salvaguarda □ Uma ação focada e implementável dentro de um controle.` |
| conversion box glyph | 957 | `. Cobertura .. Parte da população aplicável na qual a Salvaguarda é devidamente implementada. □` |
| conversion box glyph | 958 | `□ IG1 56 Higiene cibernética essencial` |
| conversion box glyph | 959 | `□ IG2 □ IG1 mais 74 salvaguardas adicionais.` |
| conversion box glyph | 959 | `□ IG2 □ IG1 mais 74 salvaguardas adicionais.` |
| ellipsis-only table row | 960 | `. . . . . .` |
| conversion box glyph | 961 | `□ Medir □ Contagem, lista, data, configuração ou resultado produzidos por operações de avaliação. □` |
| conversion box glyph | 961 | `□ Medir □ Contagem, lista, data, configuração ou resultado produzidos por operações de avaliação. □` |
| conversion box glyph | 961 | `□ Medir □ Contagem, lista, data, configuração ou resultado produzidos por operações de avaliação. □` |
| conversion box glyph | 964 | `• Revisão do procedimento; avaliação manual da existência ou não de um processo necessário e que contenha elementos necessários. □` |
| double heading marker | 967 | `# # 30.4 Índice de assunto` |
| raw separator line | 970 | `---------------------------` |
| conversion box glyph | 976 | `□ Evidências e medições` |
| conversion box glyph | 1007 | `**Lembramento final:** Frameworks, mapeamentos, ferramentas, produtos, ameaças, leis, contratos e riscos organizacionais mudam. Confirmar os recursos atuais oficiais e as obrigações aplicáveis antes de uma implementação ` |
| unclosed bold heading | 1007 | `**Lembramento final:** Frameworks, mapeamentos, ferramentas, produtos, ameaças, leis, contratos e riscos organizacionais mudam. Confirmar os recursos atuais oficiais e as obrigações aplicáveis antes de uma implementação ` |

## Publication rule

This automated audit is a minimum structural-corruption gate. A PASS does not replace native-language, visual, accessibility, link, or factual review.
