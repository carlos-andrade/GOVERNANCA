# Política de monitorização

## Obrigatoriedade

Cada projeto sob a GOVERNANCA deve identificar os objetos monitorizados, controlos aplicáveis, responsáveis, frequência, limites, evidências e resposta. A profundidade é proporcional ao risco; controlos legais, contratuais ou críticos não podem ser omitidos sem autoridade legítima.

## Requisitos por controlo

Cada controlo declara: ID, objetivo, âmbito, proprietário, criticidade, tipo de verificação, critério de sucesso, frequência, timeout, fonte de evidência, validade da evidência, destinatários, ação em caso de falha e procedimento de recuperação.

## Qualidade dos sinais

Os resultados devem ser autenticados quando possível, datados em UTC, rastreáveis à origem e protegidos contra alteração indevida. Resultados antigos ou sem origem válida são inválidos para declarar sucesso.

## Estados permitidos

`PASS`, `WARN`, `FAIL`, `UNKNOWN`. Estado de incidente e severidade são campos separados. A transição para recuperação exige nova verificação satisfatória.

## Revisão

Rever inventário e critérios em mudanças materiais, incidentes, alterações de risco e revisão periódica definida pelo proprietário.
