# Auditoria estática de concorrência — 42 workflows

| Campo | Valor |
|---|---|
| ID | GOV-AUD-CONCURRENCY-042 |
| Data da inspeção | 2026-10-21 |
| Branch observada | `main` de cada repositório |
| Método | Leitura estática de YAML, triggers, concurrency, cancel-in-progress e sinais de escrita/publicação |
| Estado | DIAGNÓSTICO PARCIAL — correções e testes dinâmicos pendentes |
| Política | Não reexecutar workflows de dados nem alterar workflows sem teste de colisão e rollback |

## 1. Resultado executivo

Foram inspecionados exatamente 42 caminhos atuais, com SHA de blob registado por workflow. A seleção inclui 25 workflows operacionais B3 classificados na matriz funcional, substituindo o caminho obsoleto `sincronizar-wiki.yml` pelo ficheiro atual `b3-auditoria-sha256-documental.yml`, mais 17 workflows de publicação/validação dos repositórios GOVERNANCA, TURISTURIS, BLOOMBERG_MAIL, STOCKS, CONSORCIO, XFI, DECIO-BAZIN e BRICKMASTER_GERAL.

**Resultado estático:** foram encontrados oito gaps de concorrência explícitos em workflows com sinais de escrita/publicação; além disso, grupos diferentes por workflow não serializam operações que concorrem pela mesma branch `main`. O risco de corrida de `git push` continua a existir mesmo quando cada workflow tem o seu próprio grupo.

**Não declarar auditoria concluída:** não foram executados testes simultâneos, recuperação após push concorrente, nem validação de cada output em ambiente controlado. Esta evidência é estática e não prova ausência de colisões em runtime.

## 2. Matriz dos 42 caminhos

Legenda: `grupo/cancel` = concurrency group e `cancel-in-progress`; `GAP` = sinal de escrita/publicação sem grupo explícito; `SERIAL` = grupo presente com cancelamento desativado; `CANCEL` = cancelamento ativo num workflow de validação/monitorização; `REVER` = grupo único não partilhado com outros escritores do mesmo recurso.

| # | Repositório | Workflow | SHA observado | Grupo / cancel | Sinal |
|---:|---|---|---|---|---|
| 1 | B3 | `.github/workflows/atualizar-readme-b3.yml` | `01c931a895aff2292210c08d02c96784d86610be` | `atualizar-readme-b3 / false` | REVER: escritor serializado só consigo próprio |
| 2 | B3 | `.github/workflows/b3-auditoria-workflows-layout-mestre-v1.yml` | `17f1445bcd089561138c26773cd2791611a78c1e` | `b3-auditoria-workflows-layout-mestre / false` | REVER: publica relatório em main |
| 3 | B3 | `.github/workflows/b3-auditoria-sha256-documental.yml` | `551637c20b949c16292f3afbe31e1acdfac4ac80` | `b3-auditoria-sha256-documental / false` | REVER: somente leitura; não serializa outros escritores |
| 4 | B3 | `.github/workflows/b3-monitor-execucoes-v1.yml` | `6e29b3c0dcd381dbd03fbad1ee1bfa80a8929882` | `b3-monitor-execucoes / false` | REVER: grupo isolado |
| 5 | B3 | `.github/workflows/bcb-sgs-nucleo-macro-v1.yml` | `d7e1fc2b323fdc479f7ce962e9993cb07940c815` | `b3-data-ingestion-serialized / false` | SERIAL: partilha grupo com captura COPOM |
| 6 | B3 | `.github/workflows/capturar-bcb-copom.yml` | `ff5f6b628f01441f12a88f398d9107a83d2c5534` | `b3-data-ingestion-serialized / false` | SERIAL: partilha grupo com SGS |
| 7 | B3 | `.github/workflows/classificar-bvbg028.yml` | `f5131ce0a709b5c97c47873f0b7d5158786fbad0` | — | GAP CRÍTICO: escrita em `ativos/catalogo/classificacao/` e push a main |
| 8 | B3 | `.github/workflows/cotahist-certificacao-anual-v1.yml` | `b7c981b09251f8b31a5bcfa8d72121085fb6e43c` | `cotahist-certificacao-anual-v1 / false` | REVER: grupo isolado |
| 9 | B3 | `.github/workflows/cotahist-dataset-oficial-v1.yml` | `7a9092f98400876f77b3bb3277a3f9b0078114c7` | `cotahist-dataset-oficial-v1 / false` | REVER: grupo isolado |
| 10 | B3 | `.github/workflows/cotahist-dataset-oficial-v2.yml` | `c47b385a6f9497725d99b86b0c52def6c9c09a0a` | `cotahist-dataset-oficial-v2 / false` | REVER: grupo isolado |
| 11 | B3 | `.github/workflows/cotahist-fase08h-recurrencia-k4-multianos-v1.yml` | `4e45fc9c8160e825801d6b80911c4086657d14e6` | — | GAP: escreve evidência em `dados/cotahist/quality/` e faz push |
| 12 | B3 | `.github/workflows/cotahist-importacao-diaria-v1.yml` | `296942c78a89ef54202c9d6064a7aeb46b0c019d` | `cotahist-importacao-diaria-v1 / false` | REVER: escritor serializado só consigo próprio |
| 13 | B3 | `.github/workflows/cotahist-m3-0-gate-capacidade-2026.yml` | `a20aaca38c0c2bff3ec41612e9221378b2ec3970` | `cotahist-m3-0-capacidade-2026 / false` | REVER: grupo isolado |
| 14 | B3 | `.github/workflows/cotahist-m3-1b-prova-lfs-2026.yml` | `f1f1d602e7dfb35da24c2736e78b9995b19fd87d` | `cotahist-m3-1b-lfs-2026 / false` | REVER: grupo isolado |
| 15 | B3 | `.github/workflows/cotahist-m3-1b-reconciliar-manifest-2026.yml` | `fe2a22b3553b725865a589bcb09b89b1747c23bc` | `cotahist-m3-1b-reconciliar-manifest-2026 / false` | REVER: grupo isolado |
| 16 | B3 | `.github/workflows/cotahist-m3-1c-ci-normalized-2026.yml` | `49ae9102ecb5bbd2073dc88f2ab4e968e54dc889` | `cotahist-m3-1c-ci-2026 / false` | REVER |
| 17 | B3 | `.github/workflows/cotahist-m3-1d-dataset-oficial-2026.yml` | `2caedc2ef36ae1f61ae1b29dbf759fb0af6a7e76` | `cotahist-m3-1d-2026 / false` | REVER |
| 18 | B3 | `.github/workflows/cotahist-m3-1e-aprovacao-global.yml` | `ceb86c61564d4de23d1653bdae2162fde8670ece` | `cotahist-m3-1e-2026 / false` | REVER |
| 19 | B3 | `.github/workflows/cotahist-normalizacao-controlada-v7.yml` | `00ee07bee16503600f5379604d80eff7183176df` | `cotahist-normalizacao-controlada-v7 / false` | REVER: escritor serializado só consigo próprio |
| 20 | B3 | `.github/workflows/cotahist-orquestrador-anual-dryrun-v1.yml` | `c73c39ebbf408af9f4fcd2a4509978c91cc1d4a7` | `cotahist-orquestrador-anual-dryrun-v1-${{ inputs.ano }} / false` | REVER: dry-run; grupo por ano |
| 21 | B3 | `.github/workflows/cotahist-orquestrador-anual-dryrun-v2.yml` | `735a8c0c5c4320e761076cde914b2ccc8e734942` | `cotahist-orquestrador-anual-dryrun-v2-${{ inputs.ano }} / false` | REVER: dry-run; grupo por ano |
| 22 | B3 | `.github/workflows/indices-b3-composicao-v1.yml` | `4ece91cb525d7215cabef4b91d068b45e0e2e3fe` | `indices-b3-composicao-v1 / false` | REVER: escritor serializado só consigo próprio |
| 23 | B3 | `.github/workflows/processar-inventario-bvbg028.yml` | `a0eeb3eb5a731ab3d0f59a2ba41854cb920fad63` | — | GAP CRÍTICO: escreve `ativos/catalogo/` e faz push |
| 24 | B3 | `.github/workflows/sincronizar-wiki-b3.yml` | `8f90b8fb9c52cc65fea9a08bc087935fe6c8df07` | `b3-wiki-sync / false` | MITIGADO: PR #20 integrada; execução de publicação ainda não testada |
| 25 | B3 | `.github/workflows/validar-bvbg02802.yml` | `84c9084bbb1bcce02d34120b6582efd7d9f8b8a8` | — | GAP CRÍTICO: escreve manifesto e push; partilha superfície de catálogo |
| 26 | GOVERNANCA | `.github/workflows/propagar-regras-governanca.yml` | `de2a091f9b04ede2f2c6afe8b6e9431a1cf4612f` | `propagar-governanca-main / false` | REVER: grupo não serializa os consumidores entre si |
| 27 | GOVERNANCA | `.github/workflows/sync-project-status.yml` | `bee49951ff93ce202f5cb312fc750d475db0197f` | `sync-project-status-main / false` | SERIAL local; push com rebase/retry |
| 28 | GOVERNANCA | `.github/workflows/watchdog-validation.yml` | `fece47551f539f65a9d6ffa5af97d9da5179bbee` | `watchdog-validation-${{ github.ref }} / true` | CANCEL: validação; não assumir segurança se publicar efeitos |
| 29 | TURISTURIS | `.github/workflows/turisturis-pages.yml` | `2bb13f51517aef196f4a7c0d1e8ee4ab3c75c5d1` | `pages / false` | SERIAL: publicação Pages |
| 30 | TURISTURIS | `.github/workflows/turisturis-publicar-rnal-tomar.yml` | `6baa086b4893cc6c038b47e175cf9b992008e683` | `turisturis-publicar-rnal-tomar-v2 / false` | REVER: grupo isolado |
| 31 | TURISTURIS | `.github/workflows/turisturis-orquestrador-fases.yml` | `373cb5a1e761b8dc4d81e5d053570866a40a03c0` | `turisturis-orquestrador-fases / false` | REVER: escritor serializado só consigo próprio |
| 32 | TURISTURIS | `.github/workflows/turisturis-gerar-tabela-mestra-rnal-peso-da-regua.yml` | `53c18a025653a3df6aaadb2c8c97b837a9e038fa` | — | GAP: escreve tabela-mestra e faz push |
| 33 | BLOOMBERG_MAIL | `.github/workflows/bloomberg-mail-ingestao-005n-normalizacao.yml` | `41e9488094db50f3a4b3e62ebf0e76056d1164f0` | — | GAP: publica em `EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/` |
| 34 | BLOOMBERG_MAIL | `.github/workflows/bloomberg-mail-ingestao-005n-validacao-normalizadores.yml` | `75bccce3d9c6140c04cb339fb04efc340baf1665` | — | GAP: publica evidência na mesma árvore NORMALIZADO |
| 35 | BLOOMBERG_MAIL | `.github/workflows/bloomberg-mail-rec001-b3-cotahist-cross-repo.yml` | `129b7a9400e1287b5dcce343690322e07a8d62c2` | — | GAP: publica evidência REC001 e faz push |
| 36 | BLOOMBERG_MAIL | `.github/workflows/bloomberg-mail-watchdog-supervisor.yml` | `0fdb2004f2043d22ac07f11fa34d59d9b11bad57` | `bloomberg-mail-watchdog-supervisor / false` | SERIAL de monitorização |
| 37 | STOCKS | `.github/workflows/governance-integration.yml` | `7fccfe0b935197a5f12fb3f66e7358096bdc5ffd` | `governance-integration-pilot-${{ github.event.pull_request.number || github.ref }} / false` | SERIAL por PR/ref |
| 38 | STOCKS | `.github/workflows/verificar-eventos-societarios.yml` | `09d7ba421f0df72a838ee4ebf4e0b4797462932a` | `verificar-eventos-societarios-${{ inputs.ticker }} / false` | SERIAL por ticker |
| 39 | CONSORCIO | `.github/workflows/governanca-diaria.yml` | `ee764816f205e5bbcb64422672d1f19863282aa8` | `governanca-diaria-main / false` | SERIAL local |
| 40 | XFI | `.github/workflows/openwrt-source-link-check.yml` | `66a3d074e435441c75faa4b3f3a57cd9cf41c2fc` | `openwrt-source-link-check / false` | SERIAL local |
| 41 | DECIO-BAZIN | `.github/workflows/verificar-regra-normativa.yml` | `295058605241a42563bf74cee90b0e4a7e2d409c` | — | REVER: trigger push; validar que não publica efeitos |
| 42 | BRICKMASTER_GERAL | `.github/workflows/validar-cabecalhos-documentais.yml` | `2c616d2da5b521730deabbf407926a95be555adf` | — | REVER: trigger push; validar que não publica efeitos |

## 3. Colisões e correções necessárias

### C1 — B3 / publicação de catálogo BVBG.028.02 — MITIGADO; teste dinâmico pendente

Os três workflows `classificar-bvbg028.yml`, `processar-inventario-bvbg028.yml` e `validar-bvbg02802.yml` agora declaram o grupo comum `b3-bvbg028-catalog-publish-${{ github.ref }}` e `cancel-in-progress: false`. A alteração foi integrada pela PR [B3 #18](https://github.com/carlos-andrade/B3/pull/18), commit `6d29578cc6b6b5155b874fd043269b0cbecae89c`. O workflow de classificação terminou com sucesso no [run 39525805546](https://github.com/carlos-andrade/B3/actions/runs/39525805546), com as etapas de classificação e `Commit classificação` concluídas; a auditoria estática pós-merge passou no [run 39525805547](https://github.com/carlos-andrade/B3/actions/runs/39525805547).

Isto comprova a execução de classificação/publicação e a configuração estática, mas **não** comprova serialização real do scheduler GitHub Actions sob disparos concorrentes, FIFO, nem recuperação de colisões entre estes workflows. Manter o gate dinâmico aberto.

### C2 — B3 / escritores COTAHIST — ALTA; ABERTO

A PR [B3 #19](https://github.com/carlos-andrade/B3/pull/19) foi integrada em 2026-10-21, commit `50fc8d12adc524761ef866b75a8571ace77ccc58`. A verificação atual do `main` confirmou o grupo comum `b3-cotahist-main-publish-${{ github.ref }}` e `cancel-in-progress: false` nos três workflows abrangidos: certificação anual e datasets oficiais V1/V2. **A integração é parcial, não encerra C2.** A listagem atual de `.github/workflows` contém 536 nomes com `cotahist`; a auditoria transversal deste documento inspecionou apenas 42 workflows selecionados, portanto não constitui inventário exaustivo dos escritores. A inspeção individual já confirmou outros publicadores com `contents: write`, `git commit` e `git push`, incluindo `cotahist-importacao-diaria-v1.yml`, `cotahist-normalizacao-controlada-v7.yml`, `cotahist-m3-1b-reconciliar-manifest-2026.yml`, `cotahist-lfs-migracao-controlada-a1987-v1.yml`, `cotahist-gate-historico-1986.yml` e workflows de fases históricas, que mantêm grupos próprios ou ausentes. É necessário classificar o conjunto completo por escrita efetiva, destino/branch e recurso partilhado; excluir workflows read-only e dry-run sem escrita. **C2 permanece ABERTO até o inventário e a harmonização completos e a validação segura.**

### C3 — BLOOMBERG_MAIL / normalização 005N — MITIGADO; scheduler real pendente

Os três workflows publicadores agora partilham `bloomberg-mail-005n-publish-${{ github.ref }}` e `cancel-in-progress: false`. A correção está integrada pela PR [BLOOMBERG_MAIL #7](https://github.com/carlos-andrade/BLOOMBERG_MAIL/pull/7), commit `53526887807455493cf024a6524abba8c53cd688`. A PR [#8](https://github.com/carlos-andrade/BLOOMBERG_MAIL/pull/8) adicionou testes isolados e não destrutivos; o [run 39526649987](https://github.com/carlos-andrade/BLOOMBERG_MAIL/actions/runs/39526649987) passou.

Os testes validam parse YAML, grupo partilhado, `cancel-in-progress: false`, idempotência de ficheiro sintético e recuperação de `non-fast-forward` por rebase num repositório Git temporário. Não invocam ingestão, APIs externas, segredos ou dados de produção. **Não** simulam o scheduler real do GitHub Actions nem garantem FIFO; esses limites permanecem explícitos.

### C4 — TURISTURIS / tabela-mestra — MITIGAÇÃO INTEGRADA; teste pendente

A PR [TURISTURIS #87](https://github.com/carlos-andrade/TURISTURIS/pull/87) foi integrada no commit `c0dae020358b8c7156e2b9e417c83f19dc5bc3e6`. O workflow agora usa `turisturis-rnal-master-publish-${{ github.ref }}`, `cancel-in-progress: false`, e repetição limitada de `fetch + rebase + push` sem force push. A alteração foi revista estaticamente; o workflow de produção não foi executado para evitar regeneração/publicação de dados apenas para teste. C4 está mitigado no código, mas requer verificação CI/execução controlada antes de fechar o gate.

### C5 — Semântica de cancelamento — MITIGADO NO CÓDIGO; teste pendente

A [PR B3 #20](https://github.com/carlos-andrade/B3/pull/20) foi integrada no commit `e5caa295cfea627ad63cfb62b0898481cfa32750`. O ficheiro atual `.github/workflows/sincronizar-wiki-b3.yml` declara `group: b3-wiki-sync` e `cancel-in-progress: false`, verificado no `main` (blob `8f90b8fb9c52cc65fea9a08bc087935fe6c8df07`). Isto impede que uma nova execução cancele a execução ativa, mas não garante FIFO e não prova uma publicação concluída. O workflow `watchdog-validation.yml` do GOVERNANCA mantém `permissions: contents: read` e executa testes e `watchdog.py --check`, sem passos de commit/push observados; o cancelamento ativo é aceitável enquanto o contrato permanecer read-only. C5 fica mitigado no código, com validação operacional ainda pendente.

## 4. Testes de concorrência e recuperação — estado atualizado em 2026-10-21

- [x] B3: inspeção estática dos três workflows confirma grupo comum e `cancel-in-progress: false`; classificação e etapa de commit/push concluídas no [run 39525805546](https://github.com/carlos-andrade/B3/actions/runs/39525805546); auditoria estática pós-merge PASS no [run 39525805547](https://github.com/carlos-andrade/B3/actions/runs/39525805547).
- [x] BLOOMBERG_MAIL: parse YAML e configuração comum dos três workflows testados em CI; idempotência sintética e recuperação de non-fast-forward/rebase em repositório temporário aprovadas no [run 39526649987](https://github.com/carlos-andrade/BLOOMBERG_MAIL/actions/runs/39526649987), PR [#8](https://github.com/carlos-andrade/BLOOMBERG_MAIL/pull/8).
- [ ] Testar o comportamento do scheduler GitHub Actions com duas execuções concorrentes num workflow isolado, recolher logs/timestamps de início e fim e comprovar que os intervalos de execução não se sobrepõem; não presumir FIFO. A evidência atual não contém esse teste. Não usar workflows que leem ou publicam dados reais como mecanismo de teste.
- [x] B3 Wiki: PR #20 integrada; configuração `b3-wiki-sync / cancel-in-progress: false` confirmada no `main`. Não foi localizada evidência de execução concorrente real nem de publicação operacional após o merge.
- [ ] B3: repetir teste sintético de idempotência e recuperação para os padrões de escrita dos três workflows; confirmar preservação de artefactos.
- [ ] Executar duas publicações COTAHIST que alterem recursos partilhados; comprovar serialização e integridade dos manifestos.
- [ ] Testar cancelamento e rollback da publicação Pages/Wiki.
- [ ] Arquivar logs relevantes, URLs de runs, SHAs, diffs e hashes; atualizar este relatório apenas após observar os resultados.

### Revalidação de execução após o merge B3 #19 — 2026-10-21

A leitura dos runs recentes identificou falhas operacionais que não devem ser confundidas com o estado da configuração de concorrência:

- [Run 39590685303 — Dataset Oficial V2](https://github.com/carlos-andrade/B3/actions/runs/39590685303): **FAIL** em `Gerar Dataset Oficial V2`; log explícito: `2026: QUALITY_MANIFEST_INVALIDO`. A publicação não foi concluída.
- [Run 39590685161 — Dataset Oficial V1](https://github.com/carlos-andrade/B3/actions/runs/39590685161): **CANCELLED**.
- [Run 39590685070 — Certificação anual](https://github.com/carlos-andrade/B3/actions/runs/39590685070): **CANCELLED**.
- [Run 39592151814 — Importação diária COTAHIST](https://github.com/carlos-andrade/B3/actions/runs/39592151814): **FAIL** no gate de autorização, em `test_cotahist_direct_file_allows_only_limited_internal_validation`, com `KeyError: 'operation_scope'`; o job de importação foi ignorado. O mesmo erro foi observado no [run 39592143030](https://github.com/carlos-andrade/B3/actions/runs/39592143030).

Os runs de V1/V2/certificação foram disparados no contexto do mesmo commit `50fc8d12...`; os estados CANCELLED confirmam que é necessário examinar os detalhes de agendamento e as políticas de concorrência, mas **não bastam, isoladamente, para provar a causa exata do cancelamento**. `cancel-in-progress: false` protege a execução ativa contra substituição, mas não é uma prova de FIFO nem de que todas as execuções pendentes serão preservadas. Estes resultados acrescentam bloqueios de execução a resolver antes de aceitar a publicação COTAHIST.

### Teste isolado do scheduler — evidência real 2026-10-21

O harness sem permissões de escrita foi executado numa branch dedicada de teste, sem dados de produção nem publicação:

- [Run 39594340734](https://github.com/carlos-andrade/B3/actions/runs/39594340734): início UTC `2026-10-21T11:45:43.190123905Z`; fim UTC `2026-10-21T11:46:08.252340858Z`; conclusão SUCCESS; [artefacto de logs](https://github.com/carlos-andrade/B3/actions/runs/39594340734/artifacts/12344070685).
- [Run 39594370310](https://github.com/carlos-andrade/B3/actions/runs/39594370310): início UTC `2026-10-21T11:46:14.681605678Z`; fim UTC `2026-10-21T11:46:39.738394171Z`; conclusão SUCCESS; [artefacto de logs](https://github.com/carlos-andrade/B3/actions/runs/39594370310/artifacts/12344325246).

Os intervalos não se sobrepõem; a segunda execução começou cerca de 6,43 segundos após o fim da primeira. Num ensaio separado com três eventos rápidos, [run 39594183327](https://github.com/carlos-andrade/B3/actions/runs/39594183327) terminou CANCELLED enquanto [39594177078](https://github.com/carlos-andrade/B3/actions/runs/39594177078) e [39594206007](https://github.com/carlos-andrade/B3/actions/runs/39594206007) terminaram SUCCESS. O teste confirma a exclusão mútua para duas execuções e também demonstra que execuções pendentes podem ser substituídas por eventos mais recentes; não prova FIFO nem preservação de todas as execuções.

### Correções técnicas preparadas, ainda não integradas

A branch `carlos-andrade/B3:fix/cotahist-gates-scheduler-harness-2026-10-21` contém alterações para: classificar o manifesto de 2026 como bloqueio de autorização (sem o desbloquear); testar que `--allow-blocked` não altera a decisão; criar o temporário no mesmo filesystem do destino; limitar o trigger push da importação diária a `main`; remover autorreferências de três publicadores; e acrescentar inventário estático e harness isolado. Estas alterações ainda não estão em `main`; não contar como correções integradas.

## 5. Limites e decisão

As correções C1 (B3) e C3 (BLOOMBERG_MAIL) estão integradas e possuem evidência de CI/testes sintéticos conforme descrito acima. O resultado é **mitigação verificada**, não certificação do comportamento concorrente real do scheduler GitHub Actions. Os testes sintéticos usam dados e repositórios temporários; nenhuma ingestão de produção foi executada para os validar.

C2, C4 e C5 e os testes dinâmicos listados continuam pendentes. Não declarar o gate transversal de concorrência como PASS até os restantes gaps relevantes serem corrigidos e validados com evidência reproduzível.

A adoção transversal, o piloto real de distribuição, a aceitação operacional WATCHDOG e a ratificação normativa são gates separados; este relatório não os aprova nem os encerra.



## Revalidação COTAHIST — 2026-10-24

- A PR [B3 #29](https://github.com/carlos-andrade/B3/pull/29) foi integrada no commit 10b20bc43cd1347da8e55998e91898ceb36f4386. Os workflows individuais de certificação/V1/V2 passaram a validação manual read-only; a publicação automática foi centralizada num workflow serial com retries e recomputação sobre o HEAD atual.
- A validação da PR [run 40046948431](https://github.com/carlos-andrade/B3/actions/runs/40046948431) passou. O Dataset V2 foi gerado localmente no job de validação com 40 anos (1986–2025), periodo.fim=2025 e exclusão explícita de 2026 por autorização de publicação não demonstrada. O manifesto de 2026 não foi alterado para VALIDADO.
- O teste de regressão de autorização passou no mesmo run; o KeyError: operation_scope pertence a um commit anterior. O código atual expõe operation_scope e publication_authorized e a regressão protege o contrato do payload bloqueado.
- O teste real isolado do scheduler passou em dois workflows independentes, sem publicação nem segredos: [Probe B](https://github.com/carlos-andrade/B3/actions/runs/40046948426) iniciou em 2026-10-24T00:50:28.155798789Z e terminou em 2026-10-24T00:50:48.166926862Z; [Probe A](https://github.com/carlos-andrade/B3/actions/runs/40046948488) iniciou em 2026-10-24T00:50:53.759351992Z e terminou em 2026-10-24T00:51:13.769522084Z. Os intervalos não se sobrepõem; há aproximadamente 5,6 segundos entre o fim de B e o início de A. Este teste prova serialização para duas execuções, não FIFO nem preservação de filas com mais de duas execuções.
- O inventário estático gerado na validação cobre 541 workflows COTAHIST/referenciados: 527 com sinais de escrita efetiva, 498 com destino explícito main, 29 com destino implícito/upstream e 70 sem grupo de concorrência. Estes são sinais estáticos; paths dinâmicos e recursos reais ainda requerem reconciliação por classe. A correção central não equivale a harmonizar todos os 527 escritores.
- A execução diária mais recente tinha ainda um erro separado de formato: um registo foi observado com 246 bytes, enquanto o parser exige 245. Não foi enfraquecido o gate nem truncado o registo sem inspecionar o byte extra; esta pendência permanece aberta.
- Após o merge, os runs [publicador serial 40047097175](https://github.com/carlos-andrade/B3/actions/runs/40047097175), [auditoria de workflows 40047097186](https://github.com/carlos-andrade/B3/actions/runs/40047097186) e [importação diária 40047097026](https://github.com/carlos-andrade/B3/actions/runs/40047097026) ainda estavam em execução/espera no momento deste registo. Não declarar a publicação operacionalmente validada até verificar os seus resultados finais.
- Decisão: manter o scorecard em 80/100 e os critérios de encerramento falsos. O scheduler isolado foi comprovado, mas a execução pós-merge, a falha de 246 bytes e a revisão dos escritores remanescentes ainda não permitem encerrar o gate global.
