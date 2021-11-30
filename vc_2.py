import cv2

import time

cap=cv2.VideoCapture("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/finger_move.mp4")

fps=25

if cap.isOpened()==False:
    print("error opening the video file")

while cap.isOpened():
    ret,frame=cap.read()

    if ret==True:
        time.sleep(1/fps)
        # we are displaying at a delay of 1/25 
        cv2.imshow("frame",frame)

        if cv2.waitKey(25) & 0xFF==ord("q"):
            break
    else:
        break 

cap.release()
cv2.destroyAllWindows()