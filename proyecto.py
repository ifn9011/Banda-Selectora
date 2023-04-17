import cv2
import numpy as np
import time
import serial

ardu=serial.Serial("COM3",9600,timeout=3)

def nada(x):
    pass

#cv2.namedWindow('mascara',cv2.WINDOW_NORMAL)
#cv2.namedWindow('mascara2',cv2.WINDOW_NORMAL)
cv2.namedWindow('normal',cv2.WINDOW_NORMAL)
#cv2.namedWindow('encontrado',cv2.WINDOW_NORMAL)
cv2.namedWindow('Slides',cv2.WINDOW_NORMAL)
#cv2.resizeWindow('mascara',400,300)
cv2.resizeWindow('normal',400,300)
#cv2.resizeWindow('encontrado',400,300)
cv2.resizeWindow('Slides',400,300)
cv2.createTrackbar("Hi","Slides",50,255,nada)
cv2.createTrackbar("Si","Slides",80,255,nada)
cv2.createTrackbar("Vi","Slides",50,255,nada)
cv2.createTrackbar("Hf","Slides",130,255,nada)
cv2.createTrackbar("Sf","Slides",255,255,nada)
cv2.createTrackbar("Vf","Slides",255,255,nada)
cv2.createTrackbar("Hiv","Slides",0,255,nada)
cv2.createTrackbar("Siv","Slides",91,255,nada)
cv2.createTrackbar("Viv","Slides",156,255,nada)
cv2.createTrackbar("Hfv","Slides",45,255,nada)
cv2.createTrackbar("Sfv","Slides",196,255,nada)
cv2.createTrackbar("Vfv","Slides",255,255,nada)

h1=0
s1=0
v1=0
h2=0
s2=0
v2=0
h1v=0
s1v=0
v1v=0
h2v=0
s2v=0
v2v=0
objetos=0
stop=1
objetosv=0
stopv=1
flag=1
flag2=1

cap = cv2.VideoCapture(0)
while(1):
    h1=cv2.getTrackbarPos("Hi","Slides")
    s1=cv2.getTrackbarPos("Si","Slides")
    v1=cv2.getTrackbarPos("Vi","Slides")
    h2=cv2.getTrackbarPos("Hf","Slides")
    s2=cv2.getTrackbarPos("Sf","Slides")
    v2=cv2.getTrackbarPos("Vf","Slides")
    h1v=cv2.getTrackbarPos("Hiv","Slides")
    s1v=cv2.getTrackbarPos("Siv","Slides")
    v1v=cv2.getTrackbarPos("Viv","Slides")
    h2v=cv2.getTrackbarPos("Hfv","Slides")
    s2v=cv2.getTrackbarPos("Sfv","Slides")
    v2v=cv2.getTrackbarPos("Vfv","Slides")

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    inicio_azul = np.array([h1,s1,v1])
    fin_azul = np.array([h2,s2,v2])
    inicio_verde = np.array([h1v,s1v,v1v])
    fin_verde = np.array([h2v,s2v,v2v])

    mask = cv2.inRange(hsv, inicio_azul, fin_azul)
    mask2 = cv2.inRange(hsv, inicio_verde, fin_verde)
    azule=cv2.countNonZero(mask)
    verdele=cv2.countNonZero(mask2)
    #print(azule)
    #print(verdele)
    if (azule<30000):
        if (stop==objetos):
            objetos=objetos+1
            stop=objetos
    if (stop==objetos):
        objetos=objetos-1
    if (azule>30000):
        objetos=objetos+1
        stop=objetos
        if flag==1:
            ardu.write(b'a')
            flag=flag+1
    if (azule<30000):
        if flag>1:
            ardu.write(b'n')
            flag=1
    #print(flag)
    if (verdele<10000):
        if (stopv==objetosv):
            objetosv=objetosv+1
            stopv=objetosv
    if (stopv==objetosv):
        objetosv=objetosv-1
    if (verdele>10000):
        objetosv=objetosv+1
        stopv=objetosv
        if flag2==1:
            ardu.write(b'v')
            flag2=flag2+1
    if (verdele<10000):
        if flag2>1:
            ardu.write(b'i')
            flag2=1
    print(azule)
    image = cv2.putText(mask,"Azules: "+str(objetos),(150, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
    image = cv2.putText(mask,"Amarillos: "+str(objetosv),(150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
    image = cv2.putText(frame,"Azules: "+str(objetos),(150, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
    image = cv2.putText(frame,"Amarillos: "+str(objetosv),(150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)          
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow("normal",frame)
    #cv2.imshow("mascara",mask)
    #cv2.imshow("mascara2",mask2)
    #cv2.imshow('encontrado',res)

    if (cv2.waitKey(1) & 0xFF == ord('q')):#si la tecla presionada es q salir
        break
   
cv2.destroyAllWindows()
   
cv2.destroyAllWindows()
