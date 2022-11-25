import imutils
import cv2
import numpy as np

image = cv2.imread('py3.jpg')
# cv2.imshow('image',image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
# cv2.imshow('gaussian', gray)
edged = cv2.Canny(gray, 20, 100)
# cv2.imshow('edged', edged)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

if len(cnts)>0:
    c = max(cnts, key=cv2.contourArea)
    mask = np.zeros(gray.shape, dtype='uint8')
    cv2.drawContours(mask, [c], -1, 255, -1)
    

    (x, y, w, h) = cv2.boundingRect(c)
    imageROI = image[y:y+h, x:x+w]
    maskROI = mask[y:y+h, x:x+w]
    imageROI = cv2.bitwise_and(imageROI, imageROI, maskROI)
    # cv2.imshow('11mask', imageROI)
for angle in np.arange(0, 360, 15):
    rotate = imutils.rotate_bound(imageROI, angle)
    cv2.imshow('rotated', rotate)
    cv2.waitKey(300)    
cv2.waitKey(0)