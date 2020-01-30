""""
StringIO

Pare ler ou escrever dados em um arquivo do sistema operacional o software precisa ter permissão:
   - Permissão de leitura -> Para ler o arquivo;
   - Permissão de escrita -> Para escrever o arquivo.

StringIO - Utilizado para ler e criar arquivo em memória
"""
# Primeiramente fazemos o import
from io import StringIO

mensagem = 'Essa é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
# Equivalente a: open('texto.txt', 'w')
arquivo = StringIO(mensagem)

# Agora que temos um arquivo, podemos fazer tudo que sabemos
print(arquivo.read())

# Podemos inserir outro texto
print(arquivo.write('\nOutro texto para teste de write.'))
arquivo.seek(0)
print(arquivo.read())
