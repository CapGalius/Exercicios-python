import cv2

# this is just to unconfuse pycharm
try:
     import cv2.__init__ as cv2
except ImportError:
     pass
import os
import numpy as np 

eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagemComId():
    caminhos =[os.path.join('fotos',f) for f in os.listdir('Deteccao/fotos')]
    print(caminhos)

getImagemComId()