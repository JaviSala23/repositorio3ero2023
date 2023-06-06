import cv2
import numpy as np

cap = cv2.VideoCapture('http://10.16.109.186:8080/video')

w  = cap.get(3)   # float `width`
h = cap.get(4)
cero= np.zeros((int(h),int(w)),np.uint8)
while(True):
    ret, frame = cap.read()
    a,v,r=cv2.split(frame)
    img=cv2.merge([cero,v,r])
     # Dibujar un cuadrado rojo en el centro de la imagen
    x1 = int(w / 2 - 50)
    y1 = int(h / 2 - 50)
    x2 = int(w / 2 + 50)
    y2 = int(h / 2 + 50)
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), thickness=2)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
