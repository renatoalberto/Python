"""
Módulo Collections - Named Tuple
Documentação: https://docs.python.org/3/library/collections.html#collections.namedtuple

Named Tuple - São tuplas diferenciadas, onde especificamos nomes para as mesmas e também parâmetros. É como criar
              um tipo de dado pessoal.
"""
from collections import namedtuple

# Precisamos definir o nome e parâmetros ----------------------------------------------------------
# Forma 1 - Declaração namedtuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração namedtuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração namedtuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])


# Usando um namedtuple ----------------------------------------------------------------------------
nick = cachorro(idade=10, raca='Shih-tzu', nome='Nick')
print(type(nick))

# Acessando os dados ------------------------------------------------------------------------------
# Forma 1
print(f'namedtuple - {nick}. Idade - {nick[0]}. Raça - {nick[1]}. Nome - {nick[2]}')

# Forma 2
print(f'namedtuple - {nick}. Idade - {nick.idade}. Raça - {nick.raca}. Nome - {nick.nome}')

# Sabendo qual o índice de um valor ---------------------------------------------------------------
print(f'Qual o índice do valor "Shih-tzu - {nick.index("Shih-tzu")}')
print(f'Quantas vezes se repete o valor "Shih-tzu - {nick.count("Shih-tzu")}')

