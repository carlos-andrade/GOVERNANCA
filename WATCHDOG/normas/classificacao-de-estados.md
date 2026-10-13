# Classificação de estados

- **PASS:** verificação executada, critério satisfeito e evidência válida.
- **WARN:** degradação, limiar preventivo, tendência adversa ou exceção dentro de prazo.
- **FAIL:** critério violado por evidência válida.
- **UNKNOWN:** verificação não executada, origem indisponível, evidência expirada, configuração não suportada ou dados insuficientes.

## Regras

1. Falta de dados nunca significa sucesso.
2. `UNKNOWN` não pode ser silenciosamente descartado; a criticidade determina se gera incidente.
3. A severidade não deve ser inferida apenas do estado: deve considerar impacto, urgência, extensão e obrigações.
4. A recuperação exige novo teste e registo da evidência.
5. Um resultado deve incluir timestamp, ID do controlo, origem, versão do avaliador e referência de evidência.
6. Os estados do controlo são distintos do estado do projeto e da percentagem de conclusão.
