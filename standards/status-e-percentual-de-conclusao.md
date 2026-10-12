# Norma — Barra de estado e percentual de conclusão

## Objetivo
Todo projeto deve expor, desde a sua abertura até ao encerramento, uma barra de estado e um percentual de conclusão calculados por evidências verificáveis. A regra aplica-se a projetos de software, dados, conteúdo, infraestrutura, investigação, operações e projetos híbridos.

## Modelo de progresso (100 pontos)

| Fase | Peso | Evidência mínima para contabilizar |
|---|---:|---|
| **Início** | 20 pontos | Objetivo e problema definidos (5); responsável e partes interessadas identificados (3); escopo e exclusões registados (4); riscos e dependências iniciais avaliados (4); critérios de aceitação e plano aprovados (4). |
| **Meio** | 60 pontos | Entregáveis executados contra o plano (até 30); requisitos e decisões rastreáveis (10); testes/revisões proporcionais ao risco (10); documentação e evidências atualizadas (5); desvios e riscos tratados ou formalmente aceites (5). |
| **Fim** | 20 pontos | Critérios de aceitação demonstrados (8); validação/revisão final aprovada (4); entrega/publicação e operação ou destino final confirmados (3); documentação e transferência de conhecimento concluídas (2); aprovação de encerramento e lições aprendidas registadas (3). |

Os pontos de cada item só são atribuídos quando a respetiva evidência está registada e verificável. Itens não aplicáveis devem ser justificados, aprovados pelo responsável de governança do projeto e redistribuídos dentro da mesma fase; não podem desaparecer silenciosamente do denominador.

## Cálculo e barra

- **Percentual = pontos comprovados ÷ 100 × 100.** Não estimar progresso com base em tempo decorrido, esforço percebido ou quantidade de commits.
- Usar uma barra de 20 segmentos. Cada segmento representa 5 pontos percentuais. Arredondar a barra para baixo; apresentar o percentual numérico exato ao lado.
- Exemplo: `Progresso: 65%  [█████████████░░░░░░░]`
- O percentual não pode diminuir por trabalho concluído que continua válido; pode diminuir apenas se evidência for invalidada, o escopo aprovado mudar ou uma entrega for reprovada. Registar motivo, data e decisão.
- O percentual mede **conclusão comprovada do escopo aprovado**, não qualidade global, probabilidade de sucesso nem cumprimento de prazo. Apresentar separadamente saúde/prazo/risco quando necessário.
- Um projeto só pode atingir **100% — Concluído** após cumprir os critérios da fase Fim e obter aprovação explícita de encerramento. 100% não significa ausência de defeitos futuros; significa que o escopo e os deveres de encerramento acordados foram satisfeitos.
- Projeto suspenso, bloqueado ou cancelado mantém o percentual comprovado e recebe estado próprio. Cancelado não equivale a 100%.

## Estados obrigatórios

- **Não iniciado — 0%:** ainda não há trabalho aceite como concluído.
- **Em início — 1–20%:** definição e autorização inicial.
- **Em execução — 21–79%:** produção dos entregáveis.
- **Em finalização — 80–99%:** validação, entrega e encerramento.
- **Concluído — 100%:** critérios finais aprovados.
- **Bloqueado / Suspenso / Cancelado:** estado adicional obrigatório quando aplicável, sem alterar artificialmente o percentual.

O nome da fase deriva dos critérios e gates efetivamente atingidos; não é inferido apenas do número. Se houver conflito, prevalecem as evidências e o gate aprovado.

## Frequência de atualização

Atualizar a barra a cada marco/gate, alteração material de escopo, aprovação/reprovação, bloqueio, release ou encerramento; em projetos ativos, rever pelo menos semanalmente. Cada atualização regista data, percentual anterior/novo, evidências, responsável e motivo.

## Onde apresentar

A barra deve estar:
1. no README ou painel principal do repositório do projeto;
2. no registo/charter do projeto;
3. no relatório de estado periódico, quando existir.

Projetos pequenos podem manter um único registo simples. Projetos grandes podem automatizar o cálculo, mas a automação só é considerada ativa após implementação, teste e validação dos dados de entrada.

## Integridade

- Não declarar uma percentagem sem lista de critérios e evidências.
- Não usar a percentagem como substituto de testes, auditoria, aprovação, gestão de risco ou aceitação do utilizador.
- Manter histórico das alterações e identificar quem atualizou/aprovou.
- A governança central define a regra; cada repositório de projeto mantém o seu valor e evidências.
