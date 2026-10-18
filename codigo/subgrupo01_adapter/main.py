"""Demonstração do padrão Adapter: três fontes de XP creditadas pelo mesmo Client.

Execução (a partir da raiz do repositório):
    python3 codigo/subgrupo01_adapter/main.py
"""

from datetime import date, timedelta

from categoria_xp import CategoriaXP
from contagem_de_agua import ContagemDeAgua
from contagem_de_agua_adapter import ContagemDeAguaAdapter
from creditador_xp import CreditadorXP, ResultadoCredito
from fonte_xp import FonteXP
from habito import Habito
from habito_adapter import HabitoAdapter
from pet_virtual import PetVirtual
from sessao_pomodoro import SessaoPomodoro
from sessao_pomodoro_adapter import SessaoPomodoroAdapter

HOJE = date(2026, 10, 19)


def titulo(texto: str) -> None:
    print(f"\n=== {texto} ===")


def rodadaDeCredito(creditador: CreditadorXP, fontes: dict[str, FonteXP], pet: PetVirtual) -> None:
    # O Client percorre a lista sem saber qual atividade está por trás de cada FonteXP.
    for nome, fonte in fontes.items():
        resultado = creditador.creditar(fonte)
        detalhe = f" (+{fonte.obterPontos()} {fonte.obterCategoria().name})" if resultado is ResultadoCredito.CREDITADO else ""
        print(f"  {nome:<22} -> {resultado.value}{detalhe}")
    print(f"  {pet.obterEstadoAtual()}")


def main() -> None:
    print("Padrão GoF Estrutural Adapter: fontes de XP do PetVirtual")
    pet = PetVirtual("pet-01")
    creditador = CreditadorXP(pet)

    # Adaptees: classes do domínio, cada uma com sua própria interface e regra.
    sessao = SessaoPomodoro("sessao-01", duracao=25, categoria=CategoriaXP.INTELECTUAL)
    agua = ContagemDeAgua("agua-01", limiteDiario=2000, dataRegistro=HOJE)
    meditar = Habito("habito-01", "Meditar 10 minutos", CategoriaXP.ZEN)

    # Adapters: cada atividade é embrulhada para falar a interface FonteXP.
    fontes = {
        "SessaoPomodoroAdapter": SessaoPomodoroAdapter(sessao),
        "ContagemDeAguaAdapter": ContagemDeAguaAdapter(agua),
        "HabitoAdapter": HabitoAdapter(meditar, HOJE),
    }

    titulo("Rodada 1: nenhuma atividade cumpriu a própria regra")
    sessao.iniciarSessao()
    sessao.registrarTempoDeFoco(25)
    agua.adicionarVolume(1500)
    print(f"  Pomodoro em {sessao.statusSessao}; água em {agua.obterProgressoPercentual():.0f}%; hábito sem check-in")
    rodadaDeCredito(creditador, fontes, pet)

    titulo("Rodada 2: o usuário conclui as três atividades")
    sessao.finalizarSessao()
    agua.adicionarVolume(500)
    meditar.marcarConcluido(HOJE)
    print(f"  Pomodoro em {sessao.statusSessao}; água em {agua.obterProgressoPercentual():.0f}%; hábito concluído")
    rodadaDeCredito(creditador, fontes, pet)

    titulo("Rodada 3: nova tentativa sem novo evento")
    agua.adicionarVolume(300)
    print("  Usuário bebeu mais 300 ml depois da meta")
    rodadaDeCredito(creditador, fontes, pet)

    titulo("Rodada 4: dia seguinte")
    amanha = HOJE + timedelta(days=1)
    agua.resetarDiario(amanha)
    agua.adicionarVolume(2000)
    meditar.marcarConcluido(amanha)
    fontes["HabitoAdapter"] = HabitoAdapter(meditar, amanha)
    print("  Água e hábito cumpridos de novo; a sessão de ontem continua a mesma")
    rodadaDeCredito(creditador, fontes, pet)

    titulo("Restrição do modelo: Pomodoro não aceita HIDRATACAO")
    try:
        SessaoPomodoro("sessao-02", duracao=25, categoria=CategoriaXP.HIDRATACAO)
    except ValueError as erro:
        print(f"  ValueError: {erro}")


if __name__ == "__main__":
    main()
