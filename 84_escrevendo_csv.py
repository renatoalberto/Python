"""
Escrevendo arquivos CSV

reader()     <=> writer()
DictReader() <=> DictWriter()
"""
from csv import writer, DictWriter

# writer()   - gera um objeto para que possamos escrever em um arquivo csv ------------------------
# writerow() - método para escrever cada linha, recebe uma lista
# newline='' evita acréscimo automático de uma linha em branco
with open('filmes.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme ("sair" para finalizar) ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme ')
            duracao = input('Informe a duração do filme ')
            escritor_csv.writerow([filme, genero, duracao])

# DictWriter() ------------------------------------------------------------------------------------
# Obs: as chaves do dicionário deve ser as mesmas do cabeçalho
# newline='' evita acréscimo automático de uma linha em branco
with open('filmes2.csv', 'w', encoding='utf-8', newline='') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme ("sair" para finalizar) ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme ')
            duracao = input('Informe a duração do filme ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
