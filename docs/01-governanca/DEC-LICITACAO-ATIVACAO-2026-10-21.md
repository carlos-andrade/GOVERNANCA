# Decisão de ativação proposta — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | DEC-LICITACAO-ACT-2026-10-21 |
| **Data** | 2026-10-21 |
| **Estado** | APROVADA E EFETIVA |
| **Projeto** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Autoridade de registo** | [Registo-mestre de consumidores](../../registry/repositorios-consumidores.json) |
| **Autorização do titular** | Instrução explícita recebida em 2026-10-21 para resolver G0 e colocar `LICITACAO.enabled=true` |

## Decisão aprovada e efetiva

Alteração efetivada: `LICITACAO.enabled=true` no registo-mestre após a integração da [GOVERNANCA PR #32](https://github.com/carlos-andrade/GOVERNANCA/pull/32), commit `cedba71292a107b1f4b5733987c6262d50c46673`. A ativação inclui o repositório no âmbito de distribuição das normas GOVERNANCA. Não certifica conformidade integral, não declara o WATCHDOG operacional e não autoriza ignorar os gates funcionais posteriores.

## Evidências que fundamentam a decisão

1. [LICITACAO PR #24](https://github.com/carlos-andrade/LICITACAO/pull/24) integrada; CI pós-merge PASS.
2. Verificação pós-merge confirmou 79/79 Git blob SHA coincidentes com a origem.
3. [Avaliação G0 e scorecard](https://github.com/carlos-andrade/LICITACAO/blob/main/docs/governanca/GATE-G0-AVALIACAO.md) atualizados.
4. [Inspeção individual](https://github.com/carlos-andrade/LICITACAO/blob/main/docs/governanca/INSPECAO-DE-ADOCAO.md) atualizada para `APROVADO_COM_LIMITACOES`.
5. A checklist WATCHDOG foi executada: 1 PASS e 7 UNKNOWN; os UNKNOWN não foram convertidos em PASS.

## Limitações operacionais

A checklist local WATCHDOG registou 1 controlo `PASS` por evidência direta e 7 `UNKNOWN`. A ativação de distribuição não substitui secret scanning, canal de alertas/escalonamento, supervisão independente nem testes de falha e recuperação.

## Estado efetivo

**Estado efetivo:** `LICITACAO.enabled=true` em `main` desde o merge da PR #32. A ativação é exclusivamente de âmbito de distribuição. Os sete controlos WATCHDOG UNKNOWN continuam limitações abertas; o WATCHDOG não é declarado operacional. A implementação funcional continua sujeita a G1 e aos gates seguintes.
