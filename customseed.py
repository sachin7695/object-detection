import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
road=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/road_image.jpg")
road_copy=road.copy()
marker_image=np.zeros(road.shape[:2],dtype=np.int32)
# plt.imshow(marker_image,cmap='gray')
segments=np.zeros(road.shape,dtype=np.int32)

# ccreate color for markers
def create_rgb(i):
    x=np.array(cm.tab10(i)[:3])
    return tuple(x)

colors=[]
for i in range(10):
    colors.append(create_rgb(i))

n_markers=10
current_marker=1
marks_update=False

# mouse callback for onclick events
def mouse_callback(event,x,y,flags,param):
    global marks_update
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image,(x,y),10,(current_marker),-1)
        cv2.circle(road_copy,(x,y),10,colors[current_marker],-1)
        marks_update=True

cv2.namedWindow("Road Image")
cv2.setMouseCallback("Road Image",mouse_callback)

while True:
    cv2.imshow("watershed segments",segments)
    cv2.imshow("Road Image",road_copy)
    # plt.show()

    k=cv2.waitKey(1)
    if k==27:
        break
    elif k==ord('c'):
        road_copy=road.copy
        marker_image=np.zeros(road.shape[:2],dtype=np.int32)
        segments=np.zeros(road.shape,dtype=np.int32)

        # if a number choose number between 0-9 index the color
    elif k>0 and chr(k).isdigit():
        current_marker=int(chr(k))
    if marks_update:
        marker_image_copy=marker_image.copy()
        cv2.watershed(road,marker_image_copy)
        segments=np.zeros(road.shape,dtype=np.int32)
        for color_ind in range(n_markers):
            segments[marker_image_copy==(color_ind)]=colors[color_ind]
        marks_update=False

cv2.destroyAllWindows()