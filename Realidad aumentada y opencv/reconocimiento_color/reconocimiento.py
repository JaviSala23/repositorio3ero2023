import cv2
import numpy as np
#cap = cv2.VideoCapture('http://10.16.109.186:8080/video')
cap1 = cv2.VideoCapture(0,)

azulBajo1 = np.array([90, 100, 20], np.uint8)
azulAlto1 = np.array([125, 255, 255], np.uint8)
lineas=[]
while(True):
    ret, frame = cap1.read()
    frame=cv2.resize(frame,(400,400))
    frame=cv2.flip(frame,2)
    frameHSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mascara=cv2.inRange(frameHSV, azulBajo1, azulAlto1)
    contornos,_ = cv2.findContours(mascara, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contornos, -1, (255,0,0), 1)   
    
    for c in contornos:
      
      area = cv2.contourArea(c)
      if area > 3000:
        M = cv2.moments(c)
        if (M["m00"]==0): M["m00"]=1
        x = int(M["m10"]/M["m00"])
        y = int(M['m01']/M['m00'])
        cv2.circle(frame, (x,y), 7, (0,255,0), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 1.5,(0,0,0),2,cv2.LINE_AA)
        nuevoContorno = cv2.convexHull(c)
        cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)
        lineas.append((x,y))
    print(lineas)
  
    mascaraVision = cv2.bitwise_and(frame, frame, mask= mascara) 
    cv2.imshow('Ventana Normal',frame)
    #cv2.imshow('Imagen HSV',frameHSV)
    #cv2.imshow('Mascara',mascara)
    #cv2.imshow('Mascara en el frame',mascaraVision)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap1.release()
cv2.destroyAllWindows()