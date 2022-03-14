#Region Of Interest(ROI): Instead of grab the whole frame for analysis, we just grab portion of it for quick analysis and save computational resource
                        
import cv2
width=640 #Define fram size,line 7 will use it
height=360

#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,frame = cam.read() #grab the frame
    frameROI = frame[150:210,250:390] #only interest in row between 150 and 210 and column between 250 and 390
    frameROIGray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY) #Create gray frame
    frameROIBGR = cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR) #Create color frame
    cv2.imshow('my ROI',frameROI)
    cv2.moveWindow('my ROI',650,90)
    cv2.imshow('my Gray ROI',frameROIGray)
    cv2.moveWindow('my Gray ROI',650,0)
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    cv2.imshow('myWebCamImg',grayFrame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()






