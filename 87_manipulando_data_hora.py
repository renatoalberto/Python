"""
Manipulando Data e Hora

Python tem um módulo builtin para se trabalhar com data e hora chamada datetime
"""
import datetime

# 'MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time',
# 'timedelta', 'timezone', 'tzinfo'
print(dir(datetime))

print(datetime.MAXYEAR)  # Maior ano possível - 9999
print(datetime.MINYEAR)  # Menor ano possível - 1

# '__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__',
# '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__',
# '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar',
# 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max',
# 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time',
# 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow',
# 'utcoffset', 'utctimetuple', 'weekday', 'year']
print(dir(datetime.datetime))

# Retorna data e hora corrente, formato - 2020-02-15 09:53:10.768319 ------------------------------
print(datetime.datetime.now())

# Representação -----------------------------------------------------------------------------------
# datetime.datetime(year, month, day, hour, minute, second, microsecond)
# datetime.datetime(2020, 2, 15, 9, 55, 53, 590948)
print(repr(datetime.datetime.now()))

# replace() para ajustar o data/hora --------------------------------------------------------------
inicio = datetime.datetime.now()
print(inicio)
inicio = inicio.replace(minute=0, second=0, microsecond=0)
print(inicio)

# Criando uma data/hora ---------------------------------------------------------------------------
evento = datetime.datetime(2020, 7, 7)
print(f'O aniversário do Renato será {evento}, tragam presentes.')

# Criando uma data a partir de dados informador pelo usuário --------------------------------------
# nascimento = input('Informe a data do seu nascimento no formato dd/mm/yyyy: ')
nascimento = '07/07/1983'
print(f'{nascimento} - {type(nascimento)}')
dia, mes, ano = nascimento.split('/')
nascimento = datetime.datetime(year=int(ano), month=int(mes), day=int(dia))
print(f'{nascimento} - {type(nascimento)}')

# Acessando os elementos individualmente ----------------------------------------------------------
agora = datetime.datetime.now()
print(f'Ano          - {agora.year}')
print(f'Mês          - {agora.month}')
print(f'Dia          - {agora.day}')
print(f'Hora         - {agora.hour}')
print(f'Minuto       - {agora.minute}')
print(f'Segundo      - {agora.second}')
print(f'Milissegundo - {agora.microsecond}')
