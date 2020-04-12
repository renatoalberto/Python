"""
Tipo Float - Tipo Real - Tipo Decimal - Com Casas Decimais

O separador de casas decimais é o "." e não a ","
Errado   | Certo
1,44     | 1.44
"""

# Dupla atribuição
numero1, numero2 = 2.5, 7.25
print(f'{numero1} e {numero2}')

# Converter um float para int
conversao = int(numero2)
print(type(conversao))

# Variável complexa
complexa = 5j
print(f'{complexa}')
print(type(complexa))
