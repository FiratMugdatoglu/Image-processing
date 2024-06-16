import cv2
import numpy as np

resim = cv2.imread("Ders1\Logo.png" , 0) #eğer 2. parametreye 0 verirsek renkleri çalıştırmaz.
cv2.imshow("Google Logo", resim)
cv2.imwrite("Ders1\Yeni Google Logo.png" , resim) #Eğer yeni oluşturduğumuz fotoğrafı kaydetmek istersek bu parametreyi kullanırız.
cv2.waitKey(0)
cv2.destroyAllWindows()

