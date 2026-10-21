# Pacote de aceitação e fecho — GOVERNANCA

| Campo | Valor |
|---|---|
| ID | GOV-CLOSEOUT-001 |
| Estado | EM_EXECUCAO |
| Versão | 1.0.0 |
| Data | 2026-10-21 |
| Aprovador | Pendente de aprovação explícita |
| Âmbito | P0 distribuição, GIF, ratificação normativa, WATCHDOG; P1 concorrência e adoção transversal |

## Regra de fecho

Nenhum gate pode ser marcado como concluído sem evidência ligada ao commit/execução, responsável e resultado reproduzível. `UNKNOWN` não equivale a `PASS`. Este pacote não ratifica políticas nem substitui a aceitação dos proprietários dos sistemas consumidores.

## G0 — Distribuição por Pull Request real (P0)

- [ ] Confirmar que `GOVERNANCA_SYNC_TOKEN` está configurado como secret de Actions, sem revelar o valor.
- [ ] Executar primeiro o dry-run no repositório autorizado.
- [ ] Executar `workflow_dispatch` com `dry_run=false` e `repository=carlos-andrade/STOCKS` apenas após confirmação da autorização e do destino.
- [ ] Confirmar a PR criada, branch, diff, ficheiros, hashes e origem.
- [ ] Reexecutar e provar idempotência, sem duplicar PR nem produzir alterações desnecessárias.
- [ ] Arquivar URL do run, URL da PR e relatório de artefacto.

**Aceitação:** PR real observada e auditada; dry-run não é evidência suficiente.

## G1 — Governance Integration Framework (P0)

- [ ] Motor suporta e valida parâmetros para `file_exists`, `json_valid`, `yaml_valid`, `yaml_field_equals` e `file_contains`.
- [ ] Caminhos absolutos, traversal e symlinks para fora da raiz são rejeitados.
- [ ] Testes positivos e negativos cobrem YAML/JSON inválidos, campo ausente/diferente e requisito malformado.
- [ ] Cada perfil tem requisitos de domínio aprovados, não apenas ficheiros estruturais.
- [ ] `complete=true` apenas após cobertura semântica, revisão e testes aprovados.
- [ ] Perfil `automatico` permanece incompleto até existir definição executável e regra de seleção validada.
- [ ] Piloto é executado em cada perfil relevante; resultados UNKNOWN permanecem bloqueios.

**Aceitação:** CI verde, relatório por perfil e revisão técnica; não inferir conformidade global apenas de testes unitários.

## G2 — Ratificação normativa (P0)

Documentos sob revisão identificados nesta auditoria:

| Documento | Versão | Estado atual | SHA-256 canónico publicado | Decisão |
|---|---:|---|---|---|
| `CONSTITUICAO.md` | 1.0.1 | PROPOSTA PARA REVISÃO | `fcdf39acc56d53b886815967080f0d183960e1ccbd2d0cca023181da9f80834d` | PENDENTE |
| `WATCHDOG/runbooks/operacao-de-alertas-e-sla.md` | 1.0.0 | EM_REVISAO | `5b38c23d743b1254707c812e63e6d6a5b5bac8e2dacb95f5539afdc3f7cd230d` | PENDENTE |
| `WATCHDOG/roadmap-de-implementacao.md` | 1.0.0 | EM_REVISAO | `2a5f3c53a20d7cec74e494e658a85c12980880fdd6748f2396998599ba0e7842` | PENDENTE |

Esta é uma lista inicial dos documentos verificados, não uma declaração de que todas as políticas fundamentais foram inventariadas. Antes da ratificação, completar o inventário de políticas e confirmar que os hashes canónicos continuam a corresponder ao conteúdo exato submetido à decisão.

- [ ] Fazer revisão de conflitos legais, contratuais e internos.
- [ ] Congelar o conteúdo e calcular o hash canónico de cada versão candidata.
- [ ] Registar decisor autorizado, decisão, data, versão e hash exatos.
- [ ] Publicar o registo da decisão e atualizar os metadados documentais após aprovação.

**Bloqueio:** este pacote não constitui ratificação. A aprovação deve ser registada pelo aprovador competente.

## G3 — WATCHDOG operacional (P0)

- [ ] Identificar responsável primário, suplente e canal alternativo independente.
- [ ] Obter aprovação dos limiares de atualidade e tempos de ACK/escalonamento.
- [ ] Confirmar configuração de heartbeat externo independente.
- [ ] Testar entrega de alerta no canal primário.
- [ ] Testar ACK e ausência de ACK, incluindo escalonamento.
- [ ] Simular indisponibilidade do canal primário.
- [ ] Demonstrar deduplicação e recuperação verificada por nova execução de controlo.
- [ ] Arquivar timestamps UTC, execuções, incidentes e aprovação operacional.

**Aceitação:** testes ponta a ponta e aprovação do proprietário; documentação e workflow verde não bastam.

## G4 — Concorrência de workflows (P1)

- [ ] Congelar o inventário e a definição de âmbito dos 42 workflows.
- [ ] Registar repositório, caminho, trigger, grupo `concurrency`, `cancel-in-progress` e recursos publicados.
- [ ] Identificar colisões de publicação, escrita ou deploy.
- [ ] Aplicar grupos de concorrência estáveis por recurso partilhado; justificar exceções.
- [ ] Executar testes de execuções simultâneas, cancelamento e recuperação.
- [ ] Verificar a branch principal após merge e arquivar os resultados.

**Aceitação:** 42/42 workflows reconciliados, exceções justificadas e testes de concorrência aprovados.

## G5 — Adoção transversal (P1)

Para cada repositório consumidor autorizado, registar: commit/ref, perfil, configuração, resultado do motor, hashes, PR de propagação, pendências, exceções, responsável, aprovador e data de aceitação.

- [ ] Validar individualmente cada consumidor ativo.
- [ ] Classificar cada resultado como PASS, FAIL ou UNKNOWN.
- [ ] Não ativar destinos sem permissões confirmadas e aceitação local.
- [ ] Manter LICITACAO desativado até cumprir os critérios de adoção e distribuição.
- [ ] Aprovar individualmente exceções com justificação, risco, mitigação, aprovador, validade e revogação.

**Aceitação:** matriz completa para todos os consumidores ativos; a inscrição no registo não equivale a aceitação.

## G6 — Auditoria final e fecho

- [ ] Reconciliar scorecard, README, roadmap, inventários, hashes e evidências.
- [ ] Confirmar todos os gates P0 e P1.
- [ ] Confirmar transferência de conhecimento e runbooks operacionais.
- [ ] Obter revisão final independente e aprovação explícita de encerramento.
- [ ] Só então atualizar os cinco `closure_checks` e pontuação final.

## Evidência atual

- A distribuição real por PR não está demonstrada pelos dry-runs existentes.
- O catálogo de perfis permanece estrutural/incompleto; o motor não deve certificar conformidade global.
- A Constituição está em proposta de revisão; o runbook e roadmap WATCHDOG estão em revisão.
- O runbook marca como pendentes os testes de entrega, ACK, escalonamento, canal alternativo, deduplicação, recuperação e aprovação.
- O roadmap WATCHDOG declara pendente a supervisão externa independente e a adoção transversal.
- A auditoria dos 42 workflows e a aceitação individual dos consumidores continuam por comprovar.

## Histórico

- 1.0.0 — 2026-10-21 — Consolidação dos critérios de aceitação e das dependências de fecho, sem promover estados não comprovados.
