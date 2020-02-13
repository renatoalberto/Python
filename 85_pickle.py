"""
Conhecendo o Pickle

A função do pickle é realizar o seguinte processo:
Objeto Python -> Binarização
Binarização   -> Objeto Python

Esse processo é chamada de "serialização/deserialização"

Obs: O módulo pickle não é seguro contra dados maliciosos e dessa forma não é
     recomendado trabalhar com arquivos pickle vindo de outras pessoas que você
     não conheça ou de fontes desconhecidas.
"""
import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo.')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        return f'{self.nome} está miando.'


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        return f'{self.nome} está latindo.'


felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo escrita em arquivos pickle --------------------------------------------------------------
# criando um arquivo com extensão pickle, a extensão não é obrigatória
# flag 'wb' - write binary - criando um arquivo binário
# escrita binária não possui o argumento encoding='utf-8'
# método dump, recebe dois parâmetros: (tupla de Objetos Python) e (arquivo que será escrito)
with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)

# Fazendo leitura em arquivos pickle --------------------------------------------------------------
# flag 'rb' - read binary - lendo um arquivo binário
# método load, recebe por parâmetro o arquivo binário a ser carregado
with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    print(gato.mia())
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    print(cachorro.late())
    print(f'O tipo do cachorro é {type(cachorro)}')
