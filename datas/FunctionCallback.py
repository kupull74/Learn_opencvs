from cv2 import cv2 as cv
import numpy as np
import os
#import datas.PytesseractwithKorean
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

def callback1(a,b):
    print('callback1 = {0}'.format(a+b))

def callback2(a):
    print('callback2 = {0}'.format(a**2))

def callback3():
    print('callback1 = hello world')

def callthecallback(callback=None, cargs=()):
    print('call the callback')
    if callback !=None:
        callback(*cargs)

callthecallback(callback1, cargs=(1,2))
callthecallback(callback2, cargs=(2,))
callthecallback(callback3)  #callback1 = hello world                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

        