import cv2
import mediapipe as mp

width=640 #Define fram size,line 7 will use it
height=360
hands=mp.solutions.hands.Hands(False,2,.5,.5) #confidence level 0.5 and detect 2 hands
mpDraw=mp.solutions.drawing_utils
def parseLandmarks(frame):
    myHands=[]
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB) #pass frame to hands for processing
    if results.multi_hand_landmarks != None: #means found a hand
        for handLandMarks in results.multi_hand_landmarks: #go through each hand
            myHand=[]
            for landMark in handLandMarks.landmark:
                myHand.append((int(landMark.x*width),int(landMark.y*height)))
            myHands.append(myHand)
    return myHands

#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,frame = cam.read() #grab the image
    #grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    frame=cv2.resize(frame,(width,height))
    myHands=parseLandmarks(frame)
    for hand in myHands:
        cv2.circle(frame,hand[20],25,(0,255,0),3) #put a circle on tip of pinkie
    cv2.imshow('myWebCamImg',frame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()




