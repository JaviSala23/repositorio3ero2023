
import cv2
import numpy as np

#CONSTANTES
ROJO=(0,0,255)
VERDE=(0,255,0)
AZUL=(255,0,0)
COLOR1=(255,255,0)

# Crea un objeto VideoCapture para capturar el video desde la cámara
cap = cv2.VideoCapture(0,)


# Comprueba si la cámara está abierta correctamente
if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()

# Captura el video de la cámara y muestra cada cuadro en una ventana
while True:
    ret, img = cap.read(cv2.IMREAD_GRAYSCALE)# Lee un cuadro desde la cámara

#dibujo  esta comentado
    ''' 
    print(img.shape)
    punto1Linea1 = (0,0)
    punto2Linea1 = (640,480)
    colorLinea1 = ROJO
    grosorLinea1 = 2

    #crea la linea co las caracteristicas anteriores y la concatena con la imagen
    cv2.line(img, punto1Linea1, punto2Linea1 , colorLinea1, grosorLinea1)
    '''    
#split de los canales de mi streaming
    #dividimos canales
    a,v,r=cv2.split(img)
    img_negro=np.zeros(img.shape[:2],dtype='uint8')
    filtroAzul=cv2.merge([a,img_negro,img_negro])
    filtroVerde=cv2.merge([img_negro,v,img_negro])
    filtroRojo=cv2.merge([img_negro,img_negro,r])
    filtroRojoAzul=cv2.merge([a,img_negro,r])
    filtroRojoVerde=cv2.merge([img_negro,v,r])
    filtroRojox2Azul=cv2.merge([a*3,img_negro,r*3])
    
    cv2.imshow('imagen Normal', img)
    cv2.imshow('fitro azul', filtroAzul)# Muestra el cuadro en una ventana llamada 'frame'
    cv2.imshow('fitro verde', filtroVerde)
    cv2.imshow('fitro rojo', filtroRojo) 
    cv2.imshow('fitro rojoAzul', filtroRojoAzul) 
    cv2.imshow('fitro rojoVerde', filtroRojoVerde)
    cv2.imshow('fitro rojox2Azul', filtroRojox2Azul)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Espera una tecla 'q' para salir del bucle
        break

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()