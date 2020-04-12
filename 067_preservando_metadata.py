"""
Preservando Metadados com Wraps

Metadados - são dados intrínseco em arquivos

Wraps     - são funções que envolvem elementos com diversas finalidade
"""


def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui é a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# Aqui imprimiu os valores esperados, pois o decorator foi desempacotado
print(soma(10, 30))

# Aqui imprimiu os valores da função decoradora, pois não houve o desempacotado
print(soma.__name__)  # logar
print(soma.__doc__)   # Eu sou uma função (logar) dentro de outra


# Resolução do problema ---------------------------------------------------------------------------
from functools import wraps  # wraps() - preservar os metadados das nossas funções


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui é a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# Aqui imprimiu os valores esperados, pois o decorator foi desempacotado
print(soma(10, 30))

# Aqui imprimiu os valores esperados, com a utilização da função wraps() de pacote functools
print(soma.__name__)  # logar
print(soma.__doc__)   # Eu sou uma função (logar) dentro de outra
