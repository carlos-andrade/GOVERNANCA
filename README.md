# GOVERNANCA — Sistema Mestre de Governança e Orquestração

> Repositório-mestre para definir como projetos são propostos, priorizados, desenhados, executados, controlados, auditados e encerrados.

**Estado:** V1, proposta inicial em revisão. A existência de documentos não significa que políticas foram formalmente ratificadas ou que controlos técnicos estejam ativos.

<!-- GOVERNANCA_STATUS_START -->
## Barra de status do GOVERNANCA

**Estado atual:** Em finalização — fase Fim.  
**Percentual comprovado:** **80%**  
`[████████████████░░░░] 80%`

| Fase | Pontos | Peso | Estado |
|---|---:|---:|---|
| **Início** | 20/20 | 20% | Concluído |
| **Meio** | 60/60 | 60% | Concluído |
| **Fim** | 0/20 | 20% | Pendente |

**Próximo marco:** Executar e validar o workflow WATCHDOG; depois implementar supervisão independente, alertas e adaptadores para os primeiros sistemas externos.  
**Bloqueios:** O WATCHDOG ainda não dispõe de adaptadores externos, alertas operacionais ou supervisão independente 24×7.; A adoção da barra de status e da sincronização automática nos restantes repositórios ainda não foi executada.  
**Última atualização do estado:** 2026-10-13  
**Evidências:** [Pull Request #1 integrado](https://github.com/carlos-andrade/GOVERNANCA/pull/1) · [Norma de percentual](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md) · [Workflow de sincronização](https://github.com/carlos-andrade/GOVERNANCA/blob/main/.github/workflows/sync-project-status.yml) · [Testes automatizados](https://github.com/carlos-andrade/GOVERNANCA/blob/main/tests/test_sync_project_status.py) · [WATCHDOG — arquitetura, normas e motor MVP](https://github.com/carlos-andrade/GOVERNANCA/tree/main/WATCHDOG) · [Workflow de validação WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/.github/workflows/watchdog-validation.yml)

> **Atualização automática:** este painel é gerado a partir de `registry/status-do-projeto.json`. Alterações nesse registo acionam o workflow `Sincronizar barra de status`. O workflow valida o esquema, as pontuações e os critérios de encerramento antes de atualizar este README. Não editar manualmente o painel; alterar a fonte de verdade e rever o resultado do workflow.
<!-- GOVERNANCA_STATUS_END -->

## Começar por aqui

**Monitorização transversal obrigatória:** consulte o [WATCHDOG](WATCHDOG/README.md), o [registo de sistemas monitorizados](WATCHDOG/registry/sistemas-monitorizados.json) e o [workflow de validação](.github/workflows/watchdog-validation.yml). O MVP valida configurações e ficheiros locais; integrações externas e monitorização contínua ainda exigem implementação e testes próprios.

1. Leia [`CONSTITUICAO.md`](CONSTITUICAO.md) e [`docs/00-fundamentos/modelo-operacional.md`](docs/00-fundamentos/modelo-operacional.md).
2. Registe a iniciativa a partir de [`templates/projeto/charter.md`](templates/projeto/charter.md).
3. Classifique risco com [`templates/avaliacao/triagem-risco.md`](templates/avaliacao/triagem-risco.md).
4. Defina resultados mensuráveis, owner, dependências, riscos e critérios de aceitação.
5. Siga os gates G0–G6 descritos em [`docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md`](docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md).
6. Registe decisões, alterações, testes, incidentes e evidências.
7. Antes de produção, utilize [`templates/release/checklist-prontidao.md`](templates/release/checklist-prontidao.md).
8. Desde o início, publique no README do projeto a barra e o percentual usando [`templates/projeto/status-do-projeto.md`](templates/projeto/status-do-projeto.md), conforme a norma [`standards/status-e-percentual-de-conclusao.md`](standards/status-e-percentual-de-conclusao.md).

## Estrutura documental

- `CONSTITUICAO.md` — princípios e autoridade, incluindo a norma transversal WATCHDOG.
- `WATCHDOG/` — política, arquitetura, contratos, inventário, motor de validação, adaptadores, runbooks e testes de monitorização.
- `docs/00-fundamentos/` — modelo operacional, taxonomia e adaptação proporcional.
- `docs/01-governanca/` — papéis, decisões, exceções e estados documentais.
- `docs/02-ciclo-de-vida/` — gates, requisitos e escopo.
- `docs/03-portfolio-e-estrategia/` — priorização.
- `docs/04-arquitetura-e-engenharia/` — padrões e controlo de versão.
- `docs/05-dados-e-ia/` — governança de dados, qualidade, linhagem e IA.
- `docs/06-seguranca-e-privacidade/` — segurança, privacidade e risco.
- `docs/07-operacoes-e-resiliencia/` — observabilidade, continuidade e incidentes.
- `docs/08-qualidade-e-validacao/` — critérios e validação.
- `docs/09-entrega-e-mudanca/` — mudanças e releases.
- `docs/10-fornecedores-e-dependencias/` — terceiros e licenças.
- `docs/11-financas-e-beneficios/` — custos e benefícios.
- `docs/12-conhecimento-e-documentacao/` — conhecimento institucional.
- `docs/13-comunicacao-e-stakeholders/` — comunicação e escalonamento.
- `docs/14-metricas-e-melhoria/` — indicadores e revisão.
- `docs/15-dominios-especializados/` — perfis por tipo de projeto.
- `templates/` — modelos reutilizáveis e checklists, incluindo o estado percentual de conclusão de cada projeto.
- `standards/status-e-percentual-de-conclusao.md` — cálculo uniforme, critérios de evidência e estados de conclusão.
- `standards/` — convenções.
- `registry/` — índices centrais leves.
- `automation/` — especificações para controlos automatizáveis.
- `.github/workflows/watchdog-validation.yml` — validação automatizada do motor WATCHDOG e dos registos locais.
- `examples/` — exemplos não normativos.

## Regras fundamentais

- Todo projeto tem objetivo, responsável, beneficiários e critérios verificáveis.
- O controlo é proporcional ao risco e não dispensa obrigações legais/contratuais.
- Nenhum segredo ou dado pessoal desnecessário deve entrar em Git.
- Nenhum teste, execução ou publicação é declarado sem evidência verificável.
- Exceções têm dono, justificação, aprovador, prazo e plano de resolução.
- O repositório mestre guarda padrões; os repositórios de projeto guardam implementação e evidências específicas.

## Limitações da V1

Não é uma certificação, parecer jurídico, implementação automática de conformidade ou proteção de branch. Os workflows existentes validam os respetivos artefactos quando acionados, mas não substituem monitorização independente 24×7. O WATCHDOG está em fase MVP: verificações locais e testes automatizados estão definidos; adaptadores externos, alertas operacionais, persistência protegida de evidências e supervisão independente ainda precisam de ser implementados e testados. O documento de apoio fornecido sobre modelos de governança de dados é referenciado na política em `docs/05-dados-e-ia/governanca-de-dados.md`.
