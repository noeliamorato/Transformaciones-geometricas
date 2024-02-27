import cv2
import numpy as np

img = cv2.imread('Llamame-Gatito.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 210], [0, 1, 20]])
dst = cv2.warpAffine(img, M, (cols, rows))
concatenated_img = cv2.hconcat([img, dst])

cv2.imshow('Original vs Traslación', concatenated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
