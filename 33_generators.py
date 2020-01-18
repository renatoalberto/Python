"""
Generators Expression

Em aulas anteriores vimos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension

Mas não vimos:
- Tuples Comprehension... porque ela se chamam Generators

Generator tem uma melhor performance em relação ao Comprehension
- Comprehension gera um iterável, array em memória
- Generator executa uma única vez e apaga
"""
from sys import getsizeof

# Vimos -------------------------------------------------------------------------------------------
nomes = ['Carlos', 'Camila', 'Chico', 'Cristina', 'Cassiano', 'Vanessa']

print('List Comprehension')
res = [nome[0] == 'C' for nome in nomes]  # Possui colchete - portanto list comprehension e retorna uma lista
print(res)
print(type(res))
print(tuple(res))
print(tuple(res))

# Poderiamos ter feito com Comprehension
print('Generator')
res = (nome[0] == 'C' for nome in nomes)   # Generators NÃO retorna uma tupla
print(res)
print(type(res))
print(tuple(res))
print(tuple(res))  # Assim como MAP e FILTER, após utilizar é apagado da memória

# --------------------------------------------------------------------------------------------------
# getsizeof - retorna a quantidade de memória do elemento passado por parâmetro
print(f'getsizeof("Geek")               - {getsizeof("Geek")}')
print(f'getsizeof("University")         - {getsizeof("University")}')
print(f'getsizeof("9")                  - {getsizeof("9")}')
print(f'getsizeof("91")                 - {getsizeof("91")}')
print(f'getsizeof("646234875687623458") - {getsizeof("646234875687623458")}')
print(f'getsizeof("True")               - {getsizeof("True")}')

# Analisando uma lista de números com Comprehension comparado a Generators
print(f'getsizeof(list)                 - {getsizeof( [x * 10 for x in range(1000)]    )}')
print(f'getsizeof(set)                  - {getsizeof( {x * 10 for x in range(1000)}    )}')
print(f'getsizeof(dictionary)           - {getsizeof( {x: x * 10 for x in range(1000)} )}')
print(f'getsizeof(generator)            - {getsizeof( (x * 10 for x in range(1000))    )}')

# Iterando em um Generator Expression -------------------------------------------------------------
gen = (num for num in range(20))
for num in gen:
    print(f'Iterando - {num}')

