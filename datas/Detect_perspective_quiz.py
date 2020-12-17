import cv2 
import numpy as np 
from cv2 import cv2 as cv
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output


img_color_approx = cv.imread('datas/images/namecard_01.jpg')
img_gray = cv.cvtColor(img_color_approx, cv.COLOR_BGR2GRAY) #회색으로...
#print(len(img_gray))
imgBlur = cv.GaussianBlur(img_gray, (7, 7), 1) #블러처리
imgCanny = cv.Canny(imgBlur, 50, 50) #캐니처리
cv.imshow('Canny and Gray', imgCanny) #보이기
imgContour = img_color_approx.copy() #이건 카피


#ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV)
contours, _= cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
for cnt in contours:
    #,y,w,h = cv.boundingRect(cnt)
    #print(x,y,w,h)
    
    

    area = cv.contourArea(cnt)
    print(area)
    if area > 500:
        epsilon = 0.1 * cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, epsilon, True)
        #cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
        
        print(len(approx))
        objCor = len(approx)
        x, y, w, h = cv.boundingRect(approx)

        cv.drawContours(img_color_approx, [approx], 0, (0,255,255), 2)
        
        width,height = 640,670
        pts1 = np.float32(approx)
        pts2 = np.float32([[0,0],[0,height],[width,height],[width,0]])
        matrix = cv.getPerspectiveTransform(pts1,pts2)    
        imgOutput = cv.warpPerspective(img_color_approx,matrix,(width,height))
        cv.rectangle(img_color_approx, (x,y), (x+w, y+h), (255,255,0), 2)
            
     

cv.imshow("Result approx", img_color_approx)
cv.imshow("Output",imgOutput)
    

cv.waitKey(0)


# cv.imshow('shapes',getContours(cv.imread('datas/images/shapes_canny.png')))
# def getContours(img):
#     contours, hierarchy = cv.findContours(
#     img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
#     print('hierarchy : ', hierarchy)
# for cnt in contours:
#     area = cv.contourArea(cnt)
#     print(area)
#     if area > 500:
#         cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
#         peri = cv.arcLength(cnt, True)
#         approx = cv.approxPolyDP(cnt, 0.02*peri, True)
#         objCor = len(approx)
#         x, y, w, h = cv.boundingRect(approx)
#         if objCor == 3:
#             cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)