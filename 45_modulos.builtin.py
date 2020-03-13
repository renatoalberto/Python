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

import math, time, random

# ----------------------------------- método math  ------------------------------------------------
# Arredondamento para cima ------------------------------------------------------------------------
print(math.ceil(5.7))  # 6
print(math.ceil(5.2))  # 6

# Arredondamento para baixo -----------------------------------------------------------------------
print(math.floor(5.7))  # 5
print(math.floor(5.2))  # 5

# Soma valores ------------------------------------------------------------------------------------
print(math.fsum([1, 2, 3, 5, 6, 7]))  # 24.0
print(math.fsum([100, 150, 200]))     # 450.0

# Raiz quadrada -----------------------------------------------------------------------------------
print(math.sqrt(9))   # 3.0
print(math.sqrt(16))  # 4.0

# ----------------------------------- método time  ------------------------------------------------
# time.localtime() --------------------------------------------------------------------------------
# time.struct_time(tm_year=2020, tm_mon=2, tm_mday=21, tm_hour=14, tm_min=17, tm_sec=36,
# tm_wday=4,    => Dia da semana (Segunda = 0, Terça = 1, ..., Domingo = 6)
# tm_yday=52,   => Dia do ano
# tm_isdst=0)
print(time.localtime())
print(f'Hora: {time.localtime().tm_hour}')
print(f'Minuto: {time.localtime().tm_min}')


# time.perf_counter() -----------------------------------------------------------------------------
# Exemplo de utilização
inicio = time.perf_counter()
print('Digite o seu nome: Renato')
fim = time.perf_counter()
tempo_gasto = fim - inicio
print(f'Você gastou {round(tempo_gasto, 2)} segundo digitando o seu nome.')

# ----------------------------------- método random -----------------------------------------------
print(random.randint(0, 10))  # Apresente números randômicos entre 0 e 10

# random - exemplo 1 - random.randint() -------------------
def numeros_mega_sena():
    mega_sena = []
    while len(mega_sena) < 6:
        numero = ('0' + str(random.randint(1, 60)))[-2:]
        if numero not in mega_sena:
            mega_sena.append(numero)
    return sorted(mega_sena)


quantidade_jogos = 10
for i in range(quantidade_jogos):
    print(numeros_mega_sena())

# random - exemplo 2 - random.choice() --------------------
alunos = ['João', 'Pedro', 'Maria', 'Helena', 'Guilherme']
print('Qual aluno fará a leitura do texto: ', random.choice(alunos))

# random - exemplo 3 - random.sample() --------------------
print('Quais alunos farão a leitura do texto: ', random.sample(alunos, 2))

