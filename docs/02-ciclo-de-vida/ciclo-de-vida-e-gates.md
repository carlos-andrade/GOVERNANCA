# Ciclo de vida e gates

| Gate | Objetivo | Evidência mínima | Decisão |
|---|---|---|---|
| G0 Entrada | Validar iniciativa | Problema, beneficiário, patrocinador e owner | Aceitar/devolver/rejeitar |
| G1 Viabilidade | Justificar investimento | Benefícios, alternativas, estimativa, riscos e dependências | Financiar/testar/suspender/cancelar |
| G2 Desenho | Construção segura e testável | Requisitos, arquitetura, dados, ameaças, aceitação e testes | Aprovar/corrigir/rejeitar |
| G3 Construção validada | Comprovar qualidade | Revisão, testes, artefactos e documentação | Aceitar/corrigir/bloquear |
| G4 Prontidão | Preparar operação | Segurança, backups, observabilidade, rollback, suporte | Lançar/bloquear |
| G5 Lançamento | Controlar implantação | Autorização, janela, métricas e rollback | Prosseguir/abortar/reverter |
| G6 Encerramento | Transferir/descontinuar | Aceitação, pendências, arquivo/eliminação e lições | Encerrar/transferir/prolongar |

Cada gate tem decisor autorizado, critérios prévios e registo de pendências. Combinar gates é admissível em baixo risco com justificação. Controlos críticos e obrigações não são dispensáveis. Cancelamentos registam dados, acessos, ativos, contratos e comunicações a tratar.