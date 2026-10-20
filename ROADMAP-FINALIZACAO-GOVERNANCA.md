# Roadmap de finalização — GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-ROADMAP-FINAL-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | ROADMAP |
| **Fase** | Finalização do sistema-mestre |
| **Estado** | EM_EXECUCAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — recalcular pelo procedimento da norma antes da aprovação |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-20 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste roadmap |
| **Autoridade superior** | [CONSTITUICAO.md](CONSTITUICAO.md), após ratificação |
| **Padrão aplicável** | [Roadmap padrão](ROADMAP-PADRAO-GOVERNANCA.md); [Carta/Contrato do roadmap](CARTA-CONTRATO-PADRAO-ROADMAP.md); [Norma de estado e percentual](standards/status-e-percentual-de-conclusao.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objetivo e critério global

Finalizar a GOVERNANCA como fonte-mestre única, aprovada, auditável, segura e operacional para os repositórios que adotem formalmente as suas regras.

A conclusão global exige evidência verificável para todos os gates abaixo, resolução ou exceção formal de todos os bloqueios críticos e aprovação explícita de encerramento. A existência de documentação, workflow, teste unitário ou registo de consumidor, isoladamente, não prova operação nem conformidade.

## 2. Painel executivo

- **Estado global:** EM_EXECUCAO — finalização bloqueada por dependências críticas.
- **Último estado scorecard publicado:** 80% comprovados, conforme `registry/status-do-projeto.json`; este roadmap não recalcula nem aumenta o percentual.
- **Fonte de estado:** `registry/status-do-projeto.json`; o README e o SVG devem ser gerados pela automação existente.
- **Bloqueios centrais conhecidos:** distribuição real por PR ainda não demonstrada; credencial de sincronização historicamente rejeitada; catálogo de perfis incompleto; adoção transversal pendente; aceitação operacional WATCHDOG incompleta; documentos fundacionais/políticas em revisão; divergência no estado do consumidor LICITACAO entre `main` e a PR #4.
- **Regra fail-closed:** não habilitar distribuição nem declarar conformidade global sem provas adequadas.

## 3. Roadmap de gates

| Gate | Entregáveis e trabalho | Critério objetivo de saída | Estado |
|---|---|---|---|
| G0 — Baseline e autoridade normativa | Rever Constituição, hierarquia normativa, decisões, políticas, responsáveis e aprovações. Classificar cada documento como proposta, em revisão, aprovado ou obsoleto. | Núcleo normativo coerente; aprovação formal da versão exata dos documentos que constituem autoridade; inventário de decisões e exceções atualizado. | BLOQUEADA — Constituição e várias políticas continuam em revisão. |
| G1 — Distribuição segura | Validar `GOVERNANCA_SYNC_TOKEN` no workflow; executar dry-run autenticado; testar acesso de leitura/escrita por destino; criar/atualizar PRs reais apenas para destinos autorizados; verificar idempotência, isolamento de ficheiros, hashes, relatórios e redação de segredos. | Evidência de workflow real concluído, relatório inspecionado, PRs esperadas criadas/atualizadas, zero destinos indevidos e repetição sem diffs desnecessários. | BLOQUEADA — run #44 foi dry-run; histórico recente inclui falhas de autenticação e distribuição. |
| G2 — Registo de consumidores e adoção | Reconciliar `registry/repositorios-consumidores.json`, PR #4 e critérios de adoção; inspecionar cada espelho, manifestos, hashes, configurações, workflows e evidência individual. | Para cada destino, estado enabled coerente com decisão formal e critérios comprovados; nenhum estado de registo interpretado como certificação. | EM EXECUÇÃO — LICITACAO apresenta divergência entre main e PR #4; demais destinos exigem revisão individual. |
| G3 — Governance Integration Framework | Completar catálogo executável para todos os perfis; definir requisitos semânticos, evidências, severidade, regras de applicability, políticas de modo aplicar, versionamento/ref imutável, relatórios e testes adversariais. | Catálogo com completude demonstrada por perfil; testes unitários, negativos e integração aprovados; relatório correto para PASS/FAIL/UNKNOWN; alteração só por PR; nenhuma certificação implícita. | EM EXECUÇÃO — F1/F2 e baseline estrutural F4 têm validações parciais; catálogo permanece `complete: false`; F5/F6 não concluídas. |
| G4 — Integridade documental | Reconciliar árvore atual de `main` com inventários; verificar cabeçalhos, IDs, links, versões e SHA-256 canónico segundo a norma; corrigir inconsistências sem perda de conteúdo histórico. | Inventário completo e reconciliado com o commit auditado; hashes recalculados; exceções justificadas, aprovadas e rastreáveis. | EM EXECUÇÃO — inventário interno e inventário transversal têm âmbito/fotografias históricas que requerem atualização. |
| G5 — WATCHDOG e operação | Resolver publicação concorrente de workflows; aprovar limites de atualidade por proprietários; configurar monitorização independente, heartbeat, canais de alerta, ACK, escalonamento, responsáveis e SLA; testar falha, recuperação e ausência de monitor. | Execuções atuais demonstram deteção e recuperação; limites aprovados; alertas recebidos e reconhecidos; dependências operacionais sem UNKNOWN crítico ou com exceção formal válida. | BLOQUEADA — aceitação operacional e supervisão independente não comprovadas. |
| G6 — Validação transversal | Executar integração/diagnóstico por cada repositório no commit/ref indicado; validar evidências e relatórios por perfil; registar pendências, exceções, responsável e próxima ação. | Matriz de cobertura completa; todos os destinos classificados com evidência; nenhum resultado UNKNOWN omitido ou promovido a PASS. | PENDENTE — adoção individual ainda incompleta. |
| G7 — Auditoria e fecho | Revisão final independente proporcional ao risco; verificar gates, evidências, hashes, logs, riscos residuais, transferência de conhecimento e relatório final. Obter aprovação explícita de encerramento. | Todos os gates de fecho cumpridos; scorecard sincronizado; aprovação de encerramento registada; 100% apenas quando a norma e a evidência o permitirem. | PENDENTE — os cinco critérios FIM do scorecard estão por comprovar. |

## 4. Ações prioritárias imediatas

1. **A1 — Reconciliar LICITACAO:** verificar o conteúdo de `main` e da PR #4; preservar o princípio fail-closed; só ativar depois da adoção local e da distribuição por PR serem comprovadas.
2. **A2 — Resolver autenticação da distribuição:** o proprietário deve substituir o secret `GOVERNANCA_SYNC_TOKEN` nas definições do repositório por uma credencial válida com privilégios mínimos e acesso explícito a cada destino. Não registar nem expor o valor do secret.
3. **A3 — Executar dry-run explícito e inspecionar artefacto:** confirmar identidade, quantidade de ficheiros, destinos e resultado esperado; parar em qualquer erro.
4. **A4 — Executar teste controlado de PR real:** começar por um consumidor autorizado e de baixo risco; confirmar branch, diff, manifesto, hashes, PR e reexecução idempotente antes de expandir.
5. **A5 — Completar catálogo de perfis:** definir e testar critérios funcionais/semânticos por domínio; manter `complete: false` enquanto faltar qualquer perfil ou critério obrigatório.
6. **A6 — Ratificar documentos fundacionais e operacionais:** rever Constituição e políticas em `EM_REVISAO`; não alterar o estado para aprovado sem aprovação explícita da versão exata.
7. **A7 — Fechar WATCHDOG:** obter decisões dos proprietários sobre atualidade; testar supervisão independente, canais, ACK, escalonamento e recuperação.
8. **A8 — Reconciliar inventários e auditoria de hashes:** auditar a árvore do commit atual, não apenas fotografias históricas; publicar a evidência.
9. **A9 — Executar fecho formal:** atualizar scorecard e painel através da automação canónica, verificar a sincronização e registar revisão/aprovação final.

## 5. Bloqueios, dependências e política de exceções

- **Credencial de sincronização:** dependência manual do proprietário do repositório; o assistente não consegue ler, recuperar ou substituir o valor secreto. A credencial não deve ser enviada no chat nem incluída em logs.
- **Permissões nos consumidores:** a autenticação da fonte não prova permissões de escrita nos destinos. Testar separadamente, sem ampliar desnecessariamente os privilégios.
- **Aprovações normativas:** a criação/revisão de textos não equivale a ratificação. Registar decisor, versão aprovada e data.
- **Aceitação operacional:** workflow verde é apenas uma evidência; não substitui confirmação de entrega de alertas, supervisão externa ou recuperação.
- **Perfis incompletos:** resultados estruturais PASS não equivalem a conformidade funcional. Usar UNKNOWN enquanto a cobertura necessária não existir.
- **Adoção transversal:** cada repositório exige inspeção e aceitação individual. A lista de consumidores é apenas o âmbito de distribuição.
- **Exceções:** toda a exceção deve indicar controlo afetado, justificação, risco, medidas compensatórias, aprovador, validade e condição de revogação. Não pode dispensar obrigação legal ou requisito crítico.

## 6. Evidências de referência

- [Branch principal e árvore do repositório](https://github.com/carlos-andrade/GOVERNANCA/tree/main)
- [Scorecard de estado](registry/status-do-projeto.json)
- [Workflow de propagação](.github/workflows/propagar-regras-governanca.yml)
- [Execução #44 — dry-run concluído](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39506967606)
- [Pull Request #4 — registo pendente do LICITACAO](https://github.com/carlos-andrade/GOVERNANCA/pull/4)
- [Framework — decisão de arquitetura](docs/01-governanca/DEC-GOV-INTEGRATION-FRAMEWORK-001.md)
- [Catálogo de perfis](catalogs/governance-profile-catalog.json)
- [Roadmap de adoção transversal](CABE%C3%87ALHO/ROADMAP-ADOCAO-TRANSVERSAL.md)
- [Roadmap de implementação WATCHDOG](WATCHDOG/roadmap-de-implementacao.md)
- [Norma de estado e percentual](standards/status-e-percentual-de-conclusao.md)

## 7. Histórico de alterações

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | 2026-10-20 | Criação do roadmap de finalização a partir da revisão do estado de `main`, workflows, scorecard e pendências publicadas. |

## 8. Regra de encerramento

A GOVERNANCA só pode ser declarada FINALIZADA quando todos os critérios de saída G0–G7 estiverem comprovados, o scorecard canónico refletir as evidências atuais, os bloqueios críticos estiverem resolvidos ou formalmente excetuados e existir aprovação explícita do encerramento. Até esse momento, manter o estado **EM_EXECUCAO / EM_FINALIZACAO** e a percentagem baseada apenas em evidência.