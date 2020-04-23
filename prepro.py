import cv2 
import time
import os

# Volledige preprocessing voor Het herkennen van gezichten. Het Preprocessen bestaat uit:
#   1. grayscalen ( Luma methode )
#   2. Gezicht vinden en de afbeelding naar het gezicht croppen
#   3. Resizen naar 64 x 64

# Paden voor afbeeldingen en results
path = "/home/pi/Opencv/Images/FACES/"
resultPath = "/home/pi/Opencv/CropResults/"

# inladen van het haarcascade_frontalface_deafult model
# https://github.com/opencv/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for file in os.listdir(path):
    # Inladen van de afbeelding
    image = cv2.imread( path + file )
    imageRGB = cv2.cvtColor( image, cv2.COLOR_BGR2RGB)
    imageCopy = imageRGB.copy()
    #omzetten naar monochroom met de luma methode
    imageGray = cv2.cvtColor( imageRGB, cv2.COLOR_RGB2GRAY )
    #detecteren face boundary box
    face = faceCascade.detectMultiScale( imageGray, 1.25, 6)
    for f in face:
        x, y, w, h = [v for v in f ]
        cv2.rectangle(imageCopy, (x,y), (x+w, y+h), (255,0,0), 3)
        #croppen van gezicht
        faceCrop = imageGray[y:y+h, x:x+w]
    #resizen naar 64 x64
    resized = cv2.resize(faceCrop, (64,64), interpolation = cv2.INTER_LINEAR)
    cv2.imwrite( resultPath + file + "result.png", resized )

