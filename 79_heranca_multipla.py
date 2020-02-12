"""
POO - Herança Múltipla

Quando em java herdamos somente de uma única classe, em Python podemos herdar de múltiplas classes, fazendo com
que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

Obs: A herança múltipla pode ser feita de 2 maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta.

Obs: Não importa se a derivação é direta ou indireta, a classe filha herdará todos os atributos e métodos da classe pai.
"""


# Exemplo 1 - Multiderivação Direta ---------------------------------------------------------------
class Pai1:
    pass


class Pai2:
    pass


class Pai3:
    pass


class MultiderivaçãoDireta(Pai1, Pai2, Pai3):
    pass


# Exemplo 2 - Multiderivação Indireta
class Pai1:
    pass


class Pai2(Pai1):
    pass


class Pai3(Pai2):
    pass


class MultiderivacaoIndireta(Pai3):
    pass


# Exemplo real ------------------------------------------------------------------------------------
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


class Pinguim(AnimalAquatico, AnimalTerrestre):
    def __init__(self, nome):
        super().__init__(nome)


baleia = AnimalAquatico('Wally')
baleia.apresentar()
baleia.nadar()

print()

tatu = AnimalTerrestre('Xim')
tatu.apresentar()
tatu.andar()

print()

# ???? em apresentar(), qual método irá executar ???? - Method Resolution Order (MRO)
# Ordem da herança altera o comportamento da classe
# Quando class Pinguim(AnimalTerrestre, AnimalAquatico) - Olá, eu sou o Tux da terra
# Quando class Pinguim(AnimalAquatico, AnimalTerrestre) - Olá, eu sou o Tux do mar
pinguim = Pinguim('Tux')
pinguim.apresentar()
pinguim.andar()
pinguim.nadar()

print()

# isinstance() para saber se um objeto é instância de uma class
print(f'pinguim Tux é instância de Piguim          - {isinstance(pinguim, Pinguim)}')
print(f'pinguim Tux é instância de AnimalTerrestre - {isinstance(pinguim, AnimalTerrestre)}')
print(f'pinguim Tux é instância de AnimalAquático  - {isinstance(pinguim, AnimalAquatico)}')
print(f'pinguim Tux é instância de Animal          - {isinstance(pinguim, Animal)}')
print(f'pinguim Tux é instância de object          - {isinstance(pinguim, object)}')
print(f'pinguim Tux é instância de str             - {isinstance(pinguim, str)}')


