#Download image from github to pc : https://github.com/mcwhorpj/demoImages unzip it and put in the same directory with this python script

import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_COMPLEX

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

unknownFace=FR.load_image_file(r'demoImages\unknown\u1.jpg')
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR) #cv2 works on BGR instead of RGB, so needs to convert the color format
faceLocations=FR.face_locations(unknownFace) #find all the face locations in the photo
unknownEncodings=FR.face_encodings(unknownFace,faceLocations) #encode the unknown faces

#it will go through the face in u3.jpg one by one. Check if the face is 'Donald Trump','Nancy Pelosi'
for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings): #go throught all the faces in picture 3 
    top,right,bottom,left=faceLocation #locate face location
    print(faceLocation) 
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)#put a rectangle on the face base on the faceLoc. Blue Box 
    name='Unknown Person'
    matches=FR.compare_faces(knownEncodings,unknownEncoding) #check wether knownencoding/unknownencoding match
    print(matches) 

    if True in matches:
        matchIndex=matches.index(True) #if there is true (found), print the index of the face (multiple faces in the pic)
        print(matchIndex)
        name=names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),3) #add text to the image
cv2.imshow('My Faces',unknownFaceBGR)


cv2.waitKey(10000)





