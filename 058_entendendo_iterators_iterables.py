"""
Entendendo Iterators e Iterables

Iterator:
 - Um objeto que pode ser iterado;
 - Um objeto que retorna um dado, sendo um elemento por vez quando a função next() é chamada.

Iterable:
 - Um objeto que retorna-rá um iterator quando a função iter() for chamada.
"""
# Iterable, pois retornam um iterator:
nome = 'Geek'
numeros = [1, 2, 3, 4, 5, 6, 7]

# A partir do iterable é possível gerar um iterator com a função iter()
it1 = iter(nome)
it2 = iter(numeros)

# A partir do iterator é possível passar por seus elementos com a função next()
# G - e - e - k
print(f'{next(it1)} - {next(it1)} - {next(it1)} - {next(it1)}')

# 1 - 2 - 3 - 4 - 5 - 6 - 7
print(f'{next(it2)} - {next(it2)} - {next(it2)} - {next(it2)} - {next(it2)} - {next(it2)} - {next(it2)}')
