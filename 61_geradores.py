"""
Geradores

- Geradores (generator) são iteradores (iterators)

Obs: O contrário não é verdadeiro, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Generators podem ser criados com expressões geradoras;
- Funções geradoras utilizam a palavra reservada yield;

Diferenças entre Funções e Generator Function (Função Geradora)

----------------------------------------------------------------------------------------
| Funções                                  | Generator Function                        |
|------------------------------------------|-------------------------------------------|
| Utilizam return                          | Utilizam yield                            |
| Retorna uma única vez                    | Retornam yield múltiplas vezes            |
| Quando executada retorna um valor        | Quando executada retorna um generator     |
----------------------------------------------------------------------------------------

"""


# Exemplo de Generator Function -------------------------------------------------------------------
def conta_ate(valor_maximo):
    contador = 1

    while contador <= valor_maximo:
        yield contador
        contador += 1


# Uma Generator Function não é um Generator, ela gera um generator, ok?
gen = conta_ate(10)
print(type(gen))        # generator

while True:
    try:
        print(f'{next(gen)}', end=' ')
    except StopIteration:
        print('')
        break

# Mesmo exemplo com for
gen = conta_ate(10)

for num in gen:
    print(num, end=' ')
print('')

# Transformando o retorno numa lista
lista = list(conta_ate(10))
print(type(lista))           # list
print(lista)
