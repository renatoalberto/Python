"""
Regressão Logística

- Usando Machine Learning para previsões categóricas

- Exemplos:
    - Se um email é spam ou não               * Binário
    - Se um tumor é maligno ou benigno        * Binário
    - Se uma planta é da espécie A, B ou C    * Múltipla Escolha

- Modelo de regressão logística é usado em classificações binárias, mas conseguimos utilizar
  com múltiplas escolhas

- Tendo duas espécies de planta, é uma classificação binária. Quando tempos 3 ou mais espécies
  comparamos especie a com bc, espécie b com ac e especie c com ab, técnica one vs all, um contra
  todas, feito isso conseguimos realizar a classificação binária, obter a melhor probabilidade.

Regressão Logística faz parte do pacote sklearn :
from sklearn.linear_model import LogisticRegression
"""