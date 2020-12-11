from cv2 import cv2 as cv
import numpy as np
import os
#import datas.PytesseractwithKorean
import matplotlib.pyplot as plt


try:
    img = cv.imread('datas/images/test1/ko11.png', cv.IMREAD_GRAYSCALE)
    ret,thresh1 = cv.threshold(img,100,255,cv.THRESH_BINARY)

    titles = ['Original Image','BINARY']
    images = [img, thresh1]
    for i in range(6):
        plt.subplot(2,3,i+1);
        plt.imshow(images[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()
    cv.waitKey(0)
    
    def threshholding(image):
        return cv.threshhold(image, 50, 255, cv.THERSH_BINARY+cv.THRESH_OPSU)[1]


        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = threshholding(img_gray)
        cv.imshow(['threshold', img])

    import pytesseract
    from pytesseract import Output

    custom_config = r'--oem 3 --psm 6 -l kor+kor_vert+eng'
    words_string = pytesseract.image_to_string(img)
    words = pytesseract.image_to_data(img, config = custom_config, output_type=Output.DICT)

    print(words.keys())
    n_boxes = len(words['text'])
    for i in range(n_boxes):
        if int(words['conf'][i]) > 40:
            (x,y,w,h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
            img = cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
            cv.imshow('Resource', img)
            
    cv.waitKey(0)

except:
    pass