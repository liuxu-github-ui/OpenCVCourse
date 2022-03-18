#copy all the harrcascade.xml files under virEn/Lib/site-packages/data to newly created file called haar which is same direct location with this python script

import cv2
width=640 #Define fram size,line 7 will use it
height=360

#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade=cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')#load .xml file
while True:
    ignore,frame = cam.read() #grab the image    
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    faces=faceCascade.detectMultiScale(frameGray,1.3,5) #detect face (even multi faces)
    for face in faces:
        x,y,w,h=face  #grab the face x,y,w,h infor
        #print('x=',x,'y=',y,'width=',w,'height=',h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3) #put a rectangle. Provide 2 diagonal positions axis. put a blue box(255,0,0) and heavy of the color is 3
    print(faces)
    cv2.imshow('myWebCamImg',frame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()




