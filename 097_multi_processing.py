"""
Como lidar com o Gil?

multi-processing - utilizamos multi-processing ao invés de multi-threading. utilizando
                   multiprocessing, cada processo Python ganha seu próprio interpretador
                   Python e espaço em memória, assim o Gil não será problema.
                 - multi-processing são mais pesados que multi-threading, pois cada processo
                   terá seu próprio ambiente Python.
"""
import time
from multiprocessing import Pool


def contagem_regressiva(n):
    while n > 0:
        n -= 1


CONTADOR = 50000000

if __name__ == '__main__':
    inicio = time.time()
    pool = Pool(processes=2)
    r1 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    r2 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    pool.close()
    pool.join()
    fim = time.time()

    print(f'Tempo de processamento em segundos multi-processing  - {fim - inicio}')  # 3.468797445297241
