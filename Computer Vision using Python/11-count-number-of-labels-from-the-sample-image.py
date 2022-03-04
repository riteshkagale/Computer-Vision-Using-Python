# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:02:29 2022

@author: siddharth
"""

import cv2
import numpy as np


img = cv2.imread("dataset/barcode.jpg")
img = cv2.resize(img, (320, 240))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 100, 150)
imgCopy = imgCanny.copy()


contours, hierarchy = cv2.findContours(imgCopy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
count = 0
for i,cnt in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    if area > 4000:
        labels = img[y:y + h, x:x + w]
        mask = np.zeros(img.shape[:2], dtype = "uint8")
        ((centerX, centerY), radius) = cv2.minEnclosingCircle(cnt)
        cv2.circle(mask, (int(centerX), int(centerY)), int(radius),255, -1)
        mask = mask[y:y + h, x:x + w]
        cv2.imshow("Masked labels", cv2.bitwise_and(labels, labels, mask = mask))
        count+=1
        cv2.imwrite("dataset/images/image_{}.jpg".format(count), labels)
        print("Total Labels are {}".format(count))
        cv2.waitKey(0)
cv2.destroyAllWindows()