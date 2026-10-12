# Operações e observabilidade

Todo o serviço produtivo tem owner operacional, dependências, métricas, logs, alertas acionáveis, runbooks, suporte e escalonamento. Minimizar telemetria e retenção ao necessário.

Perguntas mínimas: como confirmar o serviço do ponto de vista do utilizador? Que falha gera alerta e quem responde? Como distinguir falha de serviço/dependência/telemetria? Que ações seguras pode o responsável executar? Qual o procedimento manual se a automação falhar?

Para serviços contínuos, definir SLIs/SLOs e janela. Não inventar SLAs contratuais. Alertas devem ser acionáveis e ruído persistente deve ser corrigido.