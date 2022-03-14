import cv2

evt=0
def mouseClick(event,xPos,yPos,flags,params): #create function for later use #17
    global evt    
    global pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Mouse Event was: ",event)
        print("At position, ",xPos,yPos)
        pnt=(xPos,yPos)
        evt=event #make it global becuase we need to use it later
    if event==cv2.EVENT_LBUTTONUP:
        print("Mouse Event was: ",event)
        print("At position, ",xPos,yPos)
        evt=event #make it global becuase we need to use it later
    if event==cv2.EVENT_RBUTTONUP:
        print('Right Button up: ',event)
        pnt=(xPos,yPos)
        evt=event

width=640 #Define fram size,line 7 will use it
height=360

#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('myWebCamImg')
cv2.setMouseCallback('myWebCamImg',mouseClick) # listen to the main windows('myWebCamImg') for mouse click and when click, call mouseclick function
while True:
    ignore,frame = cam.read() #grab the image
    if evt==1 or evt==4: #if press left button or release left button
        cv2.circle(frame,pnt,25,(255,0,0),2) #if there is a click, put a circle. 25 pixel, blue clor, thickness 2

    #grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    cv2.imshow('myWebCamImg',frame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()




