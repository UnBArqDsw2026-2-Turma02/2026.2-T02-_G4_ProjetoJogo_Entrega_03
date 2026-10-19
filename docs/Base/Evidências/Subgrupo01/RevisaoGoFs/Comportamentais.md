# Ficha de revisão — GoFs Comportamentais

**Subgrupo responsável pela revisão:** Subgrupo 01 — Padrões Estruturais.

**Participantes da revisão informados pelo grupo:** Guilherme Negreiros Pereira, Enzo Lopes Ferreira e Gabriel Pereira da Silva.

**Data de organização deste registro:** 19/10/2026.

**Material analisado:** versão do relatório do Subgrupo 03 encaminhada pelo grupo. <a href="Base/Evidências/Subgrupo01/RevisaoGoFs/fontes/relatorio-comportamentais.txt" target="_blank" rel="noopener">Consultar cópia de referência</a>.

Esta ficha registra uma análise documental dos contextos e trechos apresentados. Não atribui falas individuais nem representa uma sessão de testes dos exemplos. Os pontos de atenção são recomendações, sem presumir sua aplicação pelos responsáveis.

## Objetivo da leitura

Compreender como os padrões organizam notificações, transições e algoritmos, relacionando essas responsabilidades aos problemas do pet virtual e da conclusão de atividades.

## 1. Observer — comunicação da conclusão

O relatório apresenta uma atividade como publicadora e `PetVirtual` e `GerenciadorConquistas` como observadores. A comunicação usa `EventoConclusaoAtividade`.

```java
for (ObservadorAtividade observador : copia) {
    observador.emAtividadeConcluida(evento);
}
```

| Aspecto | Observação da revisão | Questão ou encaminhamento |
|---|---|---|
| Contrato de notificação | A publicadora conhece a interface, permitindo variar os destinatários. | Manter as regras de cada reação no observador correspondente. |
| Ocorrência concluída | O evento mostrado possui categoria e XP, sem identificador de conclusão. | Definir como evitar crédito duplicado se a mesma ocorrência for notificada novamente. |
| Isolamento de falhas | As chamadas aos observadores são sequenciais. | Decidir se a falha de um observador deve impedir os seguintes ou ser tratada separadamente. |
| Conquistas | O gerenciador apresentado imprime mensagens sobre a verificação. | Distinguir a notificação demonstrada do desbloqueio efetivo, que não aparece no trecho. |

## 2. State — ações conforme o estado

`SessaoPomodoro` e `PetVirtual` guardam o estado atual e delegam ações a ele. O contrato de Pomodoro rejeita operações não permitidas por meio de exceções; os estados concretos habilitam ações e solicitam transições.

| Aspecto | Observação da revisão | Questão ou encaminhamento |
|---|---|---|
| Estados da sessão | Configuração, foco, pausa e conclusão ficam separados em classes. | Demonstrar também uma operação inválida e a sequência de reinício após a conclusão. |
| Evolução do pet | Os estados apresentados usam limiares de XP total e avançam uma fase por avaliação. | Definir o comportamento quando uma única recompensa ultrapassa mais de um limiar. |
| Representação do domínio | O exemplo usa bebê, criança, adolescente e adulto; o recorte estrutural trata formas por categoria predominante. | Alinhar fase de vida e afinidade sem tratá-las automaticamente como o mesmo conceito. |

## 3. Strategy — variação da fórmula de XP

O contrato `CalculoXPStrategy` recebe dados de contexto. As atividades recebem uma estratégia por `setEstrategiaXP()` e delegam o cálculo.

Recorte da fórmula de Pomodoro apresentada:

```java
float xp = minutosFocados * fatorXPPorMinuto;
if (cicloConcluido) {
    xp += bonusCicloConcluido;
}
```

Com os parâmetros do trecho, 25 minutos, fator 2 e bônus 10 resultam em **60 XP**. O Factory Method do relatório criacional documenta **50 XP** por ciclo de 25 minutos. A diferença é identificada pela comparação das fórmulas, sem executar os exemplos.

| Aspecto | Observação da revisão | Questão ou encaminhamento |
|---|---|---|
| Substituição do algoritmo | A regra de pontuação está separada da entidade que solicita o valor. | Manter claro o contrato e a possibilidade de trocar a estratégia. |
| Descrição do contexto | O texto menciona `AssuntoAtividade`, mas os trechos mostram as três atividades guardando estratégias próprias. | Alinhar a descrição e o UML à alternativa efetivamente adotada. |
| Dados de entrada | Os exemplos montam um `Map` com valores fixos e fazem conversões de tipos. | Definir presença, tipos e limites dos dados, e obter os valores reais da atividade numa integração. |
| Balanceamento | Há diferenças de pontuação em relação aos demais recortes. | Conferir a regra comum de XP e distinguir parâmetros ilustrativos de regras vigentes. |
| Relação com Decorator | Strategy seleciona um algoritmo; Decorator aplica camadas sobre um componente. | Definir onde aplicar bônus se ambos forem utilizados, evitando contabilizá-los duas vezes. |

## 4. Memento — proposta ainda não detalhada

A metodologia menciona snapshots do pet, mas a seção de Memento na versão recebida mantém campos de contexto e UML a preencher. Por isso, a revisão registra a intenção de capturar e restaurar estado, sem atribuir uma implementação concluída ao material.

Questões para um detalhamento futuro:

- Quais dados compõem o snapshot?
- Quem cria, armazena e restaura os snapshots?
- Restaurar o pet também restaura histórico e conquistas?
- Como impedir que uma restauração permita conceder novamente a mesma recompensa?

## Síntese dos aprendizados

Observer distribui a comunicação por eventos; State concentra o comportamento permitido em cada estado; Strategy permite variar um algoritmo por contrato comum. A proposta de Memento trata da preservação e restauração de estado. Esses mecanismos resolvem problemas diferentes e precisam compartilhar regras e contratos se forem utilizados no mesmo fluxo.

[Voltar aos registros da revisão](README.md).
