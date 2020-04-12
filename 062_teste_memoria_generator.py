"""
Teste de memória com generators

# Sequencia de fibonacci
1, 1, 2, 3, 5, 8, 13, 21, 34...
"""

# Função usando listas ----------------------------------------------------------------------------
def fib_lista(max):
    sequencia = []
    a, b = 0, 1

    while len(sequencia) <= max:
        sequencia.append(b)
        a, b = b, a + b

    return sequencia


# Utilizou muito recurso de memória - mais de 400MB
# for num in fib_lista(100000):
#     fibonacci = num

# Função utilizando generator ---------------------------------------------------------------------
def fib_generator(max):
    a, b, contador = 0, 1, 0

    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


# Utilizou menos recurso de memória - 5MB
for num in fib_generator(100000):
    fibonacci = num

print('Fim do fibonacci')