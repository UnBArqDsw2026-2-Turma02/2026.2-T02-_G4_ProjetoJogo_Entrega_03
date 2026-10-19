"""Adaptee: SessaoPomodoro, como modelada na Entrega 02.

Regra própria: só há XP depois de finalizarSessao(), no estado CONCLUIDA.
A categoria é escolhida na criação e fica restrita a INTELECTUAL ou SABEDORIA.
Esta classe não conhece PetVirtual, CreditadorXP nem FonteXP.
"""

from datetime import datetime

from categoria_xp import CategoriaXP

CATEGORIAS_PERMITIDAS = (CategoriaXP.INTELECTUAL, CategoriaXP.SABEDORIA)


class SessaoPomodoro:
    # RN01 (Entrega 02): sessão de 25 min concluída concede +50 XP, ou seja, 2 XP por minuto de foco.
    XP_POR_MINUTO_DE_FOCO = 2

    def __init__(self, idSessao: str, duracao: int, categoria: CategoriaXP):
        # Restrição de associação do Diagrama de Classes (Entrega 02).
        if categoria not in CATEGORIAS_PERMITIDAS:
            raise ValueError("SessaoPomodoro aceita somente INTELECTUAL ou SABEDORIA")
        self._idSessao = idSessao
        self._duracao = duracao  # minutos de foco planejados
        self._tempoDecorrido = 0  # minutos de foco efetivamente cumpridos
        self._statusSessao = "CONFIGURADA"
        self._categoria = categoria
        self._dataInicio = None
        self._dataFim = None

    # Getters somente leitura. O diagrama de classes omite getters por convenção.
    @property
    def idSessao(self) -> str:
        return self._idSessao

    @property
    def statusSessao(self) -> str:
        return self._statusSessao

    @property
    def categoria(self) -> CategoriaXP:
        return self._categoria

    def iniciarSessao(self) -> None:
        self._exigirStatus("CONFIGURADA")
        self._statusSessao = "EM_EXECUCAO"
        self._dataInicio = datetime.now()

    def pausarSessao(self) -> None:
        self._exigirStatus("EM_EXECUCAO")
        self._statusSessao = "PAUSADA"

    def retomaSessao(self) -> None:
        self._exigirStatus("PAUSADA")
        self._statusSessao = "EM_EXECUCAO"

    def registrarTempoDeFoco(self, minutos: int) -> None:
        """Simula o temporizador do estado FOCO (do / atualizar tempoDecorrido)."""
        self._exigirStatus("EM_EXECUCAO")
        self._tempoDecorrido = min(self._duracao, self._tempoDecorrido + minutos)

    def finalizarSessao(self) -> None:
        self._exigirStatus("EM_EXECUCAO")
        self._statusSessao = "CONCLUIDA"
        self._dataFim = datetime.now()

    def calcularXPGanho(self) -> int:
        # O XP considera somente o tempo de foco cumprido (decisões da SessaoPomodoro, Entrega 02).
        return self._tempoDecorrido * self.XP_POR_MINUTO_DE_FOCO

    def _exigirStatus(self, esperado: str) -> None:
        if self._statusSessao != esperado:
            raise RuntimeError(f"operação exige status {esperado}; status atual: {self._statusSessao}")
