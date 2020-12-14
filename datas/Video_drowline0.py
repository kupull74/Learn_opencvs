######################## READ IMAGE ############################
# from cv2 import cv2 as cv
# import cv2 as cv
# LOAD AN IMAGE USING 'IMREAD'
# img = cv.imread("datas/images/lena.png")
# # DISPLAY
# cv.imshow("Lena Soderberg",img)
# cv.waitKey(0)

######################### READ VIDEO #############################
from cv2 import cv2 as cv
frameWidth = 1136
frameHeight = 640
cap = cv.VideoCapture("datas/videos/roadway_01.mp4")
while True:
    success, img = cap.read()
    #img = cv.resize(img, (frameWidth, frameHeight))
    # frameWidth = frameWidth + 20
    # frameHeight = frameHeight + 20
    cv.imshow("Result", img)
    if cv.waitKey(30) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
