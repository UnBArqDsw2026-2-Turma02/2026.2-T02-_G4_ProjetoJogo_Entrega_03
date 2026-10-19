"""Testes do Decorator de bonus de XP.

Execucao a partir da raiz do repositorio:
    python3 -m unittest discover -s docs/Base/DiagramaDecorator -p "test_*.py" -v
"""

import unittest
from datetime import date

from decorator_xp import (
    BonusFimDeSemanaDecorator,
    BonusSequenciaDecorator,
    CategoriaXP,
    Habito,
    XPBaseHabito,
    montar_calculadora,
)


class TestBonusSequencia(unittest.TestCase):
    def test_percentual_por_faixa_e_teto(self):
        for dias, esperado in ((0, 0), (6, 0), (7, 10), (14, 20), (35, 50), (100, 50)):
            with self.subTest(dias=dias):
                camada = BonusSequenciaDecorator(XPBaseHabito(Habito("Agua", CategoriaXP.HIDRATACAO)), dias)
                self.assertEqual(camada.percentual(), esperado)

    def test_streak_negativo_nao_aplica_bonus(self):
        camada = BonusSequenciaDecorator(XPBaseHabito(Habito("Agua", CategoriaXP.HIDRATACAO)), -1)
        self.assertEqual(camada.percentual(), 0)
        self.assertEqual(camada.calcular_experiencia_gerada(), 10.0)


class TestBonusFimDeSemana(unittest.TestCase):
    def test_sabado_recebe_bonus(self):
        camada = BonusFimDeSemanaDecorator(
            XPBaseHabito(Habito("Agua", CategoriaXP.HIDRATACAO)), date(2026, 10, 17)
        )
        self.assertEqual(camada.percentual(), 20)
        self.assertEqual(camada.calcular_experiencia_gerada(), 12.0)

    def test_domingo_recebe_bonus(self):
        camada = BonusFimDeSemanaDecorator(
            XPBaseHabito(Habito("Agua", CategoriaXP.HIDRATACAO)), date(2026, 10, 18)
        )
        self.assertEqual(camada.percentual(), 20)

    def test_dia_util_nao_recebe_bonus(self):
        camada = BonusFimDeSemanaDecorator(
            XPBaseHabito(Habito("Agua", CategoriaXP.HIDRATACAO)), date(2026, 10, 14)
        )
        self.assertEqual(camada.percentual(), 0)
        self.assertEqual(camada.calcular_experiencia_gerada(), 10.0)


class TestMontagemDosDecorators(unittest.TestCase):
    def setUp(self):
        self.habito = Habito("Agua", CategoriaXP.HIDRATACAO, sequencia_dias_streak=14)
        self.sabado = date(2026, 10, 17)

    def test_combina_bonus_de_sequencia_e_fim_de_semana(self):
        calculadora = montar_calculadora(self.habito, self.sabado)
        self.assertAlmostEqual(calculadora.calcular_experiencia_gerada(), 14.4)

    def test_ordem_das_camadas_nao_altera_resultado(self):
        base = XPBaseHabito(self.habito)
        sequencia_depois = BonusFimDeSemanaDecorator(
            BonusSequenciaDecorator(base, 14), self.sabado
        )
        fim_de_semana_depois = BonusSequenciaDecorator(
            BonusFimDeSemanaDecorator(base, self.sabado), 14
        )
        self.assertAlmostEqual(
            sequencia_depois.calcular_experiencia_gerada(),
            fim_de_semana_depois.calcular_experiencia_gerada(),
        )

    def test_montagem_com_camadas_ativas_ou_desativadas(self):
        casos = (
            (True, True, 14.4),
            (True, False, 12.0),
            (False, True, 12.0),
            (False, False, 10.0),
        )
        for sequencia, fim_de_semana, esperado in casos:
            with self.subTest(sequencia=sequencia, fim_de_semana=fim_de_semana):
                calculadora = montar_calculadora(
                    self.habito,
                    self.sabado,
                    bonus_sequencia=sequencia,
                    bonus_fim_de_semana=fim_de_semana,
                )
                self.assertAlmostEqual(calculadora.calcular_experiencia_gerada(), esperado)

    def test_decorators_nao_alteram_o_habito(self):
        calculadora = montar_calculadora(self.habito, self.sabado)
        self.assertAlmostEqual(calculadora.calcular_experiencia_gerada(), 14.4)
        self.assertEqual(self.habito.calcular_experiencia_gerada(), 10.0)
        self.assertEqual(self.habito.sequencia_dias_streak, 14)


if __name__ == "__main__":
    unittest.main()