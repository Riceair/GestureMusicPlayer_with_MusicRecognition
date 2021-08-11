import cv2
import mediapipe as mp
import numpy as np
import time
import HandTrackingModule as htm
from GestureRecognizer import GestureRecognizer

cap = cv2.VideoCapture(0)
detector = htm.handDetector()
gRecognizer = GestureRecognizer()
PLAY_PAUSE = 0
NEXT = 1
PREV = 2
STYLE_CHANGE = 3

go = 1
###由於辨識會出現辨識錯誤的情形，因此需要連續出現一定的次數才判定為正確手勢
current_gesture = 0 #紀錄當前的手勢
gesture_appear_times = 0 #紀錄當前手勢出現的次數
TRUE_APPEAR_TIMES = 20 #連續出現n個frame判為正確

while go:
    success, img = cap.read()
    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        gesture = gRecognizer.getGestureType(lmList)
        if gesture is not None:
            if current_gesture != gesture: #若發現為不同手勢重新計次
                current_gesture = gesture
                gesture_appear_times = 1
            elif current_gesture == gesture: #發現為相同手勢計次
                gesture_appear_times += 1
            
            if gesture_appear_times==TRUE_APPEAR_TIMES: #到達累計次數
                if current_gesture==PLAY_PAUSE:
                    print("Pause")
                elif current_gesture==NEXT:
                    print("Next")
                elif current_gesture==PREV:
                    print("Prev")
                elif current_gesture==STYLE_CHANGE:
                    print("Style Change")
                gesture_appear_times = 0
                time.sleep(5)
            #time.sleep(2)


    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    #若按下esc鍵則離開
    if key & 0xFF == 27:
        print("exit")
        go=0   

#釋放攝影機qqq
cap.release()

#關閉視窗
cv2.destroyAllWindows()