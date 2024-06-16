import cv2
import numpy as np


resim = np.zeros((300,300,3),dtype="uint8")#Böyle boş bir yapı oluşturabiliyoruz ve tüm matrisleri 0 olur
print(resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
