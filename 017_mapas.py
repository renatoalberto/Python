"""
Mapas - Conhecidos em Python por Dicionários, representados por {}
"""
receita = {'Jan': 100, 'Fev': 120, 'Mar': 150, 'Abr': 175}

# Iterando sobre dicionários ----------------------------------------------------------------------
for chave in receita:
    print(f'{chave} - {receita[chave]}  |  ',  end=' ')
print()

# Iterando sobre as chaves do dicionário ----------------------------------------------------------
print(receita.keys())

for chave in receita.keys():                               # recomendado
    print(f'{chave} - {receita[chave]}  |  ',  end=' ')
print()

# Iterando sobre os valores do dicionário ----------------------------------------------------------
print(receita.values())

for valores in receita.values():                           # recomendado
    print(valores, end=' ')
print()

# Desempacotamento de dicionários -----------------------------------------------------------------
for chave, valor in receita.items():
    print(f'{chave} - {valor}  |  ', end=' ')
print()

# Valores máximo, mínimo, soma e tamanho ----------------------------------------------------------
print(f'Soma do valores - {sum(receita.values())}')
print(f'Valor máximo    - {max(receita.values())}')
print(f'Valor Mínimo    - {min(receita.values())}')
print(f'Tamanho do dic. - {len(receita.values())}')
