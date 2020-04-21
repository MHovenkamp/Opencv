import cv2 
import time
import os

path = "/home/pi/Opencv/Images/FACES/"
face_cascade = cv2.CascadeClassifier("home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
for file in os.listdir(path):
    image = cv2.imread( path + file )
    imageRGB = cv2.cvtColor( image, cv2.COLOR_BGR2RGB)
    imageCopy = imageRGB.copy()
    imageGray = cv2.cvtColor( imageRGB, cv2.COLOR_RGB2GRAY )
    print( file )
    cv2.imwrite( file + ".png", imageGray )
    face = face_cascade.detectMultiScale( imageGray, 1.25, 6)

    #x, y, w, h = [v for v in face ]
    #cv2.rectangle(imageCopy, (x,y), (x+w, y+h), (255,0,0), 3)
    #faceCrop = gray_image[y:y+h, x:x+w]

cv2.imwrite( "result.png", faceCrop )
 