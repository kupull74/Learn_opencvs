from cv2 import cv2 as cv
import numpy as np

try:
    img = cv.imread("datas/images/lambo.png")
    cv.imshow("Image",img)

    width,height = 480,200
    pts1 = np.float32([[177,87],[518,229],[50,234],[442,431]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv.warpPerspective(img,matrix,(width,height))
    cv.imshow("Output",imgOutput)

    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    pass