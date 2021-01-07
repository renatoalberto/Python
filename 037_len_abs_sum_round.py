"""
Len, ABS, Sum, Round

# len() - retorna o número de itens de um iterável

# abs() - retorna o valor absoluto de um número inteiro ou real, de forma básica, seria o próprio número sem sinal

# sum() - recebe como parâmetro um iterável e retorna a soma de seus elementos, incluindo "o valor inicial" default zero

# round() - retorna um número arredondado para n dígitos de precisão após a casa decimal. Se precisão não informada
            retorna para o valor par mais próximo
"""
# len() -------------------------------------------------------------------------------------------
print('# len() -------------------------')
print(len('Geek University'))  # quantidade de elementos de uma string
print(len(list(range(10))))    # quantidade de elementos de uma lista
print(len(set(range(10))))     # quantidade de elementos de uma conjunto
print(len({'a': 1, 'b': 2, 'c': 3}))  # quantidade de elementos de um dicionário

# abs() -------------------------------------------------------------------------------------------
print('# abs() -------------------------')
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# sum() -------------------------------------------------------------------------------------------
print('# sum() -------------------------')
print(sum(list(range(5))))     # retorna a soma dos elementos [0, 1, 2, 3, 4]
print(sum(tuple(range(5))))    # retorna a soma dos elementos (0, 1, 2, 3, 4)
print(sum(set(range(5))))      # retorna a soma dos elementos {0, 1, 2, 3, 4}
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))     # retorna a soma dos valores do conjunto

print(sum(range(5), 5))  # retorna a soma dos elementos [0, 1, 2, 3, 4], com valor inicial 5

# Exemplo de utilização, num comércio eletrônico com taxa de frete única de R$5,00
produtos = [15.50, 27.30, 45.15, 30.10, 20.15, 90.35]
print(sum(produtos, 5))  # soma o valor de todos os produtos, somado o valor do frete único

# round() -------------------------------------------------------------------------------------------
print('# round() -------------------------')
print(round(10))     # retorna 10
print(round(10.4))   # retorna 10
print(round(10.5))   # retorna 10
print(round(10.6))   # retorna 11
print(round(1.2121212, 2))   # retorna 1.21
print(round(1.2199999, 2))   # retorna 1.22

# ATENÇÃO - O Python 3 usa uma forma de arredondar chamado de Banker's rounding e
# sempre arredonda para o valor par mais próximo.
print(round(10.5))   # retorna 10
print(round(9.5))    # retorna 10
