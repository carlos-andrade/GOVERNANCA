# Modelo de execução

## Modos

- **CI/agenda:** validações periódicas de repositórios, documentação e pipelines.
- **Serviço permanente:** verificações com requisitos de baixa latência ou execução contínua.
- **Agente local:** sinais que não podem ser recolhidos remotamente.
- **Verificação externa:** sondagem independente para confirmar disponibilidade e detetar falha do monitor principal.

## Ciclo mínimo

1. Carregar inventário e configuração versionados.
2. Validar esquema, permissões e dependências.
3. Executar verificações dentro de timeout.
4. Classificar o resultado e a qualidade da evidência.
5. Emitir registo estruturado.
6. Notificar conforme política.
7. Confirmar recuperação e encerrar incidente apenas com evidência.

## Resiliência

Definir timeout, retry limitado, backoff, deduplicação e prevenção de tempestade de alertas. O resultado antigo deve expirar segundo a frequência declarada. A falha do destino de alertas deve ter canal alternativo para controlos críticos.

## Limites

Não implementar ações de correção automática até que o proprietário defina autorização, impacto, rollback, limites e teste de segurança.
