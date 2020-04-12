"""
Erros mais comuns em Python:

Todos os erros na documentação: https://docs.python.org/3/library/exceptions.html

Obs1: Erros e Exceptions são sinônimos na programação
Obs2: É importante e prestar atenção e aprender a ler as saídas de erro gerados pelo nosso código

1 - NameError        -> Ocorre quando uma variável ou função não foi definida

2 - SyntaxError      -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não
                        reconhece como parte da linguagem.

3 - TypeError        -> Ocorre quando uma função/operação/ação é aplicada sobre o tipo errado.

4 - IndexError       -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
                        utilizando um índice inválido.

5 - ValueError       -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas
                        valor inapropriado.

6 - KeyErro          -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

7 - AttributeError   -> Ocorre quando uma variável não tem um atributo ou função.

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)
"""
# Exemplo NameError -------------------------------------------------------------------------------
# NameError: name 'printf' is not defined
# printf('Geek University')

# NameError: name 'Geek' is not defined
# print(Geek)

# NameError: name 'geek' is not defined
# geek()

# NameError: name 'msg' is not defined
# a = 18
# if a < 10:
#    msg = 'a é menor que 10'  # nesse caso 'a' é maior que 10 e nunca entrará no 'if'
# print(msg)

# Exemplo SyntaxError -----------------------------------------------------------------------------
# SyntaxError: invalid syntax
# def funcao:
#    print('Geek University')

# SyntaxError: cannot assign to None
# None = 1  # Utilização de variável com nome de palavra reservada

# SyntaxError: invalid syntax
# def = 1

# Exemplo TypeError -------------------------------------------------------------------------------
# TypeError: object of type 'int' has no len()
# print(len(5))

# TypeError: can only concatenate str (not "list") to str
# print('Geek' + [])

# TypeError: can only concatenate str (not "int") to str
# print('Geek' + 4)

# Exemplo IndexError ------------------------------------------------------------------------------
# IndexError: list index out of range
# lista = ['Geek']
# print(lista[1])

# IndexError: tuple index out of range
# tupla = ('Geek',)
# print(tupla[1])

# IndexError: string index out of range
# letra = 'Geek'[5]

# Exemplo ValueError ------------------------------------------------------------------------------
# ValueError: invalid literal for int() with base 10: 'Geek'
# inteiro = int('Geek')

# ValueError: could not convert string to float: 'Geek'
# flutuante = float('Geek')

# Exemplo KeyError --------------------------------------------------------------------------------
# KeyError: 'Geek'
# dicionario = {}
# print(dicionario['Geek'])

# Exemplo AttributeError --------------------------------------------------------------------------
# AttributeError: 'tuple' object has no attribute 'sort'
# tupla = tuple(range(10))
# print(tupla.sort())

# Exemplo IndentationError ------------------------------------------------------------------------
# IndentationError: expected an indented block
# def nova():
# print('Geek')

# IndentationError: expected an indented block
# for i in range(10):
# print(i)
