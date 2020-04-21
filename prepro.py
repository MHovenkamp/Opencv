import cv2 
import time
import os

path = "/home/pi/Opencv/Images/FACES/"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
for file in os.listdir(path):
    image = cv2.imread( path + file )
    imageRGB = cv2.cvtColor( image, cv2.COLOR_BGR2RGB)
    imageCopy = imageRGB.copy()
    imageGray = cv2.cvtColor( imageRGB, cv2.COLOR_RGB2GRAY )
    print( file )
    cv2.imwrite( file + ".png", imageGray )
    face = face_cascade.detectMultiScale( imageGray, 1.25, 6)
    for f in face:
        x, y, w, h = [v for v in f ]
        cv2.rectangle(imageCopy, (x,y), (x+w, y+h), (255,0,0), 3)
        faceCrop = imageGray[y:y+h, x:x+w]
    resized = cv2.resize(faceCrop, dim, interpolation = INTER_LINEAR)
    cv2.imwrite( file + "result.png", faceCrop )

