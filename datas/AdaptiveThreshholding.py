from cv2 import cv2 as cv
import numpy as np
import os
#import datas.PytesseractwithKorean
import matplotlib.pyplot as plt
import pytesseract
# from pytesseract #import Output

try:
    img = cv.imread('datas/images/test1/sudoku.jpg',cv.IMREAD_GRAYSCALE)
    ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY) # 127<pixel=0
    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
    cv.THRESH_BINARY,11,4)
    
    th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv.THRESH_BINARY,11,4)
    

    titles = ['Original Image','BINARY','Adaptive Mean','Adaptive Gaussian']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(1,4,i+1);
        plt.imshow(images[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()
    cv.waitKey(0)

except:
    pass