import cv2
import numpy as np
from setuptools import SetuptoolsDeprecationWarning

def onTrack1(val):
    global hueLow
    hueLow=val
    print('Hue Low',hueLow)

def onTrack2(val):
    global hueHigh
    hueHigh=val
    print('Hue High',hueHigh)

def onTrack3(val):
    global satLow
    satLow=val
    print('sat Low',satLow)

def onTrack4(val):
    global satHigh
    satHigh=val
    print('sat High',satHigh)

def onTrack5(val):
    global valLow
    valLow=val
    print('val Low',valLow)

def onTrack6(val):
    global valHigh
    valHigh=val
    print('val High',valHigh)


width=640 #Define fram size,line 7 will use it
height=360

#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('myTracker') #create a window called myTracker
cv2.moveWindow('myTracker', width,0) #move to a new position

hueLow=10
hueHigh=20
satLow=10
setHigh=50
valLow=10
valHigh=30

cv2.createTrackbar('Hue Low','myTracker',10,179,onTrack1) #create a trackbar, Intital Low value to be 10, Hue value is 0-179 so max is 179
cv2.createTrackbar('Hue High','myTracker',20,179,onTrack2)
cv2.createTrackbar('Sat Low','myTracker',10,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',50,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',10,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',30,255,onTrack6)

while True:
    ignore,frame = cam.read() #grab the image
    #grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #CONVERT FRAME TO HSV format
    lowerBound=np.array([hueLow,satLow,valLow])  #define 2 arrays and check whether the frame falls within these areas
    upperBound=np.array([hueHigh,satHigh,valHigh])
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound) #create a mask and look at the frameHSV and keep the pixcels within the lpwer and upper bound range
    myObject=cv2.bitwise_and(frame,frame,mask=myMask) #Compare frame and mask. if the mask is 1 keep the frame if not ignore
    myObjectSmall=cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow('My Object',myObjectSmall)
    cv2.moveWindow('My Object',int(width/2),int(height/2))
    #cv2.imshow('My Object',myObject)
    #cv2.imshow('My Mask',myMask)
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    cv2.imshow('My Mask',myMaskSmall)
    cv2.moveWindow('My Mask',0,height)
    cv2.imshow('myWebCamImg',frame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()




