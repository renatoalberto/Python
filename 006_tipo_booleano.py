"""
Tipo booleano

Algebra Booleana, criado por George Boole

2 Constantes - Verdadeiro ou Falso

Obs: Sempre com a primeira letra em maiúsculo (True, False)
"""
ativo = False
print({ativo})
ativo = True
print({ativo})
print(type(ativo))

# Negação
print(f'not True  - {not True}')
print(f'not False - {not False}')

# Qualquer valor será convertida pra True -- MENOS ZERO
print(f'bool de qualquer número positivo - {bool(3.16)}')
print(f'bool de qualquer número negativo - {bool(-3.16)}')
print(f'bool de zero                     - {bool(0)}')
