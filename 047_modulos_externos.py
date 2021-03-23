"""
Módulos Externos - Aula exploratória do site de pacotes Python

Utilizamos o gerenciador de pacotes chamado PIP (Python Installer Package)
Instalar um pacote             : pip install nome_do_pacote;
Remover um pacote              : pip uninstall nome_do_pacote;
Verificar os pacotes instalados: pip freeze.

Podemos conhecer todos os pacotes externos oficiais em https://pypi.org/

colorama -> É utilizado para permitir impressão de texto colorido no terminal
"""
# Instalação do colorama no terminal: pip install colorama ----------------------------------------
from colorama import init, Fore, Back, Style
init()

print(Fore.RED, 'Geek University')
print(Fore.GREEN + 'Geek University')
print(Fore.YELLOW + 'Geek University')
print(Fore.BLUE + 'Geek University')
print(Style.RESET_ALL + 'Geek University')                   # retorna cores padrão
