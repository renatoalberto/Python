"""
Tradução de Texto com TextBlob

É necessário instalar - pip install TextBlob

* Biblioteca utiliza internet para realizar tradução
* Explicação retirada da aula 89_metodos_data_hora no minuto 30
"""
import datetime
from textblob import TextBlob


# strftime('%B') - Retornar o mês em inglês
def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br').title()} de {data.year}"


hoje = datetime.datetime.now()
print(formata_data(hoje))    # 15 de Fevereiro de 2020
