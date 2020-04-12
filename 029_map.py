""""
Map

Com Map fazemos mapeamento de valores para função

Map é uma função que recebe dois parâmetros e retorna um objeto do tipo "Map Object":
1 - Uma função
2 - Um iterável

"Map Object" é executado uma única vez, a partir da segunda vez ele estará zerado.
"""
import math


def area(raio):
    """Calcula o área de um círculo a partir do raio informado por parãmetro."""
    return math.pi * (raio ** 2)


print(area(2))
print(area(5.3))

# Forma comum -------------------------------------------------------------------------------------
raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []

for raio in raios:
    areas.append(area(raio))

print(areas)

# Forma utilizando Map ----------------------------------------------------------------------------
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))  # Convertendo o objeto do tipo "Map Object" para lista

# Forma utilizando Map com lambda -----------------------------------------------------------------
areas = map(lambda raio: math.pi * (raio ** 2), raios)
print(list(areas))  # Convertendo o objeto do tipo "Map Object" para lista
print(list(areas))  # "Map Object" só executa uma vez, a partir da segunda vez ele estará zerado, aqui retorna []

# Mesmo varrendo com "for", na segunda vez estará vazio
areas = map(lambda raio: math.pi * (raio ** 2), raios)
for area in areas:
    print(f'Área {area}', end=", ")
print()
print(list(areas))  # "Map Object" só executa uma vez, a partir da segunda vez ele estará zerado, aqui retorna []

# Mais um exemplo, lista contendo tuplas ----------------------------------------------------------
# Cidades mais temperaturas em Celsius
cidades_c = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26),
             ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

# Convertendo em Fahrenheit
c_para_f = lambda dado: (dado[0], (dado[1] * (9/5)) + 32)
cidades_f = map(c_para_f, cidades_c)
print(list(cidades_f))
