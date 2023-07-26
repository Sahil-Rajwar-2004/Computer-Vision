import cv2
import numpy as np

board = np.zeros((500,500,3),dtype = "uint8")
# cv2.imshow("BLANK",board)

cv2.rectangle(board,(0,0),(board.shape[1]//2,board.shape[0]//2),(0,255,0),thickness = -1)
cv2.circle(board,(board.shape[1]//2,board.shape[0]//2),50,(128,128,128),thickness = 2)
cv2.line(board,(321,123),(101,203),(255,255,255),thickness = 2)
cv2.putText(board,"Hello",(225,225),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,165,255),thickness = 2)

cv2.imshow("BOARD",board)

cv2.waitKey(0)
