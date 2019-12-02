from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import numpy as np
import matplotlib.image as mpimg

digits = datasets.load_digits()
print(digits.data.shape)
print(digits.target.shape)
'''
plt.figure(figsize=(2,2))
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)
plt.show()
'''
x = digits.data
y = digits.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20, random_state=5)

classifier = svm.SVC()
classifier.fit(x, y)


img = mpimg.imread('/home/galileu/Exercicios-python/curso_machine_learning/Digits/number.png')

def rgb2gray(rgb):
    img_array = np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    img_array = (16 - img_array*16).astype(int)
    img_array = img_array.flatten()
    return img_array

previsao = classifier.predict([rgb2gray(img)])
print(previsao)