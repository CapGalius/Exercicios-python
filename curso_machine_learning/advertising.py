import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

publi = pd.read_csv('/home/galileu/Exercicios-python/curso_machine_learning/Advertising.csv', index_col=0)

x = publi[['TV','radio','newspaper']]
y = publi['sales']

sns.pairplot(publi, x_vars=['TV','radio','newspaper'], y_vars='sales', height=4,kind='reg')
#plt.show()

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

reglin = LinearRegression()
reglin.fit(x_train,y_train)

zlist = zip(['TV','radio','newspaper'], reglin.coef_)
zlist = set(zlist)
print(zlist)

y_prev = reglin.predict(x_test)
print(y_prev)