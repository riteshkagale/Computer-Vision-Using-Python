# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:07:23 2022

@author: siddharth
"""

import cv2
import numpy as np


def empty(a):
    pass

path = "dataset/apple.jpg"
w_name = "TrackBars" 
cv2.namedWindow(w_name)
cv2.resizeWindow(w_name, (640,240))
cv2.createTrackbar("Hue min", w_name, 0, 179, empty)
cv2.createTrackbar("Hue max", w_name, 179, 179, empty)
cv2.createTrackbar("Sat min", w_name, 98, 255, empty)
cv2.createTrackbar("Sat max", w_name, 255, 255, empty)
cv2.createTrackbar("Val min", w_name, 0, 255, empty)
cv2.createTrackbar("Val max", w_name, 255, 255, empty)


while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue min", w_name)
    h_max = cv2.getTrackbarPos("Hue max", w_name)
    s_min = cv2.getTrackbarPos("Sat min", w_name)
    s_max = cv2.getTrackbarPos("Sat max", w_name)
    v_min = cv2.getTrackbarPos("Val min", w_name)
    v_max = cv2.getTrackbarPos("Val max", w_name)
    #print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower_value = np.array([h_min, s_min, v_min])
    upper_value = np.array([h_max, s_max, v_max])
    imgMask = cv2.inRange(imgHSV, lower_value, upper_value)
    
    imgBitwiseAnd = cv2.bitwise_and(img, img, mask=imgMask)
    
    cv2.imshow("BGR sample", img)
    cv2.imshow("HSV sample", imgHSV)
    cv2.imshow("Mask sample", imgMask)
    cv2.imshow("Result sample", imgBitwiseAnd)
    
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()