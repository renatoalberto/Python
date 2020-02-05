"""
Ranges
- Precisamos conhecer o loop for para trabalhar com ranges
- Precisamos conhecer o range para trabalhar melhor com loops for


"""
# range(valor_de_parada)
# início do 0 até o valor de parada não inclusivo
for num in range(11):
    print(num, end=' ')
print('')

# range(valor_de_início, valor_de_parada)
# início especificado até o valor de parada não inclusivo
for num in range(5, 11):
    print(num, end=' ')
print('')

# range(valor_de_início, valor_de_parada, valor_do_passo)
# início especificado até o valor de parada não inclusivo com passo especificado pelo usuário
for num in range(5, 11, 2):
    print(num, end=' ')
print('')

# range(valor_de_início, valor_de_parada, valor_do_passo) * inversa
# início especificado até o valor de parada não inclusivo com passo especificado pelo usuário negativo
for num in range(10, 0, -1):
    print(f'{num}', end=' ')
print('')
