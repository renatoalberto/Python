"""
Escopo de Variáveis
1ª Variáveis globais
2ª Variáveis locais
"""
# curso declarado de forma global
curso = 'Geek'


def diga_oi():
    # curso declarado de forma local, se sobrepõe sobre a global
    curso = 'Java'
    return f'Oi {curso}'


print(diga_oi())  # Aqui imprime 'Java'. Declarado de forma local na função diga_oi()
print(curso)      # Aqui imprime 'Geek'. A atribuição de forma local não alterou a variável declarada de forma global


# Informando que a variável é global
def diga_ola():
    global curso  # avisando que queremos utilizar a variável declarada de forma global
    curso = 'Python'
    return f'Olá {curso}'


print(diga_ola())  # Aqui imprime 'Python'.
print(curso)       # Aqui imprime 'Python', pois foi informado que queremos utilizar a variável global
