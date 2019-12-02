# MARK:- Libs
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# MARK:- grayscale SE

ellipse_kernel = cv.getStructuringElement(
    cv.MORPH_ELLIPSE, ksize=(3, 3))

img = cv.imread('input.jpg', 0) 
  
# Taking a matrix of size 5 as the kernel 
kernel = np.ones((5,5), np.uint8) 
kernel *= 10 
# The first parameter is the original image, 
# kernel is the matrix with which image is  
# convolved and third parameter is the number  
# of iterations, which will determine how much  
# you want to erode/dilate a given image.  

img_erosion = cv.erode(img, kernel, iterations=1)
img_open = cv.morphologyEx(img, cv.MORPH_OPEN, kernel, iterations=1)
img_close = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel, iterations=1)
img_dilation = cv.dilate(img, kernel, iterations=1)
  
cv.imshow('Input', img) 
cv.imshow('Erosion', img_erosion) 
cv.imshow('Dilation', img_dilation)
cv.imshow('Open', img_open)
cv.imshow('Close', img_close)   
  
cv.waitKey(0) 
cv.destroyAllWindows()