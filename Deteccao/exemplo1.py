import cv2

classificador = cv2.CascadeClassifier('/home/galileu/Exercicios-python/Deteccao/cascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('/home/galileu/Exercicios-python/Deteccao/pessoas/beatles.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemCinza)
print(len(facesDetectadas))