import cv2
import os
import numpy as np 

eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagemComId():
    caminhos =[os.path.join('fotos',f) for f in os.listdir('/home/galileu/Exercicios-python/Deteccao/fotos')]
    print(caminhos)
    faces= []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.imread(caminhoImagem)
        cv2.imshow("Face", imagemFace)
        cv2.waitKey(10)
getImagemComId()