#from cv2 import cv2 as cv
import cv2 as cv
import os

directoryname = os.getcwd() + '/datas/images/imageframes'
files = os.listdir(directoryname)
filename = directoryname+"/image_0.png"  # Once get shape information
img = cv.imread(filename)
height, width, layers = img.shape
size = (width, height)
fps = 5
filename_output = directoryname + '/output_video.avi'
out_avi = cv.VideoWriter(
    filename_output, cv.VideoWriter_fourcc(*'DIVX'), fps, size)
for count in range(len(files)):  # reading each files
    filename = directoryname+"/image_"+str(count)+".png"
    img = cv.imread(filename)
    if img is not None:
        cv.imshow('image_'+str(count), img)  # same title if you want one window.
        out_avi.write(img)
        cv.waitKey(1)
