"""
POO - Method Resolution Order (MRO)

Em Python podemos conferir a ordem de execução de métodos de 3 formas:
    - Via propriedade da classe ___mro___, que retorna uma tupla ()
    - Via método mro(), que retorna uma lista []
    - Via help
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def apresentar(self):
        print(f'Olá, eu sou o {self.__nome}')


class AnimalAquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        print(f'{self._Animal__nome} está nadando')

    def apresentar(self):
        print(f'Olá, eu sou o {self._Animal__nome} do mar.')


class AnimalTerrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        print(f'{self._Animal__nome} está andando')

    def apresentar(self):
        print(f'Olá, eu sou o {self._Animal__nome} da terra')


# class Pinguim(AnimalAquatico, AnimalTerrestre):   # Ordem dos métodos herdados alteram o comportamento da classe
class Pinguim(AnimalTerrestre, AnimalAquatico):     # Ordem dos métodos herdados alteram o comportamento da classe
    def __init__(self, nome):
        super().__init__(nome)


# ???? em apresentar(), qual método irá executar ???? - Method Resolution Order (MRO)
# Quando class Pinguim(AnimalTerrestre, AnimalAquatico) - Olá, eu sou o Tux da terra
# Quando class Pinguim(AnimalAquatico, AnimalTerrestre) - Olá, eu sou o Tux do mar
pinguim = Pinguim('Tux')
pinguim.apresentar()
pinguim.andar()
pinguim.nadar()

print()

# *Conferindo a ordem de execução com a classe __mro__, retorna uma tupla
#
#   Declaração Pinguim(AnimalAquatico, AnimalTerrestre) | Declaração Pinguim(AnimalTerrestre, AnimalAquatico)
#   ----------------------------------------------------|----------------------------------------------------
#     1ª - <class '__main__.Pinguim'>                   |   1ª - <class '__main__.Pinguim'>
#     2ª - <class '__main__.AnimalAquatico'>            |   2ª - <class '__main__.AnimalTerrestre'>
#     3ª - <class '__main__.AnimalTerrestre'>           |   3ª - <class '__main__.AnimalAquatico'>
#     4ª - <class '__main__.Animal'>                    |   4ª - <class '__main__.Animal'>
#     5ª - <class 'object'>                             |   5ª - <class 'object'>
print(Pinguim.__mro__)

# *Conferindo a ordem de execução com a classe mro(), retorna uma lista
print(Pinguim.mro())

# *Conferindo a ordem de execução com a classe mro(), retorna uma lista
print(help(Pinguim))
""" 
 |  Method resolution order:
 |      Pinguim
 |      AnimalTerrestre
 |      AnimalAquatico
 |      Animal
 |      builtins.object
"""
