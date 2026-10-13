# Inventário de repositórios abrangidos pela governança

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-REPOS-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | INVENTARIO |
| **Fase** | Fase 5 — inventário transversal de repositórios |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 817ae4cd3129df85641c9f39758fb788f996f50287b1590b9fe29abcdda859b9 |
| **Commit de referência (versão anterior)** | N/A — documento criado nesta execução |
| **Data de criação** | 2026-10-14 |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste inventário |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) e [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo e limites

Registar os repositórios de projetos candidatos à adoção da norma de cabeçalho do GOVERNANCA, priorizar a inspeção e manter evidência verificável. A existência do repositório foi confirmada através dos metadados do GitHub em 2026-10-14 quando assinalada como confirmada abaixo; isso **não** significa que o conteúdo tenha sido auditado nem que a norma tenha sido aplicada.

A prioridade é operacional e provisória, não uma aprovação de escopo. A adoção só será declarada após inspeção dos ficheiros Markdown, comparação com a norma, verificação de hashes/links e registo dos resultados por repositório.

## Inventário inicial

| Repositório | Prioridade inicial | Existência no GitHub | Responsável de referência | Estado de adoção | Próxima ação |
|---|---|---|---|---|---|
| [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) | P0 — norma central | Confirmada; branch `main` | Proprietário do repositório | Norma aprovada; 62 ficheiros Markdown inventariados após inclusão deste registo | Executar auditoria final e manter controlos sincronizados |
| [STOCKS](https://github.com/carlos-andrade/STOCKS) | P1 — projeto ativo | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inventariar Markdown e identificar controlos locais |
| [DECIO-BAZIN](https://github.com/carlos-andrade/DECIO-BAZIN) | P1 — projeto ativo | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar estrutura, README e documentação normativa |
| [B3](https://github.com/carlos-andrade/B3) | P1 — dados e mercado | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar documentação e pipelines de dados |
| [BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL) | P1 — ingestão de dados | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar workflows, documentação e evidências operacionais |
| [TURISTURIS](https://github.com/carlos-andrade/TURISTURIS) | P1 — dados e publicação | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar normas de captura, estrutura e publicação |
| [XFI](https://github.com/carlos-andrade/XFI) | P1 — infraestrutura e operações | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar documentação de infraestrutura e monitorização |
| [PROMPT_CHATGPT_CLAUDE](https://github.com/carlos-andrade/PROMPT_CHATGPT_CLAUDE) | P1 — cadeia de prompts | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Comparar regras de prompts e autoridade documental |
| [BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) | P1 — estratégia de trading | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar especificações, versões e evidências de testes |
| [FVG-ATLAS](https://github.com/carlos-andrade/FVG-ATLAS) | P1 — engenharia de dados de mercado | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar documentação técnica e rastreabilidade |
| [BITCOIN](https://github.com/carlos-andrade/BITCOIN) | P2 — projeto técnico | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inventariar Markdown e classificar risco |
| [PROJETO-COM-RASPBERRY](https://github.com/carlos-andrade/PROJETO-COM-RASPBERRY) | P2 — projeto técnico | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inventariar Markdown e documentação de operação |
| [CURSO_GITHUB](https://github.com/carlos-andrade/CURSO_GITHUB) | P2 — formação | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar materiais, modelos e status de conclusão |
| [KDP](https://github.com/carlos-andrade/KDP) | P2 — publicação editorial | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar guias, templates e metadados editoriais |
| [O-ULTIMO-CIGARRO](https://github.com/carlos-andrade/O-ULTIMO-CIGARRO) | P2 — conteúdo editorial | Confirmada; branch `main` | Proprietário do repositório | PENDENTE DE INSPEÇÃO | Inspecionar estrutura editorial e modelos de capítulo |
| [BRICKMASTER-CLAUDE](https://github.com/carlos-andrade/BRICKMASTER-CLAUDE) | A confirmar | Não confirmado; GitHub devolveu 404 para consulta de metadados | Proprietário do repositório | BLOQUEADO — existência/acesso não confirmados | Confirmar URL ou nome correto antes de incluir no escopo |

## Critérios de inspeção por repositório

1. Confirmar URL, branch principal, acessibilidade e responsável.
2. Inventariar todos os ficheiros Markdown e distinguir documentação normativa, técnica, operacional e editorial.
3. Verificar cabeçalho canónico, ID único, versão, estado, autoridade, origem e commit de referência.
4. Recalcular SHA-256 canónico segundo a norma; não confundir com Git blob SHA.
5. Registar cobertura, exceções, ficheiros sem necessidade de cabeçalho e riscos de alteração.
6. Aplicar a norma apenas após o gate de autorização aplicável, preservando o corpo substantivo.
7. Atualizar este inventário com a evidência da inspeção e commits reais. Não inferir adoção pela mera existência de README.

## Próxima sequência

1. Inspecionar os repositórios P1, começando por STOCKS, DECIO-BAZIN, B3, BLOOMBERG_MAIL, TURISTURIS, XFI, PROMPT_CHATGPT_CLAUDE, BRICKMASTER_GERAL e FVG-ATLAS.
2. Para cada repositório, produzir uma linha de base antes de alterar ficheiros.
3. Registar resultados e exceções; só depois planear lotes de normalização por repositório.
4. Rever os candidatos P2 após a primeira ronda P1.
