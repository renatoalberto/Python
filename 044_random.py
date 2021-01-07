"""
Módulo Random e o que são módulos?

- Em Python módulos são nada mais do que outros arquivos Python

Módulo Random - possui várias funções para geração de números pseudo-aleatórios

- Pseudo-Random
random é um função que, dada a mesma entrada, gerará o mesmo número.
Essa entrada também é chamada de seed (semente, em português).
Entre as chamadas da função random, sempre é utilizado um novo seed.
"""
# Existe duas formas de utilizar um módulo ou função deste ----------------------------------------
# --- Forma 1 --- Importando todo o módulo * Não recomendado
# import random

# Para utilizar a função random(), colocamos o nome do pacote e o nome da função separados por ponto
# print(random.random())

# É possível informar um alias (apelido) para o módulo
# import random as rdm
# print(rdm.random())

# Ao importa o todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficam disponíveis (Ficaram em memória)

# Caso você saiba quais funções você precisa utilizar deste módulo, então este não seria a forma ideal de utilização

# --- Forma 2 ---
# No import a seguir, estamos solicitando somente as funções específicas do módulo random
# É de costume utilizar tuple para importação de várias funções, com quebra de linha
from random import (
    random,
    uniform,
    randint,
    choice,
    shuffle,
    seed,
    randrange
)

# É possvel realizar o importe de todos as funções do módulo
# from random import *

# É possível informar um alias (apelido) para função
# from random import randint as rdi, random as rdm

# random() ----------------------------------------------------------------------------------------
# Gera um número aleatório entre 0 e 1
print(f'random() - {random()}')

# uniform() ---------------------------------------------------------------------------------------
# Gera um número real pseudo-aleatório entre os valores estabelecidos
print('uniform(3, 7)', end=' ')
for n in range(5):
    print(f'{uniform(3, 7)}', end=', ')  # números aleatório entre (3 - contido) e (7 - não contido)
print()

# randint() ---------------------------------------------------------------------------------------
# Gera um número inteiro pseudo-aleatório entre os valores estabelecidos
print(f'randint(1, 60) - ', end=' ')
for n in range(6):
    print(f'{randint(3, 60)}', end=', ')  # números aleatório entre (3 - contido) e (60 - contido)
print()

# choice() ----------------------------------------------------------------------------------------
# Mostra um valor aleatório entre u iterável
jogadas = ['pedra', 'papel', 'tesoura']
print(f'choice(["pedra", "papel", "tesoura"]) - {choice(jogadas)}')

# shuffle() ---------------------------------------------------------------------------------------
# Função de embaralhar cartas
cartas = ['k', 'q', 'j', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
shuffle(cartas)  # Aqui o shuffler modifica a própria lista de cartas
print(f'shuffle(cartas) - {cartas}')

# Usando seed() para demonstrar que dada a mesma entrada, gerará o mesmo número. ------------------
# Função randrange() para gerar um número aleatório entre 1 e 100.
# Antes do randrange podemos chamar o seed para definir a entrada:
seed(100)
print(f'Passando seed(100) temos o resultado - {randrange(1, 101)}')
seed(100)
print(f'Passando seed(100) temos o resultado - {randrange(1, 101)}')
