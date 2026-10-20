# Subgrupo 01 · GoF Estrutural Adapter

Fontes de XP do PetVirtual. `SessaoPomodoro`, `ContagemDeAgua` e `Habito` têm regras e interfaces diferentes para gerar XP. Cada uma é embrulhada por um Adapter que implementa `FonteXP`. O `CreditadorXP` credita o XP conhecendo somente `FonteXP`.

| Papel no padrão | Arquivo |
|---|---|
| Client | `creditador_xp.py` |
| Target | `fonte_xp.py` |
| Adapter | `sessao_pomodoro_adapter.py`, `contagem_de_agua_adapter.py`, `habito_adapter.py` |
| Adaptee | `sessao_pomodoro.py`, `contagem_de_agua.py`, `habito.py` |

## Como executar

Requisito: Python 3.10 ou superior. Não há dependências externas.

A partir da raiz do repositório:

```shell
python3 codigo/subgrupo01_adapter/main.py
python3 -m unittest discover -s codigo/subgrupo01_adapter -v
```

A explicação completa está no relatório do Subgrupo 01, em `docs/Base/Relatórios/1.1.1.SubEquipe_01.md`.
