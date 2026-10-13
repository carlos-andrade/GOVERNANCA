# Plano de lotes — normalização documental

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-LOTES-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PLANO_EXECUCAO |
| **Fase** | Preparação da normalização |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.2 |
| **SHA-256 (conteúdo canónico)** | 122450589f03ba7a7710c87d1858a9085b6fcbfe28855a16e0cfd77824ee23bb |
| **Commit de referência (versão anterior)** | [7be3b4162495922ce12f3c4f1c02813618b57489](https://github.com/carlos-andrade/GOVERNANCA/commit/7be3b4162495922ce12f3c4f1c02813618b57489) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) e [CONSTITUICAO.md](../CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Preparar a normalização dos 48 ficheiros Markdown ainda pendentes no [inventário documental](INVENTARIO-DOCUMENTAL.md), com lotes pequenos e critérios verificáveis. Este plano não ratifica a norma nem autoriza alterações retroativas.

## Gate de autorização

A Norma de Cabeçalho Documental Padrão, versão 1.0.3, foi formalmente aprovada pelo proprietário em 2026-10-13. A evidência está no [registo de aprovação](REGISTO-APROVACAO-NORMA-1.0.3.md) e na [issue #2](https://github.com/carlos-andrade/GOVERNANCA/issues/2). O gate está satisfeito; a normalização prossegue por lotes com validação individual.

L1 foi aplicado a `CONSTITUICAO.md` e `README.md`. Os 48 documentos restantes serão tratados por lotes. Não alterar estados substantivos, inventar IDs históricos ou declarar conformidade sem evidência.

## Lotes propostos

| Lote | Âmbito | Ficheiros previstos | Regra especial |
|---|---|---:|---|
| L1 | Constituição e entrada do repositório | 2 | Tratar `CONSTITUICAO.md` como autoridade superior; preservar metadados históricos do `README.md` |
| L2 | Fundamentos e governança | 7 | Preservar significado normativo e decisões existentes |
| L3 | Ciclo de vida, portefólio e engenharia | 5 | Preservar requisitos, arquitetura e histórico |
| L4 | Dados, IA, segurança e privacidade | 6 | Não inventar requisitos ou aprovações |
| L5 | Operações, standards e templates | 4 | Preservar procedimentos e critérios existentes |
| L6 | WATCHDOG — arquitetura, normas e operação | 16 | Preservar contratos técnicos, políticas e runbooks |
| L7 | WATCHDOG — adaptadores, relatórios e testes | 10 | Preservar exemplos e estrutura operacional |

Os totais corrigidos refletem 24 documentos centrais e 26 documentos WATCHDOG, totalizando 50 pendentes. Os totais são uma proposta de agrupamento. Antes de cada lote, reconciliar os caminhos com o inventário atual; se houver divergência, corrigir o plano antes de editar.

## Procedimento e aceitação

1. Obter a versão atual e blob SHA antes de editar.
2. Mapear apenas metadados sustentados pelo documento ou histórico Git.
3. Preservar o corpo substantivo e os IDs existentes.
4. Registar dados desconhecidos como `N/A — justificação`; não inferir aprovação.
5. Aplicar cabeçalho Markdown nativo e recalcular o SHA-256 canónico segundo a norma.
6. Validar commit anterior, links, IDs, renderização e diff.
7. Atualizar inventário e roadmap somente após verificação da publicação.
8. Parar perante perda de conteúdo, conflito de metadados, link inválido ou hash divergente.

## Estado e próxima ação

**Estado:** gate de aprovação satisfeito; L1 concluído. Inventário atual: 61 ficheiros Markdown, 13 com campos canónicos e 48 pendentes.

**Classificação não destrutiva:** registada em [CLASSIFICACAO-PRE-NORMALIZACAO.md](CLASSIFICACAO-PRE-NORMALIZACAO.md). **L1:** concluído; GOV-001, versão e estado da Constituição preservados, assim como os marcadores automáticos do README. **Próxima ação:** iniciar L2 após reconciliar os caminhos com o inventário.

## Histórico

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | 2026-10-13 | Plano inicial de lotes e gates |
| 1.0.1 | 2026-10-13 | Contagem dos lotes corrigida e classificação não destrutiva concluída | CABEÇALHO/CLASSIFICACAO-PRE-NORMALIZACAO.md |

| 1.0.2 | 2026-10-13 | Aprovação formal satisfeita e L1 concluído; 48 documentos permanecem pendentes | Registo de aprovação, commits L1 e inventário v1.0.4 |
