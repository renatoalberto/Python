"""
Módulo Collections - Deque
Documentação: https://docs.python.org/3/library/collections.html#collections.deque

Deque - São listas de alta performance
"""
from collections import deque

# Criando deques ----------------------------------------------------------------------------------
deq = deque('Geek')
print(deq)
print(type(deq))

# Adicionando elementos ---------------------------------------------------------------------------
deq.append('University')
print(deq)

deq.appendleft('Curso: ')
print(deq)

# Removendo elementos -----------------------------------------------------------------------------
print(f'Removendo o último elemento - {deq.pop()}')
print(deq)

print(f'Removendo o primeiro elemento - {deq.popleft()}')
print(deq)
