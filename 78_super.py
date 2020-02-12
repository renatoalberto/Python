"""
POO - O método super()

O método super() se refere a super classe, a partir dele temos acesso a qualquer elemento da classe pai
"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.especie = especie

    def emite_som(self, som):
        print(f'{self.__nome} fala {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # possível, mas não recomendado
        super().__init__(nome, especie)  # recomendado
        self.__raca = raca


gato = Gato('gato', 'felino', 'angorá')
gato.emite_som('miau')

