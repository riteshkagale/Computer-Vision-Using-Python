# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:39:55 2022

@author: siddharth
"""

import cv2

cap = cv2.VideoCapture(0)#live web cam
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, frame = cap.read()
    cv2.imshow("video sample", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    