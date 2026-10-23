# Norma — Sincronização integral da documentação após alterações

| Campo | Valor |
|---|---|
| **ID** | GOV-DOC-SYNC-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | NORMA |
| **Fase** | Aplicação transversal |
| **Estado** | APROVADO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | cd6683f633adff00449443ffd932b411f6acc9271c48d312793de549e0c74aa1 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Carlos Andrade — instrução explícita registada no histórico de trabalho |
| **Origem** | Instrução explícita para estabelecer uma regra geral de sincronização documental |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e políticas da GOVERNANCA |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git e commits que implementem esta norma |

## 1. Regra obrigatória

Sempre que uma nova funcionalidade, correção, alteração técnica, decisão ou comportamento for implementado num projeto, a documentação afetada deve ser atualizada no mesmo conjunto de trabalho. A documentação não pode ficar deliberadamente desfasada do estado real do sistema.

## 2. Documentação a avaliar

Em cada alteração, avaliar explicitamente o impacto sobre os seguintes artefactos, quando existirem:

- requisitos funcionais e não funcionais;
- arquitetura, diagramas, decisões técnicas e modelos de dados;
- contratos e especificações de API, incluindo OpenAPI, exemplos e guias de integração;
- código, comentários técnicos e documentação de configuração;
- testes, critérios de aceitação, resultados e evidências de validação;
- segurança, privacidade, ameaças, permissões e tratamento de dados;
- instalação, operação, observabilidade, recuperação e runbooks;
- roadmap, estado, limitações conhecidas e dependências;
- README principal e documentação de entrada;
- registos de versões, alterações, decisões e rastreabilidade.

A lista é orientadora e não dispensa a análise de impacto específica. Não alterar artificialmente documentos sem impacto material; registar a avaliação quando necessário.

## 3. Procedimento obrigatório

1. Identificar os artefactos de implementação e os documentos relacionados antes da alteração.
2. Implementar a mudança e executar as verificações adequadas ao risco e ao tipo de alteração.
3. Atualizar todos os documentos cujo conteúdo, instruções, exemplos, contratos ou estado tenham sido afetados.
4. Atualizar o README principal para refletir o estado real, as capacidades, limitações e o roadmap, quando relevante.
5. Verificar coerência cruzada entre requisitos, arquitetura, API, código, testes e documentação operacional.
6. Recalcular os hashes documentais segundo a norma canónica aplicável.
7. Reler os ficheiros gravados no repositório e verificar links, versões, referências, hashes e evidências.
8. Registar no histórico de trabalho os documentos alterados, as validações realizadas e qualquer item que permaneça pendente.

## 4. Critério de fecho documental

Uma implementação só pode ser declarada **documentalmente fechada** quando:

- a mudança foi validada com evidências adequadas;
- todos os documentos afetados foram atualizados, ou a ausência de impacto foi avaliada e registada;
- o README e o roadmap refletem o estado confirmado, quando aplicável;
- os ficheiros foram relidos no repositório após a gravação;
- não existem contradições conhecidas entre o comportamento implementado e a documentação;
- limitações, falhas de teste e trabalho pendente estão explicitamente registados.

A conclusão documental não substitui testes funcionais, revisão de segurança, aprovação formal ou validação de produção.

## 5. Regras de integridade e transparência

- Nunca declarar uma funcionalidade como implementada, testada, segura ou pronta sem evidência apropriada.
- Não atualizar a documentação para afirmar um resultado que os testes não demonstraram.
- Manter a distinção entre proposta, implementação, validação e aprovação.
- Não apagar limitações conhecidas para aparentar conclusão.
- Preservar os cabeçalhos, identificadores, versões, hashes e regras de autoridade definidos pela GOVERNANCA.

## 6. Aplicação transversal

Esta norma deve ser adotada pelos repositórios consumidores segundo o processo de governança aplicável. A publicação desta norma no repositório-mestre, por si só, não prova que foi propagada ou adotada por todos os repositórios; cada adoção deve ser verificada e registada.

## 7. Estado

Norma registada a partir de instrução explícita do responsável. A sua adoção operacional por cada repositório continua sujeita à integração e validação local.
