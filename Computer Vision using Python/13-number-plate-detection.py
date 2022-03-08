# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:46:19 2022

@author: siddharth
"""

import cv2


w = 640
h = 480
minArea = 500
number_plate = cv2.CascadeClassifier("dataset/HaarCascade_numberPlate.xml")


img = cv2.imread("dataset/car2.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

nPlate = number_plate.detectMultiScale(imgGray, 1.1, 1)

for (x, y, w, h) in nPlate:
    area = w*h
    if area > minArea:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
    imgROI = img[y:y+h, x:x+w]
    cv2.imshow("Number Detected", imgROI)

cv2.imshow("sample", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
