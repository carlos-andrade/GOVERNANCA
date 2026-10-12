# GOVERNANCA — Sistema Mestre de Governança e Orquestração

> Repositório-mestre para definir como projetos são propostos, priorizados, desenhados, executados, controlados, auditados e encerrados.

**Estado:** V1, proposta inicial em revisão. A existência de documentos não significa que políticas foram formalmente ratificadas ou que controlos técnicos estejam ativos.

<!-- GOVERNANCA_STATUS_START -->
## Barra de status do GOVERNANCA

**Estado atual:** Em execução — integração da barra de status concluída em `main`; adoção universal e automatização ainda pendentes.  
**Percentual comprovado desta iniciativa:** **80%**  
`[████████████████░░░░] 80%`

| Fase | Peso | Estado |
|---|---:|---|
| **Início** | 20% | Concluído — objetivo, norma e modelo definidos |
| **Meio** | 60% | Concluído — documentação integrada em `main` e README com painel de estado |
| **Fim** | 20% | Em curso — validar aplicação operacional, definir e testar atualização automática e concluir a adoção nos repositórios-alvo |

**Próximo marco:** implementar e testar mecanismo que atualize este painel quando o status do projeto mudar.  
**Bloqueios / limitações:** a atualização automática e a propagação da barra para todos os repositórios ainda não foram demonstradas. Até estarem ativas, a atualização deste README tem de ser feita no mesmo conjunto de alterações que muda o status.  
**Última atualização deste painel:** 2026-10-12.  
**Evidências:** [Pull Request #1 integrado](https://github.com/carlos-andrade/GOVERNANCA/pull/1) · [Norma de conclusão](standards/status-e-percentual-de-conclusao.md) · [Modelo de status](templates/projeto/status-do-projeto.md)

> **Regra de atualização imediata:** qualquer mudança de fase, percentual, bloqueio, aprovação, marco ou encerramento deve atualizar este painel no mesmo commit ou numa alteração imediatamente subsequente, antes de a mudança ser comunicada como status atual. Enquanto não houver automação testada, o responsável pela alteração deve atualizar manualmente o README e validar a renderização. Não afirmar que a sincronização automática está ativa sem evidência de implementação e teste.
<!-- GOVERNANCA_STATUS_END -->

## Começar por aqui

1. Leia [`CONSTITUICAO.md`](CONSTITUICAO.md) e [`docs/00-fundamentos/modelo-operacional.md`](docs/00-fundamentos/modelo-operacional.md).
2. Registe a iniciativa a partir de [`templates/projeto/charter.md`](templates/projeto/charter.md).
3. Classifique risco com [`templates/avaliacao/triagem-risco.md`](templates/avaliacao/triagem-risco.md).
4. Defina resultados mensuráveis, owner, dependências, riscos e critérios de aceitação.
5. Siga os gates G0–G6 descritos em [`docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md`](docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md).
6. Registe decisões, alterações, testes, incidentes e evidências.
7. Antes de produção, utilize [`templates/release/checklist-prontidao.md`](templates/release/checklist-prontidao.md).
8. Desde o início, publique no README do projeto a barra e o percentual usando [`templates/projeto/status-do-projeto.md`](templates/projeto/status-do-projeto.md), conforme a norma [`standards/status-e-percentual-de-conclusao.md`](standards/status-e-percentual-de-conclusao.md).

## Estrutura documental

- `CONSTITUICAO.md` — princípios e autoridade.
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
- `examples/` — exemplos não normativos.

## Regras fundamentais

- Todo projeto tem objetivo, responsável, beneficiários e critérios verificáveis.
- O controlo é proporcional ao risco e não dispensa obrigações legais/contratuais.
- Nenhum segredo ou dado pessoal desnecessário deve entrar em Git.
- Nenhum teste, execução ou publicação é declarado sem evidência verificável.
- Exceções têm dono, justificação, aprovador, prazo e plano de resolução.
- O repositório mestre guarda padrões; os repositórios de projeto guardam implementação e evidências específicas.

## Limitações da V1

Não é uma certificação, parecer jurídico, implementação automática de conformidade, proteção de branch nem pipeline CI/CD ativo. Configurações técnicas precisam de ser implementadas e testadas separadamente. O documento de apoio fornecido sobre modelos de governança de dados é referenciado na política em `docs/05-dados-e-ia/governanca-de-dados.md`.
