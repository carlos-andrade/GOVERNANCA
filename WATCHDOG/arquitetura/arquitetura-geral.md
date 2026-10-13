# Arquitetura geral

## Camadas

1. **Política e catálogo:** requisitos, critérios, responsáveis e severidade.
2. **Inventário:** sistemas, processos, dependências, localização e criticidade.
3. **Adaptadores:** recolha de sinais por API, agente, logs, métricas, eventos ou validação documental.
4. **Motor de avaliação:** normaliza resultados, aplica limites e trata dados ausentes.
5. **Evidências:** regista resultado, instante UTC, origem, versão, referência e integridade.
6. **Alertas e escalonamento:** encaminha por severidade, confirma receção e escala quando necessário.
7. **Relatórios e auditoria:** cobertura, incidentes, exceções, tendência e eficácia.
8. **Supervisão independente:** confirma que o motor e os canais de alerta estão vivos.

## Fluxo

`Inventário → recolha → validação → avaliação → evidência → alerta → resposta → verificação de recuperação`

A falha de recolha gera `UNKNOWN` ou um alerta de monitor indisponível; nunca é convertida automaticamente em `PASS`.

## Modelo de implantação

Pode combinar CI agendado, serviço permanente e agentes locais. A escolha depende de latência, criticidade, conectividade e custo. GitHub Actions é apropriado para validações periódicas de repositórios, mas não garante sozinho vigilância contínua 24×7.

## Segurança

Separar credenciais por adaptador, limitar permissões, proteger segredos fora do Git, validar entradas, limitar dados pessoais e registar alterações de configuração. A remediação deve ser desligada por defeito.
