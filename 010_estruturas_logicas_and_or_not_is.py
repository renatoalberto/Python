"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários: not, is
Operadores binários: and, not
"""
ativo, logado = False, False

if ativo and logado:
    print('Bem vindo usuário!')
elif not ativo:
    print('Você precisa ativar sua conta. Por favor cheque seu email.')
else:
    print('Efetue o log no sistema.')

# is o valor é comparado com um segundo
numero = 101
media = 10

if numero is media:
    print('Número é uma média')
else:
    print(f'Número não é uma média, {numero}.')
