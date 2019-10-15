import cv2

classificador = cv2.CascadeClassifier('/home/galileu/Exercicios-python/Deteccao/cascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('/home/galileu/Exercicios-python/Deteccao/pessoas/pessoas4.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=12, minSize=(35, 35))
print(len(facesDetectadas))
print(facesDetectadas)
 
for (x, y, l, a) in facesDetectadas:
    print(x, y, l, a)
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 2)

cv2.imshow("Faces Encontradas", imagem)
cv2.waitKey()