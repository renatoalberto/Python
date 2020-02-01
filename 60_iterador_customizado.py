"""
Escrevendo um iterador customizado

Para criar um iterador customizado, basta declarar as duas funções:
 - __iter__(self)
 - __next__(self)
"""
# função range() comum
for num in range(10):
    print(f'{num} ', end='')
print('')


# iterador personalizado, simulando o range
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero

        raise StopIteration


con = Contador(0, 10)

print(f'Menor - {con.menor}')
print(f'Maior - {con.maior}')

itr = iter(con)

while True:
    try:
        print(f'{next(itr)} ', end='')
    except StopIteration:
        print('')
        break
