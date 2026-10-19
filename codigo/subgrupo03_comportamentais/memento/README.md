# Padrão Memento

Implementação do padrão comportamental Memento em Java.

## Requisitos

- Java JDK instalado.

## Compilação

A partir da raiz do repositório, execute:

```bash
cd implementacoes_comportamentais/memento
javac -d out $(find src -name "*.java")
```

## Execução

Após a compilação, execute:

```bash
java -cp out app.Main
```

## Estrutura

- `src/dominio/`: classes do domínio.
- `src/memento/`: interfaces e classes relacionadas ao padrão Memento.
- `src/state/`: interface auxiliar para a modelagem dinâmica do Pet.
- `src/app/`: classe principal para execução e testes.