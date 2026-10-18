"""Client: credita XP no PetVirtual a partir de qualquer FonteXP.

Este módulo não importa SessaoPomodoro, ContagemDeAgua nem Habito.
Uma atividade nova exige só um Adapter novo; esta classe não muda.
"""

from enum import Enum

from fonte_xp import FonteXP
from pet_virtual import PetVirtual


class ResultadoCredito(Enum):
    CREDITADO = "XP creditado"
    REGRA_NAO_CUMPRIDA = "regra da atividade ainda não cumprida"
    JA_CREDITADO = "evento já creditado"


class CreditadorXP:
    def __init__(self, pet: PetVirtual):
        self._pet = pet
        self._chavesCreditadas = set()

    def creditar(self, fonte: FonteXP) -> ResultadoCredito:
        if not fonte.podeGerarXP():
            return ResultadoCredito.REGRA_NAO_CUMPRIDA
        chave = fonte.obterChaveCredito()
        if chave in self._chavesCreditadas:
            return ResultadoCredito.JA_CREDITADO
        self._pet.adicionarXP(fonte.obterCategoria(), fonte.obterPontos())
        self._chavesCreditadas.add(chave)
        return ResultadoCredito.CREDITADO
