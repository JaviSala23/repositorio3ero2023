#importamos la libreria de OpenCV
import cv2 
import numpy as np



imgNormal = cv2.imread('imagen.png')
b,g,r=cv2.split(imgNormal)

cv2.imshow('azul',b)
cv2.imshow('verde',g)
cv2.imshow('rojo',r)

cv2.waitKey(0)