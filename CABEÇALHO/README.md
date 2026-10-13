# CABEÇALHO — Estrutura documental canónica

**ID:** GOV-CAB-README-001  
**Versão:** 1.0.0  
**Estado:** PROPOSTA PARA VALIDAÇÃO  
**Data de criação:** 2026-10-13  
**Autoridade superior:** [GOVERNANCA](../CONSTITUICAO.md)

## Finalidade

Esta pasta centraliza o padrão de cabeçalho documental já utilizado nos projetos: metadados YAML consistentes, identificação única, estado de aprovação, datas, responsabilidade, origem, autoridade documental e rastreabilidade.

O padrão não cria uma convenção paralela. Consolida os campos e a sequência documental existentes para reutilização controlada nos repositórios.

## Estrutura

- [NORMA-CABECALHO-PADRAO.md](NORMA-CABECALHO-PADRAO.md) — regras obrigatórias, estados e aplicação.
- [MODELO-CABECALHO.yml](MODELO-CABECALHO.yml) — bloco canónico de metadados YAML.
- [MODELO-DOCUMENTO.md](MODELO-DOCUMENTO.md) — documento-base com cabeçalho e secções de conteúdo.
- [REGISTO-TIPOS-DOCUMENTAIS.md](REGISTO-TIPOS-DOCUMENTAIS.md) — tipos de documento e convenções de identificação.
- [CHECKLIST-VALIDACAO.md](CHECKLIST-VALIDACAO.md) — verificação antes de aprovar ou publicar.
- [HISTORICO.md](HISTORICO.md) — histórico de alterações ao padrão.

## Cadeia de autoridade documental

`PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO`

A cadeia identifica a ordem de autoridade e rastreabilidade já utilizada. Um artefacto inferior não pode contrariar uma norma superior aprovada. Uma proposta ou documento em revisão não é tratado como norma ratificada.

## Modelo mínimo

Os campos canónicos estão definidos em `MODELO-CABECALHO.yml`. O conteúdo de cada documento deve preservar, quando aplicável, as secções: Contexto Histórico, Estado, Evidências, Validação, Resultado e Próxima Ação.

## Regra de adoção

1. Identificar a versão do padrão adotada.
2. Aplicar o cabeçalho a documentos novos.
3. Ao rever documentos existentes, acrescentar ou normalizar metadados sem apagar o histórico nem alterar silenciosamente o conteúdo substantivo.
4. Validar IDs, estado documental, datas, responsável, origem, autoridade e ligações de rastreabilidade.
5. Registar exceções justificadas e aprovadas.
6. Não declarar adoção transversal antes da aplicação e validação em cada repositório.

## Estado de validação

A estrutura foi criada no repositório mestre. A sua ratificação e a aplicação retroativa a todos os documentos dependem da auditoria e de aprovação explícita; a existência desta pasta não constitui, por si só, essa aprovação.
