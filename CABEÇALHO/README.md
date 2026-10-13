# CABEÇALHO — Estrutura documental canónica

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-README-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | README |
| **Fase** | Validação do padrão |
| **Estado** | PROPOSTA PARA VALIDAÇÃO |
| **Versão** | 1.0.1 |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Finalidade

Esta pasta centraliza o padrão de cabeçalho documental utilizado nos projetos. **O cabeçalho visível dos ficheiros Markdown deve ser escrito em Markdown nativo, compatível com a renderização do GitHub**, usando título, tabela de metadados e secções hierárquicas.

O YAML é apenas um modelo auxiliar opcional para automação ou catalogação. Não substitui o cabeçalho Markdown visível.

## Estrutura

- [NORMA-CABECALHO-PADRAO.md](NORMA-CABECALHO-PADRAO.md) — regras e aplicação.
- [MODELO-DOCUMENTO.md](MODELO-DOCUMENTO.md) — modelo canónico Markdown para GitHub.
- [MODELO-CABECALHO.yml](MODELO-CABECALHO.yml) — metadados YAML auxiliares.
- [REGISTO-TIPOS-DOCUMENTAIS.md](REGISTO-TIPOS-DOCUMENTAIS.md) — tipos documentais.
- [CHECKLIST-VALIDACAO.md](CHECKLIST-VALIDACAO.md) — checklist de validação.
- [HISTORICO.md](HISTORICO.md) — histórico de alterações.

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

O formato foi ajustado para Markdown nativo. A ratificação e a aplicação retroativa dependem de auditoria e aprovação explícita; a existência desta pasta não constitui, por si só, aprovação.
