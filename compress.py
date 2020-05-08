import time
import os
import cv2
import gzip

imagePath = "/home/pi/Opencv/CropResults/"
resultPath = "/home/pi/Opencv/CompressResults/"

for file in os.listdir(imagePath):
    print( file )
    image = cv2.imread( imagePath + file )
    binaryImage = cv2.imencode('.png', image)[1].tostring()
    with gzip.open( resultPath+file+".gz" , "wb" ) as result:
        result.write(binaryImage)


#unzip with:
#nparr = np.fromstring(STRING_FROM_DATABASE, np.uint8)
#img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
