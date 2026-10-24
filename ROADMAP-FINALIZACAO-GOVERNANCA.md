# Roadmap de finalização — GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-ROADMAP-FINAL-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | ROADMAP |
| **Fase** | Finalização do sistema-mestre |
| **Estado** | EM_EXECUCAO |
| **Versão** | 1.0.5 |
| **SHA-256 (conteúdo canónico)** | a28777cbcc563dc4971c64a3e45ea9746854756265f88f8f888522d8c27ce222 |
| **Commit de referência (versão anterior)** | [7858580a1c9d42e70fabb18a4a12118c364d1339](https://github.com/carlos-andrade/GOVERNANCA/commit/7858580a1c9d42e70fabb18a4a12118c364d1339) |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Proprietário do repositório GOVERNANCA — reconciliação G1 após integração da STOCKS PR #10 |
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
- **Bloqueios centrais conhecidos:** a distribuição real por PR foi demonstrada num consumidor de teste autorizado: run #76 criou STOCKS PR #10 com zero erros; a PR permanece aberta e a repetição idempotente/revisão humana ainda não estão comprovadas. O catálogo de perfis permanece incompleto; a adoção transversal e a aceitação operacional WATCHDOG continuam pendentes; LICITACAO permanece `enabled: false` em `main`.
- **Regra fail-closed:** não habilitar distribuição nem declarar conformidade global sem provas adequadas.

## 3. Roadmap de gates

| Gate | Entregáveis e trabalho | Critério objetivo de saída | Estado |
|---|---|---|---|
| G0 — Baseline e autoridade normativa | Constituição v1.0.2, política de decisões v1.0.1, matriz de responsabilidades v1.0.1 e registo formal G0 integrados; hashes canónicos verificados e CI aprovada. | Constituição, hierarquia, política e responsabilidades ratificadas; versões exatas e evidência ligadas; CI verde. | CONCLUÍDA — PR #35 integrada no commit `fe56b96c427dadf9a2774a8976aab35222fd76d2`; CI #43 passou, incluindo testes F1/F2 e validação dos quatro hashes canónicos. |
| G1 — Distribuição segura | Autenticação do `GOVERNANCA_SYNC_TOKEN` validada nos runs #45/#46; executar o modo real por PR num único consumidor autorizado e testar acesso de escrita; criar/atualizar PRs reais apenas para destinos autorizados; verificar idempotência, isolamento de ficheiros, hashes, relatórios e redação de segredos. | Evidência de workflow real concluído, relatório inspecionado, PRs esperadas criadas/atualizadas, zero destinos indevidos e repetição sem diffs desnecessários. | EM VALIDAÇÃO — run #76 criou a [PR STOCKS #10](https://github.com/carlos-andrade/STOCKS/pull/10), integrada em 2026-10-23 no commit `8d6967b8a95eb282c5538e354bef8dd9ebd29778`. A PR integrou 5 ficheiros, sem reviews ou checks registados na PR. O manifesto integrado continua a apontar para o commit-fonte antigo `e54c3ca24b04971f39a5c804beedc21ff1aff355`, enquanto a GOVERNANCA `main` está em `7858580a1c9d42e70fabb18a4a12118c364d1339`; a sincronização está desatualizada. Run #78 foi apenas dry-run automático (84 ficheiros, 8 consumidores, 0 erros). Falta nova execução real limitada a STOCKS para propagar a origem atual, inspeção de hashes e uma segunda execução real sem alteração da origem para provar idempotência. A integração da PR #10 não equivale a aceitação formal nem conformidade. |
| G2 — Registo de consumidores e adoção | Reconciliar `registry/repositorios-consumidores.json`, PR #4 e critérios de adoção; inspecionar cada espelho, manifestos, hashes, configurações, workflows e evidência individual. | Para cada destino, estado enabled coerente com decisão formal e critérios comprovados; nenhum estado de registo interpretado como certificação. | EM EXECUÇÃO — LICITACAO está agora disabled em main até adoção validada; PR #4 continua aberta e desatualizada face ao estado atual, devendo ser reconciliada/fechada sem reativar o destino; demais destinos exigem revisão individual. |
| G3 — Governance Integration Framework | Completar catálogo executável para todos os perfis; definir requisitos semânticos, evidências, severidade, regras de applicability, políticas de modo aplicar, versionamento/ref imutável, relatórios e testes adversariais. | Catálogo com completude demonstrada por perfil; testes unitários, negativos e integração aprovados; relatório correto para PASS/FAIL/UNKNOWN; alteração só por PR; nenhuma certificação implícita. | EM EXECUÇÃO — F1/F2 e baseline estrutural F4 têm validações parciais; catálogo permanece `complete: false`; F5/F6 não concluídas. |
| G4 — Integridade documental | Reconciliar árvore atual de `main` com inventários; verificar cabeçalhos, IDs, links, versões e SHA-256 canónico segundo a norma; corrigir inconsistências sem perda de conteúdo histórico. | Inventário completo e reconciliado com o commit auditado; hashes recalculados; exceções justificadas, aprovadas e rastreáveis. | EM EXECUÇÃO — inventário interno e inventário transversal têm âmbito/fotografias históricas que requerem atualização. |
| G5 — WATCHDOG e operação | Resolver publicação concorrente de workflows; aprovar limites de atualidade por proprietários; configurar monitorização independente, heartbeat, canais de alerta, ACK, escalonamento, responsáveis e SLA; testar falha, recuperação e ausência de monitor. | Execuções atuais demonstram deteção e recuperação; limites aprovados; alertas recebidos e reconhecidos; dependências operacionais sem UNKNOWN crítico ou com exceção formal válida. | BLOQUEADA — aceitação operacional e supervisão independente não comprovadas. |
| G6 — Validação transversal | Executar integração/diagnóstico por cada repositório no commit/ref indicado; validar evidências e relatórios por perfil; registar pendências, exceções, responsável e próxima ação. | Matriz de cobertura completa; todos os destinos classificados com evidência; nenhum resultado UNKNOWN omitido ou promovido a PASS. | PENDENTE — adoção individual ainda incompleta. |
| G7 — Auditoria e fecho | Revisão final independente proporcional ao risco; verificar gates, evidências, hashes, logs, riscos residuais, transferência de conhecimento e relatório final. Obter aprovação explícita de encerramento. | Todos os gates de fecho cumpridos; scorecard sincronizado; aprovação de encerramento registada; 100% apenas quando a norma e a evidência o permitirem. | PENDENTE — os cinco critérios FIM do scorecard estão por comprovar. |

## 4. Ações prioritárias imediatas

1. **A1 — Reconciliar LICITACAO:** PR #38 integrada no commit `6a7dc8d2ff817d1ce409842d097d4c82bb7c035d`; o registo canónico mantém `enabled: false` e o teste de regressão protege contra reativação inadvertida. A PR #4 deve ser reconciliada/encerrada sem reativar o destino.
2. **A2 — Validar escrita e executar PR piloto:** run [#76](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914) validou a credencial como `carlos-andrade` e criou a [PR STOCKS #10](https://github.com/carlos-andrade/STOCKS/pull/10), integrada no commit `8d6967b8a95eb282c5538e354bef8dd9ebd29778`. A permissão de escrita/criação de PR está demonstrada. Não registar nem expor o valor do secret.
3. **A3 — Distribuição real por PR demonstrada, mas réplica agora desatualizada:** run #76 processou 84 ficheiros, reportou 0 erros e criou a PR #10, que foi integrada. O manifesto de destino ainda fixa a origem `e54c3ca24b04971f39a5c804beedc21ff1aff355`; a origem atual é `7858580a1c9d42e70fabb18a4a12118c364d1339`. Run #78 é dry-run e não atualizou a réplica.
4. **A4 — Propagar origem atual e validar idempotência:** a PR #10 foi integrada, portanto já não pode ser atualizada como PR aberta. Executar manualmente o workflow `Propagar regras canónicas da GOVERNANCA` com `dry_run=false`, `repository=carlos-andrade/STOCKS` e `allow_disabled_test=false`, usando a `main` atual; inspecionar o relatório e a nova PR de sincronização que o workflow criar/atualizar. Verificar os hashes dos ficheiros afetados e a origem do manifesto. Sem novo commit na origem, repetir o mesmo dispatch real e confirmar `PR_NO_CHANGE` (ou resultado idempotente equivalente), sem diff adicional. Obter revisão/aceitação humana explícita da nova PR; não inferir aceitação a partir da integração anterior.
5. **A5 — Completar catálogo de perfis:** definir e testar critérios funcionais/semânticos por domínio; manter `complete: false` enquanto faltar qualquer perfil ou critério obrigatório.
6. **A6 — Rever políticas fora do âmbito G0:** ratificar individualmente os documentos ainda em `EM_REVISAO`; a aprovação G0 não os aprova por extensão.
7. **A7 — Fechar WATCHDOG:** obter decisões dos proprietários sobre atualidade; testar supervisão independente, canais, ACK, escalonamento e recuperação.
8. **A8 — Reconciliar inventários e auditoria de hashes:** auditar a árvore do commit atual, não apenas fotografias históricas; publicar a evidência.
9. **A9 — Executar fecho formal:** atualizar scorecard e painel através da automação canónica, verificar a sincronização e registar revisão/aprovação final.

## 5. Bloqueios, dependências e política de exceções

- **Distribuição por PR real:** demonstrada para um destino por [run #76](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914), que criou a [PR STOCKS #10](https://github.com/carlos-andrade/STOCKS/pull/10) com 84 entradas de manifesto e 0 erros. Quatro ficheiros alterados foram comparados byte-a-byte com a origem e os respetivos Git blob SHAs coincidiram; os quatro SHA-256 do manifesto também coincidiram. Não estão verificados todos os 84 hashes de conteúdo nesta auditoria. Falta repetir o dispatch para provar idempotência, inspecionar o diff final e obter aceitação/revisão; a PR não tem checks ou aceitação registados.
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
- [Execução #76 — distribuição real por PR no STOCKS, 84 entradas de manifesto, 0 erros](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914)
- [STOCKS PR #10 — integrada no commit 8d6967b8a95eb282c5538e354bef8dd9ebd29778; manifesto requer atualização](https://github.com/carlos-andrade/STOCKS/pull/10)
- [Execução #78 — dry-run automático, 84 ficheiros, 8 consumidores, 0 erros](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39967268661)
- [Artefacto do relatório de distribuição do run #76](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914/artifacts/12505997272)
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
| 1.0.1 | 2026-10-23 | G0 concluído após ratificação formal, verificação dos hashes canónicos e CI verde na PR #35. |
| 1.0.2 | 2026-10-23 | G1 reavaliado após reconciliação de LICITACAO e dry-run autenticado. |
| 1.0.3 | 2026-10-23 | Run #76 criou a PR STOCKS #10; quatro documentos alterados e os respetivos SHA-256 foram validados, ficando idempotência e aceitação pendentes. |
| 1.0.4 | 2026-10-23 | Sequência de validação corrigida: primeira reexecução sincroniza a origem atual; segunda execução com origem estável comprova idempotência. |
| 1.0.5 | 2026-10-23 | PR STOCKS #10 integrada, mas manifesto aponta para origem antiga; run #78 é dry-run. Nova propagação real e idempotência continuam pendentes. |

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
- **B3 C2/C5 — revalidação 2026-10-21:** a correção da Wiki foi integrada pela PR [#20](https://github.com/carlos-andrade/B3/pull/20), commit `e5caa295cfea627ad63cfb62b0898481cfa32750`; `sincronizar-wiki-b3.yml` declara `cancel-in-progress: false`, mas não há evidência de teste concorrente real da publicação. A PR [#19](https://github.com/carlos-andrade/B3/pull/19) **já foi integrada**, commit `50fc8d12adc524761ef866b75a8571ace77ccc58`; a verificação atual confirmou o grupo `b3-cotahist-main-publish-${{ github.ref }}` nos três workflows abrangidos (certificação anual e datasets oficiais V1/V2). Isto é uma mitigação parcial. A listagem atual do diretório `.github/workflows` contém 536 nomes com `cotahist`, enquanto a auditoria transversal selecionou 42 workflows; a cobertura ainda não é exaustiva. Outros escritores já confirmados — importação diária, normalização controlada, reconciliação de manifestos, migração LFS, gate histórico e fases históricas — mantêm grupos próprios ou ausentes. C2 permanece aberto até classificar todos os workflows com escrita efetiva, harmonizar os que partilham branch/recurso e validar com segurança.
- **WATCHDOG:** `watchdog-validation.yml` tem permissões apenas de leitura e executa testes e `watchdog.py --check`; não foram observados passos de publicação. O cancelamento ativo pode ser mantido para esta validação read-only, sujeito a confirmação futura se o contrato mudar.
- **Scheduler real — teste isolado concluído:** [run 39594340734](https://github.com/carlos-andrade/B3/actions/runs/39594340734) decorreu de 11:45:43.190Z a 11:46:08.252Z e [run 39594370310](https://github.com/carlos-andrade/B3/actions/runs/39594370310) de 11:46:14.681Z a 11:46:39.738Z; ambos SUCCESS e sem sobreposição. Artefactos de logs disponíveis em cada run. O teste adicional de três eventos [39594177078](https://github.com/carlos-andrade/B3/actions/runs/39594177078), [39594183327](https://github.com/carlos-andrade/B3/actions/runs/39594183327) e [39594206007](https://github.com/carlos-andrade/B3/actions/runs/39594206007) mostrou substituição de uma execução pendente (uma CANCELLED), confirmando que o mecanismo não garante FIFO nem preserva todas as execuções. Não usar o teste para certificar publicação de produção.
- **Falhas operacionais observadas após a PR B3 #19 (2026-10-21):** [run 39590685303](https://github.com/carlos-andrade/B3/actions/runs/39590685303) falhou na geração do Dataset Oficial V2 por `2026: QUALITY_MANIFEST_INVALIDO`; os runs [39590685161](https://github.com/carlos-andrade/B3/actions/runs/39590685161) (Dataset V1) e [39590685070](https://github.com/carlos-andrade/B3/actions/runs/39590685070) (certificação) terminaram `cancelled`. O run [39592151814](https://github.com/carlos-andrade/B3/actions/runs/39592151814) falhou no teste de autorização por `KeyError: 'operation_scope'` e ignorou o job de importação; o mesmo erro surgiu no [run 39592143030](https://github.com/carlos-andrade/B3/actions/runs/39592143030). Estes resultados requerem correção e nova CI; não permitem atribuir com certeza os cancelamentos ao grupo de concorrência nem certificar a publicação.
- **Scorecard:** manter 80/100, início 20/20, meio 60/60, fim 0/20; 9 bloqueios; os cinco `closure_checks` continuam `false`. Não recalcular ainda: as evidências são insuficientes para pontuar o fecho, pois C2 e o teste real do scheduler continuam abertos, C5 está mitigado no código mas não validado operacionalmente, e outros gates globais permanecem pendentes.


## 8.3. Fecho do G0 — 2026-10-23

- Constituição v1.0.2, política de decisões v1.0.1 e matriz de responsabilidades v1.0.1 ratificadas com âmbito e limites explícitos.
- Registo formal: [CABEÇALHO/REGISTO-APROVACAO-G0-2026-10-23.md](CABE%C3%87ALHO/REGISTO-APROVACAO-G0-2026-10-23.md).
- PR #35 integrada no commit [fe56b96c427dadf9a2774a8976aab35222fd76d2](https://github.com/carlos-andrade/GOVERNANCA/commit/fe56b96c427dadf9a2774a8976aab35222fd76d2).
- CI [run #43](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39952021834) passou: testes F1/F2 e validação de SHA-256 canónico para Constituição, matriz, política e registo de aprovação.
- Âmbito limitado: G0 concluído para o baseline normativo enumerado; não significa adoção ou conformidade automática dos restantes repositórios, nem aprovação das políticas não enumeradas.


## 8.5. Distribuição real por PR — 2026-10-23

- O workflow [Propagar regras canónicas da GOVERNANCA #76](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914) foi disparado manualmente com `dry_run=false`, destino `carlos-andrade/STOCKS` e `allow_disabled_test=false`. Os trabalhos `validar` e `propagar` terminaram SUCCESS; o relatório declara modo `pull-request`, commit-fonte `e54c3ca24b04971f39a5c804beedc21ff1aff355`, 84 ficheiros e 0 erros, com resultado `PR_CREATED` para [STOCKS PR #10](https://github.com/carlos-andrade/STOCKS/pull/10).
- O artefacto [relatorio-propagacao-governanca](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914/artifacts/12505997272) foi guardado; SHA-256 do ZIP reportado pelo GitHub: `0a4128ec17df1da086d198231bd7b049e3e68476f1bdcb0be51acd3f0b00e47a`.
- O manifesto contém 84 entradas e identifica a mesma origem. Para os quatro documentos de conteúdo alterados, o conteúdo no branch da PR coincide exatamente com os ficheiros do commit-fonte e os Git blob SHAs coincidem; os respetivos SHA-256 do manifesto também foram recalculados e corresponderam.
- A PR permanece aberta, não integrada, sem checks de CI ou revisão/aceitação registados no momento da inspeção. A criação bem-sucedida da PR demonstra permissão real de escrita no destino, mas não prova idempotência, adoção local ou conformidade global. G1 permanece EM VALIDAÇÃO até a repetição controlada não produzir alteração desnecessária e a PR ser revista/aceite.


## 8.6. Reconciliação posterior à integração da STOCKS PR #10 — 2026-10-23

- A [PR #10](https://github.com/carlos-andrade/STOCKS/pull/10) foi integrada às 14:35:07 UTC no commit `8d6967b8a95eb282c5538e354bef8dd9ebd29778`, com cinco ficheiros alterados. A PR não tem reviews registadas nem checks associados à head branch; a integração, por si só, não demonstra aceitação formal do espelho.
- O manifesto em `STOCKS/main` continua a declarar `source_commit=e54c3ca24b04971f39a5c804beedc21ff1aff355`, mas a `GOVERNANCA/main` atual é `7858580a1c9d42e70fabb18a4a12118c364d1339`. Logo, o espelho está desatualizado relativamente à origem atual.
- O run [#78](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39967268661) concluiu SUCCESS em `push`, mas o relatório declara `mode=dry-run`, `files_discovered=84`, `total_repositories=8`, `errors=0` e `WOULD_OPEN_PR` para os destinos. Não é prova de propagação real nem de idempotência.
- A próxima ação de execução é um dispatch manual real restrito a `carlos-andrade/STOCKS` (`dry_run=false`, `allow_disabled_test=false`) a partir da `main` atual; inspecionar a PR/relatório resultante, validar hashes afetados e, sem alterar a origem, repetir o mesmo dispatch para exigir `PR_NO_CHANGE`/equivalente. G1 permanece EM VALIDAÇÃO.

 
## Revalidação pós-merge — 2026-10-24

A PR B3 #29 foi integrada no commit 10b20bc43cd1347da8e55998e91898ceb36f4386. A validação da PR passou (run [40046948431](https://github.com/carlos-andrade/B3/actions/runs/40046948431)); o Dataset V2 foi gerado localmente com 40 anos (1986–2025) e 2026 permaneceu explicitamente bloqueado por autorização de publicação não demonstrada. O teste de regressão de operation_scope passou. Os probes reais isolados do scheduler passaram sem sobreposição: [B](https://github.com/carlos-andrade/B3/actions/runs/40046948426), 00:50:28.155Z–00:50:48.166Z; [A](https://github.com/carlos-andrade/B3/actions/runs/40046948488), 00:50:53.759Z–00:51:13.769Z. O inventário estático cobre 541 workflows, com 527 sinais de escrita efetiva, 498 destinos explícitos main, 29 destinos implícitos e 70 sem grupo de concorrência. A harmonização de todos os escritores não está concluída. A importação diária também revelou um registo de 246 bytes contra o parser de 245; não se alterou o parser sem evidência do byte extra. Os runs pós-merge do publicador, auditor e importador permaneciam pendentes no momento da revisão. Manter 80/100, fim=0 e os cinco critérios de encerramento falsos até os runs terminarem e as pendências restantes serem reconciliadas.
