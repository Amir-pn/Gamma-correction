
from email.mime import image
import cv2
import numpy as np
 
path= ('C:/Users/dell/Desktop/Project/images/image1.jpg')
i=0
def gammaCorrection(image, gamma):
    i=+1
    table = [((i / 255) ** (1 / gamma)) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    return cv2.LUT(image, table)
 
  
img = cv2.imread(path)
gamma_corrected = gammaCorrection(img, 0.1)
cv2.imwrite("C:/Users/dell/Desktop/Project/images/Results/Image(1)_for different gammas/Image(1).jpg" ,gamma_corrected)
gamma_corrected2 = gammaCorrection(img, 0.3)
cv2.imwrite("C:/Users/dell/Desktop/Project/images/Results/Image(1)_for different gammas/Image(2).jpg" ,gamma_corrected2)
gamma_corrected3 = gammaCorrection(img, 0.6)
cv2.imwrite("C:/Users/dell/Desktop/Project/images/Results/Image(1)_for different gammas/Image(3).jpg" ,gamma_corrected3)
 
# cv2.imshow('Before gamma correction', img)
# cv2.imshow('After gamma correction', gamma_corrected)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()

###########################3

