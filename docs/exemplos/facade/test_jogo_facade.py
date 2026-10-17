import unittest
from jogo_facade import (
    CategoriaXP, Conquista, Evolucao, JogoFacade, SituacaoConclusao, Usuario,
)


class TestJogoFacade(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario("u1", conquistas=[Conquista("Primeira", 1), Conquista("Duas", 2)])
        self.jogo = JogoFacade(self.usuario)

    def test_fluxo_completo_e_conquista_usa_historico_atualizado(self):
        resultado = self.jogo.concluirAtividade("p1", CategoriaXP.INTELECTUAL, 50)
        self.assertEqual(resultado.situacao, SituacaoConclusao.PROCESSADA)
        self.assertEqual(self.usuario.pet.vetorXP, (50, 0, 0, 0, 0))
        self.assertEqual(self.usuario.pet.evolucao, Evolucao.ESTUDIOSO)
        self.assertEqual(len(self.usuario.historico.registros), 1)
        self.assertEqual(resultado.novasConquistas, ("Primeira",))
        self.assertFalse(self.usuario.conquistas[1].foiDesbloqueada)

    def test_reenvio_nao_duplica_efeitos_inclusive_em_outra_fachada(self):
        self.jogo.concluirAtividade("p1", CategoriaXP.INTELECTUAL, 50)
        resultado = JogoFacade(self.usuario).concluirAtividade("p1", CategoriaXP.INTELECTUAL, 50)
        self.assertEqual(resultado.situacao, SituacaoConclusao.JA_REGISTRADA)
        self.assertEqual(self.usuario.pet.vetorXP, (50, 0, 0, 0, 0))
        self.assertEqual(len(self.usuario.historico.registros), 1)
        self.assertEqual(resultado.novasConquistas, ())

    def test_nova_ocorrencia_atualiza_categoria_e_nao_reanuncia_conquista(self):
        self.jogo.concluirAtividade("p1", CategoriaXP.INTELECTUAL, 50)
        resultado = self.jogo.concluirAtividade("a1", CategoriaXP.HIDRATACAO, 60)
        self.assertEqual(self.usuario.pet.vetorXP, (50, 0, 0, 0, 60))
        self.assertEqual(self.usuario.pet.evolucao, Evolucao.HIDRATADO)
        self.assertEqual(resultado.novasConquistas, ("Duas",))
        self.assertEqual(len(self.usuario.historico.registros), 2)

    def test_entradas_invalidas_nao_alteram_estado(self):
        for identificador, categoria, pontos in [
            ("", CategoriaXP.ZEN, 10), ("  ", CategoriaXP.ZEN, 10),
            (None, CategoriaXP.ZEN, 10), ("h1", "ZEN", 10),
            ("h1", CategoriaXP.ZEN, -1), ("h1", CategoriaXP.ZEN, 1.5),
            ("h1", CategoriaXP.ZEN, True),
        ]:
            with self.subTest(entrada=(identificador, categoria, pontos)):
                with self.assertRaises(ValueError):
                    self.jogo.concluirAtividade(identificador, categoria, pontos)
                self.assertEqual(self.usuario.pet.vetorXP, (0, 0, 0, 0, 0))
                self.assertEqual(self.usuario.historico.registros, ())
                self.assertFalse(any(c.foiDesbloqueada for c in self.usuario.conquistas))

    def test_usuarios_nao_compartilham_estado(self):
        outro = Usuario("u2")
        self.jogo.concluirAtividade("p1", CategoriaXP.INTELECTUAL, 50)
        self.assertEqual(outro.pet.vetorXP, (0, 0, 0, 0, 0))
        self.assertEqual(outro.historico.registros, ())
        self.assertFalse(outro.conquistas[0].foiDesbloqueada)

    def test_forma_por_categoria(self):
        formas = [Evolucao.ESTUDIOSO, Evolucao.LEITOR, Evolucao.ZEN,
                  Evolucao.ATLETICO, Evolucao.HIDRATADO]
        for categoria, forma in zip(CategoriaXP, formas):
            with self.subTest(categoria=categoria):
                usuario = Usuario("u")
                JogoFacade(usuario).concluirAtividade("a1", categoria, 10)
                self.assertEqual(usuario.pet.evolucao, forma)

    def test_empate_preserva_forma_conforme_regra_ilustrativa(self):
        self.jogo.concluirAtividade("p1", CategoriaXP.INTELECTUAL, 50)
        self.jogo.concluirAtividade("h1", CategoriaXP.ZEN, 50)
        self.assertEqual(self.usuario.pet.evolucao, Evolucao.ESTUDIOSO)


if __name__ == "__main__":
    unittest.main()
