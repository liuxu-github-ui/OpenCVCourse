#Download image from github to pc : https://github.com/mcwhorpj/demoImages unzip it and put in the same directory with this python script

import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_COMPLEX
width=640 #Define fram size,line 7 will use it
height=360
#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

donFace=FR.load_image_file('demoImages\known\Donald Trump.jpg')
faceLoc=FR.face_locations(donFace) #locate face location
#print(faceLoc[0]) #grab first face (if there are mutiple faces detected)
top,right,bottom,left=faceLoc[0]
donFaceEncode=FR.face_encodings(donFace)[0]

nancyFace=FR.load_image_file(r'demoImages\known\Nancy Pelosi.jpg')
#faceLoc=FR.face_locations(nancyFace) #locate face location
nancyFaceEncode=FR.face_encodings(nancyFace)[0]

knownEncodings=[donFaceEncode,nancyFaceEncode] #trained face data for later use compare unknown face with these trained data
names=['Donald Trump','Nancy Pelosi']

while True:
    ignore,unknownFace = cam.read() #grab the image
    unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR) #Camera read as RGB but face regonition needs BGR
    faceLocations=FR.face_locations(unknownFaceBGR) #find all the face locations in the photo
    unknownEncodings=FR.face_encodings(unknownFaceBGR,faceLocations) #encode the unknown faces

    #it will go through the face in u3.jpg one by one. Check if the face is 'Donald Trump','Nancy Pelosi'
    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings): #go throught all the faces in picture 3 
        top,right,bottom,left=faceLocation #locate face location
        print(faceLocation) 
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),3)#put a rectangle on the face base on the faceLoc. Blue Box 
        name='Unknown Person'
        matches=FR.compare_faces(knownEncodings,unknownEncoding) #check wether knownencoding/unknownencoding match
        print(matches) 

        if True in matches:
            matchIndex=matches.index(True) #if there is true (found), print the index of the face (multiple faces in the pic)
            print(matchIndex)
            name=names[matchIndex]
        cv2.putText(unknownFace,name,(left,top),font,.75,(0,0,255),3) #add text to the image
    cv2.imshow('My Faces',unknownFace)
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop

cam.release()
cv2.destroyAllWindows()



while True:
    ignore,frame = cam.read() #grab the image
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    cv2.imshow('myWebCamImg',grayFrame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop





