"""
Reversed

Obs: Não confunda com a função reverse() que estudamos nas listas, a função reverse() só funciona em listas

Reversed() funciona com qualquer iterável, MENOS CONJUNTOS pois não definimos sua ordem,
           sua função é inverter o iterável

Tem retorno de acordo com tipo de iterável recebido
   - Quando tipo "list"   - retorna uma "list reverse iterator";
   - Quando tipo "tuple"  - retorna um  "reversed";
   - Quando tipo "set"    - NÃO É POSSíVEL, em conjuntos não definimos sua ordem;
   - Quando tipo "string" - retorna um  "reversed".
"""
lista = reversed(list(range(5)))
print(lista)
print(type(lista))  # <class 'list_reverseiterator'>
print(list(lista))

tupla = reversed(tuple(range(5)))
print(tupla)
print(type(tupla))  # <class 'reversed'>
print(tuple(tupla))

conjunto = set(range(5))
# conjunto = reversed(conjunto)  # Em conjuntos não definimos a ordem dos elementos
print(conjunto)
print(type(conjunto))

# Aplicando reversed() sobre uma string -----------------------------------------------------------
curso = reversed('Geek University')
print(curso)
print(type(curso))  # <class 'reversed'>

for letra in curso:
    print(letra, end='')
print()

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Podemos fazer sem o uso do reversed, com slice de string
print('Geek University'[::-1])

# Podemos fazer um loop reverso com reversed() ----------------------------------------------------
for numero in reversed(range(10)):
    print(numero)

# Apesar de ser possível mudar a propriedade do range para reservo
for numero in range(9, -1, -1):  # range(Inicio *contido, Fim *não está contido, Passo)
    print(numero)
