"""
JSON e Pickle

JSON - Javascript Object Notation
"""
import json, jsonpickle

# Forma básica ------------------------------------------------------------------------------------
ret = json.dumps([
    'produtos', {
        'Playstation 4': ('2TB', 'Novo', '220V', 2340),
        'Home Theater': ('1000W rms', 'Sony', '5.1', 1300)
    },
    'fornecedores', {
        'Banco do Brasil': 'Folha Salarial',
        'Pioneira da Borracha': 'Produtos para escritório',
        'Phillips': 'Produtos para auditório'
    }
])

print(type(ret))  # uma string <class 'str'>
print(ret)


# A partir de uma classe --------------------------------------------------------------------------
class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'vira lata')

# {'_Gato__nome': 'Felix', '_Gato__raca': 'vira lata'}
print(f'Representação dicionário: {felix.__dict__}')

ret = json.dumps(felix.__dict__)

# {"_Gato__nome": "Felix", "_Gato__raca": "vira lata"}
print(f'Representação json      : {ret}')

# Integrando Json com o Pickle é necessário instalação de pacote jsonpickle - pip install jsonpickle -------
ret = jsonpickle.encode(felix)

# {"_Gato__nome": "Felix", "_Gato__raca": "vira lata", "py/object": "__main__.Gato"}
# "py/object"      - identifica o json, é um objeto Python
# "__main__.Gato"  - do tipo Gato
print(f'Representação jsonpickle: {ret}')

# Escrevendo um arquivo json pickle ---------------------------------------------------------------
# aqui o objeto felix é codificado e gravado em um arquivo no formato json
with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo um arquivo json pickle
# aqui o json é lido e decodificado para o objeto felix
with open('felix.json', 'r') as arquivo:
    ret = arquivo.read()
    ret = jsonpickle.decode(ret)
    print(f'Representação do objeto gato: {ret}')
    print(f'Tipo do objeto              : {type(ret)}')
    print(f'Nome                        : {ret.nome}')
    print(f'Raça                        : {ret.raca}')
