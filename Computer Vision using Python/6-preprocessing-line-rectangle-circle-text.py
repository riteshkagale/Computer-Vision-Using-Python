# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:43:33 2022

@author: siddharth
"""

import cv2
import numpy as np

img = np.zeros((480, 640, 3))

#Full Green
#img[:]=(0, 255, 0) 

#small portion Red
#img[100:200, 250:350]=(0, 0, 255) 

cv2.line(img, (0, 0), (640, 480), (255, 255, 0), 1)
cv2.rectangle(img, (100, 200), (300, 400), (255, 0, 255), 1)
cv2.circle(img, (500,200), 140, (0, 255, 255), cv2.FILLED)
cv2.putText(img, "OPENCV", (120,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)

cv2.imshow("sample", img)
cv2.waitKey(0)
cv2.destroyAllWindows()