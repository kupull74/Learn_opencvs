from cv2 import cv2 as cv
import os
cascadefile = "datas/haar_cascade_files/haarcascade_frontalface_default.xml"
cascadefile1 = "datas/haar_cascade_files/haarcascade_eye.xml"
cascadefile2 = "datas/haar_cascade_files/haarcascade_mcs_nose.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_lefteye_2splits.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_righteye_2splits.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_eye_tree_eyeglasses.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_frontalcatface_extended.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_fullbody.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_frontalface_alt.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_frontalface_alt2.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_smile.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_upperbody.xml"


cascade = cv.CascadeClassifier(cascadefile)
cascade1 = cv.CascadeClassifier(cascadefile1)
cascade2 = cv.CascadeClassifier(cascadefile2)
# filepath = 'datas/images/lena.png'    # sigle human
# filepath = 'datas/images/faces.jpg'      # few human -> one missing
filepath = 'datas/images/faces.jpg'    # a lot human -> can't detect little bit
img = cv.imread(filepath)
# faces = cascade.detectMultiScale(img, 1.1, 4)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(imgGray, 1.1, 4)
eyes = cascade1.detectMultiScale(imgGray, 1.1, 4)
noses = cascade2.detectMultiScale(imgGray, 1.1, 4)

directoryname = os.getcwd() + '/face_cropped'
cnt = 0
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    imgCropped = img[y:y+h, x:x+w] # image numpy matrix     좌표 y:y, x:x

    # cv.imshow("Result", img)
    imgResize = cv.resize(img, (1400, 1000))
    cv.imshow("imgResize",imgResize)
    cv.imshow("Image Cropped",imgCropped)
    cnt = cnt + 1
    cv.imwrite(directoryname + "/face_"+str(cnt)+".png", imgCropped)
    cv.waitKey(0)
    

for (x, y, w, h) in eyes:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)
    imgCropped = img[y:y+h, x:x+w] # image numpy matrix     좌표 y:y, x:x
    
    #cv.imshow("Image",img)
    #cv.imshow("Result", img)
    imgResize = cv.resize(img, (1400, 1000))
    cv.imshow("imgResize",imgResize)
    cv.imshow("Image Cropped",imgCropped)
    cv.waitKey(0)
for (x, y, w, h) in noses:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    imgCropped = img[y:y+h, x:x+w] # image numpy matrix     좌표 y:y, x:x
    
    #cv.imshow("Image",img)
    #cv.imshow("Result", img)
    imgResize = cv.resize(img, (1400, 1000))
    cv.imshow("imgResize",imgResize)
    cv.imshow("Image Cropped",imgCropped)

    

    cv.waitKey(0)
cv.destroyAllWindows()
