
import numpy as np
from sklearn import datasets

def sigmoid (soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1- sig)

base = datasets.load_breast_cancer()

entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

saidas = np.array([[0],[1],[1],[0]])


pesos0 = 2*np.random.random((2,3)) -1
pesos1 = 2*np.random.random((3,1)) -1


epocas = 100000
taxadeAperndizagem = 0.3
momento = 1

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Erro: " + str(mediaAbsoluta))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    camadaOcultaTransposta = camadaOculta.T
    pesoNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesoNovo1 * taxadeAperndizagem)
    
    camadaEntradaTransposta = camadaEntrada.T
    pesoNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesoNovo0 * taxadeAperndizagem)
    
    