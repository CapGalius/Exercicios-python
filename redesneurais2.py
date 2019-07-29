import numpy as np

entradas = [1, 7, 5]
pesos = [0.8, 0.7, 0]

def soma(e,p):
   return e,dot(p)
#dot product/produto escalar
    
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >=1):
        return 1
    return 0

r = stepFunction