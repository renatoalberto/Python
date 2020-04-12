"""
Forçando tipos de dados com decoradores

relembrando função zip:
a = (1, 3, 5)
b = (2, 4, 6)
c = zip(a , b) => (1, 2) (3, 4) (5, 6)
"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            try:
                for (valor, tipo) in zip(args, tipos):
                    novo_args.append(tipo(valor))
                return funcao(*novo_args, **kwargs)
            except ValueError:
                print(f'Não foi possível converter "{valor}" do tipo {type(valor)} para {tipo}')
        return converter
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    [print(msg) for vez in range(vezes)]


@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)


repete_msg('Geek', '3')  # Aqui mesmo passando uma string 3, o loop consegue ser executado
repete_msg('Geek', 3.5)  # Aqui mesmo passando um float, o loop consegue ser executado

dividir(6, 3)         # aqui passando inteiros, o retorno é float
dividir('6', '3')     # aqui passando string, a função não retorna erro
dividir('renato', 2)  # Aqui passando uma string, o decorator realizou uma validação, retornando uma mensagem
dividir(5, 'Nick')    # Aqui passando uma string, o decorator realizou uma validação, retornando uma mensagem'
