"""
Tuplas (tuple)
- São bastantes parecidas com lista, com 2 diferenças básicas:
    1 - São representadas por parênteses ()
    2 - São imutáveis, não mudam, toda alteração de uma tupla, gera uma nova tupla

- Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados em uma coleção
- Tuplas são mais rápidas que listas
- Tuplas deixam seu código mais seguro, elementos imutáveis traz segurança para o código
"""
# Criação de tuplas -------------------------------------------------------------------------------
tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
print(f'tupla1 - {tupla1}. tipo da tupla1 - {type(tupla1)}.')
print(f'tupla2 - {tupla2}. tipo da tupla2 - {type(tupla2)}.')

# Atenção para criação de tuplas com 1 elemento - SÃO DEFINIDAS PELA VÍRGULA, não pelo parênteses -
tupla3 = (7)   # Isso NÃO é uma tupla
print(f'tupla3 - {tupla3}. tipo da tupla3 - {type(tupla3)}. *** NÃO GEROU UMA TUPLA')
tupla3 = (7,)  # Isso é uma tupla
print(f'tupla3 - {tupla3}. tipo da tupla3 - {type(tupla3)}.')
tupla3 = 7,    # Isso é uma tupla
print(f'tupla3 - {tupla3}. tipo da tupla3 - {type(tupla3)}.')

# Gerando tupla dinamicamente com range -----------------------------------------------------------
tupla4 = tuple(range(11))
print(f'tupla4 - {tupla4}. tipo da tupla4 - {type(tupla4)}.')

# Gerando tupla a partir de uma string ------------------------------------------------------------
escola = tuple('Geek University')
print(escola)

# Desempacotamento de tupla -----------------------------------------------------------------------
tupla5 = ('Geek University', 'Programação em Python Essencial')
escola, curso = tupla5
print(f'tupla5 - {tupla5}. tipo da tupla5 - {type(tupla5)}.')
print(f'Desempacotamento tupla5. Escola - {escola}. Curso - {curso}')

# Adição e Remoção não existem, dado o fato de serem imutáveis ------------------------------------

# Soma, Valor Máximo, Valor Mínimo, Quantidade de Elementos - para valores numéricos --------------
tupla6 = tuple(range(9))
print(f'tupla6 - {tupla6}. tipo da tupla6 - {type(tupla6)}.')
print(f'tupla6. Máximo - {max(tupla6)}, Mínimo - {min(tupla6)}, Soma - {sum(tupla6)}. Quantidade - {len(tupla6)}.')

# Concatenação de tuplas --------------------------------------------------------------------------
tupla7 = tuple(range(1, 4))
tupla8 = tuple(range(5, 9))
tupla9 = tupla7 + tupla8
print(f'tupla7 - {tupla7}')
print(f'tupla8 - {tupla8}')
print(f'tupla9 - {tupla9}')
print(f'Soma tupla7 + tupla8 - {tupla7 + tupla8}')

# Tuplas são imutáveis mas é permitido sobrescreve-lo ---------------------------------------------
tupla7 = tupla7 + tupla8
print(f'tupla7 foi sobrescrita - {tupla7}')

# Verificar se determinado elemento está contido na tupla -----------------------------------------
print(f'Número 3 está contido na tupla7? {3 in tupla7}')
print(f'Número 4 está contido na tupla7? {4 in tupla7}')

# Iterando uma tupla ------------------------------------------------------------------------------
for numero in tupla7:
    print(numero, end=", ")
print()

for indice, valor in enumerate(tupla7):
    print(f'Índice: {indice} - Valor: {valor}', end=' | ')
print()

# Quantidade de um determinado elemento em uma tupla ----------------------------------------------
tupla10 = ('a', 'b', 'c', 'a', 'r', 'n', 'g', 'a')
print(f"Na tupla {tupla10} e elemento 'a' se repete {tupla10.count('a')} vezes.")

# É permitido acessar um elemento a partir do seu índice ------------------------------------------
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(f'Mês 7 - {meses[7]}')

# Qual o índice de um elemento --------------------------------------------------------------------
print(f'Qual o índice do mês de Julho - {meses.index("Julho")}')

# Slicing - tupla[início:fim:passo] ---------------------------------------------------------------
print(f'A partir do índice 1 até 9 de 2 em 2 - {meses[1:9:2]}')


