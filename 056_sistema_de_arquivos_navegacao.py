"""
Sistema de Arquivos - Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operations System
"""
import os

# getcwd() -> pegar diretório de trabalho corrente ------------------------------------------------
print(os.getcwd())  # Retorna o caminho absoluto - C:\Users\renat\PycharmProjects\guppe

# podemos checar se um diretório é absoluto ou relativo -------------------------------------------
print(os.path.isabs("C:\\Users\\renat\\PycharmProjects\\guppe"))  # duplo contra barra <=> contra barra simples
print(os.path.isabs("Users\\renat\\PycharmProjects\\guppe"))      # duplo contra barra <=> contra barra simples

# podemos identificar qual o sistema operacional --------------------------------------------------
print(f'Sistema operacional - {os.name}')  # posix (Linux e Mac), nt (Windows)

# podemos ter mais detalhes sobre o sistema operacional -------------------------------------------
# print(os.uname())  # funciona somente em ambiente linux

# sobre a plataforma ------------------------------------------------------------------------------
import sys

print(sys.platform)  # win32 ou linux

# chdir() -> change dir - mudar o diretório -------------------------------------------------------
print(f'Diretório atual           - {os.getcwd()}')  # C:\Users\renat\PycharmProjects\guppe

os.chdir('..')
print(f'Sai da pasta guppe        - {os.getcwd()}')  # C:\Users\renat\PycharmProjects

# os.path.join - importante pois respeita as regras do sistema operacional
diretorio = os.path.join(os.getcwd(), 'guppe', 'pacote', 'geek')
os.chdir(diretorio)
print(f'Retornei para pasta guppe - {os.getcwd()}')  # C:\Users\renat\PycharmProjects\guppe\pacote\geek

# podemos listar os documentos e diretórios com listdir() -----------------------------------------
print(f'listar os documentos e diretórios - {os.listdir()}')

# mais detalhes com scandir() ---------------------------------------------------------------------
scanner = os.scandir()
arquivo = list(scanner)

# print(dir(arquivo[0]))  # Verificar o que é possível fazer para cada item listado

print(arquivo[0].inode())          # identificador de node - número na árvore de diretórios
print(arquivo[0].is_dir())         # é um diretório?
print(arquivo[0].is_file())        # é um arquivo?
print(arquivo[0].is_symlink())     # é um link de atalho?
print(arquivo[0].name)             # nome do arquivo
print(arquivo[0].path)             # a partir do diretório atual, mostra o caminho até ele
print(arquivo[0].stat())           # várias informações de estatística
print(arquivo[0].stat().st_size)   # várias informações de estatística, tamanho do arquivo em bytes

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim como fazemos quando abrimos um arquivo
scanner.close()
