import cv2
import imutils

image = cv2.imread('te.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('im', gray)
edged = cv2.Canny(gray, 100, 200)
cv2.imshow('edged', edged)

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('thresh', thresh)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
print('11:', cnts)
cnts = imutils.grab_contours(cnts)
print('aaa',cnts)
print('detection:', len(cnts), 'objects')
output = image.copy()
for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow('Counters', output)
    cv2.waitKey
cv2.imshow('thress', thresh)
cv2.imshow('gray', edged)
# cv2.waitKey(0)

mask1 = thresh.copy()
mask1 = cv2.erode(mask1, None, iterations=5)
cv2.imshow('Eroded', mask1)

mask2 = thresh.copy()
mask2 = cv2.dilate(mask2, None, iterations=5)
cv2.imshow('Dilated', mask2)


mask3 = thresh.copy()
output1 = cv2.bitwise_and(image, image, mask=mask3)
cv2.imshow('output', output1)
cv2.waitKey(0)