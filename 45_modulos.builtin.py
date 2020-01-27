"""
Trabalhando com módulos built-in - (São módulos integrados, que já vem instalados)

Documentação - https://docs.python.org/3/py-modindex.html

|Python|Módulos Built-in|

Existem vários módulos pré instalados, mas é necessário realizar o import para não sobrecarregar a memória
"""
print(dir())
# Lista de módulos carregados
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__']

from random import random
print(dir())
# Lista de módulos carregados - após import da função random é disponibilizada em memória
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'random']

# Realizando imports ------------------------------------------------------------------------------
# Existe duas formas de utilizar um módulo ou função deste 
# --- Forma 1 --- Importando todo o módulo * Não recomendado
# import random

# Para utilizar a função random(), colocamos o nome do pacote e o nome da função separados por ponto
# print(random.random())

# É possível informar um alias (apelido) para o módulo
# import random as rdm
# print(rdm.random())

# Ao importa o todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficam disponíveis (Carregados em memória)

# Caso você saiba quais funções precisa utilizar deste módulo, então este não seria a forma ideal de utilização

# --- Forma 2 ---
# No import a seguir, estamos solicitando somente a funçao específica do módulo random
# from random import random

# É de costume utilizar tuple para importação de várias funções, com quebra de linha
# from random import (
#     random,
#     uniform,
#     randint,
#     choice,
#     shuffle
# )

# É possível realizar o importe de todos as funções do módulo
# from random import *

# É possível informar um alias (apelido) para função
# from random import randint as rdi, random as rdm

# Para utilizar a função random(), não é necessário fazer referência do módulo
# print(random())

