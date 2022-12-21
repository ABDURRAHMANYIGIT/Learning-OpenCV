import cv2
import numpy as np

img1 = cv2.imread("C:\Python\PycharmProjects\OpenCvDersleri\My Datas\deneme.jpg")
img2 = np.zeros((250,500,3), np.uint8)
img2 = cv2.rectangle(img2,(200,0), (300,100) , (255,255,255), -1)

img1 = cv2.resize(img1 , (512,512))
img2 = cv2.resize(img2 , (512,512))


#bitNot1 = cv2.bitwise_not(img1) \
#bitnot2 = cv2.bitwise_not(img2) | --> NOT
#cv2.imshow('bitnot1',bitNot1)   |
#cv2.imshow('bitnot2',bitnot2)   /

#bitAnd = cv2.bitwise_and(img1,img2) \
#cv2.imshow('bitAnd', bitAnd)        /--> AND

#bitOr = cv2.bitwise_or(img1,img2) \
#cv2.imshow('bitOr' , bitOr)       /--> OR

#bitXor = cv2.bitwise_xor(img1, img2) \
#cv2.imshow('bitXor' , bitXor)        / --> XOR

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)


cv2.waitKey(1) & 0xFF == ord('q')

cv2.waitKey(0)
