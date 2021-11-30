import cv2
import numpy as np
import matplotlib .pyplot as plt

# flat_chess=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/flat_chessboard.png")
# flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
# found,corners=cv2.findChessboardCorners(flat_chess,(7,7))
# if found:
#     print("opencv was able to find the corners")
# else:
#     print("opencv was not able to find the corners double check your patternsize")
# flat_chess_copy=flat_chess.copy()
# cv2.drawChessboardCorners(flat_chess_copy,(7,7),corners,found)
# plt.imshow(flat_chess_copy)
# plt.show()

dots=cv2.imread("/home/sachin269/Desktop/Computer-Vision-with-Python (2)/Computer-Vision-with-Python/DATA/dot_grid.png")
found,corners=cv2.findCirclesGrid(dots,(10,10),cv2.CALIB_CB_ASYMMETRIC_GRID)
if found:
    print("opencv was able to detect circle grids")
else:
    print("opencv was not able to detect circle grids please check the patternsize")
dots_copy=dots.copy()
cv2.drawChessboardCorners(dots_copy,(10,10),corners,found)
plt.imshow(dots_copy)
plt.show()