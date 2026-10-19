"""Implementacao independente do Decorator para bonus de XP de habitos."""

from abc import ABC, abstractmethod
from datetime import date
from enum import Enum


class CategoriaXP(Enum):
    INTELECTUAL = 0
    SABEDORIA = 1
    ZEN = 2
    ATLETICO = 3
    HIDRATACAO = 4


class DiaSemana(Enum):
    SEGUNDA = 0
    TERCA = 1
    QUARTA = 2
    QUINTA = 3
    SEXTA = 4
    SABADO = 5
    DOMINGO = 6

    @classmethod
    def de_data(cls, data: date) -> "DiaSemana":
        return cls(data.weekday())


class Habito:
    XP_BASE = 10.0

    def __init__(
        self,
        titulo_habito: str,
        categoria: CategoriaXP,
        sequencia_dias_streak: int = 0,
    ) -> None:
        self.titulo_habito = titulo_habito
        self.categoria = categoria
        self.sequencia_dias_streak = sequencia_dias_streak

    def calcular_experiencia_gerada(self) -> float:
        return self.XP_BASE


class CalculadoraXP(ABC):
    @abstractmethod
    def calcular_experiencia_gerada(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def descrever(self) -> str:
        raise NotImplementedError


class XPBaseHabito(CalculadoraXP):
    def __init__(self, habito: Habito) -> None:
        self._habito = habito

    def calcular_experiencia_gerada(self) -> float:
        return self._habito.calcular_experiencia_gerada()

    def descrever(self) -> str:
        return f"XP base ({self.calcular_experiencia_gerada():.2f})"


class BonusXPDecorator(CalculadoraXP):
    def __init__(self, componente: CalculadoraXP) -> None:
        self._componente = componente

    def calcular_experiencia_gerada(self) -> float:
        return self._componente.calcular_experiencia_gerada()

    def descrever(self) -> str:
        return self._componente.descrever()


class BonusSequenciaDecorator(BonusXPDecorator):
    DIAS_POR_BLOCO = 7
    PERCENTUAL_POR_BLOCO = 10
    PERCENTUAL_MAXIMO = 50

    def __init__(self, componente: CalculadoraXP, sequencia_dias_streak: int) -> None:
        super().__init__(componente)
        self._sequencia_dias_streak = max(0, sequencia_dias_streak)

    def percentual(self) -> int:
        blocos = self._sequencia_dias_streak // self.DIAS_POR_BLOCO
        return min(blocos * self.PERCENTUAL_POR_BLOCO, self.PERCENTUAL_MAXIMO)

    def calcular_experiencia_gerada(self) -> float:
        xp_anterior = super().calcular_experiencia_gerada()
        return xp_anterior * (1 + self.percentual() / 100)

    def descrever(self) -> str:
        return (
            f"{super().descrever()} + bônus de sequência "
            f"+{self.percentual()}% ({self._sequencia_dias_streak} dias)"
        )


class BonusFimDeSemanaDecorator(BonusXPDecorator):
    PERCENTUAL = 20
    DIAS_COM_BONUS = frozenset({DiaSemana.SABADO, DiaSemana.DOMINGO})

    def __init__(self, componente: CalculadoraXP, data_checkin: date) -> None:
        super().__init__(componente)
        self._dia = DiaSemana.de_data(data_checkin)

    def percentual(self) -> int:
        return self.PERCENTUAL if self._dia in self.DIAS_COM_BONUS else 0

    def calcular_experiencia_gerada(self) -> float:
        xp_anterior = super().calcular_experiencia_gerada()
        return xp_anterior * (1 + self.percentual() / 100)

    def descrever(self) -> str:
        return (
            f"{super().descrever()} + bônus de fim de semana "
            f"+{self.percentual()}% ({self._dia.name})"
        )


def montar_calculadora(
    habito: Habito,
    data_checkin: date,
    *,
    bonus_sequencia: bool = True,
    bonus_fim_de_semana: bool = True,
) -> CalculadoraXP:
    calculadora: CalculadoraXP = XPBaseHabito(habito)
    if bonus_sequencia:
        calculadora = BonusSequenciaDecorator(calculadora, habito.sequencia_dias_streak)
    if bonus_fim_de_semana:
        calculadora = BonusFimDeSemanaDecorator(calculadora, data_checkin)
    return calculadora