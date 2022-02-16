# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:34:50 2022

@author: siddharth
"""

#import the libraries
from tensorflow.keras.applications import Xception
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np
import cv2

#loading the image
img_path = '../images/test12.jpg'
img = load_img(img_path)

#Resize to 299*299
img = img.resize((299, 299))
#convert img to array
img_array = img_to_array(img)

#convert image into 4 dimensional tensor
#convert from (height, width, channel) to (batchsize, height, width, channel)
img_array = np.expand_dims(img_array, axis=0)

#preprocess the input image array
img_array = preprocess_input(img_array)

#load the model
pretrained_model = Xception(weights='imagenet')

#predict
prediction = pretrained_model.predict(img_array)

#decode the predictions
actual_prediction = imagenet_utils.decode_predictions(prediction)

print("Predicted Object is: ", (actual_prediction[0][0][1]).upper())
print("Accuracy is:", actual_prediction[0][0][2]*100)

#read image
disp_img = cv2.imread(img_path)
cv2.putText(disp_img,  (actual_prediction[0][0][1]).upper(), (20, 20), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0))
cv2.imshow("Prediction", disp_img)
