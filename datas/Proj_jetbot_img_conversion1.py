#import cv2 
import numpy as np 
#import matplotlib.pyplot as plt
import cv2 as cv
import os
#import requests, wget

img_color_approx = cv.imread('snapshots/048.jpg')
img_gray = cv.cvtColor(img_color_approx, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(img_gray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 100, 180)
ret, img_binary = cv.threshold(img_gray, 80, 255, cv.THRESH_BINARY_INV)
#120부터 노이즈 낌 100이 그나마 제일 나은듯
cv.imshow('Blur', imgBlur)
cv.imshow('Canny', imgCanny)
cv.imshow('binary', img_binary)


# img_color_approx = cv.imread('datas/images/namecard_01.jpg')
# img_gray = cv.cvtColor(img_color_approx, cv.COLOR_BGR2GRAY) #회색으로...
# #print(len(img_gray))
# imgBlur = cv.GaussianBlur(img_gray, (7, 7), 1) #블러처리
# imgCanny = cv.Canny(imgBlur, 50, 50) #캐니처리


# 125, 100   230, 100
# imgContour = img_color_approx.copy()
# cv.THRESH_BINARY_INV


th2 = cv.adaptiveThreshold(imgCanny,255,cv.ADAPTIVE_THRESH_MEAN_C,\
    cv.THRESH_BINARY,11,4)
  
th3 = cv.adaptiveThreshold(imgCanny,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv.THRESH_BINARY,11,4)



contours, _= cv.findContours(img_gray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv.contourArea(cnt)
    print(area)
    if area > 500:
        epsilon = 0.02 * cv.arcLength(cnt, True) #꼭지점 숫자? 각도?
        approx = cv.approxPolyDP(cnt, epsilon, True) #폴리곤 그리기?
        
        objCor = len(approx)  #폴리곤? 들의 꼭지점 갯수 정의
        if objCor == 4: #꼭지점이 4개인 놈들을
        # x, y, w, h = cv.boundingRect(approx) #좌표들
            cv.drawContours(img_color_approx, [approx], 0, (0,255,255), 2) #컨투어 그리기?
        #    cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 1) #그려내라 뭐 이건가
cv.imshow("Result approx", img_color_approx)
cv.waitKey(0)

