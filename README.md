# GOVERNANCA — Sistema Mestre de Governança e Orquestração

| Campo | Valor |
|---|---|
| **ID** | GOV-README-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | README |
| **Fase** | Entrada e orientação do repositório |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | d82477491f18a740caad5e84da33abfb503a3e3c6b57e8c31701bed7ba02cb26 |
| **Commit de referência (versão anterior)** | [62a2354c6372417a36c4df256fff267e691d8495](https://github.com/carlos-andrade/GOVERNANCA/commit/62a2354c6372417a36c4df256fff267e691d8495) |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal do README |
| **Autoridade superior** | [CONSTITUICAO.md](CONSTITUICAO.md) e [Norma de cabeçalho](CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


> Repositório-mestre para definir como projetos são propostos, priorizados, desenhados, executados, controlados, auditados e encerrados.

**Estado:** V1, proposta inicial em revisão. A existência de documentos não significa que políticas foram formalmente ratificadas ou que controlos técnicos estejam ativos.

<!-- GOVERNANCA_STATUS_START -->
## Painel executivo de status — GOVERNANCA

![Painel visual de status: 70% comprovados](assets/status-dashboard.svg)

**70% comprovados** · `[██████████████░░░░░░] 70%` · **Estado:** Em execução · **Fase:** Meio

| Fase | Pontos comprovados | Peso máximo | Estado |
|---|---:|---:|---|
| **Início** | 20/20 | 20% | Concluído |
| **Meio** | 50/60 | 60% | Em curso |
| **Fim** | 0/20 | 20% | Pendente |

**Próximo marco:** Executar e aprovar os testes da nova barra de status e do SVG no GitHub Actions; em seguida, revalidar no main a correção transversal de publicação concorrente e o gate WATCHDOG/B3.

**Bloqueios ativos (5):**
- A correção transversal de publicação concorrente dos 42 workflows ainda precisa de verificação conclusiva na branch main; não retirar o bloqueio sem evidência atual.
- Os limiares de atualidade BCB SGS, BDI, COTAHIST anual (30 dias) e COTAHIST diário (5 dias) continuam PROVISIONAL, sem aprovação dos proprietários registada.
- A supervisão externa independente ainda não foi comprovada como operacional: faltam confirmar configuração dos secrets, ausência de heartbeat e recuperação.
- Responsáveis, canais de alerta, confirmação de receção, ACK/escalonamento e SLA ainda precisam de aprovação e teste com evidência.
- A adoção transversal do padrão de roadmap e das regras de governança continua sujeita a inspeção, integração e aceitação individual por repositório.

**Última revisão:** 2026-10-17 · **Atualização do registo:** 2026-10-17

> **Limite da revisão:** Revisão documental efetuada em 2026-10-17. A pontuação foi rebaselined de forma conservadora: a barra anterior mostrava 80% agregado, mas os 10 pontos de testes da nova implementação só serão atribuídos após a execução bem-sucedida do conjunto atualizado. A issue B3 #9 está fechada no GitHub, mas o corpo publicado mantém a checklist de aceitação externa por concluir; o encerramento da issue, isoladamente, não prova aceitação operacional.

**Evidências:** [Norma de percentual e estados](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md) · [Testes automatizados da barra](https://github.com/carlos-andrade/GOVERNANCA/blob/main/tests/test_sync_project_status.py) · [Workflow de sincronização](https://github.com/carlos-andrade/GOVERNANCA/blob/main/.github/workflows/sync-project-status.yml) · [WATCHDOG — validação técnica](https://github.com/carlos-andrade/GOVERNANCA/actions/workflows/watchdog-validation.yml) · [Gate de aceitação WATCHDOG/B3](https://github.com/carlos-andrade/B3/issues/9) · [Issue de atualidade de dados B3](https://github.com/carlos-andrade/B3/issues/8)

> **Fonte de verdade:** `registry/status-do-projeto.json`. O script valida os critérios pontuados e gera este painel Markdown e o SVG. Não editar manualmente este bloco. Uma fase só recebe pontos se tiver evidência; 100% exige aprovação explícita de todos os controlos de encerramento.
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

## Padrão obrigatório de roadmap

O roadmap deste repositório e dos projetos que adotem formalmente estas regras deve seguir o [Roadmap padrão — Governança](ROADMAP-PADRAO-GOVERNANCA.md), nos termos da [Carta/Contrato — padrão obrigatório de roadmap](CARTA-CONTRATO-PADRAO-ROADMAP.md). A existência da norma não certifica automaticamente os repositórios adotantes: cada repositório deve ser inspecionado e validado individualmente.
