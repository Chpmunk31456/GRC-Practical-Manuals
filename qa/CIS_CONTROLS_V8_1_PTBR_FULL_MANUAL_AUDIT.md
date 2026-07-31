# CIS Controls v8.1 Brazilian Portuguese Full-Manual Audit

Target: `01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`

## Result

**FAIL — publication-blocking defects remain**

## Summary

- standalone numbered heading without hash: **39**
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
| standalone numbered heading without hash | 757 | `1. Selecione o IG1 e documente três acréscimos baseados em risco provenientes do IG2 ou IG3.` |
| standalone numbered heading without hash | 758 | `2. Construa inventários de ativos empresariais, software, dados, contas, sistemas de autenticação, redes, prestadores de serviços, aplicações e fontes de logs.` |
| standalone numbered heading without hash | 759 | `3. Utilize Nmap e osquery em um ambiente isolado para reconciliar inventários de ativos e software.` |
| standalone numbered heading without hash | 760 | `4. Utilize OpenSCAP ou Lynis em um host de laboratório e registre achados de configuração, exceções, correções e nova avaliação.` |
| standalone numbered heading without hash | 761 | `5. Utilize Greenbone em alvos aprovados; valide cobertura, achados, remediação e nova varredura.` |
| standalone numbered heading without hash | 762 | `6. Utilize Wazuh ou Suricata para gerar e investigar um alerta de teste seguro.` |
| standalone numbered heading without hash | 763 | `7. Utilize Trivy ou ZAP em um repositório de treinamento ou aplicação de laboratório; registre correção e reteste.` |
| standalone numbered heading without hash | 764 | `8. Execute um teste documentado de restauração de backup e um exercício de mesa de resposta a incidentes.` |
| standalone numbered heading without hash | 765 | `9. Crie cinco papéis de trabalho alinhados à CIS Controls Assessment Specification, incluindo entradas, operações, medidas, métricas, exceções e conclusões.` |
| standalone numbered heading without hash | 766 | `10. Publique somente artefatos higienizados e declare claramente que o projeto é fictício e não constitui uma avaliação formal do CIS.` |
| unclosed bold heading | 897 | `**Lembrete final:** Estruturas, mapeamentos, ferramentas, produtos, ameaças, leis, contratos e riscos organizacionais mudam. Confirme sempre os recursos oficiais atuais e as obrigações aplicáveis antes de implementar, av` |

## Publication rule

This automated audit is a minimum structural-corruption gate. A PASS does not replace native-language, visual, accessibility, link, or factual review.
