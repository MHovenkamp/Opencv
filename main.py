import cv2 #to read the image
import time
import os

import cv2

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
for i in range(len(methods)):
    total = open('/home/pi/Opencv/Results/total.txt', "a")
    results = open(resultFiles[i], "a")
    path = "/home/pi/Opencv/Images/FACES/"
    pathResults = paths[i]

    for file in os.listdir(path):
        image = cv2.imread(path + file)
        tStart = time.time()
        
        #grayscalling
	print( path+file )
        gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)


        #laten zien van de images, staat uit voor terminal gebruik
        #cv2.imshow('Original image', image)
        #cv2.imshow('Gray boi', gray)

        #resizen
        dim = (64, 64)
        resized = cv2.resize(gray, dim, interpolation = methods[i])

        #opslaan van de afbeeldingen
#        grayName = pathResults + file + "Gray.png"
#        resizedName = pathResults + file + "Gray_resized.png"
#        cv2.imwrite(grayName,gray)
#        cv2.imwrite(resizedName, resized) 

        # Voor laten zien afbeeldingen, uit vo rterminal gebruik
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

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
