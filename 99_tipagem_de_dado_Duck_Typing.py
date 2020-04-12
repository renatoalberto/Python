"""
Duck Typing

Se determinado objeto se parece com um pato, anda como um pato, nada como um pato então é um pato

O tipo ou a classe de um objeto é menos importante que os métodos que o definem, e ao invés de
checar a classe ou o tipo de dado, é checado a presença de métodos ou atributos específicos.

Objetos similares devem ter métodos ou atributos ou comportamentos similares
"""


class CisneiNegro:

    def __len__(self):
        return 42


livro = CisneiNegro()

print(len(livro))

nome = 'Geek University'
lista = [12, 34, 55, 49]
dicionario = {'Carlos': 12, 'Vanessa': 34, 'Joana': 49}

print(len(nome))
print(len(lista))
print(len(dicionario))

"""
int - Não possui o método len()

idade = 36
print(type(idade))
print(len(idade))
"""
