"""
try / except / else / finally

try     - Tente executar o código a seguir
except  - Em caso de erro executa o código a seguir
else    - Em caso de processamento normal
finally - Ao final sempre executar o código a seguir, ocorrendo exceção ou não

finally é utilizado para fechar ou desalocar recursos.

Dica de onde e quando tratar o código:
- Toda entrada deve ser tratada;

"""
# try e except são comuns, mas else e finally não
try:
    num = int(input('Informe um número:'))
except ValueError as err1:
    print(f'Caracter inválido, digite apenas números: {err1}')
else:
    print(f'Você digitou o número : {num}')
finally:
    print(f'Fim da execução.')


# Exemplo mais complexo ---------------------------------------------------------------------------

""" 
tratamento individualizado:
def dividir(valor1, valor2):
    try:
        return int(valor1) / int(valor2)
    except ValueError as err1:
        print(f'Valor não numérico - {err1}')
    except ZeroDivisionError as err2:
        print(f'Segundo valor zerado. - {err2}')
"""


# tratamento "Semi genérico"
def dividir(valor1, valor2):
    try:
        return int(valor1) / int(valor2)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ocorreu um erro. - {err}')


num1 = input('Informe o primeiro valor: ')
num2 = input('Informe o segundo  valor: ')
print(f'Divisão de {num1}/{num2} - {dividir(num1, num2)}')
