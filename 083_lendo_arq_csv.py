"""
Lendo arquivos CSV - Comma Separated Values - Valores separados por vírgula

PORTAL BRASILEIRO DE DADOS ABERTOS: http://dados.gov.br/dataset

# Separador por vírgula:
1, 2, 3, 4, 5, 6
"geek", "university", "python", "ciências", "dados"

# Separador ponto e vírgula
1; 2; 3; 4; 5; 6
"geek"; "university"; "python"; "ciências"; "dados"

# Separador por espaços
1 2 3 4 5 6
"geek" "university" "python" "ciências" "dados"

A linguagem Python possui duas formas para ler arquivos CSS:
   - reader     -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
   - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderDicts.

"""
from csv import reader, DictReader

# É possível ir lapidando o registro para conseguir separar os dados, mas não é o ideal (trabalhoso)
with open("lutadores.csv", encoding='utf-8') as arquivo:
    dados = arquivo.read()
    dados = dados.split('\n')
    dados = [dado.split(',') for idx, dado in enumerate(dados) if idx > 0]  # pular o cabeçalho
    for dado in dados:
        print(f'{dado[0]} nasceu no {dado[1]} e mede {dado[2]}cm')

print()

# Reader ------------------------------------------------------------------------------------------
# reader(arquivo, delimiter=",") => use delimiter quando limitador diferente de vírgula
with open("lutadores.csv", encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # pular o cabeçalho
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no {linha[1]} e mede {linha[2]}cm')

print()

# DictReader --------------------------------------------------------------------------------------
# No dicionário não precisa pular o cabeçalho, pois o usa como chave
# DictReader(arquivo, delimiter=",") => use delimiter quando limitador diferente de vírgula
with open("lutadores.csv", encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f'{linha["Nome"]} nasceu no {linha["País"]} e mede {linha["Altura (em cm)"]}')
