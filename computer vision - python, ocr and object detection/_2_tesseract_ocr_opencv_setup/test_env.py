# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 12:04:58 2022

@author: siddharth
"""

#import libraries
import pytesseract
import pkg_resources
import cv2

#declaring the exe path for tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#printing the tesseract version
print(pkg_resources.working_set.by_key['pytesseract'].version)

#printing the opencv version
print(cv2.__version__)

