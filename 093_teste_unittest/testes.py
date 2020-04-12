"""
O arquivo de teste é um arquivo separado, não vai junto ao módulo, é independente da aplicação

A impressão no terminal é melhor que o retorno do Pycharm
no terminal informe: python testes.py
"""

import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTeste(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_trash_food(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir 4 horas'
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormir muito, estou atrasado para o trabalho'
        )

    def test_eh_engracada(self):
        """Testando retorno pessoa engraçada"""

        # metodologia TDD - enquanto método eh_engracada não foi implementada, utilize assertEqual
        self.assertEqual(eh_engracada('Sérgio Malandro'), False)

        # metodologia TDD - enquanto método eh_engracada não foi implementado, o assertFalse sempre será ok
        # porque None = False
        self.assertFalse(eh_engracada('Sérgio Malandro'), 'Sérgio Malandro não deveria ser engraçado.')

        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado.')


if __name__ == '__main__':
    unittest.main()
