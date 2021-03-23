"""
Pybrain - http://pybrain.org/docs/

Rede Feed Forward - Onde cada camada se conecta a próxima camada, partindo
                    da camada de entrada rumo a de saída, exemplo seria a
                    MultiLayer Perceptron (MLP).

Instalação do pybrain:
 1 - Download do github https://github.com/pybrain/pybrain
 2 - descompactar pasta baixada
 3 - acessar pelo CMD a pasta baixada e descompactada
 4 - informar o comando -> 'python setup.py install'
"""
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
import pandas as pd
import numpy as np

# passa as dimensões dos vetores de entrada e do objetivo
dataset = SupervisedDataSet(2, 1)

# Tabela verdade XOR ---------------------------------------------------------------------------------------------------
dataset.addSample([0, 0], [0])
dataset.addSample([0, 1], [1])
dataset.addSample([1, 0], [1])
dataset.addSample([1, 1], [0])

# Primeiro parâmetro - Número de dimensões da entrada - 2
# Segundo  parâmetro - Quantidade de neurônios da camada intermediária (escondida)
# Terceiro parâmetro - Número de dimensões da saída - 1
# Quarto   parâmetro - bias para permitir uma melhor adaptação por parte da rede ao conhecimento a ela fornecido
network = buildNetwork(dataset.indim, 4, dataset.outdim, bias=True)

# Treinando a rede
# learningrate - taxa de aprendizado
# momentum - aumentar a velocidade de treinamento da rede neural e diminuir a instabilidade
trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.99)

# O treinamento é feito de forma manual
for epoch in range(1000):
   trainer.train()

# Outras formas de treino
# trainer.trainEpochs(1000)
# trainer.trainUntilConvergence()

test_data = SupervisedDataSet(2, 1)
test_data.addSample([1, 1], [0])
test_data.addSample([0, 1], [1])
test_data.addSample([1, 0], [1])
test_data.addSample([0, 0], [0])

# Realizando a previsão
# verbose para imprimir o processo de validação
trainer.testOnData(test_data, verbose=True)

# Redes Neurais com Paybrain e Dataset Iris.data  ----------------------------------------------------------------------
dados = pd.read_csv('iris.data', delimiter=',', header=None)

# Converter tipo de íris de texto para números
dicionarioIris = {
    'Iris-setosa': 0,
    'Iris-versicolor': 1,
    'Iris-virginica': 2
}

dados.columns = pd.Series(['compSépala', 'largSépala', 'compPétala', 'largPétala', 'tipoIris'])

dados.tipoIris = dados.tipoIris.apply(lambda tipoIris: dicionarioIris[tipoIris])

# Dividindo em dados de 70% para treino(105/3 = 35 registros) e 30% para teste(45/3 = 15 registros)
dados_setosa     = pd.DataFrame(dados.query('tipoIris == 0'), columns=['compSépala', 'largSépala', 'compPétala', 'largPétala'])
dados_versicolor = pd.DataFrame(dados.query('tipoIris == 1'), columns=['compSépala', 'largSépala', 'compPétala', 'largPétala'])
dados_virginica  = pd.DataFrame(dados.query('tipoIris == 2'), columns=['compSépala', 'largSépala', 'compPétala', 'largPétala'])

entradas_treino = np.concatenate((
   dados_setosa.head(35),
   dados_versicolor.head(35),
   dados_virginica.head(35)
))

entradas_teste = np.concatenate((
   dados_setosa.tail(15),
   dados_versicolor.tail(15),
   dados_virginica.tail(15)
))

dados_setosa     = pd.DataFrame(dados.query('tipoIris == 0'), columns=['tipoIris'])
dados_versicolor = pd.DataFrame(dados.query('tipoIris == 1'), columns=['tipoIris'])
dados_virginica  = pd.DataFrame(dados.query('tipoIris == 2'), columns=['tipoIris'])

saidas_treino = np.concatenate((
   dados_setosa.head(35),
   dados_versicolor.head(35),
   dados_virginica.head(35)
))

saidas_teste = np.concatenate((
   dados_setosa.tail(15),
   dados_versicolor.tail(15),
   dados_virginica.tail(15)
))

# passa as dimensões dos vetores de entrada e do objetivo
dataset = SupervisedDataSet(4, 1)

# adicionar entradas para o treinamento
for i in range(len(entradas_treino)):
   dataset.addSample(entradas_treino[i], saidas_treino[i])

# Primeiro parâmetro - Número de dimensões da entrada - 2
# Segundo  parâmetro - Quantidade de neurônios da camada intermediária (escondida)
# Terceiro parâmetro - Número de dimensões da saída - 1
# Quarto   parâmetro - bias para permitir uma melhor adaptação por parte da rede ao conhecimento a ela fornecido
network = buildNetwork(dataset.indim, 2, dataset.outdim, bias=True)

# Treinando a rede
# learningrate - taxa de aprendizado
# momentum - aumentar a velocidade de treinamento da rede neural e diminuir a instabilidade
trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.3)

# O treinamento é feito de forma manual
for epoch in range(1000):
   trainer.train()

# Testando a rede
test_data = SupervisedDataSet(4, 1)

for i in range(len(entradas_teste)):
   test_data.addSample(entradas_teste[i], saidas_teste[i])

# Realizando a previsão
# verbose para imprimir o processo de validação
previsao = trainer.testOnData(test_data, verbose=True)
print(previsao)

# Redes Neurais com Paybrain e Dataset Iris.data + ClassificationDataSet -----------------------------------------------
from pybrain.datasets.classification import ClassificationDataSet

# 1ª Parâmetro - Quantidade de entradas
# 2ª Parâmetro - Quantidade de saídas
# 3ª Parâmetro - Número de classes (setosa ou versicolor ou virginica)
dataset = ClassificationDataSet(4, 1, nb_classes=3)

# adicionar entradas para o treinamento
for i in range(len(entradas_treino)):
   dataset.addSample(entradas_treino[i], saidas_treino[i])

# print(dataset['input'])       # Para saber as entradas
# print(dataset['target'])      # Para saber as saidas
# print(len(dataset['target'])) # Para saber quantidade de amostras

# Primeiro parâmetro - Número de dimensões da entrada - 4
# Segundo  parâmetro - Quantidade de neurônios da camada intermediária (escondida)
# Terceiro parâmetro - Número de dimensões da saída - 1
# Quarto   parâmetro - bias para permitir uma melhor adaptação por parte da rede ao conhecimento a ela fornecido
network = buildNetwork(dataset.indim, 3, dataset.outdim, bias=True)

# Treinando a rede
# learningrate - taxa de aprendizado
# momentum - aumentar a velocidade de treinamento da rede neural e diminuir a instabilidade
trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.1, verbose=True)

# Testando a rede
test_data = SupervisedDataSet(4, 1)

for i in range(len(entradas_teste)):
   test_data.addSample(entradas_teste[i], saidas_teste[i])


train_erros, val_erros = trainer.trainUntilConvergence(dataset=test_data, maxEpochs=100)
