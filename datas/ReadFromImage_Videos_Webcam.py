######################## READ IMAGE ############################
#from cv2 import cv2 as cv
# import cv2 as cv
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv.imread("datas/images/lena.png")
# # DISPLAY
# cv.imshow("Lena Soderberg",img)
# cv.waitKey(0)

######################### READ VIDEO #############################
from cv2 import cv2 as cv
frameWidth = 320
frameHeight = 240
cap = cv.VideoCapture("datas/videos/roadway_1.mp4")
while True:
    success, img = cap.read()
    img = cv.resize(img, (frameWidth, frameHeight))
    #frameWidth = frameWidth + 20
    #frameHeight = frameHeight + 20
    cv.imshow("Result", img)
    if cv.waitKey(30) == ord('q'):
        break
cap.release()

# ######################### READ WEBCAM  ############################
# from cv2 import cv2 as cv
# 1280/720
# 640/480
# 2560/960
# 1280/480

# frameWidth = 1366
# frameHeight = 768
# cap = cv.VideoCapture(2)

# cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
# cap.set(cv.CAP_PROP_BRIGHTNESS,10)
# #cap.set(cv.CAP_PROP_CONTRAST,2)
# cap.set(cv.CAP_PROP_SATURATION,70)
# #cap.set(cv.CAP_PROP_WHITE_BALANCE_BLUE_U,10)
# while cap.isOpened():
#     success, img = cap.read()
#     cv.imshow("Result", img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()