"""
Métodos Data Hora

https://docs.python.org/3/library/datetime.html
"""
from textblob import TextBlob
import datetime, timeit, functools

# Com now podemos especificar um timezone (Fuso Horário) ------------------------------------------
agora = datetime.datetime.now()
print(agora)                 # 2020-02-15 21:38:26.996746
print(type(agora))           # <class 'datetime.datetime'>
print(repr(agora))           # datetime.datetime(2020, 2, 15, 21, 38, 26, 996746)

print()

# Com today NÃO é possível especificar um timezone (Fuso Horário) ---------------------------------
hoje = datetime.datetime.today()
print(hoje)                  # 2020-02-15 21:38:26.996747
print(type(hoje))            # <class 'datetime.datetime'>
print(repr(hoje))            # datetime.datetime(2020, 2, 15, 21, 38, 26, 996747)

print()

# Manutenção ocorrendo a meia noite (combine) -------------------------------------------------------
# datetime.time() -> quando vazio, zera as horas, minutos e segundos
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)            # 2020-02-16 00:00:00
print(type(manutencao))      # <class 'datetime.datetime'>
print(repr(manutencao))      # datetime.datetime(2020, 2, 16, 0, 0)

print()

# Encontrando o dia da semana com weekday() -------------------------------------------------------
# weekday() retorna de 0 a 6:
# 0 - Segunda-Feira | 1 - Terça-Feira | 2 - Quarta-Feira | 3 - Quinta-Feira
# 4 - Sexta-Feira   | 5 - Sábado      | 6 - Domingo

print(hoje.weekday())        # 5
print(manutencao.weekday())  # 6

print()

# Outro exemplo com aniversário
# aniversario = input('Informa a data do seu aniversario no formato DD/MM/YYYY: ')
aniversario = '07/07/1983'
dia, mes, ano = aniversario.split('/')
aniversario = datetime.datetime(year=int(ano), month=int(mes), day=int(dia))

if aniversario.weekday() == 0:
    print(f'Você nasceu em uma Segunda-Feira')
elif aniversario.weekday() == 1:
    print(f'Você nasceu em uma Terça-Feira')
elif aniversario.weekday() == 2:
    print(f'Você nasceu em uma Quarta-Feira')
elif aniversario.weekday() == 3:
    print(f'Você nasceu em uma Quinta-Feira')
elif aniversario.weekday() == 4:
    print(f'Você nasceu em uma Sexta-Feira')
elif aniversario.weekday() == 5:
    print(f'Você nasceu em uma Sábado')
elif aniversario.weekday() == 6:
    print(f'Você nasceu em um Domingo')

print()

# Formatando datas/horas com strftime() (String Format Time) --------------------------------------
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)        # 15/02/2020
print(type(hoje_formatado))  # <class 'str'> *Retorna uma string

print()


# Formatação manual q=/ ----------------------------------------------------------------------------
def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    else:
        return f'{data.day} de Dezembro de {data.year}'


print(formata_data(hoje))    # 15 de Fevereiro de 2020


# Formatando utilizando a biblioteca de tradução TextBlob -----------------------------------------
# strftime('%B') - Retornar o mês em inglês
def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br').title()} de {data.year}"


hoje = datetime.datetime.now()
print(formata_data(hoje))    # 15 de Fevereiro de 2020

print()

# Convertendo texto para um datetime com o método strptime() --------------------------------------
# facilita, não necessita fazer split e converter para int, é direto
nascimento = datetime.datetime.strptime('07/07/1983', '%d/%m/%Y')
print(nascimento)            # 1983-07-07 00:00:00
print(type(nascimento))      # <class 'datetime.datetime'>

print()

# Trabalhar somente com a hora utilizando o método time() -----------------------------------------
# time recebe 3 parâmetro, hora, minuto e segundo
almoco = datetime.time(12, 30, 0)
print(almoco)                # 12:30:00
print(type(almoco))          # <class 'datetime.time'>

print()

# Marcando o tempo de processamento com timeit ----------------------------------------------------
# timeit sabe o tempo de início e fim, retornando o tempo gasto
# timeit recebe dois parâmetro:
#   - 1ª uma expressão que queremos testar
#   - 2ª número de vezes queremos executar

# entendo o que acontece
print("-".join(str(n) for n in range(100)))  # 0-1-2-3-4-5-6-7-8-9-... até -99-100

# Testando generator -------------
objeto = (str(n) for n in range(100))
print(type(objeto))        # <class 'generator'>
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)                 # 0.43643410000000005

# Testando list comprehension ----
objeto = [str(n) for n in range(100)]
print(type(objeto))
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)                 # 0.3666969

# Testando set comprehension -----
objeto = {str(n) for n in range(100)}
print(type(objeto))
tempo = timeit.timeit('"-".join({str(n) for n in range(100)})', number=10000)
print(tempo)                 # 0.4704051

# Testando map -------------------
objeto = map(str, range(100))
print(type(objeto))
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)                 # 0.3229008999999998 campeão


# Marcando o tempo de processamento de uma função com functools.partial() -------------------------
# partial recebe dois parâmetros:
#  - 1ª uma função
#  - 2ª dado de entrada da função passada por parâmetro
def funcao_qualquer(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


tempo = timeit.timeit(functools.partial(funcao_qualquer, 2), number=1000)
print(tempo)                 # 3.2741505999999996
