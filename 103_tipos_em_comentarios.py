"""
Tipos em comentários

Outra forma de implementar Type Hinting
Não duplique a implementação do Type Hinting (direta na variável e em comentário), MyPy retorna erro
"""
import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


# utilização a própria IDE reconhece a tipagem dos atributos da função circunferência
circunferencia(8)

# validação com MyPy reconhece tipagem feita em comentários
# error: Argument 1 to "circunferencia" has incompatible type "str"; expected "float"
# circunferencia('Renato')


# Forma 1 -------------------------------------------------------------------------------
def cabecalho1(texto, alinhamento):
    # type: (str, bool) -> str
    if alinhamento:
        return f'{texto.title()}\n{"=" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '=')


# Forma 2
def cabecalho2(
        texto,  # type: str
        alinhamento  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return f'{texto.title()}\n{"=" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '=')


print(cabecalho1.__annotations__)  # Annotations não reconhece type hinting em comentários

# tipagem de atributos com comentário ---------------------------------------------------
nome = 'Geek University'  # type: str
