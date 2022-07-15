## HANDTRACKING
| ![Alt Text](https://github.com/facumruiz/HandTracking/blob/main/docs/hand_tracking_3d_android_gpu.gif)   | ![Image Text](https://github.com/facumruiz/HandTracking/blob/main/docs/hand_landmarks.png) |
| ------------- | ------------- |
| ![Image Text](https://github.com/facumruiz/HandTracking/blob/main/docs/land_marks_results.PNG)  |  import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

mpH = mp.solutions.hands
hands = mpH.Hands()


while (capture.isOpened()):
    ret, frame = capture.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)




    cv2.imshow('webCam',frame)

    if (cv2.waitKey(1) == ord('s')):
        break







capture.release()
cv2.destroyAllWindows() |
