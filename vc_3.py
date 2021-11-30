import cv2
import numpy as np
# cap = cv2.VideoCapture(0)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# x=width//2
# y=height//2
# w=width//4
# h=height//4
# # these two // allows to return integer
# while True:
#     ret,frame=cap.read()
#     cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=-1)

#     cv2.imshow("frame",frame)
#     if cv2.waitKey(1) & 0xFF ==ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()

# call back function rectangle
def draw_rectangle(event,x,y,flags,param):
    global pt1,pt2,topleft_clicked,botright_clicked

    if event ==cv2.EVENT_LBUTTONDOWN:
        if topleft_clicked == True and botright_clicked ==True:
            topleft_clicked=False
            botright_clicked=False
            pt1=(0,0)
            pt2=(0,0)
        if topleft_clicked ==False:
            pt1=(x,y)
            topleft_clicked=True
        elif botright_clicked == False:
            pt2 = (x,y)
            botright_clicked = True


# global variables
pt1=(0,0)
pt2=(0,0)
topleft_clicked=False
botright_clicked=False

# connect to the callback
cap=cv2.VideoCapture(0)
cv2.namedWindow("Test")
cv2.setMouseCallback("Test",draw_rectangle)

while True:
    ret,frame=cap.read()
    if topleft_clicked:
        cv2.circle(frame, center=pt1, radius=3, color=(0,0,255), thickness=-1)

    if topleft_clicked and botright_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),thickness=-1)

    cv2.imshow("Test",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()