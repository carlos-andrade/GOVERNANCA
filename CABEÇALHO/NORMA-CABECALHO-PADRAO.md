# Norma — Cabeçalho documental padrão

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-NORMA-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | NORMA |
| **Fase** | Validação do padrão |
| **Estado** | PROPOSTA PARA VALIDAÇÃO |
| **Versão** | 1.0.2 |
| **SHA-256 (conteúdo canónico)** | 9878fecace3881e5e3ef185bfc604e1bf9c03e72578d1bb10a562d85eb3b1ef1 |
| **Commit de referência (versão anterior)** | [f38a30d19400038c0e10108b750500f952fdeacd](https://github.com/carlos-andrade/GOVERNANCA/commit/f38a30d19400038c0e10108b750500f952fdeacd) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Convenção documental já utilizada nos projetos |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) e políticas da GOVERNANCA |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objetivo

Uniformizar identificação, estado, versão, origem, autoridade e rastreabilidade. O cabeçalho visível dos documentos Markdown deve usar Markdown nativo renderizado pelo GitHub.

## 2. Formato obrigatório para Markdown no GitHub

Cada ficheiro `.md` deve começar com:
1. Um título Markdown de nível 1 (`#`).
2. Uma tabela Markdown de metadados.
3. O corpo organizado por títulos Markdown de nível 2 e 3.

Exemplo canónico:

```markdown
# Título do documento

| Campo | Valor |
|---|---|
| **ID** | PROJ-TIPO-001 |
| **Projeto** | Nome do projeto |
| **Repositório** | [OWNER/REPOSITORY](https://github.com/OWNER/REPOSITORY) |
| **Tipo documental** | RELATORIO |
| **Fase** | FASE_XX |
| **Estado** | RASCUNHO |
| **Versão** | 1.0.0 |
| **Data de criação** | AAAA-MM-DD |
| **Data de atualização** | AAAA-MM-DD |
| **Responsável** | Papel ou responsável |
| **Aprovador** | Pendente ou identificação |
| **Origem** | Referência verificável |
| **Autoridade superior** | Caminho ou URL |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
```

Não usar YAML front matter como substituto do cabeçalho visual em documentos Markdown. YAML pode existir num ficheiro auxiliar ou numa integração específica, mas não substitui a tabela Markdown canónica.

## 3. Metadados

Incluir, quando aplicável: projeto, repositório, tipo, fase, ID, título, estado, versão, datas, responsável, aprovador, origem, autoridade, cadeia de autoridade e rastreabilidade. Escopo, objetivo e dependências podem integrar a tabela quando relevantes.

Quando um campo não for aplicável, registar `N/A — justificação`; não o remover silenciosamente. Documentos `APROVADO` devem identificar a autoridade aprovadora e evidência da aprovação.

## 4. Identificação única

O ID deve ser único e não reutilizável. Recomenda-se prefixo de projeto/domínio, tipo e sequência, por exemplo `GOV-CAB-NORMA-001`.

## 5. Estados documentais

Usar `RASCUNHO`, `EM_REVISAO`, `APROVADO`, `DEPRECADO` ou `REJEITADO`. Não apresentar propostas como normas ratificadas. A aprovação identifica a versão exata e o aprovador autorizado.

## 6. Datas e versões

- Datas no formato ISO `AAAA-MM-DD`.
- Versão `MAJOR.MINOR.PATCH` quando aplicável.
- Atualizar a data após alteração substantiva.
- Rever a versão e o histórico quando houver alteração normativa.
- Não declarar aprovação ou vigência sem evidência.

## 7. Corpo documental

Usar, quando aplicável: Contexto Histórico, Estado, Evidências, Validação, Resultado e Próxima Ação. Podem existir secções técnicas adicionais. Para código e formatos não Markdown, usar o formato de comentário suportado pela linguagem, preservando os metadados essenciais.

## 8. Autoridade e rastreabilidade

Referenciar norma superior, origem, requisitos, decisões, issues, commits, testes e evidências relevantes. Preservar a cadeia `PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO` quando aplicável.

## 9. Aplicação retroativa

Inventariar documentos, classificar tipo e estado, mapear metadados, inserir o cabeçalho sem apagar conteúdo ou histórico, validar links e IDs, registar exceções e publicar evidência de revisão. Não declarar conformidade apenas por inserir um cabeçalho.

## 10. Critérios de aceitação

- ID único e tipo definidos.
- Cabeçalho Markdown renderizado corretamente no GitHub.
- Estado, versão e datas corretos.
- Responsável, origem e autoridade identificáveis.
- Referências verificáveis.
- Secções necessárias presentes.
- Exceções justificadas e histórico preservado.

## 11. Integridade e rastreabilidade por commit

### SHA-256 canónico

Cada documento Markdown deve apresentar o campo **SHA-256 (conteúdo canónico)**. Para calcular o valor, normalizar o ficheiro para UTF-8 com finais de linha LF e calcular SHA-256 sobre o conteúdo integral, removendo antes do cálculo apenas as duas linhas da tabela de metadados intituladas **SHA-256 (conteúdo canónico)** e **Commit de referência (versão anterior)**. Esta regra evita autorreferência e permite que a atualização dos campos de controlo não altere o hash canónico. Qualquer outra alteração ao documento deve resultar num novo hash.

O SHA-256 aqui definido é um checksum canónico do conteúdo segundo esta regra; não é o hash Git do blob nem substitui a verificação de assinatura ou a confiança na origem.

### Commit de referência

Quando disponível, incluir um link para o commit GitHub que introduziu a versão anterior usada como base para esta atualização. O commit que contém a própria alteração não pode ser incluído no mesmo conteúdo sem criar uma referência circular; por isso, o campo aponta para o commit de referência anterior. Em documentos novos, usar `N/A — documento inicial` até existir um commit anterior. O histórico Git continua a ser a fonte autoritativa para o commit atual.

## 12. Limites

Esta norma continua em estado de proposta. A adoção transversal depende de aprovação formal e validação individual dos repositórios.
