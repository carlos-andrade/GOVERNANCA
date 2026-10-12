# Modelo operacional

## Padrão de governança

Usar governança federada: princípios, níveis de risco, taxonomia, gates e formatos comuns no núcleo; execução autónoma pelos domínios dentro desses limites. Data Mesh é opção para domínios de dados maduros, não uma meta universal.

## Intensidade de controlo

- **A — Essencial:** protótipo reversível, baixo risco, sem dados sensíveis. Charter curto, owner, critérios de aceitação, versionamento e decisões críticas.
- **B — Normal:** integração ou uso por terceiros. Acrescentar análise de risco, desenho, revisão, testes, plano de lançamento e suporte.
- **C — Elevado:** produção crítica, dados pessoais/sensíveis ou impacto financeiro/operacional material. Revisão especializada, segregação quando possível, evidência formal, continuidade e autorização explícita.
- **D — Crítico:** serviços essenciais, segurança física, movimento de dinheiro ou alto impacto sobre pessoas. Governação setorial, revisão independente e salvaguardas específicas antes de avançar.

O nível depende da avaliação de risco e pode subir. Desconhecido não significa baixo risco. A classificação interna não substitui classificações legais ou regulatórias.

## Ciclo de controlo

Propor → classificar → planear → desenhar → executar → validar → lançar → observar → melhorar → encerrar. Cada transição tem responsável, evidência, decisão, pendências e risco residual.

## Repositório-mestre e repositórios de projeto

GOVERNANCA mantém políticas comuns, modelos, padrões, registos índice e taxonomia. Cada repositório de projeto mantém código, configuração, testes e evidência específica. Referenciar a versão normativa adotada; evitar duplicação e nunca guardar segredos em Git.

## Automação

Uma ferramenta não é por si só um controlo. Uma automação só é considerada ativa depois de implementada, testada, monitorizada, atribuída a um owner e acompanhada de procedimento de falha.