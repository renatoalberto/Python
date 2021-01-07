"""
Estruturas condicionais: if, else, elif

Seguem todas as operadores de comparação:
< - menor que
> - maior que
<= - menor ou igual a
>= - maior ou igual a
== - igual a
!= - diferente de
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


# Em uma linha, instrução mais enxuta, condição in line
idade1 = 10
idade2 = 20

mais_novo = idade1 if idade1 < idade2 else idade2

print(f'Mais novo {mais_novo}')  # 10
