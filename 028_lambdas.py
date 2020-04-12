"""
Utilizando Lambdas

- Conhecidas por expressões lambdas, ou simplesmente lambdas, são funções sem nome, ou seja, funções anônimas

Sintaxe - lambda x1, x2, x3, ..., xn: <expressão>

dois pontos separam os parâmetros da expressão a ser executada
"""
# Modo básico de expressão lambda --------------------------------------------------------------------------------------
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' renato ', ' alberto '))

# Obs: Quantidade de argumentos deve ser a mesma quantidade de parâmetros


# Modo mais interessante de expressão lambda ---------------------------------------------------------------------------
autores = ['Arthur C. Clarke', 'Douglas Adams', 'Walter Lippmann', 'Arthur M. Schlesinger', 'Joseph Wood Krutch',
         'Buckminster Fuller', 'Omar Bradley', 'Reece Elizabeth', 'John Lasseter', 'Sydney J. Harris']

# cada nome passa pelo parâmetro da expressão lambda, é transformado em 'último sobrenome' e utilizado na classificação
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Função Quadrática - f(x) = a * x ** 2 + b * x + c --------------------------------------------------------------------
def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = funcao_quadratica(2, 3, -5)  # retorna a expressão lambda que recebe x como parâmetro
print(teste(0))                      # executa passado o argumento x
print(teste(1))                      # executa passado o argumento x
print(teste(2))                      # executa passado o argumento x
