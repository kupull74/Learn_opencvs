from cv2 import cv2 as cv

try:
    img = cv.imread("datas/images/book.jpg")
    #imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgCanny = cv.Canny(img,150,200)
    cv.imshow("Canny Image",imgCanny)

    # imgBlur = cv.GaussianBlur(imgGray,(7,7),0)
    # cv.imshow("Blur Image",imgBlur)

    import numpy as np
    kernel = np.ones((3,3),np.uint8)

    imgDialation = cv.dilate(imgCanny,kernel,iterations=1)
    cv.imshow("Dialation Image",imgDialation)

    imgEroded = cv.erode(imgDialation,kernel,iterations=1)
    cv.imshow("Eroded Image",imgEroded)

    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    pass