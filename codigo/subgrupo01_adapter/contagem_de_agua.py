"""Adaptee: ContagemDeAgua, como modelada na Entrega 02.

Regra própria: só há XP quando validarMetaDiaria() é verdadeiro.
A RN01 prevê XP a cada registro de 250 ml; aqui o XP sai uma vez, ao bater a meta.
A divergência está justificada no relatório (item "Divergência na água", em "Escopo, premissas e decisões").
A categoria é sempre HIDRATACAO (restrição {readOnly} do Diagrama de Classes).
Esta classe não conhece PetVirtual, CreditadorXP nem FonteXP.
"""

from datetime import date

from categoria_xp import CategoriaXP


class ContagemDeAgua:
    CATEGORIA = CategoriaXP.HIDRATACAO
    XP_META_DIARIA = 20

    def __init__(self, idContagemDeAgua: str, limiteDiario: int = 2000, dataRegistro: date | None = None):
        self._idContagemDeAgua = idContagemDeAgua
        self._volumeML = 0
        self._limiteDiario = limiteDiario  # meta diária em ml
        self._dataRegistro = dataRegistro or date.today()

    # Getters somente leitura. O diagrama de classes omite getters por convenção.
    @property
    def idContagemDeAgua(self) -> str:
        return self._idContagemDeAgua

    @property
    def dataRegistro(self) -> date:
        return self._dataRegistro

    def adicionarVolume(self, ml: int) -> None:
        if ml <= 0:
            raise ValueError("ml deve ser maior que zero")
        self._volumeML += ml

    def validarMetaDiaria(self) -> bool:
        return self._volumeML >= self._limiteDiario

    def obterProgressoPercentual(self) -> float:
        return min(100.0, 100 * self._volumeML / self._limiteDiario)

    def calcularXPGanho(self) -> int:
        return self.XP_META_DIARIA

    def resetarDiario(self, novaData: date | None = None) -> None:
        self._volumeML = 0
        self._dataRegistro = novaData or date.today()
