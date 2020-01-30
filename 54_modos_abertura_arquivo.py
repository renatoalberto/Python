"""
Modos de Abertura de Arquivo:

'r' - abre para leitura (padrão)
'w' - abre para escrita, sobrescreve o arquivo anterior existente
'x' - abre para escrita, falhando se o arquivo já existir (FileExistsError)
'a' - abre para escrita, adicionando no SEMPRE ao final do arquivo, caso existir

'b' - modo binário
't' - modo de texto (padrão)
'+' - aberto para atualização (leitura e escrita)
"""
# Mode 'x' de abertura de arquivo -----------------------------------------------------------------
# Executa a primeira vez criando o arquivo
try:
    with open('text5.txt', 'x') as arquivo:
        arquivo.write('arquivo criado na aula 54_modos_abertura_arquivo.py\n')
except FileExistsError:
    print('Arquivo já existente')
else:
    print('Realizou a gravação com sucesso.')

# Falha na segunda, pois arquivo já existente - FileExistsError
try:
    with open('text5.txt', 'x') as arquivo:
        arquivo.write('arquivo criado na aula 54_modos_abertura_arquivo.py\n')
except FileExistsError:
    print('Arquivo já existente')

# Mode 'a' de abertura de arquivo -----------------------------------------------------------------
# Abre para gravação SEMPRE ao final do arquivo, não é possível controlar o cursor com seek()
with open('text5.txt', 'a') as arquivo:
    arquivo.write('nova linha adicionada no final ao arquivo.\n')
