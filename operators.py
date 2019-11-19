# MARK:- Libs
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# MARK: support function


def plus(img, p, Z, origin):
    """
    define an operation that apply structuring element Z with the kernel at 'origin' on pixel p of image img
    """


def getUimage():
    img = np.ones((12, 12))
    for i in range(0, 9):
        for j in range(3, 9):
            img[i][j] = 0

    return img

# MARK:- operators


def erosion(img, kernel):
    """
    erodes away the boundaries of foreground object
    """

    erosion = cv.morphologyEx(img, cv.MORPH_ERODE, kernel)
    return erosion

def dilation(img, kernel):
    """
    increase size of foreground object
    """

    dilation = cv.dilate(img, kernel, iterations=1)
    return dilation


# MARK:- read image
img = getUimage()
kernel = cv.getStructuringElement(cv.MORPH_CROSS, ksize=(3,3), anchor=(1,1))
print(kernel)
output = erosion(img, kernel)

# MARK:- show image
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot("121")
ax.set_title("original")
ax.imshow(img)

ax = plt.subplot("122")
ax.set_title("erosion")
ax.imshow(output)
plt.show()
