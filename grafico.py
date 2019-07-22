import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [1500,800,750,200,756,3000]
plt.plot(x,y)
legenda =  ["Jan","Fev", "Mar","Abr","Mai","Jun"]
plt.xticks(x,legenda)
plt.show()