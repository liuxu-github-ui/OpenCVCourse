import cv2
import numpy as np

while True:
    frame=np.zeros([250,250,3],dtype=np.uint8) # all pixels to 0 (black color) 250 row and column and each intersection has 3 numbers R,G,B
    #frame[:,:]=255 #all pixel to 255 white color
    #frame[:,0:125]=255 #half black and half white
    frame[:,:]=[0,0,255] #red color
    frame[:,0:125] =[0,255,0] #greeen color
    print(frame)
    cv2.imshow('My Window',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

