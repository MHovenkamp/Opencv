import cv2 #to read the image
import timeit

codeToTest = """
import cv2

image = cv2.imread('/home/pi/Opencv/images/bigJared.jpg')
gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)

#laten zien van de images, staat uit voor terminal gebruik
#cv2.imshow('Original image', image)
#cv2.imshow('Gray boi', gray)

dim = (48, 48)
resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

#opslaan van de afbeeldingen voor evaluatie
cv2.imwrite("original.jpg",image)
cv2.imwrite("gray.jpg", resized) 

# Voor laten zien afbeeldingen, uit vo rterminal gebruik
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
elapsed_time = timeit.timeit(codeToTest, number=100)/100
print(elapsed_time)
