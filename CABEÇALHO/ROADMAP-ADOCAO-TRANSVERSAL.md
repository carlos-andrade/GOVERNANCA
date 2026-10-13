# Roadmap — adoção transversal do cabeçalho documental

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-ROADMAP-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PLANO |
| **Fase** | Auditoria e adoção transversal |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a06196595270793919c402f4c6a0b093a81b78927d53fbde4364313c1b1d0704 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-13 |
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
| 2 | Validar coerência interna da pasta CABEÇALHO | README, norma, modelo, registo, checklist, histórico e YAML sem contradições; hashes verificados | EM_EXECUÇÃO |
| 3 | Inventariar os documentos Markdown do repositório GOVERNANCA | Inventário com caminho, tipo, estado, presença de cabeçalho, SHA e exceções | PENDENTE |
| 4 | Normalizar documentos elegíveis de GOVERNANCA | Cabeçalhos aplicados sem perda de conteúdo; exceções documentadas | PENDENTE |
| 5 | Inventariar repositórios de projetos abrangidos | Lista de repositórios, responsáveis, prioridades e evidências de inspeção | PENDENTE |
| 6 | Normalizar por repositório | Alterações publicadas e verificadas individualmente; links e hashes validados | PENDENTE |
| 7 | Validar adoção transversal | Relatório de conformidade por repositório, pendências e exceções | PENDENTE |
| 8 | Ratificar formalmente a norma | Aprovação explícita, autoridade, versão aprovada e data registadas | PENDENTE |

## Registo de execução

| Data | Evidência/atividade | Resultado |
|---|---|---|
| 2026-10-13 | Norma, README, checklist e histórico revistos para coerência do SHA-256 e commit de referência; exemplo normativo atualizado | Publicações efetuadas; verificação pós-publicação pendente |

## Bloqueios e limites

- Não foi concluído um inventário integral de todos os documentos Markdown do repositório nem dos repositórios associados.
- Não se deve inferir conformidade de um documento apenas pela existência de um cabeçalho.
- A norma permanece proposta até aprovação formal.
- A normalização deve ser feita em lotes verificáveis, sem alterações em massa não auditadas.

## Próxima ação

Concluir a validação pós-publicação dos documentos da pasta CABEÇALHO; depois inventariar os ficheiros Markdown de GOVERNANCA e registar os resultados antes de alterar outros documentos.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-13 | Criação do roadmap de validação e adoção transversal | Histórico Git |
