"""
Doctests

Doctests - São testes incluídos nas docstring das funções/métodos do Python

No terminal:
- Execução do código : python 92_testes_doctests.py
- Execução do doctest: python -m doctest -v 92_testes_doctests.py
"""


def soma(a, b):
    """Soma os parâmetros a e b

    >>> soma(1, 2)
    3
    >>> soma(4, 6)
    10
    >>> soma(7, 4)
    5
    """
    return a + b


# Outro exemplo, Aplicando o TDD (Test Driven Develop) --------------------------------------------
def duplicar(valores):
    """Duplicar os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
       ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
    """
    return [elemento * 2 for elemento in valores]


# Erro inesperado ---------------------------------------------------------------------------------
def fala_oi():
    """
    Somente diz oi

    * Cuidado para não utilizar aspas duplas em uma docstring

    >>> fala_oi()
    "oi"
    """
    return "oi"


# Outro erro inesperado ---------------------------------------------------------------------------
def verdade():
    """Retorna verdade

    * Cuidado com os espaços finais no retorno da função, no doctest, pois aparentemente  estará  tudo  certo,
    * mas o Python vai Retornar um erro que pode ser difícil entender. A ferramenta Pycharm retira os espaços
    * automaticamente quando salvar.

    >>> verdade()
    True
    """
    return True
