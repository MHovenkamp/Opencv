import cv2 #to read the image
import time
import os

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
resultsList = []
names = ['Area', 'Cubic', 'Lanczos4', 'Linear', 'Nearest']
paths = [   "/home/pi/Opencv/Results/Area/", 
            "/home/pi/Opencv/Results/Cubic/", 
            "/home/pi/Opencv/Results/Lanczos4/", 
            "/home/pi/Opencv/Results/Linear/", 
            "/home/pi/Opencv/Results/Nearest/"]
methods = [ cv2.INTER_AREA,
            cv2.INTER_CUBIC,
            cv2.INTER_LANCZOS4,
            cv2.INTER_LINEAR,
            cv2.INTER_NEAREST]
resultFiles = ['/home/pi/Opencv/Results/resultsArea.txt',
                '/home/pi/Opencv/Results/resultsCubic.txt',
                '/home/pi/Opencv/Results/resultsLanczos4.txt',
                '/home/pi/Opencv/Results/resultsLinear.txt',
                '/home/pi/Opencv/Results/resultsNearest.txt']
for i in range(10):
    for i in range(len(methods)):
        total = open('/home/pi/Opencv/Results/total.txt', "a")
        results = open(resultFiles[i], "a")
        path = "/home/pi/Opencv/Images/200x200/"
        pathResults = paths[i]

        for file in os.listdir(path):
            image = cv2.imread(path + file)
            tStart = time.time()
            
            print( path+file )
            image = cv2.imread( path + file )
            imageRGB = cv2.cvtColor( image, cv2.COLOR_BGR2RGB)
            imageCopy = imageRGB.copy()
            imageGray = cv2.cvtColor( imageRGB, cv2.COLOR_RGB2GRAY )
            
            face = faceCascade.detectMultiScale( imageGray, 1.25, 6)
            if (face is not None):
                for (x, y, w, h) in faces:
                    cv2.rectangle(imageCopy, (x,y), (x+w, y+h), (255,0,0), 3)
                #croppen van gezicht
                faceCrop = imageGray[y:y+h, x:x+w]
                #resizen
                dim = (64, 64)
                resized = cv2.resize(faceCrop, dim, interpolation = methods[i])
            else:
                dim = (64, 64)
                resized = cv2.resize(imageGray, dim, interpolation = methods[i])

            #opslaan van de afbeeldingen
            # resizedName = pathResults + file + "Gray_resized.png"
            # cv2.imwrite(resizedName, resized) 

            tEnd = time.time()
            elapsedTime =  tEnd-tStart
            
            resultsList.append(elapsedTime)
            print(elapsedTime)
            results.write( file + ': ' + str(elapsedTime) + '\n' )

        #berekenen en schrijven van average
        average = sum(resultsList) / len(resultsList)
        results.write("Average: " + str(average) + "\n" + "----------------------\n")
        total.write( names[i] + " " + str(average) + '\n' ) 
    total.write("----------------------\n")