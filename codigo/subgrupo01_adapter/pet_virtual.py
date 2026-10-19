"""PetVirtual: recebe o XP. Não conhece nenhuma fonte de XP."""

from categoria_xp import CategoriaXP
from evolucao import Evolucao

# RN05 (Entrega 02): a forma do pet segue a categoria predominante no vetorXP.
EVOLUCAO_POR_CATEGORIA = {
    CategoriaXP.INTELECTUAL: Evolucao.ESTUDIOSO,
    CategoriaXP.SABEDORIA: Evolucao.LEITOR,
    CategoriaXP.ZEN: Evolucao.ZEN,
    CategoriaXP.ATLETICO: Evolucao.ATLETICO,
    CategoriaXP.HIDRATACAO: Evolucao.HIDRATADO,
}


class PetVirtual:
    def __init__(self, idPet: str):
        self._idPet = idPet
        self._vetorXP = [0] * len(CategoriaXP)

    def adicionarXP(self, categoria: CategoriaXP, pontos: int) -> None:
        if pontos <= 0:
            raise ValueError("pontos deve ser maior que zero")
        self._vetorXP[categoria.value] += pontos

    # Leitura do vetorXP por categoria. O diagrama de classes omite getters por convenção.
    def obterXP(self, categoria: CategoriaXP) -> int:
        return self._vetorXP[categoria.value]

    def calcularAtividadeMaxima(self) -> CategoriaXP | None:
        """Categoria com mais XP. None quando nenhuma predomina: vetor zerado ou empate no topo."""
        maior = max(self._vetorXP)
        if maior == 0 or self._vetorXP.count(maior) > 1:
            return None
        return CategoriaXP(self._vetorXP.index(maior))

    def determinarEvolucao(self) -> Evolucao:
        # Recorte: a RN05 também exige taxa de conclusão (Usuario.calcularTaxaCompletacao()),
        # que fica fora do escopo do Adapter. Por isso DESMOTIVADO não é avaliado aqui.
        categoria = self.calcularAtividadeMaxima()
        if categoria is None:
            return Evolucao.NEUTRO
        return EVOLUCAO_POR_CATEGORIA[categoria]

    def obterEstadoAtual(self) -> str:
        valores = ", ".join(f"{c.name}={self._vetorXP[c.value]}" for c in CategoriaXP)
        return f"Pet {self._idPet} [{valores}] forma: {self.determinarEvolucao().name}"
