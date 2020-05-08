import zlib

path = "/home/pi/Opencv/CompressResults/ZLIB"

for file in os.listdir(imagePath):
    print( file )
    str_object1 = open(path+file, 'rb').read()
    str_object2 = zlib.decompress(str_object1)
    f = open(file+"uncompressed.png", 'wb')
    f.write(str_object2)
    f.close()