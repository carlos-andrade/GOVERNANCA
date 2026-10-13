# CABEÇALHO — Estrutura documental canónica

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-README-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | README |
| **Fase** | Validação do padrão |
| **Estado** | PROPOSTA PARA VALIDAÇÃO |
| **Versão** | 1.0.2 |
| **SHA-256 (conteúdo canónico)** | 7a7966e8801ead7dd1e1f3c5b1fb670c65317ced7dadb2c71c2db9300cc1f49d |
| **Commit de referência (versão anterior)** | [d973fa7718f5b723c9121e46c45151d13e4a658e](https://github.com/carlos-andrade/GOVERNANCA/commit/d973fa7718f5b723c9121e46c45151d13e4a658e) |
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
