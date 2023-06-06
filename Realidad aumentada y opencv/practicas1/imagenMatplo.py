#importamos la libreria de OpenCV
import cv2 
import numpy as np
import matplotlib.pyplot as plt


imgNormal = cv2.imread('imagen.png')
img = cv2.cvtColor(imgNormal, cv2.COLOR_BGR2RGB)
cv2.imshow('Mi imagen en gris', img)


plt.imshow(img)
plt.show()

color_array=np.array(img)
print(color_array)