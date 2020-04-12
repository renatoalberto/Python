import unittest
from robo import Robo


class RoboTestes(unittest.TestCase):

    # o setUp criará o objeto megaman antes da execução do teste
    def setUp(self):
        print('O método setUp() está sendo executado....')
        self.megaman = Robo(nome='Megaman', bateria=75)

    def test_carregar(self):
        """Testando o método de carregamento de bateria"""
        self.assertEqual(self.megaman.carregar(), 100, 'A bateria não foi carregada até atingir 100%.')

    def test_dizer_nome(self):
        """Testando método dizendo_nome() e verificação do consumo de bateria"""
        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BOOP BEEP BEEP BOOP. EU SOU MEGAMAN')
        self.assertEqual(self.megaman.bateria, 74, 'A bateria deveria está em 74%.')

    def tearDown(self):
        print('O método tearDown() está sendo executado..')
        print()


if __name__ == '__main__':
    unittest.main()
