import cv2 #to read the image

image = cv2.imread("~/Opencv/images/jared.jpg")
gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Gray boi', gray)