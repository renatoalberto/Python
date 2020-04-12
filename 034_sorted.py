"""
Sorted

Obs: Não confunda, apesar do nome, com a função sort() que já estudamos e só funciona em listas

Podemos usar sorted com qualquer iterável.

Como o próprio nome diz serve para ordenar elementos e RETORNA UMA LISTA

Parâmetros:
- Key
- Reverse
"""
# Em lista é possível
lista = [2, 9, 3, 5, 7, 1, 0]
lista.sort()  # Altera a própria lista
print(f'lista - {lista}')

tupla = (2, 9, 3, 5, 7, 1, 0)
# tupla.sort()  # Não é possível
print(f'tupla - {tupla}')

print(f'tupla - {sorted(tupla)}')  # Orderna do menor para o maior e retorna uma lista

conjunto = {2, 9, 3, 5, 7, 1, 0}
# conjunto.sort()  # Não é possível
print(f'conjunto - {conjunto}')

print(f'conjunto - {sorted(conjunto)}')  # Orderna do menor para o maior e retorna uma lista

# Mudando tipo de ordenação para Reversa ----------------------------------------------------------
lista = [2, 9, 3, 5, 7, 1, 0]
print(f'lista - {sorted(lista, reverse=True)}')

# Podemos converter o resultado de lista para outros formatos -------------------------------------
tupla = tuple(sorted(lista))
print(tupla)
conjunto = set(sorted(lista))
print(conjunto)

# Operações complexas -----------------------------------------------------------------------------
usuarios = [
    {'username': 'renato', "twitters": ['eu adoro bolo', 'eu adoro pizza']},
    {'username': 'raissa', "twitters": ['eu adoro chocolate', 'eu adoro brincar']},
    {'username': 'nick', "twitters": ['eu adoro dormir'], "likes": 4, "seguidores": 10},
    {'username': 'lana', "twitters": ['eu adoro comer']},
    {'username': 'tati', "twitters": [], "likes": 7},
    {'username': 'karina', "twitters": []},
    {'username': 'jessica', "twitters": [], "likes": 2}
]

print(usuarios)
print(sorted(usuarios, key=len))  # Classificando por quantidade de chaves

print(sorted(usuarios, key=lambda usuario: usuario['username']))  # classificando por username
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))  # classificando por username inverso

print(sorted(usuarios, key=lambda usuario: len(usuario['twitters'])))  # classificando por quantidade de twitters
print(sorted(usuarios, key=lambda usuario: len(usuario['twitters']), reverse=True))  # Quantidade de twitters inverso

