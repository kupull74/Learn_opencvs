import cv2 
import numpy as np 
import matplotlib.pyplot as plt

from cv2 import cv2 as cv
import os, requests, wget

img_color_approx = cv.imread('datas/images/shapes.png')
img_gray = cv.cvtColor(img_color_approx, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
contours, _= cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    print(x,y,w,h)
    epsilon = 0.008 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    print(len(approx))
       
    cv.drawContours(img_color_approx, [approx], 0, (0,255,255), -1)
    #print(img_color)
cv.imshow("Result approx", img_color_approx)
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