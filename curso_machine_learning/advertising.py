import pandas as pd

publi = pd.read_csv('/home/galileu/Exercicios-python/curso_machine_learning/Advertising.csv', index_col=0)

x = publi[['TV','radio','newspaper']]
y = publi['sales']

