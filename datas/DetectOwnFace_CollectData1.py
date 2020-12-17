import cv2 
import numpy as np 
from cv2 import cv2 as cv
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output
import os

cascadefile = "datas/haar_cascade_files/haarcascade_frontalface_default.xml"
cascade = cv.CascadeClassifier(cascadefile)

filepath = 'datas/images/faces.jpg'
img = cv.imread(filepath)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_detector = cascade.detectMultiScale(imgGray, 1.1, 4)
directory_name = os.getcwd() + '/face_cropped'
cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read(); #put_text ="
    #cascade_face = face_detector(frame)
    cropped_area = face_extractor(frame)
        count = 0
    if cropped_area is not None:
        count+=1
        area = cv.resize(cropped_area,(200,200))
        area = cv.cvtColor(area,cv.COLOR_BGR2GRAY)
        file_name = directory_name + 'user' +str(count) + '.jpg'
        cv.imwrite(file_name,area)
        put_text = "Face Found!, imwrite() count" + str(count)
    else:
        put_text = "Face not Found!"
    
    cv.putText(area,put_text,(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv.imshow('Face Cropper', area)
    
    count=0
    if cv.waitKey(1)==ord('q') or count == 1000:
        break
cap.release


