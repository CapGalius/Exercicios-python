#Importação dos dados
from sklearn.datasets import load_iris
iris = load_iris()

#Observações
x = iris.data
print(x)

#Target 
y = iris.target
print(y)

#Import KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=11)

#Treinar maquina
knn.fit(x,y)
print(knn.fit)

#previsões
species = knn.predict([[5.9, 3, 5.1, 1.8]])[0]
print(iris.target_names[species])

#Separar dados em 2 grupos
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.40)


#Avaliação de performance do Modelo
knn.fit(x_train,y_train)
previsoes =knn.predict(x_test)
from sklearn import metrics
acertos = metrics.accuracy_score(y_test,previsoes)
print(acertos)

#Regressao logistica
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(multi_class='ovr')
logreg.fit(x_train, y_train)
previsoes_logreg = logreg.predict(x_test)
acertos_logreg = metrics.accuracy_score(y_test,previsoes_logreg)
print(acertos_logreg)
