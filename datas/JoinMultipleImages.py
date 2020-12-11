from cv2 import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)
cap1 = cv.VideoCapture("datas/videos/roadway_01.mp4")

try:
    while cap.isOpened() & cap1.isOpened():
        ret, frame = cap.read()
        sucess, video = cap1.read()
        img = cv.imread('datas/images/15.jpg')
        #cv.waitKey(0)
        imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        grayTOBGR = cv.cvtColor(imgGray, cv.COLOR_GRAY2BGR)

        imgHor = np.hstack((frame, img, grayTOBGR))
        imgHor1 = np.hstack((img, grayTOBGR, video))
        imgVer = np.vstack((imgHor,imgHor1))
        

        imgResize = cv.resize(imgVer, (1000, 1000))
        cv.imshow("imgResize",imgResize)
        

        #cv.waitKey(0)
            
        # img = cv.imread('datas/images/15.jpg')
        # imgStack = stackImages(0.6, ([frame, img, video], [img, video, frame]))
        # cv.imshow("ImageStack", imgStack)
        # if cv.waitKey(1) == 27:
        #     break
except :
    pass
finally:
   
    cap.release()
    cv.destroyAllWindows()

    # frameWidth = 320
    # frameHeight = 200
    # cap = cv.VideoCapture("datas/videos/Armbot.mp4")
    # while True:
    #     success, img = cap.read()
    #     img = cv.resize(img, (frameWidth, frameHeight))
    #     # frameWidth = frameWidth + 20
    #     # frameHeight = frameHeight + 20
    #     cv.imshow("Result", img)
    #     if cv.waitKey(30) == ord('q'):
    #         break
    # cap.release()


   

# def Video():
#     frameWidth = 320
#     frameHeight = 200
#     cap = cv.VideoCapture("datas/videos/Armbot.mp4")
#     while True:
#         success, img = cap.read()
#         img = cv.resize(img, (frameWidth, frameHeight))
#         # frameWidth = frameWidth + 20
#         # frameHeight = frameHeight + 20
#         cv.imshow("Result", img)
#         if cv.waitKey(30) == ord('q'):
#             break
#     cap.release()

# #Video()

# imgStack = stackImages(0.5, ([img, imgGray, img], [imgGray, img, imgGray]))
# cv.imshow("ImageStack", imgStack)


# cv.destroyAllWindows()
