"""
Zip

zip() - Cria um iterável (Zip Object) que agrega cada um dos iteráveis passados como entrada em pares.
      - A partir do objeto zip gerado sempre é possível gerar uma Lista, Tupla ou Dicionário*

* Geração de dicionário a partir de "zip object" somente com 2 iteráveis

- Gera conjunto para índices presentes em todos os iteráveis, os excedentes não serão listado no retorno
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

print(list(zip1))  # Apresentação do iterável gerado
print(list(zip1))  # Após primeira execução o objeto é eliminado

print(list(zip(lista1, lista2, 'abc')))  # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]
print(set(zip(lista1, lista2, 'abc')))   # {(3, 6, 'c'), (2, 5, 'b'), (1, 4, 'a')}
print(dict(zip(lista1, lista2)))         # {1: 4, 2: 5, 3: 6}

# zip com iteráveis de diferentes tamanhos --------------------------------------------------------
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))      # Não apresenta conjunto para os índices sem pares

# podemos utilizar diferentes iteráveis -----------------------------------------------------------
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zip1 = zip(tupla, lista, dicionario.values())
print(list(zip1))

# Lista de tuplas ---------------------------------------------------------------------------------
dados = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
zip1 = zip(*dados)
print(list(zip1))

# Exemplo com alguma complexidade -----------------------------------------------------------------
alunos = ['Pedro', 'João', 'Maria', 'José', 'Antônio']
nota1 = [98, 87, 95, 70, 80]
nota2 = [80, 93, 88, 95, 20]

# Representar cada aluno com sua maior nota
maiorNota = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, nota1, nota2)}  # set comprehension
print(maiorNota)

maiorNota = zip(alunos, map(lambda nota: max(nota), zip(nota1, nota2)))  # utilizado map()
print(dict(maiorNota))
