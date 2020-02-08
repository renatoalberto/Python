"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular o código nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular - com as classes é possível encapsular, englobar, nosso atributos e métodos, de forma agrupada, organizada,
             dentro de um grupo lógico e hierárquico.

Abstração  - com a linguagem Python não é possível bloquear o acesso aos nossos atributos e métodos privados, utilizamos
             na verdade, uma convenção, nomeando com duplo underline os nomes desses atributos e métodos, exemplo seria
             um atributo __nome e método __falar(). Esses elementos deveriam ser acessados somente dentro da classe,
             mas o Python não bloqueia esse acesso, entretanto ocorre um fenômeno chamado Name Mangling, que faz uma
             alteração na forma de se acessar os elementos privados, conforme _Classe__nome, entretanto não recomendado.
           - Abstração, em POO, é o ato de expor somente dados relevantes de uma classe, escondendo atributos e métodos
             privados do usuário.
           - Quando realizamos uma chamada, desbloqueamos o telefone, discamos um número, conversamos, e finalizamos a
             conversa. Nesse exemplo é possível perceber que não importa para o usuário que o celular se conecte a uma
             central telefônica, busque em uma base de dados o numero requerido, realize a conexão, gerenciando o tempo
             e a qualidade da chamada. Isso porque os passos que não são relevantes para o usuário são ABSTRAÍDOS.
"""


class Conta:
    contador = 399

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador + 1
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador = self.numero

    def extrato(self):
        print(f'O saldo do(a) {self.titular} é de {self.saldo}')

    def depositar(self, valor):
        if self.__valida_valor(valor):
            self.saldo += valor
        else:
            print('Valor informado inválido, não é possível depositar valor negativo.')

    def sacar(self, valor):
        if self.__valida_valor(valor):
            self.saldo -= valor
        else:
            print('Valor informado inválido. não é possível sacar valor negativo.')

    def transferir(self, valor, conta_credora):
        self.sacar(valor)
        conta_credora.depositar(valor)

    # método privado
    @staticmethod
    def __valida_valor(valor):
        return valor > 0


# Testando a classe
conta3 = Conta('University', 600, 1000)
conta1 = Conta('Geek', 500, 2000)

print(conta1.__dict__)
conta1.extrato()
conta1.depositar(150)
conta1.extrato()
conta1.depositar(-150)
conta1.extrato()
conta1.sacar(-150)
conta1.extrato()

conta1.transferir(100, conta3)
conta1.extrato()
conta3.extrato()

conta1.transferir(-100, conta3)
conta1.extrato()
conta3.extrato()


# Com dados público é possível realizar as seguintes ações, demonstrando a baixa segurança da aplicação
conta1.titular = 'Xuxa'
conta1.saldo = 999999999
conta1.limite = 99999999999
conta1.numero = 456
print(conta1.__dict__)
conta1.extrato()


# Refatorando -------------------------------------------------------------------------------------
class Conta2:
    contador = 399

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        print(f'O saldo do(a) {self.__titular} é de {self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


# Testando a classe
conta2 = Conta2('Geek', 500, 2000)
print(conta2.__dict__)
conta2.extrato()

# Com dados privados é possível limitar o acesso aos atributos diretamente, gerando erro AttributeError
# print(conta2.__titular)  # AttributeError: 'Conta2' object has no attribute '__titular'
# print(conta2.__saldo)    # AttributeError: 'Conta2' object has no attribute '__saldo'
# print(conta2.__limite)   # AttributeError: 'Conta2' object has no attribute '__limite'
# print(conta2.__numero)   # AttributeError: 'Conta2' object has no attribute '__numero'

# Com dados privados, apesar de limitar, não bloqueia, continuando acessível com Name Mangling, não recomendado
print(conta2._Conta2__titular)
print(conta2._Conta2__saldo)
print(conta2._Conta2__limite)
print(conta2._Conta2__numero)

# Com Name Mangling permite tanto imprimir o valor, quanto alterar
conta2._Conta2__titular = 'Renato'
print(conta2.__dict__)
