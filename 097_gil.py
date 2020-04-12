"""
Python Global Interpreter Lock - GIL

Gil - é um mutex (lock), que permite que apenas uma thread tome conta do interpretador Python, isso significa
      que apenas uma thread pode está em execução em qualquer ponto do tempo.
    - aplica a regra de single lock, prevenindo qualquer deadlock, o que por outro lado transforma qualquer
      código Python em single thread.

Gil faz parte da implementação original (CPython escrito em C). Outras implementações como (Jython escrito em Java),
    (IronPython escrito em C#), e (PyPy escrito em Python) não teremos os problemas que o GIL traz.
"""
import sys, timeit, functools
from threading import Thread
from multiprocessing import Pool

# O Python faz uma contagem de quantas referências fazem apontamento a um objeto criado na memória heap
a = []
b = a
print(sys.getrefcount(a))  # retornou 3, que são o a, b e a própria sys.getrefcount()

b = None
print(sys.getrefcount(a))  # retornou 2, que são o a e a própria sys.getrefcount()


# Testando a performance de um processamento em single thread -------------------------------------
def contagem_regressiva(n):
    while n > 0:
        n -= 1


CONTADOR = 50_000_000

tempo = timeit.timeit(functools.partial(contagem_regressiva, CONTADOR), number=1)
print(f'Tempo de processamento em segundos single thread - {tempo}')  # 5.902446299999999


# Testando a performance de um processamento em multi thread --------------------------------------
def processa_mult_thread():
    global CONTADOR

    t1 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
    t2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


tempo = timeit.timeit(functools.partial(processa_mult_thread), number=1)
print(f'Tempo de processamento em segundos multi thread  - {tempo}')  # 4.8112236

# OBS: Mesmo com a utilização do multi thread a melhora não é significativa, por causa do GIL,
#      que torna uma aplicação single thread muito performatica e a maioria das aplicações das
#      aplicações não precisam utilizar multi thread.

# Como lidar com o Gil ----------------------------------------------------------------------------
# Podemos utilizar multi-processing ao invés de multi-threading. utilizando multiprocessing,
# cada processo Python ganha seu próprio interpretador Python e espaço em memória, assim o
# Gil não será problema.