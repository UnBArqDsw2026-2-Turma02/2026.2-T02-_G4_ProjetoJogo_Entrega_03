"""Adapter: traduz Habito para a interface FonteXP."""

from datetime import date

from categoria_xp import CategoriaXP
from fonte_xp import FonteXP
from habito import Habito


class HabitoAdapter(FonteXP):
    def __init__(self, habito: Habito, data: date | None = None):
        self._habito = habito
        # FonteXP não recebe parâmetros; o Adapter guarda o dia avaliado
        # que verificarConclusaoAoDia(data) exige.
        self._data = data or date.today()

    def podeGerarXP(self) -> bool:
        return self._habito.verificarConclusaoAoDia(self._data)

    def obterCategoria(self) -> CategoriaXP:
        return self._habito.categoria  # categoria do próprio hábito

    def obterPontos(self) -> int:
        return self._habito.calcularXPGanho()

    def obterChaveCredito(self) -> str:
        return f"habito:{self._habito.idHabito}:{self._data.isoformat()}"  # uma vez por hábito por dia
