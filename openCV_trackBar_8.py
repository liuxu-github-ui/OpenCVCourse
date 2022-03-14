import cv2


def myCallBack1(val):
    global xPos
    print('xPos: ',val)
    xPos=val

def myCallBack2(val):
    global yPos
    print('yPos: ',val)
    yPos=val

def myCallBack3(val):
    global myRad
    print('yPos: ',val)
    myRad=val

myRad=25
width=640 #Define fram size,line 7 will use it
height=360
xPos=int(width/2)
yPos=int(height/2)
#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,150)#windows size
cv2.moveWindow('myTrackbars',width,0) #put myTrackbars windows besides the main windows
cv2.createTrackbar('xPos','myTrackbars',xPos,1920,myCallBack1) #bar crated in 'myTrackBar' windows and scale from 0-1920 
cv2.createTrackbar('yPos','myTrackbars',yPos,1080,myCallBack2)
cv2.createTrackbar('radius','myTrackbars',myRad,int(height/2),myCallBack3)
while True:
    ignore,frame = cam.read() #grab the image
    cv2.circle(frame,(xPos,yPos),myRad,(255,0,0),2)
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    cv2.imshow('myWebCamImg',frame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()




