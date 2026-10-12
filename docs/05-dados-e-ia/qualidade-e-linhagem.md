# Qualidade, proveniência e linhagem de dados

Para cada dataset crítico, declarar owner, descrição, granularidade, esquema, origem, frequência, regras de qualidade, consumidores, classificação, retenção, limitações e contacto operacional.

Validar esquemas, tipos, domínios, obrigatoriedade, duplicados, nulos, atrasos, saltos e alterações de esquema. Registar contagens de entrada/saída e reconciliação em pipelines críticos. Preservar origem, timestamp e versão da transformação. Definir quarentena/reprocessamento para dados inválidos. Distinguir zero, nulo, desconhecido, não aplicável e não recebido.

Ligar origem → transformação → ativo derivado → relatório/modelo → consumidor. Mudanças semânticas exigem análise de compatibilidade.