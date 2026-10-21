# Decisão de ativação proposta — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | DEC-LICITACAO-ACT-2026-10-21 |
| **Data** | 2026-10-21 |
| **Estado** | PROPOSTA EM RASCUNHO — NÃO EFETIVA |
| **Projeto** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Autoridade de registo** | [Registo-mestre de consumidores](../../registry/repositorios-consumidores.json) |
| **Autorização do titular** | Instrução explícita recebida em 2026-10-21 para resolver G0 e colocar `LICITACAO.enabled=true` |

## Decisão proposta

Alterar o registo-mestre para `LICITACAO.enabled=true`, para incluir o repositório no âmbito de distribuição das normas GOVERNANCA. Esta ativação não certifica conformidade integral, não declara o WATCHDOG operacional e não autoriza ignorar os gates funcionais posteriores.

## Pré-condições obrigatórias para efetivar

1. [PR #24 do LICITACAO](https://github.com/carlos-andrade/LICITACAO/pull/24) integrada em `main` com check obrigatório `validate` concluído com sucesso.
2. Verificação pós-merge comprova 79/79 ficheiros normativos com Git blob SHA coincidente com a origem.
3. Avaliação de G0 e scorecard atualizados em `main`.
4. Inspeção individual da adoção atualizada para `APROVADO_COM_LIMITACOES`, explicitando os controlos WATCHDOG ainda `UNKNOWN`.
5. Nenhum estado `UNKNOWN` é apresentado como `PASS`; WATCHDOG continua declarado não operacional enquanto faltarem os testes correspondentes.

## Limitações operacionais

A checklist local WATCHDOG registou 1 controlo `PASS` por evidência direta e 7 `UNKNOWN`. A ativação de distribuição não substitui secret scanning, canal de alertas/escalonamento, supervisão independente nem testes de falha e recuperação.

## Estado efetivo

**Até todas as pré-condições estarem comprovadas e esta decisão ser aprovada e integrada por PR, o registo em `main` continua `enabled=false`.** Esta proposta permanece em rascunho e não deve ser integrada antecipadamente.
