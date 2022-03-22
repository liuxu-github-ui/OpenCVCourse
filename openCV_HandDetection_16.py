import cv2
import mediapipe as mp
width=640 #Define fram size,line 7 will use it
height=360

#lanuch webcam
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #tell python which camera to use
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) #LINE 7-10 for faster launch of cam and smooth capture, no lagging
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

hands=mp.solutions.hands.Hands(False,2,.5,.5) #Look at the frame and find the hands. False means not static image and 2 means max hands are 2
mpDraw=mp.solutions.drawing_utils #draw data on the hands
while True:
    myHands=[]
    ignore,frame = cam.read() #grab the image
    #grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #create a grey frame
    frame=cv2.resize(frame,(width,height))
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #cv2 use RGB format 
    results=hands.process(frameRGB)
    if results.multi_hand_landmarks != None: #if there are hands
        for handLandMarks in results.multi_hand_landmarks: #maybe multiple hands
            myHand=[]
            #mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS) #draw the marks on hand
            for Landmark in handLandMarks.landmark: #check invidiaul landmarks (total 21 landmarks)
               # print((Landmark.x,Landmark.y))
                myHand.append((int(Landmark.x*width),int(Landmark.y*height))) #append all the hand landmarks info into an tuple
            #print('')
            #print(myHand)
            cv2.circle(frame,myHand[20],25,(255,0,255),-1) #put a circle on my pinkie, 25 radius, purple color, thickness -1
            


    cv2.imshow('myWebCamImg',frame) #assign the frame a name
    cv2.moveWindow('myWebCamImg',0,0) # move webcam to a specify location 
    if cv2.waitKey(1) & 0xff == ord('q'):  #wait for 1 second to see whether anyone press the key. If yes and press "q"
        break #break the while loop
cam.release()






