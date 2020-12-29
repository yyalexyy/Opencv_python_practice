import cv2
import numpy as np
"""
Chapter 4 -
Draw Shapes and put text on Image
"""
img = np.zeros((512,512,3), np.uint8)    # create a matrix of 0s(black). Size 512x512
# print(img.shape)

"""
Coloring the image
"""
# img[:] = 255, 0, 0                    # Color the whole image blue
# img[100:200, 50:200] = 255, 0, 0      # Color the image btw height(100-200), width(50-200) blue

"""
Creating a line on an image
"""
# cv2.line(img, (0,0), (300, 300), (0,255,0), 3)                      # (img, starting point, ending point, color, thickness)
# cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 3)      # (img, starting point, ending point(width, height) color, thickness)

"""
Creating a rectangle on an image
"""
# cv2.rectangle(img, (0,0), (250, 350), (0,0,255))                #(img, starting point, ending point, color)
# cv2.rectangle(img, (0,0), (250, 350), (0,0,255), cv2.FILLED)    #(img, starting point, ending point, color, fill the rec)

"""
Creating a circle on an image
"""
# cv2.circle(img, (400,50), 30, (255,255,0), 2)   #(img, center point, radius, color, thickness)
# cv2.circle(img, (400,50), 30, (255,255,0), -1)   #(img, center point, radius, color, -1 to fill the circle)

"""
Adding text to an image
"""
# cv2.putText(img, "OPENCV", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255,255,255), 1)  #(img, wat text to show (string), origin, text_font, scale, color, thickness


"""
Practice
"""
cv2.rectangle(img, (128, 128), (384,384), (255,255,0))
cv2.circle(img, (256,256), 128, (0,255,0), 1)
cv2.line(img, (128,128), (256,256), (0,0,255), 1)
cv2.line(img, (384,128), (256,256), (0,0,255), 1)
cv2.putText(img, "Shapes", (200,300), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)

cv2.circle(img, (50,50), 30, (255,255,255), -1)
cv2.circle(img, (462,50), 30, (255,255,255), -1)
cv2.circle(img, (50,462), 30, (255,255,255), -1)
cv2.circle(img, (462,462), 30, (255,255,255), -1)
cv2.rectangle(img, (20,50), (80, 462), (255,255,255), cv2.FILLED)
cv2.rectangle(img, (432,50), (492, 462), (255,255,255), cv2.FILLED)

cv2.imshow("Image", img)

cv2.waitKey(0)