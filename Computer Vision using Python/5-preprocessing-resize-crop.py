# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:17:47 2022

@author: siddharth
"""

import cv2

img = cv2.imread("dataset/apple.jpg")
print(img.shape)

imgResize = cv2.resize(img, (640, 480))

imgCrop = imgResize[0:200,200:500]

cv2.imshow("Sample", img)
cv2.imshow("Resize Sample", imgResize)
cv2.imshow("Crop Sample", imgCrop)

cv2.waitKey(0)
cv2.destroyAllWindows()

