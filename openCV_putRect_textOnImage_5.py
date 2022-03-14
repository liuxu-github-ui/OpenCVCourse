import cv2
import time
width=640 #Define fram size,line 7 will use it
height=360
myText="frame Text"

#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
tLast=time.time()
time.sleep(0.1) # #13 and #16 too close results into dT becomes 0. To prevent that delay 0.1 seconds
while True:
    dT=time.time()-tLast   
    #print(dT) #check how fast it generate 1 frame
    fps=1/dT #Check frame per second
    tLast=time.time()
    ignore,frame = cam.read() #grab the image
    #frame[140:220,280:360] = (0,0,255)    #create box in the middle of the frame refer to #2,3 defined width,height as a referene
    cv2.rectangle(frame,(250,140),(390,220),(0,225,0),2) #points axis location (250,140) and (390,220) and color i (0,225,0) thickness is 2
    cv2.putText(frame,myText,(120,60),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2) #locaiton(120,60), fontsize2 and color blue
    cv2.putText(frame,str(fps),(0,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1) #put fps value on (0,30) location and blue color
    cv2.imshow('myWebCamImg',frame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()




