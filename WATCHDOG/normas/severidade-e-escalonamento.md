# Severidade e escalonamento

## Níveis recomendados

- **SEV-1 — Crítico:** risco imediato para segurança, integridade, continuidade ou obrigação crítica. Notificação imediata e escalonamento para responsável e suplente.
- **SEV-2 — Alto:** impacto significativo ou controlo prioritário falhado. Resposta urgente dentro do SLA definido pelo proprietário.
- **SEV-3 — Moderado:** degradação localizada, risco limitado ou incumprimento não crítico. Tratamento no prazo operacional acordado.
- **SEV-4 — Baixo/Informativo:** aviso preventivo, tendência ou melhoria.

Os tempos de resposta devem ser definidos por serviço e risco, não presumidos globalmente. Cada regra deve identificar destinatário primário, suplente, canal alternativo, condição de escalonamento e confirmação de receção.

## Ciclo de alerta

Detetar → deduplicar → notificar → confirmar receção → escalar se necessário → registar decisão → verificar recuperação → encerrar com evidência.

Alertas críticos não podem depender exclusivamente do mesmo sistema monitorizado.
