import cv2
import datetime

cap = cv2.VideoCapture(0) #0 yazarsan kameranı seçer
cv2.namedWindow('Kamera',1)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,1280)
cap.set(4,700)
print(cap.get(3))
print(cap.get(4))

while(True):
    ret , frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_PLAIN
        text = "  Width: "+ str(cap.get(3)) + "  Height: "+ str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet+text,(750,650),font,1 , (236,255,45), 2 , cv2.LINE_AA)

        cv2.imshow('Kamera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()