"""
Pacotes

Módulos - É apenas um programa Python que possui diversas funções para utilizarmos
Pacotes - É um diretório contendo uma coleção de módulos

Obs: Na versão 2.x do Python, um pacote Python deveria conter dentro dele um arquivos chamado __init__.py
     Na versão 3.x do Python, não é mais obrigatório a utilização desse arquivo, mas normalmente ainda é
        utilizado para manter compatibilidade.
"""
from pacote import geek1, geek2
from pacote.geek import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(7, 3))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())
