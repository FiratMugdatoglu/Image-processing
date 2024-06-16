import cv2
import numpy as np

resim = cv2.imread("Ders10\indir.jpg")
#resim = cv2.imread("Ders10\indir.jpg",0)#Burada ikinci parametreye 0 verince resim grileşir.
griResim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)#Resmi grileştirdik.Resmi grileştirdik diye kanal sayısıda 1 e düşer




cv2.imshow("Resim",resim)
cv2.imshow("Gri Resim",griResim)


yukseklik,genislik,kanalSayisi=resim.shape
yukseklik,genislik=griResim.shape

print("Original Resim",yukseklik,genislik,kanalSayisi)
print("Gri Resim",yukseklik,genislik)


cv2.waitKey(0)
cv2.destroyAllWindows()