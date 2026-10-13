# Instalação

Requisitos do MVP: Python 3.10 ou superior, sem dependências externas.

Na raiz do repositório:

```bash
python -m unittest discover -s WATCHDOG/tests -v
python WATCHDOG/engine/watchdog.py --check
```

O validador imprime JSON para stdout. Código de saída 2 indica erro de configuração/execução; código 1 indica falha verificável; código 0 indica que não foi encontrada falha verificável. Um resultado `UNKNOWN` permanece visível e não equivale a cobertura operacional completa.

O workflow GitHub Actions executa os testes quando há alterações no diretório WATCHDOG. Isso valida o código versionado, não instala um agente contínuo em sistemas externos.
