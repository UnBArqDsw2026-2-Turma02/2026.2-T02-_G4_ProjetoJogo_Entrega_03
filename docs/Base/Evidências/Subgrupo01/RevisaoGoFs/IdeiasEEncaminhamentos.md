# Síntese de ideias e encaminhamentos entre os subgrupos

**Referência:** análise dos relatórios criacional e comportamental pelo Subgrupo 01.

**Participantes da revisão informados:** Guilherme Negreiros Pereira, Enzo Lopes Ferreira e Gabriel Pereira da Silva.

**Data de organização deste registro:** 19/10/2026.

Este documento organiza as questões e possibilidades extraídas da revisão. Os encaminhamentos são propostas para alinhamento entre equipes, sem atribuir aprovação ou execução conjunta ainda não registrada. A síntese não é uma ata nem uma transcrição de conversa.

## Por que revisar os outros recortes

A especialização de cada integrante em um padrão favoreceu o aprofundamento individual, mas o jogo reúne problemas de construção, organização e comportamento. A leitura dos outros subgrupos ajuda a compreender o papel de cada solução e a identificar decisões que não podem ser resolvidas de modo independente numa implementação comum.

## Questões organizadas pela revisão

| Tema | Base identificada nos materiais | Ideia para alinhamento | Situação neste registro |
|---|---|---|---|
| XP do Pomodoro | A fórmula Strategy exemplifica 60 XP em 25 minutos concluídos; Factory Method documenta 50 XP por ciclo. | Manter uma tabela compartilhada de entradas e resultados de referência. | Divergência identificada; regra comum a confirmar com os responsáveis. |
| Concessão de recompensa | Factory Method, Observer e Facade possuem caminhos que podem chegar ao crédito de XP. | Eleger um único responsável pelo efeito e identificar cada ocorrência concluída. | Proposta de integração; exemplos continuam independentes. |
| Estado do pet | Há fases de vida, afinidade por categoria, XP total e vetor por categoria. | Elaborar um pequeno glossário do domínio e distinguir os conceitos. | Diferenças identificadas; consolidação sugerida. |
| Cálculo e bônus | Strategy troca fórmulas; Decorator acrescenta camadas ao cálculo. | Definir primeiro o cálculo base e depois os bônus aplicáveis, com uma única aplicação de cada regra. | Possibilidade arquitetural, sem integração executada nesta revisão. |
| Completude da documentação | Existem exemplos demonstrados e campos ainda a preencher nas versões recebidas. | Vincular cada afirmação ao modelo, ao código e à evidência disponível. | Recomendação de rastreabilidade. |
| Recuperação de estado | Memento é anunciado, mas a seção específica ainda não detalha o funcionamento. | Definir a relação entre snapshots, histórico e créditos antes de integrar restauração. | Questão para detalhamento futuro. |

## Cenários sugeridos para uma futura verificação comum

Estes cenários são propostas de verificação, não resultados de testes realizados pelo subgrupo nesta revisão.

| Cenário proposto | O que permitiria verificar |
|---|---|
| Sessão concluída com 25 minutos de foco | Consistência entre regra oficial e fórmulas de XP dos exemplos. |
| Reenvio do mesmo identificador de conclusão | Uma única concessão de XP, mesmo havendo fachada e observadores. |
| Atividade com um e com dois bônus | Aplicação das camadas uma única vez sobre o cálculo base. |
| Pausa, retomada e conclusão do Pomodoro | Ações permitidas em cada estado e ausência de recompensa antecipada. |
| Ganho de XP superior a vários limiares | Regra de progressão de fases claramente definida. |
| Dois usuários com atividades simultâneas | Separação dos objetos, inscrições e históricos por usuário. |
| Construção de dois mascotes com configurações diferentes | Independência dos produtos e integridade do inventário. |

## Distinções que orientaram a análise

| Padrão | Pergunta principal no projeto |
|---|---|
| Builder | Como montar um mascote configurável por etapas? |
| Factory Method | Qual produto de atividade o criador deve instanciar? |
| Adapter | Como apresentar fontes distintas por um contrato comum? |
| Decorator | Como acrescentar bônus combináveis ao cálculo? |
| Facade | Como oferecer uma entrada simples para coordenar subsistemas? |
| Observer | Como comunicar uma ocorrência aos componentes interessados? |
| State | Quais ações e transições dependem do estado atual? |
| Strategy | Qual algoritmo de pontuação deve ser utilizado? |
| Memento | Qual estado deve ser preservado e restaurado? |

## Encaminhamento geral

As fichas foram organizadas para apoiar o diálogo técnico entre as equipes e tornar os pontos de revisão consultáveis. Uma implementação comum exigirá confirmar contratos e regras e então verificar o fluxo completo. Os arquivos atuais registram a análise dos materiais e as propostas resultantes, sem presumir que essas etapas posteriores já ocorreram.

[Voltar aos registros da revisão](README.md).
