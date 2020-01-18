"""
Any e All

Any - Retorna True se QUALQUER UM dos elementos do iterável for verdadeiro,  se iterável for vazio retorna False
All - Retorna True se TODOS        os elementos do iterável são verdadeiros, se iterável for vazio retorna True
"""
# Exemplo 1 All -----------------------------------------------------------------------------------
print('************** all() ***************************')
print(all([]))            # Iterável - lista
print(all(()))            # Iterável - tupla
print(all({}))            # Iterável - set
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros?
print(all([0, 1, 2, 3]))  # Todos os números são verdadeiros? - "ZERO no Python é considerados Falso"

# Exemplo 2 All - Strings -------------------------------------------------------------------------
print(all('Renato'))      # String é um iterável no Python

print(all(nome[0] == 'R' for nome in ['Renato', 'Raíssa', 'Rafaela', 'Ronaldo']))  # Expressão lambda - True
print(all(nome[0] == 'R' for nome in ['Renato', 'Raíssa', 'Rafaela', 'Daniela']))  # Expressão lambda - False

print(f'"aeiou" está presente em "aeiou"? - {all(letra in "aeiou" for letra in "aeiou")}')
print(f'"abcde" está presente em "aeiou"? - {all(letra in "abcde" for letra in "aeiou")}')

# Exemplo 3 All -----------------------------------------------------------------------------------
print(f'Cuidado com a lista vazia que retorna True - '
      f'{list((num for num in [2, 4, 6, 8] if num % 2 == 0))} - {all(num for num in [2, 4, 6, 8] if num % 2 == 0)}')

print(f'Cuidado com a lista vazia que retorna True - '
      f'{list((num for num in [1, 3, 5, 7] if num % 2 == 0))} - {all(num for num in [1, 3, 5, 7] if num % 2 == 0)}')


# Exemplo 1 Any -----------------------------------------------------------------------------------
print('************** any() ***************************')
print(any([]))            # Iterável - lista
print(any(()))            # Iterável - tupla
print(any({}))            # Iterável - set
print(any([1, 2, 3, 4]))  # Algum número é verdadeiro?
print(any([0, 1, 2, 3]))  # Algum número é verdadeiro? - "ZERO no Python é considerados Falso"

# Exemplo 2 Any - Strings -------------------------------------------------------------------------
print(f'Renato - {any("Renato")}')      # String é um iterável no Python

print(any(nome[0] == 'R' for nome in ['Renato', 'Raíssa', 'Rafaela', 'Ronaldo']))  # Expressão lambda - True
print(any(nome[0] == 'R' for nome in ['Renato', 'Raíssa', 'Rafaela', 'Daniela']))  # Expressão lambda - False

print(f'Alguma das letras "aeiou" está presente em "aeiou"? - {any(letra in "aeiou" for letra in "aeiou")}')
print(f'Alguma das letras "abcde" está presente em "aeiou"? - {any(letra in "abcde" for letra in "aeiou")}')

# Exemplo 3 Any -----------------------------------------------------------------------------------
print(f'Cuidado com a lista vazia que retorna False - '
      f'{list((num for num in [2, 4, 6, 8] if num % 2 == 0))} - {any(num for num in [2, 4, 6, 8] if num % 2 == 0)}')

print(f'Cuidado com a lista vazia que retorna False - '
      f'{list((num for num in [1, 3, 5, 7] if num % 2 == 0))} - {any(num for num in [1, 3, 5, 7] if num % 2 == 0)}')
