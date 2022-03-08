# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:27:58 2022

@author: siddharth
"""

import cv2

faceCascade = cv2.CascadeClassifier("dataset/FaceFontal_default.xml")

img = cv2.imread("dataset/person1.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0))
    

cv2.imshow("sample", img)
cv2.waitKey(0)