"""
Definindo Funções

- São pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber ter entrada de dados e retornar uma saída de dado;
- Evita repetição de código;

DRY - Don't Repeat Yourself ( Não repita você mesmo - Não repita o código )

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é interessante fazer uma verificação
     para que a função seja simplificada.

Sequencia obrigatória dos parâmetros:
1ª - Parâmetros obrigatórios
2ª - *args
3ª - Parâmetros default (Não obrigatórios)
4ª - **kwargs
"""
from random import random


# Exemplo de utilização de funções
cores = []
cores.extend(['verde', 'amarelo', 'azul', 'vermelho', 'preto', 'branco', 'rosa', 'roxo', 'marrom', 'bege'])

# Utilização de função integrada é chamada de (Built-in) do Python - print()
cores.append('ciano')
print(cores)

"""
Em Python, a forma geral de definição de uma função e:

def nome_da_função(parâmetros_de_entrada):
     bloco_da_função

Onde:
=> def: Informa ao Python que estamos definindo uma função;
=> nome_da_função: SEMPRE, com letras minúsculas, e para nome composto será separado por underline (snake case);
=> parâmetros_de_entrada: Opcionais, separadas por vírgula;
=> bloco_da_função: ou corpo da função, é onde o processamento da função acontece, pode ter ou não retorno;   
"""


# Definindo a primeira função ---------------------------------------------------------------------
def diga_oi():
    print('Oi!')


"""
1ª - Veja que dentro da nossa função podemos chamar outras funções;
2ª - Veja que nossa função só executa uma tarefa;
3ª - Veja que essa função não recebe nenhum parâmetro de entrada;
4ª - Veja que essa função não retorna nada.
"""

# Para utilizar é necessário chamar a função -- =/ sério??? ---------------------------------------
diga_oi()

# Podemos criar uma variável do tipo de função ----------------------------------------------------
cumprimenta = diga_oi
cumprimenta()


# Definindo funções com retorno -------------------------------------------------------------------
# Em Python quando uma função não retorna nenhum valor, o retorno será None

# Função com parâmetros de entrada
def quadrado_de_um_numero(numero):
    return numero ** 2


# Quando parâmetro é declarado recebendo um valor, ele se torna opcional
# Quando opcionais DEVEM ser declarados a direita dos parâmetros, caso contrário causará erro
def cumprimentar(nome, sobrenome=''):
    return f'Bem vindo {nome} {sobrenome}!'


# -------------------------------------------------------------------------------------------------
# Imprimindo o resultado da função quadrado_de_um_numero()
# Sobre nomenclatura:
#  - A função recebe (PARÂMETROS) - variáveis declaradas na definição da função
#  - chamamos um função passando (ARGUMENTOS) - dados passados durante a execução da função
print(quadrado_de_um_numero(7))

# Guardando e imprimindo o resultado da função quadrado_de_um_numero()
resultado = quadrado_de_um_numero(7)
print(resultado)

# É possível passar argumentos nomeados
texto_saudacao = cumprimentar(nome='Renato', sobrenome='Alberto')
print(texto_saudacao)
texto_saudacao = cumprimentar(sobrenome='Alberto', nome='Renato')
print(texto_saudacao)
texto_saudacao = cumprimentar(nome='Raíssa')
print(texto_saudacao)


# -------------------------------------------------------------------------------------------------
# Retornando múltiplos retornos
def retorna_4_numeros():
    return 1, 2, 3, 4


num1, num2, num3, num4 = retorna_4_numeros()

print(f'{num1} | {num2} | {num3} | {num4}')
print(retorna_4_numeros())


# Uma função que retorna valor randômico
def cara_ou_coroa():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(f'Retornou {cara_ou_coroa()}')


# -------------------------------------------------------------------------------------------------
# Documentando funções com Docstrings
# Podemos ter acesso a documentação a partir da função especial "__doc__"
# Podemos ter acesso a documentação a partir da função "help()"
def divide_pela_metade(numero):
    """
     Essa é uma DOCSTRING -
        Função divide_pela_metade: Divide o número recebido por parâmetro pela metade, ou seja, divide por 2

    :param numero: Número que desejamos gerar o quadrado
    :return: Retorna o quadrado do número informado
    """
    return numero / 2


print(divide_pela_metade.__doc__)
print(help(divide_pela_metade))


# -------------------------------------------------------------------------------------------------
# *args - é um parâmetro como outro qualquer, começado por "*",
#         reconhecendo os valor extras de uma função como uma tupla
def soma_todos_os_numeros(nome, email, *args):
    return f'{nome} - {email} realizou {sum(args)} vendas.'


print(f'Soma dos número 7 e 8 - {soma_todos_os_numeros("Renato", "renato.alb@gmail.com", 7, 8)}')
print(f'Soma dos número 7, 8 e 20 - {soma_todos_os_numeros("Renato", "renato.alb@gmail.com", 7, 8, 20)}')
print(f'Soma dos número 7, 8, 20 e 40 - {soma_todos_os_numeros("Renato", "renato.alb@gmail.com", 7, 8, 20, 40)}')

# passando um lista para args é necessário desempacotar com um *, dessa forma *lista, assim ele saberá que é
# necessário desempacotar antes da chamada da função
quantidade_vendas = [7, 3, 15, 23, 12, 17]
print(soma_todos_os_numeros('Raíssa', 'raissa.alb@gmail.com', *quantidade_vendas))


# -------------------------------------------------------------------------------------------------
# **kwargs - é um parâmetro, diferente do *args que transforma os parâmetros em uma tupla,
#            **kwargs permite que utilizemos parâmetros nomeados, e transforma os parâmetros extras
#            em um dicionário.
def cores_favoritas(**kwargs):
    print(f'Tipo - {type(kwargs)}. {kwargs}')

    for pessoa, cor in kwargs.items():
        print(f'{pessoa} gosta da cor {cor}')


cores_favoritas(marcos='verde', renato='amarelo', raissa='lilas', theo='azul')


# Outro exemplo
def cumprimento_especial(**funcionario):
    if 'Geek' in funcionario and funcionario['Geek'] == 'Renato':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'Geek' in funcionario:
        return f'{funcionario["Geek"]} Geek!'
    else:
        return f'Não tenho certeza de quem você é.'


print(cumprimento_especial())
print(cumprimento_especial(Geek='Renato'))
print(cumprimento_especial(Geek='Raíssa'))
print(cumprimento_especial(Banco_do_Brasil='Tomaz'))


# Desempacotar com kwargs ------------------
def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': "Renato", 'sobrenome': "Alberto"}
print(mostra_nomes(**nomes))          # **nomes - realiza o desempacotamento


def soma_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
soma_numeros(*lista)
tupla = (1, 2, 3)
soma_numeros(*tupla)
conjunto = {1, 2, 3}   # set
soma_numeros(*conjunto)
dicionario = {'a': 1, 'b': 2, 'c': 3}  # os nomes das chave devem ser os mesmos nomes da função
soma_numeros(**dicionario)

# -------------------------------------------------------------------------------------------------
"""
Sequencia obrigatória dos parâmetros:
1ª - Parâmetros obrigatórios
2ª - *args
3ª - Parâmetros default (Não obrigatórios)
4ª - **kwargs
"""


def minha_funcao(nome, idade, *args, casado=False, **kwargs):
    print(f'{nome} e tenho {idade} anos.')
    print(args)
    if casado:
        print('Casado')
    else:
        print('Solteiro')
    print(kwargs)


minha_funcao('Renato', 36)
minha_funcao('Renato', 36, 5, 4, 3, casado=True)
minha_funcao('Renato', 36, 5, 4, 3, eu='Nao', voce='Vai')
minha_funcao('Renato', 36, 5, 4, 3, casado=True, eu='Nao', voce='Vai')
minha_funcao('Renato', 36, 5, 4, 3, eu='Nao', voce='Vai')
