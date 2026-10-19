# Ficha de revisão — GoFs Criacionais

**Subgrupo responsável pela revisão:** Subgrupo 01 — Padrões Estruturais.

**Participantes da revisão informados pelo grupo:** Guilherme Negreiros Pereira, Enzo Lopes Ferreira e Gabriel Pereira da Silva.

**Data de organização deste registro:** 19/10/2026.

**Material analisado:** versão do relatório do Subgrupo 02 encaminhada pelo grupo. <a href="Base/Evidências/Subgrupo01/RevisaoGoFs/fontes/relatorio-criacionais.txt" target="_blank" rel="noopener">Consultar cópia de referência</a>.

Este documento consolida a análise dos trechos apresentados no relatório. É uma ficha de revisão documental, com observações e questões de alinhamento; não é transcrição de reunião. As recomendações não representam correções já aplicadas pelos responsáveis.

## Objetivo da leitura

Entender como o jogo organiza a montagem do mascote e a instanciação das atividades, distinguindo esses problemas da organização de interfaces estudada pelo Subgrupo 01.

## 1. Builder — montagem do mascote

### Funcionamento identificado

O produto é `Mascote`. O contrato `MascoteBuilder` define as etapas de configuração; `MascoteConcretoBuilder` realiza a montagem; `MascoteDirector` reúne receitas. Os métodos encadeados tornam explícita a configuração de nome, estágio de vida, atributos, taxas e inventário.

### Trecho examinado

Recorte de `construir()` reproduzido no relatório recebido:

```javascript
if (!this.mascote.taxasDecaimento)
    this._calcularDecaimentoPorTemperamento();
const produto = this.mascote;
this.reset();
return produto;
```

| Ponto | Leitura da revisão | Encaminhamento sugerido |
|---|---|---|
| Separação entre montagem e uso | O Builder prepara o objeto; as ações do mascote não precisam ficar no construtor. | Preservar essa divisão quando acrescentar novas configurações. |
| Reutilização | `reset()` após a entrega inicia a preparação de outro produto. | Verificar com duas construções consecutivas se atributos e inventário não são compartilhados. |
| Temperamento e taxas | O construtor de `Mascote` já preenche `taxasDecaimento`; o recorte só recalcula quando esse objeto não existe. | Conferir o arquivo completo e o caminho de alteração do temperamento antes de concluir que as taxas são recalculadas. |
| Validação | O exemplo utiliza limites de 0 a 100 para os atributos. | Acrescentar casos com valor não numérico e não finito; o limite numérico, sozinho, não garante rejeição dessas entradas. |
| Correspondência UML–código | Interface, Director e Builder concreto apresentam uma API de montagem extensa. | Conferir a presença e a assinatura de cada método chamado na receita contra o arquivo completo. |

### Questão de alinhamento

Como a receita inicial do mascote deve se relacionar às fases de vida e formas por afinidade adotadas nos outros recortes? A montagem inicial e a evolução posterior precisam compartilhar definições do domínio, embora sejam responsabilidades distintas.

## 2. Factory Method — instanciação das atividades

### Funcionamento identificado

`CriadorDeAtividade` declara `criarAtividade()`. Os criadores concretos escolhem Pomodoro, check-in de hábito ou hidratação. A operação herdada `registrarAtividade()` trabalha pelo contrato de `Atividade`.

### Trecho examinado

Recorte do fluxo comum apresentado:

```javascript
const atividade = this.criarAtividade(dados);
atividade.validar();
const xp = atividade.calcularXP();
historico.registrarSessao(atividade);
mascote.receberXP(xp, atividade.getCategoria());
```

| Ponto | Leitura da revisão | Encaminhamento sugerido |
|---|---|---|
| Identificação do padrão | A especialização de `criarAtividade()` determina o produto concreto. | Destacar esse ponto ao explicar o Factory Method, separando-o do processamento posterior. |
| Fluxo comum | Validação, cálculo, histórico e crédito são reaproveitados pelos criadores. | Verificar os contratos exigidos por esse fluxo, como `getCategoria()` e `getNomeCategoria()`. |
| Cenários documentados | O relatório descreve três registros válidos e rejeições de sessão incompleta e de check-in fora de dia ativo. | Relacionar cada cenário à respectiva validação, sem tratar a leitura da saída como uma nova execução da revisão. |
| Relação com Facade e Observer | O fluxo já concede XP diretamente ao mascote. | Numa integração, escolher uma única autoridade de crédito para não somar novamente a recompensa por notificação ou por outra coordenação. |
| Evidência de vídeo | Na versão recebida, o campo de vídeo contém uma instrução de preenchimento. | Completar o vínculo quando o material estiver disponível. |

## Síntese dos aprendizados

Builder organiza como um objeto complexo é montado. Factory Method permite especializar qual produto é instanciado por uma operação de criação. A presença de um fluxo comum de registro não torna os dois padrões equivalentes nem substitui a necessidade de definir quem concede XP no jogo.

Os pontos desta ficha são observações sobre o material recebido. A conferência dos arquivos completos e a aplicação de mudanças permanecem encaminhamentos aos responsáveis.

[Voltar aos registros da revisão](README.md).
