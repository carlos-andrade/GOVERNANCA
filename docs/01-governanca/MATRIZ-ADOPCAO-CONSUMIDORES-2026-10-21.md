# Matriz de adoção dos consumidores — GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-ADOPTION-MATRIX-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | MATRIZ_ADOCAO_CONSUMIDORES |
| **Fase** | G2 — Registo de consumidores e adoção |
| **Estado** | INVENTÁRIO RECONCILIADO; ACEITAÇÕES INDIVIDUAIS PENDENTES |
| **Versão** | 1.0.3 |
| **SHA-256 (conteúdo canónico)** | cf322e3324d34dde73178d5670b94f60b5b0d927b2dd70a3a315b6c250d800d2 |
| **Commit de referência (versão anterior)** | [7858580a1c9d42e70fabb18a4a12118c364d1339](https://github.com/carlos-andrade/GOVERNANCA/commit/7858580a1c9d42e70fabb18a4a12118c364d1339) |
| **Data de criação** | 2026-10-21 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente — atualização de inventário; adoção global não aprovada |
| **Origem** | Inspeção dos workflows #76/#78, integração da STOCKS PR #10 e manifesto atual em STOCKS/main |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md); [DEC-GOV-INT-001](DEC-GOV-INTEGRATION-FRAMEWORK-001.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Registo central, runs #76/#78, STOCKS PR #10, commit de merge e UPSTREAM-MANIFEST.json |
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
| [STOCKS](https://github.com/carlos-andrade/STOCKS) | true | [`.governanca/config.yml`](https://github.com/carlos-andrade/STOCKS/blob/main/.governanca/config.yml); PR #10 integrada em `8d6967b8a95eb282c5538e354bef8dd9ebd29778`; manifesto ainda aponta para origem `e54c3ca24b04971f39a5c804beedc21ff1aff355`, anterior à `main` atual da GOVERNANCA `7858580a1c9d42e70fabb18a4a12118c364d1339`; run #78 foi dry-run | PR_INTEGRADA / ESPELHO_DESATUALIZADO / ACEITAÇÃO_PENDENTE / CONFORMIDADE_UNKNOWN | Executar dispatch real limitado ao STOCKS para sincronizar a origem atual; validar hashes e repetir sem alteração da origem para comprovar idempotência; obter aceitação formal. Não certificar conformidade global |
| [TURISTURIS](https://github.com/carlos-andrade/TURISTURIS) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [LICITACAO](https://github.com/carlos-andrade/LICITACAO) | false | Existe espelho `.governanca/upstream/` e `UPSTREAM-MANIFEST.json` (blob SHA `bd7c33b95fa853ba2b44142a49ef9e53cbf61072`); o destino está desativado no registo central | DESATIVADO — não é adoção aceite | Manter `enabled: false`; só considerar reativação após aprovação local e piloto real por PR |

## 3. Conclusão

- Consumidores ativos registados: 8.
- Adoção global demonstrada: 0.
- Piloto de distribuição real: STOCKS PR #10 integrada, mas manifesto upstream desatualizado; aceitação formal e conformidade global continuam pendentes.
- Consumidor desativado: LICITACAO.
- Resultados UNKNOWN: B3, DECIO-BAZIN, XFI, CONSORCIO, STOCKS (conformidade global), TURISTURIS, BLOOMBERG_MAIL e BRICKMASTER_GERAL.

A matriz de inventário fica reconciliada com o registo e com a presença/ausência de configuração observada. **A adoção transversal não fica aprovada**: os consumidores ativos sem configuração continuam bloqueados para certificação; o destino LICITACAO permanece desativado. Cada aceitação exige evidência própria do repositório consumidor.

## 4. Evidências de referência

- [Registo canónico de consumidores](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json)
- [Relatório do piloto F3 — STOCKS](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/RELATORIO-PILOTO-F3-STOCKS.md)
- [Pacote de aceitação e fecho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/governanca/PACOTE-ACEITACAO-E-FECHO.md)
- [PR #4 — LICITACAO desativado no registo](https://github.com/carlos-andrade/GOVERNANCA/pull/4)
- [Run #76 — distribuição real no STOCKS](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39964100914)
- [STOCKS PR #10 — integrada; manifesto ainda desatualizado](https://github.com/carlos-andrade/STOCKS/pull/10)
- [Run #78 — dry-run automático](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39967268661)

## 5. Histórico de alterações

| Versão | Data | Alteração | Responsável | Evidência |
|---|---|---|---|---|
| 1.0.1 | 2026-10-23 | Inventário atualizado: distribuição real criou a PR #10, com aceitação global ainda pendente. | Proprietário do repositório GOVERNANCA | Run #76; STOCKS PR #10 |
| 1.0.2 | 2026-10-23 | Sequência de execução atualizada para refletir a origem canónica pós-PR #41 e separar sincronização de prova de idempotência. | Proprietário do repositório GOVERNANCA | Run #77; PR #10 |
| 1.0.3 | 2026-10-23 | PR #10 integrada; manifesto continua na origem e54c3ca; run #78 apenas dry-run. Nova propagação real pendente. | Proprietário do repositório GOVERNANCA | Merge commit 8d6967b8; run #78 |
