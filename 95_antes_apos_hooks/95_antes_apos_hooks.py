"""
Unittest - Antes e após hooks

hooks - são os testes em si. Ou seja, a execução dos testes.

setup()    -> é executado antes de cada método de teste, é útil para criarmos instâncias
              de objetos ou outros dados.
tearDown() -> é executado ao final de cada método de teste, é útil para excluir dados ou
              fechar conexões de bancos de dados
"""
import unittest


class MuduloTest(unittest.TestCase):

    def setUp(self):
        # Configuração do setUp()
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
