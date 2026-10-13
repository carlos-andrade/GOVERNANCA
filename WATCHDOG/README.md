# WATCHDOG — Monitorização transversal da GOVERNANCA

**Estado:** MVP normativo e validador local em implementação; monitorização externa ainda não configurada.  
**Objetivo:** tornar verificável a cobertura e a eficácia dos controlos de sistemas, dados, processos e organizações que adotem a GOVERNANCA.

## Começar por aqui

Consulte também o [roadmap de implementação e critérios de encerramento](roadmap-de-implementacao.md) para distinguir o MVP validado das fases pendentes.

1. Leia a [Carta WATCHDOG](CARTA-WATCHDOG.md) e a [política de monitorização](normas/politica-de-monitorizacao.md).
2. Registe os sistemas em [registry/sistemas-monitorizados.json](registry/sistemas-monitorizados.json).
3. Declare os controlos aplicáveis em [registry/controlos-obrigatorios.json](registry/controlos-obrigatorios.json).
4. Defina os critérios e as evidências conforme os [contratos](contratos/).
5. Execute o validador: `python WATCHDOG/engine/watchdog.py --check`.
6. Execute os testes: `python -m unittest discover -s WATCHDOG/tests -v`.
7. Integre adaptadores específicos e um monitor independente antes de afirmar cobertura operacional contínua.

## Estados

- `PASS`: verificação executada e satisfeita, com evidência gerada ou referenciada.
- `WARN`: condição degradada que exige avaliação.
- `FAIL`: condição verificada que viola o critério.
- `UNKNOWN`: não há dados suficientes, a verificação não está implementada ou o monitor está indisponível.

**Regra de segurança:** ausência de dados nunca equivale a `PASS`. O validador inicial verifica configuração e ficheiros locais; não afirma que serviços externos estejam saudáveis.

## Estrutura

- `arquitetura/`: desenho e integração.
- `normas/`: regras de monitorização, estados, escalonamento, evidência e segurança.
- `contratos/`: formatos de configuração, alerta e evidência.
- `registry/`: inventário e cobertura declarada.
- `adapters/`: pontos de integração por domínio.
- `engine/`: validador e avaliação inicial.
- `reports/`: modelos e exemplos.
- `runbooks/`: resposta a incidentes.
- `tests/`: testes unitários, integração e falhas simuladas.
- `docs/`: instalação, configuração e operação.

## Limites atuais

O MVP valida registos e verificações locais declaradas. Ainda não fornece recolha universal, agente 24×7, envio de alertas, armazenamento imutável de evidências, integração com sistemas externos ou remediação automática. Estas capacidades exigem adaptadores, infraestrutura, credenciais protegidas e testes próprios.

## Critério de adoção

Um projeto só pode declarar o WATCHDOG operacional quando: inventário aprovado; controlos prioritários definidos; adaptadores testados; alertas e responsáveis validados; indisponibilidade do monitor detetável por via independente; retenção e acesso às evidências definidos; e aceitação registada.
