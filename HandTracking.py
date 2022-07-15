import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

mpH = mp.solutions.hands
hands = mpH.Hands()
mpD = mp.solutions.drawing_utils

while (capture.isOpened()):
    ret, frame = capture.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpD.draw_landmarks(frame, handLms)



    cv2.imshow('webCam',frame)

    if (cv2.waitKey(1) == ord('s')):
        break


capture.release()
cv2.destroyAllWindows()