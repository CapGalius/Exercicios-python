import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

testes = [['TV','radio','newspaper'],['radio','newspaper'],['TV','newspaper'],['TV','radio',]]
vencedor ={"teste":' ','performance': None}
primeira_passagem = True

publi = pd.read_csv('/home/galileu/Exercicios-python/curso_machine_learning/Advertising.csv', index_col=0)

for teste in testes:
    x = publi[teste]
    y = publi['sales']
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=5)
    reglin = LinearRegression()
    reglin.fit(x_train,y_train)
    y_prev = reglin.predict(x_test)
    rmse= np.sqrt(metrics.mean_squared_error(y_test, y_prev))
    print("teste: ")
    print(teste)
    print("Performance: ")
    print(rmse)
    print('-'*20)
    if (primeira_passagem):
        vencedor['teste'] = teste
        vencedor['performance'] = rmse
        primeira_passagem = False
    else:
        if(rmse < vencedor['performance']):
            vencedor['teste'] = teste
            vencedor['performance'] = rmse

print('-'*20)    
print("Vencedor: ")
print(teste)
print("Performance do Vencedor: ")
print(rmse)