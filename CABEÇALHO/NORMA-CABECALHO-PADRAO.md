# Norma — Cabeçalho documental padrão

**ID:** GOV-CAB-NORMA-001  
**Versão:** 1.0.0  
**Estado:** PROPOSTA PARA VALIDAÇÃO  
**Data de criação:** 2026-10-13  
**Data de revisão:** 2026-10-13  
**Responsável:** Proprietário do repositório GOVERNANCA  
**Aprovador:** Pendente de aprovação formal  
**Origem:** Convenção documental já utilizada nos projetos do utilizador  
**Autoridade superior:** `CONSTITUICAO.md` e políticas documentais da GOVERNANCA  
**Cadeia de autoridade:** `PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO`

## 1. Objetivo

Uniformizar a identificação, o estado, a versão, a origem, a autoridade e a rastreabilidade de documentos em GOVERNANCA e, após validação, nos demais repositórios.

## 2. Regra de não duplicação

Este documento consolida a convenção existente. Não devem ser criados padrões concorrentes com campos equivalentes sem decisão registada. Quando um repositório já possuir um cabeçalho compatível, adaptar por mapeamento dos campos e preservar a informação válida; não substituir por uma variante local incompatível.

## 3. Metadados canónicos

Cada documento deve incluir, em YAML no início do ficheiro Markdown, os campos aplicáveis definidos no modelo:

- `projeto`
- `repositorio`
- `tipo_documento`
- `fase`
- `id_documento`
- `titulo`
- `status`
- `versao`
- `data_criacao`
- `data_atualizacao`
- `origem`
- `autoridade_documental`
- `cadeia_autoridade`
- `rastreabilidade`
- `escopo`
- `objetivo`
- `dependencias`

Os campos não aplicáveis devem ser explicitamente indicados como `"N/A — justificação"`; não devem ser removidos silenciosamente. Campos como aprovador, data de aprovação, vigência e próxima revisão são obrigatórios para documentos em estado `APROVADO`.

## 4. Identificação única

O `id_documento` deve ser único no âmbito definido pelo registo documental. Recomenda-se um prefixo de projeto/domínio, tipo e sequência, por exemplo `GOV-CAB-NORMA-001`. Não reutilizar IDs de documentos eliminados, substituídos ou depreciados.

## 5. Estados documentais

Usar os estados de conformidade documental já definidos em GOVERNANCA:

- `RASCUNHO`
- `EM_REVISAO`
- `APROVADO`
- `DEPRECADO`
- `REJEITADO`

Um documento não pode ser apresentado como norma ratificada quando estiver em `RASCUNHO` ou `EM_REVISAO`. Documentos de alto impacto não devem ser autoaprovados pelo autor. A aprovação deve identificar a versão exata e o aprovador autorizado.

## 6. Datas e versões

- Datas em formato ISO `AAAA-MM-DD`.
- Versões no formato `MAJOR.MINOR.PATCH` quando o documento exigir versionamento semântico.
- `data_atualizacao` deve refletir a última alteração substantiva ao documento.
- Uma alteração de conteúdo normativo exige revisão da versão e do histórico.
- Não declarar aprovação, vigência ou revisão concluída sem evidência.

## 7. Corpo documental

Após o cabeçalho, usar quando aplicável esta sequência de secções:

1. Contexto Histórico
2. Estado
3. Evidências
4. Validação
5. Resultado
6. Próxima Ação

Podem ser acrescentadas secções técnicas específicas, mantendo rastreabilidade e sem omitir secções necessárias à natureza do documento. Para código-fonte, configurações e formatos que não aceitem front matter, usar o cabeçalho equivalente suportado pela linguagem e manter os mesmos metadados essenciais.

## 8. Autoridade e rastreabilidade

O cabeçalho deve apontar para a fonte normativa superior, documento de origem, requisitos, decisões, issues, commits, testes ou evidências relevantes. A cadeia `PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO` deve ser preservada quando aplicável.

## 9. Aplicação a documentos existentes

A normalização retroativa deve ser feita em lotes auditáveis:

1. inventariar documentos;
2. classificar tipo, estado e autoridade;
3. mapear os metadados existentes;
4. adicionar o cabeçalho sem eliminar conteúdo ou histórico;
5. validar links, IDs, datas e estados;
6. registar exceções e documentos não aplicáveis;
7. publicar o resultado com evidência de revisão.

Não marcar toda a documentação como conforme apenas por inserir um bloco YAML.

## 10. Critérios de aceitação

- O documento tem ID único e tipo definido.
- O estado corresponde à aprovação real.
- Versão e datas são válidas.
- Responsável, origem e autoridade são identificáveis.
- A rastreabilidade aponta para referências existentes quando declaradas.
- O corpo tem as secções necessárias ao tipo documental.
- Exceções são justificadas e aprovadas.
- O histórico é preservado.

## 11. Limites

A publicação desta norma em estado de proposta não significa ratificação formal nem adoção automática por outros repositórios. A adoção transversal requer aprovação do padrão e validação individual dos repositórios.
