"""
Escrevendo em arquivos

write() - utilizamos a função write() para escrever em arquivos, que recebe por parâmetro "uma string"

Por padrão abrimos o arquivo no mode de leitura, mode='r', quando queremos abrir um arquivo escrito devemos
abrir com mode='w'

Ao abrir uma arquivo para escrita, o arquivo é criado no sistema operacional caso ele ainda não exista.
Caso ele já exista todo conteúdo anterior que existia será apagado e sobrescrito com a nova entrada.

"""
# Forma Pythônica de se escrever em um arquivo ----------------------------------------------------
with open('text2.txt', mode='w', encoding='UTF-8') as arquivo:
    arquivo.write('Arquivo criado na aula 53_escrever_em_arquivo.py\n')
    arquivo.write('Escrever em um arquivo com Python é muito fácil\n')
    arquivo.write('Podemos colocar quantas linhas quisermos\n')
    arquivo.write('Essa é a última linha\n')

# Forma não Pythônica de se escrever em um arquivo ------------------------------------------------
arquivo = open('text3.txt', 'w', encoding='UTF-8')
arquivo.write('Arquivo criado na aula 53_escrever_em_arquivo.py\n')
arquivo.write('Escrever em um arquivo com Python é muito fácil\n')
arquivo.write('Podemos colocar quantas linhas quisermos\n')
arquivo.write('Essa é a última linha\n')
arquivo.write((('Geek ' * 20) + '\n') * 50)  # trabalhando com string, 20 Geeks por linha em 50 linhas
arquivo.close()

# Recebendo entrada do usuário---------------------------------------------------------------------
with open('text4.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Arquivo criado na aula 53_escrever_em_arquivo.py\n')
    arquivo.write('Lista de frutas criada a partir da entrada do usuário\n')

    while True:
        fruta = input('Informe a fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
