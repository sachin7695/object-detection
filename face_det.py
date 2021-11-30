import numpy as np
import cv2
import matplotlib.pyplot as plt
nadia=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/Nadia_Murad.jpg",0)
denis=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/manjit.jpeg",0)
solvay=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/solvay_conference.jpg",0)

# cascade files
face_cascade=cv2.CascadeClassifier("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_frontalface_default.xml")
def adj_detect_face(img):
    face_img=img.copy()
    face_rects=face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=1)

    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
    return face_img
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read(0)
    frame=adj_detect_face(frame)
    cv2.imshow("video capture face",frame)
    c=cv2.waitKey(1)
    if c==27:
        break
cap.release()
cv2.destroyAllWindows()



# result=adj_detect_face(denis)
# plt.imshow(result,cmap="gray")
# plt.show()
