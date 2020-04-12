"""
Trabalhando com Delta de data e hora

Delta é o tempo decorrido entre duas datas/horas - delta = tempo_final - tempo_inicial
"""
import datetime

data_hoje = datetime.datetime.now()
data_evento = datetime.datetime(2020, 7, 7)

delta = data_evento - data_hoje

print(type(delta))  # <class 'datetime.timedelta'>
print(repr(delta))  # datetime.timedelta(days=142, seconds=48103, microseconds=736724)
print(delta)        # 142 days, 13:21:43.736724

# Retornando somente quantidade de dias e horas ---------------------------------------------------
print(f'Faltam {delta.days} dias e {delta.seconds//60//60} horas para o meu aniversário.')

# *Lembrando que // retorna a divisão inteira

# Exemplo de boleto com vencimento para daqui 3 dias ----------------------------------------------
regra_vencimento = datetime.timedelta(days=3)
data_vencimento = data_hoje + regra_vencimento
print(f'A data de vencimento do boleto - {data_vencimento}')

print(type(regra_vencimento))  # <class 'datetime.timedelta'>
print(regra_vencimento)        # 3 days, 0:00:00
