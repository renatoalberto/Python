"""
Annotations


__annotations__

A própria Type Hinting é uma annotation, informando a tipagem de uma variável e qual o tipo de retorno de uma função.
"""
from math import pi


def circunferencia(raio: float) -> float:
    return 2 * pi * raio


print(circunferencia.__annotations__)  # {'raio': <class 'float'>, 'return': <class 'float'>}

nome: str = 'Theo'
peso: float = 3,4
ativo: bool = True

# Annotations das variáveis globais do programa
print(__annotations__)  # {'nome': <class 'str'>, 'peso': <class 'float'>, 'ativo': <class 'bool'>}


# Declaração de uma classe
class Pessoa:

    def __init__(self, nome: str, peso: float, ativo: bool) -> None:
        self.__nome: str = nome
        self.__peso: float = peso
        self.__ativo: bool = ativo

    def andar(self) -> str:
        return f'{self.nome.title()} está andando'


theo = Pessoa(nome, peso, ativo)
print(theo.__dict__)                # A instância theo não possui annotation
print(theo.andar.__annotations__)   # O método andar de theo possui annotations
print(theo.__init__.__annotations__)
