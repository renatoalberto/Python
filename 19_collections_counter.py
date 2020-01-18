"""
Módulo Collections - Counter (Contador)
Documentação: https://docs.python.org/3/library/collections.html#collections.Counter

Collections - High - Performance Container Datetypes (Tipo de dado conteiner de alta performance)

Counter - Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
          dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de
          ocorrências desse elemento.
"""
from collections import Counter

# Utilizando Counter ---------------------------------------------------------------------------------------------------

# podemos utilizar qualquer iterável aqui, estamos utilizando uma lista
lista = [1, 1, 1, 2, 2, 2, 1, 1, 4, 5, 6, 5, 5, 6, 6, 7, 40, 45, 47, 50, 45]

# Para cada elemento da lista é crido uma chave - no valor é informado a quantidade de ocorrências
counter = Counter(lista)

print(f'Tipo de res - {type(counter)}')
print(f'Counter gerado - {counter}')

# Criando um collections.Counter a partir de uma string
counter = Counter('Geek University')
print(f'Counter gerado - {counter}')

# Utilização interessante do Counter --------------------------------------------------------------
longo_texto = """Depois de uma temporada de 2019 em que Sebastian Vettel foi superado pelo jovem companheiro de equipe
 Charles Leclerc, a Ferrari deve investir em um carro mais voltado para o veterano piloto alemão. Quem garante isso é 
 Mattia Binotto, chefe da escuderia italiana. Nós vamos desenhar um carro que se adapta mais ao estilo de pilotagem do 
 Sebastian Vettel, com mais pressão aerodinâmica na traseira", explicou o italiano em entrevista ao Motorsport.com."""

lista_palavras = longo_texto.split()

counter = Counter(lista_palavras)
print(counter)

# Apresentando as 5 palavras mais comum no texto
print(counter.most_common(5))
