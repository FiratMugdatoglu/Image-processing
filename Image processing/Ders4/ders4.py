import cv2
import numpy as np


resim = cv2.imread("Ders4\joker.jpg")

resim[50,30]=[255,255,255]

for i in range(100):
    resim[70,i] = [255,255,255]

cv2.imshow("Joker" , resim)

cv2.waitKey(0)
cv2.destroyAllWindows()