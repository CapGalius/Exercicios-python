import cv2

classificadorGato = cv2.CascadeClassifier('/home/galileu/Exercicios-python/Deteccao/cascades/haarcascade_frontalcatface.xml')

imagem = cv2.imread('/home/galileu/Exercicios-python/Deteccao/pessoas/gato3.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificadorGato.detectMultiScale(imagemCinza, scaleFactor=1.02)
print(len(facesDetectadas))
print(facesDetectadas)
 
for (x, y, l, a) in facesDetectadas:
    print(x, y, l, a)
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 2)

cv2.imshow("Miaus Encontrados", imagem)
cv2.waitKey()