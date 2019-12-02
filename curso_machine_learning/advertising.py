import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np



publi = pd.read_csv('/home/galileu/Exercicios-python/curso_machine_learning/Advertising.csv', index_col=0)

x = publi[['TV','radio','newspaper']]
y = publi['sales']

sns.pairplot(publi, x_vars=['TV','radio','newspaper'], y_vars='sales', height=4,kind='reg')
#plt.show()

#treinamento

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

reglin = LinearRegression()
reglin.fit(x_train,y_train)

zlist = zip(['TV','radio','newspaper'], reglin.coef_)
zlist = set(zlist)
print(zlist)

y_prev = reglin.predict(x_test)
#print(y_prev)
#print(y_test)

# Avaliação da performance
#MAE Mean absolute error
print(metrics.mean_absolute_error(y_test,y_prev))

#MSE Mean squared error
print(metrics.mean_squared_error(y_test, y_prev))

#RMSE Root mean squared error
print(np.sqrt(metrics.mean_squared_error(y_test, y_prev)))

