"""
SVM: Support Vector Machine

É um algorítimo de machine learning supervisionado para criar limites entre grupos de dados.

Detalhando um pouco mais, em um gráfico de eixos x e y, sendo os elementos jogados nesse gráfico, o SVM
encontra a posição da linha que dê maior distância entre os pontos mais próximos de cada lado (Hyperplane, ou
hiperplano) e a soma das distâncias entre a linha e o ponto mais próximo de cada elemento é chamado de margem,
o objetivo do SVM é traçar uma linha com a maior margem possível.

Após traçado o Hyperplane, a inclusão de um novo ponto no gráfico será classificado por sua posição dentro da
fronteira traçada.
"""