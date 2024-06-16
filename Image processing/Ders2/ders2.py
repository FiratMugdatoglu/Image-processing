import cv2
import numpy as np

resim = cv2.imread("Ders2\Tiger.jpg") 
cv2.imshow("Kaplan", resim)
print(resim) #fotoğrafın kaç piksel olduğunu bu kodla öğreniriz
print(resim.size) #fotoğrafın boyutunu bu kodla görürüz
print(resim.dtype) #fotoğrafın datasını öğreniriz.
print(resim.shape) #Fotoğrafın genişliğini,yüksekliğini ve kaç kanal kullandığını gösterir.
cv2.waitKey(0)
cv2.destroyAllWindows()

