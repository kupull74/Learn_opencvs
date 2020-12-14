from cv2 import cv2 as cv
import numpy as np
import os
#import datas.PytesseractwithKorean
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

try:
    
    
    img = cv.imread("datas/images/26.png", cv.IMREAD_GRAYSCALE)
    #cv.imshow("Image",img)

    width,height = 250,300
    pts1 = np.float32([[126,44],[452,147],[44,296],[366,405]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv.warpPerspective(img,matrix,(width,height))
    
    #cv.imshow("Output",imgOutput)
    #cv.waitKey(0)
    #cv.destroyAllWindows()


    #img1 = cv.imread('datas/images/26.png',cv.IMREAD_GRAYSCALE)
    ret,th1 = cv.threshold(imgOutput,127,255,cv.THRESH_BINARY) # 127<pixel=0
    th2 = cv.adaptiveThreshold(imgOutput,255,cv.ADAPTIVE_THRESH_MEAN_C,\
    cv.THRESH_BINARY,11,4)
    
    th3 = cv.adaptiveThreshold(imgOutput,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv.THRESH_BINARY,11,4)
    

    titles = ['Original Image','BINARY','Adaptive Mean','Adaptive Gaussian']
    images = [img, th1, th2, th3]

    
    for i in range(4):
        plt.subplot(1,4,i+1);
        plt.imshow(images[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
        
    
    plt.show()
    #cv.imshow("Output",imgOutput)
    cv.waitKey(0)

except:
    pass