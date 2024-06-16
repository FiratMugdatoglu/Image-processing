import cv2
import numpy as np


resim = cv2.imread("Ders8\insanlar.jpg")
cv2.rectangle(resim,(20,160),(130,40),[0,0,255],3)

cv2.imshow("Resim" , resim)


cv2.waitKey(0)
cv2.destroyAllWindows()