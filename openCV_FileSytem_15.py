import os
import cv2
import face_recognition as FR
print(cv2.__version__)
imageDir=r'C:\\Users\xuliu102\OneDrive - Advanced Micro Devices Inc\Unity_coursera\AIForEveryone\demoImages\known'
for root,dirs,files in os.walk(imageDir): #root is knowns and dirs will be empty array since no folders and knowns,, files will the images
    #print('my Working Folder (root): ',root)
    #print('dirs in root: ',dirs)
    #print('files in dirs: ',files)
    for file in files:
        #print(file) #print file 
        fullFilePath=os.path.join(root,file) #concatenate the root and file into a string
        name=os.path.splitext(file)[0] #split .jpg and get name
        myPicture=FR.load_image_file(fullFilePath)
        myPicture=cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR) #OPENCV needs BGR format
        cv2.imshow(name,myPicture)
        cv2.moveWindow(name,0,0)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()
        