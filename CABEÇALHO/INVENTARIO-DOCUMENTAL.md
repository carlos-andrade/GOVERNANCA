# Inventário documental Markdown — GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-INV-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | INVENTARIO |
| **Fase** | Auditoria documental |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 1d8b89220bcd494eb32d3b14613951f4750ec7ad057e05b4412d0c1e35ac9c13 |
| **Commit de referência (versão anterior)** | [69ea5236b624ab735a68d4bf8cfa8d82a434938a](https://github.com/carlos-andrade/GOVERNANCA/commit/69ea5236b624ab735a68d4bf8cfa8d82a434938a) |
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
- Total identificado: **57 ficheiros Markdown**.
- Critério de conformidade inicial: título Markdown, tabela de metadados `Campo | Valor`, linha SHA-256 canónico e linha de commit de referência.
- Os ficheiros classificados como conformes foram também verificados quanto à presença dos campos; os sete hashes canónicos da pasta `CABEÇALHO` foram recalculados e coincidiram com os valores declarados.
- A classificação é estrutural, não uma aprovação substantiva do conteúdo.
- Ficheiros de modelo, como `CABEÇALHO/MODELO-DOCUMENTO.md`, podem conter marcadores de preenchimento; a conformidade do modelo não torna automaticamente conformes os documentos criados a partir dele.

## Resumo

| Resultado | Quantidade |
|---|---:|
| Ficheiros Markdown inventariados | 57 |
| Com campos canónicos presentes | 7 |
| A normalizar ou avaliar individualmente | 50 |
| Cobertura estrutural do padrão | 12,3% |

## Inventário completo

| Caminho | Resultado da auditoria estrutural |
|---|---|
| `CABEÇALHO/CHECKLIST-VALIDACAO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/HISTORICO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/MODELO-DOCUMENTO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/NORMA-CABECALHO-PADRAO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/README.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/REGISTO-TIPOS-DOCUMENTAIS.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/ROADMAP-ADOCAO-TRANSVERSAL.md` | CONFORME — campos canónicos presentes |
| `CONSTITUICAO.md` | PENDENTE — normalização necessária |
| `README.md` | PENDENTE — normalização necessária |
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
| `docs/00-fundamentos/modelo-operacional.md` | PENDENTE — normalização necessária |
| `docs/00-fundamentos/principios-de-adaptacao.md` | PENDENTE — normalização necessária |
| `docs/00-fundamentos/taxonomia-e-glossario.md` | PENDENTE — normalização necessária |
| `docs/01-governanca/papeis-e-responsabilidades.md` | PENDENTE — normalização necessária |
| `docs/01-governanca/politica-de-conformidade-documental.md` | PENDENTE — normalização necessária |
| `docs/01-governanca/politica-de-decisoes.md` | PENDENTE — normalização necessária |
| `docs/01-governanca/politica-de-excecoes.md` | PENDENTE — normalização necessária |
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

1. Os sete ficheiros da pasta `CABEÇALHO` contêm os campos SHA-256 e commit de referência; os seus hashes canónicos foram recalculados e validados.
2. Os restantes 50 ficheiros não têm o conjunto de campos canónicos. Alguns contêm metadados antigos em texto corrido ou tabelas temáticas; esses elementos não equivalem ao cabeçalho normativo.
3. `CONSTITUICAO.md` contém metadados em formato anterior e requer tratamento específico por ser documento de autoridade superior.
4. Os documentos WATCHDOG incluem cartas, políticas, runbooks, documentação operacional e modelos; devem ser normalizados preservando o conteúdo técnico e os estados reais.
5. Não foram alterados os 50 ficheiros pendentes nesta fase. A alteração retroativa deverá preservar o corpo original, usar `N/A — justificação` quando os dados históricos não possam ser comprovados e manter os IDs existentes.
6. A norma permanece proposta até aprovação formal; este inventário não constitui aprovação nem certificação de conformidade substantiva.

## Próxima ação

Rever e aprovar formalmente a norma e os critérios de normalização; depois aplicar as alterações em lotes controlados, verificar os hashes, confirmar os commits de referência e atualizar este inventário com evidências.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-13 | Inventário inicial dos ficheiros Markdown e classificação estrutural | Árvore Git da branch `main` |
