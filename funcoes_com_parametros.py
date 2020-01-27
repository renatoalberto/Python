"""
Módulo criado com nome padrão para que seja possível importar no módulo 46_modulos_customizados.py
"""


def soma_impares(numeros):
    total = 0
    primeiro = True

    for numero in numeros:
        if numero % 2 != 0:
            total += numero

            if primeiro:
                primeiro = False
                print(f'{numero}', end=' ')
            else:
                print(f'+ {numero}', end=' ')

    print(f' = ', end=' ')
    return total


# if a seguir para evitar que print seja executado quando este módulo for importado
if __name__ == '__main__':
    lista = list(range(7))
    print(soma_impares(lista))

    tupla = tuple(range(7))
    print(soma_impares(tupla))
else:
    print(f'O módulo {__name__} foi importado.')


def divide_por_2(num1, num2):
    return num1 / num2
