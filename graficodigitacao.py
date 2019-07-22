import time
import matplotlib

print("-"*40)
print("-"*10, "Teste tempo digitação.", "-"*5)
print("-"*40)

def count_tempo():
    inicio = time.clock()
    input("Escreva seu nome:") 
    fim = time.clock()
    tempo = inicio - fim
    grafico.append(tempo)    

i = 0
grafico=[]
while i < 6:
    count_tempo()
    i = i+1

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = grafico
plt.plot(x,y)
legenda =  ["1ª Vez","2ª Vez", "3ª Vez","4ª vez","5ª vez","6ª Vez"]
plt.xticks(x,legenda)
plt.show()