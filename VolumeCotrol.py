import cv2
import time
import math
import numpy as np
import HandTrackingProject.HandTrackingModule as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480

capture = cv2.VideoCapture(0)
capture.set(3, wCam)
capture.set(4, hCam)
pTime = 0
fps = 0

detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = capture.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2) // 2, (y1+y2) // 2

        cv2.circle(img, (x1,y1), 15, (0,255,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 15, (0,255,255), cv2.FILLED)
        cv2.line(img, (x1,y1),(x2,y2), (0,255,255), 2)
        cv2.circle(img, (cx,cy), 15, (0,255,255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)


        # Hand Range 70 - 390
        # Volume Range -96 to 0

        vol = np.interp(length, [70,320], [minVol, maxVol])
        volBar = np.interp(length, [70, 320], [400, 150])
        volPer = np.interp(length, [70, 320], [0, 100])
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length<70:
            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (0,255,0), 2)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'FPS: {int(fps)}', (20, 35), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'{int(volPer)} %', (20,450), cv2.FONT_HERSHEY_COMPLEX,
                1, (0,255,0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)