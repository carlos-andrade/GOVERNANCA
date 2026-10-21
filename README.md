# GOVERNANCA — Sistema Mestre de Governança e Orquestração

| Campo | Valor |
|---|---|
| **ID** | GOV-README-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | README |
| **Fase** | Entrada e orientação do repositório |
| **Estado** | EM_REVISAO |
| **Versão** | 1.2.0 |
| **SHA-256 (conteúdo canónico)** | 7718b182dd455bbe8045fbe48f22adcbdf1e6b3bdab25c7b1e28cb87979ca20d |
| **Commit de referência (versão anterior)** | [fc1ebf06323d65c919f9a7dd2c741f37a49560e7](https://github.com/carlos-andrade/GOVERNANCA/commit/fc1ebf06323d65c919f9a7dd2c741f37a49560e7) |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-21 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal do README |
| **Autoridade superior** | [CONSTITUICAO.md](CONSTITUICAO.md) e [Norma de cabeçalho](CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


> Repositório-mestre para definir como projetos são propostos, priorizados, desenhados, executados, controlados, auditados e encerrados.

**Estado operacional:** Sistema-mestre em finalização, com 80% comprovados no scorecard canónico. A adoção global ainda não está aprovada: permanecem bloqueios de distribuição real por PR, completude semântica dos perfis, ratificação normativa e aceitação operacional do WATCHDOG. A existência de documentos ou workflows não equivale a conformidade.

<!-- GOVERNANCA_STATUS_START -->
## Painel executivo de status — GOVERNANCA

![Painel visual de status: 80% comprovados](assets/status-dashboard.svg)

**80% comprovados** · `[████████████████░░░░] 80%` · **Estado:** Em finalização · **Fase:** Fim

| Fase | Pontos comprovados | Peso máximo | Estado |
|---|---:|---:|---|
| **Início** | 20/20 | 20% | Concluído |
| **Meio** | 60/60 | 60% | Concluído |
| **Fim** | 0/20 | 20% | Pendente |

**Próximo marco:** Executar um teste controlado de distribuição por Pull Request real num único consumidor autorizado; completar critérios semânticos do Governance Integration Framework; resolver as decisões de aprovação normativa e a aceitação operacional WATCHDOG antes do fecho.

**Bloqueios ativos (9):**
- A correção transversal de publicação concorrente dos 42 workflows ainda precisa de verificação conclusiva na branch main; não retirar o bloqueio sem evidência atual.
- Os limiares de atualidade BCB SGS, BDI, COTAHIST anual (30 dias) e COTAHIST diário (5 dias) continuam PROVISIONAL, sem aprovação dos proprietários registada.
- A supervisão externa independente ainda não foi comprovada como operacional: faltam confirmar configuração dos secrets, ausência de heartbeat e recuperação.
- Responsáveis, canais de alerta, confirmação de receção, ACK/escalonamento e SLA ainda precisam de aprovação e teste com evidência.
- A adoção transversal do padrão de roadmap e das regras de governança continua sujeita a inspeção, integração e aceitação individual por repositório.
- A distribuição por Pull Request real ainda não foi demonstrada. Os runs #45 e #46 validaram a autenticação como carlos-andrade e executaram dry-run com 78 ficheiros, 8 consumidores ativos no segundo run e 0 erros; todos os destinos retornaram WOULD_OPEN_PR. Falta teste controlado em modo real por PR e validação de permissões de escrita por destino.
- Governance Integration Framework: catálogo v1.2.0 e motor com requisitos semânticos publicados. A correção do teste semântico foi integrada pela PR #23 no commit c447c85c82e095ababaaf0030a733f2561cfc960; CI F1/F2 passou no run 39521820489 e a sincronização do painel passou no run 39521820440. Os perfis continuam complete:false, automatico permanece sem requisitos executáveis e os requisitos de domínio ainda não estão aprovados; o GIF não certifica conformidade global.
- LICITACAO permanece disabled no registo canónico até adoção local aprovada e teste real de propagação. A PR #4 foi integrada em 2026-10-20 no commit a212d6bf8e26c0b26b7035926a01d2300a1c76b3; validar que a branch main mantém enabled:false.
- O roadmap de finalização ROADMAP-FINALIZACAO-GOVERNANCA.md foi publicado e o SHA-256 canónico calculado conforme a norma; a aprovação formal da versão exata do documento continua pendente.

**Última revisão:** 2026-10-21 · **Atualização do registo:** 2026-10-21

> **Limite da revisão:** Revisão documental em 2026-10-17. O workflow de sincronização executou com sucesso os testes automatizados, gerou o README e o SVG e confirmou a sincronização final nos runs 38981823399 e 38981877103. Os 10 pontos de testes da barra v2 foram atribuídos com evidência de CI. A aceitação externa do WATCHDOG continua pendente: a issue B3 #9 está fechada no GitHub, mas a checklist publicada não tem evidência de conclusão; fechar a issue isoladamente não prova aceitação operacional. A adoção transversal ainda exige validação individual por repositório. Implementação inicial da distribuição transversal publicada em 2026-10-17 (script, workflow, registo de consumidores e testes de validação); não considerar operacional até autenticação, dry-run e PRs reais serem verificados. Verificação técnica adicional em 2026-10-17: no workflow [run 38995449792](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/38995449792), o job `validar` passou e o job `propagar` falhou na autenticação porque o secret `GOVERNANCA_SYNC_TOKEN` contém um token inválido. Não houve tentativa de distribuição nem Pull Requests criadas nessa execução. O workflow foi ajustado para guardar um relatório de diagnóstico também quando a autenticação falha; essa correção ainda aguarda execução CI posterior. Formalização da arquitetura em 2026-10-20: a decisão DEC-GOV-INT-001 foi integrada em main pela PR #3, commit 7003bd9848983c211aca588e68e5281a5babc39a. O documento define arquitetura, controlos, roadmap F1–F6 e critérios de aceitação; a implementação integral permanece pendente. A integração não altera o estado operacional da distribuição transversal, que continua bloqueada até validação do GOVERNANCA_SYNC_TOKEN, dry-run autenticado e PRs reais. Fase F1 do Governance Integration Framework concluída em 2026-10-20: contrato e modos documentados em docs/01-governanca/ESPECIFICACAO-GOVERNANCE-INTEGRATION-FRAMEWORK-001.md; JSON Schema 2020-12 em schemas/governanca-config.schema.json; nove testes de contrato executados com sucesso no workflow [run 39459837269](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39459837269); PR #5 integrada no commit 3904c00bd80786d3e8a64d2beab1d076b70410a8. A F1 está concluída; F2–F6 continuam pendentes. O bloqueio de autenticação da distribuição transversal continua independente e não foi resolvido nesta fase.

Atualização 2026-10-20: F2 — núcleo inicial do Governance Integration Framework integrado na main pela PR #7, commit 7543446d45e59d5d4947fddea00a49ba0f04dbc6. CI F1/F2 passou no run 39460690733. Entregues leitura YAML segura, validação JSON Schema, relatório JSON com hashes SHA-256 e estados fail-closed; modo aplicar permanece bloqueado até F3. O catálogo de requisitos por perfil, piloto, validação adversarial, expansão e atualização contínua permanecem pendentes. A distribuição transversal continua bloqueada independentemente pela credencial GOVERNANCA_SYNC_TOKEN inválida.

Atualização 2026-10-20 — correção do fluxo de distribuição: PR #9 integrada (diagnóstico estruturado para token ausente/inválido, identidade não confirmada e redação de segredos); PR #10 integrada (isolamento de sys.argv nos testes e cobertura de propagação adicionada à CI). CI [run 39463666897](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39463666897) passou. Após integração, [run 39463793012](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39463793012) confirmou que a validação de registo/testes passou, mas a credencial foi rejeitada; distribuição foi corretamente ignorada, sem tentativas em consumidores. O secret GOVERNANCA_SYNC_TOKEN necessita substituição manual por credencial válida com permissões mínimas. Não declarar a distribuição operacional até dry-run autenticado e PRs por destino serem demonstrados.

Atualização 2026-10-20 — piloto F3: workflow reutilizável executado no STOCKS em [run 39467662909](https://github.com/carlos-andrade/STOCKS/actions/runs/39467662909), com artefacto [12286047005](https://github.com/carlos-andrade/STOCKS/actions/runs/39467662909/artifacts/12286047005). Relatório inspecionado: CFG-002 e SRC-001 PASS; source_commit e pinned_ref coincidem em e105218721d771f58264044bb7ad9fba7ab65b84; hashes SHA-256 da configuração e esquema presentes. Estado emitido DESCONHECIDO, corretamente, devido à ausência de catálogo executável por perfil. PR de consumidor STOCKS #8 continua aberta para aceitação humana; F3 não é declarada concluída. A credencial de distribuição transversal continua bloqueada e independente.\n\nAtualização 2026-10-20 — catálogo estrutural inicial por perfil: PR GOVERNANCA #14 integrada no commit b24e9580a145b0692abf9ea79aaf0cf35d260f48; CI F1/F2 [run 39476355134](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39476355134) passou. O catálogo `catalogs/governance-profile-catalog.json` foi ligado ao motor e ao workflow reutilizável, com validação de caminhos, IDs e hashes. O piloto STOCKS foi atualizado para esse commit e executado em [run 39476495677](https://github.com/carlos-andrade/STOCKS/actions/runs/39476495677); o relatório [artefacto 12288803976](https://github.com/carlos-andrade/STOCKS/actions/runs/39476495677/artifacts/12288803976) confirma CFG-002, SRC-001, DAD-STR-001 e DAD-STR-002 PASS e source_commit=pinned_ref. O estado permanece DESCONHECIDO por o catálogo estar explicitamente incompleto e cobrir apenas estrutura. PR STOCKS #8 continua aberta para aceitação humana. A distribuição transversal continua bloqueada pelo secret GOVERNANCA_SYNC_TOKEN inválido.\n\nAtualização 2026-10-20 — F4, validação adversarial inicial: PR GOVERNANCA #16 integrada no commit e5a7499d3a8a0877f4fc99774bb604a90f01e6f3; CI [run 39476819589](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39476819589) passou. O motor agora reporta catálogo ausente como DESCONHECIDO com bloqueio explícito e converte erro estrutural do esquema em erro controlado; testes incluem traversal de caminhos e perfil ausente do catálogo. STOCKS atualizado para o commit e5a7499d3a8a0877f4fc99774bb604a90f01e6f3 e validado no [run 39476916364](https://github.com/carlos-andrade/STOCKS/actions/runs/39476916364), artefacto [12289608239](https://github.com/carlos-andrade/STOCKS/actions/runs/39476916364/artifacts/12289608239): CFG-002, SRC-001, DAD-STR-001 e DAD-STR-002 PASS; source_commit=pinned_ref; estado DESCONHECIDO corretamente preservado. PR STOCKS #8 continua aberta para aceitação humana. Distribuição transversal continua bloqueada pelo secret GOVERNANCA_SYNC_TOKEN inválido.

Atualização 2026-10-20 — baseline estrutural v1.1 e aceitação do piloto: PR GOVERNANCA #18 integrada no commit c9be6d5224c7b412aa78a2b1d417b8315e5730f1; CI [run 39480798454](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39480798454) passou. Catálogo com baseline estrutural para os sete perfis concretos; perfil `automatico` sem mapeamento gera bloqueio explícito. Adicionada proteção contra symlinks que escapem da raiz do repositório. Piloto STOCKS final [run 39481074174](https://github.com/carlos-andrade/STOCKS/actions/runs/39481074174), artefacto [12291647106](https://github.com/carlos-andrade/STOCKS/actions/runs/39481074174/artifacts/12291647106): CFG-002, SRC-001, GOV-STR-001/002/003 e DAD-STR-001/002 PASS; source_commit=pinned_ref confirmado. Estado permanece DESCONHECIDO porque o catálogo é estrutural e `complete: false`. A PR STOCKS #8 foi integrada no commit 4f2650394fd6bee6d86871d05518392f3a00261f, após instrução expressa de conclusão; aceitação do piloto de diagnóstico registada, sem certificação global. O token de distribuição continua inválido e requer substituição manual.

Atualização 2026-10-20 — finalização central: publicado ROADMAP-FINALIZACAO-GOVERNANCA.md com gates G0–G7. A credencial GOVERNANCA_SYNC_TOKEN foi validada como carlos-andrade nos runs [39510683461](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39510683461) e [39510865206](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39510865206): cada dry-run descobriu 78 ficheiros, processou 8 destinos enabled no segundo run e reportou 0 erros; ambos retornaram WOULD_OPEN_PR, pelo que não provam criação de PR real nem permissões de escrita nos consumidores. LICITACAO foi mantido disabled em registry/repositorios-consumidores.json e a PR #4 foi integrada no commit a212d6bf8e26c0b26b7035926a01d2300a1c76b3; o inventário canónico continua a requerer adoção individual. O catálogo de perfis permanece complete:false; a Constituição continua como proposta e políticas operacionais em EM_REVISAO; os cinco critérios finais de fecho permanecem por comprovar. A pontuação continua 80/100 e não é aumentada nesta atualização.

Correção de estado em 2026-10-20: as referências históricas a token rejeitado permanecem apenas como histórico e não representam o último resultado. Nos runs [#45](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39510683461) e [#46](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39510865206), a identidade `carlos-andrade` foi autenticada com sucesso; os dry-runs reportaram 78 ficheiros, 0 erros e `WOULD_OPEN_PR`, sem abrir PRs reais. O roadmap de finalização tem SHA-256 canónico calculado: `5880222a0ee96712aa60ebc08d967a704155f229cf2797e263d0cfebecac2b77`. A Constituição permanece proposta e as políticas continuam em revisão; não foi concedida aprovação normativa implícita por esta atualização. A pontuação permanece 80/100.

Higiene do scorecard (2026-10-21): removido o bloqueio duplicado sobre distribuição por PR real. Mantido um único bloqueio canónico, que distingue explicitamente dry-run autenticado de distribuição real ainda não demonstrada. Nenhum ponto de conclusão foi atribuído.

Atualização 2026-10-21 — roadmap de finalização: registada a evidência do run [#51](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39515702729), que passou após a deduplicação do scorecard; o painel foi sincronizado sem alterar a pontuação 80/100. O roadmap foi atualizado para documentar os cinco workflows atuais do repositório-mestre, a limitação do motor a requisitos `file_exists` e a impossibilidade de comprovar distribuição real por PR a partir dos dry-runs. SHA-256 canónico atual do roadmap (excluindo as linhas de controlo definidas pela norma): `718edec0146bbe8f556b2a71fb095221cca488c3a95b107b8f18f2c3c36473ac`.

Atualização 2026-10-21 — integridade do painel: a automação `automation/sync_project_status.py` passou a recalcular o SHA-256 canónico do README após renderizar o painel, segundo a norma UTF-8/LF e exclusão das duas linhas de controlo. Foi acrescentado teste dedicado; a CI [run #56](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39516044531) passou com 39 testes e `--check` confirmou README/SVG sincronizados. O roadmap foi atualizado com esta evidência; SHA-256 canónico atual do roadmap: `1bb8a67028db068182be0f9b5633a54e1bfdd775c2a5f0c413284209b4408a82`. Pontuação mantém-se em 80/100.

Atualização documental 2026-10-21: README principal atualizado para a versão 1.2.0, com data de atualização 2026-10-21 e referência da versão anterior ao commit `fc1ebf06323d65c919f9a7dd2c741f37a49560e7`. O hash canónico será recalculado pela automação do painel após esta alteração; o estado do documento continua EM_REVISAO até aprovação formal.

Atualização executiva 2026-10-21: o resumo principal do README foi alinhado com o estado canónico de finalização e os bloqueios atuais, removendo a descrição obsoleta de 'proposta inicial'. O estado documental permanece EM_REVISAO até aprovação formal; a pontuação continua 80/100.

Auditoria CI pós-merge 2026-10-21: os workflows [validação F1/F2 #39521270191](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39521270191) e [sincronização #39521269962](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39521269962) falharam. A causa observada em ambos foi `StopIteration` no teste `test_semantic_yaml_field_mismatch_fails_closed`: a alteração do campo `governanca.fonte` faz o esquema rejeitar a configuração antes de o motor avaliar os requisitos do perfil, pelo que o teste não podia encontrar `GOV-SEM-001`. Correção preparada na branch `fix/ci-semantic-test-scorecard`: testar o comparador semântico com um ficheiro YAML de prova independente, mantendo o comportamento fail-closed da configuração oficial. A pontuação mantém-se em 80/100, `fim=0`, e todos os `closure_checks` permanecem false até a CI passar, a sincronização README/SVG ser validada e os gates operacionais/normativos serem aceites. A integração da PR #22 não equivale a validação aprovada.

Revalidação 2026-10-21 — PR #23 integrada: corrigido `test_semantic_yaml_field_mismatch_fails_closed` para testar `yaml_field_equals` num YAML de prova independente, sem alterar o fail-closed do esquema oficial. CI F1/F2 passou no [run 39521820489](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39521820489). A sincronização de README/SVG e a validação final do painel passaram no [run 39521820440](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39521820440), com publicação automática no commit [3bfdf2f01fc49804b9ebf7aab6172b82a851d592](https://github.com/carlos-andrade/GOVERNANCA/commit/3bfdf2f01fc49804b9ebf7aab6172b82a851d592). As falhas anteriores dos runs 39521270191 e 39521269962 permanecem no histórico, mas já não representam o estado da última CI. O scorecard mantém 80/100 e `fim=0`: os restantes gates de distribuição real, ratificação normativa, aceitação WATCHDOG, auditoria dos 42 workflows, adoção individual e aprovação final continuam por demonstrar.

**Evidências:** [CI F1 — esquema e testes do contrato aprovados](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39459837269) · [Especificação F1 — Governance Integration Framework](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/ESPECIFICACAO-GOVERNANCE-INTEGRATION-FRAMEWORK-001.md) · [DEC-GOV-INT-001 — Governance Integration Framework (merged)](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/DEC-GOV-INTEGRATION-FRAMEWORK-001.md) · [Validação CI do scorecard e painel visual a 80% — SUCCESS](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/38981877103) · [Norma de percentual e estados](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md) · [Testes automatizados da barra](https://github.com/carlos-andrade/GOVERNANCA/blob/main/tests/test_sync_project_status.py) · [Workflow de sincronização](https://github.com/carlos-andrade/GOVERNANCA/blob/main/.github/workflows/sync-project-status.yml) · [WATCHDOG — validação técnica](https://github.com/carlos-andrade/GOVERNANCA/actions/workflows/watchdog-validation.yml) · [Gate de aceitação WATCHDOG/B3](https://github.com/carlos-andrade/B3/issues/9) · [Issue de atualidade de dados B3](https://github.com/carlos-andrade/B3/issues/8) · [Relatório do piloto F3 — STOCKS (aceitação pendente)](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/RELATORIO-PILOTO-F3-STOCKS.md) · [CI do catálogo estrutural por perfil — F1/F2 PASS](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39476355134) · [Piloto STOCKS atualizado — catálogo estrutural por perfil, estado DESCONHECIDO](https://github.com/carlos-andrade/STOCKS/actions/runs/39476495677) · [CI de validação adversarial F4 — PASS](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39476819589) · [Piloto STOCKS após hardening F4 — relatório verificado](https://github.com/carlos-andrade/STOCKS/actions/runs/39476916364) · [CI do catálogo estrutural v1.1 e hardening de caminhos — PASS](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39480798454) · [Piloto STOCKS final, catálogo v1.1 — execução PASS; conformidade DESCONHECIDO](https://github.com/carlos-andrade/STOCKS/actions/runs/39481074174) · [PR STOCKS #8 — piloto técnico integrado](https://github.com/carlos-andrade/STOCKS/pull/8) · [Roadmap de finalização GOVERNANCA — gates G0–G7](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-FINALIZACAO-GOVERNANCA.md) · [Dry-run autenticado — 78 ficheiros, 0 erros, resultados WOULD_OPEN_PR](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39510683461) · [Dry-run após LICITACAO ficar disabled — 8 destinos ativos, 0 erros](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39510865206) · [Registo de consumidores com LICITACAO disabled](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json) · [Sincronização do scorecard pós-atualização — 38 testes PASS, README/SVG sincronizados](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39511676636) · [Validação CI F1/F2 pós-integração — PASS](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39511319638) · [Roadmap de finalização atualizado com evidências do run #51 e limitações verificadas](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-FINALIZACAO-GOVERNANCA.md) · [Integridade do painel e 39 testes aprovados — run #56](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39516044531)

> **Fonte de verdade:** `registry/status-do-projeto.json`. O script valida os critérios pontuados e gera este painel Markdown e o SVG. Não editar manualmente este bloco. Uma fase só recebe pontos se tiver evidência; 100% exige aprovação explícita de todos os controlos de encerramento.
<!-- GOVERNANCA_STATUS_END -->

## Distribuição transversal das regras

A distribuição das regras canónicas é orquestrada por [`propagar-regras-governanca.yml`](.github/workflows/propagar-regras-governanca.yml), com registo explícito em [`registry/repositorios-consumidores.json`](registry/repositorios-consumidores.json), script [`automation/propagar_governanca.py`](automation/propagar_governanca.py) e procedimento [`docs/01-governanca/distribuicao-automatica-regras.md`](docs/01-governanca/distribuicao-automatica-regras.md). As atualizações são propostas por Pull Request para revisão local; não existe merge automático. A execução operacional depende do secret `GOVERNANCA_SYNC_TOKEN` e da validação bem-sucedida do workflow.

## Governance Integration Framework

A arquitetura foi formalmente aprovada e integrada através da decisão [DEC-GOV-INT-001 — Governance Integration Framework](docs/01-governanca/DEC-GOV-INTEGRATION-FRAMEWORK-001.md), commit [`7003bd9`](https://github.com/carlos-andrade/GOVERNANCA/commit/7003bd9848983c211aca588e68e5281a5babc39a). A [especificação F1](docs/01-governanca/ESPECIFICACAO-GOVERNANCE-INTEGRATION-FRAMEWORK-001.md), o [JSON Schema](schemas/governanca-config.schema.json), os testes de contrato e o [workflow de validação](.github/workflows/governance-integration-validation.yml) foram integrados após CI aprovada ([run 39459837269](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39459837269)).

**Estado:** arquitetura e F1 integradas; F2–F6 ainda pendentes. A distribuição transversal existente continua sem validação operacional enquanto não forem confirmados `GOVERNANCA_SYNC_TOKEN`, dry-run autenticado e Pull Requests reais nos destinos.

## Começar por aqui

**Monitorização transversal obrigatória:** consulte o [WATCHDOG](WATCHDOG/README.md), o [registo de sistemas monitorizados](WATCHDOG/registry/sistemas-monitorizados.json) e o [workflow de validação](.github/workflows/watchdog-validation.yml). O MVP valida configurações e ficheiros locais; integrações externas e monitorização contínua ainda exigem implementação e testes próprios.

1. Leia [`CONSTITUICAO.md`](CONSTITUICAO.md) e [`docs/00-fundamentos/modelo-operacional.md`](docs/00-fundamentos/modelo-operacional.md).
2. Registe a iniciativa a partir de [`templates/projeto/charter.md`](templates/projeto/charter.md).
3. Classifique risco com [`templates/avaliacao/triagem-risco.md`](templates/avaliacao/triagem-risco.md).
4. Defina resultados mensuráveis, owner, dependências, riscos e critérios de aceitação.
5. Siga os gates G0–G6 descritos em [`docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md`](docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md).
6. Registe decisões, alterações, testes, incidentes e evidências.
7. Antes de produção, utilize [`templates/release/checklist-prontidao.md`](templates/release/checklist-prontidao.md).
8. Desde o início, publique no README do projeto a barra e o percentual usando [`templates/projeto/status-do-projeto.md`](templates/projeto/status-do-projeto.md), conforme a norma [`standards/status-e-percentual-de-conclusao.md`](standards/status-e-percentual-de-conclusao.md).

## Estrutura documental

- `CONSTITUICAO.md` — princípios e autoridade, incluindo a norma transversal WATCHDOG.
- `WATCHDOG/` — política, arquitetura, contratos, inventário, motor de validação, adaptadores, runbooks e testes de monitorização.
- `docs/00-fundamentos/` — modelo operacional, taxonomia e adaptação proporcional.
- `docs/01-governanca/` — papéis, decisões, exceções e estados documentais.
- `docs/02-ciclo-de-vida/` — gates, requisitos e escopo.
- `docs/03-portfolio-e-estrategia/` — priorização.
- `docs/04-arquitetura-e-engenharia/` — padrões e controlo de versão.
- `docs/05-dados-e-ia/` — governança de dados, qualidade, linhagem e IA.
- `docs/06-seguranca-e-privacidade/` — segurança, privacidade e risco.
- `docs/07-operacoes-e-resiliencia/` — observabilidade, continuidade e incidentes.
- `docs/08-qualidade-e-validacao/` — critérios e validação.
- `docs/09-entrega-e-mudanca/` — mudanças e releases.
- `docs/10-fornecedores-e-dependencias/` — terceiros e licenças.
- `docs/11-financas-e-beneficios/` — custos e benefícios.
- `docs/12-conhecimento-e-documentacao/` — conhecimento institucional.
- `docs/13-comunicacao-e-stakeholders/` — comunicação e escalonamento.
- `docs/14-metricas-e-melhoria/` — indicadores e revisão.
- `docs/15-dominios-especializados/` — perfis por tipo de projeto.
- `templates/` — modelos reutilizáveis e checklists, incluindo o estado percentual de conclusão de cada projeto.
- `standards/status-e-percentual-de-conclusao.md` — cálculo uniforme, critérios de evidência e estados de conclusão.
- `standards/` — convenções.
- `registry/` — índices centrais leves.
- `automation/` — especificações para controlos automatizáveis.
- `.github/workflows/watchdog-validation.yml` — validação automatizada do motor WATCHDOG e dos registos locais.
- `examples/` — exemplos não normativos.

## Regras fundamentais

- Todo projeto tem objetivo, responsável, beneficiários e critérios verificáveis.
- O controlo é proporcional ao risco e não dispensa obrigações legais/contratuais.
- Nenhum segredo ou dado pessoal desnecessário deve entrar em Git.
- Nenhum teste, execução ou publicação é declarado sem evidência verificável.
- Exceções têm dono, justificação, aprovador, prazo e plano de resolução.
- O repositório mestre guarda padrões; os repositórios de projeto guardam implementação e evidências específicas.

## Limitações da V1

Não é uma certificação, parecer jurídico, implementação automática de conformidade ou proteção de branch. Os workflows existentes validam os respetivos artefactos quando acionados, mas não substituem monitorização independente 24×7. O WATCHDOG está em fase MVP: verificações locais e testes automatizados estão definidos; adaptadores externos, alertas operacionais, persistência protegida de evidências e supervisão independente ainda precisam de ser implementados e testados. O documento de apoio fornecido sobre modelos de governança de dados é referenciado na política em `docs/05-dados-e-ia/governanca-de-dados.md`.

## Padrão obrigatório de roadmap

O roadmap deste repositório e dos projetos que adotem formalmente estas regras deve seguir o [Roadmap padrão — Governança](ROADMAP-PADRAO-GOVERNANCA.md), nos termos da [Carta/Contrato — padrão obrigatório de roadmap](CARTA-CONTRATO-PADRAO-ROADMAP.md). A existência da norma não certifica automaticamente os repositórios adotantes: cada repositório deve ser inspecionado e validado individualmente.
