""""
Dicionários (dict) - Coleções do tipo {chave e valor}

- São representados por chave {}
- Chave e valor separados por ':' {chave: valor, chave: valor}
- Tanto a chave quanto o valor podem ser de qualquer tipo
- Não podemos ter chave repetidas
"""
print(type({}))

# Forma 1 -----------------------------------------------------------------------------------------
paises = {'br': 'Brasil', 'eua': 'Estados Unido', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 -----------------------------------------------------------------------------------------
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando valores -------------------------------------------------------------------------------
# Forma 1 ------------------------------------
print(f'eua representa {paises["eua"]}')
print(f'br  representa {paises["br"]}')

# OBS-  caso índice não seja localizado retornará um erro

# Forma 2 ------------------------------------
print(f'eua representa {paises.get("eua")}')
print(f'br  representa {paises.get("br")}')
print(f'ru  representa {paises.get("ru")}')

# OBS-  caso índice não seja localizado retornará tipo "None"
#       None - representa o tipo sem tipo ou vazio
#            - em uma condição será considerado Falso

russia = paises.get("ru", 'País não localizado')   # Caso não encontre, retornará padrão
print(f'Teste do valor padrão - {russia}')

# Verificar se uma chave está contido no dicionário -----------------------------------------------
print(f'br está contido em paises - {"br" in paises}')
print(f'ru está contido em paises - {"ru" in paises}')
print(f'Paraguai está contido em paises - {"Paraguai" in paises}')  # não busca por valor

# Podemos utilizar qualquer tipo de dado como chave do dicionário ---------------------------------
localidades = {
    (35.68875, 39.43378): 'Escritório em Tokyo',       # tuplas como chave de dicionário, imutáveis
    (40.63225, 11.57278): 'Escritório em Nova York',
    (23.21475, 65.44378): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário ------------------------------------------------------------
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita)

# Forma 1 ------------------------ Mais comum
receita['Abr'] = 250
print(receita)

# Forma 2 ------------------------
novo_dado = {'Mai': 310}
receita.update(novo_dado)     # mesmo que receita.update({'Mai': 310})
print(receita)

receita.update({'Mai': 600})  # Permite atualização de valor já existente
print(receita)

# Remover dados de um dicionário ------------------------------------------------------------------
# Forma 1 ------------------------ Mais comum
mes = receita.pop('Mai')            # obrigatório informar a chave
print(f'{receita} e excluiu e valor - {mes}')

# OBS: chave não localizada causa erro

# Forma 2 ------------------------
del receita['Fev']                 # Não retorna valor
print(receita)

# OBS: chave não localizada causa erro

# Muito utilizados em carrinho de compras (lista + dicionário) ------------------------------------
produto1 = {'nome': 'Playstation', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'preco': 150.00}

carrinho = list()
carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)  # Identifica todos os itens da lista

# Limpar o dicionário -----------------------------------------------------------------------------
carrinho.clear()
print(f'Carrinho de compras excluido - {carrinho}')

# Copiando um dicionário --------------------------------------------------------------------------
# Forma 1 ------------------------------------------
dicionario1 = dict(a=1, b=2, c=3)
print(f'dicionario1 - {dicionario1}')

dicionario2 = dicionario1.copy()         # Deep Copy - Cópia profunda
print(f'dicionario2 - {dicionario2}')

# Forma 2 ------------------------------------------
dicionario3 = dicionario2                # Shallow Copy - Cópia rasa
print(f'dicionario3 - {dicionario3}')

dicionario3.update({'d': 4})
print('Cópia rasa de dicionário 2 para 3. Impacto em ambos')
print(f'dicionario2 - {dicionario2}')
print(f'dicionario3 - {dicionario3}')

# Método não usual de criação de dicionários ------------------------------------------------------
novo = {}.fromkeys('a', 'b')
print(novo)
print(type(novo))

novo = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(novo)
print(type(novo))

# o método fromkeys recebe 2 parâmetros:
#    1ª - um iterável - cria um chava para cada iterável
#    2ª - um valor    - atribui o valor a todas as chaves do iterável

novo = {}.fromkeys('teste', 'valor')  # CUIDADO - string é um iterável, cada caracter se tornará uma chave
print(novo)
print(type(novo))

novo = {}.fromkeys(range(2, 11, 2), 'Número par')
print(novo)
print(type(novo))
