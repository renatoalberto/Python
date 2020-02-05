"""
Estruturas condicionais: if, else, elif
"""
idade = 11

if idade < 10:
    print(f'Criança, {idade} anos.')
elif idade < 13:
    print(f'Pré-adolescente, {idade} anos')
elif idade < 18:
    print(f'Adolescente, {idade} anos')
elif idade < 60:
    print(f'Adulto, {idade} anos')
else:
    print(f'Idoso, {idade} anos')
