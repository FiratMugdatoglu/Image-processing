import cv2
import numpy as np


resim = cv2.imread("Ders7\\resim.jpg")

aynalananResim = cv2.copyMakeBorder(resim,150,150,150,150,cv2.BORDER_REFLECT)
uzatilanResim = cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarResim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
sarilanResim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT,value=(75,150,255))

cv2.imshow("Araba",aynalananResim)
cv2.imshow("Araba",uzatilanResim)
cv2.imshow("Araba",tekrarResim)
cv2.imshow("Araba",sarilanResim)


cv2.waitKey(0)
cv2.destroyAllWindows()