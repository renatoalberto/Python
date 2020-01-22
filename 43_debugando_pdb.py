"""
Debugando com PDB - Python Debug

#OBS - Utilizar o print é uma prática ruim de debugar um código
     - Existem formas mais profissionais fazer um debug:
         + Utilizando o debug de diferentes IDEs como o do Pycharm
         + Utilizando o PDB - Python Debug

Com Pycharm (recomendado):
    1 - Inclua pontos de parada clicando no lado do número da linha
    2 - Inicie o debug clicando na joaninha ou botão direito do mouser e debug
    3 - Assim que iniciado, a execução pausa sore o primeiro ponto de parada
    4 - As variáveis são listadas, informando o seu tipo
    5 - botões disponibilizados (F8 - Próxima Linha)
    6 - É possível selecionar um cálculo e clicando com o botão direito em (Add to whatches) para visualizar o resultado

Com PDB - Python Debug (recomendado quando não utilizando uma IDE)
    1 - Importar biblioteca pdb*
    2 - incluir ponto de para com "dpb.trace()"
    3 - l - para listar onde estamos no código
    4 - n - próxima linha
    5 - p - imprime variável quando conflito de nome (p l) (p n) (p c), ou digitando o nome da variável
    6 - c - continua execução - finaliza o debug

* A partir do Python 3.7 a biblioteca pdb foi incorporada como função built-in (integrada) chamada "breakpoint()"
"""


def dividir(valor1, valor2):
    print(f'Primeiro valor - {valor1}, \nSegundo  valor - {valor2}')  # prática ruim de debugar um código
    try:
        return valor1 / valor2
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ocorreu um erro - {err}')


print(dividir(4, 7))


# Exemplo com PDB - Python Debug
# Precisamos importar a biblioteca pbd e então utilizar a função set_trace()
# import pdb  # import comum

nome = 'Raíssa'
sobrenome = 'Alberto'

# Formato de import + utilizando o comando
# Para incluir o ponto de parada com a função set_trace():
# import pdb; pdb.set_trace()
breakpoint()

nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Realizar o import mais utilização da biblioteca na mesma linha facilita a remoção do debug pois é utilizado somente
# durante o desenvolvimento

