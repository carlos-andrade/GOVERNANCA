# Recuperação e remediação

A primeira versão opera em modo de deteção e validação. Remediações automáticas ficam desativadas por defeito.

Antes de ativar uma ação automática, documentar: proprietário autorizador, condições de disparo, âmbito permitido, limites, idempotência, risco, rollback, timeout, auditoria e teste em ambiente seguro. Ações destrutivas, financeiras, de acesso ou com impacto em pessoas exigem revisão humana explícita, salvo política formal aprovada com salvaguardas adequadas.

Após remediação, executar nova verificação independente. Não encerrar incidente com base apenas no código de saída da ação.
