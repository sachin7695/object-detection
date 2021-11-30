import cv2
import numpy as np
import matplotlib.pyplot as plt
flat_chess=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/flat_chessboard.png")
flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
gray_flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
real_chess=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/real_chessboard.jpg")
real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
gray_real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)

# gray=np.float32(gray_flat_chess)
# dst=cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
# dst=cv2.dilate(dst,None)
# flat_chess[dst>0.01*dst.max()]=[255,0,0]

# plt.imshow(flat_chess)
# plt.show()

# gray=np.float32(gray_real_chess)

# dst=cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
# dst=cv2.dilate(dst,None)

# real_chess[dst>0.01*dst.max()]=[255,0,0]

# plt.imshow(real_chess)
# plt.show()

corners=cv2.goodFeaturesToTrack(gray_real_chess,100,0.01,10)
corners=np.int0(corners)
for i in corners:
    x,y=i.ravel()
    cv2.circle(real_chess,(x,y),3,255,-1)
plt.imshow(real_chess)
plt.show()
print(corners)