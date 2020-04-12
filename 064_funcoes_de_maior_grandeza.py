"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?
- Quando um linguagem de programação suporta HOF, indica que podemos ter funções que retornam
  outras funções como resultado ou mesmo que podemos passar funções como argumento para outras
  funções, e até mesmo criar variáveis do tipo de funções nos nossos programas.

OBS: Na seção de funções utilizamos isso.

Em Python as funções são cidadões de primeira classe, First Class Citizen
"""
from random import choice


# Definindo as funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(a, b, funcao):
    return funcao(a, b)


# Testando as funções
print(calcular(5, 7, somar))
print(calcular(10, 3, diminuir))
print(calcular(3, 3, multiplicar))
print(calcular(9, 3, dividir))

# Funções aninhadas (Nested Functions) ------------------------------------------------------------
# Em Python podemos ter funções dentro de funções,
# também chamadas de funções internas (Inner Functions)


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Nick'))


# Retornando funções de outras funções ------------------------------------------------------------
def faz_me_rir():
    def rir():
        return choice(('HAHAHAHAHAHA', 'kkkkkkkkk', 'HEHEHEHEHEHE'))
    return rir


rindo = faz_me_rir()
print(rindo())


# Funções internas (Inner Functions) poder acessar o escopo de funções mais externas --------------
def chame_alguem(pessoa):
    def chamar():
        grito = choice(('Vem aqui', 'Ooou', 'Cadê vocêee'))
        return f'{grito} {pessoa}'
    return chamar


chamando = chame_alguem('Raíssa')
print(chamando())
