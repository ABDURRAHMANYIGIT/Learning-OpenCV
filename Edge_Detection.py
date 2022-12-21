import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Python\PycharmProjects\OpenCvDersleri\My Datas\3.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
grayİmg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(img,-1,2,2)
lapla = cv2.Laplacian(img,-1,3)
scharr = cv2.Scharr(img,-1,0,1)
canny = cv2.Canny(grayİmg,100,200)


titles = ['image','sobel','lapla','scharr','canny']
images = [img,sobel,lapla,scharr,canny]

for i in range (5):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()