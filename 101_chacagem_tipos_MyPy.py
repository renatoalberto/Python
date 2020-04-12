"""
MyPy

http://mypy-lang.org/

Criado para ser uma nova linguagem de programação, e reescrito para ser um checados de tipos
da linguagem Python oficial

Instalação:
pip install mypy

Execução, no terminal informe:
mypy 101_chacagem_tipos_Mypy.py

1ª - Usar o "Type Hinting" em todas as funções/métodos/classes/atributos
2² - Utilizar o MyPy para checar o arquivo para avaliar se código está correto

"""


# ---------------------------------------------------------------------------------------
def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"=" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '=')


print(cabecalho('geek university'))
print(cabecalho('geek university', alinhamento=False))

# Avaliando como é tratado o erro no MyPy -----------------------------------------------
# 101_chacagem_tipos_Mypy.py:29: error: Argument "alinhamento" to "cabecalho" has incompatible type "str"; expected "bool"
print(cabecalho('geek university', alinhamento='geek'))
