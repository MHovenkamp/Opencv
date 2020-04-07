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
resized = cv2.resize(gray, dim, interpolation = cv2.INTER_LINEAR)

#opslaan van de afbeeldingen voor evaluatie
cv2.imwrite("original.jpg",image)
cv2.imwrite("gray.jpg", resized) 

# Voor laten zien afbeeldingen, uit vo rterminal gebruik
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
#time it cost to run 1 image = 1.96884473085 

#| method of resizing | method of grayscaling | speed |
#| INTER_AREA | COLOR_BGR2GRAY | 1.96884473085 |
#| INTER_LINEAR | COLOR_BGR2GRAY | 


#f187ff244ecfc9e264b67ae04aca4498fe608f6b van gray image 
elapsed_time = timeit.timeit(codeToTest, number=100)/100
print(elapsed_time)
