"""
Bloco Try/Except

Utilizamos o bloco try/except para tratar erros no nosso código. Previnindo assim que o programa pare de funcionar
e o usuário receba mensagens de erro inesperadas.

A forma geral é:
try:
    //execução problemática
except:
    //o que deve ser feito em caso dr problemas

"""
# Exemplo1 ----------------------------------------------------------------------------------------
# tente executar a função geek(), caso ocorra qualquer tipo de erro, imprima uma mensagem de erro
try:
    geek()  # função não declarada
except:
    print('Deu algum problema na chamada da função geek()')

# Exemplo2 ----------------------------------------------------------------------------------------
# importante tratar o erro de forma específica, e mais de um erro por vez.
try:
    len(5)  # não é possível retornar o tamanho de um int
except TypeError:
    print('Não é possível retornar o tamanho de um int.')
except NameError:
    print('Função inexistente, não declarada.')

try:
    geek(5)  # Função inexistente não declarada
except ValueError:
    print('Não é possível retornar o tamanho de um int.')
except NameError:
    print('Função inexistente, não declarada.')

# Exemplo3 ----------------------------------------------------------------------------------------
# É possível receber o erro por parâmetro
try:
    len(5)  # não é possível retornar o tamanho de um int
except TypeError as err:
    print(f'A aplicação gerou o erro: {err}')

# Exemplo4 ----------------------------------------------------------------------------------------
# Tratamento de erro não previsto
try:
    print('Geek'[9])
except TypeError as erra:
    print(f'A aplicação gerou o erro: {err}')
except ValueError as errb:
    print('Não é possível retornar o tamanho de um int.')
except:
    print('Aconteceu um erro não previsto.')

# Exemplo5 ----------------------------------------------------------------------------------------
# Tratamento de erro de uma função declarada


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as errx:
        return f'Chave não localizada: {errx}'
    except :
        return f'Erro não previsto.'


dicionario = {'nome': 'Geek'}
print(pega_valor(dicionario, 'nome'))
print(pega_valor(dicionario, 'University'))
print(pega_valor(None, 'University'))
