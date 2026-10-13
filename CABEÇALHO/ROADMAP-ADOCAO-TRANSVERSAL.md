# Roadmap — adoção transversal do cabeçalho documental

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-ROADMAP-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PLANO |
| **Fase** | Auditoria e adoção transversal |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.3 |
| **SHA-256 (conteúdo canónico)** | a8f9054830903dc45392e6e9ed8594a3bcf73068359460fd2d9420a52208be2e |
| **Commit de referência (versão anterior)** | [32d2e5fdc4756865366ec8e2074ff34caeb0dd5d](https://github.com/carlos-andrade/GOVERNANCA/commit/32d2e5fdc4756865366ec8e2074ff34caeb0dd5d) |
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
| 2 | Validar coerência interna da pasta CABEÇALHO | README, norma, modelo, registo, checklist, histórico e YAML sem contradições; hashes verificados | CONCLUÍDA |
| 3 | Inventariar os documentos Markdown do repositório GOVERNANCA | Inventário com caminho, tipo, estado, presença de cabeçalho, SHA e exceções | CONCLUÍDA — 58 ficheiros listados; 8 conformes estruturalmente e 50 pendentes |
| 4 | Normalizar documentos elegíveis de GOVERNANCA | Cabeçalhos aplicados sem perda de conteúdo; exceções documentadas | PENDENTE — aguarda ratificação explícita do padrão e execução em lotes |
| 5 | Inventariar repositórios de projetos abrangidos | Lista de repositórios, responsáveis, prioridades e evidências de inspeção | PENDENTE |
| 6 | Normalizar por repositório | Alterações publicadas e verificadas individualmente; links e hashes validados | PENDENTE |
| 7 | Validar adoção transversal | Relatório de conformidade por repositório, pendências e exceções | PENDENTE |
| 8 | Ratificar formalmente a norma | Aprovação explícita, autoridade, versão aprovada e data registadas | PENDENTE |

## Registo de execução

| Data | Evidência/atividade | Resultado |
|---|---|---|
| 2026-10-13 | Norma, README, checklist e histórico revistos; exemplo normativo atualizado; SHA-256 recalculado e conferido em sete documentos Markdown | 7/7 hashes canónicos válidos; linhas de controlo presentes; YAML auxiliar não faz parte da contagem de Markdown |
| 2026-10-13 | Inventário recursivo da branch main publicado em CABEÇALHO/INVENTARIO-DOCUMENTAL.md | 58 ficheiros Markdown identificados; 8 com campos canónicos e 50 pendentes de normalização individual |

## Bloqueios e limites

- O inventário do repositório GOVERNANCA foi concluído; falta iniciar a normalização dos 50 documentos pendentes e inventariar os outros repositórios abrangidos.
- Não se deve inferir conformidade de um documento apenas pela existência de um cabeçalho.
- A norma permanece proposta até aprovação formal.
- A normalização deve ser feita em lotes verificáveis, sem alterações em massa não auditadas.

## Próxima ação

Obter ratificação explícita da norma e iniciar a normalização retroativa em lotes auditáveis, começando pelos documentos de governança de GOVERNANCA; preservar o corpo original e registar exceções.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-13 | Criação do roadmap de validação e adoção transversal | Histórico Git |
| 1.0.1 | 2026-10-13 | Registo da validação pós-publicação de sete documentos Markdown e conclusão da revisão interna da pasta CABEÇALHO | Histórico Git |
| 1.0.2 | 2026-10-13 | Inventário dos 57 ficheiros Markdown do repositório; identificados 7 conformes estruturalmente e 50 pendentes de normalização | CABEÇALHO/INVENTARIO-DOCUMENTAL.md |
