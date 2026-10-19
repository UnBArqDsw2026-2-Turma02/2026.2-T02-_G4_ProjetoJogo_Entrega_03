"""Target: a interface que o CreditadorXP (Client) espera de qualquer atividade."""

from abc import ABC, abstractmethod

from categoria_xp import CategoriaXP


class FonteXP(ABC):
    @abstractmethod
    def podeGerarXP(self) -> bool:
        """Verdadeiro quando a regra da atividade permite creditar XP."""

    @abstractmethod
    def obterCategoria(self) -> CategoriaXP:
        """Categoria em que o XP deve ser creditado."""

    @abstractmethod
    def obterPontos(self) -> int:
        """Quantidade de XP a creditar."""

    @abstractmethod
    def obterChaveCredito(self) -> str:
        """Identifica o evento que gera XP. O Client usa a chave para não creditar o mesmo evento duas vezes."""
