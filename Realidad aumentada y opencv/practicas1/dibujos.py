import cv2
import numpy as np

#CONSTANTES
ROJO=(0,0,255)
VERDE=(0,255,0)
AZUL=(255,0,0)
COLOR1=(255,255,0)



#crea un fondo Negro array de 700 x 800 de 3 canales todos en 0
img = np.zeros((700,800,3), np.uint8)

#remplaza los canales por el color BGR 
img[:]=COLOR1


#Características de línea1

punto1Linea1 = (0,0)
punto2Linea1 = (800,700)
colorLinea1 = ROJO
grosorLinea1 = 2

#crea la linea co las caracteristicas anteriores y la concatena con la imagen
cv2.line(img, punto1Linea1, punto2Linea1 , colorLinea1, grosorLinea1 )






#Muestra la imagen creada
cv2.imshow('Fondo de color', img)
cv2.imwrite('imagenverde.jpg',img)



cv2.waitKey(0)




