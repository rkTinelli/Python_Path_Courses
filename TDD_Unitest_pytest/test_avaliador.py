from unittest import TestCase
from src.leilao.dominio import Avaliador, Lance, Leilao, Usuario

class TestAvaliador(TestCase):
    def test_avalia(self):

        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lance_do_yuri =Lance(yuri, 100.00)
        lance_do_gui =Lance(gui, 150.00)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
