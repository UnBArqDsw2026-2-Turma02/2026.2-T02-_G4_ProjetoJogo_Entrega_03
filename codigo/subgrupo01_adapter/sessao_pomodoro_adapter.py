"""Adapter: traduz SessaoPomodoro para a interface FonteXP."""

from categoria_xp import CategoriaXP
from fonte_xp import FonteXP
from sessao_pomodoro import SessaoPomodoro


class SessaoPomodoroAdapter(FonteXP):
    def __init__(self, sessao: SessaoPomodoro):
        self._sessao = sessao

    def podeGerarXP(self) -> bool:
        return self._sessao.statusSessao == "CONCLUIDA"

    def obterCategoria(self) -> CategoriaXP:
        return self._sessao.categoria  # INTELECTUAL ou SABEDORIA, escolhida na sessão

    def obterPontos(self) -> int:
        return self._sessao.calcularXPGanho()

    def obterChaveCredito(self) -> str:
        return f"pomodoro:{self._sessao.idSessao}"  # uma sessão gera XP uma única vez
