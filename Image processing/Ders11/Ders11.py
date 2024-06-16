import cv2
import numpy as np


resim = cv2.imread("Ders11\\18537-1598536967.webp")
ikiKatBuyuk=cv2.pyrUp(resim)#Resmin yüksekliğini ve genişliğini iki kat arttırır.
ikiKatKucuk=cv2.pyrDown(resim)#Resmin yüksekliğini ve genişliğini iki kat düşürüyor.

cv2.imshow("Resim",resim)
cv2.imshow("Büyültülmüş Resim",ikiKatBuyuk)
cv2.imshow("Kucultulmus Resim",ikiKatKucuk)

print("Orijinal Resim",resim.shape)
print("Buyutulmus Resim" , ikiKatBuyuk.shape)
print("Kucultulmus Resim" , ikiKatKucuk.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()