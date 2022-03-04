# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:19:15 2022

@author: siddharth
"""

import cv2
#import numpy as np


def hconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    # take minimum hights
    h_min = min(img.shape[0] for img in img_list)
      
    # image resizing 
    im_list_resize = [cv2.resize(img,
                                 (int(img.shape[1] * h_min / img.shape[0]),h_min), 
                                 interpolation= interpolation) 
                      for img in img_list]
      
    # return final image
    return cv2.hconcat(im_list_resize)



def vconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    # take minimum width
    w_min = min(img.shape[1] for img in img_list)
      
    # resizing images
    im_list_resize = [cv2.resize(img,
                      (w_min, int(img.shape[0] * w_min / img.shape[1])),
                                 interpolation = interpolation)
                      for img in img_list]
    # return final image
    return cv2.vconcat(im_list_resize)


img = cv2.imread("dataset/cat.jpg")
img1 = cv2.imread("dataset/cards.jpg")

### Type 1 using Numpy
#imgHor = np.hstack([img, img1])
#imgVer = np.vstack([img, img1])
#cv2.imshow("Horzontal stack Sample", imgHor)
#cv2.imshow("Vertical stack Sample", imgVer)

### Type 2 using cv2
#imgConHor = cv2.hconcat([img, img1])
#imgConVer = cv2.vconcat([img, img1])
#cv2.imshow("cv2 concatinate Horzontal stack Sample", imgConHor)
#cv2.imshow("cv2 concatinate  Vertical stack Sample", imgConVer)


### Type 3 creating resize functions for horizontal and vertical stack 
# function calling
img_h_resize = hconcat_resize([img, img1, img])
img_v_resize = vconcat_resize([img, img1, img])

# show the Output image
cv2.imshow('hconcat_resize.jpg', img_h_resize)
cv2.imshow('vconcat_resize.jpg', img_v_resize)


cv2.waitKey(0)
cv2.destroyAllWindows()


