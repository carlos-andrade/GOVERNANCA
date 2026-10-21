# Revalidação de concorrência — B3 e BLOOMBERG_MAIL

| Campo | Valor |
|---|---|
| ID | GOV-AUD-CONCURRENCY-B3-BM-2026-10-21 |
| Data | 2026-10-21 |
| Estado | PARCIALMENTE VALIDADO — controlos estáticos e testes sintéticos PASS; concorrência real do scheduler ainda pendente |
| Repositórios | B3; BLOOMBERG_MAIL; GOVERNANCA |
| Dados de produção | Não foram executadas ingestões/normalizações de produção para esta validação |

## 1. Resultado executivo

1. **B3 — execução confirmada:** o workflow `Classificar BVBG.028.02`, run [39525805546](https://github.com/carlos-andrade/B3/actions/runs/39525805546), terminou `success`. Os passos `Classificar inventário` e `Commit classificação` concluíram com sucesso. O commit que acionou a execução foi `6d29578cc6b6b5155b874fd043269b0cbecae89c`. A auditoria de conformidade dos workflows, run [39525805547](https://github.com/carlos-andrade/B3/actions/runs/39525805547), também terminou com sucesso.
2. **Integridade dos seis workflows:** os três ficheiros de cada repositório foram lidos na branch `main`; todos contêm um grupo de concorrência comum aos três escritores do respetivo repositório e `cancel-in-progress: false`.
3. **BLOOMBERG_MAIL — sintaxe e testes:** PR [#8](https://github.com/carlos-andrade/BLOOMBERG_MAIL/pull/8) integrada no commit `a216bb40889612bddaec469a3913c7ca86a41c91`. O workflow de testes seguros, run [39526649987](https://github.com/carlos-andrade/BLOOMBERG_MAIL/actions/runs/39526649987), terminou `success`; os três testes passaram.
4. **Scorecard:** manter 80/100, com início 20/20, meio 60/60 e fim 0/20. A evidência deste recorte não demonstra os restantes gates de finalização global.

## 2. Ficheiros e integridade verificada

### B3

| Ficheiro | Blob SHA observado | Resultado |
|---|---|---|
| `.github/workflows/classificar-bvbg028.yml` | `f2ebd4e11265d249b528ae67cbde383e9afc26e9` | Grupo comum; cancelamento desativado; execução concluída |
| `.github/workflows/processar-inventario-bvbg028.yml` | `8498c3c8903d12c0f6b787457591068ae366fa9c` | Grupo comum; cancelamento desativado |
| `.github/workflows/validar-bvbg02802.yml` | `751938bae9e344031c7894e4fbc61317b5ce9ebb` | Grupo comum; cancelamento desativado |

Grupo comum: `b3-bvbg028-catalog-publish-${{ github.ref }}`.

### BLOOMBERG_MAIL

| Ficheiro | Blob SHA observado | Resultado |
|---|---|---|
| `.github/workflows/bloomberg-mail-ingestao-005n-normalizacao.yml` | `7f3086f93a4f8fa5484c0acee5235e1ec2c85f80` | Grupo comum; cancelamento desativado |
| `.github/workflows/bloomberg-mail-ingestao-005n-validacao-normalizadores.yml` | `82ee2bb6354404440aebee0fbf0f90a99d6a0ccf` | Grupo comum; cancelamento desativado |
| `.github/workflows/bloomberg-mail-rec001-b3-cotahist-cross-repo.yml` | `1d08135a366d9ca9ac8153a5934bbabae3a397be` | Grupo comum; cancelamento desativado |

Grupo comum: `bloomberg-mail-005n-publish-${{ github.ref }}`.

Os SHA acima são SHA de blobs observados antes da integração dos testes; devem ser tratados como identificação da versão inspecionada, não como prova de que os ficheiros de workflow foram alterados pela PR #8.

## 3. Testes sintéticos executados

O novo workflow [BLOOMBERG_MAIL — Testes seguros de publicação 005N](https://github.com/carlos-andrade/BLOOMBERG_MAIL/actions/runs/39526649987) executa com permissões `contents: read` e não chama os scripts de ingestão.

| Teste | Resultado | O que demonstra |
|---|---|---|
| Parse YAML dos três workflows e igualdade do grupo/cancelamento | PASS | Sintaxe YAML parseável e configuração de concorrência consistente |
| Repetição de geração de evidência idêntica | PASS | O conteúdo idêntico não cria alteração staged nem commit adicional no cenário sintético |
| Push concorrente, rejeição non-fast-forward, rebase e nova publicação | PASS | O padrão de recuperação preserva ficheiros de dois escritores num repositório Git temporário |

Código dos testes: [scripts/tests/test_workflow_publication_safety.py](https://github.com/carlos-andrade/BLOOMBERG_MAIL/blob/main/scripts/tests/test_workflow_publication_safety.py). Workflow: [.github/workflows/bloomberg-mail-publication-safety-tests.yml](https://github.com/carlos-andrade/BLOOMBERG_MAIL/blob/main/.github/workflows/bloomberg-mail-publication-safety-tests.yml).

## 4. Limites de interpretação e testes ainda necessários

- Os testes sintéticos não simulam o scheduler real do GitHub Actions nem dois runs reais concorrentes a publicar na mesma branch.
- `concurrency` limita execuções simultâneas no grupo, mas não oferece fila FIFO garantida; uma execução pendente pode ser substituída por outra mais recente.
- A passagem do teste local de rebase não prova que todos os scripts de publicação tratam cada erro real, cada estado parcial ou cada artefacto de produção corretamente.
- Não foram executados workflows de ingestão/normalização 005N nem workflows B3 de captura/importação para evitar alterações não planeadas aos dados.
- Para fechar o risco operacional, ainda é necessário um teste explícito, reversível e aprovado do scheduler real, com artefactos sintéticos isolados, duas execuções concorrentes, inspeção de commits/pushes e recuperação demonstrada. Não utilizar os caminhos de produção como fixture.

## 5. Decisão de auditoria

**Aceites:** resultado final do workflow de classificação B3; inspeção estática dos seis workflows; sintaxe YAML e três testes sintéticos de BLOOMBERG_MAIL.

**Não aceites como concluídos:** concorrência real do scheduler, garantia de processamento de todos os eventos pendentes, recuperação de todos os modos de falha de publicação e auditoria global dos 42 workflows.

A pontuação central permanece **80/100**. Nenhum ponto de conclusão é atribuído com esta evidência parcial; os cinco `closure_checks` permanecem falsos.
