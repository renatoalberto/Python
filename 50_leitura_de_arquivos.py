"""
Leitura de Arquivos

Para ler o conteúdo de arquivo em Python, utilizamos a função open().

open()
 - documentação: https://docs.python.org/3/library/functions.html#open

 - na forma mais simples de utilização passamos apenas um parâmetro de entrada, que neste
         caso é o caminho do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper;

 - parâmetros possíveis:
       open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)


OBS: Por padrão, a função open() abre o arquivo para leitura, este arquivo deve existir, ou então
     teremos o erro: FileNotFoundErro

OBS: Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo no disco e nosso programa.
     Essa conexão é chamada de streaming, ao finalizar os trabalhos com esse arquivo devemos chamas a função close()
"""
arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo)         # <_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
print(type(arquivo))   # <class '_io.TextIOWrapper'>

# Para ler TODO o conteúdo do arquivo utilizamos a função read(), que retorna uma string
texto = arquivo.read()
print(type(texto))
print(texto)

# O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor funciona como o cursor
# quando estamos escrevendo. Após a primeira leitura o cursor é posicionado no fim do arquivo, não tendo mais
# nada a imprimir.
print(arquivo.read())

# podemos limitar a quantidade de caracteres impressos com a função read() ------------------------
arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo.read(30))  # imprima somente 30 caracteres
print(arquivo.read())    # imprima o restante
