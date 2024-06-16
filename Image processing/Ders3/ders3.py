import cv2
import numpy as np



resim = cv2.imread("Ders3\kurt.jpg")
cv2.imshow("Kurt Resmi",resim)
print(resim[(230,80)]) #230 piksel sağa ve 80 piksel aşağıda bir nokta alır ve bu noktanın rengini görüntüler.

cv2.waitKey(0)
cv2.destroyAllWindows()