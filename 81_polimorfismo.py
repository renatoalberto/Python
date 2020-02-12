"""
POO - Polimorfismo

Latim:
    - Poli   -> Muitas
    - Morfis -> Formas

Quando a gente reimplementa um método da classe pai na classe filha estamos realizando uma
sobrescrita de método (Overriding).

Overriding é a melhor representação do polimorfismo.
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    # Classe falar() é abstrata.
    def falar(self):
        raise NotImplementedError('A classe filha deve implementar o método falar.')

    def comer(self):
        print(f'{self.__nome} está comendo.')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au.')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau.')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo.')


nick = Cachorro('Nick')
gato = Gato('Tom')
rato = Rato('Jerry')

nick.comer()
nick.falar()

gato.comer()
gato.falar()

rato.comer()
rato.falar()
