import cv2 
import numpy as np 
import matplotlib.pyplot as plt

from cv2 import cv2 as cv
import os, requests, wget
def store_raw_images():
    jetbot_images_link = 'https://www.google.com/search?q=road+with+signs&sxsrf=ALeKk01WPahvxB5yzHLceatat1nuVY1u2w:1608091891097&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjG9byP0dHtAhWNfXAKHerZAx8Q_AUoAXoECBEQAw&biw=1848&bih=jpg' # using Above URI
    res = requests.get(jetbot_images_link)
    jetbot_image_urls = res.content.decode("utf-8")
    
    count = 0
    for geturl in jetbot_image_urls.split('\r\n'):
        count+=1
        try:
            image_name = os.getcwd() + '/datas/jetbot/' + geturl.split('/')[-1]
            retname = wget.download(url=geturl, out=image_name)
        except Exception as e:
            print(str(e))
if __name__ == "__main__":
    store_raw_images()
    # if cv.waitKey(1)==13: #or count==1000:
    #     break    


    