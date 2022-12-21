import cv2
import numpy as np

#kameradan görüntü alınıp, görüntü siyah beyaza çevilecek, ondan sonra adaptive thresholding kullanılarak daha net bir görüntü sağlanacak

cap = cv2.VideoCapture(0)
cv2.namedWindow('Kamera',1)

cap.set(3,1920)
cap.set(4,1080)

while(True):
    ret , frame = cap.read()
    grayFrame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    th1 = cv2.adaptiveThreshold(grayFrame , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 11 , 2)

    cv2.imshow('Kamera' , grayFrame)
    cv2.imshow('Threshold' , th1)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()