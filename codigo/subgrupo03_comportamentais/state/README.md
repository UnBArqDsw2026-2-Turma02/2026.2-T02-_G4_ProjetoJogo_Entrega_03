# Padrão State

Implementação do padrão comportamental State em Java.

## Requisitos

- Java JDK instalado.

## Compilação

A partir da raiz do repositório, execute:

```bash
cd implementacoes_comportamentais/state
javac -d out $(find src -name "*.java")
```

## Execução

Após a compilação, execute:

```bash
java -cp out app.Main
```

## Estrutura

- `src/state/pomodoro/`: estados da sessão Pomodoro.
- `src/state/pet/`: estados de desenvolvimento do pet virtual.
- `src/atividades/`: implementação da sessão Pomodoro.
- `src/dominio/`: classes do domínio.
- `src/app/`: classe principal para execução e testes.