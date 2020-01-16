"""
recebendo dados do usuário
input() - Todo dado recebido via input() é uma string

"""
# Entrada de dados
# input() Em 1 linha
nome = input("Qual o seu nome?").title()

# input() Em 2 linha
print('Quantos anos você tem?')
idade = input()

# Processamento

# Saída de Dados
# print antigo - exemplo versão 2.x do python
print('Seja bem vindo(a) %s, você tem %s anos' % (nome, idade))

# print moderno - exemplo versão 3.x do python
print('Seja bem vindo(a) {0}, você tem {1} anos'.format(nome, idade))

# print moderno - exemplo versão 3.7 do python
print(f'Seja bem vindo(a) {nome}, você tem {idade} anos')
print(f'O(A) {nome} nasceu no ano {2019 - int(idade)}')

