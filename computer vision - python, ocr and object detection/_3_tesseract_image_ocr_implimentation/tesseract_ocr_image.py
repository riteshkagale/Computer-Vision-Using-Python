# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 12:25:50 2022

@author: siddharth
"""

#import the libraries
from PIL import Image
import pytesseract
import cv2
import re

#declaring the exe path for tesseract
#pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#load the image
image_to_ocr = cv2.imread('sample_images/image1.png')

#preprocessing the image
# step1: convert the image to gray
preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)
# step2: do binary and otsu thresholding
preprocessed_img = cv2.threshold(preprocessed_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# step3: smooth the image using median blur
preprocessed_img = cv2.medianBlur(preprocessed_img, 3)

#save the preprocessed image temporarily into the disk
cv2.imwrite("temp_image/test_preprocessed_img.jpg", preprocessed_img)

#read the temp image from the disk as pil image
preprocessed_pil_img = Image.open("temp_image/test_preprocessed_img.jpg")

#pass preprocessed pil image to tesseract to do ocr
text_extracted = pytesseract.image_to_string(preprocessed_pil_img)


# The print to console may not work in case there are 'non-printable' chars included in the string. 
# Please try the below code to transform the string using regular expression prior to printing

#print the text
text_extracted = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', text_extracted)
print(text_extracted)

#display the actual image
cv2.imshow("Actual Image", image_to_ocr)