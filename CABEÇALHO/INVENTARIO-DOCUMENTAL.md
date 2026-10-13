# Inventário documental Markdown — GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-INV-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | INVENTARIO |
| **Fase** | Auditoria documental |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.5 |
| **SHA-256 (conteúdo canónico)** | 608b9ff32bdf705ccd3097773da93177e32a830ba9dc12ded3d6ea4965824abf |
| **Commit de referência (versão anterior)** | [81596ce47122d8eae6d998365ff574cb330e8628](https://github.com/carlos-andrade/GOVERNANCA/commit/81596ce47122d8eae6d998365ff574cb330e8628) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo e âmbito

Inventariar todos os ficheiros Markdown presentes na árvore Git recursiva da branch `main`, classificar a presença dos elementos centrais do cabeçalho canónico e preparar a normalização controlada. Este inventário cobre ficheiros com extensão `.md`; não avalia ficheiros YAML, JSON, código ou binários.

## Método

- Fonte: árvore Git recursiva do repositório `main`, inspecionada em 2026-10-13.
- Total identificado após inclusão do registo de aprovação e aplicação do L1 e L2: **61 ficheiros Markdown**.
- Critério de conformidade inicial: título Markdown, tabela de metadados `Campo | Valor`, linha SHA-256 canónico e linha de commit de referência.
- Os documentos com campos canónicos foram verificados quanto à presença dos campos; os hashes canónicos dos 11 documentos Markdown da pasta `CABEÇALHO` foram recalculados ou conferidos nesta revisão.
- A classificação é estrutural, não uma aprovação substantiva do conteúdo.
- Ficheiros de modelo, como `CABEÇALHO/MODELO-DOCUMENTO.md`, podem conter marcadores de preenchimento; a conformidade do modelo não torna automaticamente conformes os documentos criados a partir dele.

## Resumo

| Resultado | Quantidade |
|---|---:|
| Ficheiros Markdown inventariados | 61 |
| Com campos canónicos presentes | 20 |
| A normalizar ou avaliar individualmente | 41 |
| Cobertura estrutural do padrão | 32,8% |

## Inventário completo

| Caminho | Resultado da auditoria estrutural |
|---|---|
| `CABEÇALHO/CHECKLIST-VALIDACAO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/HISTORICO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/MODELO-DOCUMENTO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/NORMA-CABECALHO-PADRAO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/README.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/REGISTO-TIPOS-DOCUMENTAIS.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/REGISTO-APROVACAO-NORMA-1.0.3.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/ROADMAP-ADOCAO-TRANSVERSAL.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/INVENTARIO-DOCUMENTAL.md` | CONFORME — campos canónicos presentes (este inventário) |
| `CABEÇALHO/PLANO-LOTES-NORMALIZACAO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/CLASSIFICACAO-PRE-NORMALIZACAO.md` | CONFORME — campos canónicos presentes |
| `CONSTITUICAO.md` | CABEÇALHO APLICADO — GOV-001 e estado de proposta preservados |
| `README.md` | CABEÇALHO APLICADO — marcadores de automação preservados |
| `WATCHDOG/CARTA-WATCHDOG.md` | PENDENTE — normalização necessária |
| `WATCHDOG/README.md` | PENDENTE — normalização necessária |
| `WATCHDOG/adapters/aplicacoes/README.md` | PENDENTE — normalização necessária |
| `WATCHDOG/adapters/dados/README.md` | PENDENTE — normalização necessária |
| `WATCHDOG/adapters/github-actions/README.md` | PENDENTE — normalização necessária |
| `WATCHDOG/adapters/infraestrutura/README.md` | PENDENTE — normalização necessária |
| `WATCHDOG/adapters/processos/README.md` | PENDENTE — normalização necessária |
| `WATCHDOG/arquitetura/arquitetura-geral.md` | PENDENTE — normalização necessária |
| `WATCHDOG/arquitetura/modelo-de-execucao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/arquitetura/modelo-de-integracao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/docs/configuracao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/docs/instalacao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/docs/operacao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/normas/classificacao-de-estados.md` | PENDENTE — normalização necessária |
| `WATCHDOG/normas/evidencias-e-auditoria.md` | PENDENTE — normalização necessária |
| `WATCHDOG/normas/politica-de-monitorizacao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/normas/recuperacao-e-remediacao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/normas/seguranca-e-privacidade.md` | PENDENTE — normalização necessária |
| `WATCHDOG/normas/severidade-e-escalonamento.md` | PENDENTE — normalização necessária |
| `WATCHDOG/registry/adocao-transversal.md` | PENDENTE — normalização necessária |
| `WATCHDOG/reports/exemplos/README.md` | PENDENTE — normalização necessária |
| `WATCHDOG/reports/modelos/relatorio-de-execucao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/roadmap-de-implementacao.md` | PENDENTE — normalização necessária |
| `WATCHDOG/runbooks/incidente-critico.md` | PENDENTE — normalização necessária |
| `WATCHDOG/runbooks/operacao-de-alertas-e-sla.md` | PENDENTE — normalização necessária |
| `WATCHDOG/tests/README.md` | PENDENTE — normalização necessária |
| `docs/00-fundamentos/modelo-operacional.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/00-fundamentos/principios-de-adaptacao.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/00-fundamentos/taxonomia-e-glossario.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/01-governanca/papeis-e-responsabilidades.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/01-governanca/politica-de-conformidade-documental.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/01-governanca/politica-de-decisoes.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/01-governanca/politica-de-excecoes.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md` | PENDENTE — normalização necessária |
| `docs/02-ciclo-de-vida/gestao-de-requisitos-e-escopo.md` | PENDENTE — normalização necessária |
| `docs/03-portfolio-e-estrategia/priorizacao-de-portfolio.md` | PENDENTE — normalização necessária |
| `docs/04-arquitetura-e-engenharia/arquitetura-e-padroes.md` | PENDENTE — normalização necessária |
| `docs/04-arquitetura-e-engenharia/controle-de-versao-e-revisao.md` | PENDENTE — normalização necessária |
| `docs/05-dados-e-ia/governanca-de-dados.md` | PENDENTE — normalização necessária |
| `docs/05-dados-e-ia/qualidade-e-linhagem.md` | PENDENTE — normalização necessária |
| `docs/05-dados-e-ia/uso-responsavel-de-ia.md` | PENDENTE — normalização necessária |
| `docs/06-seguranca-e-privacidade/gestao-de-risco.md` | PENDENTE — normalização necessária |
| `docs/06-seguranca-e-privacidade/politica-de-seguranca.md` | PENDENTE — normalização necessária |
| `docs/06-seguranca-e-privacidade/privacidade-e-dados-pessoais.md` | PENDENTE — normalização necessária |
| `docs/07-operacoes-e-resiliencia/continuidade-backup-recuperacao.md` | PENDENTE — normalização necessária |
| `docs/07-operacoes-e-resiliencia/operacoes-e-observabilidade.md` | PENDENTE — normalização necessária |
| `standards/status-e-percentual-de-conclusao.md` | PENDENTE — normalização necessária |
| `templates/projeto/status-do-projeto.md` | PENDENTE — normalização necessária |

## Achados e limitações

1. Os 11 documentos Markdown de controlo da pasta `CABEÇALHO` contêm os campos SHA-256 e commit de referência. Os hashes canónicos foram recalculados ou conferidos nesta revisão; a validação estrutural não constitui aprovação substantiva.
2. Os restantes 41 ficheiros não têm o conjunto de campos canónicos. Alguns contêm metadados antigos em texto corrido ou tabelas temáticas; esses elementos não equivalem ao cabeçalho normativo.
3. `CONSTITUICAO.md` recebeu o cabeçalho canónico; o ID GOV-001, a versão 1.0.0 e o estado de proposta para revisão foram preservados.
4. Os documentos WATCHDOG incluem cartas, políticas, runbooks, documentação operacional e modelos; devem ser normalizados preservando o conteúdo técnico e os estados reais.
5. L1 foi aplicado a `CONSTITUICAO.md` e `README.md`; L2 aplicou cabeçalhos a sete documentos de fundamentos e governança. Os 41 documentos restantes não foram alterados. A alteração retroativa deverá preservar o corpo original, usar `N/A — justificação` quando os dados históricos não possam ser comprovados e manter os IDs existentes.
6. A Norma de Cabeçalho v1.0.3 foi formalmente aprovada pelo proprietário em 2026-10-13; esta aprovação não ratifica automaticamente outros documentos nem certifica conformidade substantiva.

## Próxima ação

L1 e L2 publicados e hashes verificados. Próxima ação: reconciliar os documentos de controlo e preparar L3, validando individualmente cada diff, hash e commit de referência.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.1 | 2026-10-13 | Ajuste do inventário para incluir o próprio documento; total atualizado para 58 ficheiros | Árvore Git da branch `main` e histórico Git |
| 1.0.2 | 2026-10-13 | Inclusão do plano de lotes e da classificação; total reconciliado para 60 ficheiros | Árvore Git da branch `main` |
| 1.0.3 | 2026-10-13 | Recalculo do SHA-256 canónico e atualização do estado de verificação dos dez documentos da pasta CABEÇALHO | Auditoria canónica dos ficheiros publicados |

| 1.0.4 | 2026-10-13 | Aprovação formal registada e L1 aplicado; inventário reconciliado para 61 ficheiros, 13 com campos canónicos e 48 pendentes | Norma aprovada, registo de aprovação e commits L1 |

| 1.0.5 | 2026-10-13 | L2 aplicado a sete documentos; inventário reconciliado para 61 ficheiros, 20 com campos canónicos e 41 pendentes | Sete commits L2 e validação SHA-256 canónica |
