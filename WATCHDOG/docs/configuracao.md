# Configuração

Edite `WATCHDOG/registry/sistemas-monitorizados.json`. Cada sistema deve ter ID único, nome, proprietário, criticidade e lista de verificações com IDs únicos.

Tipos locais suportados no MVP:
- `file_exists`
- `nonempty_file`
- `json_valid`

Tipos externos ainda não implementados resultam em `UNKNOWN`. Os caminhos são relativos à raiz do repositório e caminhos que escapem dessa raiz são rejeitados.

Antes de declarar um controlo obrigatório, definir o critério de sucesso, frequência, timeout, validade da evidência, severidade e responsável pela resposta. Não guardar credenciais no JSON.
