"""Testes do padrão Adapter.

Execução (a partir da raiz do repositório):
    python3 -m unittest discover -s codigo/subgrupo01_adapter -v
"""

import unittest
from datetime import date, timedelta

from categoria_xp import CategoriaXP
from contagem_de_agua import ContagemDeAgua
from contagem_de_agua_adapter import ContagemDeAguaAdapter
from creditador_xp import CreditadorXP, ResultadoCredito
from evolucao import Evolucao
from fonte_xp import FonteXP
from habito import Habito
from habito_adapter import HabitoAdapter
from pet_virtual import PetVirtual
from sessao_pomodoro import SessaoPomodoro
from sessao_pomodoro_adapter import SessaoPomodoroAdapter

DIA = date(2026, 10, 19)


class BaseCredito(unittest.TestCase):
    def setUp(self):
        self.pet = PetVirtual("pet-teste")
        self.creditador = CreditadorXP(self.pet)


class TestSessaoPomodoroAdapter(BaseCredito):
    def setUp(self):
        super().setUp()
        self.sessao = SessaoPomodoro("s1", duracao=25, categoria=CategoriaXP.SABEDORIA)
        self.fonte = SessaoPomodoroAdapter(self.sessao)
        self.sessao.iniciarSessao()
        self.sessao.registrarTempoDeFoco(25)

    def test_sem_xp_antes_de_concluida(self):
        self.assertEqual(self.creditador.creditar(self.fonte), ResultadoCredito.REGRA_NAO_CUMPRIDA)
        self.assertEqual(self.pet.obterXP(CategoriaXP.SABEDORIA), 0)

    def test_credita_na_categoria_da_sessao_depois_de_concluida(self):
        self.sessao.finalizarSessao()
        self.assertEqual(self.creditador.creditar(self.fonte), ResultadoCredito.CREDITADO)
        self.assertEqual(self.pet.obterXP(CategoriaXP.SABEDORIA), 50)  # RN01: 25 min = +50 XP

    def test_mesma_sessao_nao_credita_duas_vezes(self):
        self.sessao.finalizarSessao()
        self.creditador.creditar(self.fonte)
        self.assertEqual(self.creditador.creditar(self.fonte), ResultadoCredito.JA_CREDITADO)
        self.assertEqual(self.pet.obterXP(CategoriaXP.SABEDORIA), 50)

    def test_restricao_de_categoria(self):
        with self.assertRaises(ValueError):
            SessaoPomodoro("s2", duracao=25, categoria=CategoriaXP.HIDRATACAO)


class TestContagemDeAguaAdapter(BaseCredito):
    def setUp(self):
        super().setUp()
        self.agua = ContagemDeAgua("a1", limiteDiario=2000, dataRegistro=DIA)
        self.fonte = ContagemDeAguaAdapter(self.agua)

    def test_sem_xp_abaixo_da_meta(self):
        self.agua.adicionarVolume(1999)
        self.assertEqual(self.creditador.creditar(self.fonte), ResultadoCredito.REGRA_NAO_CUMPRIDA)

    def test_credita_sempre_em_hidratacao(self):
        self.agua.adicionarVolume(2000)
        self.assertEqual(self.creditador.creditar(self.fonte), ResultadoCredito.CREDITADO)
        self.assertEqual(self.pet.obterXP(CategoriaXP.HIDRATACAO), ContagemDeAgua.XP_META_DIARIA)

    def test_volume_extra_no_mesmo_dia_nao_credita_de_novo(self):
        self.agua.adicionarVolume(2000)
        self.creditador.creditar(self.fonte)
        self.agua.adicionarVolume(500)
        self.assertEqual(self.creditador.creditar(self.fonte), ResultadoCredito.JA_CREDITADO)

    def test_novo_dia_credita_de_novo(self):
        self.agua.adicionarVolume(2000)
        self.creditador.creditar(self.fonte)
        self.agua.resetarDiario(DIA + timedelta(days=1))
        self.agua.adicionarVolume(2000)
        self.assertEqual(self.creditador.creditar(self.fonte), ResultadoCredito.CREDITADO)
        self.assertEqual(self.pet.obterXP(CategoriaXP.HIDRATACAO), 2 * ContagemDeAgua.XP_META_DIARIA)


class TestHabitoAdapter(BaseCredito):
    def setUp(self):
        super().setUp()
        self.habito = Habito("h1", "Correr 20 minutos", CategoriaXP.ATLETICO)

    def test_sem_xp_sem_conclusao_no_dia(self):
        fonte = HabitoAdapter(self.habito, DIA)
        self.assertEqual(self.creditador.creditar(fonte), ResultadoCredito.REGRA_NAO_CUMPRIDA)

    def test_credita_na_categoria_do_habito(self):
        self.habito.marcarConcluido(DIA)
        fonte = HabitoAdapter(self.habito, DIA)
        self.assertEqual(self.creditador.creditar(fonte), ResultadoCredito.CREDITADO)
        self.assertEqual(self.pet.obterXP(CategoriaXP.ATLETICO), Habito.XP_POR_CONCLUSAO)

    def test_conclusao_de_outro_dia_nao_conta(self):
        self.habito.marcarConcluido(DIA)
        fonte = HabitoAdapter(self.habito, DIA + timedelta(days=1))
        self.assertEqual(self.creditador.creditar(fonte), ResultadoCredito.REGRA_NAO_CUMPRIDA)


class TestClienteDependeSoDoTarget(BaseCredito):
    def test_target_e_abstrato(self):
        with self.assertRaises(TypeError):
            FonteXP()

    def test_fonte_nova_funciona_sem_alterar_o_creditador(self):
        # Uma atividade futura só precisa implementar FonteXP.
        class FonteFicticia(FonteXP):
            def podeGerarXP(self):
                return True

            def obterCategoria(self):
                return CategoriaXP.ZEN

            def obterPontos(self):
                return 7

            def obterChaveCredito(self):
                return "ficticia:1"

        self.assertEqual(self.creditador.creditar(FonteFicticia()), ResultadoCredito.CREDITADO)
        self.assertEqual(self.pet.obterXP(CategoriaXP.ZEN), 7)


class TestEvolucaoDoPet(unittest.TestCase):
    def setUp(self):
        self.pet = PetVirtual("pet-teste")

    def test_vetor_zerado_e_neutro(self):
        self.assertEqual(self.pet.determinarEvolucao(), Evolucao.NEUTRO)

    def test_categoria_predominante_define_a_forma(self):
        self.pet.adicionarXP(CategoriaXP.INTELECTUAL, 50)
        self.pet.adicionarXP(CategoriaXP.HIDRATACAO, 20)
        self.assertEqual(self.pet.calcularAtividadeMaxima(), CategoriaXP.INTELECTUAL)
        self.assertEqual(self.pet.determinarEvolucao(), Evolucao.ESTUDIOSO)

    def test_empate_no_topo_mantem_neutro(self):
        self.pet.adicionarXP(CategoriaXP.ZEN, 30)
        self.pet.adicionarXP(CategoriaXP.ATLETICO, 30)
        self.assertIsNone(self.pet.calcularAtividadeMaxima())
        self.assertEqual(self.pet.determinarEvolucao(), Evolucao.NEUTRO)


if __name__ == "__main__":
    unittest.main()
