import cv2
import numpy as np
import matplotlib.pyplot as plt
full=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/sammy.jpg")
full=cv2.cvtColor(full,cv2.COLOR_BGR2RGB)
face=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/sammy_face.jpg")
face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
height,width,channels=face.shape
for m in methods:
    full_copy=full.copy()
    method=eval(m)
    res=cv2.matchTemplate(full_copy,face,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc
    else:
        top_left=max_loc
    
    bot_right=(top_left[0]+width,top_left[0]+height)

    cv2.rectangle(full_copy,top_left,bot_right,(0,0,255),thickness=3)

    plt.subplot(121)
    plt.imshow(res)
    plt.title("Result of template matching")

    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title("detected point")
    plt.suptitle(m)

    plt.show()
    print("\n")
    print("\n")
