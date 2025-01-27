import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math
import VolumeControl



wCam,hCam=1200,720

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

detector= htm.handDetector(detectionCon=0.4)
volRange=VolumeControl.GetVolumeRange()
minVol=volRange[0]
maxVol=volRange[1]









while True:
    success,img= cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList)!=0:
        # print(f"thumb {lmList[4]}   index finger {lmList[8]}")
        # time.sleep(300)
        x1,y1=lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx,cy = (x1+x2)//2,(y1+y2)//2
        # cv2.circle(img,(x1,y1),15,(255,255,255),cv2.FILLED)
        # cv2.circle(img, (x2, y2), 15, (255, 255, 255), cv2.FILLED)
        # cv2.line(img,(x1,y1),(x2,y2),(255,0,0),10)
        # cv2.circle(img, (cx,cy),3,(255,255,0),5,cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        # print(length)


        ####### hand range : 50-300 #######
        ####### volume range : 0-100  #######
        vol=np.interp(length,[50,300],[0,100])
        # print(f"volume is {vol}")
        VolumeControl.SetMasterVolume(vol)

        if length<50:
            cv2.circle(img, (cx, cy), 3, (0, 255, 255), 5, cv2.FILLED)





    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,f"fps {int(fps)}",(40,70),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),5)
    # cv2.imshow("img",img)  # uncomment if u wanna see urself !
    cv2.waitKey(1)

