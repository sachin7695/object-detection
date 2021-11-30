import numpy as np
import cv2
import matplotlib.pyplot as plt

def display(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap=cmap)
    plt.show()

sep_coins=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/pennies.jpg")
# # median blur
# sep_blur=cv2.medianBlur(sep_coins,ksize=25)
# gray_sep_coins=cv2.cvtColor(sep_blur,cv2.COLOR_BGR2GRAY)
# # display(gray_sep_coins,cmap='gray')
# ret,sep_thresh=cv2.threshold(gray_sep_coins,160,255,cv2.THRESH_BINARY_INV)
# contours,hierarchy=cv2.findContours(sep_thresh.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

# for i in range(len(contours)):
#     if hierarchy[0][i][3]==-1:
#         cv2.drawContours(sep_coins,contours,i,(255,0,0),10)
# READ IMAGE
img=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/pennies.jpg")
# APPLY BLUR
img=cv2.medianBlur(img,35)
# convert to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# APPLY THRESHOLD(INVERSE BINARY WITH OTSU as well)
ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# noise removal
# morphological operator
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# grab background that you are sure of 
sure_bg=cv2.dilate(opening,kernel,iterations=3)
# display(sure_bg,cmap='gray')
# find sure foreground
dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret,sure_fg=cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# display(dist_transform,cmap='gray')
# display(sure_fg,cmap='gray')
# find unknown region
sure_fg=np.uint8(sure_fg)
unknown=cv2.subtract(sure_bg,sure_fg)
# LEVEL MARKERS FOR SURE BACKGROUND
ret,markers=cv2.connectedComponents(sure_fg)
markers=markers+1
markers[unknown==255]=0
# display(markers,cmap='gray')

# apply watershed algorithms to find marekrs
markers=cv2.watershed(img,markers)
# display(markers)

# find contours on markers
contours,hierarchy=cv2.findContours(markers.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3]==-1:
        cv2.drawContours(sep_coins,contours,i,(255,0,0),10)
display(sep_coins)
# print(sure_fg)

