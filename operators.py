# MARK:- Libs
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# MARK: support function


def plus(img, p, Z, origin):
    """
    define an operation that apply structuring element Z with the kernel at 'origin' on pixel p of image img
    """


# resize image
def resizeImage(img):
    result = np.zeros((16, 16))
    # result[:img.shape[0], :img.shape[1]] = img

    x_offset = 2
    y_offset = 2
    result[x_offset:img.shape[0]+x_offset,
           y_offset:img.shape[1]+y_offset] = img

    return result


def getUimage():
    img = np.ones((12, 12))
    for i in range(0, 9):
        for j in range(3, 9):
            img[i][j] = 0
    img = resizeImage(img)
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
cross_kernel = cv.getStructuringElement(
    cv.MORPH_CROSS, ksize=(3, 3), anchor=(1, 1))
left_cross_kernel = cv.getStructuringElement(
    cv.MORPH_CROSS, ksize=(3, 3), anchor=(1, 0))
rect_kernel = cv.getStructuringElement(
    cv.MORPH_RECT, ksize=(3, 3), anchor=(1, 1))
print(cross_kernel)
output = erosion(img, cross_kernel)
output = dilation(output, rect_kernel)
# output = erosion(output, left_cross_kernel)
# MARK:- show image
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot("121")
ax.set_title("original")
ax.imshow(img)

ax = plt.subplot("122")
ax.set_title("erosion")
ax.imshow(output)
plt.show()
