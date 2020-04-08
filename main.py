import cv2 #to read the image
import timeit

import cv2

path = '/home/pi/Opencv/images/
name = input()
codeToTest = """
image = cv2.imread(path + name)
gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)


#laten zien van de images, staat uit voor terminal gebruik
#cv2.imshow('Original image', image)
#cv2.imshow('Gray boi', gray)

dim = (48, 48)
resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
#resized = cv2.resize(gray, dim, interpolation = cv2.INTER_LINEAR)
#resized = cv2.resize(gray, dim, interpolation = cv2.INTER_CUBIC)
#resized = cv2.resize(gray, dim, interpolation = cv2.INTER_LANCZOS4)
#resized = cv2.resize(gray, dim, interpolation = cv2.INTER_NEAREST)

#opslaan van de afbeeldingen voor evaluatie
cv2.imwrite("original.jpg",image)
cv2.imwrite("gray.jpg", resized) 

# Voor laten zien afbeeldingen, uit vo rterminal gebruik
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
#time it cost to run 1 image = 1.96884473085 

# Dit zijn de testen op 1 afbeelding aangezien ik nog geen database heb
# Volgorde grayscalling -> Resizing
#| method of resizing | method of grayscaling | speed | shasum |
#| INTER_AREA | COLOR_BGR2GRAY | +-1.96884473085 | #f187ff244ecfc9e264b67ae04aca4498fe608f6b |
#| INTER_LINEAR | COLOR_BGR2GRAY | +-1.6719028306 | 3cbf05488ee00e09193cf213c9db1c8ff3f9dd05 |
#| INTER_CUBIC | COLOR_BGR2GRAY | +-1.63356585026 | 8cc27a0f5c6bb12fca6dbcd73c742d706f8be9e0 |
#| INTER_LANCZOS4 | COLOR_BGR2GRAY | +- 1.62078979969 | 24ebc32e9d596af09c3043905858c09717157406 | 
#| INTER_NEAREST | COLOR_BGR2GRAY | +-



elapsed_time = timeit.timeit(codeToTest, number=10)/10
print(elapsed_time)
