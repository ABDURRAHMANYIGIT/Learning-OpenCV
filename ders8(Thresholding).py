import cv2

img = cv2.imread('C:\Python\PycharmProjects\OpenCvDersleri\My Datas\photoshop-foreground-background-gradient.jpg')

_, th1 = cv2.threshold(img, 127 , 255 , cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img , 127 , 255 , cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127 , 255 , cv2.THRESH_TOZERO)
_, th4 = cv2.threshold(img, 127 , 255 , cv2.THRESH_TOZERO_INV)

cv2.imshow("th1" , th1)
cv2.imshow("th2" , th2)
cv2.imshow("th3" , th3)
cv2.imshow("th4" , th4)
cv2.imshow("image" , img)

cv2.waitKey(0)
cv2.destroyWindow()