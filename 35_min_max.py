"""
Min e Max

max() - retorna o maior valor de um iterável ou o maior entre dois ou mais elementos
min() - retorna o menor valor de um iterável ou o menor entre dois ou mais elementos

"""
lista = [1, 8, 4, 99, 34, 129]
tupla = (1, 8, 4, 99, 34, 129)
conjunto = {1, 8, 4, 99, 34, 129}
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(max(lista))
print(max(tupla))
print(max(conjunto))
print(max(dicionario))           # retorna o maior índice
print(max(dicionario.values()))  # retorna o maior valor

# Maior entre dois ou três valores ----------------------------------------------------------------
print(f'Maior entre dois - {max(3, 5)}')

# Min() -------------------------------------------------------------------------------------------
print(min(lista))
print(min(tupla))
print(min(conjunto))
print(min(dicionario))           # retorna o menor índice
print(min(dicionario.values()))  # retorna o menor valor

# Menor entre dois ou três valores ----------------------------------------------------------------
print(f'Menor entre dois - {min(3, 5)}')

# Maior e Menor com expressão lambda --------------------------------------------------------------
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))  # Tim
print(min(nomes))  # Arya
print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim

# Maior e Menor com objetos mais complexos --------------------------------------------------------
usuarios = [
    {'username': 'renato', "twitters": ['eu adoro bolo', 'eu adoro pizza'], "likes": 2},
    {'username': 'raissa', "twitters": ['eu adoro chocolate', 'eu adoro brincar'], "likes": 5},
    {'username': 'nick', "twitters": ['eu adoro dormir'], "likes": 4, "seguidores": 10},
    {'username': 'lana', "twitters": ['eu adoro comer'], "likes": 7},
    {'username': 'tati', "twitters": [], "likes": 7},
    {'username': 'karina', "twitters": [], "likes": 2},
    {'username': 'jessica', "twitters": [], "likes": 2}
]

print(max(usuarios, key=lambda usuario: usuario['likes']))  # Imprimindo objeto inteiro
print(min(usuarios, key=lambda usuario: usuario['likes']))  # Imprimindo objeto inteiro

print(max(usuarios, key=lambda usuario: usuario['likes'])['username'])  # Imprimindo somente o username
print(min(usuarios, key=lambda usuario: usuario['likes'])['username'])  # Imprimindo somente o username


# Sem utilizar instruções max() e min() com loops -------------------------------------------------
maiorUsuario = {}
menorUsuario = {}

for usuario in usuarios:
    if len(maiorUsuario) == 0 or maiorUsuario['likes'] < usuario['likes']:
        maiorUsuario = usuario

    if len(menorUsuario) == 0 or menorUsuario['likes'] > usuario['likes']:
        menorUsuario = usuario

print(maiorUsuario)
print(menorUsuario)
