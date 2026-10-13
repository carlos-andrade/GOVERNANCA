# Modelo de integração

Cada projeto adotante fornece:

- identificador único e proprietário;
- inventário de sistemas/processos e criticidade;
- controlos aplicáveis e justificativa para exclusões;
- adaptador e método de recolha;
- frequência, timeout e tolerância a dados atrasados;
- severidade, destinatários e prazos de resposta;
- formato e localização das evidências;
- procedimento de recuperação e contacto de escalonamento.

A integração começa em modo somente leitura. O adaptador deve demonstrar teste positivo, teste negativo, indisponibilidade, dados inválidos, timeout e recuperação. As credenciais são fornecidas pelo mecanismo de segredos do ambiente, nunca por ficheiros versionados.

Uma integração não pode declarar conformidade integral apenas porque o pipeline terminou com sucesso: a cobertura real e os controlos não implementados devem ser apresentados separadamente.
