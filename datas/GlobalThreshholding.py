from cv2 import cv2 as cv
import numpy as np
import os
#import datas.PytesseractwithKorean
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

try:
    img = cv.imread('datas/images/test1/ko11.png',cv.IMREAD_GRAYSCALE)
    ret,thresh1 = cv.threshold(img,100,255,cv.THRESH_BINARY) # 127<pixel=0
    ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV) # 127>pixel=0
    ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC) # 127<pixel=pixel
    ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO) # 127>pixel=pixel
    ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV) # 127<pixel=0

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1);
        plt.imshow(images[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()
    cv.waitKey(0)

except:
    pass