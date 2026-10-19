#### Metodologia do Foco_02

##### Objetivo e delimitação

Esta seção trata da aplicação independente do padrão GoF estrutural Facade ao fluxo de conclusão de atividades do jogo. O objetivo é oferecer ao cliente uma operação simples para coordenar experiência, evolução do pet, histórico e conquistas. A demonstração implementada não depende dos padrões Adapter e Decorator dos demais integrantes.

O responsável pela seção é Guilherme Negreiros Pereira, conforme a divisão registrada na página do Subgrupo 01. A organização do GitHub Pages permanece uma contribuição adicional e não substitui a modelagem, a implementação e a execução do Facade.

##### Processo de elaboração

A preparação foi organizada em etapas, separando os artefatos já elaborados das atividades ainda previstas:

| Etapa | Procedimento | Resultado e situação |
|---|---|---|
| Compreensão do domínio | Consulta aos relatórios das Entregas 01 e 02 e ao roteiro do Subgrupo 01 da Entrega 03. | Identificação do fluxo de recompensas e das classes existentes. |
| Fundamentação | Consulta à aula de Milene Serrano e à seção 5.10 da dissertação de Figueiredo. | Caracterização do Facade como interface simplificada para subsistemas. |
| Delimitação | Escolha de uma demonstração independente, recebendo dados de uma atividade já concluída. | Recorte definido por Guilherme. |
| Modelagem estática | Distribuição das responsabilidades entre cliente, fachada e subsistemas. | Diagrama de classes proposto nesta seção. |
| Modelagem dinâmica | Ordenação das chamadas e tratamento do reenvio da mesma conclusão. | Diagrama de sequência proposto nesta seção. |
| Revisão da modelagem | Análise e ajustes dos diagramas e das responsabilidades das classes por Guilherme. | Modelo revisado por Guilherme. |
| Implementação | Implementar o recorte independente em Python e verificar os cenários. | Código e demonstração executados; sete testes passaram. |
| Evidências | Registrar a apresentação e a execução, relacionando vídeo, modelo, código e participação. | [Vídeo publicado](https://youtu.be/QQM7oWCMstk) e vinculado ao relatório, às evidências e à participação. |

#### GoF Estrutural

##### Contexto (Problema)

O projeto combina pet virtual, Pomodoro e acompanhamento de hábitos saudáveis. Na Entrega 01, as ações de produtividade e autocuidado são relacionadas ao estado e ao desenvolvimento do pet [3]. Na Entrega 02, essa ideia aparece em classes como `PetVirtual`, `Usuario`, `HistoricoUsuario` e `Conquista`, além das atividades que calculam experiência [4].

Quando uma atividade é concluída, o jogo pode precisar adicionar XP à categoria correspondente, verificar a evolução do pet, registrar a conclusão e avaliar conquistas. Se cada cliente executar diretamente essa sequência, precisará conhecer as interfaces e a ordem das operações de vários objetos. A repetição pode provocar diferenças entre os fluxos: uma tela pode atualizar XP e esquecer o histórico, por exemplo.

Esse é um risco identificado na análise da modelagem, e não uma afirmação de que essas falhas já ocorreram em um jogo implementado.

##### Padrão selecionado e justificativa

A proposta é criar `JogoFacade`, com a operação pública `concluirAtividade(idConclusao, categoria, pontos)`. O cliente fornece os dados da conclusão, e a fachada coordena os objetos envolvidos.

Na aula de Milene Serrano, os padrões estruturais são associados à redução de acoplamento, e Facade é apresentado como uma interface simplificada de acesso a várias interfaces do sistema [1, páginas 6, 8 e 61 do PDF]. Figueiredo discute, em jogos, a utilização de uma fachada para reduzir a dependência entre a camada de interação e os componentes internos [2, seção 5.10]. Neste projeto, o princípio é aplicado ao fluxo de recompensas, em vez do exemplo gráfico utilizado pelo autor.

A escolha se sustenta em três aspectos:

- **Simplificação do cliente:** a solicitação do fluxo fica concentrada em uma operação, sem exigir que cada tela repita a coordenação dos subsistemas.
- **Localização da coordenação:** ajustes na sequência podem ser feitos na fachada, preservando uma entrada estável para o cliente.
- **Preservação das responsabilidades:** a fachada solicita ações; o pet continua responsável pela evolução, e as conquistas continuam responsáveis pelos próprios critérios.

A redução de acoplamento se refere ao cliente em relação aos subsistemas. A fachada passa a conhecê-los, e sua interface ainda pode precisar mudar caso o fluxo de negócio mude. Criar uma classe com nome Facade, sem oferecer simplificação e delegação, não caracteriza adequadamente a aplicação do padrão.

##### Alternativas consideradas

| Alternativa | Avaliação para este problema |
|---|---|
| Chamadas diretas em cada tela | Pode bastar para uma única demonstração curta, mas repete a coordenação quando existem vários clientes. |
| Colocar todo o fluxo em `PetVirtual` | Mistura a evolução do pet com registro de atividades e gestão de conquistas. |
| Colocar todo o fluxo em `Usuario` | Aumenta as responsabilidades de uma classe que já representa perfil e contexto do usuário. |
| Adapter | Resolve compatibilidade entre contratos; não é o problema central da coordenação deste recorte. |
| Decorator | Permite compor comportamentos adicionais; não é necessário para organizar as chamadas aos subsistemas. |
| Facade | Oferece uma entrada simples para a operação composta e mantém o comportamento nos responsáveis. |

##### Escopo, premissas e decisões

A operação representa o processamento das consequências de uma conclusão. Ela **não encerra o cronômetro nem marca o hábito como cumprido**: recebe uma ocorrência já concluída, com categoria e XP calculados e validados pela atividade. Essa premissa permite estudar Facade sem incorporar outros padrões.

O contrato de entrada inclui `idConclusao`, identificador de uma ocorrência específica. O mesmo hábito em dias diferentes tem conclusões diferentes. Categoria e pontos respeitam as restrições da Entrega 02: água usa HIDRATACAO; Pomodoro usa INTELECTUAL ou SABEDORIA. A fachada não estabelece as fórmulas de XP.

A fachada mantém referências ao usuário, ao pet, ao histórico e às conquistas desse mesmo usuário. O objeto `Usuario` é contexto para a avaliação de conquistas, preservando a operação `validarRequisitoGeral(usuario)` do modelo anterior. As referências são recebidas na montagem do exemplo; não se propõe que a fachada crie ou controle o ciclo de vida desses objetos.

No histórico são propostas `possuiConclusao()` e `registrarConclusao()`. Essas operações não constam no diagrama anterior e devem ser incorporadas de modo explícito na implementação desta demonstração. O registro mínimo contém identificador, categoria e pontos; métricas específicas como tempo de foco e volume de água exigirão ampliar o contrato se forem utilizadas por uma conquista.

O histórico é atualizado antes da avaliação das conquistas para que o contexto possa refletir a conclusão atual. A implementação deve garantir acesso aos mesmos objetos do usuário. A verificação de conclusão repetida é uma decisão complementar do exemplo, não uma exigência do padrão Facade.

##### Modelagem (Notação UML)

###### Diagrama de classes

<div class="state-diagram">
  <img src="Base/Diagramas/Facade/classes.png" alt="Figura 1 — Diagrama de classes proposto para o Facade independente" width="1640" height="1060" loading="lazy" tabindex="0" role="button" aria-label="Ampliar diagrama de classes do Facade">
</div>

**Figura 1 — Facade aplicado ao processamento de uma atividade concluída.** Fonte: elaborado e revisado por Guilherme Negreiros Pereira, com base nas classes da Entrega 02 e na estrutura apresentada em [1] e [2]. A IA generativa foi utilizada como ferramenta de apoio à elaboração e à revisão.

O diagrama é um recorte: omite atributos e operações sem participação no fluxo. `CategoriaXP` e `Evolucao` são os tipos enumerados já existentes. `ResultadoConclusao` é um objeto de retorno proposto com a situação PROCESSADA ou JA_REGISTRADA e as novas conquistas. O tipo é referido na assinatura, sem uma caixa própria para manter o foco nos participantes do padrão.

| Participante do padrão | Elemento do projeto | Responsabilidade |
|---|---|---|
| Cliente | `ClienteDemo` | Simular uma tela solicitando o processamento pela fachada. |
| Fachada | `JogoFacade` | Coordenar a operação sem concentrar as fórmulas e critérios. |
| Subsistema | `PetVirtual` | Adicionar XP e verificar evolução. |
| Subsistema | `HistoricoUsuario` | Consultar e registrar ocorrências concluídas. |
| Subsistema | `Conquista` | Avaliar o usuário e desbloquear a conquista. |
| Contexto | `Usuario` | Fornecer o contexto de avaliação das conquistas. |

**Legenda UML:** `+` indica visibilidade pública; `-`, privada; linha contínua com seta indica associação navegável; linha tracejada com seta indica dependência; `1` e `0..*` indicam multiplicidades. Os rótulos `client` e `facade` identificam papéis do padrão. As associações não representam composição nem exigem herança. O desenho de `Conquista` com dependência de `Usuario` expressa o parâmetro utilizado em sua operação de avaliação.

<details>
<summary>Ver código Mermaid — diagrama de classes</summary>

```mermaid
classDiagram
    direction TB
    class ClienteDemo {
        <<client>>
        +executar()
    }
    class JogoFacade {
        <<facade>>
        +concluirAtividade(idConclusao: String, categoria: CategoriaXP, pontos: int) ResultadoConclusao
    }
    class Usuario {
        +calcularTaxaCompletacao() double
    }
    class PetVirtual {
        -vetorXP: int[5]
        +adicionarXP(categoria: CategoriaXP, pontos: int) void
        +verificarEvolucao() void
        +determinarEvolucao() Evolucao
    }
    class HistoricoUsuario {
        +possuiConclusao(idConclusao: String) boolean
        +registrarConclusao(idConclusao: String, categoria: CategoriaXP, pontos: int) void
    }
    class Conquista {
        -foiDesbloqueada: boolean
        +validarRequisitoGeral(usuario: Usuario) boolean
        +desbloquearConquista() void
    }
    ClienteDemo ..> JogoFacade : solicita conclusao
    JogoFacade "1" --> "1" Usuario : usuario
    JogoFacade "1" --> "1" PetVirtual : pet
    JogoFacade "1" --> "1" HistoricoUsuario : historico
    JogoFacade "1" --> "0..*" Conquista : conquistas
    Conquista ..> Usuario : avalia contexto
    note for JogoFacade "Precondicao: atividade concluida e XP calculado/validado.\nObjetos pertencem ao mesmo usuario."
    note for HistoricoUsuario "Operacoes novas propostas nesta modelagem."
```

</details>

<a href="Base/Diagramas/Facade/classes.mmd" target="_blank" rel="noopener">Abrir fonte Mermaid do diagrama de classes</a> · <a href="Base/Diagramas/Facade/classes.svg" target="_blank" rel="noopener">Abrir imagem vetorial</a>.

###### Diagrama de sequência

<div class="state-diagram">
  <img src="Base/Diagramas/Facade/sequencia.png" alt="Figura 2 — Diagrama de sequência do Facade" width="1640" height="1250" loading="lazy" tabindex="0" role="button" aria-label="Ampliar diagrama de sequência do Facade">
</div>

<details>
<summary>Ver código Mermaid — diagrama de sequência</summary>

```mermaid
sequenceDiagram
    autonumber
    actor Cliente as Cliente de demonstracao
    participant F as JogoFacade
    participant P as PetVirtual
    participant H as HistoricoUsuario
    participant C as Conquista
    Note over Cliente,F: Atividade ja concluida; categoria e XP ja calculados e validados
    Cliente->>F: concluirAtividade(idConclusao, categoria, pontos)
    F->>H: possuiConclusao(idConclusao)
    H-->>F: registrada
    alt Conclusao ja registrada
        F-->>Cliente: ResultadoConclusao(JA_REGISTRADA)
    else Nova conclusao
        F->>P: adicionarXP(categoria, pontos)
        F->>P: verificarEvolucao()
        F->>H: registrarConclusao(idConclusao, categoria, pontos)
        loop Para cada conquista ainda bloqueada
            F->>C: validarRequisitoGeral(usuario)
            C-->>F: criterioAtendido
            opt Criterio atendido
                F->>C: desbloquearConquista()
            end
        end
        F-->>Cliente: ResultadoConclusao(PROCESSADA, novasConquistas)
    end
```

</details>

**Figura 2 — Sequência proposta para conclusão nova e reenvio.** Fonte: elaborado e revisado por Guilherme Negreiros Pereira, a partir do diagrama de classes, com a IA generativa como ferramenta de apoio à elaboração e à revisão. <a href="Base/Diagramas/Facade/sequencia.mmd" target="_blank" rel="noopener">Abrir fonte Mermaid</a> · <a href="Base/Diagramas/Facade/sequencia.svg" target="_blank" rel="noopener">Abrir imagem vetorial</a>.

**Leitura do fluxo:** a fachada consulta o histórico; uma ocorrência já registrada retorna sem nova recompensa. Para uma ocorrência nova, solicita XP e evolução ao pet, registra o evento e percorre as conquistas ainda bloqueadas. Cada conquista avalia seu critério com o usuário e é desbloqueada apenas se ele for atendido. O retorno informa o processamento e as novas conquistas.

A ordem é proposta para o caminho de sucesso de uma demonstração síncrona. O modelo não promete transações ou recuperação automática de falhas entre etapas. Esses mecanismos exigiriam decisões adicionais de persistência e consistência.

##### Implementação (Código & Vídeo com Padrão em Execução)

A implementação em Python corresponde ao recorte independente do UML. O exemplo usa os subsistemas `PetVirtual`, `HistoricoUsuario` e `Conquista`, com o contexto de `Usuario`. A fachada recebe o usuário na construção e mantém referências aos mesmos objetos. Não depende dos códigos de Adapter ou Decorator.

**Arquivos:**

- <a href="exemplos/facade/jogo_facade.py" target="_blank" rel="noopener">Código da fachada e dos participantes</a>.
- <a href="exemplos/facade/demo.py" target="_blank" rel="noopener">Cliente de demonstração</a>.
- <a href="exemplos/facade/test_jogo_facade.py" target="_blank" rel="noopener">Testes automatizados</a>.

###### Montagem dos objetos

```python
usuario = Usuario("usuario-demo")
jogo = JogoFacade(usuario)
```

`Usuario` reúne seu pet, histórico e conquistas. Cada instância recebe objetos próprios para evitar compartilhar dados entre usuários. `JogoFacade` mantém referências a esses objetos; sua criação não transfere a responsabilidade das regras de negócio para a fachada.

###### Entrada, validação e repetição

```python
resultado = jogo.concluirAtividade(
    "pomodoro-001", CategoriaXP.INTELECTUAL, 50
)
```

O identificador representa uma ocorrência já concluída. A fachada verifica se ele é uma string não vazia e valida categoria e pontos inteiros não negativos antes de alterar o estado. Em seguida, consulta `historico.possuiConclusao()`. Se o evento já existe, retorna `ResultadoConclusao` com situação `JA_REGISTRADA`, sem repetir os efeitos. A atividade de origem continua responsável por validar sua conclusão e a categoria permitida.

###### Delegação aos subsistemas

```python
self.pet.adicionarXP(categoria, pontos)
self.pet.verificarEvolucao()
self.historico.registrarConclusao(idConclusao, categoria, pontos)
```

Essas chamadas seguem o diagrama de sequência. O pet administra o vetor de cinco categorias e calcula sua forma. O histórico armazena uma ocorrência imutável com identificador, categoria e pontos. A fachada organiza a sequência sem implementar a fórmula da evolução.

###### Avaliação das conquistas

```python
for conquista in self.conquistas:
    if (not conquista.foiDesbloqueada
            and conquista.validarRequisitoGeral(self.usuario)):
        conquista.desbloquearConquista()
        novas.append(conquista.nome)
```

A avaliação recebe o usuário, preservando a assinatura da Entrega 02. O histórico já contém a conclusão atual quando o critério é verificado. Somente conquistas ainda bloqueadas são avaliadas; o resultado contém apenas os novos desbloqueios.

###### Cliente e resultado

`ClienteDemo` monta os objetos, exibe o estado inicial e solicita cada processamento pela fachada. O cliente consulta os objetos para mostrar o resultado, mas não executa diretamente as alterações dos subsistemas. `ResultadoConclusao` informa PROCESSADA ou JA_REGISTRADA e os nomes das novas conquistas.

###### Regras ilustrativas e limites

Os valores 50, 20 e 40 XP são dados da demonstração, não uma fórmula de cálculo. As conquistas “Primeira atividade” e “Duas atividades” exigem uma e duas conclusões, respectivamente. A evolução escolhe a categoria com maior XP, preserva a forma atual em empate e mantém NEUTRO quando o vetor está zerado. O estado DESMOTIVADO não é acionado neste recorte, pois depende de critérios adicionais. A taxa de completação ilustrativa divide as conclusões pelas atividades previstas e não participa da decisão de evolução deste exemplo.

Os dados ficam em memória e são reiniciados a cada execução. Não há persistência, concorrência, transações ou recuperação de falhas entre etapas.

###### Execução e verificação

Na raiz do repositório, com Python 3.10 ou superior:

```sh
python docs/exemplos/facade/demo.py
python -m unittest discover -s docs/exemplos/facade -p "test_*.py" -v
```

No ambiente local desta preparação, a execução foi verificada com o Python disponibilizado pelo aplicativo. A demonstração executou os quatro cenários abaixo, e os sete testes passaram em 17/10/2026. Os testes verificam o fluxo completo, reenvio inclusive por outra instância de fachada, nova ocorrência, entradas inválidas sem efeitos, isolamento de usuários, formas por categoria e empate.

| Cenário demonstrado | Resultado observado |
|---|---|
| Pomodoro, 50 XP intelectual | Pet ESTUDIOSO, um registro e primeira conquista desbloqueada. |
| Reenvio do Pomodoro | JA_REGISTRADA; XP, histórico e conquistas preservados. |
| Água, 20 XP de hidratação | Dois registros e segunda conquista desbloqueada; pet continua ESTUDIOSO. |
| Nova ocorrência, 40 XP de hidratação | Hidratação totaliza 60 XP; pet HIDRATADO, três registros e nenhum desbloqueio repetido. |

###### Testes automatizados do Facade

Os testes complementam a demonstração do padrão e estão no arquivo `test_jogo_facade.py`, utilizando o módulo `unittest` da biblioteca padrão do Python. O vídeo apresenta o Facade e sua demonstração em execução; a verificação automatizada está documentada separadamente nesta seção.

O método `setUp()` prepara um usuário com pet, histórico e duas conquistas, além da fachada correspondente, antes de cada teste. Assim, cada caso parte de um estado próprio e não depende das alterações realizadas pelos demais.

| Verificação | Procedimento | Resultado esperado |
|---|---|---|
| Fluxo completo e histórico atualizado | Processar uma conclusão com 50 XP intelectual. | Retornar PROCESSADA, adicionar XP, alterar a forma para ESTUDIOSO, registrar uma conclusão e desbloquear apenas a primeira conquista. A avaliação considera o histórico já atualizado. |
| Reenvio por outra fachada | Processar a mesma ocorrência novamente usando outra instância de `JogoFacade` para o mesmo usuário. | Retornar JA_REGISTRADA, mantendo os pontos e o único registro, sem novos desbloqueios. |
| Nova ocorrência e outra categoria predominante | Após o Pomodoro, processar uma nova conclusão com 60 XP de hidratação. | Preservar o XP intelectual, alterar a forma para HIDRATADO, registrar a segunda ocorrência e desbloquear apenas a segunda conquista. |
| Entradas inválidas | Informar identificador vazio, apenas espaços ou nulo; categoria fora de `CategoriaXP`; pontos negativos, fracionários ou booleanos. | Lançar `ValueError` antes de alterar XP, histórico ou conquistas. |
| Isolamento entre usuários | Processar uma conclusão para um usuário e consultar outro usuário recém-instanciado. | O segundo usuário permanece com XP zerado, histórico vazio e conquista bloqueada. |
| Evolução por categoria | Processar separadamente uma conclusão para cada uma das cinco categorias. | Obter ESTUDIOSO, LEITOR, ZEN, ATLETICO ou HIDRATADO, conforme a categoria predominante. |
| Empate de experiência | Conceder 50 XP intelectual e, depois, 50 XP ZEN. | Preservar a forma ESTUDIOSO, conforme a regra ilustrativa de empate adotada no exemplo. |

Os casos de entrada inválida e evolução por categoria utilizam `subTest()` para verificar várias entradas dentro de um mesmo método. O total de **sete testes** corresponde aos sete métodos da classe `TestJogoFacade`.

Para reproduzir a verificação, executar na raiz do repositório:

```powershell
python -m unittest discover -s .\docs\exemplos\facade -p "test_*.py" -v
```

**Resultado registrado:** os sete testes passaram na execução de 17/10/2026, com o resumo `Ran 7 tests` seguido de `OK`. O tempo de execução pode variar entre ambientes.

**Código dos testes:** [versão permanente no repositório](https://github.com/UnBArqDsw2026-2-Turma02/2026.2-T02-_G4_ProjetoJogo_Entrega_03/blob/74c0200c9c1470deffa12de092975adb6ee5a59a/docs/exemplos/facade/test_jogo_facade.py).

Essas verificações cobrem o comportamento do recorte independente em memória. Não validam persistência, concorrência, recuperação de falhas entre etapas ou integração com os outros padrões do subgrupo.

###### Vídeo do padrão em execução

<div class="evidence-slot"><strong>Vídeo do padrão em execução</strong>
<p>Apresentação de Guilherme Negreiros Pereira sobre o Facade aplicado ao fluxo de conclusão de atividades do jogo, com a explicação do padrão e a demonstração do código em execução.</p>
<div style="position:relative;width:100%;max-width:860px;aspect-ratio:16/9;margin:0.5rem 0;">
  <iframe src="https://www.youtube.com/embed/QQM7oWCMstk" title="Padrão Facade — conclusão de atividades do PetVirtual — Guilherme Negreiros Pereira" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe>
</div>
<p><a href="https://youtu.be/QQM7oWCMstk" target="_blank" rel="noopener">▶ Abrir no YouTube</a></p></div>

**Links permanentes do código:** [Implementação](https://github.com/UnBArqDsw2026-2-Turma02/2026.2-T02-_G4_ProjetoJogo_Entrega_03/blob/7e8cd5779f12df89b970835819eb5c35f9cf3ea2/docs/exemplos/facade/jogo_facade.py) · [Demonstração](https://github.com/UnBArqDsw2026-2-Turma02/2026.2-T02-_G4_ProjetoJogo_Entrega_03/blob/bb84e13a20ecffd8a1ef04dd083f0c045c4250ec/docs/exemplos/facade/demo.py) · [Testes](https://github.com/UnBArqDsw2026-2-Turma02/2026.2-T02-_G4_ProjetoJogo_Entrega_03/blob/74c0200c9c1470deffa12de092975adb6ee5a59a/docs/exemplos/facade/test_jogo_facade.py). O registro da execução local está na [página de Evidências](/Base/Evidências/1.1.1.SubEquipe_01.md#execução-local-do-facade).

##### Rastreabilidade das decisões

| Origem | Decisão nesta proposta | Elemento do modelo | Situação |
|---|---|---|---|
| Entrega 01: atividades relacionadas ao desenvolvimento do pet [3] | Processar consequências da conclusão | Entrada da fachada e relação com pet | Modelado |
| Entrega 02: XP por categoria e operações de evolução [4] | Delegar XP e evolução ao pet | `PetVirtual` | Modelado, implementado e verificado · [Execução em vídeo](https://youtu.be/QQM7oWCMstk) |
| Entrega 02: histórico e conquistas [4] | Registrar ocorrência e avaliar o usuário | `HistoricoUsuario`, `Conquista`, `Usuario` | Implementado, com avaliação após o registro · [Vídeo](https://youtu.be/QQM7oWCMstk) |
| Aula e dissertação: simplificação de acesso [1][2] | Uma operação pública para coordenar subsistemas | `JogoFacade` e `ClienteDemo` | Modelado e implementado · [Vídeo](https://youtu.be/QQM7oWCMstk) |
| Decisão local da demonstração | Evitar reprocessar a mesma ocorrência | `possuiConclusao()` | Implementado e verificado · [Vídeo](https://youtu.be/QQM7oWCMstk) |
| Roteiro do FOCO_02 [5] | Relacionar modelo, código, vídeo e autoria | Relatório, Evidências e Participações | Modelos, código, commits e [vídeo publicado](https://youtu.be/QQM7oWCMstk) vinculados |

##### Referências utilizadas por Guilherme — Facade

1. SERRANO, Milene. **Arquitetura e Desenho de Software — Aula GoFs Estruturais**. Material da disciplina. Páginas 6, 8 e 61 do PDF. <a href="Base/Referencias/Aula_GoFs_Estruturais_Profa_Milene.pdf" target="_blank" rel="noopener">Consultar material</a>.
2. FIGUEIREDO, Roberto Tenorio. **Padrões de Projeto GoF aplicados ao Desenvolvimento de Jogos Eletrônicos**. Dissertação de mestrado, Universidade Federal de Pernambuco, 2014. Seção 5.10, páginas impressas 68–71 (páginas 70–73 do PDF). <a href="Base/Referencias/Dissertacao_Roberto_Tenorio_Figueiredo.pdf" target="_blank" rel="noopener">Consultar dissertação</a> · [Repositório UFPE](https://repositorio.ufpe.br/handle/123456789/11981).
3. EQUIPE G4. **Entrega 01 — Relatório da SubEquipe 03**. Contexto do pet virtual, produtividade e hábitos. [Consultar relatório](https://unbarqdsw2026-2-turma02.github.io/2026.2-T02-_G4_ProjetoJogo_Entrega_01/#/Base/Relat%C3%B3rios/1.1.3.SubEquipe_03).
4. EQUIPE G4. **Entrega 02 — Relatório da SubEquipe 01**. Modelagem estática e dinâmica. [Consultar relatório](https://unbarqdsw2026-2-turma02.github.io/2026.2-T02-_G4_ProjetoJogo_Entrega_02/#/Base/Relat%C3%B3rios/1.1.1.SubEquipe_01).
5. EQUIPE G4. **Entrega 03 — Subgrupo 01, FOCO_02**. Roteiro do relatório, responsáveis e entregáveis. [Consultar página do subgrupo](/Base/Relatórios/1.1.1.SubEquipe_01.md).
