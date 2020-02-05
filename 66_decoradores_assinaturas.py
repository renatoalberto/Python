"""
Decorators com diferentes assinaturas

Assinatura de uma função é representada pelo seu retorno, nome ou parâmetros de entrada

Padrão de Projeto - Decorator Pattern (*args, **kwargs)
"""
# Relembrando--------------------------------------------------------------------------------------

# Aqui a decoration function só recebe um parâmetro
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome.upper())
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(saudacao('Raíssa'))
# print(ordenar('Picanha', 'Batata Recheada'))  # Não permite decorar pois a função decorador só recebe um parâmetro


# Decorator Pattern (*args, **kwargs) -------------------------------------------------------------

# Aqui a decoration function recebe uma quantidade de parâmetros variada
def gritar2(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*[parametro.upper() for parametro in args], **kwargs)
    return aumentar


@gritar2
def saudacao2(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar2
def ordenar2(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


@gritar2
def lol2():
    return f'lol'


print(saudacao2('Renato'))
print(ordenar2('Picanha', 'Batata Recheada'))  # Não permite decorar pois a função decorador só recebe um parâmetro
print(lol2())  # Aqui o decorator também vai funcionar, mesmo não havendo parâmetro de entrada para transformar p/ upper


# Decorator com argumentos ------------------------------------------------------------------------
# Cadeia de funções
# 1ª - função com parâmetro recebida pelo decorator
# 2ª - função com função a ser decorada
# 3ª - função com parâmetros da função a ser decorada
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args):
            if args and args[0] != valor:
                return f'Valor incorreto, primeiro argumento precisa ser {valor}'
            return funcao(*args)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(comida_favorita('pizza', 'churrasco', 'pão'))    # ('pizza', 'churrasco', 'pão')
print(comida_favorita('sorvete', 'churrasco', 'pão'))  # Valor incorreto, primeiro argumento precisa ser pizza

print(soma_dez(10, 12))  # 22
print(soma_dez(15, 12))  # Valor incorreto, primeiro argumento precisa ser 10
