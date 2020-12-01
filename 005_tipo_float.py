"""
Tipo Float - Tipo Real - Tipo Decimal - Com Casas Decimais

O separador de casas decimais é o "." e não a ","
Errado   | Certo
1,44     | 1.44
"""

# Dupla atribuição
numero1, numero2 = 2.5, 7.25
print(f'{numero1} e {numero2}')

numero1 = 0.000005
print(f'Notação científica - {numero1}')  # 5e-06

# Atenção ao truncamento
numero1 = 0.3
numero2 = 0.1 + 0.2
print(f'0.3 == 0.3 - {0.3 == 0.3}')          # True
print(f'0.3 == 0.3 - {numero1 == numero2}')  # False

# para não truncar utilize "round()"
numero1 = 0.3
numero2 = round(0.1 + 0.2, 4)  # com 4 casas decimais
print(f'0.3 == 0.3 - {0.3 == 0.3}')          # True
print(f'0.3 == 0.3 - {numero1 == numero2}')  # True

# Converter um float para int
conversao = int(numero2)
print(type(conversao))

# Variável complexa
complexa = 5j
print(f'{complexa}')
print(type(complexa))
