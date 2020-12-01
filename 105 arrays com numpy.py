# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:11:28 2020

@author: renato

Instalaçao          -  pip install numpy
no jupyter notebook - !pip install numpy
"""

import numpy as np

# Criando primeiro array numpy
data = np.array([2, 4, 6, 8, 10])

print(data)          # [ 2  4  6  8 10]
print(type(data))    # <class 'numpy.ndarray'>
print(data.shape)    # (5,)

# Verificação do tipo do array numpy
print(data.dtype)    # int32

# Criando array informando quantidade de elementos
data = np.arange(15)

print(data)          # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

# Criando array numpy de dados aleatórios do tipo float
data = np.random.rand(15)

print(data)          # [0.69531653 0.87180345 0.47954523 0.77264841 0.10714715 0.7376156 ...]

# Criando array numpy de dados aleatórios entre 0 e 10 do tipo int
data = np.random.randint(10, size = 10)

print(data)          # [6 2 2 0 7 2 6 2 7 2]

# Criando matriz 2X2 numpy de dados aleatórios tipo float
data = np.random.random((2, 2))

print(data)          # [[0.80593173 0.32968955] [0.43540867 0.65546819]]

# Criando matriz 3x4 numpy de valores zeros
data = np.zeros((3, 4))

print(data)          # [[0. 0. 0. 0.] [0. 0. 0. 0.]  [0. 0. 0. 0.]]

# Criando matriz 3x4 numpy de valores Uns
data = np.ones((3, 4))

print(data)          # [[1. 1. 1. 1.] [1. 1. 1. 1.] [1. 1. 1. 1.]]

# Criando matriz 3x4 numpy de valores informado
data = np.full((3, 4), 3.14)

print(data)          # [[3.14 3.14 3.14 3.14] [3.14 3.14 3.14 3.14] [3.14 3.14 3.14 3.14]]

# Criando matriz 3x4 numpy de espaços vazios
data = np.empty((3, 4))

print(data)          # retorno array com lixo de memória, vantagem de ser muito rápida

# Criando matriz 3x4 numpy de valores negativos
data = np.arange(10) * -1

print(data)          # [ 0 -1 -2 -3 -4 -5 -6 -7 -8 -9]

# Criando array com tamanho predefinido em variável
tamanho = 6
data = np.random.permutation(tamanho)

print(data)          # [2 4 5 0 3 1]

# Criando array tridimensional com tamanho 5 camadas, 3 linhas, 4 colunas
data = np.random.randint(5, size = (5, 3, 4))

print(data)          

"""
retorno do print:
    
[[[4 2 2 4]
  [2 4 0 4]
  [4 1 0 3]]

 [[4 2 4 2]
  [4 4 0 1]
  [1 0 1 2]]

 [[3 4 2 2]
  [3 4 4 2]
  [0 2 0 1]]

 [[3 4 0 1]
  [1 2 4 2]
  [4 1 4 1]]

 [[1 0 2 4]
  [3 3 1 3]
  [0 0 2 0]]]

"""

# Reutilizando a matriz tridimensional criada anteriormente podemos realizar as
# consultas a seguir:
print(f'Número de dimensões                  - {data.ndim}')     # Número de dimensões                  - 3
print(f'Formato da matriz                    - {data.shape}')    # Formato da matriz                    - (5, 3, 4)
print(f'Tamanho total da matriz              - {data.size}')     # Tamanho total da matriz              - 60
print(f'Tamanho de cada elemento em em bytes - {data.itemsize}') # Tamanho em bytes                     - 4
print(f'Tamanho de toda a matriz em bytes    - {data.nbytes}')   # Tamanho de toda a matriz em bytes    - 240
print(f'Qual o valor do maior elemento       - {data.max()}')    # Qual o valor do maior elemento       - 4
print(f'Qual o valor contido no índ [2,3,4]  - {data[2,2,3]}')   # Qual o valor contido no índ [2,3,4]  - 1


# Convertendo array multidimensional para unidimensional
data = np.array([[2,4,6,8], [1,3,5,7]])

data = data.flatten()

print(data)          # [2 4 6 8 1 3 5 7]

# Consultando elementos dentro de um intervalo
data = np.arange(15)    # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(f'Os 5 primeiros elementos         - {data[:5]}')  # Os 5 primeiros elementos         - [0 1 2 3 4]
print(f'Do 3ª elemento até o fim         - {data[3:]}')  # Do 3ª elemento até o fim         - [ 3  4  5  6  7  8  9 10 11 12 13 14]
print(f'Do 4ª contido até 8ª não contido - {data[4:8]}') # Do 4ª contido até 8ª não contido - [4 5 6 7]
print(f'Todos os elementos de 2 em 2     - {data[::2]}') # Todos os elementos de 2 em 2     - [ 0  2  4  6  8 10 12 14]


# Atribuindo um valor float para um array numpy int 
data[1] = 6.58745
print(f'O valor é convertido para int - {data[1]}')  # O valor é convertido para int - 6
print(type(data[1]))                                 # Array definido como int - <class 'numpy.int32'>


# Convertendo o array para float
data = np.array(data, dtype='float')
print(type(data[1]))                                 # Array alterado para float - <class 'numpy.float64'>

data[1] = 6.58745
print(f'O valor float é mantido - {data[1]}')        # O valor float é mantido - 6.58745


# Criando um array com números uniformemente distribuidos
data = np.linspace(0,1,7)   # Array de 7 elementos igualmente distribuidos entre 0 e 1
print(data) # [0.         0.16666667 0.33333333 0.5        0.66666667 0.83333333  1.        ]


# Alterando o formato do array 
data = np.arange(8)         # Temos um array unidimensional de 8 elementos ordenados
data = data.reshape(2, 4)   # Array redimensionado para 2 linhas e 4 colunas
print(data)                 # [[0 1 2 3] [4 5 6 7]]


# Realizando operações lógicas
data = np.arange(10)
print(data > 5)             # [False False False False False False  True  True  True  True]

# Realizando operações aritiméticas. Diferentemente de limples lista o operador
# + tentaria fazer uma concatenação, em um array numpy é atribuido o valor a cada elemento
data = np.arange(8)
print(data + 10)            # [10 11 12 13 14 15 16 17]


# Para casos específicos podemos criar uma matriz diagonal
data = np.arange(8)
data = np.diag(data)
print(data)

"""
Resultado do print resultante da função diag()
[[0 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0]
 [0 0 2 0 0 0 0 0]
 [0 0 0 3 0 0 0 0]
 [0 0 0 0 4 0 0 0]
 [0 0 0 0 0 5 0 0]
 [0 0 0 0 0 0 6 0]
 [0 0 0 0 0 0 0 7]]
"""

# Outro tipo de matriz diagonal contendo zeros e uns
data = np.eye(4)
print(data)

"""
Resultado da função eye()
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
"""

# Duplicando padrões *somente linha
data = np.tile(np.array([[9, 4], [7, 1]]), 4)
print(data)

"""
Resultado da função tile() repetiu as linha 4x
[[9 4 9 4 9 4 9 4]
 [7 1 7 1 7 1 7 1]]
"""

# Duplicando padrões *linhas e colunas - sem sobrepor a ordem original dos elementos.
data = np.tile(np.array([[9, 4], [7, 1]]), (2,3))
print(data)

"""
Resultado da função tile() repetiu as linha 2x e colunas 3x
[[9 4 9 4 9 4]
 [7 1 7 1 7 1]
 [9 4 9 4 9 4]
 [7 1 7 1 7 1]]
"""


# Soma de arrays com mesmo formato e tamanho
data1 = np.arange(10)       # [0 1 2 3 4 5 6 7 8 9]
data2 = np.arange(10) + 5   # [ 5  6  7  8  9 10 11 12 13 14]

data = data1 + data2
print(data)                 # [ 5  7  9 11 13 15 17 19 21 23]


# Subtração de arrays com mesmo formato e tamanho
data = data2 - data1
print(data)                 # [5 5 5 5 5 5 5 5 5 5]


# Divisão
data1 = np.array([3, 6, 9, 12, 15])
data2 = np.array([1, 2, 3, 4, 5])

data = data1 / data2

print(data)                 # [3. 3. 3. 3. 3.]

# Multiplicação
data = data1 * data2
print(data)                 # [ 3 12 27 48 75]   


# Realizando operações lógicas entre arrays
data1 = np.array([3, 6, 9, 12, 15, 18, 21])
data2 = np.array([1, 2, 3, 4, 5, 20, 25])

data = data1 > data2

print(data)                 # [ True  True  True  True  True False False]


# Realizando transposição de matriz, transformando linhas em colunas e vice versa
data = np.array([[1, 2, 3], [4, 5, 6]])
print(data.shape)           # (2, 3)

data = data.transpose()
print(data.shape)           # (3, 2)

print(data)

"""
Resultado da matris gerada pelo transpose()
[[1 4]
 [2 5]
 [3 6]]
"""

# Salvando um array numpy em disco
np.save('Meu Array Numpy', data)

# Lendo o array salvo em disco
data2 = np.load('Meu Array Numpy.npy')



