# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:48:20 2022

@author: siddharth
"""

import cv2
import numpy as np

img = cv2.imread("dataset/dog.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.medianBlur(imgGray, 7, 0)
imgCanny = cv2.Canny(imgBlur, 90, 90)
kernel = np.ones((3,3), np.uint8)
imgDilate = cv2.dilate(imgCanny, kernel, iterations=5)
imgErode = cv2.erode(imgDilate, kernel, iterations=3)

cv2.imshow("Gray sample", imgGray)
cv2.imshow("Blur sample", imgBlur)
cv2.imshow("Canny sample", imgCanny)
cv2.imshow("Dilation sample", imgDilate)
cv2.imshow("Erodation sample", imgErode)
cv2.waitKey(0)
