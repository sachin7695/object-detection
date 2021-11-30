import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import median
img=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/sammy_face.jpg")
# choosing thresholds
blurred_img=cv2.blur(img,ksize=(5,5))
med_val=np.median(img)
lower=int(max(0,0.07*med_val))
upper=int(min(255,1.3*med_val))
edges=cv2.Canny(image=blurred_img,threshold1=lower,threshold2=upper)
plt.imshow(edges)
plt.show()