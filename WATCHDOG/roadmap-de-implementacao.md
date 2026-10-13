# Roadmap de implementação do WATCHDOG

**Atualizado:** 2026-10-13  
**Estado global:** MVP central validado; piloto B3 em expansão, ainda não certificado para operação universal 24×7.

## Fase 1 — Padrão central e motor local

**Estado: concluída para o MVP.**

- Carta WATCHDOG, política, estados, severidade, evidências e segurança documentados.
- Contratos JSON, inventário inicial, motor de validação e testes unitários criados.
- Workflow central de validação executado com sucesso.

## Fase 2 — Piloto de monitorização de workflows

**Estado: implementada; testes de ponta a ponta concluídos para evidências e alertas GitHub.**

- Monitor B3 a cada 15 minutos e análise das últimas 24 horas.
- Relatórios JSON/Markdown publicados como artefactos com retenção configurada de 30 dias.
- Issue de alerta criada/atualizada quando são detetadas execuções desfavoráveis.
- Validação do inventário e da configuração do monitor em GitHub Actions.

Limites: os artefactos não são armazenamento imutável; issues não confirmam que um responsável recebeu ou reconheceu o alerta; o monitor não deteta autonomamente a sua própria falha.

## Fase 3 — Atualidade de dados

**Estado: implementação inicial; primeira execução e calibração pendentes de revisão.**

- Catálogo explícito para BCB SGS 432, 11, 12, 1 e 433, B3 BDI DailyAverageStocks e manifesto COTAHIST 2026.
- Avaliação da idade baseada em data de observação declarada.
- UNKNOWN quando a data de observação não existe; a data de ingestão não é usada como substituto.
- Workflow agendado, testes, relatório JSON/Markdown, artefacto de 30 dias e issue de alerta para datasets fora do limite.

Critério de saída: rever cada resultado, confirmar fonte/semântica, calibrar limites por periodicidade e comprovar recuperação após atualização.

## Fase 4 — Alertas operacionais e resiliência

**Estado: pendente.**

- Definir proprietário primário e suplente por controlo.
- Implementar confirmação de receção, SLA, escalonamento e canal alternativo.
- Deduplicar alertas e documentar ciclo de resolução.
- Validar indisponibilidade de credenciais, API, quota e canal de alerta.

## Fase 5 — Supervisão independente

**Estado: pendente; bloqueador para alegações de monitorização 24×7.**

- Escolher e configurar serviço externo independente do GitHub Actions monitorizado.
- Detetar falta de heartbeat e falha do pipeline de monitorização.
- Testar o mecanismo com falhas simuladas e registar evidências.
- Definir responsável e canal de contingência.

## Fase 6 — Integridade e reconciliação de dados

**Estado: planeada.**

- Integrar hashes, manifests, atualidade, cardinalidade e reconciliação para COTAHIST, BCB SGS e BDI.
- Distinguir falha de ingestão, atraso da fonte, lacuna de calendário e falha de validação.
- Preservar proveniência e evitar certificação baseada apenas em sucesso do workflow.

## Fase 7 — Adoção transversal

**Estado: pendente.**

- Priorizar repositórios por criticidade e dependências.
- Aplicar inventário e adaptadores por repositório, sem presumir cobertura.
- Exigir workflow aprovado, evidência e responsável antes de marcar integração como operacional.
- Atualizar a barra de status central apenas com evidências verificadas.

## Critérios de encerramento

O WATCHDOG só pode ser declarado operacional num âmbito quando os controlos obrigatórios estão inventariados, os resultados têm evidência válida, alertas foram testados ponta a ponta, a falha do próprio monitor é detetável independentemente, a retenção/acesso estão definidos e o proprietário aprovou formalmente a aceitação.
