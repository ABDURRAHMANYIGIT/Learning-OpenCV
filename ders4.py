import cv2
import numpy as np

img = cv2.imread("C:\Python\PycharmProjects\OpenCvDersleri\My Datas\L1.jpg")
img2 = cv2.imread("C:\Python\PycharmProjects\OpenCvDersleri\My Datas\colorTable.jpg")


def event_call(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_PLAIN
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x, y), font, 2, (255, 0, 255), 2)
        cv2.imshow('Resim Uzerine Sekil Cizme', img)


print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

img2 = cv2.resize(img2, (512, 512))
img = cv2.resize(img, (512, 512))
dst = cv2.add(img, img2)

cv2.imshow('Resim Uzerine Sekil Cizme', dst)
cv2.setMouseCallback('Resim Uzerine Sekil Cizme', event_call)
cv2.waitKey(0)
cv2.destroyAllWindows()
