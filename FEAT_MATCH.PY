import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img,cmap='gray'):
    fig=plt.figure(figsize=(10,10))
    ax=fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

reeses=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/reeses_puffs.png",0)

cereals=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/many_cereals.jpg",0)


# Brute Force Detection with ORB Descriptors

orb=cv2.ORB_create()

kp1,des1=orb.detectAndCompute(reeses,None)
kp2,des2=orb.detectAndCompute(cereals,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches=bf.match(des1,des2)

matches=sorted(matches,key=lambda x:x.distance)

reeses_matches=cv2.drawMatches(reeses,kp1,cereals,kp2,matches[:25],None,flags=2)

# display(reeses_matches)

sift=cv2.xfeatures2d.SIFT_create()
kp3,des3=sift.detectAndCompute(reeses,None)
kp4,des4=sift.detectAndCompute(cereals,None)
# bf1=cv2.BFMatcher()
# FLANN parameters
FLANN_INDEX_KDTREE=0
index_params=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_params=dict(checks=50)
# matches1=bf1.knnMatch(des3,des4,k=2)
flann=cv2.FlannBasedMatcher(index_params,search_params)
matches1=flann.knnMatch(des3,des4,k=2)
# good=[]
matchesMask=[[0,0] for i in range (len(matches1))]
# ?ratio test
for i,(match1,match2) in enumerate(matches1):
    if match1.distance < 0.7*match2.distance:
        # good.append([match1])
        matchesMask[i]=[1,0]

# sift_matches=cv2.drawMatchesKnn(reeses,kp3,cereals,kp4,good,None,flags=2)
draw_params=dict(matchColor=(0,255,0),singlePointColor=(0,0,255),matchesMask=matchesMask,flags=0)
flann_matches=cv2.drawMatchesKnn(reeses,kp3,cereals,kp4,matches1,None,**draw_params)
display(flann_matches)
# print(len(good))
# print(len(matches1))

# FLANN-FIRST LIBRARY FOR APPROXIMATE LAST NEAREST NEIGHBORS

