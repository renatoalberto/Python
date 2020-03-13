"""
Loop For - Estrutura de Repetição

Exemplo de iteráveis:
- Strings
- Lista
- Range
"""
umaString = 'Renato'
for letra in umaString:
    print(letra)

# -------------------------------------------------------------------------------------------------
umaLista = ['Renato', 'Raíssa', 'Nick', 'Lana']
for item in umaLista:
    print(item)

    if item == 'Raíssa':
        break              # break utilizado para sair do loop de maneira projetada

# -------------------------------------------------------------------------------------------------
umRange = range(1, 10)
for item in umRange:
    print(item, end=' - ')

print()

# -------------------------------------------------------------------------------------------------
nome = 'Banco do Brasil'
for tupla in enumerate(nome):  # enumerate retorna uma tupla(nome, valor)
    print(f'{tupla} - {tupla[0]} - {tupla[1]}', end=' - ')

print()

for indice, letra in enumerate(nome):
    print(f'{indice}ª - {nome[indice]} ou {letra}', end=' - ')

print()

for _, letra in enumerate(nome):  # quando não precisamos de um valor, descartamos com um '_'
    print(f'{letra}', end=' ')    # end é parâmetro do método print, que por default pula linha end="\n'

