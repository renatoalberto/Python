"""
Filter

filter() - Serve para filtrar dados de uma determinada coleção

filter é uma função que recebe dois parâmetros e retorna um objeto do tipo "Filter Object":
1 - Uma função
2 - Um iterável

"Filter Object" é executado uma única vez, a partir da segunda vez ele estará zerado.
"""
import statistics  # Biblioteca para trabalhar com dados estatísticos
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

# filter é uma função que recebe dois parâmetros: função e um iterável
res = filter(lambda x: x > media, dados)
print('Média = ', media)
print(type(res))  # retorna um objeto do tipo "Filter Object"
print(list(res))
print(list(res))  # após utilizar uma vez o objeto é zerado

# Removendo dados faltante ------------------------------------------------------------------------
paises = ['', 'Brasil', '', '', 'Venezuela', 'Uruguai', 'Paraguai', '', '', 'Bolívia', 'Chile', '']

# Forma 1
res = filter(lambda pais: pais != '', paises)
print(list(res))

# Forma 2
res = filter(None, paises)  # Modo profissa
print(list(res))

# Simulação de entrevista no Twitter --------------------------------------------------------------
usuarios = [
    {'username': 'renato', "twitters": ['eu adoro bolo', 'eu adoro pizza']},
    {'username': 'raissa', "twitters": ['eu adoro chocolate', 'eu adoro brincar']},
    {'username': 'nick', "twitters": ['eu adoro dormir']},
    {'username': 'lana', "twitters": ['eu adoro comer']},
    {'username': 'tati', "twitters": []},
    {'username': 'karina', "twitters": []},
    {'username': 'jessica', "twitters": []}
]

# levantar usuários inativos no twitter
# Forma 1
res = filter(lambda usuario: len(usuario['twitters']) == 0, usuarios)
print(list(res))

# Forma 2
res = filter(lambda usuario: not usuario['twitters'], usuarios)  # vazio é falso no python
print(list(res))

# Combinar Filter e Map ---------------------------------------------------------------------------
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo "sua instrutora é" + nome, desde que o nome tenha menos de 5 caracteres
res = map(lambda nome: f'sua instrutor é {nome}', filter(lambda nome: len(nome) < 5, nomes))
print(list(res))
