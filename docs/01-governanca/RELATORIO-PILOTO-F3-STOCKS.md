# Relatório do piloto F3 — STOCKS

| Campo | Valor |
|---|---|
| **ID** | GOV-INT-F3-PILOT-STOCKS-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório consumidor** | [carlos-andrade/STOCKS](https://github.com/carlos-andrade/STOCKS) |
| **Tipo documental** | Relatório de validação de piloto |
| **Estado** | EXECUÇÃO TÉCNICA PASSOU — ACEITAÇÃO PENDENTE |
| **Data** | 2026-10-20 |
| **Fonte normativa** | [DEC-GOV-INT-001](DEC-GOV-INTEGRATION-FRAMEWORK-001.md) |
| **PR de integração do consumidor** | [STOCKS #8](https://github.com/carlos-andrade/STOCKS/pull/8) |

## 1. Objetivo

Validar a invocação do workflow reutilizável oficial a partir de um repositório consumidor, em modo estritamente de diagnóstico, sem escrita automática nem substituição dos documentos locais.

## 2. Execução

- Workflow: [GOVERNANCA — piloto F3 (diagnóstico)](https://github.com/carlos-andrade/STOCKS/actions/workflows/governance-integration.yml)
- Execução de referência com a fonte corrigida: [run 39467662909](https://github.com/carlos-andrade/STOCKS/actions/runs/39467662909)
- Artefacto do relatório: [governance-integration-report](https://github.com/carlos-andrade/STOCKS/actions/runs/39467662909/artifacts/12286047005)
- Commit do consumidor executado: `1409a41960d99e12cd10980d3b48e3a26adb3259`
- Commit exato da fonte reportado: `e105218721d771f58264044bb7ad9fba7ab65b84`
- Perfil: `dados`
- Modo: `diagnostico`
- Resultado do job: `success`
- Estado de conformidade emitido pelo motor: `DESCONHECIDO`

## 3. Evidência do relatório

| Verificação | Resultado | Interpretação |
|---|---|---|
| CFG-002 | PASS | Configuração válida segundo JSON Schema Draft 2020-12 |
| SRC-001 | PASS | Fonte configurada corresponde a `carlos-andrade/GOVERNANCA` |
| Commit de origem | PASS | `source_commit` coincide com o `pinned_ref` fixado |
| Hash da configuração | Registado | SHA-256: `900e1c419c9897b7e80d7562f0413601495781e03594686da36b88578158178c` |
| Hash do esquema | Registado | SHA-256: `c2090d3007509533137af8815d3eee977897ccbc06525c3a599731336241c0fb` |
| Catálogo executável por perfil | PENDENTE | A ausência impede certificação global e mantém o estado `DESCONHECIDO` |

## 4. Preservação e segurança

- A configuração local seleciona exclusivamente `diagnostico`.
- O workflow reutilizável tem permissão `contents: read` e publica o relatório como artefacto.
- A integração foi proposta na [PR STOCKS #8](https://github.com/carlos-andrade/STOCKS/pull/8), com apenas dois ficheiros novos/modificados para o piloto.
- O motor F2 não implementa alterações ao repositório consumidor; o modo `aplicar` continua bloqueado.
- A PR do consumidor permanece aberta para revisão humana. Não foi feito merge automático nem declarada adoção operacional.

## 5. Avaliação dos critérios F3

| Critério | Estado | Evidência/pendência |
|---|---|---|
| Workflow reutilizável invocado num consumidor | PASS | Run 39467662909 |
| Relatório gerado e arquivado | PASS | Artefacto 12286047005 |
| Fonte e versão rastreáveis | PASS | SHA de origem presente no relatório |
| Configuração validada | PASS | CFG-002 |
| Alterações propostas por PR | PASS | STOCKS #8, ainda aberta |
| Preservação do conteúdo local | PASS limitado ao escopo da PR | A proposta não substitui os documentos de governança existentes; a aceitação final requer revisão da PR |
| Relatório aceite pelo responsável | PENDENTE | Requer revisão humana |
| Catálogo de requisitos por perfil | PENDENTE | Necessário para sair de `DESCONHECIDO` |
| Distribuição transversal aos oito consumidores | BLOQUEADO | Secret `GOVERNANCA_SYNC_TOKEN` rejeitado; não foi executada propagação |

## 6. Conclusão

O piloto demonstrou a execução técnica do workflow reutilizável, a validação da configuração, a geração do relatório e a rastreabilidade do commit de origem. **F3 não está encerrada**: a aceitação humana da PR STOCKS #8 e a implementação do catálogo de requisitos por perfil continuam pendentes. O bloqueio da distribuição transversal por credencial inválida é independente deste piloto.

Não interpretar o sucesso do job como conformidade do STOCKS.
