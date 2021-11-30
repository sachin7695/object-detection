import cv2

video_capt=cv2.VideoCapture(0)

width=int(video_capt.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(video_capt.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer=cv2.VideoWriter("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/practice code/myvideo/mysupervideo.mp4",cv2.VideoWriter_fourcc(*"XVID"),25,(width,height))
while True:
    ret,frame=video_capt.read()

    # gray1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    writer.write(gray)
    cv2.imshow("frame",gray)
    # print(ret)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capt.release()
writer.release()
cv2.destroyAllWindows()