import time
import os
import cv2
import gzip

imagePath = "/home/pi/Opencv/CropResults/"
resultPath = "/home/pi/Opencv/CompressResults/"

for file in os.listdir(imagePath):
    image = cv2.imread( imagePath + file )
    binaryImage = cv2.imencode( "png", image )
    with gzip.open( resultPath+file+".gz" , "wb" ) as result:
        result.write(binaryImage)


# >>> import gzip
# >>> data = b'Python - Batteries included'
# >>> with gzip.open("test.txt.gz", "wb") as f:
# 	f.write(data)