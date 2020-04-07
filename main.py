import cv2 #to read the image

image = cv2.imread('/home/pi/Opencv/images/bigJared.jpg')
gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Original image', image)
#cv2.imshow('Gray boi', gray)

dim = (48, 48)
resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

cv2.imwrite("original.jpg",image)
cv2.imwrite("gray.jpg", gray) 

cv2.waitKey(0)
cv2.destroyAllWindows()
