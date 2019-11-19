# MARK:- Libs
import cv2 as cv
import numpy as np

# MARK:- read image
img = cv.imread('j.png')

# MARK:- show image
cv.imshow('j.png', img)
cv.waitKey(0)
cv.destroyAllWindows()