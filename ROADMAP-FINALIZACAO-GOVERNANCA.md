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
| **SHA-256 (conteúdo canónico)** | 1bb8a67028db068182be0f9b5633a54e1bfdd775c2a5f0c413284209b4408a82 |
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
- **Bloqueios centrais conhecidos:** distribuição real por PR ainda não demonstrada; credencial de sincronização validada no dry-run, mas permissões de escrita e abertura de PR ainda não testadas; catálogo de perfis incompleto; adoção transversal pendente; aceitação operacional WATCHDOG incompleta; documentos fundacionais/políticas em revisão; a PR #4 foi integrada em 2026-10-20 (commit `a212d6bf8e26c0b26b7035926a01d2300a1c76b3`) e LICITACAO permanece `enabled: false` em `main`.
- **Regra fail-closed:** não habilitar distribuição nem declarar conformidade global sem provas adequadas.

## 3. Roadmap de gates

| Gate | Entregáveis e trabalho | Critério objetivo de saída | Estado |
|---|---|---|---|
| G0 — Baseline e autoridade normativa | Rever Constituição, hierarquia normativa, decisões, políticas, responsáveis e aprovações. Classificar cada documento como proposta, em revisão, aprovado ou obsoleto. | Núcleo normativo coerente; aprovação formal da versão exata dos documentos que constituem autoridade; inventário de decisões e exceções atualizado. | BLOQUEADA — Constituição e várias políticas continuam em revisão. |
| G1 — Distribuição segura | Autenticação do `GOVERNANCA_SYNC_TOKEN` validada nos runs #45/#46; executar o modo real por PR num único consumidor autorizado e testar acesso de escrita; criar/atualizar PRs reais apenas para destinos autorizados; verificar idempotência, isolamento de ficheiros, hashes, relatórios e redação de segredos. | Evidência de workflow real concluído, relatório inspecionado, PRs esperadas criadas/atualizadas, zero destinos indevidos e repetição sem diffs desnecessários. | BLOQUEADA — runs #45 e #46 validaram autenticação e dry-run sem erros; a credencial foi aceite, mas nenhum dos runs criou PRs reais. |
| G2 — Registo de consumidores e adoção | Reconciliar `registry/repositorios-consumidores.json`, PR #4 e critérios de adoção; inspecionar cada espelho, manifestos, hashes, configurações, workflows e evidência individual. | Para cada destino, estado enabled coerente com decisão formal e critérios comprovados; nenhum estado de registo interpretado como certificação. | EM EXECUÇÃO — LICITACAO está agora disabled em main até adoção validada; PR #4 continua aberta e desatualizada face ao estado atual, devendo ser reconciliada/fechada sem reativar o destino; demais destinos exigem revisão individual. |
| G3 — Governance Integration Framework | Completar catálogo executável para todos os perfis; definir requisitos semânticos, evidências, severidade, regras de applicability, políticas de modo aplicar, versionamento/ref imutável, relatórios e testes adversariais. | Catálogo com completude demonstrada por perfil; testes unitários, negativos e integração aprovados; relatório correto para PASS/FAIL/UNKNOWN; alteração só por PR; nenhuma certificação implícita. | EM EXECUÇÃO — F1/F2 e baseline estrutural F4 têm validações parciais; catálogo permanece `complete: false`; F5/F6 não concluídas. |
| G4 — Integridade documental | Reconciliar árvore atual de `main` com inventários; verificar cabeçalhos, IDs, links, versões e SHA-256 canónico segundo a norma; corrigir inconsistências sem perda de conteúdo histórico. | Inventário completo e reconciliado com o commit auditado; hashes recalculados; exceções justificadas, aprovadas e rastreáveis. | EM EXECUÇÃO — inventário interno e inventário transversal têm âmbito/fotografias históricas que requerem atualização. |
| G5 — WATCHDOG e operação | Resolver publicação concorrente de workflows; aprovar limites de atualidade por proprietários; configurar monitorização independente, heartbeat, canais de alerta, ACK, escalonamento, responsáveis e SLA; testar falha, recuperação e ausência de monitor. | Execuções atuais demonstram deteção e recuperação; limites aprovados; alertas recebidos e reconhecidos; dependências operacionais sem UNKNOWN crítico ou com exceção formal válida. | BLOQUEADA — aceitação operacional e supervisão independente não comprovadas. |
| G6 — Validação transversal | Executar integração/diagnóstico por cada repositório no commit/ref indicado; validar evidências e relatórios por perfil; registar pendências, exceções, responsável e próxima ação. | Matriz de cobertura completa; todos os destinos classificados com evidência; nenhum resultado UNKNOWN omitido ou promovido a PASS. | PENDENTE — adoção individual ainda incompleta. |
| G7 — Auditoria e fecho | Revisão final independente proporcional ao risco; verificar gates, evidências, hashes, logs, riscos residuais, transferência de conhecimento e relatório final. Obter aprovação explícita de encerramento. | Todos os gates de fecho cumpridos; scorecard sincronizado; aprovação de encerramento registada; 100% apenas quando a norma e a evidência o permitirem. | PENDENTE — os cinco critérios FIM do scorecard estão por comprovar. |

## 4. Ações prioritárias imediatas

1. **A1 — Reconciliar LICITACAO:** o registo foi corrigido em `main` para `enabled: false` no commit `31ec179bb267ece9ee92663110189d75821df2be`. A PR #4 deve ser encerrada ou atualizada de modo que não reintroduza um estado divergente; não ativar LICITACAO até adoção local validada.
2. **A2 — Validar escrita e executar PR piloto:** a credencial `GOVERNANCA_SYNC_TOKEN` foi aceite nos dry-runs #45/#46 para a identidade `carlos-andrade`. O próximo passo é executar manualmente o workflow com `dry_run=false` para um único consumidor de teste autorizado, confirmar permissões de escrita nesse destino e verificar a PR resultante. Não registar nem expor o valor do secret.
3. **A3 — Dry-run concluído:** runs #45 e #46 confirmam autenticação para `carlos-andrade`, 78 ficheiros descobertos, 8 consumidores ativos e zero erros; os resultados foram `WOULD_OPEN_PR`. Falta o teste real controlado.
4. **A4 — Executar teste controlado de PR real:** começar por um consumidor autorizado e de baixo risco; confirmar branch, diff, manifesto, hashes, PR e reexecução idempotente antes de expandir.
5. **A5 — Completar catálogo de perfis:** definir e testar critérios funcionais/semânticos por domínio; manter `complete: false` enquanto faltar qualquer perfil ou critério obrigatório.
6. **A6 — Ratificar documentos fundacionais e operacionais:** rever Constituição e políticas em `EM_REVISAO`; não alterar o estado para aprovado sem aprovação explícita da versão exata.
7. **A7 — Fechar WATCHDOG:** obter decisões dos proprietários sobre atualidade; testar supervisão independente, canais, ACK, escalonamento e recuperação.
8. **A8 — Reconciliar inventários e auditoria de hashes:** auditar a árvore do commit atual, não apenas fotografias históricas; publicar a evidência.
9. **A9 — Executar fecho formal:** atualizar scorecard e painel através da automação canónica, verificar a sincronização e registar revisão/aprovação final.

## 5. Bloqueios, dependências e política de exceções

- **Distribuição por PR real:** os dry-runs #45 e #46 provaram autenticação e leitura, com 0 erros, mas continuam a retornar `WOULD_OPEN_PR`. Falta uma execução manual controlada com `dry_run=false` e confirmação das permissões de escrita no consumidor escolhido.
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
- [Execução #45 — dry-run autenticado, 78 ficheiros, 9 destinos no registo/8 ativos, 0 erros](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39510683461)
- [Execução #46 — dry-run após desativar LICITACAO, 78 ficheiros, 8 destinos ativos, 0 erros](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39510865206)
- [Execução #44 — dry-run anterior](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39506967606)
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

## 8.2. Integridade do painel — 2026-10-21

- Foi corrigida a automação `automation/sync_project_status.py` para atualizar o SHA-256 canónico do README segundo a norma: UTF-8/LF e exclusão das duas linhas de controlo.
- Foi acrescentado teste específico de checksum em `tests/test_sync_project_status.py`.
- A CI [run #56](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39516044531) passou com **39 testes**; o passo `automation/sync_project_status.py --check` confirmou o painel Markdown e o SVG sincronizados.
- Os runs #53–#55 falharam durante a introdução inicial da mudança e do teste; a falha do teste foi corrigida antes do run #56. O histórico é preservado e o último resultado é PASS.
- O SHA-256 do README é agora recalculado automaticamente sempre que o bloco de status muda; o cabeçalho mantém as restantes decisões de versão e aprovação sob controlo documental separado.

## 8.1. Registo de execução — 2026-10-21

- O scorecard canónico foi reconciliado para remover um bloqueio duplicado de distribuição; os bloqueios ativos passaram de 10 para 9, sem alteração dos pontos comprovados.
- O workflow de sincronização do status voltou a passar após a alteração: [run #51](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39515702729). O README e o SVG foram regenerados a partir do registo canónico.
- Estado após a verificação: 80/100; início 20/20, meio 60/60, fim 0/20; os cinco controlos de encerramento continuam falsos.
- A verificação da árvore atual encontrou cinco workflows no repositório-mestre; quatro definem controlo de concorrência. O workflow reutilizável não declara concorrência própria. Este resultado não resolve o bloqueio separado sobre os 42 workflows transversais.
- O catálogo de perfis continua estrutural, com todos os perfis em `complete: false`; o motor só suporta `file_exists` como tipo de requisito. Não é seguro marcar perfis completos sem ampliar os tipos de controlo, acrescentar testes e definir critérios semânticos aprovados.
- A distribuição por PR real não pode ser marcada como concluída com a evidência disponível: os runs #45/#46 foram dry-runs e retornaram `WOULD_OPEN_PR`. A ferramenta de integração disponível nesta sessão não permite iniciar um workflow manual com `dry_run=false`; o teste real permanece uma ação operacional pendente.
- A limpeza do scorecard foi publicada no commit `c1617b7fb7724d511bb06a9495cfa3f6d28570c4`; a sincronização subsequente passou no run #51.

## 8. Regra de encerramento

A GOVERNANCA só pode ser declarada FINALIZADA quando todos os critérios de saída G0–G7 estiverem comprovados, o scorecard canónico refletir as evidências atuais, os bloqueios críticos estiverem resolvidos ou formalmente excetuados e existir aprovação explícita do encerramento. Até esse momento, manter o estado **EM_EXECUCAO / EM_FINALIZACAO** e a percentagem baseada apenas em evidência.

## 8.3. Revalidação de concorrência B3 / BLOOMBERG_MAIL — 2026-10-21

- **B3:** PR [#18](https://github.com/carlos-andrade/B3/pull/18) integrada no commit `6d29578cc6b6b5155b874fd043269b0cbecae89c`. Os três workflows de publicação BVBG.028.02 usam o grupo comum `b3-bvbg028-catalog-publish-${{ github.ref }}` e `cancel-in-progress: false`. O workflow [run 39525805546](https://github.com/carlos-andrade/B3/actions/runs/39525805546) terminou com sucesso, incluindo classificação e etapa de commit/push; auditoria estática [run 39525805547](https://github.com/carlos-andrade/B3/actions/runs/39525805547) passou.
- **BLOOMBERG_MAIL:** PR [#7](https://github.com/carlos-andrade/BLOOMBERG_MAIL/pull/7) integrada no commit `53526887807455493cf024a6524abba8c53cd688`; os três workflows publicadores 005N partilham `bloomberg-mail-005n-publish-${{ github.ref }}` e `cancel-in-progress: false`. PR [#8](https://github.com/carlos-andrade/BLOOMBERG_MAIL/pull/8) integrada com testes seguros; [run 39526649987](https://github.com/carlos-andrade/BLOOMBERG_MAIL/actions/runs/39526649987) passou a validação YAML/configuração, idempotência sintética e recuperação de non-fast-forward/rebase em repositório temporário.
- Os testes BLOOMBERG_MAIL não executaram ingestões, APIs externas, segredos ou dados de produção. Os testes demonstram o padrão Git de recuperação, não o comportamento do scheduler GitHub Actions nem uma garantia FIFO.
- A auditoria [AUDITORIA-CONCORRENCIA-WORKFLOWS-42-2026-10-21.md](docs/01-governanca/AUDITORIA-CONCORRENCIA-WORKFLOWS-42-2026-10-21.md) foi atualizada para distinguir gaps mitigados de testes dinâmicos pendentes.
- **Scorecard:** manter 80/100 (início 20/20, meio 60/60, fim 0/20); não atribuir pontos de encerramento. Os cinco `closure_checks` permanecem `false`. C2/C4/C5, testes reais do scheduler, distribuição real por PR, aceitação WATCHDOG e gates normativos/operacionais continuam pendentes.


## 8.4. Mitigações adicionais de concorrência — 2026-10-21

- **TURISTURIS C4:** PR [#87](https://github.com/carlos-andrade/TURISTURIS/pull/87) integrada no commit `c0dae020358b8c7156e2b9e417c83f19dc5bc3e6`. A tabela-mestra RNAL agora usa `turisturis-rnal-master-publish-${{ github.ref }}`, `cancel-in-progress: false` e recuperação limitada de `git push` por `fetch + rebase`, sem force push. O workflow de produção não foi executado para testar concorrência; validação operacional pendente.
- **B3 C2/C5:** PR [#19](https://github.com/carlos-andrade/B3/pull/19) permanece em draft. Foi proposto `cancel-in-progress: false` para publicação Wiki e grupo comum COTAHIST apenas no workflow de certificação anual. Isto é insuficiente para C2: todos os outros escritores COTAHIST ainda precisam de grupo comum. Não integrar a PR como resolução completa sem expandir a correção e validar.
- **WATCHDOG:** `watchdog-validation.yml` tem permissões apenas de leitura e executa testes e `watchdog.py --check`; não foram observados passos de publicação. O cancelamento ativo pode ser mantido para esta validação read-only, sujeito a confirmação futura se o contrato mudar.
- **Scheduler real:** permanece sem evidência. Os testes Git sintéticos não demonstram o comportamento do scheduler GitHub Actions. Não foi iniciada execução de produção para fabricar concorrência; é necessário um harness isolado aprovado, com duas execuções de teste e logs de início/fim que comprovem ausência de sobreposição.
- **Scorecard:** 80/100, início 20/20, meio 60/60, fim 0/20; 9 bloqueios; os cinco `closure_checks` continuam `false`. Nenhum ponto de encerramento atribuído, pois C2, teste real do scheduler, C5 e outros gates globais permanecem abertos.
