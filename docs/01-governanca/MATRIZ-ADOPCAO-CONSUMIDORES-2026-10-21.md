# Matriz de adoção dos consumidores — GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-ADOPTION-MATRIX-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | MATRIZ_ADOCAO_CONSUMIDORES |
| **Fase** | G2 — Registo de consumidores e adoção |
| **Estado** | INVENTÁRIO RECONCILIADO; ACEITAÇÕES INDIVIDUAIS PENDENTES |
| **Versão** | 1.0.2 |
| **SHA-256 (conteúdo canónico)** | 3e5b453e8a9152215663e3cd75625988ee848b05c23791b3a557bbb56f582a2f |
| **Commit de referência (versão anterior)** | [86fbd285958c097bd52dfc31836214d0a15836a8](https://github.com/carlos-andrade/GOVERNANCA/commit/86fbd285958c097bd52dfc31836214d0a15836a8) |
| **Data de criação** | 2026-10-21 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente — atualização de inventário; adoção global não aprovada |
| **Origem** | Inspeção do workflow #76 e da STOCKS PR #10 |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md); [DEC-GOV-INT-001](DEC-GOV-INTEGRATION-FRAMEWORK-001.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Registo central de consumidores, run #76, STOCKS PR #10 e UPSTREAM-MANIFEST.json |
| **Escopo** | Oito consumidores ativos e LICITACAO desativado |
| **Objetivo** | Registar estado real de distribuição e adoção, sem inferir conformidade a partir do registo |
| **Dependências** | Idempotência real, revisão humana da PR #10 e aceitação individual dos consumidores |

## 1. Critério de classificação

- **PILOTO_DIAGNOSTICO_PASS / CONFORMIDADE_UNKNOWN**: configuração e piloto técnico existem, mas não demonstram adoção normativa global.
- **SEM_CONFIG_LOCAL / UNKNOWN**: não foi encontrado o diretório `.governanca` na branch `main`; não há evidência local de integração do Governance Integration Framework.
- **DESATIVADO**: consumidor não pode receber distribuição automática até aprovação individual.
- **PASS de adoção** exige configuração local, ref imutável, execução do motor, relatório/hash, revisão humana, PR real e aceitação registada. A mera presença no registo de consumidores não é aceitação.

## 2. Matriz reconciliada

| Repositório | `enabled` no registo | Evidência observada em `main` | Estado de adoção | Próxima ação obrigatória |
|---|---:|---|---|---|
| [B3](https://github.com/carlos-andrade/B3) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR, fixar ref, executar motor e obter aceitação do proprietário; manter WATCHDOG separado até aceitação operacional |
| [DECIO-BAZIN](https://github.com/carlos-andrade/DECIO-BAZIN) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [XFI](https://github.com/carlos-andrade/XFI) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [STOCKS](https://github.com/carlos-andrade/STOCKS) | true | [`.governanca/config.yml`](https://github.com/carlos-andrade/STOCKS/blob/main/.governanca/config.yml), blob SHA `c4f1ea14e4d0f174f8130510a11b435ae1998e43`; `modo: diagnostico`, `perfil: dados`, `exigir_pull_request: true`, `ref: c9be6d5224c7b412aa78a2b1d417b8315e5730f1`; distribuição real por [run #76](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914), com [PR #10](https://github.com/carlos-andrade/STOCKS/pull/10) aberta, ainda fora de `main` | PR_REAL_CRIADA / ACEITAÇÃO_PENDENTE / CONFORMIDADE_UNKNOWN | Sincronizar a origem atual na PR #10; em seguida, sem novo commit na origem, repetir o mesmo run real para confirmar `PR_NO_CHANGE`; rever hashes restantes e obter aceitação do proprietário. Manter conformidade global UNKNOWN |
| [TURISTURIS](https://github.com/carlos-andrade/TURISTURIS) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [LICITACAO](https://github.com/carlos-andrade/LICITACAO) | false | Existe espelho `.governanca/upstream/` e `UPSTREAM-MANIFEST.json` (blob SHA `bd7c33b95fa853ba2b44142a49ef9e53cbf61072`); o destino está desativado no registo central | DESATIVADO — não é adoção aceite | Manter `enabled: false`; só considerar reativação após aprovação local e piloto real por PR |

## 3. Conclusão

- Consumidores ativos registados: 8.
- Adoção global demonstrada: 0.
- Piloto técnico de diagnóstico conhecido: STOCKS; PR #10 aberta após distribuição real, sem certificação global.
- Consumidor desativado: LICITACAO.
- Resultados UNKNOWN: B3, DECIO-BAZIN, XFI, CONSORCIO, STOCKS (conformidade global), TURISTURIS, BLOOMBERG_MAIL e BRICKMASTER_GERAL.

A matriz de inventário fica reconciliada com o registo e com a presença/ausência de configuração observada. **A adoção transversal não fica aprovada**: os consumidores ativos sem configuração continuam bloqueados para certificação; o destino LICITACAO permanece desativado. Cada aceitação exige evidência própria do repositório consumidor.

## 4. Evidências de referência

- [Registo canónico de consumidores](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json)
- [Relatório do piloto F3 — STOCKS](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/RELATORIO-PILOTO-F3-STOCKS.md)
- [Pacote de aceitação e fecho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/governanca/PACOTE-ACEITACAO-E-FECHO.md)
- [PR #4 — LICITACAO desativado no registo](https://github.com/carlos-andrade/GOVERNANCA/pull/4)
- [Run #76 — distribuição real no STOCKS](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914)
- [STOCKS PR #10 — revisão/aceitação pendentes](https://github.com/carlos-andrade/STOCKS/pull/10)

## 5. Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.1 | 2026-10-23 | Inventário atualizado: distribuição real criou a PR #10, com aceitação global ainda pendente. | Proprietário do repositório GOVERNANCA | Run #76; STOCKS PR #10 |
| 1.0.2 | 2026-10-23 | Sequência de execução atualizada para refletir a origem canónica pós-PR #41 e separar sincronização de prova de idempotência. | Proprietário do repositório GOVERNANCA | Run #77; PR #10 |
