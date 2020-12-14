from cv2 import cv2 as cv
import numpy as np

try:
    img = cv.imread("datas/images/24.jpg")
    cv.imshow("Image",img)

    width,height = 250,300
    pts1 = np.float32([[769,110],[943,146],[787,412],[964,409]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv.warpPerspective(img,matrix,(width,height))
    cv.imshow("Output",imgOutput)

    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    pass