"""Demonstração do Decorator de bônus de XP (roteiro para o vídeo).

Executar a partir da raiz do repositório:
    python3 docs/Base/DiagramaDecorator/demo.py
"""
import sys
from datetime import date

from decorator_xp import (
    BonusFimDeSemanaDecorator,
    BonusSequenciaDecorator,
    CategoriaXP,
    Habito,
    XPBaseHabito,
    montar_calculadora,
)

try:  # garante acentos corretos em terminais Windows
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

QUARTA = date(2026, 10, 14)
SABADO = date(2026, 10, 17)

# (descrição, dias de streak, data do check-in, bônus de sequência, bônus de fim de semana, XP esperado)
CENARIOS = [
    ("Quarta, sequência de 2 dias", 2, QUARTA, True, True, 10.00),
    ("Quarta, sequência de 7 dias", 7, QUARTA, True, True, 11.00),
    ("Sábado, sequência de 2 dias", 2, SABADO, True, True, 12.00),
    ("Sábado, sequência de 14 dias (os dois bônus se combinam)", 14, SABADO, True, True, 14.40),
    ("Sábado, sequência de 100 dias (sequência no teto de +50%)", 100, SABADO, True, True, 18.00),
    ("Sábado, 14 dias, só o bônus de fim de semana", 14, SABADO, False, True, 12.00),
    ("Sábado, 14 dias, só o bônus de sequência", 14, SABADO, True, False, 12.00),
    ("Sábado, 14 dias, nenhum bônus", 14, SABADO, False, False, 10.00),
]


def titulo(texto: str) -> None:
    print("\n" + "=" * 74)
    print(texto)
    print("=" * 74)


def parte_1_camada_por_camada() -> None:
    titulo("PARTE 1 - Empilhando as camadas, uma por vez")
    habito = Habito("Beber água", CategoriaXP.HIDRATACAO, sequencia_dias_streak=14)
    print(f"Hábito: {habito.titulo_habito} | sequência: {habito.sequencia_dias_streak} dias | check-in: sábado\n")

    calculadora = XPBaseHabito(habito)
    print(f"{'1) XP base, sem nenhuma camada':<46}-> {calculadora.calcular_experiencia_gerada():6.2f}")

    calculadora = BonusSequenciaDecorator(calculadora, habito.sequencia_dias_streak)
    rotulo = f"2) + camada de sequência (+{calculadora.percentual()}%)"
    print(f"{rotulo:<46}-> {calculadora.calcular_experiencia_gerada():6.2f}")

    calculadora = BonusFimDeSemanaDecorator(calculadora, SABADO)
    rotulo = f"3) + camada de fim de semana (+{calculadora.percentual()}%)"
    print(f"{rotulo:<46}-> {calculadora.calcular_experiencia_gerada():6.2f}")

    print(f"\nCamadas aplicadas: {calculadora.descrever()}")
    print(
        f"O Habito continua devolvendo {habito.calcular_experiencia_gerada():.2f}: "
        "a classe original não foi alterada."
    )


def parte_2_cenarios() -> bool:
    titulo("PARTE 2 - Combinações de bônus (XP base = 10,00)")
    todos_ok = True
    for numero, (descricao, streak, data, sequencia, fim_de_semana, esperado) in enumerate(CENARIOS, 1):
        habito = Habito("Beber água", CategoriaXP.HIDRATACAO, sequencia_dias_streak=streak)
        calculadora = montar_calculadora(
            habito, data, bonus_sequencia=sequencia, bonus_fim_de_semana=fim_de_semana
        )
        xp = calculadora.calcular_experiencia_gerada()
        conferiu = abs(xp - esperado) < 1e-9
        todos_ok = todos_ok and conferiu
        marca = "[OK]  " if conferiu else "[ERRO]"
        print(f"{marca} {numero}. {descricao:<58} {xp:6.2f}")
    return todos_ok


def main() -> int:
    parte_1_camada_por_camada()
    todos_ok = parte_2_cenarios()
    print()
    if todos_ok:
        print(f"Resultado: os {len(CENARIOS)} cenários bateram com o valor esperado.")
        return 0
    print("Resultado: algum cenário não bateu com o valor esperado.")
    return 1


if __name__ == "__main__":
    sys.exit(main())