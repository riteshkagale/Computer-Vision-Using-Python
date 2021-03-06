# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:07:17 2022

@author: siddharth
"""

#import libraries
import numpy as  np
import cv2

# load the image to detect
img_to_detect = cv2.imread('testing/scene7.jpg')
# get width, height of the image
img_height = img_to_detect.shape[0]
img_width = img_to_detect.shape[1]
# resize to match input size
resized_img_to_detect = cv2.resize(img_to_detect,(300,300))
# convert to blob to pass into model
img_blob = cv2.dnn.blobFromImage(resized_img_to_detect,0.007843,(300,300),127.5)
# recommended scale factor is 0.007843, width,height of blob is 300,300, mean of 255 is 127.5, 

# set of 21 class labels in alphabetical order (background + rest of 20 classes)
class_labels = ["background", "aeroplane", "bicycle", "bird", "boat","bottle", 
                "bus", "car", "cat", "chair", "cow", "diningtable","dog", 
                "horse", "motorbike", "person", "pottedplant", "sheep","sofa", 
                "train", "tvmonitor"]

# Loading pretrained model from prototext and caffemodel files
mobilenetssd = cv2.dnn.readNetFromCaffe('models/mobilenetssd.prototext', 
                                        'models/mobilenetssd.caffemodel')
# input preprocessed blob into model and pass through the model
mobilenetssd.setInput(img_blob)
# obtain the detection predictions by the model using forward() method
obj_detections = mobilenetssd.forward()

# returned obj_detections[0, 0, index, 1] , 
# 1 => will have the prediction class index
# 2 => will have confidence, 
# 3 to 7 => will have the bounding box co-ordinates
no_of_detections = obj_detections.shape[2]

# loop over the detections
for index in np.arange(0, no_of_detections):
    prediction_confidence = obj_detections[0, 0, index, 2]
    # take only predictions with confidence more than 20%
    if prediction_confidence > 0.20:
        #get the predicted label
        predicted_class_index = int(obj_detections[0, 0, index, 1])
        predicted_class_label = class_labels[predicted_class_index]

        #obtain the bounding box co-oridnates for actual image from resized image size
        bounding_box = obj_detections[0, 0, index, 3:7] * np.array([img_width, img_height, img_width, img_height])
        (start_x_pt, start_y_pt, end_x_pt, end_y_pt) = bounding_box.astype("int")
        
        # print the prediction in console
        predicted_class_label = "{}: {:.2f}%".format(class_labels[predicted_class_index], prediction_confidence * 100)
        print("predicted object {}: {}".format(index+1, predicted_class_label))
        
        # draw rectangle and text in the image
        cv2.rectangle(img_to_detect, (start_x_pt, start_y_pt), (end_x_pt, end_y_pt), (0,255,0), 2)
        cv2.putText(img_to_detect, predicted_class_label, (start_x_pt, start_y_pt-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

cv2.imshow("Detection Output", img_to_detect)


