"""
Seek e Cursors

seek() -> é utilizado para movimentar o cursor pelo arquivo
       -> recebe um parâmetro que indica onde queremos posicionar o cursor

OBS: Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo no disco e nosso programa.
     Essa conexão é chamada de streaming, ao finalizar os trabalhos com esse arquivo devemos chamas a função close()
"""
arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo.read())
print(arquivo.read())  # Aqui não imprime nada porque o cursor está parado no fim do arquivo

# movimentando o cursor com a função seek() -------------------------------------------------------
arquivo.seek(0)
print(arquivo.read())  # aqui foi possível imprimir todo o texto

arquivo.seek(40)
print(arquivo.read())  # aqui foi possível imprimir todo o texto

# função readline() retorna uma string e lê o arquivo linha a linha -------------------------------
arquivo.seek(0)
print(f'linha 1 - {arquivo.readline()}')
print(f'linha 2 = {arquivo.readline()}')

# função readlines() retorna uma lista de string --------------------------------------------------
arquivo.seek(0)
linhas = arquivo.readlines()
print(f'Quantidade de linha {len(linhas)}')
print(f'linha 1 - {linhas[0]}')
print(f'linha 2 = {linhas[1]}')

# Verifica se arquivo está fechado com o atributo closed ------------------------------------------
print(f'Arquivo está fechado? {arquivo.closed}')

# ao termino da utilização do arquivo, devemos fechar o arquivo com close() -----------------------
arquivo.close()

# Verifica se arquivo está fechado
print(f'Arquivo está fechado? {arquivo.closed}')
