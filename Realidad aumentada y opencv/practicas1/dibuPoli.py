import cv2
import numpy as np
import time

#CONSTANTES
ROJO=(0,0,255)
VERDE=(0,255,0)
AZUL=(255,0,0)
COLOR1=(255,255,0)

img = np.zeros((700,800,3), np.uint8)
img[:]=(190,2,159)




     
a=0       
#Muestra la imagen creada
while(True):
    
    #Características de línea1
    punto1Linea1 = (0,100)
    punto2Linea1 = (0+a,100)
    colorLinea1 = ROJO
    grosorLinea1 = 2

    #crea la linea co las caracteristicas anteriores y la concatena con la imagen
    cv2.line(img, punto1Linea1, punto2Linea1 , colorLinea1, grosorLinea1)
    
    cv2.imshow('Fondo de color', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    a=a+10
    time.sleep(0.5)