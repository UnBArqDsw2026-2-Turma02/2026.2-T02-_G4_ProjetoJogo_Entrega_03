"""Adapter: traduz ContagemDeAgua para a interface FonteXP."""

from categoria_xp import CategoriaXP
from contagem_de_agua import ContagemDeAgua
from fonte_xp import FonteXP


class ContagemDeAguaAdapter(FonteXP):
    def __init__(self, contagem: ContagemDeAgua):
        self._contagem = contagem

    def podeGerarXP(self) -> bool:
        return self._contagem.validarMetaDiaria()

    def obterCategoria(self) -> CategoriaXP:
        return ContagemDeAgua.CATEGORIA  # sempre HIDRATACAO

    def obterPontos(self) -> int:
        return self._contagem.calcularXPGanho()

    def obterChaveCredito(self) -> str:
        # A meta gera XP uma vez por dia, mesmo que o usuário continue bebendo água.
        return f"agua:{self._contagem.idContagemDeAgua}:{self._contagem.dataRegistro.isoformat()}"
