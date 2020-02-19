"""
Alocação e Gerenciamento de Memória

Código Fonte |              Python                             | Área de Memória
-------------|-------------------------------------------------|-----------------------------------
x = 10       | Reserva área de memória para alocar x           | x=10
y = x        | y apontado para o mesmo local de memória que x  | x,y=10
x += 1       | x reserva nova área de memória                  | y=10 x=11
z = 10       | Inteligentemente z aponta para mesma área de y  | y,z=10 x=11
z = Carro()  | z reserva nova área de memória                  | y=10, x=11, z=Carro

Utilização da Memória Ram:
Momentos     | Código           | Memória Stack                         | Memória Heap
-------------|------------------|---------------------------------------|-----------------------------------
   1ª        | principal():     | y                                     |  y=5
             |     y=5          | z                                     |
             |     z=funcao1(y) |                                       |
-------------|------------------|---------------------------------------|-----------------------------------
   2ª        | principal():     | y                                     |  y=5
             |     y=5          | z                                     |
             |     z=funcao1(y) |                                       |
             |                  |                                       |
             | funcao1(x):      | x                                     |  x=10
             |     x=x*2        | y                                     |
             |     y=funcao2(x) |                                       |
             |     return y     |                                       |
-------------|------------------|---------------------------------------|-----------------------------------
   3ª        | principal():     | y                                     |  y=5
             |     y=5          | z                                     |
             |     z=funcao1(y) |                                       |
             |                  |                                       |
             | funcao1(x):      | x                                     |  x=10
             |     x=x*2        | y                                     |
             |     y=funcao2(x) |                                       |
             |     return y     |                                       |
             |                  |                                       |
             | funcao2(x):      | x                                     |  x=11
             |     x=x+1        |                                       |
             |     return x     |                                       |
-------------|------------------|---------------------------------------|-----------------------------------
   4ª        | principal():     | y                                     |  y=5
             |     y=5          | z                                     |
             |     z=funcao1(y) |                                       |
             |                  |                                       |
             | funcao1(x):      | x                                     |  x=10
             |     x=x*2        | y                                     |  y=11
             |     y=funcao2(x) |                                       |
             |     return y     |                                       |
             |                  |                                       |
-------------|------------------|---------------------------------------|-----------------------------------
   5ª        | principal():     | y                                     |  y=5
             |     y=5          | z                                     |  z=11
             |     z=funcao1(y) |                                       |    10? *dead objects
             |                  |                                       |
-------------|------------------|---------------------------------------|-----------------------------------

Para a limpeza de memória temos o Garbage Collector para limpar dead objects

"""
import sys

# O Python faz uma contagem de quantas referências fazem apontamento a um objeto criado na memória heap
a = []
b = a
print(sys.getrefcount(a))  # retornou 3, que são o 'a', 'b' e a própria 'sys.getrefcount()'

b = None
print(sys.getrefcount(a))  # retornou 2, que são o 'a' e a própria 'sys.getrefcount()'
