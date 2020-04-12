"""
POO - Objetos

Objetos -> São instâncias da classe, ou seja, após o mapeamento do objeto no mundo real para sua
           representação computacional, devemos poder criar quantos objetos forem necessários.
           Podemos pensar em objetos/instâncias de uma classe com variável do tipo definido da classe.
"""
# Biblioteca para criptografia de senha
# Necessário instalação: pip install passlib
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def lampada_ligada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome


class Cliente:
    def __init__(self, usuario, cpf):
        self.__usuario = usuario
        self.__cpf = cpf

    def recupera_nome_usuario(self):
        return self.__usuario.get_nome() + ' ' + self.__usuario.get_sobrenome()


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.limite = limite
        self.__saldo = saldo
        self.__cliente = cliente

        ContaCorrente.contador = self.__numero

    def recupera_cliente_cliente(self):
        return self.__cliente.recupera_nome_usuario()


# instância/objeto --------------------------------------------------------------------------------
lamp = Lampada('Branca', 220, 60)

print(f'Lâmpada ligada? {lamp.lampada_ligada()}')
lamp.ligar_desligar()
print(f'Lâmpada ligada? {lamp.lampada_ligada()}')

# Observe que uma classe pode receber um objeto por parâmetro
user = Usuario('Renato', 'Alberto', 'renato.alb@gmail.com', '123456')
cli1 = Cliente(user, 984_600_647_15)
cont = ContaCorrente(2000, 500, cli1)

# Apresentando toda a estrutura de um objeto "__dict__" em forma de um dicionário
print(cont.__dict__)
print(cont._ContaCorrente__cliente.__dict__)
print(cont._ContaCorrente__cliente._Cliente__usuario.__dict__)

# Recuperando atributo de classe
print(user._Usuario__nome + ' ' + user._Usuario__sobrenome)  # A partir do usuário - Name Mangling, não recomendado

print(user.get_nome() + ' ' + user.get_sobrenome())    # A partir do usuário
print(cli1.recupera_nome_usuario())                    # A partir do cliente
print(cont.recupera_cliente_cliente())                 # A partir da conta corrente
