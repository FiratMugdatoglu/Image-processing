import cv2
import numpy as np


resim1 = cv2.imread("Ders9\\ronaldo.webp")
resim2 = cv2.imread("Ders9\messi.webp")

print(resim1[100,200])
print(resim2[300,130])

cv2.imshow("Ronaldo", resim1)
cv2.imshow("Messi",resim2)

print(resim1[100,200]+resim2[300,130])#Ağırlıklı toplama yapıyoruz.

toplam = cv2.add(resim1,resim2)#İki resmi üst üste koyma işlemi.
agirlikliToplama = cv2.addWeighted(resim1,0.7,resim2,0.3,0)#Resimlerin ağırlıklı bir şekilde göstermek için kullanılır.

cv2.imshow("Ronaldo+Messi" , toplam)
cv2.imshow("Ronaldo+Messi" , agirlikliToplama)

cv2.waitKey(0)
cv2.destroyAllWindows()