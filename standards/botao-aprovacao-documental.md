# Norma — Botão de aprovação documental

| Campo | Valor |
|---|---|
| **ID** | GOV-APPROVAL-BUTTON-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | NORMA |
| **Fase** | Aplicação transversal |
| **Estado** | APROVADO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 1917eada61e03e58ac55d365ee5168aba13f40231aa49437419472dfeaa2112c |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Carlos Andrade — instrução explícita registada na conversa de 2026-10-23 |
| **Origem** | Instrução explícita do responsável para padronizar o acesso à aprovação documental |
| **Autoridade superior** | [Norma de Cabeçalho Documental Padrão](../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) e [CONSTITUICAO.md](../CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git e registos de aprovação associados às versões documentais |

## 1. Regra obrigatória

Todo documento Markdown que aguarde aprovação formal deve apresentar, de forma visível junto ao cabeçalho ou no início do corpo, um botão verde com o texto exato **APROVAR AGORA?**. O botão deve abrir um registo de aprovação específico, acessível ao aprovador autorizado, que identifique inequivocamente o documento e a versão submetida.

## 2. Representação padrão no GitHub

Usar Markdown com um badge verde clicável. Exemplo:

[![APROVAR AGORA?](https://img.shields.io/badge/APROVAR%20AGORA%3F-%E2%9C%93-2ea44f?style=for-the-badge)](URL_DO_REGISTO_DE_APROVACAO)

Substituir URL_DO_REGISTO_DE_APROVACAO por um link real, verificado e específico para o documento/versão. Não criar links fictícios nem apontar todos os documentos para um registo genérico sem identidade documental.

## 3. Requisitos do registo de aprovação

1. Identificar ID, caminho e versão exata do documento submetido.
2. Apresentar o conteúdo ou link para a versão em revisão.
3. Indicar claramente como aprovar e como rejeitar/solicitar alterações.
4. Requerer uma manifestação explícita do aprovador autorizado.
5. Preservar evidência rastreável da decisão no histórico do sistema de controlo de versão.

## 4. Separação entre acesso e aprovação

Clicar no botão, abrir o link, visualizar o documento, reagir a uma publicação ou não responder **não** constitui aprovação. A aprovação só existe quando a pessoa autorizada regista explicitamente a decisão para a versão exata. Após qualquer alteração material ao documento, a aprovação anterior não se transfere automaticamente: criar/atualizar o registo para a nova versão e voltar a solicitar aprovação.

## 5. Estados e integridade documental

- Enquanto a aprovação não estiver registada e validada, manter o estado documental EM_REVISAO (ou o estado não aprovado que a norma de estados aplicável determinar).
- Não preencher o aprovador como confirmado nem alterar o estado para APROVADO apenas porque o botão foi adicionado.
- Atualizar a versão, a data, o histórico e o SHA-256 canónico do documento alterado.
- Depois de gravar, reler o documento no repositório e validar o destino do botão, a versão no registo, o hash e a coerência dos metadados.
- Não declarar a aprovação, validação ou execução de ações sem evidência verificável.

## 6. Adoção transversal

Esta norma passa a ser o padrão de referência para novos documentos e para documentos existentes que aguardem aprovação, sempre que o repositório e a plataforma suportem links clicáveis em Markdown. A adoção em cada repositório deve ser verificada e documentada; a publicação desta norma não prova que todos os consumidores a implementaram automaticamente.

## 7. Exemplo de instrução de aprovação

O registo deve pedir uma frase inequívoca, por exemplo: APROVO ID-DOCUMENTAL v1.2.3. O identificador e a versão do exemplo devem ser substituídos pelos valores reais do documento em análise.
