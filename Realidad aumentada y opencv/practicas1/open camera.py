import cv2
import urllib.request
import numpy as np

stream = urllib.request.urlopen('http://10.16.109.186:8080/video')
bytes = b''  # Initialize bytes as a bytes object
while True:
    bytes += stream.read(16384)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        
        bytes = bytes[b+2:]
        
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        
#------------------------------------------------------------------------------
#dibujo 
        print(i.shape)
        punto1Linea1 = (0,0)
        punto2Linea1 = (800,700)
        colorLinea1 = (0,0,255)
        grosorLinea1 = 2

        #crea la linea co las caracteristicas anteriores y la concatena con la imagen
        cv2.line(i, punto1Linea1, punto2Linea1 , colorLinea1, grosorLinea1)      
        
        
        
        
#-------------------------------------------------------------------------------        
        cv2.imshow('i', i)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Espera una tecla 'q' para salir del bucle
            break
