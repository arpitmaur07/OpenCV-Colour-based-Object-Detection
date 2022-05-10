# --------------object tracking with it's colors on live camera----------------
import cv2
import numpy as np

def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow('tracking')
cv2.createTrackbar('lowerHue','tracking',0,255,nothing)
cv2.createTrackbar('lowerSeturation','tracking',0,255,nothing)
cv2.createTrackbar('lowerValue','tracking',0,255,nothing)
cv2.createTrackbar('upperHue','tracking',255,255,nothing)
cv2.createTrackbar('upperSeturation','tracking',255,255,nothing)
cv2.createTrackbar('upperValue','tracking',255,255,nothing)

while(1):
    # img=cv2.imread('smarties.png')
    ret,frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    LH=cv2.getTrackbarPos('lowerHue','tracking')
    LS=cv2.getTrackbarPos('lowerSeturation','tracking')
    LV=cv2.getTrackbarPos('lowerValue','tracking')

    UH=cv2.getTrackbarPos('upperHue','tracking')
    US=cv2.getTrackbarPos('upperSeturation','tracking')
    UV=cv2.getTrackbarPos('upperValue','tracking')

    lowerBound=np.array([LH,LS,LV]) #for blue color=[110,50,50]    # lower_red = np.array([0,50,50])
    upperBound=np.array([UH,US,UV]) #for blue color=[130,255,255]  # upper_red = np.array([10,255,255]) 
    

    
    mask=cv2.inRange(hsv,lowerBound,upperBound)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    
    # cv2.imshow('image',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
cap.release()    
cv2.destroyAllWindows()