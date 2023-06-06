import cv2
img1 = cv2.imread('agregacion/cadena.jpg')
img2 = cv2.imread('agregacion/sacapuntas.jpg')
resA = cv2.add(img1,img2)
cv2.imshow('resA',resA)
cv2.waitKey(0)
cv2.destroyAllWindows()