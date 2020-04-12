"""
Teste de velocidade com expressões geradoras
"""
import time


# Relembrando conceitos ( Generator X Generator Expression)
# Generators (geradores)
def numeros(ini, fim):
    while ini < fim:
        yield ini
        ini += 1


gen1 = numeros(1, 10)
print(gen1)        # <generator object numeros>
print(type(gen1))  # <class 'generator'>

while True:
    try:
        print(next(gen1), end=' ')
    except StopIteration:
        print('')
        break


# Generator Expression
gen2 = (num for num in numeros(1, 10))

print(gen2)        # <generator object <genexpr>>
print(type(gen2))  # <class 'generator'>

while True:
    try:
        print(next(gen2), end=' ')
    except StopIteration:
        print('')
        break

# Teste Tempo de processamento --------------------------------------------------------------------
# performance com generators
gen_inicio = time.time()
print(sum((num for num in range(10000000))))  # 10 milhões
gen_tempo_total = time.time() - gen_inicio

# performance com list comprehension
list_inicio = time.time()
print(sum([num for num in range(10000000)]))  # 10 milhões
list_tempo_total = time.time() - list_inicio

print(f'Generators Expression levou {gen_tempo_total}')
print(f'List Comprehension    levou {list_tempo_total}')

# Conclusão pessoal:
# - Generators para pequeno volume de dados perde para List Comprehension.
# - List Comprehension para alto volume de dados nem roda - MemoryError, ocupando todo a memória disponível
