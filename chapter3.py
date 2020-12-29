import cv2
import numpy as np

"""
Chapter 3 - 
Resizing and cropping an image
"""
img = cv2.imread("Resources/gal.png")
print(img.shape)

imgResize = cv2.resize(img, (500, 750))     # (width,height)
print(imgResize.shape)

imgCropped = img[100:800, 300:800]    # [height, width]


cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)