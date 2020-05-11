import time
import os
import cv2
import gzip
import zlib

imagePath = "/home/pi/Opencv/CropResults/"
resultPath = "/home/pi/Opencv/CompressResults/"
amountOfPictures = 72

startGzip = time.time()
for file in os.listdir(imagePath):
    print( file )
    image = cv2.imread( imagePath + file )
    binaryImage = cv2.imencode('.png', image)[1].tostring()
    with gzip.open( resultPath+"/GZIP/"+file+".gz" , "wb" ) as result:
        result.write(binaryImage)
endGzip = time.time()

startZlib = time.time()
for file in os.listdir(imagePath):
    print( file )
    image = cv2.imread( imagePath + file )
    binaryImage = cv2.imencode('.png', image)[1].tostring()
    compressed = zlib.compress(binaryImage, 9)
    outputfile = open(resultPath+"/ZLIB/Results/"+file+".txt", "w")
    outputfile.write(compressed)
endZlib = time.time()

startCV = time.time()
for file in os.listdir(imagePath):
    print( file )
    image = cv2.imread( imagePath + file )
    compressed = cv2.imwrite(resultPath+"/CV/"+file+'.png', image,  [cv2.IMWRITE_PNG_COMPRESSION, 9])
endCV = time.time()

results = open("/home/pi/Opencv/CompressResults/times.txt", "a")
results.write( "GZIP average: " + str((endGzip-startGzip)/amountOfPictures))
results.write( "\n ZLIB average: " + str((endZlib-startZlib)/amountOfPictures))
results.write( "\n GZIP average: " + str((endCV-startCV)/amountOfPictures))
results.close()
#unzip with:
#nparr = np.fromstring(STRING_FROM_DATABASE, np.uint8)
#img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
