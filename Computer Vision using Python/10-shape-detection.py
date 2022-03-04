# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:33:59 2022

@author: siddharth
"""

import cv2


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area > 200:
            cv2.drawContours(imgCopy, cnt, -1, (255,0,0), 3)
            parameter = cv2.arcLength(cnt, True)
            #print(parameter)
            approx = cv2.approxPolyDP(cnt, 0.02*parameter, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 3: 
                objectType = "Triangle"
            elif objCor == 4:
                aspRatio = w/float(h)
                #print(aspRatio)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    #print("asp: ",aspRatio)
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circle"
            else:
                objectType = "None"
            cv2.rectangle(imgCopy, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgCopy, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)

img = cv2.imread("dataset/shapes1.png")
img = cv2.resize(img, (320, 240))
imgCopy = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 100, 100)
getContours(imgCanny)

cv2.imshow("Sample", img)
cv2.imshow("Gray Sample", imgGray)
cv2.imshow("Blur Sample", imgBlur)
cv2.imshow("Canny Sample", imgCanny)
cv2.imshow("Contour sample", imgCopy)
cv2.waitKey(0)
cv2.destroyAllWindows()