import cv2 
import numpy as np 
import matplotlib.pyplot as plt

from cv2 import cv2 as cv
import os, requests, wget

img_color_approx = cv.imread('snapshots/050.jpg')
img_gray = cv.cvtColor(img_color_approx, cv.COLOR_BGR2GRAY)
#print(len(img_gray))

imgBlur = cv.GaussianBlur(img_gray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 180, 100)
cv.imshow('Canny and Gray', imgCanny)

ret, img_binary = cv.threshold(img_gray, 90, 255, cv.THRESH_BINARY_INV)
cv.imshow('Conversions', img_binary)


contours, _= cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
for cnt in contours:
    area = cv.contourArea(cnt)
    if area > 500:
        epsilon = 0.02 * cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, epsilon, True)
        print(len(imgCanny))
        
        #cv.drawContours(img_color_approx, [approx], 0, (0,255,255), 1)
        objCor = len(approx)  #폴리곤? 들의 꼭지점 갯수 정의
        if objCor == 4: #꼭지점이 4개인 놈들을
            cv.drawContours(img_color_approx, [approx], 0, (0,255,255), 2)
    
    
    

cv.imshow("Result approx", img_color_approx)
cv.waitKey(0)
#cv.imshow("Result approx", img_color_approx)
#cv.waitKey(0)


# for cnt in contours:
#     x,y,w,h = cv.boundingRect(cnt)
#     print(x,y,w,h)
#     epsilon = 0.01 * cv.arcLength(cnt, True)
#     approx = cv.approxPolyDP(cnt, epsilon, True)
#     print(len(approx))
       
#     cv.drawContours(img_color_approx, [approx], 0, (0,255,255), 1)
#     cv.rectangle(img_color_approx, (x,y), (x+w, y+h), (255,255,0), 2)
    
#     vertexNum = len(approx)
#     objectType = None

#     txt = cv.putText(img_color_approx, objectType,
#                         (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.7,
#                         (0, 0, 0), 2)
#     if vertexNum == 3:
#         objectType = "TriGun"

#     if objectType:
#         txt

#     if vertexNum == 4:
#         objectType = "Squadron"

#     if objectType:
#         txt

#     if vertexNum > 4:
#         objectType = "Circus"

#     if objectType:
#         cv.putText(img_color_approx, objectType,
#                         (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.7,
#                         (0, 0, 0), 2)

# cv.imshow("Result approx", img_color_approx)
# cv.waitKey(0)


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