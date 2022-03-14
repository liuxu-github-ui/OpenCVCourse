import cv2

#lanuch webcam
cam=cv2.VideoCapture(0) #tell python which camer to use
while True:
    ignore,frame = cam.read() #grab the image
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    cv2.imshow('myWebCamImg',grayFrame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()




