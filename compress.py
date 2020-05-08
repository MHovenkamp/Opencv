import time
import os
import gzip

imagePath = "/home/pi/Opencv/CropResults/"
resultPath = "/home/pi/Opencv/CompressResults/"

for file in os.listdir(imagePath):
    data = file
    with gzip.open( resultPath+file+".gz" , "rb" ) as result:
        result.write(data)


# >>> import gzip
# >>> data = b'Python - Batteries included'
# >>> with gzip.open("test.txt.gz", "wb") as f:
# 	f.write(data)