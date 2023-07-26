import cv2
import numpy as np
import os

board = np.zeros((500,500,3),dtype = "uint8")
cv2.imshow("BOARD",board)

# BGR color-code

# RED
board[:] = 0,0,255
cv2.imshow("RED",board)

# GREEN
board[:] = 0,255,0
cv2.imshow("GREEN",board)

# BLUE
board[:] = 255,0,0
cv2.imshow("BLUE",board)

# WHITE
board[:] = 255,255,255
cv2.imshow("WHITE",board)

cv2.waitKey(0)
