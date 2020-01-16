"""
Módulo Collections - Default Dict
Documentação: https://docs.python.org/3/library/collections.html#collections.defaultdict

Default Dict - Criamos um valor default, podemos utilizar um lambda para isso.
               Este valor utilizado sempre que não houver um valor definido,
               caso tentemos acessar uma chave que não existe, essa chave será
               criada e o valor default será atribuído.

Obs: Lambdas - são funções sem nome, que podem ou não receber parâmetros de
     entrada e retornar valores.
"""
from collections import defaultdict

dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])
# print(dicionario['outro'])  # Gera um erro para chave inexistente

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # NÃO Gera um erro - retorna valor default 0
print(dicionario)


