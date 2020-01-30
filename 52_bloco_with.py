"""
O Bloco With

O bloco with é utilizado para criar um contexto de trabalho, onde os recursos utilizados são fechado após o bloco with
"""
# iniciando o contexto with, forma Pythônica de se programar
with open('texto.txt', encoding='UTF-8') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha, end='')

    print(f'Arquivo está fechado dentro do bloco with? {arquivo.closed}')

# Após o término do bloco with o arquivo é fechado
print(f'Arquivo está fechado fora   do bloco with? {arquivo.closed}')
