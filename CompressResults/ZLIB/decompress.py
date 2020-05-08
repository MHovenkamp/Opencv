import zlib
import os

imagePath = "/home/pi/Opencv/CompressResults/ZLIB/"
pathUncom = "/home/pi/Opencv/CompressResults/ZLIB/Results/"
for file in os.listdir(imagePath):
    print( file )
    str_object1 = open(imagePath+file, 'rb').read()
    str_object2 = zlib.decompress(str_object1)
    f = open(pathUncom + file+"uncompressed.png", 'wb')
    f.write(str_object2)
