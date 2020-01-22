"""
Levantando os próprios erros com raise

raise -> lança excessões, não é uma função, é uma palavra reservada assim como def ou qualquer outra em Python.

Simplificando, pense em raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro

Forma geral de utilização :
raise TipoDoErro('mensagem de erro')

Obs: O raise, assim como o return, finaliza a função. Ou seja, nada após o rase é executado.
"""
# Demonstrando
# raise ValueError('Valor incorreto.')

"""  No picharm gera o erro a seguir:
Traceback (most recent call last):
  File "C:/Users/renat/PycharmProjects/guppe/40_raise.py", line 12, in <module>
    raise ValueError('Valor incorreto.')
ValueError: Valor incorreto.
"""


# Exemplo real
def cores(texto, cor):
    tuplaCores = 'amarelo', 'azul', 'preto', 'vermelho'
    if type(texto) is not str:
        raise TypeError('Texto deve ser uma string.')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in tuplaCores:
        raise ValueError(f'Cor precisa ser uma entre {tuplaCores}')
    print(f'O texto {texto} será impresso na cor {cor}')


cores('Geek', 'azul')
# cores('Geek', 3)       # Gera uma exceção - Cor precisa ser uma string
# cores(7, 'azul')       # Gera uma exceção - Texto precisa ser uma string
# cores('Geek', 'anil')  # Gera uma exceção - Cor precisa ser uma entre ('amarelo', 'zul', 'preto', 'vermelho')

