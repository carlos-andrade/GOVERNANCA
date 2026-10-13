# Governança de dados
| Campo | Valor |
|---|---|
| **ID** | GOV-DATA-GOV-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | POLITICA |
| **Fase** | Dados e IA |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 4db9e4fe1f09eb6798743206a476ba9bc9c6c116c7e7ddb728edcf9ed080dc96 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `docs/05-dados-e-ia/governanca-de-dados.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Modelo organizacional

Usar como padrão governança federada: padrões, classificação e controlos comuns no núcleo; responsabilidade operacional nos domínios. Modelos centralizado, descentralizado/autónomo e orientado a domínio/Data Mesh podem ser adequados conforme escala, maturidade, obrigações e natureza dos dados.

## Papéis

Proprietário do dado (definição e uso permitido); steward/curador (metadados e qualidade); custodiante técnico (armazenamento, backup e acesso); consumidor (uso autorizado); segurança/privacidade (risco e obrigações).

## Controlos

1. Inventário de conjuntos de dados e origens.
2. Catálogo e glossário para ativos relevantes.
3. Classificação por sensibilidade e impacto.
4. Proveniência, qualidade e linhagem conforme risco.
5. Menor privilégio e RBAC/ABAC quando apropriado.
6. Retenção, arquivo, eliminação e resposta a pedidos.
7. Regras de qualidade mensuráveis, owner e escalonamento.
8. Registo de partilha e uso por terceiros quando relevante.
9. Gestão de incidentes e obrigações de notificação.

Qualidade inclui completude, validade, unicidade, consistência, atualidade, exatidão e rastreabilidade. A relevância de cada dimensão depende do uso.

## Conformidade

Referências ao RGPD são pontos de triagem, não conclusão jurídica. Base legal, prazos e avaliações exigidas dependem do contexto e devem ser confirmados por pessoa competente.

## Documento-base fornecido

O ficheiro “Os modelos de governança de dados mais utilizados.docx” identifica governança centralizada, descentralizada/autónoma, federada/híbrida e orientada a domínio/Data Mesh; destaca pessoas, políticas, processos e tecnologia como pilares. Este documento usa esses conceitos como referência inicial e acrescenta controlos operacionais.