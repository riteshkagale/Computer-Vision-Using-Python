# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:02:23 2022

@author: siddharth
"""

import cv2

cap = cv2.VideoCapture("dataset/people_walking.mp4")

while True:
    success, frame = cap.read()
    cv2.imshow("video sample", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    