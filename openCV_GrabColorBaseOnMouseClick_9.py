from pyexpat.errors import XML_ERROR_INVALID_TOKEN
import cv2
import numpy as np

evt= 0#Assign some inital value (If dont assign it,when entering the functino mouseClick first time it wil run into error)
xVal=0
yVal=0

def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global xVal
    global yVal
    if event==cv2.EVENT_LBUTTONDOWN: #If left button down, grab the color underneath the x,y cursor position
        print(event)
        xVal=xPos
        yVal=yPos
        evt=event
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
        print(event)




width=640 #Define fram size,line 7 will use it
height=360

#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam') #create a window called 'my WEBcam'
cv2.setMouseCallback('my WEBcam',mouseClick) #lisen to mouseclick on 'my WEBcam' window and execute mouseClick function
while True:
    ignore,frame = cam.read() #grab the image
    #grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    if evt==1: #if left button been clicked, evt is global initiated #9
        x=np.zeros([250,250,3],dtype=np.uint8) #create 250 rows/columns and at the intersection has 3 numbers R,G,B
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #convert to HSV format
        clr=y[yVal][xVal] #get the mouse click location (row -> Y, colum -> X)
        print(clr)
        x[:,:]=clr #all rows/columns. The new window color should be the same as the mouse click area in the main window
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1) #put text at positon (0,50) and color is 0,0,0 black
        cv2.imshow('Color Picker',x) #show the window named as 'Color Picker'
        cv2.moveWindow('Color Picker',width,0) #move the window to new location
        evt=0 #just print color once 

    cv2.imshow('my WEBcam',frame) #assign the frame a name
    cv2.moveWindow('my WEBcam',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()




