import cv2
import numpy as np

blank = np.zeros((400,400),dtype = "uint8")

reactangle = cv2.rectangle(blank.copy(),(30,30),(370,370),(255,255,255),-1)
circle = cv2.circle(blank.copy(),(200,200),200,(255,255,255),-1)

cv2.imshow("Rectangle",reactangle)
cv2.imshow("Circle",circle)

OR = cv2.bitwise_or(reactangle,circle)
cv2.imshow("OR",OR)

AND = cv2.bitwise_and(reactangle,circle)
cv2.imshow("AND",AND)

XOR = cv2.bitwise_xor(reactangle,circle)
cv2.imshow("XOR",XOR)

NOT = cv2.bitwise_not(reactangle,circle)
cv2.imshow("NOT",NOT)

cv2.waitKey(0)
