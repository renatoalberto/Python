"""
Reduce

Obs: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar e
     utilizar a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em outro caso. 99% da vezes um loop
                  for é mais legível.

Para enterder o reduce():

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, a4, ..., an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y;

# Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e um iterável

reduce(funcao, dados)

# A função reduce funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2)    # Aplica a função nos dois primeiros parâmetros da coleção  e guarda o resultado
    Passo 2: res2 = f(res1, a3)  # Aplica a função no resulta do passo 1 mais o terceiro parâmetro e guarda o resultado
    Passo 3: res3 = f(res2, a4)  # Assim por diante
    ...
    Passo n: resn = f(resn -1, an)

# Alternativamente poderiamos ver a função reduce() como:

funcao(funcao(funcao(funcao(a1, a2), a3), a4) an)
"""
from functools import reduce

dados = [2, 3, 7, 13, 17, 22, 24, 27, 35, 37, 39, 40, 44, 53, 54]

# Para utilizar o reduce() precisamos de uma função que recebe dois parâmetros
mult = lambda x, y: x + y

res = reduce(mult, dados)
print(f'O resultado do reduce - {res} é o mesmo que utilizar a soma com sum() - {sum(dados)}' )
