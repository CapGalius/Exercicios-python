from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)

valores_performance = {}
k = 1

while k <= 25:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    previsoes = knn.predict(x_test)
    acertos = metrics.accuracy_score(y_test, previsoes)
    valores_performance[k] = round(acertos,4)
    k += 1

print(valores_performance)
plt.plot(list(valores_performance.keys()),list(valores_performance.values()))
plt.xlabel('Valores de K')
plt.ylabel('Performance')
plt.show()