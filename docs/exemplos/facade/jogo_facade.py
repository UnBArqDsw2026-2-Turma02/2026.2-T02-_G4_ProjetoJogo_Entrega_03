"""Facade independente para o jogo de pet virtual. Python 3.10+.

Os subsistemas são didáticos, síncronos e em memória. Os valores de XP e os
critérios de conquistas do exemplo não definem novas regras do projeto.
"""
from dataclasses import dataclass, field
from enum import Enum


class CategoriaXP(Enum):
    INTELECTUAL = "INTELECTUAL"
    SABEDORIA = "SABEDORIA"
    ZEN = "ZEN"
    ATLETICO = "ATLETICO"
    HIDRATACAO = "HIDRATACAO"


class Evolucao(Enum):
    NEUTRO = "NEUTRO"
    ESTUDIOSO = "ESTUDIOSO"
    LEITOR = "LEITOR"
    ZEN = "ZEN"
    ATLETICO = "ATLETICO"
    HIDRATADO = "HIDRATADO"
    DESMOTIVADO = "DESMOTIVADO"


def validarRecompensa(categoria: CategoriaXP, pontos: int) -> None:
    if not isinstance(categoria, CategoriaXP):
        raise ValueError("A categoria deve ser um valor de CategoriaXP.")
    if type(pontos) is not int or pontos < 0:
        raise ValueError("Os pontos devem ser um inteiro não negativo.")


class PetVirtual:
    def __init__(self):
        self._vetorXP = [0] * len(CategoriaXP)
        self.evolucao = Evolucao.NEUTRO

    @property
    def vetorXP(self) -> tuple[int, ...]:
        return tuple(self._vetorXP)

    def adicionarXP(self, categoria: CategoriaXP, pontos: int) -> None:
        validarRecompensa(categoria, pontos)
        self._vetorXP[list(CategoriaXP).index(categoria)] += pontos

    def determinarEvolucao(self) -> Evolucao:
        maior = max(self._vetorXP)
        if maior == 0:
            return Evolucao.NEUTRO
        # Regra ilustrativa: empate preserva a forma atual.
        if self._vetorXP.count(maior) > 1:
            return self.evolucao
        categoria = list(CategoriaXP)[self._vetorXP.index(maior)]
        formas = {
            CategoriaXP.INTELECTUAL: Evolucao.ESTUDIOSO,
            CategoriaXP.SABEDORIA: Evolucao.LEITOR,
            CategoriaXP.ZEN: Evolucao.ZEN,
            CategoriaXP.ATLETICO: Evolucao.ATLETICO,
            CategoriaXP.HIDRATACAO: Evolucao.HIDRATADO,
        }
        return formas[categoria]

    def verificarEvolucao(self) -> None:
        self.evolucao = self.determinarEvolucao()


@dataclass(frozen=True)
class RegistroConclusao:
    idConclusao: str
    categoria: CategoriaXP
    pontos: int


class HistoricoUsuario:
    def __init__(self):
        self._registros: dict[str, RegistroConclusao] = {}

    @property
    def registros(self) -> tuple[RegistroConclusao, ...]:
        return tuple(self._registros.values())

    def possuiConclusao(self, idConclusao: str) -> bool:
        return idConclusao in self._registros

    def registrarConclusao(self, idConclusao: str, categoria: CategoriaXP,
                          pontos: int) -> None:
        if self.possuiConclusao(idConclusao):
            raise ValueError("Esta conclusão já foi registrada.")
        self._registros[idConclusao] = RegistroConclusao(idConclusao, categoria, pontos)


@dataclass
class Conquista:
    nome: str = "Primeira atividade"
    minimoConclusoes: int = 1
    foiDesbloqueada: bool = field(default=False, init=False)

    def __post_init__(self):
        if type(self.minimoConclusoes) is not int or self.minimoConclusoes < 1:
            raise ValueError("O critério deve exigir ao menos uma conclusão.")

    def validarRequisitoGeral(self, usuario: "Usuario") -> bool:
        # Critério ilustrativo; recebe o usuário, conforme o UML da Entrega 02.
        return len(usuario.historico.registros) >= self.minimoConclusoes

    def desbloquearConquista(self) -> None:
        self.foiDesbloqueada = True


@dataclass
class Usuario:
    idUsuario: str
    pet: PetVirtual = field(default_factory=PetVirtual)
    historico: HistoricoUsuario = field(default_factory=HistoricoUsuario)
    conquistas: list[Conquista] = field(default_factory=lambda: [Conquista()])
    totalAtividadesPrevistas: int = 0

    def calcularTaxaCompletacao(self) -> float:
        # Recorte ilustrativo: conclusões registradas / atividades previstas.
        if self.totalAtividadesPrevistas <= 0:
            return 0.0
        return min(1.0, len(self.historico.registros) / self.totalAtividadesPrevistas)


class SituacaoConclusao(Enum):
    PROCESSADA = "PROCESSADA"
    JA_REGISTRADA = "JA_REGISTRADA"


@dataclass(frozen=True)
class ResultadoConclusao:
    situacao: SituacaoConclusao
    novasConquistas: tuple[str, ...] = ()


class JogoFacade:
    def __init__(self, usuario: Usuario):
        # Todas as referências vêm do mesmo usuário.
        self.usuario = usuario
        self.pet = usuario.pet
        self.historico = usuario.historico
        self.conquistas = usuario.conquistas

    def concluirAtividade(self, idConclusao: str, categoria: CategoriaXP,
                          pontos: int) -> ResultadoConclusao:
        """Processa as consequências de uma atividade já concluída e validada."""
        if not isinstance(idConclusao, str) or not idConclusao.strip():
            raise ValueError("Informe o identificador desta ocorrência concluída.")
        validarRecompensa(categoria, pontos)
        if self.historico.possuiConclusao(idConclusao):
            return ResultadoConclusao(SituacaoConclusao.JA_REGISTRADA)

        self.pet.adicionarXP(categoria, pontos)
        self.pet.verificarEvolucao()
        self.historico.registrarConclusao(idConclusao, categoria, pontos)

        novas = []
        for conquista in self.conquistas:
            if (not conquista.foiDesbloqueada
                    and conquista.validarRequisitoGeral(self.usuario)):
                conquista.desbloquearConquista()
                novas.append(conquista.nome)
        return ResultadoConclusao(SituacaoConclusao.PROCESSADA, tuple(novas))
