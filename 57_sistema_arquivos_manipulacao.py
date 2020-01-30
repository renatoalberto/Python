"""
Sistema de Arquivos - Manipulação

Módulo grande, mais detalhes na documentação
documentação: https://docs.python.org/3/library/os.html?module=os
"""
import os

# Descobrindo de um arquivo ou diretório existe ---------------------------------------------------
# Arquivo
print(f'Existe o arquivo texto.txt?  {os.path.exists("texto.txt")}')
print(f'Existe o arquivo frutas.txt? {os.path.exists("frutas.txt")}')

# Diretório, paths relativos
print(f'Existe o diretório pacote?       {os.path.exists("pacote")}')
print(f'Existe o diretório\\geek pacote? {os.path.exists("pacote/geek")}')  # observe a barra
print(f'Existe o diretório outro?        {os.path.exists("outro")}')

# Diretório, paths absolutos
print(f'Existe o diretório C:\\Users\\renat?  {os.path.exists("C:/Users/renat")}')
print(f'Existe o diretório C:\\Users\\raissa? {os.path.exists("C:/Users/raissa")}')

# Criando arquivo ---------------------------------------------------------------------------------
# Forma 1 - sobrescrita
open('text6.txt', 'w').close()

# Forma 2 - escrita a partir da última linha
open('text6.txt', 'a').close()

# Forma 3 - sobrescrita
with open('text6.txt', 'w'):
    pass

# Forma 4 - forma correta
# recursos só estão disponíveis para sistemas operacionais de uso profissional.
# no sistema operacional mac precisa de permissão, pode não funcionar
# se arquivo já existir teremos o erro FileExistsError
# os.mknod('text7.txt')

# Criando diretórios ------------------------------------------------------------------------------
# mkdir() - cria um único diretório
# se diretório já existir teremos o erro FileExistsError
# se não tivermos permissão para criar um diretório teremos um PermissionError
try:
    os.mkdir('templates')
except FileExistsError:
    print('Diretório "templates" já existe')

# makedirs() - cria multi-diretórios
try:
    os.makedirs('templates/geek/university')
except FileExistsError:
    print('Diretório "templates\\geek\\university" já existe')

# parâmetro exists_ok=True - Caso diretório já exista não apresente erro
os.makedirs('templates/geek/university', exist_ok=True)

# Renomear arquivos ou diretórios -----------------------------------------------------------------
# arquivo no diretório atual
try:
    os.rename('text6.txt', 'text6-renomeado.txt')
except FileExistsError:
    print('Arquivo "text6-renomeado.txt" já existe')
except FileNotFoundError:
    print('Arquivo "text6-renomeado.txt" não existe')

# arquivo no diretório profundo
try:
    os.rename('templates/geek/university/texto.txt', 'templates/geek/university/texto-renomeado.txt')
except FileExistsError:
    print('Arquivo "texto.txt" já existe')
except FileNotFoundError:
    print('Arquivo "texto-renomeado.txt" não existe')

# diretório
try:
    os.rename('templates', 'templates-renomeado')
except FileExistsError:
    print('Diretório "templates-renomeado" já existe')
except FileNotFoundError:
    print('Diretório "templates-renomeado" não existe')

# Deletar arquivos --------------------------------------------------------------------------------
# ATENÇÃO - ao deletar arquivos ou diretórios, eles não vão para lixeira
# No windows, caso o arquivo estiver em uso, a deleção retornará um erro
# Arquivo - remove()
try:
    os.remove('templates/geek/university/texto-renomeado.txt')
except FileNotFoundError:
    print('Arquivo "texto-renomeado.txt" não existe')

# Diretório - rmdir()
try:
    os.rmdir('templates')
except FileNotFoundError:
    print('Diretório "templates" não existe')
except OSError:
    print('A pasta não está vazia')

try:
    os.rmdir('templates/geek/university')
except FileNotFoundError:
    print('Diretório "university" não existe')
except OSError:
    print('A pasta não etá vazia')

# Árvore de diretórios - removedirs()
os.makedirs('templates2/geek/university')
os.removedirs('templates2/geek/university')           # Aqui remove desde templates2

# A biblioteca send2trash envia arquivos e diretórios para a lixeira
# é preciso instalar - pip install send2trash
from send2trash import send2trash

# Arquivo
with open('cesta_frutas.txt', 'w', encoding='UTF-8') as cesta:
    cesta.write('Laranja\n')
    cesta.write('Maçã\n')
    cesta.write('Kiwi\n')

try:
    send2trash('cesta_frutas.txt')
except OSError:
    print('Arquivo cesta_frutas.txt não existe')

# Diretório
try:
    send2trash('templates-renomeado/geek/university')  # Somente a pasta university é removida e envia para lixeira
    send2trash('templates-renomeado/geek')             # Somente a pasta geek       é removida e envia para lixeira
    send2trash('templates-renomeado')                  # Somente a pasta templates-renomeado
except OSError:
    print('diretório templates-renomeado/geek/university não existe')

# Criando um diretórios temporários com a biblioteca tempfile -------------------------------------
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário: {tmp}')

    with open(os.path.join(tmp, 'arquivo_temp.txt'), 'a', encoding='UTF-8') as arq:
        arq.write('Geek University')

    # aqui é uma pausa para poder certificar que pasta temporária foi criada
    print(input('Tecle enter, após isso o documento temporário será excluída.'))

# Criando um arquivo temporários com a biblioteca tempfile ----------------------------------------
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')  # "b" - convertendo para binário, só é possível escrever dados binários
    tmp.seek(0)
    print(tmp.read())

# Sem o uso do with é obrigatório o fechamento
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Raissa no pais das maravilhas\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Arquivo nomeado, é possível localiza-lo na pasta
arquivo = tempfile.NamedTemporaryFile()
print(f'Arquivo temporário criado - {arquivo.name}')
arquivo.write(b'Raissa no pais das maravilhas\n')
arquivo.seek(0)
print(arquivo.read())
print(input('Localize o arquivo temporário criado e tecle Enter para finalizar'))
arquivo.close()
