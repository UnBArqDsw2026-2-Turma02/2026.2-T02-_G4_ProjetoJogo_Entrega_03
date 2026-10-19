#### Metodologia do Foco_02

##### Objetivo e delimitação

Esta seção trata da aplicação do padrão GoF estrutural Adapter às fontes de XP do PetVirtual. O objetivo é permitir que o crédito de XP trate Pomodoro, água e hábito pela mesma interface, sem conhecer a regra de cada atividade. A demonstração é independente dos padrões Decorator e Facade dos demais integrantes.

O responsável pela seção é Enzo Lopes Ferreira, conforme a divisão registrada na Reunião de Alinhamento Geral do Subgrupo 01.

##### Processo de elaboração

| Etapa | Procedimento | Resultado e situação |
|---|---|---|
| Ideação | Na Reunião de Alinhamento Geral, a integração de atividades com interfaces diferentes foi associada ao Adapter. | Problema e padrão definidos. |
| Contexto para a IA | Enzo descreveu o problema e a ideia de aplicação em um prompt ao Claude Code, com os links do template da professora e do projeto. O link da Entrega 01, enviado por engano, foi corrigido para o da Entrega 02. | Prompts registrados nas [Evidências](/Base/Evidências/1.1.1.SubEquipe_01.md#prompts-e-documentos-de-ia). |
| Modelagem e implementação | A IA gerou os diagramas de classes e de sequência em Mermaid, o código Python e os testes, a partir do Diagrama de Classes da Entrega 02. | Primeira versão. |
| Revisão | Conferência com as regras de negócio da Entrega 02. O XP do Pomodoro foi alinhado à RN01 (+50 XP por sessão de 25 minutos), a evolução do pet (RN05) foi incluída no código e no diagrama, e a divergência da água em relação à RN01 foi registrada. A linguagem prevista no início era JavaScript; Enzo optou por Python. | Versão revisada; 16 testes passam. |
| Execução e vídeo | Enzo gravou a narração (lógica, diagramas e uso dos prompts) e o Terminal executando a demonstração e os testes; o vídeo foi montado com apoio de IA sobre essas gravações. | Vídeo publicado: [youtu.be/pcs7FTFvy3M](https://youtu.be/pcs7FTFvy3M). |
| Evidências | Registro dos prompts, da execução e do commit. | [Evidências do Subgrupo 01](/Base/Evidências/1.1.1.SubEquipe_01.md). |

#### GoF Estrutural
##### Contexto (Problema)

O PetVirtual evolui conforme o XP que o usuário acumula em cinco categorias (`CategoriaXP`). O [Diagrama de Classes da Entrega 02](https://github.com/UnBArqDsw2026-2-Turma02/2026.2-T02-_G4_ProjetoJogo_Entrega_02/blob/main/docs/Base/Relat%C3%B3rios/1.1.1.SubEquipe_01.md) definiu três atividades que geram esse XP. Cada uma tem interface e regra próprias:

| Atividade | Quando gera XP | Categoria do XP |
|---|---|---|
| `SessaoPomodoro` | Depois de `finalizarSessao()`, com `statusSessao = CONCLUIDA` | `INTELECTUAL` ou `SABEDORIA`, escolhida na sessão |
| `ContagemDeAgua` | Quando `validarMetaDiaria()` é verdadeiro | Sempre `HIDRATACAO` (restrição `{readOnly}`) |
| `Habito` | Quando `verificarConclusaoAoDia(data)` é verdadeiro | A categoria do próprio hábito |

Sem um padrão, quem credita o XP precisa conhecer as três classes e as três regras:

```python
# Sem o padrão: o creditador conhece cada atividade concreta
if isinstance(atividade, SessaoPomodoro) and atividade.statusSessao == "CONCLUIDA":
    pet.adicionarXP(atividade.categoria, atividade.calcularXPGanho())
elif isinstance(atividade, ContagemDeAgua) and atividade.validarMetaDiaria():
    pet.adicionarXP(CategoriaXP.HIDRATACAO, atividade.calcularXPGanho())
elif isinstance(atividade, Habito) and atividade.verificarConclusaoAoDia(hoje):
    pet.adicionarXP(atividade.categoria, atividade.calcularXPGanho())
```

Essa abordagem gera três problemas:

1. **Acoplamento.** O creditador depende de três classes concretas e de três assinaturas diferentes.
2. **Extensão difícil.** Cada atividade nova (por exemplo, um treino registrado por um aplicativo externo, na categoria `ATLETICO`) obriga a alterar o creditador.
3. **Responsabilidade espalhada.** Nos Diagramas de Estados da Entrega 02, `SessaoPomodoro` (estado `CONCLUIDA`) e `Habito` (estado `CUMPRIDO`) chamam `PetVirtual.adicionarXP()` diretamente. As atividades conhecem o pet.

##### Padrão selecionado e justificativa

O padrão escolhido é o Adapter (GoF Estrutural). A intenção do Adapter é converter a interface de uma classe em outra interface que os clientes esperam, permitindo que classes com interfaces incompatíveis trabalhem juntas (GAMMA et al., 1994). Aqui, cada atividade é embrulhada por um Adapter que fala uma única interface, `FonteXP`. O creditador passa a conhecer somente essa interface.

| Papel no padrão (GAMMA et al., 1994) | Classe no projeto | Responsabilidade |
|---|---|---|
| Client | `CreditadorXP` | Credita XP no `PetVirtual` a partir de qualquer `FonteXP` e impede crédito duplicado. |
| Target | `FonteXP` | Interface comum: `podeGerarXP()`, `obterCategoria()`, `obterPontos()` e `obterChaveCredito()`. |
| Adapter | `SessaoPomodoroAdapter`, `ContagemDeAguaAdapter`, `HabitoAdapter` | Traduzem a regra, a categoria e os pontos de cada atividade para a interface `FonteXP`. |
| Adaptee | `SessaoPomodoro`, `ContagemDeAgua`, `Habito` | Classes de domínio da Entrega 02, mantidas com a interface original. |

##### Alternativas consideradas

- **Atividades implementando `FonteXP` diretamente.** O cenário clássico do Adapter é uma classe que não pode ser alterada, como uma biblioteca de terceiros (GAMMA et al., 1994). Aqui, uma alternativa seria fazer as três atividades implementarem `FonteXP` diretamente. A equipe preferiu o Adapter por três motivos: (1) mantém as atividades focadas no próprio domínio, sem regras de gamificação, o que preserva a Alta Coesão (GRASP); (2) preserva a interface modelada e validada na Entrega 02; (3) o `HabitoAdapter` fornece a data que `verificarConclusaoAoDia(data)` exige. Larman (2004) descreve o Adapter como aplicação de Indireção e Polimorfismo para obter Variações Protegidas, o que liga esta entrega ao módulo de GRASPs. O custo é de três classes a mais.
- **Adapter de classe (herança).** Foi adotado o **Adapter de objeto** (composição): cada Adapter guarda uma referência à atividade adaptada. O Adapter de classe (herança múltipla) também é possível em Python, mas expõe pelo Adapter todos os métodos da atividade e prende o Adapter a uma classe concreta. O Adapter de objeto funciona com a classe adaptada e com qualquer subclasse dela (GAMMA et al., 1994).

##### Escopo, premissas e decisões

- **Mudança em relação à Entrega 02.** Os Diagramas de Estados de `SessaoPomodoro` e `Habito` registram `PetVirtual.adicionarXP()` como ação de entrada dos estados `CONCLUIDA` e `CUMPRIDO`. Com o Adapter, essa chamada passa a ser do `CreditadorXP`. As atividades apenas mudam de estado.
- **Crédito duplicado.** `validarMetaDiaria()` continua verdadeiro até o fim do dia. Sem controle, cada consulta creditaria XP de novo. Por isso, o Target inclui `obterChaveCredito()`. Limitação: as chaves ficam em memória; a persistência está fora do escopo desta entrega.
- **Getters.** O Diagrama de Classes da Entrega 02 marca os atributos como privados e não lista getters. O Adapter precisa ler `statusSessao` e `categoria`. A equipe considerou os getters omitidos por convenção e os implementou como propriedades somente leitura (`@property`).
- **Nome do método de `Habito`.** O Diagrama de Classes da Entrega 02 traz `verificarConclusoAoDia`, e o texto do relatório traz `verificarConclusaoAoDia`. O código adota a segunda forma.
- **Valores de XP.** O XP do Pomodoro segue a RN01 da Entrega 02: uma sessão de 25 minutos concluída concede +50 XP. Como o XP considera só o tempo de foco cumprido, o código usa 2 XP por minuto. A RN01 não fixa os valores da água e do hábito, então o código usa valores ilustrativos: 20 XP pela meta de água e 15 XP por hábito concluído. Em todos os casos, a regra de pontuação fica no Adaptee (`calcularXPGanho()`) e o Adapter apenas repassa os pontos. O Adapter define só a condição de crédito (`podeGerarXP()`) e a identidade do evento (`obterChaveCredito()`), sem calcular XP.
- **Divergência na água.** A RN01 prevê XP a cada registro de 250 ml. O código credita XP uma vez por dia, quando `validarMetaDiaria()` fica verdadeiro, porque essa é a regra exposta pela interface de `ContagemDeAgua` no Diagrama de Classes. Creditar por registro exigiria observar cada chamada de `adicionarVolume()`, o que é um modelo de eventos diferente. A divergência deve ser conciliada com a equipe, ajustando a RN01 ou o modelo.
- **Evolução do pet.** `determinarEvolucao()` considera só a categoria predominante do `vetorXP`. Se o vetor estiver zerado ou houver empate no topo, a forma é `NEUTRO`, como registram as decisões do PetVirtual na Entrega 02. A RN05 também exige taxa de conclusão de pelo menos 75%, calculada em `Usuario.calcularTaxaCompletacao()`, e usa a taxa abaixo de 40% para a forma `DESMOTIVADO`. Essa parte fica fora do escopo do Adapter.
- **Recortes.** Os ciclos de descanso do Pomodoro e o congelamento de streak do Hábito ficaram fora do código, pois não interferem no padrão.
- **Convenção de nomes.** Os métodos usam camelCase, fora do padrão PEP 8 do Python, para manter correspondência direta com o modelo UML.

##### Modelagem (Notação UML)

###### Diagrama de classes

A modelagem estática mostra os participantes do padrão e a ligação com as classes da Entrega 02. As notas amarelas indicam o papel de cada classe no padrão e a tradução feita por cada Adapter.

<figure class="state-diagram">
  <img src="Base/assets/subEquipe01/adapter-diagrama-classes.png" alt="Diagrama de Classes do padrão Adapter aplicado às fontes de XP" width="1568" height="814" loading="lazy" tabindex="0" role="button" aria-label="Ampliar Diagrama de Classes do padrão Adapter">
  <figcaption><em>Figura 1 — Diagrama de Classes do padrão Adapter (fontes de XP do PetVirtual)</em><br>Fonte: Elaborado pelos autores, a partir do Diagrama de Classes da Entrega 02.</figcaption>
</figure>

<details class="diagram-source">
<summary>Ver código Mermaid — Diagrama de Classes do Adapter</summary>

```text
classDiagram
    direction TB

    class CreditadorXP {
        - chavesCreditadas: Set~String~
        + creditar(fonte: FonteXP) ResultadoCredito
    }

    class ResultadoCredito {
        <<enumeration>>
        CREDITADO
        REGRA_NAO_CUMPRIDA
        JA_CREDITADO
    }

    class FonteXP {
        <<interface>>
        + podeGerarXP() boolean
        + obterCategoria() CategoriaXP
        + obterPontos() int
        + obterChaveCredito() String
    }

    class SessaoPomodoroAdapter {
        - sessao: SessaoPomodoro
        + podeGerarXP() boolean
        + obterCategoria() CategoriaXP
        + obterPontos() int
        + obterChaveCredito() String
    }

    class ContagemDeAguaAdapter {
        - contagem: ContagemDeAgua
        + podeGerarXP() boolean
        + obterCategoria() CategoriaXP
        + obterPontos() int
        + obterChaveCredito() String
    }

    class HabitoAdapter {
        - habito: Habito
        - data: Date
        + podeGerarXP() boolean
        + obterCategoria() CategoriaXP
        + obterPontos() int
        + obterChaveCredito() String
    }

    class SessaoPomodoro {
        - statusSessao: String
        - tempoDecorrido: int
        + iniciarSessao() void
        + finalizarSessao() void
        + calcularXPGanho() int
    }

    class ContagemDeAgua {
        - volumeML: int
        - limiteDiario: int
        - dataRegistro: Date
        + adicionarVolume(ml: int) void
        + validarMetaDiaria() boolean
        + calcularXPGanho() int
        + resetarDiario() void
    }

    class Habito {
        - streakAtual: int
        - dataUltimaCompletacao: Date
        + marcarConcluido() void
        + verificarConclusaoAoDia(data: Date) boolean
        + calcularXPGanho() int
    }

    class PetVirtual {
        - vetorXP: int[5]
        + adicionarXP(categoria: CategoriaXP, pontos: int) void
        + calcularAtividadeMaxima() CategoriaXP
        + determinarEvolucao() Evolucao
        + obterEstadoAtual() String
    }

    class Evolucao {
        <<enumeration>>
        NEUTRO
        ESTUDIOSO
        LEITOR
        ZEN
        ATLETICO
        HIDRATADO
        DESMOTIVADO
    }

    class CategoriaXP {
        <<enumeration>>
        INTELECTUAL
        SABEDORIA
        ZEN
        ATLETICO
        HIDRATACAO
    }

    CreditadorXP ..> FonteXP : usa
    CreditadorXP ..> ResultadoCredito : retorna
    CreditadorXP "1" --> "1" PetVirtual : creditaXP

    FonteXP <|.. SessaoPomodoroAdapter
    FonteXP <|.. ContagemDeAguaAdapter
    FonteXP <|.. HabitoAdapter

    SessaoPomodoroAdapter "1" --> "1" SessaoPomodoro : adapta
    ContagemDeAguaAdapter "1" --> "1" ContagemDeAgua : adapta
    HabitoAdapter "1" --> "1" Habito : adapta

    PetVirtual "1" --> "5" CategoriaXP : vetorXPMapeadoPor
    PetVirtual "1" --> "1" Evolucao : evoluiPara

    note for CreditadorXP "Client: depende só de FonteXP"
    note for FonteXP "Target"
    note for SessaoPomodoroAdapter "podeGerarXP(): statusSessao == CONCLUIDA<br>obterCategoria(): categoria da sessão<br>(INTELECTUAL ou SABEDORIA)"
    note for ContagemDeAguaAdapter "podeGerarXP(): validarMetaDiaria()<br>obterCategoria(): HIDRATACAO"
    note for HabitoAdapter "podeGerarXP(): verificarConclusaoAoDia(data)<br>obterCategoria(): categoria do hábito"
```

Arquivo-fonte: <a href="Base/assets/subEquipe01/adapter-diagrama-classes.mmd" target="_blank" rel="noopener">adapter-diagrama-classes.mmd</a>.

</details>

Os atributos das atividades aparecem resumidos: a figura mostra os atributos e métodos relevantes ao crédito de XP, e os identificadores e a associação com `CategoriaXP` foram omitidos. A lista completa está no Diagrama de Classes da Entrega 02.

###### Diagrama de sequência

A modelagem dinâmica mostra uma rodada de crédito para a sessão Pomodoro. O `CreditadorXP` conversa somente com o Adapter. Só o Adapter conversa com a `SessaoPomodoro`.

<figure class="state-diagram">
  <img src="Base/assets/subEquipe01/adapter-diagrama-sequencia.png" alt="Diagrama de Sequência do crédito de XP de uma sessão Pomodoro via Adapter" width="1568" height="1506" loading="lazy" tabindex="0" role="button" aria-label="Ampliar Diagrama de Sequência do Adapter">
  <figcaption><em>Figura 2 — Diagrama de Sequência: crédito de XP de uma sessão Pomodoro concluída</em><br>Fonte: Elaborado pelos autores.</figcaption>
</figure>

<details class="diagram-source">
<summary>Ver código Mermaid — Diagrama de Sequência do Adapter</summary>

```text
sequenceDiagram
    autonumber
    actor U as Usuário
    participant J as :Aplicação
    participant S as :SessaoPomodoro
    participant C as :CreditadorXP
    participant A as :SessaoPomodoroAdapter
    participant P as :PetVirtual

    U->>J: encerra o Pomodoro
    J->>S: finalizarSessao()
    Note over S: statusSessao = CONCLUIDA
    J->>C: creditar(fonte: FonteXP)
    C->>A: podeGerarXP()
    A->>S: statusSessao
    S-->>A: CONCLUIDA
    A-->>C: true
    C->>A: obterChaveCredito()
    A-->>C: "pomodoro:sessao-01"
    alt chave ainda não creditada
        C->>A: obterCategoria()
        A->>S: categoria
        S-->>A: INTELECTUAL
        A-->>C: INTELECTUAL
        C->>A: obterPontos()
        A->>S: calcularXPGanho()
        S-->>A: 50
        A-->>C: 50
        C->>P: adicionarXP(INTELECTUAL, 50)
        C-->>J: CREDITADO
    else chave já creditada
        C-->>J: JA_CREDITADO
    end
    Note over C,A: ContagemDeAguaAdapter e HabitoAdapter seguem a mesma sequência.<br/>Muda só a tradução dentro do Adapter.
```

Arquivo-fonte: <a href="Base/assets/subEquipe01/adapter-diagrama-sequencia.mmd" target="_blank" rel="noopener">adapter-diagrama-sequencia.mmd</a>.

</details>

`ContagemDeAguaAdapter` e `HabitoAdapter` seguem a mesma sequência. Muda somente a tradução dentro de cada Adapter:

| Método de `FonteXP` | `SessaoPomodoroAdapter` | `ContagemDeAguaAdapter` | `HabitoAdapter` |
|---|---|---|---|
| `podeGerarXP()` | `statusSessao == "CONCLUIDA"` | `validarMetaDiaria()` | `verificarConclusaoAoDia(data)` |
| `obterCategoria()` | `categoria` da sessão | `HIDRATACAO` | `categoria` do hábito |
| `obterPontos()` | `calcularXPGanho()` | `calcularXPGanho()` | `calcularXPGanho()` |
| `obterChaveCredito()` | `pomodoro:<idSessao>` | `agua:<id>:<dataRegistro>` | `habito:<idHabito>:<data>` |

##### Implementação (Código & Vídeo com Padrão em Execução)

O código está em [`codigo/subgrupo01_adapter`](https://github.com/UnBArqDsw2026-2-Turma02/2026.2-T02-_G4_ProjetoJogo_Entrega_03/tree/main/codigo/subgrupo01_adapter), em Python 3.10 ou superior, sem dependências externas. Os nomes de classes e métodos seguem os do modelo UML, para manter a rastreabilidade.

| Arquivo | Papel no padrão |
|---|---|
| `fonte_xp.py` | Target |
| `sessao_pomodoro_adapter.py`, `contagem_de_agua_adapter.py`, `habito_adapter.py` | Adapter |
| `sessao_pomodoro.py`, `contagem_de_agua.py`, `habito.py` | Adaptee |
| `creditador_xp.py` | Client |
| `pet_virtual.py`, `categoria_xp.py`, `evolucao.py` | Classes de apoio do domínio |
| `main.py` | Demonstração em execução |
| `test_adapter.py` | Testes automatizados (16 casos) |

**Target: `FonteXP`.** Classe abstrata (`abc.ABC`) com os quatro métodos que o Client espera. Uma classe que não implementa todos os métodos não pode ser instanciada.

```python
class FonteXP(ABC):
    @abstractmethod
    def podeGerarXP(self) -> bool: ...
    @abstractmethod
    def obterCategoria(self) -> CategoriaXP: ...
    @abstractmethod
    def obterPontos(self) -> int: ...
    @abstractmethod
    def obterChaveCredito(self) -> str: ...
```

**Adapters.** Cada Adapter recebe a atividade no construtor (composição) e traduz cada método de `FonteXP` para a interface da atividade. O `HabitoAdapter` também guarda a data avaliada, porque `verificarConclusaoAoDia(data)` exige um parâmetro que `podeGerarXP()` não tem.

```python
class SessaoPomodoroAdapter(FonteXP):
    def __init__(self, sessao: SessaoPomodoro):
        self._sessao = sessao

    def podeGerarXP(self) -> bool:
        return self._sessao.statusSessao == "CONCLUIDA"

    def obterCategoria(self) -> CategoriaXP:
        return self._sessao.categoria  # INTELECTUAL ou SABEDORIA


class ContagemDeAguaAdapter(FonteXP):
    def podeGerarXP(self) -> bool:
        return self._contagem.validarMetaDiaria()

    def obterCategoria(self) -> CategoriaXP:
        return ContagemDeAgua.CATEGORIA  # sempre HIDRATACAO


class HabitoAdapter(FonteXP):
    def __init__(self, habito: Habito, data: date | None = None):
        self._habito = habito
        self._data = data or date.today()

    def podeGerarXP(self) -> bool:
        return self._habito.verificarConclusaoAoDia(self._data)
```

**Client: `CreditadorXP`.** O módulo não importa nenhuma atividade concreta. O método `creditar()` trata qualquer `FonteXP` da mesma forma. A chave de crédito impede que o mesmo evento gere XP duas vezes.

```python
def creditar(self, fonte: FonteXP) -> ResultadoCredito:
    if not fonte.podeGerarXP():
        return ResultadoCredito.REGRA_NAO_CUMPRIDA
    chave = fonte.obterChaveCredito()
    if chave in self._chavesCreditadas:
        return ResultadoCredito.JA_CREDITADO
    self._pet.adicionarXP(fonte.obterCategoria(), fonte.obterPontos())
    self._chavesCreditadas.add(chave)
    return ResultadoCredito.CREDITADO
```

**Execução.** A partir da raiz do repositório:

```shell
python3 codigo/subgrupo01_adapter/main.py
python3 -m unittest discover -s codigo/subgrupo01_adapter -v
```

A demonstração executa quatro rodadas de crédito sobre as mesmas três fontes e, ao fim de cada uma, mostra o `vetorXP` e a forma do pet (`determinarEvolucao()`): (1) nenhuma regra cumprida, nenhum XP, forma `NEUTRO`; (2) as três atividades concluídas, XP creditado em `INTELECTUAL` (+50), `HIDRATACAO` (+20) e `ZEN` (+15), e o pet passa a `ESTUDIOSO`; (3) o usuário bebe mais água depois da meta, e nada é creditado de novo; (4) no dia seguinte, água e hábito voltam a gerar XP, mas a sessão Pomodoro do dia anterior não. Ao final, a demonstração mostra a restrição da Entrega 02: uma `SessaoPomodoro` não aceita a categoria `HIDRATACAO`.

<div class="evidence-slot"><strong>Vídeo do padrão em execução</strong>
<p>Narração de Enzo Lopes Ferreira (aprox. 4min30): contexto e problema, a solução em Adapter (Target, Adapters, Adaptees e Client), os diagramas de classes e de sequência com destaque em cada parte, o uso da IA pelos prompts e a execução de <code>main.py</code> e dos 16 testes no Terminal.</p>
<div style="position:relative;width:100%;max-width:860px;aspect-ratio:16/9;margin:0.5rem 0;">
  <iframe src="https://www.youtube.com/embed/pcs7FTFvy3M" title="Padrão Adapter — fontes de XP do PetVirtual" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe>
</div>
<p><a href="https://youtu.be/pcs7FTFvy3M" target="_blank" rel="noopener">▶ Abrir no YouTube</a></p></div>

##### Rastreabilidade das decisões

| Requisito ou problema | Decisão e papel do padrão | Modelo UML | Código | Evidência de execução |
|---|---|---|---|---|
| Três atividades com regras de XP diferentes (Diagrama de Classes da Entrega 02) | Um Adapter por atividade traduz a regra para `FonteXP` | Figura 1 | `*_adapter.py` | `main.py`, rodadas 1 e 2 |
| O creditador não deve depender das atividades concretas | `CreditadorXP` (Client) depende somente de `FonteXP` (Target) | Figuras 1 e 2 | `creditador_xp.py` | `test_fonte_nova_funciona_sem_alterar_o_creditador` |
| Pomodoro gera XP só em `INTELECTUAL` ou `SABEDORIA` (restrição da Entrega 02) | A atividade valida a categoria; o Adapter repassa a categoria da sessão | Figura 1 | `sessao_pomodoro.py`, `sessao_pomodoro_adapter.py` | `main.py`, última etapa; `test_restricao_de_categoria` |
| Água gera XP sempre em `HIDRATACAO` (restrição `{readOnly}` da Entrega 02) | `ContagemDeAguaAdapter.obterCategoria()` devolve sempre `HIDRATACAO` | Figura 1 | `contagem_de_agua_adapter.py` | `test_credita_sempre_em_hidratacao` |
| `validarMetaDiaria()` continua verdadeiro depois da meta | Chave de crédito por dia; o Client ignora chave já creditada | Figura 2 (fragmento `alt`) | `creditador_xp.py` | `main.py`, rodada 3; `test_volume_extra_no_mesmo_dia_nao_credita_de_novo` |
| `verificarConclusaoAoDia(data)` exige uma data | `HabitoAdapter` guarda a data avaliada | Figura 1 | `habito_adapter.py` | `test_conclusao_de_outro_dia_nao_conta` |
| RN01 (Entrega 02): sessão Pomodoro de 25 min concede +50 XP | A regra de pontuação fica no Adaptee (`calcularXPGanho()`); o Adapter só repassa os pontos | Figuras 1 e 2 | `sessao_pomodoro.py` | `main.py`, rodada 2; `test_credita_na_categoria_da_sessao_depois_de_concluida` |
| RN05 (Entrega 02): a forma do pet segue a categoria predominante | `PetVirtual.determinarEvolucao()` usa `calcularAtividadeMaxima()` | Figura 1 | `pet_virtual.py`, `evolucao.py` | `main.py`, todas as rodadas; `TestEvolucaoDoPet` |

##### Referências utilizadas por Enzo — Adapter

- SERRANO, Milene. **Aula — GoFs Estruturais**. Material da disciplina Arquitetura e Desenho de Software. <a href="Base/Referencias/Aula_GoFs_Estruturais_Profa_Milene.pdf" target="_blank" rel="noopener">Abrir PDF disponibilizado pela equipe</a>.
- GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. **Design Patterns: Elements of Reusable Object-Oriented Software**. Reading: Addison-Wesley, 1994.
- LARMAN, Craig. **Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and Iterative Development**. 3. ed. Upper Saddle River: Prentice Hall, 2004.
- REFACTORING.GURU. **Adapter**. Disponível em: [refactoring.guru/pt-br/design-patterns/adapter](https://refactoring.guru/pt-br/design-patterns/adapter).
- PYTHON SOFTWARE FOUNDATION. **abc — Abstract Base Classes**. Disponível em: [docs.python.org/3/library/abc.html](https://docs.python.org/3/library/abc.html).
- GRUPO 4. **Entrega 02 — Requisitos e regras de negócio (RN01 a RN05)**. [Iniciativas Extras da Entrega 02](https://github.com/UnBArqDsw2026-2-Turma02/2026.2-T02-_G4_ProjetoJogo_Entrega_02/blob/main/docs/Base/1.3.IniciativasExtras.md).
- GRUPO 4. **Entrega 02 — Relatório da SubEquipe 01 (Diagrama de Classes e Diagramas de Estados)**. [Repositório da Entrega 02](https://github.com/UnBArqDsw2026-2-Turma02/2026.2-T02-_G4_ProjetoJogo_Entrega_02/blob/main/docs/Base/Relat%C3%B3rios/1.1.1.SubEquipe_01.md).

**Relação entre fontes e decisões.** Gamma et al. (1994) fundamentam a intenção do padrão, os quatro papéis (Client, Target, Adapter e Adaptee) e a escolha do Adapter de objeto. Larman (2004) relaciona o Adapter aos GRASPs Indireção, Polimorfismo e Variações Protegidas, base da justificativa e das alternativas. O relatório da Entrega 02 é a origem das classes adaptadas, das restrições de categoria e dos Diagramas de Estados revistos nesta entrega. As regras RN01 e RN05 definem o XP do Pomodoro e a evolução do pet. A documentação do módulo `abc` sustenta a implementação do Target como classe abstrata em Python.
