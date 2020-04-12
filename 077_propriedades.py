"""
POO - Propriedades - Properties

Em algumas linguagens de programação como java ao declararmos um atributo privado na classe,
é de costume criar métodos públicos para manipulação desses atributos, esses métodos são conhecidos
por getters e setters, onde getters retornam os valores desses atributos e setters alteram os valores dos mesmos,
que funciona bem em Python, mas não a forma pythonica.

    # (getters e setters) - forma e nomenclatura estilo java
    def get_conta(self):
        return self.__conta

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite = limite

- Em Python criamos métodos decorados com @property quando queremos ter acesso aos atributos de uma classe:

    DECLARAÇÃO                                 |    ACESSO
    -------------------------------------------|------------------------------------------
    @property                                  | conta1 = Conta('Renato', 5000, 2000)
    def titular(self):                         | print(conta1.titular)
        return self.__titular                  |

- É possível criar novos atributos a partir de métodos decorados com @property:

    DECLARAÇÃO                                 |    ACESSO
    -------------------------------------------|------------------------------------------
    @property                                  | conta1 = Conta('Renato', 5000, 2000)
    def saldo_total(self):                     | print(conta1.saldo_total)
        return self.__saldo + self.__limite    |

- Quando queremos alterar o valor de um atributo privado em Python criamos métodos decorados com @atributo_setter

    DECLARAÇÃO                                 |    ACESSO
    -------------------------------------------|------------------------------------------
    @limite.setter                             | conta1 = Conta('Renato', 5000, 2000)
    def limite(self, novo_valor):              | conta1.limite = 2500
        self.__limite = novo_valor             |

"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__conta = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__conta

    @property
    def conta(self):
        return self.__conta

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_valor):
        self.__limite = novo_valor

    # Aqui criamos uma "nova propriedade" que retornará a soma de saldo mais limite
    @property
    def saldo_total(self):
        return self.__saldo + self.__limite

    def extrato(self):
        return f'Conta {self.__conta} - titular {self.__titular}, saldo R${self.__saldo} mais limite de {self.__limite}'

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, contar_destino):
        self.sacar(valor)
        contar_destino.depositar(valor)


conta1 = Conta('Renato', 5000, 2000)
conta2 = Conta('Raíssa', 900, 500)

print(conta1.extrato())
print(conta2.extrato())

conta1.transferir(100, conta2)

print(conta1.extrato())
print(conta2.extrato())

# utilizando @property é possível ter acesso controlado aos atributos de uma classe
print(f'Soma do saldo das 2 contas {conta1.saldo + conta2.saldo}')

# atribuindo valor a um atributo utilizando @limite.setter
conta1.limite = 2500
print(conta1.extrato())

# acessando a nova propriedade saldo_total
print(f'O saldo total da Conta {conta1.conta} é de {conta1.saldo_total}')
