""""
Listas (list)
- funcionam como vetores/matrizes (arrays), com a diferença de serem DINÂMICOS e
  também permitir colocar QUALQUER tipo de dado.

Dinâmico: Porque não possui tamanho fixo, podemos criar a lista e simplesmente ir acrescentando valores.
Qualquer tipo de dado: Não possuem tipos de dado fixo.

Lista em Python são representados por colchetes []
São mutáveis
"""
from random import random

lista1 = [1, 99, 25, 43, 70, 35, 77, 23, 17, 43, 60]
lista2 = ['r', 't', 'u', 'p', 'i', 'v', 'm', 'z']
lista3 = list(range(1, 11))
lista4 = []
lista5 = list('Geek University')

#  Podemos saber quantidade de elementos dentro da lista ------------------------------------------
print(f'Quantidade de elementos da lista1 - {len(lista1)}')

#  Podemos facilmente checar se um determinado valor está contido na lista ------------------------
valorPesquisado = int(input('Qual valor deseja procurar? '))
if valorPesquisado in lista1:
    print(f'Valor {valorPesquisado} encontrado na lista1.')
else:
    print(f'Valor {valorPesquisado} não está contido na lista1.')

# Podemos facilmente ORDENAR uma lista ------------------------------------------------------------
lista1.sort()
print(lista1)

# Podemos facilmente contar o NÚMERO DE OCORRÊNCIAS de uma lista ----------------------------------
print(f"{lista5} possui {lista5.count('e')} letras 'e'.")

# Podemos ADICIONAR elementos na lista "ao final" -------------------------------------------------
lista1.append(2)
print(f'Lista1 agora possui o número 2 - {lista1}')         # append - "um por vez"

lista1.append([3, 4, 5, 6])
print(f'Criou uma sublista - {lista1}')                     # append - "dessa forma cria uma sublista"

lista1.extend([3, 4, 5, 6])
print(f'Vários elementos adicionados a lista1 - {lista1}')  # extend - "vários por vez"

# Podemos inserir um elemento informando qual a posição -------------------------------------------
lista1.insert(3, 2)  # (posição, valor)
print(f'Número dois inserido na posição 3 - {lista1}')

# Podemos facilmente juntar as duas listas ( ou somando ou utilizando extend) ---------------------
lista1 = lista1 + lista5
print(lista1)

lista6 = []
lista6.extend(lista1)
print(lista6)

# Podemos inverter as posições do array -----------------------------------------------------------
lista1.reverse()       # Forma 1 - com reverse()
print(lista1)

print(lista5[::-1])    # Forma 2 - slice - modo pythônico

# Podemos copiar uma lista ------------------------------------------------------------------------
lista7 = lista6.copy()
print(lista7)

# Podemos REMOVER ELEMENTO de uma lista -----------------------------------------------------------
valorExcluido = lista7.pop()      # pop() - remove o ÚLTIMO ELEMENTO e também o retorna
print(f'{valorExcluido} excluído da lista7 - {lista7}')

valorExcluido = lista7.pop(2)     # pop(índice) - remove o elemento do índice informado, deslocando para a esquerda
print(f'{valorExcluido} excluído da lista7 - {lista7}')

# Se não existir o índice no array será retornado erro

# Podemos zerar a lista ---------------------------------------------------------------------------
lista7.clear()
print(f'lista7 vazia - {lista7}')

# Para repetir o conteúdo de uma lista ------------------------------------------------------------
lista7 = [1, 2, 3]
lista7 = lista7 * 3
print(f'O conteúdo foi repetido 3x - {lista7}')

# Converter uma STRING EM LISTA -------------------------------------------------------------------
# Forma 1 - Padrão
curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()  # Padrão separa palavras pelo espaço
print(curso)

# Forma 2 - Informando qual é o separador
curso = 'Programação_em_Python_Essencial'
print(curso)
curso = curso.split('_')
print(curso)

# Converter uma LISTA EM STRING -------------------------------------------------------------------
curso = ' '.join(curso)  # monta uma string inserindo espaço entre os elementos
print(curso)

# ITERANDO SOBRE LISTA ----------------------------------------------------------------------------
# usando while
carrinho = []
produto = ''
while produto != 'sair':
    produto = input('Informe o produto desejado (para finalizar informe "sair"): ')
    if produto != 'sair':
        carrinho.append(produto)
# usando for
for elemento in carrinho:
    print(elemento)

# Acessando um índice de forma inversa ------------------------------------------------------------
print(f'{lista3}, acessando o último elemento utilizando -1: {lista3[-1]}')  # Pense no índice como um círculo

# Listar índices de uma lista ---------------------------------------------------------------------
cores = ['amarelo', 'verde', 'azul', 'preto', 'branco']
for indice, cor in enumerate(cores):   # enumerate() gera tupla (índice, valor)
    print(f'{indice} - {cor}')

# Encontrar o índice de um valor ------------------------------------------------------------------
# index apresenta erro caso não encontre o valor
print(f'Para a lista {lista3}, mostre o índice do valor 8 - {lista3.index(8)}')
print(f'Para a lista {lista7}, mostre o índice do valor 3 a partir da posição 6 - Índice {lista7.index(3,6)}')
print(f'Para a lista {lista7}, mostre o índice do valor 3 entre índices 3 e 7 - Índice {lista7.index(3,3,7)}')

# Trabalhando slicing -----------------------------------------------------------------------------
# lista(início:fim:passo)
# range(início:fim:range)
print(f'Para a lista {lista3}, mostre todos os elementos a partir do índice 1 - {lista3[1:]}')
print(f'Para a lista {lista3}, mostre todos os elementos até o índice 2 - {lista3[:2]}')
print(f'Para a lista {lista3}, mostre todos os elementos do índice 2 até 7 - {lista3[2:7]}')
print(f'Para a lista {lista3}, mostre todos os elementos de 2 em 2 - {lista3[::2]}')
print(f'Para a lista {lista3}, mostre todos os elementos a partir do índice 2 de 2 em 2 - {lista3[2::2]}')

# INVERTENDO VALORES sem variável auxiliar ---------------------------------------------------------
lista3[0], lista3[1] = lista3[1], lista3[0]
print(f'Posições 0 e 1 foram invertidas sem uso de variável auxiliar {lista3}')

# Pesquisa MAIOR VALOR*, MENOR VALOR*, SOMA* e TAMANHO --------------------------------------------
# *Somente para valores numéricos
print(f'Para a lista {lista3}, mostre o maior valor - {max(lista3)}')
print(f'Para a lista {lista3}, mostre o menor valor - {min(lista3)}')
print(f'Para a lista {lista3}, mostre a soma de todos os valores - {sum(lista3)}')
print(f'Para a lista {lista3}, mostre o tamanho da lista - {len(lista3)}')

# Desempacotamento de lista -----------------------------------------------------------------------
# Se quantidade de variáveis diferente da quantidade de elementos da lista vai gerar um erro
cor1, cor2, cor3, cor4, cor5 = cores
print(f'Da lista {cores}, desempacotamento cor1 da {cor1}')
print(f'Da lista {cores}, desempacotamento cor2 da {cor2}')
print(f'Da lista {cores}, desempacotamento cor3 da {cor3}')
print(f'Da lista {cores}, desempacotamento cor4 da {cor4}')
print(f'Da lista {cores}, desempacotamento cor5 da {cor5}')

# Copiando uma lista - (Shallow Copy - Deep Copy) -------------------------------------------------
# Forma 1
lista = list(range(11))
nova = lista.copy()                # gera outra lista independente (Deep Copy - Cópia Profunda)
nova.append(11)                    # Não altera lista original
print(f'Lista original {lista}')
print(f'Lista nova {nova}')

# Forma 2
lista = list(range(11))
nova = lista                       # gera uma copia espelho (Shallow Copy - Cópia Rasa)  *IMPORTANTE
nova.append(11)                    # Altera lista original
print(f'Lista original {lista}')
print(f'Lista nova {nova}')

# Lista aninhadas - Nested Lists ------------------------------------------------------------------
"""
Algumas linguagens de programação possuem estrutura de dados chamadas arrays.
    - Arrays Unidimensionais
    - Arrays Multidimensionais (Matrizes)

Em Python nós temos as listas
"""
# Exemplo 1 ----------
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista)
print(lista[0])
print(lista[2][1])  # 8
print(lista[1][2])  # 6
print(type(lista))

for item in lista:
    for item2 in item:
        print(item2)

# Utilizando List Comprehension
print('List Comprehension')
([[print(valor) for valor in lista_auxiliar] for lista_auxiliar in lista])

# Gerando um tabuleiro 3X3 - Muito Pythonico
tabuleiro = [[f'{linha}x{coluna}' for coluna in range(1, 4)] for linha in range(1, 4)]
print(tabuleiro)

# Gerando um jogo da velha
tabuleiro = [['X' if (round(random(), 2) * 100) % 2 == 0 else 'O' for numero in range(1, 4)] for linha in range(1, 4)]
print(tabuleiro)
