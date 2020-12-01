"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe da List Comprehension
[ realize a ação para cada valor da lista ]
"""
numeros = list(range(11))

# Multiplique por 10 e grave o resultado da divisão para cada número da lista de números
res = [numero * 10 for numero in numeros]
print(res)

res = [numero / 2 for numero in numeros]
print(res)

# For encadeado
lista = [(linha, coluna) for linha in range(3) for coluna in range(3)]
print(f'For encadeado - {lista}')  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


# Podemos utilizar função -------------------------------------------------------------------------
def quadrado_do_numero(valor):
    return valor * valor


res = [quadrado_do_numero(numero) for numero in numeros]
print(res)


# Mais exemplos: colocando todas as letras em maiúsculo -------------------------------------------
res = [letra.upper() for letra in 'Geek University']
print(res)

# Mais exemplos: colocando a primeira letras em maiúsculo -----------------------------------------
amigos = ['maria', 'juliano', 'fernanda', 'pedro', 'lucas', 'leleco']
res = [f'{amigo[0].upper()}{amigo[1::]}' for amigo in amigos]
print(res)

# Mais exemplo: verificando se valor é considerado falso ou verdadeiro ----------------------------
res = [f'{valor} é {bool(valor)}' for valor in [0, '', [], None, True, 1, 3, 14]]
print(res)

# Mais exemplo: transformando um número em string -------------------------------------------------
res = [str(numero) for numero in range(11)]
print(res)

# podemos adicionar estruturas condicionais lógicas na list comprehension -------------------------
numeros = list(range(16))
pares = [numero for numero in numeros if numero % 2 == 0]  # Com condição
impares = [numero for numero in numeros if numero % 2 == 1]  # Com condição
print(pares)
print(impares)

# refatorando
numeros = list(range(16))
pares = [numero for numero in numeros if not numero % 2]  # zero em python é falso
impares = [numero for numero in numeros if numero % 2]  # Com condição
print(pares)
print(impares)

# podemos também utilizar a estrutura else em list comprehension ----------------------------------
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

