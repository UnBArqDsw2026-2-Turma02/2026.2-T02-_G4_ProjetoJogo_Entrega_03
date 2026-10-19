# Facade independente — demonstração Python

Requer Python 3.10 ou superior. Sem dependências externas.

Na raiz do repositório:

```sh
python docs/exemplos/facade/demo.py
python -m unittest discover -s docs/exemplos/facade -p "test_*.py" -v
```

Se o comando `python` não estiver disponível, use o caminho do interpretador instalado. No ambiente Codex deste projeto, os comandos foram verificados no PowerShell com:

```powershell
& "$env:USERPROFILE/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe" -B docs/exemplos/facade/demo.py
& "$env:USERPROFILE/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe" -B -m unittest discover -s docs/exemplos/facade -p 'test_*.py' -v
```

- `jogo_facade.py`: participantes do UML e coordenação da conclusão.
- `demo.py`: cliente, montagem e quatro cenários de execução.
- `test_jogo_facade.py`: sete testes do comportamento.

A entrada representa uma atividade já concluída, com categoria e XP calculados e validados. A fachada coordena XP, evolução, histórico e conquistas sem depender de Adapter ou Decorator. Os subsistemas usam memória; os critérios e valores são ilustrativos e não incluem persistência, concorrência ou transações.

## Vídeo da apresentação e execução

[Assistir ao vídeo do Facade — Guilherme Negreiros Pereira](https://youtu.be/QQM7oWCMstk). O vídeo também está incorporado na seção do Facade no relatório do Subgrupo 01.
