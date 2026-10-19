# Padrão Observer

Implementação do padrão comportamental Strategy em Java.

## Requisitos

- Java JDK instalado.

## Compilação

A partir da raiz do repositório, execute:

```bash
cd implementacoes_comportamentais/strategy
javac -d out $(find src -name "*.java")
```

## Execução

Após a compilação, execute:

```bash
java -cp out app.Main
```

## Estrutura

- `src/dominio/`: classes do domínio.
- `src/strategy/`: interfaces e classes relacionadas ao padrão Observer.
- `src/atividades/`: implementação das atividades observadas.
- `src/app/`: classe principal para execução e testes.