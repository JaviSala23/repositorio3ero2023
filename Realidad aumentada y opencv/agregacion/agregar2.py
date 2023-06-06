import cv2
img1 = cv2.imread('agregacion/cadena.jpg')
img2 = cv2.imread('agregacion/sacapuntas.jpg')
resAW = cv2.addWeighted(img1,0.5,img2,0.9,1)
cv2.imshow('resAW',resAW)
cv2.waitKey(0)
cv2.destroyAllWindows()