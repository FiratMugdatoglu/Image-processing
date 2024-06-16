import cv2
import numpy as np

resim = cv2.imread("Ders6\\resim.png")
kesit = resim[350:550,400:800] #Resim üzerinden belirli bir kesit aldık
resim[100:300,100:500] = kesit #kestiğimiz yeri fotoğrafın belirli kordinatına koyduk
resim[:,:,0]=255#Resme mavi efekt verdik

cv2.imshow("Kesilen Resim" , kesit)
cv2.imshow("Resim",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()