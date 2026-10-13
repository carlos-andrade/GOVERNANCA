# Roadmap — adoção transversal do cabeçalho documental

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-ROADMAP-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PLANO |
| **Fase** | Auditoria e adoção transversal |
| **Estado** | EM_REVISAO |
| **Versão** | 1.1.5 |
| **SHA-256 (conteúdo canónico)** | 551d604ce31dd413a453a1be833d3492aeed934bd13ef992efc3fdbf23a932fe |
| **Commit de referência (versão anterior)** | [b55de1f609e33e8b7cd190507e23f0d183cd6622](https://github.com/carlos-andrade/GOVERNANCA/commit/c27f591c6c846de076c34b8451cf0dbc52bacc13) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) e [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Conduzir a validação do padrão Markdown para GitHub, a integridade SHA-256 canónica e a rastreabilidade por commit, sem declarar conformidade antes da inspeção e validação de cada repositório.

## Princípios de execução

- O cabeçalho visível dos ficheiros Markdown é uma tabela Markdown nativa, precedida por título `#`.
- O YAML é auxiliar e não substitui o cabeçalho visível.
- O SHA-256 canónico segue a norma e não é o Git blob SHA.
- O commit de referência aponta para uma versão anterior real, quando disponível; o histórico Git é a autoridade para o commit atual.
- Alterações retroativas preservam o conteúdo substantivo, IDs históricos e histórico de decisões.
- Nenhuma adoção transversal é considerada aprovada sem validação explícita.

## Roadmap

| Fase | Trabalho | Critério de conclusão | Estado |
|---|---|---|---|
| 1 | Definir formato Markdown e campos de integridade | Norma e modelo descrevem o mesmo formato; SHA e commit definidos | CONCLUÍDA |
| 2 | Validar coerência interna da pasta CABEÇALHO | 10/10 documentos Markdown da pasta CABEÇALHO com hashes canónicos verificados; YAML auxiliar excluído da contagem | CONCLUÍDA |
| 3 | Inventariar os documentos Markdown do repositório GOVERNANCA | Inventário com caminho, tipo, estado, presença de cabeçalho, SHA e exceções | CONCLUÍDA — inventário reconciliado para 60 ficheiros: 10 com campos canónicos e 50 pendentes |
| 4 | Normalizar documentos elegíveis de GOVERNANCA | Cabeçalhos aplicados sem perda de conteúdo; exceções documentadas | EM_EXECUÇÃO — L1–L5 aplicados; L6 é o próximo lote |
| 5 | Inventariar repositórios de projetos abrangidos | Lista de repositórios, responsáveis, prioridades e evidências de inspeção | PENDENTE |
| 6 | Normalizar por repositório | Alterações publicadas e verificadas individualmente; links e hashes validados | PENDENTE |
| 7 | Validar adoção transversal | Relatório de conformidade por repositório, pendências e exceções | PENDENTE |
| 8 | Ratificar formalmente a norma | Aprovação explícita, autoridade, versão aprovada e data registadas | CONCLUÍDA — v1.0.3 aprovada em 2026-10-13; registo publicado |

## Registo de execução

| Data | Evidência/atividade | Resultado |
|---|---|---|
| 2026-10-13 | Auditoria da pasta CABEÇALHO | Hash canónico verificado para os 10 documentos Markdown da pasta CABEÇALHO; inventário reconciliado e hashes conferidos após publicação |
| 2026-10-13 | Inventário recursivo da branch main publicado e reconciliado em CABEÇALHO/INVENTARIO-DOCUMENTAL.md | 60 ficheiros Markdown: 10 com campos canónicos e 50 pendentes; contagem do README alinhada |
| 2026-10-13 | Ratificação da Norma v1.0.3 e aplicação L1 | Gate 8 concluído; cabeçalhos de Constituição e README aplicados; inventário atualizado para 61 ficheiros, 13 canónicos e 48 pendentes | [Registo de aprovação](REGISTO-APROVACAO-NORMA-1.0.3.md), [issue #2](https://github.com/carlos-andrade/GOVERNANCA/issues/2), commits `b87b0857` e `ce33acdf` |
| 2026-10-13 | Aplicação L2 | Sete documentos de fundamentos e governança normalizados; inventário atualizado para 20 canónicos e 41 pendentes | Inventário v1.0.5 e commits L2 |
| 2026-10-13 | Aplicação L3 | Cinco documentos de ciclo de vida, portefólio e engenharia normalizados; inventário atualizado para 25 canónicos e 36 pendentes | Inventário v1.0.6 e commits L3 |
| 2026-10-13 | Aplicação L4 | Seis documentos de dados, IA, segurança e privacidade normalizados; inventário atualizado para 31 canónicos e 30 pendentes | Inventário v1.0.7 e commits L4 |
| 2026-10-13 | Classificação não destrutiva dos 50 documentos pendentes registada em [CLASSIFICACAO-PRE-NORMALIZACAO.md](CLASSIFICACAO-PRE-NORMALIZACAO.md); plano de lotes corrigido para 24 documentos centrais e 26 WATCHDOG | Metadados legados e riscos de preservação identificados; nenhuma alteração retroativa aplicada |

## Bloqueios e limites

- A classificação dos 50 documentos pendentes foi concluída sem alterar os documentos auditados; a normalização retroativa continua bloqueada até aprovação formal da norma.
- Não se deve inferir conformidade de um documento apenas pela existência de um cabeçalho.
- A Norma v1.0.3 está aprovada; a aprovação substantiva dos documentos individuais continua separada.
- A normalização deve ser feita em lotes verificáveis, sem alterações em massa não auditadas.

## Próxima ação

Fases 8 e L1 concluídos. L2 aplicado a sete documentos; L3 a cinco documentos; L4 a seis documentos de dados, IA, segurança e privacidade. Inventário reconciliado: 61 ficheiros Markdown, 31 com campos canónicos e 30 pendentes. Próxima ação: reconciliar o plano e iniciar L5.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-13 | Criação do roadmap de validação e adoção transversal | Histórico Git |
| 1.0.1 | 2026-10-13 | Registo da validação pós-publicação de sete documentos Markdown e conclusão da revisão interna da pasta CABEÇALHO | Histórico Git |
| 1.0.2 | 2026-10-13 | Inventário dos 57 ficheiros Markdown do repositório; identificados 7 conformes estruturalmente e 50 pendentes de normalização | CABEÇALHO/INVENTARIO-DOCUMENTAL.md |
| 1.0.3 | 2026-10-13 | Inventário corrigido para 58 ficheiros e 8 com campos canónicos; normalização pendente de ratificação | CABEÇALHO/INVENTARIO-DOCUMENTAL.md |
| 1.0.4 | 2026-10-13 | Registo da classificação não destrutiva dos 50 documentos e correção da contagem dos lotes | CABEÇALHO/CLASSIFICACAO-PRE-NORMALIZACAO.md |
| 1.0.5 | 2026-10-13 | Atualização da contagem documental após publicação do plano e do relatório de classificação | Árvore Git da branch main |
| 1.0.6 | 2026-10-13 | Identificação explícita da reconciliação pendente entre a árvore atual e o inventário-base | Histórico Git |
| 1.0.7 | 2026-10-13 | Reconciliação para 60 documentos e correção do estado de verificação dos hashes recentes | Inventário documental e auditoria da pasta CABEÇALHO |
| 1.0.8 | 2026-10-13 | Registo da verificação independente de quatro hashes e isolamento do hash do inventário como pendência | Cálculo SHA-256 canónico dos documentos publicados |
| 1.0.9 | 2026-10-13 | Fecho da verificação canónica dos dez documentos Markdown da pasta CABEÇALHO | Inventário v1.0.3 e hashes recalculados/conferidos |
| 1.1.0 | 2026-10-13 | Conclusão da Fase 2 e explicitação do único gate imediato: ratificação formal da norma | Verificação canónica e regra de autorização |
| 1.1.1 | 2026-10-13 | Ratificação formal da Norma v1.0.3, conclusão da Fase 8 e início da normalização L1; inventário reconciliado | Registo de aprovação, issue #2 e commits L1 |
| 1.1.2 | 2026-10-13 | L2 aplicado a sete documentos; inventário atualizado para 61 documentos, 20 canónicos e 41 pendentes | Commits L2 e inventário v1.0.5 |

| 2026-10-14 | Aplicação L5 | Quatro documentos de operações, standards e templates normalizados; inventário reconciliado para 35 canónicos e 26 pendentes | Inventário v1.0.8 e validação SHA-256 pós-publicação |
