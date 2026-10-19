"""Adaptee: Habito, como modelado na Entrega 02 (recorte: sem dias ativos e congelamento).

Regra própria: só há XP no dia em que verificarConclusaoAoDia(data) é verdadeiro.
A categoria é a do próprio hábito (associação pertenceA).
Esta classe não conhece PetVirtual, CreditadorXP nem FonteXP.
"""

from datetime import date

from categoria_xp import CategoriaXP


class Habito:
    XP_POR_CONCLUSAO = 15

    def __init__(self, idHabito: str, nomeHabito: str, categoria: CategoriaXP):
        self._idHabito = idHabito
        self._nomeHabito = nomeHabito
        self._categoria = categoria
        self._streakAtual = 0
        self._streakMaximo = 0
        self._dataUltimaCompletacao = None
        self._datasConcluidas = set()

    # Getters somente leitura. O diagrama de classes omite getters por convenção.
    @property
    def idHabito(self) -> str:
        return self._idHabito

    @property
    def nomeHabito(self) -> str:
        return self._nomeHabito

    @property
    def categoria(self) -> CategoriaXP:
        return self._categoria

    def marcarConcluido(self, data: date | None = None) -> None:
        # O parâmetro data permite simular dias diferentes; por padrão, hoje.
        data = data or date.today()
        if data in self._datasConcluidas:
            return
        self._datasConcluidas.add(data)
        self._dataUltimaCompletacao = data
        self._streakAtual += 1
        self._streakMaximo = max(self._streakMaximo, self._streakAtual)

    def verificarConclusaoAoDia(self, data: date) -> bool:
        return data in self._datasConcluidas

    def calcularXPGanho(self) -> int:
        return self.XP_POR_CONCLUSAO
