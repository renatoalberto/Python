"""
Criando sua própria versão de loop
"""
# Loops comuns ------------------------------------------------------------------------------------
for num in [1, 2, 3, 5, 6, 7]:
    print(f'{num} - ', end='')

print()

for letra in 'Geek University':
    print(f'{letra} - ', end='')

print()


# Loop personalizado ------------------------------------------------------------------------------
# com ponto no final
def meu_for(iterable):
    iterator = iter(iterable)

    try:
        print(f'{next(iterator)}', end='')
    except StopIteration:
        pass

    while True:
        try:
            print(f' - {next(iterator)}', end='')
        except StopIteration:
            print('.')
            break


meu_for('')
meu_for([])
meu_for([1, 2, 3, 5, 6, 7])
meu_for('Geek University')


