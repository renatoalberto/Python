"""
KNN (K Nearest Neighbors) ou K Vizinhos Mais Próximos

Quando:
  - K = 1, o método irá pegar um vizinho mais próximo, na qual será do mesma tipo;
  - K = 3, o método irá pegar três vizinhos mais próximos, na qual será do tipo que tiver maior quantidade de elementos;

KNN faz parte do pacote sklearn :
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
"""