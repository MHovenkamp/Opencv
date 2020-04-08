import cv2 #to read the image
import time
import os

import cv2

resultsList = []

paths = [   "/home/pi/Opencv/Results/Area/", 
            "/home/pi/Opencv/Results/Cubic/", 
            "/home/pi/Opencv/Results/Lanczos4/", 
            "/home/pi/Opencv/Results/Linear/", 
            "/home/pi/Opencv/Results/nearest/"]
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
for i in range(len(methods)):
    results = open(resultFiles[i], "a")
    path = "/home/pi/Opencv/Images/"
    pathResults = paths[i]

    for file in os.listdir(path):
        image = cv2.imread(path + file)
        tStart = time.time()
        gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)


        #laten zien van de images, staat uit voor terminal gebruik
        #cv2.imshow('Original image', image)
        #cv2.imshow('Gray boi', gray)

        dim = (48, 48)
        resized = cv2.resize(gray, dim, interpolation = methods[i])

        #opslaan van de afbeeldingen voor evaluatie
        grayName = pathResults + file + "Gray.jpg"
        resizedName = pathResults + file + "Gray_resized.jpg"

        cv2.imwrite(grayName,image)
        cv2.imwrite(resizedName, resized) 

        # Voor laten zien afbeeldingen, uit vo rterminal gebruik
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        tEnd = time.time()

        elapsedTime =  tEnd-tStart
        resultsList.append(elapsedTime)
        print(elapsedTime)

        results.write( file + ': ' + str(elapsedTime) + '\n' )

    average = sum(resultsList) / len(resultsList)
    results.write("Average: " + str(average))
