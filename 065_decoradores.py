"""
Decoradores (Decorators)

O que são decorators?
 - Decorator Functions são funções
 - Decorators também são exemplos de Higher Order Function
 - Decorators envolve outras funções e aprimoram seus comportamentos
 - Decorators tem uma sintaxe própria, usando "@" (Syntactic Sugar - para facilitar a visualização)

OBS: não confunda "decorator function" com "decorator"
"""
# Decorators como funções - sintaxe não recomendada, sem syntactic sugar --------------------------


# Decorator function
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia')
    return sendo


def saudacao():
    print('Seja bem vindo a Geek University')


# Testando 1 - função "saudacao" foi aprimorada pela função decoradora "seja_educado"
comprimento_educado = seja_educado(saudacao)
comprimento_educado()
print('--------------------------')


# testando 2
def raiva():
    print('EU TE ODEIO')


raiva_educado = seja_educado(raiva)
raiva_educado()
print('--------------------------')


# Decorator com Sintactic Sugar - recomendado -----------------------------------------------------
# *Decorator Function
def seja_educado_mesmo(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia')
    return sendo


# *Decorator
@seja_educado_mesmo
def saudacao_mesmo():
    print('Seja bem vindo a Geek University')


# Testando 1 - agora que a função "saudação_mesmo" foi decorada, basta executar que ela terá
#              o comportamento da função "seja_educado_mesmo"
saudacao_mesmo()
print('--------------------------')


# Testando 2
@seja_educado_mesmo
def quero_dormir():
    print('Quero dormir.')


quero_dormir()
