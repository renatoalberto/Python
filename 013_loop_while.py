"""
Loop While

Forma Geral:
while expressão booleana
    //execução do loop

Loop while executa enquanto expressão booleana for verdadeira
"""
numero = 10

while numero > 0:
    print(f'{numero}', end=' ')
    numero -= 1           # Em um loop while, é importante cuidar do critério de parada para não causar loop infinito
print('')

# ----------------------------------------------------------------------------------------------------------------------

resposta = ''

while resposta != 'Sim':
    resposta = (input('Já lavou o pé Jessica? ')).title()

# ----------------------------------------------------------------------------------------------------------------------

# Não existe o comando do while como em javascript
