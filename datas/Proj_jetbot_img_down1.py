import cv2 
import numpy as np 
import matplotlib.pyplot as plt

from cv2 import cv2 as cv
import os, requests, wget

import os 
os.getcwd()
import time

from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request


driver = webdriver.Chrome("/home/jerry/Documents/Develop/chromedriver")
driver.get("https://www.google.com/search?q=road+with+signs&sxsrf=ALeKk01WPahvxB5yzHLceatat1nuVY1u2w:1608091891097&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjG9byP0dHtAhWNfXAKHerZAx8Q_AUoAXoECBEQAw&biw=1848&bih=jpg")

driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').click() 
#driver.find_element_by_xpath('//*[@id="txt"]/form/div[2]/div[2]/button').click()

m_imgs=driver.find_elements_by_css_selector(".autosize") #.get_attribute("src")
count = 1 
for m_img in m_imgs:
    #print(m_imgs)
    count = count + 1
    imgs = m_img.get_attribute("src")
    urllib.request.urlretrieve(imgs, str(count) + ".jpg")