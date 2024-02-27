import cv2
import numpy as np

img = cv2.imread('Llamame-Gatito.jpg')
height, width = img.shape[:2]

scale_factor = 0.5 
scaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Escalado', scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
