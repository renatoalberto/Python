""""
Conjuntos - tudo o que faz referência das teorias dos conjuntos em matemática
Documentação - https://docs.python.org/3/library/stdtypes.html#set

- Em Python os conjuntos são chamados de Sets
- Sets não possuem duplicados
- Sets não possuem valores ordenados
- Sets não são indexados
- Armazena elementos hasheado - hash() (Exemplo armazena tupla imutavel, não armazena lista)

Conjuntos são bons para:
- Armazenar elementos, sem se preocupar com a classificação
- Armazenar elementos, sem se preocupar com chaves
- Armazenar elementos, sem duplicações

Referenciados por {}

Diferenças de (Sets - Conjuntos) e (Mapas - Dicionários) em Python
- Um dicionário tem chave e valor, um conjunto tem valor
"""
# Definindo um conjunto ---------------------------------------------------------------------------
# Forma 1 -----------------------------
conj = set({1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7})    # valores repetidos são ignorados

print(conj)
print(type(conj))

# Forma 1 ----------------------------- Mais comum
# deve conter elementos dentro das chaves, chaves vazias é um dicionario
conj = {1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7}         # valores repetidos são ignorados

print(conj)
print(type(conj))

# Outras -------------------------------
conj = set('Geek University')

print(conj)
print(type(conj))

lista = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
conj = set(lista)

print(conj)
print(type(conj))

tupla = (1, 2, 3, 4, 4, 4, 5, 6, 7, 7,)
conj = set(tupla)

print(conj)
print(type(conj))

# Verificando se um elemento está contido no conjunto ---------------------------------------------
print(f'Número 3 está contido no conjunto - {3 in conj}')
print(f'Número 8 está contido no conjunto - {8 in conj}')

# IMPORTANTE - Sem valores duplicados e sem ordem -------------------------------------------------
lista = [99, 3, 70, 5, 60, 7, 40, 9, 7]
print(f'Lista - {lista}')
tupla = (99, 3, 70, 5, 60, 7, 40, 9, 7)
print(f'Tupla - {tupla}')
dicionario = {}.fromkeys(lista, 'dicionário')
print(f'Dicionário - {dicionario}')
conj = {99, 3, 70, 5, 60, 7, 40, 9, 7}
print(f'Conjunto - {conj}')

# Dados misturados --------------------------------------------------------------------------------
conj = set({'Renato', 'Raíssa', 5, True, 7, 4, 9, 'Renato'})

print(conj)
print(type(conj))

# Iterando sobre conjuntos ------------------------------------------------------------------------
for valor in conj:
    print(valor, end=' ')
print()

# Uso interessante de conjuntos -------------------------------------------------------------------
listaVisitantes = ['Brasília', 'São Paulo', 'Rio Grande do Sul', 'Brasília', 'Rio de Janeiro', 'São Paulo', 'Acre']
print(f'Lista de cidades de cada visitante - {listaVisitantes}')
print(f'Quantidade de visitantes - {len(listaVisitantes)}, quantidade de cidades - {len(set(listaVisitantes))}')

# Adicionando elementos ao conjunto ---------------------------------------------------------------
conj = {1, 2, 3}
conj.add(17)
print(conj)

# removendo elemento do conjunto ------------------------------------------------------------------
# Forma 1 -------------------------------
conj.remove(17)    # Gera erro quando elemento não encontrado
print(conj)

# Forma 2 -------------------------------
conj.discard(3)     # NÃO Gera erro quando elemento não encontrado
print(conj)

# Copiando conjuntos ------------------------------------------------------------------------------
conj = {3, 7, 9, 1, 2, 5, 7, 4, 7, 3, 2}

# Forma 1 - Deep Copy ----------
conj2 = conj.copy()           # cria outro conjunto totalmente separado
conj2.add(10)

print(f'conj  - {conj}. possui {len(conj)} elementos.')
print(f'conj2 - {conj2}. possui {len(conj2)} elementos.')
print(f'Posição de memória do conj  - {id(conj)}')
print(f'Posição de memória do conj2 - {id(conj2)}')

# Forma 1 - Shallow Copy -------
conj2 = conj                  # cria uma referência para o mesmo conjunto
conj2.add(10)

print(f'conj  - {conj}. possui {len(conj)} elementos.')
print(f'conj2 - {conj2}. possui {len(conj2)} elementos.')
print(f'Posição de memória do conj  - {id(conj)}')
print(f'Posição de memória do conj2 - {id(conj2)}')

# Remover todos os elementos de um conjunto -------------------------------------------------------
conj.clear()
print(f'Removido todos os elementos do conjunto conj - {conj})')

# Métodos Matemáticos de Conjunto - Importante no Big Data ----------------------------------------
alunos_curso_python = {'Renato', 'Ricardo', 'Théo', 'Pedro', 'Ellen', 'Patrícia'}
alunos_curso_java = {'Raíssa', 'Patrícia', 'Théo', 'Fernando', 'Tati'}

# Em geral os arquivo são gigantes e impossível de saber alunos em comum

# Gerar com conjunto com todos os alunos matriculados
# Forma 1 - union() -------------------------------- Recomendado, mais intuitivo
alunos_matriculado = alunos_curso_java.union(alunos_curso_python)
print(f'Todos os alunos: {alunos_matriculado}. Quantidade: {len(alunos_matriculado)}')

# Forma 2 - caracter | pipe ------------------------
alunos_matriculado = alunos_curso_java | alunos_curso_python
print(f'Todos os alunos: {alunos_matriculado}. Quantidade: {len(alunos_matriculado)}')

# Gerar um conjunto com alunos em ambos os cursos
# Forma 1 - intersection()
alunos_ambos = alunos_curso_java.intersection(alunos_curso_python)
print(f'Alunos em ambos os cursos: {alunos_ambos}. Quantidade: {len(alunos_ambos)}')

# Forma 2 - &
alunos_ambos = alunos_curso_java & alunos_curso_python
print(f'Alunos em ambos os cursos: {alunos_ambos}. Quantidade: {len(alunos_ambos)}')

# Gerar um conjunto com alunos que só fazem um dos curso
# Forma única - difference()
so_python = alunos_curso_python.difference(alunos_curso_java)
so_java = alunos_curso_java.difference(alunos_curso_python)

print(f'Só cursam python - {so_python}')
print(f'Só cursam java - {so_java}')

# Soma, Maior, Menor, Tamanho - Somente números ---------------------------------------------------
conj = set(range(0, 11, 2))
print(f'Conjunto - {conj}')
print(f'Maior valor - {max(conj)}')
print(f'Menos valor - {min(conj)}')
print(f'Soma valores - {sum(conj)}')
print(f'Tamanho do conjunto - {len(conj)}')

