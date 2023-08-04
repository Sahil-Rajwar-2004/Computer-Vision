import os
from tkinter import filedialog
import cv2
import numpy as np

"""
    RED:
        Lower: [0, 100, 100]
        Upper: [10, 255, 255]

        Lower: [160, 100, 100]
        Upper: [180, 255, 255]

    Green:
        Lower: [40, 40, 40]
        Upper: [80, 255, 255]

    Blue:
        Lower: [100, 50, 50]
        Upper: [130, 255, 255]

    Yellow:
        Lower: [20, 100, 100]
        Upper: [40, 255, 255]

    Orange:
        Lower: [10, 100, 100]
        Upper: [25, 255, 255]

    Purple:
        Lower: [130, 40, 40]
        Upper: [170, 255, 255]

    Pink:
        Lower: [150, 40, 40]
        Upper: [170, 255, 255]
"""

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fulllPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("MP4","*.mp4"),("AVI","*avi")))

def colorDetection(frame,lowerBound,upperBound):
    hsvFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvFrame,lowerBound,upperBound)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    return result

lowerBound = np.array([40,40,40])
upperBound = np.array([80,255,255])

vid = cv2.VideoCapture(fulllPATH)
vid.set(cv2.CAP_PROP_FPS,60)
running = True

while running:
    ret,frame = vid.read()
    if not ret:
        running = False
    
    detectedColor = colorDetection(frame,lowerBound,upperBound)
    cv2.imshow("Orginal",frame)
    cv2.imshow("Detected Color",detectedColor)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        running = False

vid.release()
cv2.destroyAllWindows()
