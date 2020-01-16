"""
Tipo String
"""
texto1 = 'Renato'            # Aspas simples - Mais comum
texto2 = "Raíssa"            # Aspas duplas
texto3 = '''Nick'''          # Aspas simples triplas
texto4 = """McDonald's"""    # Aspas duplas  triplas

print(texto1)
print(texto2)
print(texto3)
print(texto4)
print(type(texto1))

# Quebra de linha
texto1 = 'Renato \nTrabalha no Banco do Brasil'
print(texto1)

texto1 = """Renato
Trabalha no Banco do Brasil"""
print(texto1)

# Métodos string
#         012345678901234
texto1 = 'Geek University'
print(texto1.upper())  # Maiúsculo
print(texto1.lower())  # Minúsculo
print(texto1.title())  # Primeira letra em maiúsculo
print(texto1.split())  # Divide palavras em uma lista

# Escreve parte do texto - Slice de string
print(texto1[0:4])    # Da posição 0 até antes da posição 4
print(texto1[5:15])   # Da posição 5 até antes da posição 15

# split - Divide palavras em lista
print(texto1.split()[0])  # Geek
print(texto1.split()[1])  # University

# Comece do primeiro elemento e vá até o ultimo elemento e inverta
print(texto1[::-1])   # Pythônico - inversão da string

# Replace - mudar uma letra por outra
print(texto1.replace('e', 'i'))
