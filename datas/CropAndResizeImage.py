from cv2 import cv2 as cv
import numpy as np

# img = cv.imread("datas/images/shapes.png")
img = cv.imread("datas/images/15.jpg")
print(img.shape)
# (462, 623, 3)

imgResize = cv.resize(img,(1000,500))
print(imgResize.shape)
# (500, 1000, 3)
cv.imshow("Image Resize",imgResize)

imgCropped = img[350:453,92:185] # image numpy matrix     좌표 y:y, x:x

cv.imshow("Image",img)
cv.imshow("Image Cropped",imgCropped)

cv.waitKey(0)
cv.destroyAllWindows()