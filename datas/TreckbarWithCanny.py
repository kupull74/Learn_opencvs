from cv2 import cv2 as cv
#import numpy as np
import os
#import datas.PytesseractwithKorean
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

def nothing():
    pass
cv.namedWindow("Canny Edge")
cv.createTrackbar('low threshold', 'Canny Edge', 0, 1000, nothing)
cv.createTrackbar('high threshold', 'Canny Edge', 0, 1000, nothing)
img_gray = cv.imread('datas/images/lambo.png', cv.IMREAD_GRAYSCALE)

while True:
    low = cv.getTrackbarPos('low threshold', 'Canny Edge')
    high = cv.getTrackbarPos('high threshold', 'Canny Edge')

    #img = cv.imread("datas/images/lena.png")
    img_Canny = cv.Canny(img_gray,low,high)
    cv.imshow("Canny Image",img_Canny)
    if cv.waitKey(1) == ord('q'):
        break
