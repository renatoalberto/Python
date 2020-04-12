"""
Set Comprehension
"""
# Exemplo 1 ---------------------------------------------------------------------------------------
numeros = {numero for numero in range(1, 7)}
print(numeros)

# Exemplo 2 ---------------------------------------------------------------------------------------
quadrado = {numero ** 2 for numero in range(1, 7)}
print(quadrado)

# Exemplo 3 ---------------------------------------------------------------------------------------
letras = {letra for letra in 'Geek University'}
print(letras)  # Conjuntos não permitem valores duplicados, nem ordenação

