import cv2
import numpy as np



resim = cv2.imread("Ders5\kemalsunal.webp")
resim[175:220,400:580,0]=255#bu kod belirli bir bölgedeki (175:220 satırlar, 400:580 sütunlar) piksellerin mavi kanalını 255'e ayarlar.
#resim[:,:,0]=50#bu kod, görüntünün mavi kanalındaki tüm piksellerin rengini 50 olarak ayarlar. 
#resim[:,:,1]=200# bu görüntüdeki tüm piksellerin yeşil kanalını (kanal 1), 200 değeriyle ayarlar




cv2.imshow("Kemal Sunal" , resim)





cv2.waitKey(0)
cv2.destroyAllWindows()