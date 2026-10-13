# Carta WATCHDOG

**ID:** GOV-WD-001  
**Versão:** 1.0.0  
**Estado:** proposta operacional sujeita a revisão e aprovação formal.

## Mandato

O WATCHDOG é o mecanismo transversal de supervisão da GOVERNANCA. Monitoriza, de forma proporcional ao risco, sistemas, organizações, dados, processos, obrigações de controlo e a própria infraestrutura de monitorização.

## Objetivos

1. Detetar desvios relativamente a critérios declarados.
2. Produzir evidência rastreável e útil para auditoria.
3. Alertar responsáveis dentro de prazos definidos.
4. Escalar incidentes sem depender exclusivamente do componente que falhou.
5. Medir cobertura, eficácia, falsos positivos, atrasos e reincidência.
6. Apoiar melhoria contínua sem substituir decisões humanas obrigatórias.

## Âmbito

O âmbito pode incluir infraestrutura, aplicações, pipelines, qualidade e atualidade de dados, controlos de segurança, processos operacionais, prazos, dependências, requisitos contratuais e tarefas de governança. Cada integração tem de declarar limites, permissões, frequência e dados recolhidos.

## Princípios não negociáveis

- Evidência antes de alegação.
- Estado `UNKNOWN` quando não existe evidência suficiente.
- Privilégio mínimo e recolha mínima de dados.
- Separação entre deteção, notificação e remediação.
- Nenhuma ação destrutiva ou alteração automática sem autorização explícita, limites, rollback e auditoria.
- Supervisão independente do próprio WATCHDOG.
- Controlos proporcionais ao risco, sem dispensar obrigações legais ou contratuais.

## Autoridade e responsabilidade

O proprietário do sistema/processo responde pelo critério de aceitação; o responsável operacional responde pela resposta; a equipa WATCHDOG mantém o mecanismo e os adaptadores; segurança/privacidade revê recolhas e permissões; um revisor independente valida controlos de risco elevado.

## Critérios mínimos de aceitação

O WATCHDOG só pode ser declarado operacional para um âmbito quando o inventário está completo e aprovado, os controlos críticos têm testes positivos e negativos, os alertas foram entregues e reconhecidos em teste, a indisponibilidade do monitor é detetável por mecanismo independente, as evidências são protegidas e o responsável aceita formalmente os resultados.

## Estado desta carta

Esta carta define o padrão proposto. Não constitui, por si só, aprovação corporativa nem prova de que todos os ambientes estejam monitorizados.
