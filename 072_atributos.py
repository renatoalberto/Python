"""
POO - Atributos

Representa as características do objeto, ou seja, pelos atributos nós conseguimos representar computacionalmente os
estados de um objeto.

Atributos em Python podem ser divididos em 3 grupos:
  - Atributos de instância
  - Atributos de classe
  - Atributos dinâmicos

Atributos de instância:
  - São atributos declarados dentro do método *construtor (método especial para construção de objetos)
  - Todas as instâncias terão esses mesmos atributos particulares
  - Atributos individuais para cada objeto gerado, cada instância criada

Atributos de classe:
  - São atributos declarados diretamente na classe, fora do construtor
  - Geralmente inicializamos com um valor
  - Valor compartilhado entre todas as instâncias da classe, todas as instâncias terão o mesmo valor para esse atributo
  - O armazenamento é único para todas as instâncias, se existirem mil objetos, só existirá uma única alocação de
    em memória para atributo de classe para todos os objetos gerados
  - Em java são chamados de atributos estáticos

Atributos dinâmicos:
  - Atributo criado em tempo de execução
  - Atributo exclusivo da instância que o criou


Visibilidade - em Python ficou estabelecido que todo os atributos declarados são considerados públicos,
               ou Seja, pode ser acessado em todo o projeto.
               Caso queiramos declarar um atributo como privado, ou seja, acessível somente dentro da própria
               classe onde foi declarado, devemos utilizar __ duplo underscore no início do nome.

__ duplo underscore - conhecido como Name Mangling.

"""


# Declaração de atributos de instância ------------------------------------------------------------
# self - nome por convenção, é uma referência para o próprio objeto,
#        podemos renomear, mas não é recomendado
# Classe com atributos de instância público
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Visibilidade de atributos de instância (Público ou Privado)--------------------------------------
# Classe com atributo de instância "senha" privado, declarado com __ duplo underscore
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        return self.__senha

    def mostra_email(self):
        return self.email


# Obs: Lembre-se que atributos privados, criado com duplo underscore é apenas uma convenção, ou seja,
#      a linguagem Python não vai impedir que façamos acesso direto aos atributos sinalizados como privados
#      fora da classe.

# Exemplo
user = Acesso('user@gmail.com', '123456')

# Acessando o atributo de instância público email
print(f'email: {user.email}')
print(f'email: {user.mostra_email()}')

# Acessando o atributo de instância privado senha
# print(f'senha: {user.__senha}')  # aqui retorna um erro - AttributeError

# Mas podemos verificar com dir() que o atributo senha pode ser acessível com _Acesso__senha
# Apesar de termos acesso, não é recomendado acessarmos diretamente esses atributos
print(dir(user))
print(f'senha - {user._Acesso__senha}')  # Name Mangling

# Forma correta de acessar a senha é a partir do método mostra_senha()
print(f'senha - {user.mostra_senha()}')

# Todas as instâncias terão esses mesmos "atributos de instância"
user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

print(user1.email)
print(user1.mostra_senha())
print(user2.email)
print(user2.mostra_senha())


# Declaração de atributos de classe  --------------------------------------------------------------
#  - São atributos declarados diretamente na classe, fora do construtor
#  - Geralmente inicializamos com um valor
#  - Valor compartilhado entre todas as instâncias da classe, todas as instâncias terão o mesmo valor para esse atributo

# Refatorando a classe Produto
class Produto:

    # imposto - atributo de classe
    imposto = 1.05  # equivale a 0,05% de imposto

    # contador - atributo de classe
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto

        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Vídeo Game', 2300)
p2 = Produto('Xbox S', 'Vídeo Game', 2500)

print(f'Imposto do produto p1 {p1.imposto}, valor {p1.valor}')
print(f'Imposto do produto p2 {p2.imposto}, valor {p2.valor}')

# Não é necessário criar uma instância para acessar um atributo de classe
print(f'Valor do imposto, diretamente da classe {Produto.imposto}')

print(f'id do produto p1 - {p1.id}')
print(f'id do produto p2 - {p2.id}')
print(f'Quantidade de produtos instânciados - {Produto.contador}')

# Declaração de atributos dinâmico  ---------------------------------------------------------------
# criando um atributo dinâmico em tempo de execução
p3 = Produto('Arroz', 'Mercearia', 18)
p3.peso = '5kg'  # Note que a classe Produto não existe o atributo peso

print(f'Somente o objeto p3 possui o atributo peso - {p3.peso}')
# print(f'Produto p1 não possui o atributo peso {p1.peso}')  # AttributeError

# Apresentando toda a estrutura de um objeto "__dict__" em forma de um dicionário
print(p1.__dict__)  # {'id': 1, 'nome': 'Playstation 4', 'descricao': 'Vídeo Game', 'valor': 2415.0}
print(p3.__dict__)  # {'id': 3, 'nome': 'Arroz', 'descricao': 'Mercearia', 'valor': 18.900000000000002, 'peso': '5kg'}

# Deleção de um atributo
del p3.peso       # deleção de um atributo dinâmico
del p3.valor      # deleção de um atributo de instância
# del p3.imposto  # deleção de um atributo de classe NÃO PERMITIDA - AttributeError

print(p3.__dict__)  # {'id': 3, 'nome': 'Arroz', 'descricao': 'Mercearia'}
