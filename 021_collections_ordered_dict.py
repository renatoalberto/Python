"""
Módulo Collections - Ordered Dict
Documentação: https://docs.python.org/3/library/collections.html#collections.OrderedDict

Ordered Dict - É um dicionário que nos garante a ordem de inserção dos elementos, além de ter uma melhor performance
"""
from collections import OrderedDict

# Em um dicionário a ordem de inserção de elementos não é garantida
dicionario = {'Renato': 10, 'Raíssa': 2, 'Jéssica': 3, 'Karina': 4, 'Luiza': 5}
for chave, valor in dicionario.items():
    print(f'{chave} : {valor}', end=' ')
print()

# Com OrderedDict a ordem de inserção é garantida
dicionario = OrderedDict({'Renato': 10, 'Raíssa': 2, 'Jéssica': 3, 'Karina': 4, 'Luiza': 5})
for chave, valor in dicionario.items():
    print(f'{chave} : {valor}', end=' ')
print()

# Demonstrando que a ordem em um dict não importa
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 2, 'a': 1}

print(f'Os dicionários são iguais porque a ordem não importa: {dic1 == dic2}')  # True

dic1 = OrderedDict({'a': 1, 'b': 2})
dic2 = OrderedDict({'b': 2, 'a': 1})

print(f'Os dicionários NÃO são iguais porque no OrderedDict a ordem importa: {dic1 == dic2}')  # False
