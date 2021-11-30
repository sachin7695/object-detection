import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/internal_external.png", 0)
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

external_contour = np.zeros(img.shape)

for i in range(len(contours)):

    if hierarchy[0][i][3] == 0:
        cv2.drawContours(external_contour, contours, i, 255, -1)


plt.imshow(external_contour, cmap='gray')
plt.show()

# /home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/internal_external.png

