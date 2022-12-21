import cv2

#RESİM OKUMA
img = cv2.imread("C:\\Users\\imran\\Desktop\\Python\\PycharmProjects\\OpenCvDersleri\\My Datas\\colorTable.jpg")
cv2.namedWindow("Pencerem") #Pencerem isimli bir pencere açtık
cv2.imshow("Pencerem",img) #-->img olarak atadığımız değişkeni imshow komutu ile pencerem isimli penceremizde gösterdik.
cv2.waitKey(0)             #   eğer namedWindow olarak tanımlanmış bir pencere yok ise de kendi kendine gösterebiliyor.
cv2.destroyAllWindows()    #   kendi kendine pencere açabiliyor, eğer varsa da var olanı kullanıyor.

#VİDEO OKUMA
cap = cv2.VideoCapture("C:\\Users\\imran\\Desktop\\Python\\PycharmProjects\\OpenCvDersleri\\My Datas\\hideo.mp4")

if(cap.isOpened() == False):
    print("Açılamadı")

else:
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Video Oynatıcı',frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

