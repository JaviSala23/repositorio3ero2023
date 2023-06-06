#importamos la libreria de OpenCV
import cv2 
import numpy as np
img = cv2.imread('foto.jpeg')
imgRGB=cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
imgHSV=cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

#dividimos canales
a,v,r=cv2.split(img)




#con los division de canales vamos a generar una imagen de dimencion zero 
# de numpy y de esta manaera poder combinarla con cada capa de intensidad esto nos dara
#como resultado la imagen con el color combinado

img_negro=np.zeros(img.shape[:2],dtype='uint8')
print(img_negro)

comb_azul=cv2.merge([a,img_negro,img_negro])
comb_verde=cv2.merge([img_negro,v,img_negro])
comb_rojo=cv2.merge([img_negro,img_negro,r])


comb_azuVer=cv2.merge([a,v,img_negro])
comb_azuRojo=cv2.merge([a,img_negro,r])
comb_verdeRojo=cv2.merge([img_negro,v,r])


#img saturada en rojo

saturacion = np.clip(1.8 * r, 0, 255).astype(np.uint8)
imagen_Sat_rojo=cv2.merge([a,v,saturacion])

cv2.imshow('BGR Normal para CV2',img)
cv2.imshow('RGB Normal para otras apps',imgRGB)
cv2.imshow('HSV',imgHSV)

#mostramos por separado la intensida de los colores los pixeles solo tienen un tipo que es su intnsidad
cv2.imshow('Solo azul',a)
cv2.imshow('Solo verde',v)
cv2.imshow('Solo rojo',r)



#mostramos por separada las imagenes filtradas en azul verde y rojo
cv2.imshow('Filtro azul',comb_azul)
cv2.imshow('Filtro verde',comb_verde)
cv2.imshow('Filtro rojo',comb_rojo)



cv2.imshow('comb Azul Verde',comb_azuVer)
cv2.imshow('comb Azul Rojo',comb_azuRojo)
cv2.imshow('comb Verde Rojo',comb_verdeRojo)

#guardamos las imagenes
cv2.imwrite('verdeRojo.jpg', comb_verdeRojo)
cv2.imwrite('azulrojo.jpg', comb_azuRojo)

#muestra imagen saturada en rojo
cv2.imshow('sat en rijo Rojo',imagen_Sat_rojo)












# esperar hasta que se presiona una tecla
cv2.waitKey(0)