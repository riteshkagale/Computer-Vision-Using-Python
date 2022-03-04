# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:19:43 2022

@author: siddharth
"""

import cv2
import numpy as np

img = cv2.imread("dataset/cards1.jpg")
print(img.shape) #(275, 183, 3)

#cv2.circle(img, (35,90), 5, (255,255,0), cv2.FILLED) ##[35,90],[105,75],[65,190],[138,173]
#cv2.circle(img, (105,75), 5, (0,255,255), cv2.FILLED) ##[35,90],[105,75],[65,190],[138,173]
#cv2.circle(img, (65,190), 5, (0,255,0), cv2.FILLED) ##[35,90],[105,75],[65,190],[138,173]
#cv2.circle(img, (138,173), 5, (255,0,255), cv2.FILLED) ##[35,90],[105,75],[65,190],[138,173]

w = 183
h = 275
pts1 = np.float32([[37,92],[105,75],[65,190],[138,173]])
pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgWarp = cv2.warpPerspective(img, matrix, (w, h))

cv2.imshow("Samples", img)
cv2.imshow("Warped Sample", imgWarp)

cv2.waitKey(0)
cv2.destroyAllWindows()