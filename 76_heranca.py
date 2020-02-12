"""
POO - Herança (Inheritance)

Herança - Reaproveitamento de código. Também extender nossas classes. Com a herança, a partir de uma classe já
          existente, nós estendemos novas classes que passam a herdar atributos e métodos da classe herdada.

* Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?

- sintaxe de herança, representando Cliente herda Pessoa - class Cliente(Pessoa):
- A partir do momento que ocorre a herança, quem herda passa a ter também os atributos e métodos da classe herdada
- A atribuição dos valores da classe herdada é feita a partir do método super(): super().__init__(nome, sobrenome, cpf)

A classe herdada (Pessoa) é conhecida como:
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Super Classe
    - Classe Genérica

A classe herda (Cliente, Funcionário) é conhecida como:
    - Sub Classe
    - Classe Filha
    - Classe Específica

Sobrescrita de método (Overriding)
    - Ocorre quando reescrevemos um método da classe pai na classe filha
"""


# Forma redundante, evite.
class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return self.__nome + ' ' + self.__sobrenome


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return self.__nome + ' ' + self.__sobrenome


cliente1 = Cliente('Renato', 'Alberto', '984.600.698-75', 3000)
funcionario1 = Funcionario('Raíssa', 'Alberto', '117.358+745-60', 7000)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


# Forma correta, sem redundâncias, utilizando herança ---------------------------------------------
class Pessoa2:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    # Sobrescrita de método da classe pai
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


class Cliente2(Pessoa2):
    """Cliente2 é uma Classe Filha que herda da Classe Pai Pessoa2"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa2.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        # super().__init__(nome, sobrenome, cpf)      # Forma comum de acessar dados da super classe
        self.renda = renda

    # Sobrescrita de método da classe pai
    def nome_completo(self):
        return f'Olá, sou o cliente {super().nome_completo()}'


class Funcionario2(Pessoa2):
    """Funcionario2 é uma Classe Filha que herda da Classe Pai Pessoa2"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        # Pessoa2.__init__(self, nome, sobrenome, cpf)    # Forma não comum de acessar dados da super classe
        super().__init__(nome, sobrenome, cpf)            # Forma comum de acessar dados da super classe
        self.matricula = matricula

    def nome_completo(self):
        return f'Olá, sou o funcionário {super().nome_completo()}'


cliente2 = Cliente2('Renato', 'Alberto', '984.600.698-75', 3000)
funcionario2 = Funcionario2('Raíssa', 'Alberto', '117.358+745-60', 7000)

print(cliente2.nome_completo())
print(funcionario2.nome_completo())

print(cliente2.__dict__)
print(funcionario2.__dict__)
