import numpy as np
import cv2

img = cv2.imread("C:\\Users\\imran\\Desktop\\Python\\PycharmProjects\\OpenCvDersleri\\My Datas\\hababam5.jpg")

img = cv2.line (img , (0,0),(255,255),(0,0,255),5)
img = cv2.arrowedLine (img , (0,255),(255,255),(0,0,255),5)

font = cv2.FONT_HERSHEY_PLAIN

img = cv2.rectangle(img,(384,0),(510,128),(212, 100, 72),-1) #-1 verir isen verdiğin renk ile içini doldurur
img = cv2.circle(img,(256,63),63,(212, 250, 72),4)
img = cv2.putText(img,"SELAMUN ALEYKUM AQ",(50,250),font,4,(255,255,255))

cv2.imshow('Sekil Cizimi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

