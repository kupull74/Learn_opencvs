#from cv2 import cv2 as cv
import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
img[:]= 255,0,0     # Try 0,255,0
print(img.shape)

cv.line(img,(0,100),(img.shape[1],img.shape[0]),(0,255,0),3) # 첫번째는 좌표, 쉐입은 모르겠고, 세번째는 칼라, 네번째는 두께
cv.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv.imshow("Image",img)

cv.circle(img,(380,180),30,(255,255,0),3) #첫번째는 좌표, 두번째는 반지름, 세번째괄호는 칼라, 마지막 숫자는 선두께

x,y,w,h = 310,320,150,160
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.putText(img," OPENCV  ",(300,270),cv.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
cv.imshow("Image",img)

cv.waitKey(0)
cv.destroyAllWindows()