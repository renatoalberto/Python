"""
Assertions (Afirmações/Checagem/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.

Se a expressão for verdadeira retorna None, se for falsa retorna um erro do tipo
AssertionError.

# Obs1: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de erro personalizada.

# Obs2: A palavra 'assert' pode ser usada em qualquer função ou código, não precisa ser
exclusivamente ser nos testes.

ALERTA: cuidado ao utilizar assert:
- Se um programa Python for executado o parâmetro -O, nenhum assertion será validado, ou seja,
  todas as suas validações serão desconsideradas.
- No terminal: python -O 91_testes_assertions.py
"""
# Utilização simples ------------------------------------------------------------------------------
assert 4 == 4
# assert 4 == 2  # AssertionError

# É possível passar um segundo argumento para o assert --------------------------------------------
# assert 4 == 2, '4 não é igual a 2'  # AssertionError: 4 não é igual a 2


# Testando parâmetros de entrada de uma função ----------------------------------------------------
def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(4, 6)
print(ret)  # 10

# ret = soma_numeros_positivos(10, -5)  # AssertionError: Ambos os números precisam ser positivos


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doce',
        'batata-frita',
        'cachorro-quente',
    ], 'A comida precisa ser um fast-food.'

    return f'Eu estou comendo {comida}.'


ret = comer_fast_food('pizza')
print(ret)
# comer_fast_food('churrasco')  # AssertionError: A comida precisa ser um fast-food.
