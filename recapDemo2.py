import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(grayFrame,100,200)

    cv2.imshow("Frame", frame)
    cv2.imshow("Canny",canny)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

