# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 11:38:16 2022

@author: siddharth
"""

import cv2

img = cv2.imread("dataset/apple.jpg")

cv2.imshow("Sample", img)
cv2.waitKey(0)