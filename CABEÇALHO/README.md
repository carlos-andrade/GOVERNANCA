# CABEÇALHO — Estrutura documental canónica

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-README-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | README |
| **Fase** | Validação do padrão |
| **Estado** | PROPOSTA PARA VALIDAÇÃO |
| **Versão** | 1.0.5 |
| **SHA-256 (conteúdo canónico)** | cea7a721befe5fb2506caff6d572c1a1e57753babef92691b413675d64d3be2d |
| **Commit de referência (versão anterior)** | [6f74c89881696609cd01d3c848a31fc131361c29](https://github.com/carlos-andrade/GOVERNANCA/commit/6f74c89881696609cd01d3c848a31fc131361c29) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Finalidade

Esta pasta centraliza o padrão de cabeçalho documental utilizado nos projetos. **O cabeçalho visível dos ficheiros Markdown deve ser escrito em Markdown nativo, compatível com a renderização do GitHub**, usando título, tabela de metadados e secções hierárquicas.

O YAML é apenas um modelo auxiliar opcional para automação ou catalogação. Não substitui o cabeçalho Markdown visível.

O cabeçalho inclui também um **SHA-256 canónico** para verificação de integridade e um **commit de referência** para navegação até à versão anterior. O algoritmo e as limitações estão definidos na norma.

## Estrutura

- [NORMA-CABECALHO-PADRAO.md](NORMA-CABECALHO-PADRAO.md) — regras e aplicação.
- [MODELO-DOCUMENTO.md](MODELO-DOCUMENTO.md) — modelo canónico Markdown para GitHub.
- [MODELO-CABECALHO.yml](MODELO-CABECALHO.yml) — metadados YAML auxiliares.
- [REGISTO-TIPOS-DOCUMENTAIS.md](REGISTO-TIPOS-DOCUMENTAIS.md) — tipos documentais.
- [CHECKLIST-VALIDACAO.md](CHECKLIST-VALIDACAO.md) — checklist de validação.
- [HISTORICO.md](HISTORICO.md) — histórico de alterações.
- [INVENTARIO-DOCUMENTAL.md](INVENTARIO-DOCUMENTAL.md) — inventário dos 57 ficheiros Markdown e estado estrutural do cabeçalho.
- [ROADMAP-ADOCAO-TRANSVERSAL.md](ROADMAP-ADOCAO-TRANSVERSAL.md) — fases e critérios de adoção.

## Cadeia de autoridade

`PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO`

## Regra de adoção

1. Usar o cabeçalho Markdown definido em `MODELO-DOCUMENTO.md` nos ficheiros Markdown.
2. Usar YAML apenas quando necessário para integração automática.
3. Ao rever documentos existentes, normalizar os metadados sem apagar o histórico nem alterar silenciosamente o conteúdo.
4. Validar IDs, estado, datas, responsável, origem, autoridade e rastreabilidade.
5. Registar exceções justificadas.
6. Não declarar adoção transversal antes da validação em cada repositório.

## Estado de validação

O formato foi ajustado para Markdown nativo. O inventário inicial identificou 58 ficheiros Markdown: 8 com campos canónicos presentes e 50 pendentes de normalização individual. A ratificação e a aplicação retroativa dependem de auditoria e aprovação explícita; a existência desta pasta não constitui, por si só, aprovação.

## Roadmap de adoção

Consultar [ROADMAP-ADOCAO-TRANSVERSAL.md](ROADMAP-ADOCAO-TRANSVERSAL.md) para fases, critérios de conclusão, evidências e pendências da adoção nos repositórios. A conformidade só é declarada após inventário, verificação e registo por repositório.
