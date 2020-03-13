"""
WeatherApp - App de Previsão do Tempo

https://www.geoplugin.com/         - api de geolocalização
https://docs.mapbox.com/api/       - api de pesquisa de localização a partir do nome
https://developer.accuweather.com/ - api de previsão do tempo

"""
import requests
import json
import datetime
from urllib import parse
# import pprint  # pprint - Módulo externo Python para impressão de objetos dict


def dia_da_semana(data):
    ano = int(data[0:4])
    mes = int(data[5:7])
    dia = int(data[8:10])

    dia = datetime.datetime(year=ano, month=mes, day=dia)
    
    dia_semana = dia.weekday()

    semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira',  'Sábado',  'Domingo']

    return semana[dia_semana]


def trata_geoplugin():
    """
    Pegar coordenada com a Api Geoplugin
    :return: lat, long
    """
    req = requests.get('http://www.geoplugin.net/json.gp')

    if req.status_code != 200:
        print('Não foi possível obter a localização (geoplugin).')
    else:
        # print(req.text)
        # print(type(req.text))  # <class 'str'>

        # Converte string para dicionário
        localizacao = json.loads(req.text)
        # print(pprint.pprint(localizacao))
        # print(type(localizacao))  # <class 'dict'>

        # recuperando latitude e longitude
        lat = localizacao['geoplugin_latitude']
        long = localizacao['geoplugin_longitude']
        # print(f'Latitude: {latitude}')
        # print(f'longitude {longitude}')

        return lat, long


def trata_accuweather_geoposition_search(lat, long):
    """
    Accuweather - Geoposition Search:
        Retorna informações sobre um local específico, por GeoPosition (Latitude e Longitude).

    :param lat: Latitude
    :param long: Longitude
    :return: Cidade, Estado, País e Código do Local
    """
    accuweather_geoposition_search_api = "http://dataservice.accuweather.com/" \
                                         + "locations/v1/cities/geoposition/" \
                                         + "search?apikey=" + accuwether_api_key \
                                         + "&q=" + lat + "%2C" + long \
                                         + "&language=pt-br"

    req = requests.get(accuweather_geoposition_search_api)

    if req.status_code != 200:
        print('Não foi possível obter o código do local (Accuweather Geoposition Search).')
    else:
        # Converte string para dicionário
        localizacao = json.loads(req.text)
        # print(pprint.pprint(localizacao))

        geo_cidade = localizacao['LocalizedName']
        geo_estado = localizacao['AdministrativeArea']['LocalizedName']
        geo_pais = localizacao['Country']['LocalizedName']
        geo_codigo_local = localizacao['Key']

        return geo_cidade, geo_estado, geo_pais, geo_codigo_local


def trata_accuweather_current_conditions(localizacao):
    """
    Accuweather - Current Conditions API:
        Retorna dados das Condições Atuais para um local específico.

    :param localizacao: Código da localização em Accuweather
    :return: texto_clima, temperatura_celsius
    """
    accuweather_current_conditions_api = "http://dataservice.accuweather.com/currentconditions/v1/" \
                                         + localizacao \
                                         + "?apikey=" + accuwether_api_key \
                                         + "&language=pt-br"

    req = requests.get(accuweather_current_conditions_api)

    if req.status_code != 200:
        print('Não foi possível obter o clima atual (Accuweather Current Conditions API).')
    else:
        # Converte string para dicionário
        previsao_tempo = json.loads(req.text)
        # print(pprint.pprint(previsao_tempo))

        weather_texto_clima = previsao_tempo[0]['WeatherText']
        weather_temperatura_celsius = previsao_tempo[0]['Temperature']['Metric']['Value']

        return weather_texto_clima, weather_temperatura_celsius


def trata_accuweather_5_days_of_daily_forecasts(localizacao):
    """
    Accuweather - 5 Days of Daily Forecasts API:
    Retorna uma matriz de previsões diárias para os próximos 5 dias para um local específico.
    Por padrão, uma versão truncada dos dados de previsão por hora é retornada.
    O objeto completo pode ser obtido passando "detalhes = true" para a string da URL.

    :param localizacao: Código da localização em Accuweather
    :return: revisões dos últimos 5 dias
         [{dia da semana, Mínima, Máxima, Clima},  {...}, ...]
    """
    accuweather_5_days_of_daily_forecasts_api = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" \
                                                + localizacao \
                                                + "?apikey=" + accuwether_api_key \
                                                + "&language=pt-br&details=false&metric=true"

    req = requests.get(accuweather_5_days_of_daily_forecasts_api)

    previsoes = []

    if req.status_code != 200:
        print('Não foi possível obter a previsão para os próximos 5 dias (Accuweather 5 Days of Daily Forecasts API).')
    else:
        # Converte string para dicionário
        previsao_5_dias = json.loads(req.text)
        # print(pprint.pprint(previsao_5_dias))

        previsoes = []

        for prv in previsao_5_dias['DailyForecasts']:
            previsoes.append({
                'dia': dia_da_semana(prv['Date']),
                'minima': prv['Temperature']['Minimum']['Value'],
                'maxima': prv['Temperature']['Maximum']['Value'],
                'clima': prv['Day']['IconPhrase']
            })

    print('Previsões para hoje e próximos dias:')

    for indice, prv in enumerate(previsoes):
        print('---------------------------------------------------------')

        if indice == 0:
            print('Hoje')
        else:
            print(prv['dia'])

        print(f'Mínima: {round(int(prv["minima"]), 2)}° Celsius')
        print(f'Máxima: {round(int(prv["maxima"]), 2)}° Celsius')
        print(f'Clima: {prv["clima"]}')

    print()


def trata_mapbox_search_service(nome_localizacao):
    """
    Mapbox - Search Service
    A API de geocodificação do Mapbox faz duas coisas: geocodificação direta e geocodificação reversa.
    A geocodificação direta converte o texto do local em coordenadas geográficas,
    transformando 2 Lincoln Memorial Circle NW em -77.050,38.889.

    :param nome_localizacao: Nome do local pesquisado
    :return: lat, long
    """
    # urllib.parse.quote(texto) - transforma texto em caracteres legíveis para url
    _nome_localizacao = parse.quote(nome_localizacao)

    mapbox_search_service_api = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' \
                                + _nome_localizacao \
                                + '.json?access_token=' + mapbox_token

    req = requests.get(mapbox_search_service_api)

    mapbox_longitude = 0
    mapbox_latitude = 0

    if req.status_code != 200:
        print('Não foi possível obter a localização solicitada (Mapbox - Search Service).')
    else:
        # Converte string para dicionário
        localizacao = json.loads(req.text)
        # print(pprint.pprint(localizacao))

        mapbox_latitude = str(localizacao['features'][0]['geometry']['coordinates'][0])
        mapbox_longitude = str(localizacao['features'][0]['geometry']['coordinates'][1])

    return mapbox_longitude, mapbox_latitude


def apresenta_clima():
    print(f'Localizando o clima para o Local: {cidade}, {estado} - {pais}')
    print(f'Clima no momento: {textoClima}')
    print(f'Temperatura {round(temperaturaCelsius, 2)}° Celsius\n')


# ############################### Início do programa ##############################################

# Criado no site https://developer.accuweather.com ------------------------------------------------
accuwether_api_key = 'Dh8Ro3yREM080T7GljOtYr1Z4MR6zKlA'

# Criado no site https://docs.mapbox.com/api/ -----------------------------------------------------
mapbox_token = 'pk.eyJ1IjoicmVuYXRvLWFsYiIsImEiOiJjazc1aTVoYjkwam5uM2xzOTAybW1tamh1In0.ich875kUu6T3miCHoyMpOQ'

if input('Deseja ver a previsão para a sua localização (Sim, Não)? ').title() == 'Sim':
    # Recuperando minha localização com a API - Geoplugin - Longitude e Latitude-------------------
    latitude, longitude = trata_geoplugin()

    # Recuperando minha localização com a API - Accuweather - Geoposition Search ------------------
    # A partir da latitude/longitude recupera código do local
    cidade, estado, pais, localKey = trata_accuweather_geoposition_search(latitude, longitude)

    # Recupera dados climáticos com a API - Accuweather - Current Conditions ----------------------
    textoClima, temperaturaCelsius = trata_accuweather_current_conditions(localKey)

    # Apresentando o resultado final --------------------------------------------------------------
    apresenta_clima()

    if input(f'Deseja ver previsão para os próximos dias para {cidade}  (Sim/Não)? ').title() == 'Sim':
        # Recupera previsão para os próximos 5 dias com a API - Accuweather - 5 Days of Daily Forecasts ---
        trata_accuweather_5_days_of_daily_forecasts(localKey)
else:
    print()

resp = ''
while resp != 'Sim':

    if input('Deseja ver previsão para algum local específico (Sim/Não)? ').title() == 'Sim':
        local = input('Informe o local que deseja saber informações sobre o clima: ')

        latitude, longitude = trata_mapbox_search_service(local)
        cidade, estado, pais, localKey = trata_accuweather_geoposition_search(latitude, longitude)
        textoClima, temperaturaCelsius = trata_accuweather_current_conditions(localKey)

        # Apresentando o resultado final ------------------------------------------------------------------
        apresenta_clima()

        if input(f'Deseja ver previsão para os próximos dias para {cidade} (Sim/Não)? ').title() == 'Sim':
            # Recupera previsão para os próximos 5 dias com a API - Accuweather - 5 Days of Daily Forecasts ---
            trata_accuweather_5_days_of_daily_forecasts(localKey)

    resp = input('Deseja finalizar o programa (Sim/Não) ').title()

    print()
