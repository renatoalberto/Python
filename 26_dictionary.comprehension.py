"""
Dictionary Comprehension

Pense o seguinte:
se quisermos criar uma lista: [1, 2, 3, 4, 5]
Se quisermos criar uma tupla: (1, 2, 3, 4, 5) ou 1, 2, 3, 4, 5
Se quisermos criar um conjunto (set): {1, 2, 3, 4, 5}
Se quisermos criar um dicionário: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Sintaxe:
{chave:valor for chave, valor in iterável}
"""
# Exemplo 1 ---------------------------------------------------------------------------------------
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in dicionario.items()}
print(quadrado)

# Exemplo 2 ---------------------------------------------------------------------------------------
lista = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
quadrado = {valor: valor ** 2 for valor in lista}
print(quadrado)

# Exemplo 3 ---------------------------------------------------------------------------------------
tupla = (1, 2, 3, 4, 5)
quadrado = {valor: valor ** 2 for valor in tupla}
print(quadrado)

# Exemplo 4 ---------------------------------------------------------------------------------------
conjunto = {1, 2, 3, 4, 5}
quadrado = {valor: valor ** 2 for valor in conjunto}
print(quadrado)

# Exemplo 5 ---------------------------------------------------------------------------------------
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com lógica condicional ------------------------------------------------------------------
lista = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
parImpar = {numero: 'Par' if numero % 2 == 0 else 'Impar' for numero in lista}
print(parImpar)
