######################## READ IMAGE ############################
# from cv2 import cv2 as cv
import cv2 as cv
import numpy as np

# mesh img load
img = cv.imread("datas/images/load_image.jpg")
# cv.imshow("Messi", img)
#cv.waitKey(0)

#cv.line(img,(0,100),(img.shape[1],img.shape[0]),(0,255,0),3) # 첫번째는 좌표, 쉐입은 모르겠고, 세번째는 칼라, 네번째는 두께
cv.rectangle(img,(50,60),(120,125),(0,0,255),2)
#cv.imshow("Image",img)

cv.circle(img,(240,95),50,(255,255,0),2) #첫번째는 좌표, 두번째는 반지름, 세번째괄호는 칼라, 마지막 숫자는 선두께

cv.rectangle(img,(415,300),(470,240),(0,0,255),2) # 첫번째는 크기, 두번째가 좌표, 세번째는 칼라, 네번째는 선 두께.
#cv.imshow("Image",img)

x,y,w,h = 330,280,65,60
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.putText(img," GOD~DAMN~OPENCV!!  ",(90,180),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv.imshow("Image",img)

cv.waitKey(0)
cv.destroyAllWindows()
    
