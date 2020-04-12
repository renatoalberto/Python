"""
POO - Métodos

Métodos (funções) - Representam o comportamento do objeto. Ou Seja, As ações que este objeto pode realizar
                    no seu sistema.

Em Python, dividimos os métodos em 3 grupos:
  - Métodos de instância
  - Métodos de classe
  - Métodos estáticos

Métodos de Instância
  - O método dunder init "__init__", é um método especial chamado de construtor e sua função é construir
    o objeto a partir da classe
  - Métodos específicos do objeto
  - Visibilidade, métodos privados criados com duplo underline "__"

Métodos de Classe
  - Conhecidos como estáticos em outras linguagens
  - Tem acesso a classe
  - É decorado com @classmethod
  - recebe por parâmetro "cls" referência para própria classe
  - Métodos comum a todos os objetos
  - Não permite acesso a atributos de instância
  - Quando um método não acessa nenhum atributo de instância, o próprio Pycharm recomenda criação método estático

Métodos estático
  - É decorado com @staticmethod
  - Não tem acesso a classe
  - Não permite acesso a atributos de instância

Obs:
  - Todo elemento em Python que inicia e finaliza em duplo underline de chamado de dunder (Double Underline)
  - Os elementos dunder em Python são chamados de métodos mágicos
  - Apesar de ser possível criar funções dunder, não é recomendado, por risco de alterar o comportamento de
    alguma função interna do Python. Evite, de preferência nunca o faça.

Obs2:
  - Métodos são nomeado com letras minúsculas, em caso de nome comporto, o nome terá as palavras por underline
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


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo

        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return self.__valor * (1 - (porcentagem/100))


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Quantidade de usuários registrados: {Usuario.contador}')

    @staticmethod
    def definicao():
        return 'UXE3154'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email

        Usuario.contador = self.__id

        # rounds - vai realizar 200000 embaralhamentos
        # salt_size - tamanho da parte do texto que será juntada
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

        print(f'Usuário criado {self.__gera_usuario()}')

    def correr(self, metros):
        print(f'{self.__nome} está correndo {metros} metros.')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # Método privado, criado com duplo underline, acessível somente dentro da classe
    def __gera_usuario(self):
        return self.__email.split('@')[0]



produto1 = Produto('Playstation 4', 'Video Game', 2300)
print(f'Aplicando 10% de desconto {produto1.desconto(10)}')

# é possível chamar um método a partir da classe
print(f'Aplicando 10% de desconto {Produto.desconto(produto1, 10)}')

usuario1 = Usuario('Renato', 'Alberto', 'renato.alb@gmail.com', '123456')
usuario2 = Usuario('Raíssa', 'Alberto', 'raissa.alb@gmail.com', '321654')

print(f'Nome completo do usuario1 - {usuario1.nome_completo()}')
print(f'Nome completo do usuario2 - {usuario2.nome_completo()}')

print(f'Senha do usuario1 - {usuario1._Usuario__senha}')  # Senha cifrada, modo de recuperação não recomendado
print(f'Senha do usuario2 - {usuario2._Usuario__senha}')  # Senha cifrada, modo de recuperação não recomendado

senha = input('Informe a senha do usuário 1: ')

if usuario1.checa_senha(senha):
    print(f'Acesso liberado')
else:
    print(f'Senha incorreta')

# Métodos de Classe -------------------------------------------------------------------------------
Usuario.conta_usuarios()   # Forma correta de para acessar um método de classe
usuario1.conta_usuarios()  # Forma não recomendada, a partir de um objeto

# Método Privado ----------------------------------------------------------------------------------
# print(usuario1.__gera_usuario())        # Acesso direto gera erro - AttributeError
print(usuario1._Usuario__gera_usuario())  # Name Mangling, acesso não recomendado, fora da classe

# Método Estático ---------------------------------------------------------------------------------
print(f'Contador  a partir da classe - {Usuario.contador}')
print(f'Definição a partir da classe - {Usuario.definicao()}')
print(f'Contador  a partir do objeto - {usuario1.contador}')
print(f'Definição a partir do objeto - {usuario1.definicao()}')
